#!/usr/bin/env python3
"""Conservative SG research queue consumer. GitHub Issues remain sole opportunity state.

Only exact employer-controlled closure or exact GitHub Issue readback can settle
a candidate automatically. Other first-party JDs are *triaged*, not promoted
to APPLY by a heuristic. Unavailable endpoints remain pending.

Usage: python scripts/consume_platform_queue.py --state discovery-state/platform-index-sg.json --output artifacts/consumer.json
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from html import unescape
import json
import os
from pathlib import Path
import re
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from platform_index_queue import ack, atomic_write, canonical, utcnow, validate_state, verify_issue_readback

HOST = "ntu.wd3.myworkdayjobs.com"
CXS = "https://ntu.wd3.myworkdayjobs.com/wday/cxs/ntu/careers"
RE_ID = re.compile(r"_(R\d{8})(?:-\d+)?$")
SIGNALS = {
    "llm": re.compile(r"\bLLMs?\b|large language model|generative language model", re.I),
    "rag": re.compile(r"\bRAG\b|retrieval.augmented|retrieval systems", re.I),
    "agent": re.compile(r"\bagents?\b|agentic|tool.calling|multi.agent", re.I),
    "evaluation": re.compile(r"evaluat|benchmark|reliability|guardrails?|red.team", re.I),
    "nlp": re.compile(r"\bNLP\b|natural language processing|dialogue|language understand", re.I),
    "knowledge": re.compile(r"knowledge graph|knowledge base|knowledge retrieval", re.I),
}
REVIEW_FLAGS = {
    "possible_phd_requirement": re.compile(r"(?:Ph\.?D\.?|doctoral)\s*(?:degree|qualification|holder|required)", re.I),
    "experience_years_mentioned": re.compile(r"\b(?:at least|minimum(?: of)?|require[sd]?)\s*\d+\+?\s*years?\b", re.I),
    "fixed_term_mentioned": re.compile(r"\b(?:contract|fixed.term|temporary|short.term)\b", re.I),
    "security_specialism": re.compile(r"penetration test|red.team|prompt injection|cybersecurity|security audit", re.I),
    "domain_specific": re.compile(r"aviation|medical imaging|robotics|earth observation|insurance", re.I),
}
STALE_AFTER = timedelta(hours=48)
MAX_ISSUE_PAGES = 30


def http_json(url: str, token: str = "", data: dict | None = None) -> dict | list:
    raw = json.dumps(data).encode("utf-8") if data is not None else None
    headers = {"User-Agent": "job-resources-conservative-consumer/1.0",
               "Accept": "application/vnd.github+json" if "api.github.com" in url else "application/json"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = "Bearer " + token
        if "api.github.com" in url:
            headers["X-GitHub-Api-Version"] = "2022-11-28"
    req = Request(url, data=raw, headers=headers)
    with urlopen(req, timeout=18) as response:
        payload = response.read(3_000_001)
        if len(payload) > 3_000_000:
            raise ValueError("response oversized")
    return json.loads(payload.decode("utf-8"))


def full_issue_history(token: str, get=http_json) -> list[dict]:
    if not token:
        raise ValueError("GITHUB_TOKEN is required; cannot conclude negative dedupe otherwise")
    found = []
    for page in range(1, MAX_ISSUE_PAGES + 1):
        url = f"https://api.github.com/repos/kolihhan/job-resources/issues?state=all&per_page=100&page={page}"
        values = get(url, token)
        if not isinstance(values, list):
            raise ValueError("GitHub Issues returned non-list; do not assume absence of duplicates")
        found.extend(x for x in values if isinstance(x, dict) and "pull_request" not in x)
        if len(values) < 100:
            return found
    raise RuntimeError("GitHub Issue history exceeded safety page cap; dedupe not proven")


def exact_req_from_nturoute(row: dict) -> str | None:
    url = row.get("url", "")
    p = urlparse(url)
    if p.scheme != "https" or p.hostname != HOST or not p.path.startswith("/Careers/job/"):
        return None
    m = RE_ID.search(p.path)
    return m.group(1) if m else None


def issue_for_req(req_id: str, history: list[dict]) -> dict | None:
    """Matching Issue must name exact Req in its *title*, not sibling refs in body."""
    matches = []
    pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(req_id) + r"(?![A-Za-z0-9])", re.I)
    for issue in history:
        if pat.search(str(issue.get("title", ""))):
            matches.append(issue)
    if len(matches) > 1:
        raise ValueError(f"ambiguous exact requisition: {req_id}, {len(matches)} Issue titles")
    return matches[0] if matches else None


def firstparty_detail(row: dict, get=http_json) -> dict:
    req_id = exact_req_from_nturoute(row)
    if not req_id:
        raise ValueError("not a verified NTU first-party job URL")
    u = urlparse(row["url"])
    suffix = u.path.split("/job/", 1)[1]
    payload = get(CXS + "/job/" + suffix, "")
    if not isinstance(payload, dict) or not isinstance(payload.get("jobPostingInfo"), dict):
        raise ValueError("official Workday response missing jobPostingInfo")
    info = payload["jobPostingInfo"]
    if info.get("jobReqId") != req_id:
        raise ValueError("official Workday jobReqId mismatch")
    return info


def clean_jd(html: str) -> str:
    text = unescape(re.sub(r"<[^>]*>", " ", html or ""))
    return re.sub(r"\s+", " ", text).strip()


def review_summary(info: dict, now_iso: str) -> dict:
    jd = clean_jd(str(info.get("jobDescription") or ""))
    signals = [k for k, pat in SIGNALS.items() if pat.search(jd)]
    flags = [k for k, pat in REVIEW_FLAGS.items() if pat.search(jd)]
    return {"stage": "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW",
            "checked_at": now_iso,
            "source_kind": "NTU Workday first party",
            "source_verified_can_apply": True,
            "req_id": info.get("jobReqId"),
            "jd_sha256": sha256(jd.encode("utf-8")).hexdigest(),
            "jd_chars": len(jd),
            "signals": signals,
            "review_flags": flags,
            "job_description_excerpt": jd[:250],
            "employment_time_type": info.get("timeType"),
            "note": "Technical signals do not prove skill fit, sponsorship, contract quality, or APPLY eligibility."}


def due(row: dict, now: datetime) -> bool:
    review = row.get("consumer_review")
    if not review:
        return True
    checked = review.get("checked_at")
    if not checked:
        return True
    try:
        ts = datetime.fromisoformat(checked.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return True
    return now - ts >= STALE_AFTER


def run_consumer(state: dict, history: list[dict], *, get=http_json,
                 confirm_issue=None, now: datetime | None = None, limit=12,
                 sleep=False) -> tuple[dict, dict]:
    validate_state(state, state["market"])
    if state["market"] != "SG":
        raise ValueError("Only SG verified for this official-source consumer")
    now = now or datetime.now(timezone.utc)
    now_iso = now.isoformat().replace("+00:00", "Z")
    # One full history is mandatory before any candidate can be classified.
    if not isinstance(history, list) or not history:
        raise ValueError("Full GitHub Issue history is required")
    if confirm_issue is None:
        raise ValueError("Issue verification function required")

    report = {"observed_at": now_iso, "market": "SG",
              "considered": 0, "issue_ack": 0, "closed_by_employer": 0,
              "firstparty_jds_verified": 0, "needs_canonical_route": 0,
              "errors": 0, "outcomes": []}
    candidates = sorted((r for r in state["pending"] if due(r, now)),
                        key=lambda r: (bool(r.get("consumer_review")), r["seq"]))
    for row in candidates[:limit]:
        key = row["key"]
        report["considered"] += 1
        result = {"seq": row["seq"], "key": key, "title": row["title"],
                  "company": row.get("company"), "source": row.get("source")}
        try:
            req_id = exact_req_from_nturoute(row)
            if req_id is None:
                # Search-index / aggregator item: no employer-controlled JD yet.
                row["consumer_review"] = {"stage": "NEEDS_EMPLOYER_CANONICAL_ROUTE",
                    "checked_at": now_iso,
                    "note": "A third-party source URL cannot prove exact employer requisition or open status."}
                result["stage"] = "NEEDS_EMPLOYER_CANONICAL_ROUTE"
                report["needs_canonical_route"] += 1
            else:
                old = issue_for_req(req_id, history)
                if old is not None:
                    issue_num = old.get("number")
                    issue_url = f"https://github.com/kolihhan/job-resources/issues/{issue_num}"
                    if not isinstance(issue_num, int) or issue_num <= 0:
                        raise ValueError("invalid exact GitHub issue number")
                    if confirm_issue(issue_url, row["url"]) is not True:
                        raise ValueError("live exact Issue readback not proven")
                    title = str(old.get("title") or "")
                    action = ("ISSUE_VERIFIED" if title.startswith(("[APPLY]", "[CHECK]"))
                              else "DUPLICATE_CONFIRMED")
                    ack(state, {"key": key, "action": action, "issue_url": issue_url,
                                "evidence_url": issue_url}, issue_proven=True)
                    result.update(stage=action, issue=issue_url)
                    report["issue_ack"] += 1
                else:
                    info = firstparty_detail(row, get)
                    jd = clean_jd(str(info.get("jobDescription") or ""))
                    if info.get("canApply") is False:
                        ack(state, {"key": key, "action": "HARD_REJECTED",
                                    "evidence_url": row["url"],
                                    "reason": ("Employer official Workday exact requisition "
                                               + req_id + " returned canApply=false on "
                                               + now_iso[:10] + ".")})
                        result["stage"] = "EMPLOYER_NOT_ACCEPTING"
                        report["closed_by_employer"] += 1
                    elif info.get("canApply") is True and jd:
                        row["consumer_review"] = review_summary(info, now_iso)
                        result.update(stage="FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW",
                                      signals=row["consumer_review"]["signals"],
                                      review_flags=row["consumer_review"]["review_flags"])
                        report["firstparty_jds_verified"] += 1
                    else:
                        row["consumer_review"] = {"stage": "UNVERIFIED_APPLY_OR_JD",
                            "checked_at": now_iso,
                            "note": "Exact requisition matched but canApply or full JD is unavailable."}
                        result["stage"] = "UNVERIFIED_APPLY_OR_JD"
        except Exception as exc:
            # No guessed/irreversible closing if API incomplete or conflicting.
            row["consumer_review"] = {
                "stage": "FETCH_OR_IDENTITY_RETRY", "checked_at": now_iso,
                "error": type(exc).__name__ + ": " + str(exc)[:180]}
            result["stage"] = "FETCH_OR_IDENTITY_RETRY"
            report["errors"] += 1
        report["outcomes"].append(result)
        if sleep:
            time.sleep(0.25)
    state["next_unacknowledged_seq"] = min(
        (r["seq"] for r in state["pending"]), default=state["next_seq"])
    validate_state(state, state["market"])
    report["pending_after"] = len(state["pending"])
    report["terminal_after"] = len(state["terminal"])
    report["cursor_after"] = state["next_unacknowledged_seq"]
    report["review_ready_total"] = sum(
        r.get("consumer_review", {}).get("stage") == "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW"
        for r in state["pending"])
    report["untouched_pending_total"] = sum(
        not r.get("consumer_review") for r in state["pending"])
    return state, report


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--limit", type=int, default=12)
    args = ap.parse_args()
    if args.limit < 1 or args.limit > 50:
        raise SystemExit("limit must be between 1 and 50")
    token = os.environ.get("GITHUB_TOKEN", "")
    issues = full_issue_history(token)
    state = json.loads(args.state.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    state, report = run_consumer(
        state, issues,
        confirm_issue=lambda issue_url, role_url: verify_issue_readback(issue_url, role_url, token),
        now=now, limit=args.limit, sleep=True)
    atomic_write(args.state, state)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "outcomes"},
                     ensure_ascii=False), flush=True)
    for item in report["outcomes"]:
        print("CONSUMED " + json.dumps(item, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
