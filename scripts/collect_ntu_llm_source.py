#!/usr/bin/env python3
"""Read-only NTU Workday LLM / agent research jobs source collector.

Owns only source observations; no recruiter contact, applications or Issues.
The public employer-controlled CXS endpoint is undocumented and may change:
bounded, respectful requests; errors remain coverage debt, not 'no jobs'.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
from html import unescape
import json
from pathlib import Path
import re
import time
from urllib.request import Request,urlopen

HOST="ntu.wd3.myworkdayjobs.com"
ROOT=f"https://{HOST}/wday/cxs/ntu/careers"
MARKET="SG"
QUERIES=("LLM","agent")
LIMIT=20
MAX_PAGES=3
MAX_DETAILS=25
JOB_TITLE=re.compile(r"(?i)(?:research\s+(?:engineer|associate|assistant)|\bAI\s+(?:engineer|safety)|applied\s+AI\s+engineer)")
MATURE=re.compile(r"(?i)\b(?:senior|staff|principal|lead|chief|director|manager)\b")
TECH=re.compile(r"(?i)(?:\bLLM\b|large language model|\bRAG\b|retrieval.augmented|\bagent(?:ic|s)?\b|natural language processing|language model|knowledge graph)")
REQID=re.compile(r"^R\d{8}$")
MAX_BYTES=3_000_000

def get_json(url:str,payload:dict|None=None) -> dict:
    data=json.dumps(payload).encode("utf-8") if payload is not None else None
    request=Request(url,data=data,headers={
        "User-Agent":"Mozilla/5.0 (compatible; ReadOnlyResearchJobs/1.0)",
        "Accept":"application/json","Content-Type":"application/json"})
    with urlopen(request,timeout=17) as response:
        if response.status!=200:raise ValueError(f"HTTP {response.status}")
        data=response.read(MAX_BYTES+1)
    if len(data)>MAX_BYTES:raise ValueError("oversized Workday response")
    obj=json.loads(data.decode("utf-8"))
    if not isinstance(obj,dict):raise ValueError("not JSON object")
    return obj

def source_scan(fetch=get_json, pause=True, known_reqs=frozenset()) -> dict:
    observations={}
    probes=[]
    for query in QUERIES:
        for page in range(MAX_PAGES):
            try:
                data=fetch(ROOT+"/jobs",{"appliedFacets":{},"limit":LIMIT,
                       "offset":page*LIMIT,"searchText":query})
                rows=data.get("jobPostings")
                if not isinstance(rows,list):raise ValueError("no jobPostings")
                valid=0
                for row in rows:
                    if not isinstance(row,dict):continue
                    p=row.get("externalPath")
                    title=row.get("title")
                    if (not isinstance(p,str) or not p.startswith("/job/")
                         or not isinstance(title,str) or not JOB_TITLE.search(title)
                         or MATURE.search(title)):
                        continue
                    match=re.search(r"_(R\d{8})(?:-\d+)?$",p)
                    if not match:continue
                    req=match.group(1)
                    if req not in observations:
                        observations[req]={"id":req,"title":title,"externalPath":p,
                            "postedOn":row.get("postedOn")}
                    valid+=1
                probes.append({"query":query,"page":page+1,"offset":page*LIMIT,
                    "raw_rows":len(rows),"qualified_title_rows":valid,
                    "reported_total":data.get("total"),"state":"LIST_OBTAINED"})
                if len(rows)<LIMIT:break
            except Exception as e:
                probes.append({"query":query,"page":page+1,"offset":page*LIMIT,
                    "state":"SOURCE_FETCH_FAILED","error":type(e).__name__+":"+str(e)[:150]})
                break
            if pause:time.sleep(0.35)
    if not any(p["state"]=="LIST_OBTAINED" for p in probes):
        raise RuntimeError("No NTU list API page succeeded. Source not scanned; do not claim zero vacancies.")
    items=[]
    fail=[]
    chosen=[r for r in observations.values() if r["id"] not in known_reqs]
    exact_known_count=len(observations)-len(chosen)
    for role in chosen[:MAX_DETAILS]:
        try:
            detail=fetch(ROOT+role["externalPath"],None)
            jd=detail.get("jobPostingInfo")
            if not isinstance(jd,dict):raise ValueError("missing jobPostingInfo")
            if jd.get("jobReqId")!=role["id"]:
                raise ValueError("first-party requisition identity mismatch")
            if jd.get("canApply") is not True:
                continue  # Explicitly not a currently usable role.
            content=unescape(re.sub(r"<[^>]*>"," ",str(jd.get("jobDescription") or "")))
            if not TECH.search(content):
                continue
            direct=jd.get("externalUrl")
            if not isinstance(direct,str) or not direct.startswith("https://"+HOST+"/"):
                raise ValueError("bad first-party role URL")
            items.append({
                "market":MARKET,"platform":"NTU Workday (first party)",
                "source_kind":"official_employer","source_id":role["id"],
                "url":direct,"company":"Nanyang Technological University",
                "title":str(jd.get("title") or role["title"])[:180],
                "location":str(jd.get("location") or "Singapore")[:140],
                "posted_at":jd.get("startDate"),
                "query":";".join(QUERIES),
                "source_verified_can_apply":True,
                "requires_hard_jd_screen":True
            })
        except Exception as e:
            fail.append({"id":role["id"],"error":type(e).__name__+":"+str(e)[:160]})
        if pause:time.sleep(0.3)
    incomplete_queries=[
        p for p in probes if p["state"]=="SOURCE_FETCH_FAILED" or
        (p["page"]==MAX_PAGES and p.get("raw_rows")==LIMIT)
    ]
    complete=(not incomplete_queries and not fail and len(chosen)<=MAX_DETAILS)
    return {
        "source":"ntu:official-cxs:SG",
        "source_kind":"official_employer",
        "source_credit":"Nanyang Technological University official careers, employer Workday CXS",
        "market":MARKET,
        "observed_at":datetime.now(timezone.utc).isoformat(),
        "coverage":"BOUNDED_QUERY_EXHAUSTED" if complete else "PARTIAL_COVERAGE",
        "title_candidates":len(chosen),
        "strong_history_id_suppressed":exact_known_count,
        "detail_budget":MAX_DETAILS,
        "details_attempted":min(MAX_DETAILS,len(chosen)),
        "details_failed":fail,
        "list_probes":probes,
        "items":items,
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--known-index",type=Path)
    args=ap.parse_args()
    known_ids=set()
    if args.known_index and args.known_index.exists():
        known=json.loads(args.known_index.read_text(encoding="utf-8"))
        for url in known.get("strong",{}).get("urls",[]):
            # Only the unique employer requisition is a strong exclusion;
            # company or title similarity alone must never suppress a role.
            if "ntu.wd3.myworkdayjobs.com" in str(url):
                known_ids.update(re.findall(r"R\d{8}",str(url)))
    r=source_scan(known_reqs=known_ids)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(r,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"source":r["source"],"coverage":r["coverage"],
         "list_probes":r["list_probes"],"title_candidates":r["title_candidates"],
         "verified_ids":[x["source_id"] for x in r["items"]],
         "detail_failures":r["details_failed"]},ensure_ascii=False),flush=True)
