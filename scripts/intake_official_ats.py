#!/usr/bin/env python3
"""Durably hand off bounded *unverified* official ATS leads to existing queues.

No new opportunity tracker and no automatic APPLY/CHECK/WAIT. The producer is
freehirefetch's first-party employer-board JSON, never its FreeHire aggregator.
GitHub Issues and Gmail remain the only authoritative applicant lifecycle.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re

from build_review_dispatch import classify_track, normalized_company, allowed_ats_url
from platform_index_queue import (MARKETS, atomic_write, canonical, ingest,
                                  known_urls, new_state, validate_state)

MATURE = re.compile(r"\b(?:senior|staff|principal|lead|head|manager|director|architect|intern)\b"
                    r"|资深|高级|实习", re.I)
TECH = re.compile(r"\b(?:AI|LLM|RAG|NLP|GenAI|agent|machine learning|"
                  r"applied scientist|research|data scientist|ML|retrieval|"
                  r"software|backend|platform|algorithm)\b|智能体|算法|大模型|检索|研究", re.I)
ALLOWED_EVIDENCE = {"full_jd", "partial_jd", "listing_only"}
MAX_UNVERIFIED_API_CHARS = 4000
API_PROVENANCE = "UNVERIFIED_THIRD_PARTY_API"
# A product/team named "AI Finance Agent" does not make an iOS/frontend
# developer an agent engineer. These are ordering hints, not hard exclusions.
CORE_TITLE = re.compile(
    r"\b(?:applied ai|generative ai|machine learning|llm|nlp|rag|retrieval|"
    r"ai engineer|ai developer|research engineer|research scientist|"
    r"applied scientist|ai research|ml engineer|agentic|agent systems)\b"
    r"|大模型|机器学习|算法工程师|人工智能工程师", re.I)
UI_TITLE = re.compile(r"\b(?:ios|android|mobile|frontend|front.end)\b", re.I)


def core_title(title):
    return bool(CORE_TITLE.search(str(title or "")))



def priority(row):
    title = row["title"]
    weak = not TECH.search(title)
    is_mature = bool(MATURE.search(title))
    secondary = row.get("lane") == "MY_SWE_SECONDARY"
    ui_only = bool(UI_TITLE.search(title))
    focused = core_title(title)
    evidence_rank = {"full_jd": 0, "partial_jd": 1, "listing_only": 2}
    return (int(is_mature), int(ui_only), int(secondary), int(not focused), int(weak),
            evidence_rank.get(row.get("evidence"), 3),
            {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(row.get("triage_priority"), 3),
            row["company"].lower(), row["url"])


def candidate(row, market):
    if not isinstance(row, dict) or row.get("market") != market:
        return None
    if not all(isinstance(row.get(k), str) and row[k].strip()
               for k in ("company", "title", "url", "key", "job_id")):
        return None
    if row.get("evidence") not in ALLOWED_EVIDENCE:
        return None
    url = canonical(row["url"], market)
    if not url:
        return None
    # Existing canonical() is the sole trust boundary: strict recognized
    # employer ATS/native exact job URLs, never arbitrary aggregator pages.
    return {**row, "url": url}


def unverified_api_context(item):
    """Bounded third-party source context; NEVER a complete employer JD."""
    if (item.get("discovery_access") != "API_PROXY_ONLY"
            or item.get("api_description_provenance") != API_PROVENANCE
            or ":public-api:" not in str(item.get("source") or "")):
        return None
    body = item.get("api_description_text")
    if not isinstance(body, str) or not body.strip() or len(body) > MAX_UNVERIFIED_API_CHARS:
        return None
    return {
        "provenance": API_PROVENANCE,
        "text": body,
        "truncated": item.get("api_description_truncated") is True,
        "employer_verified": False,
    }


def attach_unverified_api_context(state, snapshot, market):
    """Update only exact existing Pending source identities, never terminal/Issue data."""
    pending = {row["url"]: row for row in state["pending"]}
    updated = 0
    for raw in snapshot["jobs"]:
        item = candidate(raw, market)
        if not item:
            continue
        row = pending.get(item["url"])
        context = unverified_api_context(item)
        if (not row or context is None
                or row.get("source") != item.get("source")
                or row.get("ats_key") != item["key"]
                or row.get("source_job_id") != item["job_id"]
                or normalized_company(row.get("company")) != normalized_company(item["company"])
                or str(row.get("title") or "").casefold().strip()
                   != str(item["title"]).casefold().strip()):
            continue
        if row.get("api_source_context") != context:
            row["api_source_context"] = context
            updated += 1
    return updated


def choose(rows, limit, company_cap, existing_pending=()):
    """Fair source sampling with backlog-aware employer caps, not fit judgment."""
    if limit < 1 or company_cap < 1:
        raise ValueError("limit and company_cap must be positive")
    ordered = sorted(rows, key=priority)
    chosen = []
    picked = set()
    per_company = Counter()
    pending_by_company = Counter(normalized_company(x.get("company"))
                                 for x in existing_pending if x.get("company"))
    focused_pending = Counter(normalized_company(x.get("company"))
                              for x in existing_pending
                              if x.get("company") and core_title(x.get("title")))

    def pick(track, until):
        for row in ordered:
            if len(chosen) >= limit or sum(x["_track"] == track for x in chosen) >= until:
                return
            company = normalized_company(row["company"])
            if row["url"] in picked or per_company[company] >= company_cap or row["_track"] != track:
                continue
            # Across cycles, cap ordinary company backlog at company_cap.
            # Reserve up to company_cap MORE for substantive AI/Research titles
            # if older low-quality source candidates already filled the cap.
            if pending_by_company[company] >= company_cap:
                if (not core_title(row["title"]) or
                    focused_pending[company] >= company_cap or
                    pending_by_company[company] >= company_cap * 2):
                    continue
            chosen.append(row)
            picked.add(row["url"])
            per_company[company] += 1
            pending_by_company[company] += 1
            if core_title(row["title"]):
                focused_pending[company] += 1

    # Reserve space for both tracks where each has candidates, then borrow
    # available seats; do not reclassify research as an engineering fallback.
    reserve = min(3, limit // 2)
    for track in ("ENG", "RES"):
        pick(track, reserve)
    for row in ordered:
        if len(chosen) >= limit:
            break
        company = normalized_company(row["company"])
        if row["url"] in picked or per_company[company] >= company_cap:
            continue
        if pending_by_company[company] >= company_cap:
            if (not core_title(row["title"]) or
                focused_pending[company] >= company_cap or
                pending_by_company[company] >= company_cap * 2):
                continue
        chosen.append(row)
        picked.add(row["url"])
        per_company[company] += 1
        pending_by_company[company] += 1
        if core_title(row["title"]):
            focused_pending[company] += 1
    return chosen


def process_market(market, snapshot, state, known, *, limit=12, company_cap=3,
                   max_pending=45):
    validate_state(state, market)
    if snapshot is None:
        return state, {"market": market, "source": "UNAVAILABLE",
                       "observed": None, "selected": 0, "created": 0,
                       "pending_after": len(state["pending"]),
                       "coverage_gaps": ["ATS_SNAPSHOT_MISSING_NOT_ZERO_JOBS"]}

    if snapshot.get("market") != market or not isinstance(snapshot.get("jobs"), list):
        raise ValueError("ATS snapshot contract mismatch: " + market)

    seen = {r["url"] for r in state["pending"]+state["terminal"]}
    known_exact = known_urls(known, market)
    wait_employers = set(known.get("weak", {}).get("wait_employers", []))
    rows, invalid, old, history = {}, 0, 0, 0
    for raw in snapshot["jobs"]:
        item = candidate(raw, market)
        if item is None:
            invalid += 1
            continue
        if item["url"] in seen:
            old += 1
            continue
        if item["url"] in known_exact:
            history += 1
            continue
        # Exact canonical role identity, not vendor source/key text.
        item["_track"] = classify_track(item["title"])
        rows.setdefault(item["url"], item)  # first-party record wins over API repost

    room = max(0, max_pending - len(state["pending"]))
    # Reserve small space for a genuinely independent API source. Otherwise
    # first-party snapshots always take all capacity and the new API is never
    # evaluated against real GitHub/Gmail history by downstream Scouts.
    api_rows = [x for x in rows.values() if ":public-api:" in str(x.get("source",""))]
    selected = []
    if room and api_rows:
        selected = choose(api_rows, min(3, room, limit), company_cap,
                          existing_pending=state["pending"])
    if room > len(selected):
        used = {x["url"] for x in selected}
        taken = Counter(normalized_company(x["company"]) for x in selected)
        remaining = [x for x in rows.values() if x["url"] not in used and
                     taken[normalized_company(x["company"])] < company_cap]
        selected += choose(remaining, min(limit, room)-len(selected), company_cap,
                           existing_pending=state["pending"]+selected) if min(limit,room)>len(selected) else []
    payload = {"source": f"freehirefetch:official-ats:{market}", "items": []}
    for row in selected:
        payload["items"].append({
            "market": market,
            "platform": ("public jobs API (unverified)" if row.get("source")
                         else str(row.get("ats", "ATS")) + " official ATS"),
            "source": row.get("source") or payload["source"],
            "source_listing_url": row.get("source_listing_url") or "",
            "source_platform": row.get("source_platform") or "",
            "discovery_access": row.get("discovery_access") or
                "OFFICIAL_ATS_SOURCE",
            "url": row["url"], "title": row["title"], "company": row["company"],
            "query": row.get("location") or "",
            "ats_key": row["key"], "source_job_id": row["job_id"],
            "source_evidence": row["evidence"],
            "description_excerpt": row.get("description_excerpt") or "",
            "prior_wait_employer_hint": normalized_company(row["company"]) in wait_employers,
        })
    if selected:
        state, stats = ingest(state, known, payload)
        if stats["new_pending"] != len(selected):
            raise ValueError("partial verified intake; expected selected exact IDs")
    else:
        stats = {"new_pending": 0}
    context_updated = attach_unverified_api_context(state, snapshot, market)
    validate_state(state, market)
    return state, {
        "market": market, "source": "AVAILABLE",
        "unverified_api_context_updated": context_updated,
        "observed": len(snapshot["jobs"]), "bad_rows": invalid,
        "already_in_source_queue": old, "known_exact_history": history,
        "unhandled_exact_ids": len(rows), "selected": len(selected),
        "selected_by_track_hint": {
            t: sum(row["_track"] == t for row in selected)
            for t in ("ENG", "RES")},
        "employers_selected": len({normalized_company(row["company"]) for row in selected}),
        "prior_wait_employer_hints": sum(normalized_company(row["company"]) in wait_employers
                                         for row in selected),
        "created": stats["new_pending"], "pending_after": len(state["pending"]),
        "deferred_unhandled_ids": len(rows)-len(selected),
        "source_review_capacity": room,
        "coverage_gaps": (
            (["PENDING_REVIEW_BACKPRESSURE"] if room == 0 and rows else [])
            + (["NO_RESEARCH_ROLES_IN_OBSERVED_SOURCE"] if
               not any(row["_track"] == "RES" for row in rows.values()) else [])
        ),
    }


def run(root, snapshot_dir, known, *, limit=12, company_cap=3,
        max_pending=45, api_dir=None):
    report = {
        "mode": "UNVERIFIED_ATS_SOURCE_QUEUE_ONLY_NO_APPLY",
        "markets": {},
        "limits": [
            "Official ATS listing not proof of current live apply flow or eligible candidate.",
            "Existing Issues/Gmail may contain sibling or generic application receipts.",
            "No ATS snapshot means source unavailable, NEVER an empty market.",
            "Queue entries require full JD, eligibility, route, and readback before APPLY/CHECK.",
        ],
    }
    api_health = {}
    if api_dir and (api_dir / "health.json").is_file():
        api_health = json.loads((api_dir / "health.json").read_text())
    for market in ("SG", "MY", "CN"):
        src = snapshot_dir / (market + ".json")
        snapshot = json.loads(src.read_text()) if src.is_file() else None
        present = ["ATS"] if snapshot is not None else []
        api_problem = False
        if api_dir:
            provider_status = api_health.get(market, {})
            available = any(x.get("status") in ("COMPLETE", "PARTIAL")
                            for x in provider_status.values() if isinstance(x,dict))
            api_path = api_dir / (market + ".json")
            if available and api_path.is_file():
                apis = json.loads(api_path.read_text())
                if apis.get("market")!=market or not isinstance(apis.get("jobs"),list):
                    raise ValueError("API market contract mismatch: "+market)
                snapshot = {"market": market,
                            "jobs": (snapshot["jobs"] if snapshot else []) + apis["jobs"]}
                present.append("API")
            else:
                api_problem = True
        dest = root / "discovery-state" / f"platform-index-{market.lower()}.json"
        state = json.loads(dest.read_text()) if dest.is_file() else new_state(market)
        original = json.dumps(state, sort_keys=True)
        next_state, stats = process_market(
            market, snapshot, state, known, limit=limit, company_cap=company_cap,
            max_pending=max_pending)
        if json.dumps(next_state, sort_keys=True) != original:
            atomic_write(dest, next_state)
        stats["sources_present"] = present
        if api_problem:
            stats["coverage_gaps"].append("API_SOURCE_UNAVAILABLE")
        report["markets"][market] = stats
    return report


def markdown(report):
    lines = [
        "# Official ATS → durable source queue intake (not APPLY)",
        "",
        "| Market | Feed | Rows | Unhandled IDs | New queued | ENG hints | RES hints | Employers | Pending |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for market, d in report["markets"].items():
        val = lambda k: str(d.get(k)) if d.get(k) is not None else "unknown"
        by = d.get("selected_by_track_hint") or {}
        lines.append(f"| {market} | {d['source']} | {val('observed')} | "
                     f"{val('unhandled_exact_ids')} | {d['created']} | "
                     f"{by.get('ENG', 0)} | {by.get('RES', 0)} | "
                     f"{d.get('employers_selected', 0)} | {d['pending_after']} |")
    lines += ["", "## Coverage debt", ""]
    for market, d in report["markets"].items():
        for gap in d.get("coverage_gaps", []):
            lines.append(f"- {market}: {gap}")
    lines += ["", "## Invariants", ""]
    lines += ["- " + x for x in report["limits"]]
    return "\n".join(lines)+"\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", type=Path, default=Path("."))
    p.add_argument("--snapshots", type=Path, required=True)
    p.add_argument("--api-dir", type=Path)
    p.add_argument("--limit", type=int, default=12)
    p.add_argument("--company-cap", type=int, default=3)
    p.add_argument("--max-pending", type=int, default=45)
    p.add_argument("--report", type=Path, required=True)
    args = p.parse_args()
    known = json.loads((args.repo/"discovery-state"/"known-role-index.json").read_text())
    report = run(args.repo, args.snapshots, known, limit=args.limit,
                 company_cap=args.company_cap, max_pending=args.max_pending,
                 api_dir=args.api_dir)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2)+"\n")
    print(markdown(report))
    if all(v["source"] == "UNAVAILABLE" for v in report["markets"].values()):
        raise SystemExit("All first-party ATS sources unavailable; no zero-market claim")


if __name__ == "__main__":
    main()
