#!/usr/bin/env python3
"""Bounded read-only official NTU Workday openings/liveness probe.

Workday CXS is an undocumented public UI endpoint; this is a one-off feasibility
check, no login/CAPTCHA bypass, posting or application. A web-index snippet or
200 on the HTML shell is not evidence the requisition is still open.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import time

HOST="ntu.wd3.myworkdayjobs.com"
TENANT="ntu"
SITES=("careers","Careers")
IDS=("R00025211","R00025212","R00026053")
KEYWORDS=("Research Engineer","LLM")
MAX_BYTES=3_000_000

def api_json(url,post=None):
    data=json.dumps(post).encode() if post is not None else None
    req=Request(url,data=data,headers={"Accept":"application/json",
        "Content-Type":"application/json","User-Agent":"Mozilla/5.0 (compatible; ResearchJobsVerify/1.0)"})
    with urlopen(req,timeout=18) as resp:
        body=resp.read(MAX_BYTES+1)
        if len(body)>MAX_BYTES:raise ValueError("response too large")
        if resp.status!=200:raise ValueError("non-200 "+str(resp.status))
        return json.loads(body.decode("utf-8"))

def endpoint(site):
    return f"https://{HOST}/wday/cxs/{TENANT}/{site}"

def fetch_results():
    output={"checked_at":datetime.now(timezone.utc).isoformat(),"host":HOST,
            "site":None,"attempts":[],"searches":[],"candidates":[]}
    site=None
    for s in SITES:
        url=endpoint(s)+"/jobs"
        try:
            payload=api_json(url,{"appliedFacets":{},"limit":20,"offset":0,"searchText":"Research Engineer"})
            postings=payload.get("jobPostings")
            if not isinstance(postings,list):raise ValueError("CXS returned no jobPostings array")
            site=s
            output["attempts"].append({"site":s,"state":"LIST_OK","total":payload.get("total"),
                "sample_count":len(postings)})
            break
        except Exception as e:
            output["attempts"].append({"site":s,"state":type(e).__name__,"error":str(e)[:150]})
    if not site:
        output["state"]="OFFICIAL_API_UNAVAILABLE"
        return output
    output["site"]=site
    seen={}
    for term in KEYWORDS:
        for offset in (0,20):
            try:
                payload=api_json(endpoint(site)+"/jobs",
                    {"appliedFacets":{},"limit":20,"offset":offset,"searchText":term})
                rows=payload.get("jobPostings")
                if not isinstance(rows,list):raise ValueError("missing jobPostings array")
                query_rows=[]
                for r in rows:
                    path=r.get("externalPath")
                    title=r.get("title")
                    if not isinstance(path,str) or not isinstance(title,str) or not path.startswith("/job/"):
                        continue
                    item={"title":title,"externalPath":path,
                          "locationsText":str(r.get("locationsText") or ""),
                          "postedOn":str(r.get("postedOn") or "")}
                    seen[path]=item
                    query_rows.append({"title":title[:140],"externalPath":path})
                output["searches"].append({"term":term,"offset":offset,"total":payload.get("total"),
                    "returned":len(rows),"valid_ids":len(query_rows),"sample":query_rows[:7]})
                if len(rows)<20:break
            except Exception as e:
                output["searches"].append({"term":term,"offset":offset,"error":type(e).__name__+":"+str(e)[:130]})
                break
            time.sleep(0.35)
    output["candidates"]=list(seen.values())
    output["liveness"]=[]
    for req_id in IDS:
        matching=[r for r in output["candidates"] if req_id.lower() in r["externalPath"].lower()]
        entry={"id":req_id,"listed_in_bounded_search":bool(matching),"state":"NOT_VERIFIED"}
        if matching:
            url=endpoint(site)+matching[0]["externalPath"]
            try:
                payload=api_json(url)
                job=payload.get("jobPostingInfo") if isinstance(payload,dict) else None
                if not isinstance(job,dict):raise ValueError("missing jobPostingInfo")
                jd=str(job.get("jobDescription") or "")
                entry.update(state="LIVE_OFFICIAL_DETAIL" if jd and (req_id.lower() in str(payload).lower()) else "DETAIL_ID_OR_JD_UNVERIFIED",
                   title=job.get("title"),description_chars=len(jd),
                   externalPath=matching[0]["externalPath"],
                   jobReqId=job.get("jobReqId"),timeType=job.get("timeType"),
                   detail_url=f"https://{HOST}/en-US/{site}"+matching[0]["externalPath"])
                entry["jd_excerpt"]=jd[:550]
            except Exception as e:
                entry.update(state="DETAIL_FETCH_FAILED",error=type(e).__name__+":"+str(e)[:150])
        else:
            entry["state"]="NOT_FOUND_IN_BOUNDED_SEARCH"
        output["liveness"].append(entry)
        time.sleep(0.35)
    output["state"]="SEARCH_OBSERVED"
    return output

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    x=fetch_results()
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(x,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    for z in x.get("attempts",[]):print("site",json.dumps(z))
    for z in x.get("searches",[]):print("search",json.dumps({k:v for k,v in z.items() if k!="sample"}))
    for z in x.get("liveness",[]):print("liveness",json.dumps({k:v for k,v in z.items() if k!="jd_excerpt"}))
