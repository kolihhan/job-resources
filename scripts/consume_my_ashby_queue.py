#!/usr/bin/env python3
"""MY high-quality Ashby intake consumer: official JD, all-Issue dedupe, durable review.

Does not create application Issues or decide user fit by title/keyword. Uses the
Gen Digital/MoneyLion first-party public board, not third-party snippets.
"""
from __future__ import annotations
import argparse,json,os,re,time
from datetime import datetime,timezone
from pathlib import Path
from platform_index_queue import ack, atomic_write, validate_state, verify_issue_readback
from consume_platform_queue import due, full_issue_history, review_summary
from probe_gen_digital_ashby import get as fetch_board

UUID=re.compile(r"^https://jobs\.ashbyhq\.com/gen-digital/([0-9a-f-]{36})$",re.I)
SOURCE="gen-digital:official-ashby:MY"

def run(state,issues,board,confirm_issue,now=None,limit=12):
    validate_state(state,"MY")
    if not isinstance(issues,list) or not issues:
        raise ValueError("Full GitHub Issues history is required before classification")
    if not isinstance(board,dict) or not isinstance(board.get("jobs"),list):
        raise ValueError("Current complete first-party Ashby board is unavailable")
    if not callable(confirm_issue):
        raise ValueError("Live Issue readback must be supplied")
    now=now or datetime.now(timezone.utc)
    iso=now.isoformat().replace("+00:00","Z")
    jobs={str(j.get("id")):j for j in board["jobs"] if isinstance(j,dict)}
    selected=sorted((r for r in state["pending"] if due(r,now)),
                    key=lambda r:(bool(r.get("consumer_review")),r["seq"]))[:limit]
    report={"observed_at":iso,"market":"MY","official_board_total":len(board["jobs"]),
            "considered":0,"verified_jd":0,"issue_ack":0,"retry_or_other":0,
            "outcomes":[]}
    for row in selected:
        report["considered"]+=1
        item={"seq":row["seq"],"title":row["title"],"url":row["url"]}
        try:
            match=UUID.fullmatch(row["url"])
            if not match or row.get("source")!=SOURCE:
                row["consumer_review"]={"stage":"NEEDS_CANONICAL_EMPLOYER_JD",
                       "checked_at":iso}
                item["state"]="NEEDS_CANONICAL_EMPLOYER_JD"
                report["retry_or_other"]+=1
            else:
                uid=match.group(1).lower()
                # Full exact URL in Issue is necessary; similar title or short ID
                # is not a confirmed match. A fully enumerated Issue history
                # is required before concluding no prior application.
                matched=[i for i in issues if isinstance(i,dict)
                          and uid in str(i.get("body") or "").lower()
                          and row["url"].lower() in str(i.get("body") or "").lower()]
                if len(matched)>1:
                    raise ValueError("ambiguous prior exact-job Issue match")
                if len(matched)==1:
                    i=matched[0]
                    link="https://github.com/kolihhan/job-resources/issues/"+str(i["number"])
                    if confirm_issue(link,row["url"]) is not True:
                        raise ValueError("live canonical Issue readback not confirmed")
                    title=str(i.get("title") or "")
                    action="ISSUE_VERIFIED" if title.startswith(("[APPLY]","[CHECK]")) else "DUPLICATE_CONFIRMED"
                    ack(state,{"key":row["key"],"action":action,
                               "evidence_url":link,"issue_url":link},issue_proven=True)
                    item["state"]=action
                    report["issue_ack"]+=1
                elif uid not in jobs:
                    row["consumer_review"]={"stage":"NOT_PRESENT_ON_CURRENT_BOARD_RECHECK",
                        "checked_at":iso,
                        "note":"Cannot assert closed solely from a missing current board snapshot."}
                    item["state"]="NOT_PRESENT_ON_CURRENT_BOARD_RECHECK"
                    report["retry_or_other"]+=1
                else:
                    info=jobs[uid]
                    link=str(info.get("jobUrl") or "")
                    location=str(info.get("location") or "").lower()
                    jd=str(info.get("descriptionPlain") or info.get("descriptionHtml") or "")
                    if (not link.startswith(row["url"]) or
                        not any(t in location for t in ("mys","malaysia","kuala lumpur","selangor","petaling jaya","penang")) or
                        len(jd)<100):
                        raise ValueError("first-party Ashby exact URL, location or full JD not proven")
                    common={"jobReqId":uid,"jobDescription":jd,
                            "timeType":info.get("employmentType")}
                    review=review_summary(common,iso)
                    review["source_kind"]="Gen Digital first-party Ashby"
                    review["public_employer_board_listed"]=True
                    review["source_verified_can_apply"]="NOT_ASSERTED_BY_ASHBY_FEED"
                    row["consumer_review"]=review
                    report["verified_jd"]+=1
                    item.update(state=review["stage"],signals=review["signals"],
                                flags=review["review_flags"])
        except Exception as e:
            row["consumer_review"]={"stage":"FETCH_OR_IDENTITY_RETRY",
                "checked_at":iso,"error":type(e).__name__+": "+str(e)[:170]}
            item["state"]="FETCH_OR_IDENTITY_RETRY"
            report["retry_or_other"]+=1
        report["outcomes"].append(item)
    state["next_unacknowledged_seq"]=min([x["seq"] for x in state["pending"]],
                                        default=state["next_seq"])
    validate_state(state,"MY")
    report.update(pending_after=len(state["pending"]),
       review_ready=sum(x.get("consumer_review",{}).get("stage")=="FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW"
                        for x in state["pending"]),
       cursor_after=state["next_unacknowledged_seq"])
    return state,report

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--state",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--limit",type=int,default=12)
    a=p.parse_args()
    if a.limit<1 or a.limit>30:raise SystemExit("limit out of range")
    token=os.environ.get("GITHUB_TOKEN","")
    issues=full_issue_history(token)
    board=fetch_board()
    state=json.loads(a.state.read_text(encoding="utf8"))
    state,report=run(state,issues,board,
        confirm_issue=lambda i,u:verify_issue_readback(i,u,token),
        limit=a.limit)
    atomic_write(a.state,state)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=="__main__":main()
