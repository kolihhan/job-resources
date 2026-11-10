#!/usr/bin/env python3
"""Private, fail-closed exact-Issue duplicate ACK for source Pending queues.

This is applicant-history reconciliation, never public source batching or an
application decision. It requires all-state live GitHub Issue readback and
exact primary role URL + employer + role title, never weak company-only hints.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import os

from build_known_role_index import _norm_text, _weak_company_title, _urls_from_issue, fetch_all_issues
from platform_index_queue import canonical, validate_state, atomic_write

ISSUE_URL = "https://github.com/kolihhan/job-resources/issues/"


def compact(value):
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", str(value or "").casefold())


def issue_role_match(row, issue, market):
    """Exact first-party role identity, not a similar title or a sibling req."""
    if issue.get("pull_request") or not isinstance(issue.get("number"),int):
        return False
    title=issue.get("title") or ""
    role=compact(row.get("title"))
    company=compact(row.get("company"))
    if len(role)<12 or len(company)<3:
        return False
    compact_title=compact(title)
    if role not in compact_title or company not in compact_title:
        return False
    expected=canonical(row.get("url"),market)
    if not expected:
        return False
    return expected in {
        canonical(u,market)
        for u in _urls_from_issue(issue)
        if canonical(u,market)
    }


def possible_cross_platform_issues(row, issues, market):
    """A discovery hint ONLY: same named role and plausible employer, different URL.

    Never terminal-ACK on text: different regional requisitions can have
    identical titles (Binance Pioneer is a real example). Require explicit
    market in Issue title and unique match to avoid noise; still manual review.
    """
    role = compact(row.get("title"))
    company = compact(row.get("company"))
    if len(role) < 12 or len(company) < 5:
        return []
    options = []
    for issue in issues:
        title = str(issue.get("title") or "")
        if issue.get("pull_request") or not isinstance(issue.get("number"), int):
            continue
        if not re.search(r"\\[" + re.escape(market) + r"(?:-[A-Z]+)?\\]", title, re.I):
            continue
        weak = _weak_company_title(title)
        if not weak:
            continue
        past_company, past_role = weak.split("|", 1)
        lhs, rhs = compact(past_company), compact(past_role)
        if (len(lhs) < 5 or len(rhs) < 12 or
                not (company == lhs or company.startswith(lhs) or lhs.startswith(company))):
            continue
        if role == rhs:
            options.append(issue["number"])
    return sorted(set(options))


def reconcile(state, issues, *, checked_at=None):
    market=state["market"]
    validate_state(state,market)
    now=checked_at or datetime.now(timezone.utc).isoformat()
    report={"market":market,"pending_before":len(state["pending"]),"verified_duplicates":0,
            "ambiguous":0,"unmatched":0,"possible_cross_platform":0,
            "history_hints_added":0,"hint_examples":[],"examples":[]}
    refs=defaultdict(list)
    for issue in issues:
        if issue.get("pull_request") or not isinstance(issue.get("number"),int):
            continue
        for url in _urls_from_issue(issue):
            can=canonical(url,market)
            if can:refs[can].append(issue)
    keep=[]
    for row in state["pending"]:
        url=canonical(row.get("url"),market)
        options={i["number"]:i for i in refs.get(url,[]) if issue_role_match(row,i,market)}
        if not options:
            # Preserve source Pending: never infer exact duplicate from names.
            # A bounded private hint saves repetitive Gmail/Issue searches for
            # the Scout, without claiming an application was already submitted.
            names = possible_cross_platform_issues(row, issues, market)
            if len(names) == 1:
                report["possible_cross_platform"] += 1
                issue_num = names[0]
                review = row.get("consumer_review") or {}
                if review.get("possible_prior_issue") != issue_num:
                    row["consumer_review"] = {
                        **review, "possible_prior_issue": issue_num,
                        "history_hint": "Same title/likely employer in prior GitHub Issue; "
                                        "different URL. CHECK exact requisition, location, "
                                        "work contents and Gmail before any ACK/APPLY.",
                    }
                    report["history_hints_added"] += 1
                if len(report["hint_examples"]) < 8:
                    report["hint_examples"].append({
                        "source_key": row["key"], "prior_issue": issue_num})
            keep.append(row)
            report["unmatched"] += 1
            continue
        if len(options)!=1:
            keep.append(row)
            report["ambiguous"]+=1
            continue
        issue=next(iter(options.values()))
        record={
            **row, "state":"DUPLICATE_CONFIRMED",
            "issue_url":ISSUE_URL+str(issue["number"]),
            "evidence_url":str(row["url"]),
            "reason":f"Exact role URL + employer + title independently matched current GitHub Issue #{issue['number']}. No reapply.",
            "checked_at":now,
        }
        state["terminal"].append(record)
        report["verified_duplicates"]+=1
        if len(report["examples"])<8:
            report["examples"].append({"source_key":row["key"],"issue":issue["number"]})
    state["pending"]=keep
    state["next_unacknowledged_seq"]=min((x["seq"] for x in keep),default=state["next_seq"])
    validate_state(state,market)
    report["pending_after"]=len(keep)
    return report


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo",type=Path,default=Path("."))
    p.add_argument("--report",type=Path,required=True)
    p.add_argument("--repository",default="kolihhan/job-resources")
    a=p.parse_args()
    token=os.environ.get("GITHUB_TOKEN","")
    if not token:raise SystemExit("GITHUB_TOKEN required")
    issues=fetch_all_issues(a.repository,token)
    if not issues:raise RuntimeError("empty live Issue history; stop without mutation")
    report={"mode":"PRIVATE_EXACT_ISSUE_DEDUPE_NOT_SOURCE_OR_APPLY",
            "issues_read":len(issues),"markets":{}}
    for market in ("SG","MY","CN"):
        path=a.repo/"discovery-state"/f"platform-index-{market.lower()}.json"
        state=json.loads(path.read_text())
        summary=reconcile(state,issues)
        report["markets"][market]=summary
        if summary["verified_duplicates"] or summary["history_hints_added"]:
            atomic_write(path,state)
        print(market,summary["verified_duplicates"],"verified source duplicates ACKed,",
              summary["history_hints_added"],"private cross-platform review hints")
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf8")


if __name__=="__main__":
    main()
