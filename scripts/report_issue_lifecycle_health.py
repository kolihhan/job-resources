#!/usr/bin/env python3
"""Audit live GitHub Issue lifecycle without creating a second opportunity tracker.

This is an ephemeral CI health artifact, not evidence of external application
submission or full-market recall.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REPO = "kolihhan/job-resources"
PHASES = ("ACTION", "APPLY", "CHECK", "WAIT")
PREFIX = re.compile(r"^\[(ACTION|APPLY|CHECK|WAIT)\]")
ACTION_WORKFLOW = "owner-application-comment.yml"


def parse_date(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def api_json(path, token):
    if not token:
        raise ValueError("GITHUB_TOKEN is required; no false empty report")
    url = f"https://api.github.com/repos/{REPO}/{path}"
    request = Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "job-resources-lifecycle-health/1.0",
        },
    )
    with urlopen(request, timeout=20) as response:
        raw = response.read(8_000_001)
    if len(raw) > 8_000_000:
        raise ValueError("Issue API response exceeded 8 MB; snapshot incomplete")
    return json.loads(raw.decode("utf-8"))


def fetch_open_issues(token):
    all_issues = []
    for page in range(1, 101):
        params = urlencode({"state": "open", "per_page": 100, "page": page})
        rows = api_json("issues?" + params, token)
        if not isinstance(rows, list):
            raise ValueError("GitHub issues response malformed; snapshot incomplete")
        all_issues.extend(row for row in rows if "pull_request" not in row)
        if len(rows) < 100:
            return all_issues
    raise ValueError("Exceeded 100 issue pages; refusing partial snapshot")


def count_lifecycle(issues, now=None):
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=7)
    counts = Counter()
    recent = Counter()
    mismatches = []
    unknown_prefix = []

    for issue in issues:
        if "pull_request" in issue:
            continue
        title = str(issue.get("title") or "")
        number = issue.get("number")
        match = PREFIX.match(title)
        if not match:
            unknown_prefix.append(number)
            continue
        phase = match.group(1)
        counts[phase] += 1
        created = parse_date(issue.get("created_at"))
        if created is not None and created >= cutoff:
            recent[phase] += 1

        status_labels = [
            label if isinstance(label, str) else label.get("name")
            for label in issue.get("labels") or []
        ]
        status_labels = [label for label in status_labels if
                         isinstance(label, str) and label.startswith("status:")]
        required = "status:" + phase.lower()
        if status_labels != [required]:
            mismatches.append({
                "number": number,
                "expected": required,
                "actual": status_labels,
            })

    return {
        "open_lifecycle_issues": sum(counts.values()),
        "by_status": {phase: counts[phase] for phase in PHASES},
        "currently_open_created_in_last_7d": {
            phase: recent[phase] for phase in PHASES
        },
        "unclassified_open_issue_numbers": unknown_prefix,
        "label_mismatches": mismatches,
        "label_mismatch_count": len(mismatches),
        "interpretation": (
            "Current statuses of OPEN Issues created in the past 7 days. "
            "WAIT is NOT proof of an employer receipt; APPLY is NOT an application sent."
        ),
    }


def measure_event_runs(runs, now=None):
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=7)
    evidence = {}
    for event in ("issues", "issue_comment"):
        selected = [
            r for r in runs
            if r.get("event") == event and
            (parse_date(r.get("created_at")) or datetime.min.replace(
                tzinfo=timezone.utc)) >= cutoff
        ]
        selected.sort(key=lambda r: r.get("created_at") or "", reverse=True)
        evidence[event] = {
            "runs_7d": len(selected),
            "successful_7d": sum(r.get("conclusion") == "success" for r in selected),
            "failed_7d": sum(r.get("conclusion") == "failure" for r in selected),
            "latest_url": selected[0].get("html_url") if selected else None,
            "latest_conclusion": selected[0].get("conclusion") if selected else None,
            "tested": bool(selected),
        }
    return evidence


def render_markdown(result):
    issues = result["issues"]
    events = result.get("event_runs")
    lines = [
        "# Recruiting lifecycle — observed acceptance",
        "",
        "Read-only GitHub Issues snapshot. Not a new job tracker.",
        "",
        "| Open Issue state | Current | Created last 7 days, still open |",
        "|---|---:|---:|",
    ]
    for phase in PHASES:
        lines.append(
            f"| {phase} | {issues['by_status'][phase]} | "
            f"{issues['currently_open_created_in_last_7d'][phase]} |"
        )
    lines += [
        "",
        f"**Label mismatches:** {issues['label_mismatch_count']}.",
        f"**Unclassified open Issues:** {len(issues['unclassified_open_issue_numbers'])}.",
    ]
    if issues["label_mismatches"]:
        lines += [
            "",
            "Mismatched Issues (read-only; must be reconciled): "
            + ", ".join("#" + str(x["number"]) for x in issues["label_mismatches"]),
        ]
    lines += [
        "",
        "## Real GitHub Actions event evidence",
        "",
        "| Event | Runs in last 7 days | Successful | Failed | Latest |",
        "|---|---:|---:|---:|---|",
    ]
    if events is None:
        lines.append("| Both event types | UNKNOWN (API unavailable) | — | — | — |")
    else:
        for event in ("issues", "issue_comment"):
            e = events[event]
            latest = e["latest_url"] or "not yet observed"
            lines.append(
                f"| {event} | {e['runs_7d']} | {e['successful_7d']} | "
                f"{e['failed_7d']} | {latest} |"
            )
    lines += [
        "",
        "## Interpretation",
        "",
        "- Counts reflect current GitHub state, not external job-market coverage.",
        "- Newly created Issue numbers are not automatically new eligible APPLY outcomes.",
        "- WAIT is not an employer acknowledgement; an Issue with APPLY is not a submitted application.",
        "- A zero issue_comment run means the owner-comment fast path is untested, not successful.",
        "- The 7-day created cohort is not seven daily historical snapshots or a conversion rate.",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    now = datetime.now(timezone.utc)
    result = {
        "observed_at": now.isoformat(),
        "issues": count_lifecycle(fetch_open_issues(token), now),
        "event_runs": None,
    }
    try:
        runs = api_json(
            f"actions/workflows/{ACTION_WORKFLOW}/runs?per_page=100", token
        )
        if not isinstance(runs.get("workflow_runs"), list):
            raise ValueError("Workflow runs response malformed")
        result["event_runs"] = measure_event_runs(runs["workflow_runs"], now)
    except Exception as exc:
        result["event_run_evidence_error"] = str(exc)[:200]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps({
        "open": result["issues"]["open_lifecycle_issues"],
        "states": result["issues"]["by_status"],
        "mismatches": result["issues"]["label_mismatch_count"],
        "comment_action_tested": (
            result["event_runs"]["issue_comment"]["tested"]
            if result["event_runs"] else None
        ),
    }))
    if args.strict and (
        result["issues"]["label_mismatch_count"] > 0
        or result["issues"]["unclassified_open_issue_numbers"]
    ):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
