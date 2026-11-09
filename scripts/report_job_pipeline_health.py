#!/usr/bin/env python3
"""Read-only pipeline health derived from canonical queue state + GitHub Actions.

No new opportunity tracker. The JSON and Markdown outputs are disposable
GitHub Actions artifacts; GitHub Issues remain the only actionable jobs.
"""
from __future__ import annotations
import argparse,json,os
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import Request,urlopen

WORKFLOWS=(
 "SG Conservative Queue Consumer",
 "MY TOP Conservative First-Party JD Consumer",
 "NTU First-Party LLM Research Intake",
 "MY TOP Gen Digital Official Source Intake",
 "SG MY Structured Feed Intake",
 "Six-Battlefield Candidate Review Dispatch",
 "Official ATS Durable Source Intake",
 "SG Research First-Party Portal Probe",
)
STAGES={
 "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW":"jd_verified_awaiting_fit",
 "FETCH_OR_IDENTITY_RETRY":"retry_needed",
 "NEEDS_EMPLOYER_CANONICAL_ROUTE":"canonical_route_missing",
 "NEEDS_CANONICAL_EMPLOYER_JD":"canonical_route_missing",
 "NOT_PRESENT_ON_CURRENT_BOARD_RECHECK":"listing_recheck",
}
URL="https://api.github.com/repos/kolihhan/job-resources/actions/runs?per_page=100"


def now_utc():
    return datetime.now(timezone.utc)

def parse_dt(text):
    try:
        return datetime.fromisoformat(str(text).replace("Z","+00:00"))
    except (TypeError,ValueError):
        return None

def measure_queue(state,now=None):
    now=now or now_utc()
    market=state["market"]
    if state.get("version")!=1 or not isinstance(state.get("pending"),list):
        raise ValueError("missing canonical queue contract")
    p=state["pending"]
    sources=Counter(x.get("source","UNKNOWN") for x in p)
    stages=Counter(STAGES.get(x.get("consumer_review",{}).get("stage"),
          "not_consumer_reviewed") for x in p)
    dates=[parse_dt(x.get("first_seen_at")) for x in p]
    known=[x for x in dates if x is not None]
    age=max([round((now-x).total_seconds()/3600,1) for x in known],default=0)
    last=state.get("last_ingestion") or {}
    ingestion=parse_dt(last.get("at"))
    hours_since_ingestion=(round((now-ingestion).total_seconds()/3600,1) if ingestion else None)
    backlog=bool(p)
    # Lifetime outcomes over this specific durable source queue, NOT a
    # representative job-market conversion rate or an ATS-wide denominator.
    outcomes=Counter(x.get("state","UNKNOWN") for x in state.get("terminal",[]))
    # This is a read-only worklist derived from the existing pending source rows.
    # JD text itself stays in that canonical machine state; this is not an Issue.
    review_ready=[]
    for row in p:
        review=row.get("consumer_review") or {}
        if review.get("stage")!="FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW":
            continue
        review_ready.append({
            "seq":row["seq"],"title":row.get("title",""),"url":row.get("url",""),
            "source":row.get("source",""),"signals":review.get("signals",[]),
            "review_flags":review.get("review_flags",[]),
            "checked_at":review.get("checked_at"),
            "jd_sha256":review.get("jd_sha256"),
            "full_jd_complete":bool(review.get("full_jd_complete")),
        })
    review_ready.sort(key=lambda row:row["seq"])
    return {"market":market,"pending":len(p),"terminal":len(state.get("terminal",[])),
        "cursor":state["next_unacknowledged_seq"],
        "by_source":dict(sources),"by_stage":dict(stages),
        "unreviewed":stages["not_consumer_reviewed"],
        "jd_verified_awaiting_fit":stages["jd_verified_awaiting_fit"],
        "retry_needed":stages["retry_needed"],
        "oldest_pending_age_hours":age,
        "last_ingestion_at":last.get("at"),"last_ingestion_source":last.get("source"),
        "hours_since_ingestion":hours_since_ingestion,
        "high_concentration":(max(sources.values())/len(p) if backlog else None),
        "fit_review_candidates":review_ready,
        "fit_review_with_complete_jd":sum(r["full_jd_complete"] for r in review_ready),
        "cohort_observed_lifetime":len(p)+len(state.get("terminal",[])),
        "issue_ack_lifetime":outcomes["ISSUE_VERIFIED"],
        "hard_rejected_lifetime":outcomes["HARD_REJECTED"],
        "duplicate_confirmed_lifetime":outcomes["DUPLICATE_CONFIRMED"],
        "note":"Cohort outcomes are not a true eligibility-adjusted conversion rate; other ATS feeds are outside this queue."}

def fetch_action_runs(token):
    if not token:
        raise ValueError("GITHUB_TOKEN required for GitHub Actions evidence")
    req=Request(URL,headers={"Authorization":"Bearer "+token,
      "Accept":"application/vnd.github+json",
      "X-GitHub-Api-Version":"2022-11-28",
      "User-Agent":"job-resources-health/1.0"})
    with urlopen(req,timeout=18) as response:
        data=response.read(2_500_001)
    if len(data)>2_500_000:
        raise ValueError("run inventory too big")
    result=json.loads(data.decode("utf-8"))
    runs=result.get("workflow_runs")
    if not isinstance(runs,list):
        raise ValueError("missing action runs; cannot claim scheduled health")
    return runs

