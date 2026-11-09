#!/usr/bin/env python3
"""Source-diverse, read-only candidate review dispatch for SG/MY/CN x ENG/RES.

This is a disposable *work order*, never a candidate database or automated
eligibility verdict. Official consumer queues and upstream public employer ATS
feed are sources; GitHub Issues alone remain canonical application state.

A title is only a routing hint. Every exact job still requires full employer JD,
hard-eligibility, work rights, current route, all-Issue and Gmail dedupe before
a Scout may create APPLY or CHECK. No external contact or user application.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlsplit, urlunsplit

MARKETS = ("SG", "MY", "CN")
TRACKS = ("ENG", "RES")
RESEARCH = re.compile(
    r"\b(?:research (?:assistant|associate|engineer|officer|scientist|fellow|analyst)"
    r"|applied scientist|research scientist|ai researcher|nlp researcher)\b"
    r"|研究助理|研究工程师|研究员|助理研究员|科研助理", re.I)
MATURE = re.compile(
    r"\b(?:senior|staff|principal|lead|head|director|manager|chief)\b"
    r"|资深|高级专家|架构师|负责人|总监", re.I)
CORE = re.compile(
    r"\b(?:LLM|RAG|NLP|GenAI|agentic|agents?|AI|ML|applied scientist|"
    r"machine learning|research|retrieval|language model|evaluation|"
    r"coding agent|backend|software engineer)\b"
    r"|大模型|人工智能|智能体|检索|算法|研究", re.I)
VALID_ATS_HOSTS = frozenset(
    ("jobs.ashbyhq.com", "jobs.lever.co", "jobs.smartrecruiters.com"))
MAX_OFFICIAL_JD_AGE = timedelta(hours=48)


def now_utc():
    return datetime.now(timezone.utc)


def parse_date(value):
    if not isinstance(value, str):
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt if dt.tzinfo else None
    except ValueError:
        return None


def normalized_url(url):
    """Exact URL for strong history exclusion; no fuzzy company/title merges."""
    if not isinstance(url, str):
        return None
    p = urlsplit(url)
    if p.scheme != "https" or not p.hostname or p.username or p.password:
        return None
    path = p.path.rstrip("/") or "/"
    # Do not remove meaningful job ID path components; query strings may be
    # identity-bearing on other sites, so this helper is used only for ATS.
    return urlunsplit(("https", p.netloc.lower(), path, "", ""))


def allowed_ats_url(url):
    if not isinstance(url, str):
        return False
    p = urlsplit(url)
    host = (p.hostname or "").lower()
    allowed = (host in VALID_ATS_HOSTS or
               host in ("job-boards.greenhouse.io", "job-boards.eu.greenhouse.io") or
               host.endswith(".myworkdayjobs.com"))
    return bool(p.scheme == "https" and allowed and not p.username
                and not p.password and p.path.count("/") >= 2)


def classify_track(title):
    """Routing ONLY: research and engineering are equal GOLD paths."""
    return "RES" if RESEARCH.search(str(title or "")) else "ENG"


def normalized_company(value):
    """Use the same conservative company normalization as known-role-index."""
    text = unicodedata.normalize("NFKC", str(value or "")).lower().strip()
    return " ".join(re.sub(r"[^\w\u4e00-\u9fff]+", " ", text).split())


def official_status(review, now):
    if review.get("stage") != "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW":
        return None
    if review.get("full_jd_complete") is not True or not review.get("full_jd_text"):
        return "JD_INCOMPLETE_FETCH_DUE"
    checked = parse_date(review.get("checked_at"))
    if checked is None or now - checked > MAX_OFFICIAL_JD_AGE:
        return "JD_STALE_REVERIFY_DUE"
    return "JD_VERIFIED_FIT_REVIEW_DUE"


def _candidate_official(row, market, now):
    if not isinstance(row, dict):
        return None
    rev = row.get("consumer_review") or {}
    stage = rev.get("stage")
    verified = stage == "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW"
    # The previously built dispatcher silently ignored the durable
    # UNVERIFIED_INDEX queue: newly discovered API jobs were never reviewed.
    if not verified and row.get("state") != "UNVERIFIED_INDEX":
        return None
    url = normalized_url(row.get("url"))
    if not url or not row.get("title") or not isinstance(row.get("seq"), int):
        return None
    track = classify_track(row["title"])
    status = (official_status(rev, now) if verified else
              "UNVERIFIED_INDEX_NEEDS_EXACT_EMPLOYER_JD_AND_FIT")
    return {
        "market": market, "track_hint": track, "title": row["title"],
        "company": str(row.get("company") or "UNKNOWN"), "url": url,
        "origin": "official_queue" if verified else "durable_queue",
        "source": row.get("source"),
        "queue_seq": row["seq"], "queue_key": row.get("key"),
        "status": status, "title_maturity_flag": bool(MATURE.search(row["title"])),
        "review_flags": rev.get("review_flags", []),
        "signal_tags": rev.get("signals", []),
        "full_jd_complete": bool(rev.get("full_jd_complete")),
        "jd_sha256": rev.get("jd_sha256"),
        "source_checked_at": rev.get("checked_at"),
        "where_to_review": f"discovery-state/platform-index-{market.lower()}.json",
        "decision": "NOT_MADE",
    }


def _candidate_ats(row, market):
    if not isinstance(row, dict):
        return None
    if row.get("market") != market or not row.get("job_id") or not row.get("key"):
        return None
    url = normalized_url(row.get("url"))
    if not url or not allowed_ats_url(url) or not row.get("title") or not row.get("company"):
        return None
    evidence = row.get("evidence")
    if evidence not in ("full_jd", "partial_jd", "listing_only"):
        return None
    track = classify_track(row["title"])
    status = ("NEEDS_LIVE_OFFICIAL_JD_AND_FIT" if evidence == "full_jd" else
              "NEEDS_FULL_JD_AND_LIVE_ROUTE")
    return {
        "market": market, "track_hint": track, "title": str(row["title"])[:180],
        "company": str(row["company"])[:150], "url": url,
        "origin": "ats_feed", "source": row.get("ats"), "ats_key": row["key"],
        "source_job_id": row["job_id"], "status": status,
        "title_maturity_flag": bool(MATURE.search(str(row["title"]))),
        "review_flags": ["title_maturity_not_hard_reject"] if MATURE.search(str(row["title"])) else [],
        "signal_tags": [],
        "feed_jd_evidence": evidence,
        "feed_lane": row.get("lane"),
        "full_jd_complete": False,  # upstream full_jd ≠ fresh liveness/eligibility
        "where_to_review": "kolihhan/freehirefetch/feed/ats/jd/index.json + exact ATS job page",
        "decision": "NOT_MADE",
    }


def _sort_priority(role):
    # Source provenance, not title marketing, comes first. Mature titles are
    # only deprioritized, NEVER treated as conclusive hard ineligibility.
    origin = 0 if role["origin"] == "official_queue" else 1
    maturity = bool(role["title_maturity_flag"])
    secondary = role.get("feed_lane") == "MY_SWE_SECONDARY"
    evidence = {"full_jd": 0, "partial_jd": 1, "listing_only": 2}
    jd_rank = evidence.get(role.get("feed_jd_evidence"), 0)
    title_weak = not bool(CORE.search(role["title"]))
    seq = role.get("queue_seq", 999999999)
    return (maturity, secondary, origin, jd_rank, title_weak, seq,
            role["company"].lower(), role["url"])


def _choose_fair(candidates, limit, min_each_track):
    if limit < 1 or min_each_track < 0:
        raise ValueError("invalid dispatch limit / track reserve")
    # A smaller ad-hoc batch still gets the largest feasible equal reserve.
    min_each_track = min(min_each_track, limit // 2)
    rows = sorted(candidates, key=_sort_priority)
    selected = []
    seen = set()
    companies = Counter()

    def take(track, target, company_cap):
        if target <= 0:
            return
        for row in rows:
            if len(selected) >= limit or sum(x["track_hint"] == track for x in selected) >= target:
                break
            if row["url"] in seen or row["track_hint"] != track:
                continue
            if companies[row["company"].lower()] >= company_cap:
                continue
            selected.append(row)
            seen.add(row["url"])
            companies[row["company"].lower()] += 1

    # Equal reserved opportunities; only borrow when a track is exhausted.
    for cap in (2, limit):
        for track in TRACKS:
            take(track, min_each_track, cap)

    # Diverse employers first, then allow an employer to overflow if there is
    # otherwise unused review budget. Never stall the only active source.
    for cap in (2, limit):
        for row in rows:
            if len(selected) >= limit:
                break
            if row["url"] in seen or companies[row["company"].lower()] >= cap:
                continue
            selected.append(row)
            seen.add(row["url"])
            companies[row["company"].lower()] += 1
    return selected


def build_dispatch(states, feeds, known_index, *, now=None,
                   limit_per_market=10, min_each_track=3):
    """Derived review suggestions. No repo/Gmail mutations or fit decisions."""
    now = now or now_utc()
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    known_urls = {
        normalized_url(url) for url in known_index.get("strong", {}).get("urls", [])
        if isinstance(url, str) and normalized_url(url)
    }
    wait_employers = set(known_index.get("weak", {}).get("wait_employers", []))
    result = {
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "mode": "READ_ONLY_SOURCE_DERIVED_REVIEW_DISPATCH_NOT_APPLY",
        "markets": {},
        "limits": {
            "dedupe": "Exact known-role-index URLs are snapshot-only; all live/closed Issue search and two-account Gmail dedupe remain mandatory before promotion.",
            "fit": "Title track is a routing hint, not verified research/engineering ownership or eligibility.",
            "source": "Public ATS snapshots may be stale or incomplete; a feed full_jd is never a fresh official liveness check.",
            "writes": "No Issue changes, source cursor acknowledgements, job applications, or employer contact.",
        },
    }
    for market in MARKETS:
        state = states.get(market)
        feed = feeds.get(market)
        if state is not None and (state.get("market") != market or
                                  not isinstance(state.get("pending"), list)):
            raise ValueError(f"bad authoritative source queue for {market}")
        if feed is not None and (feed.get("market") != market or
                                 not isinstance(feed.get("jobs"), list)):
            raise ValueError(f"bad ATS feed snapshot for {market}")
        by_url = {}
        ready = 0
        current = 0
        pending_rows = state["pending"] if state is not None else []
        for source in pending_rows:
            row = _candidate_official(source, market, now)
            if row is None:
                continue
            ready += int(row["status"] in (
                "JD_VERIFIED_FIT_REVIEW_DUE", "JD_INCOMPLETE_FETCH_DUE",
                "JD_STALE_REVERIFY_DUE"))
            current += int(row["status"] == "JD_VERIFIED_FIT_REVIEW_DUE")
            by_url[row["url"]] = row
        suppressed = 0
        bad = 0
        jobs = feed["jobs"] if feed is not None else []
        companies = set()
        for item in jobs:
            if isinstance(item, dict) and item.get("company"):
                companies.add(str(item["company"]).casefold())
            row = _candidate_ats(item, market)
            if row is None:
                bad += 1
                continue
            if row["url"] in by_url:
                continue  # canonical official queue evidence wins
            if row["url"] in known_urls:
                suppressed += 1
                continue  # advisory snapshot exclusion, not fresh verified dedupe
            by_url[row["url"]] = row
        for role in by_url.values():
            # A new requisition may be a replacement or repost of an already
            # submitted role. This is an advisory history check, NOT a
            # match or suppression: distinct requisitions can be legitimate.
            role["prior_wait_employer_hint"] = (
                normalized_company(role["company"]) in wait_employers
            )
            if role["prior_wait_employer_hint"]:
                role["review_flags"] = list(role.get("review_flags") or []) + [
                    "CHECK_PRIOR_SUBMISSION_HISTORY"
                ]
        selected = _choose_fair(list(by_url.values()), limit_per_market, min_each_track)
        by_track = Counter(x["track_hint"] for x in selected)
        available = Counter(x["track_hint"] for x in by_url.values())
        result["markets"][market] = {
            "official_pending_total": len(pending_rows),
            "verified_waiting_fit": ready,
            "current_full_jd_for_fit": current,
            "official_need_reverify_or_rehydrate": ready-current,
            "ats_snapshot_state": "AVAILABLE" if feed is not None else "UNAVAILABLE",
            "ats_rows_observed": len(jobs) if feed is not None else None,
            "ats_unique_employers_observed": len(companies) if feed is not None else None,
            "suppressed_exact_snapshot_url": suppressed,
            "bad_source_rows": bad,
            "unique_review_candidates": len(by_url),
            "available_by_track_hint": {t: available[t] for t in TRACKS},
            "selected_by_track": {t: by_track[t] for t in TRACKS},
            "prior_wait_employer_hints": sum(
                bool(x["prior_wait_employer_hint"]) for x in selected),
            # A dispatch run performs no substantive fit or hard screening.
            "fit_decisions_made": 0,
            "coverage_gaps": (
                (["NO_ENGINEERING_CANDIDATES_IN_OBSERVED_SOURCES"]
                 if available["ENG"] == 0 else [])
                + (["NO_RESEARCH_CANDIDATES_IN_OBSERVED_SOURCES"]
                   if available["RES"] == 0 else [])
                + (["ATS_FEED_UNAVAILABLE"] if feed is None else [])
                + (["ATS_CANDIDATES_FROM_ONE_EMPLOYER_ONLY"]
                   if feed is not None and len(companies) == 1 else [])
            ),
            "selected": selected,
        }
    return result


def markdown_report(report):
    lines = [
        "# Six-battlefield review dispatch",
        "",
        "Derived public-source review orders, NOT verified APPLY/CHECK vacancies. Neither track is secondary.",
        "No existing opportunity tracker or application state was changed.",
        "",
        "| Market | ATS snapshot | ATS rows | ATS employers | Verified pending JD | Fresh complete pending JD | Select ENG | Select RES |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for market in MARKETS:
        m = report["markets"][market]
        n = lambda v: str(v) if v is not None else "unknown"
        lines.append(
            f"| {market} | {m['ats_snapshot_state']} | {n(m['ats_rows_observed'])} | "
            f"{n(m['ats_unique_employers_observed'])} | {m['verified_waiting_fit']} | "
            f"{m['current_full_jd_for_fit']} | {m['selected_by_track']['ENG']} | "
            f"{m['selected_by_track']['RES']} |"
        )
    lines += ["", "## Source and track coverage debt", ""]
    for market in MARKETS:
        m = report["markets"][market]
        for gap in m["coverage_gaps"]:
            lines.append(f"- **{market}** {gap}. Coverage debt, NOT proof of zero vacancies.")
    lines += ["", "## Exactly what scouts should review", ""]
    for market in MARKETS:
        m = report["markets"][market]
        lines.append(f"### {market}: Engineering and Research (routing hints)")
        if not m["selected"]:
            lines.append("No dispatchable source candidates in these snapshots; coverage unknown.")
        for row in m["selected"]:
            title = row["title"].replace("[", "").replace("]", "").replace("|", "/")
            origin = ("existing queue #" + str(row["queue_seq"])
                      if row["origin"] in ("official_queue", "durable_queue")
                      else "ATS key " + row["ats_key"])
            mature = " — mature title: verify requirements" if row["title_maturity_flag"] else ""
            prior = (" — **PRIOR WAIT AT EMPLOYER: confirm exact submission and sibling/repost history**"
                     if row.get("prior_wait_employer_hint") else "")
            lines.append(
                f"- **{row['track_hint']}** [{title}]({row['url']}) ({row['company']}); "
                f"{origin}; **{row['status']}**{mature}{prior}"
            )
        lines.append("")
    lines += [
        "## Promotion gate",
        "",
        "MANDATORY: before creating a new APPLY/CHECK, reconcile prior WAIT/APPLY/ACTION at the "
        "same employer, including alternate requisitions, reposts and generic acknowledgements. "
        "An exact-ID Gmail miss does not prove that the candidate never applied. "
        "User-confirmed applied means WAIT, not a new APPLY. A company-level WAIT hint never "
        "proves that a distinct requisition is a duplicate.",
        "",
        "Review exact employer JD and current route; verify substantive work, hard qualifications,",
        "employment terms, SG/CN work-pass exclusions, campaign/cohort rules, all-state GitHub Issues,",
        "and both Gmail accounts. Create and read back APPLY/CHECK Issue only after passing each gate.",
        "Then acknowledge the existing source candidate exact key if applicable.",
        "Unknowns/retries require one specific next evidence; title/ATS feed tags are not eligibility.",
        "",
        "## Source limits",
        "",
    ]
    lines += ["- " + text for text in report["limits"].values()]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--ats-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--summary", type=Path, required=True)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--track-reserve", type=int, default=3)
    args = ap.parse_args()
    states = {}
    feeds = {}
    for market in MARKETS:
        queue = args.repo / "discovery-state" / f"platform-index-{market.lower()}.json"
        if queue.exists():
            states[market] = json.loads(queue.read_text(encoding="utf-8"))
        source = args.ats_dir / f"{market}.json"
        if source.exists():
            feeds[market] = json.loads(source.read_text(encoding="utf-8"))
    known_path = args.repo / "discovery-state" / "known-role-index.json"
    known = json.loads(known_path.read_text(encoding="utf-8"))
    report = build_dispatch(states, feeds, known, limit_per_market=args.limit,
                            min_each_track=args.track_reserve)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(markdown_report(report), encoding="utf-8")
    print(json.dumps({"markets": {
        m: {"selected": len(v["selected"]), "by_track": v["selected_by_track"],
            "ats_snapshot": v["ats_snapshot_state"],
            "verified_pending_fit": v["verified_waiting_fit"]}
        for m,v in report["markets"].items()}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