def measure_runs(runs,now=None):
    now=now or now_utc()
    rows={}
    for name in WORKFLOWS:
        matches=[r for r in runs if r.get("name")==name]
        matches.sort(key=lambda x:x.get("created_at") or "",reverse=True)
        scheduled=[r for r in matches if r.get("event")=="schedule"]
        latest=matches[0] if matches else None
        scheduled_latest=scheduled[0] if scheduled else None
        age=(
          round((now-parse_dt(latest["created_at"])).total_seconds()/3600,1)
          if latest and parse_dt(latest.get("created_at")) else None)
        rows[name]={"latest_run":latest.get("html_url") if latest else None,
                    "latest_conclusion":latest.get("conclusion") if latest else None,
                    "latest_event":latest.get("event") if latest else None,
                    "latest_run_age_hours":age,
                    "last_scheduled_run":scheduled_latest.get("html_url") if scheduled_latest else None,
                    "last_scheduled_conclusion":scheduled_latest.get("conclusion") if scheduled_latest else None,
                    "scheduled_execution_observed_in_last_100":bool(scheduled_latest)}
    return rows

def summarize(data):
    lines=["# Job discovery pipeline — observed health",
      "","Source: GitHub machine queues and recent GitHub Actions. This is not an application tracker.",
      "","## Durable candidate state",
      "","| Market | Pending | JD verified, needs fit | Uninspected | Retry | Oldest pending (h) |",
      "|---|---:|---:|---:|---:|---:|"]
    for q in data["queues"]:
        lines.append(f"| {q['market']} | {q['pending']} | {q['jd_verified_awaiting_fit']} | "
                     f"{q['unreviewed']} | {q['retry_needed']} | {q['oldest_pending_age_hours']} |")
    lines+=["","## Source queue lifetime dispositions (no misleading conversion %)",
      "",
      "| Market | Observed IDs | Issue readback ACK | Hard rejected | Exact duplicate | Still pending |",
      "|---|---:|---:|---:|---:|---:|"]
    for q in data["queues"]:
        lines.append(f"| {q['market']} | {q.get('cohort_observed_lifetime','?')} | "
                     f"{q.get('issue_ack_lifetime','?')} | {q.get('hard_rejected_lifetime','?')} | "
                     f"{q.get('duplicate_confirmed_lifetime','?')} | {q['pending']} |")
    lines+=["", "Durable SG/MY/CN source queues when present, NOT entire job-market coverage. "
                  "An ACK includes APPLY/CHECK and other confirmed historical Issue states. "
                  "Do not calculate applicant conversion, eligibility rate or interview probability.",
            "", "## Exact first-party roles awaiting full fit review",
      "", "Official JD verification is not APPLY eligibility. A missing persisted snapshot",
      "requires a fresh official read before promotion; never decide from signals alone.",
      "", "| Market | Source role | Signals | Review flags | Complete JD in queue? |",
      "|---|---|---|---|---|"]
    for q in data["queues"]:
        for role in q.get("fit_review_candidates",[]):
            title=str(role["title"]).replace("|", "/").replace("[", "").replace("]", "")
            link=role["url"] if str(role["url"]).startswith("https://") else ""
            name=f"[{title}]({link})" if link else title
            signals=", ".join(role.get("signals") or []) or "none"
            flags=", ".join(role.get("review_flags") or []) or "none"
            snapshot="yes" if role["full_jd_complete"] else "no — re-fetch"
            lines.append(f"| {q['market']} | {name} | {signals} | {flags} | {snapshot} |")
    if data.get("missing_source_queues"):
        lines += ["", "**Missing source queue telemetry:** " +
                  ", ".join(data["missing_source_queues"]) +
                  " (not proof of zero job vacancies)."]
    lines+=["","## Workflow evidence",
            "","| Workflow | Latest run | Conclusion | Scheduled run seen? |",
            "|---|---|---|---|"]
    for name,r in data["workflows"].items():
        link=r["latest_run"] or "Not in recent 100 runs"
        lines.append(f"| {name} | {link} | {r['latest_conclusion'] or 'N/A'} | "
                     f"{'yes' if r['scheduled_execution_observed_in_last_100'] else 'not established'} |")
    lines+=["","## Explicit limits",
      "",
      "- No workflow scheduled execution is claimed just because it has a schedule definition.",
      "- Raw source IDs and queued JDs are not APPLY jobs.",
      "- Company concentration and full market recall are not established from this report.",
      "- Missing market queues are unavailable telemetry, not evidence of no vacancies."]
    return "\n".join(lines)+"\n"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,default=Path("."))
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--summary",type=Path,required=True)
    args=ap.parse_args()
    states=[]
    missing=[]
    for m in ("sg","my","cn"):
        p=args.repo/"discovery-state"/f"platform-index-{m}.json"
        if p.is_file():
            states.append(json.loads(p.read_text(encoding="utf-8")))
        else:
            missing.append(m.upper())
    now=now_utc()
    result={"observed_at":now.isoformat(),"queues":[measure_queue(s,now) for s in states],
            "missing_source_queues":missing,
            "workflows":measure_runs(fetch_action_runs(os.environ.get("GITHUB_TOKEN","")),now)}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    args.summary.parent.mkdir(parents=True,exist_ok=True)
    args.summary.write_text(summarize(result),encoding="utf-8")
    print(json.dumps({"markets":{x["market"]:{"pending":x["pending"],"jd_ready":x["jd_verified_awaiting_fit"],
              "unreviewed":x["unreviewed"],"errors":x["retry_needed"]} for x in result["queues"]},
              "workflows_seen":sum(bool(x["latest_run"]) for x in result["workflows"].values())},
              ensure_ascii=False))
if __name__=="__main__":main()
