#!/usr/bin/env python3
"""Verify exact MY first-party Workday AI requisitions via employer CXS details.

The job pages are public; no credentials, application submission or employer contact.
A successful HTTP 200 without exact jobReqId & canApply does not prove liveness.
"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen

ROLES=[
{"name":"Intel Graduate Talent — GenAI Software Solutions Engineer",
 "req":"JR0284164","host":"intel.wd1.myworkdayjobs.com","tenant":"intel","site":"External",
 "path":"/job/Graduate-Talent--GenAI-Software-Solutions-Engineer-_JR0284164-1"},
{"name":"Accenture Full Stack LLM / Agentic AI Developers",
 "req":"R00351598","host":"accenture.wd103.myworkdayjobs.com","tenant":"accenture","site":"AccentureCareers",
 "path":"/job/Kuala-Lumpur-Exchange-106/Full-Stack-LLM---Agentic-AI-Developers_R00351598"}
]
# Intel path starts /job/role at Workday; consistent with employer's original web URL.
MAX_BODY=4_000_000

def get_json(url:str)->dict:
    req=Request(url,headers={"Accept":"application/json","User-Agent":"Mozilla/5.0 (compatible; PublicCareerVerification/1.0)"})
    with urlopen(req,timeout=18) as res:
        raw=res.read(MAX_BODY+1)
        if len(raw)>MAX_BODY:raise ValueError("oversized first party detail")
    data=json.loads(raw.decode("utf8"))
    if not isinstance(data,dict):raise ValueError("invalid first party schema")
    return data

def verify(role,fetch=get_json):
    reqid=role["req"]
    base=f'https://{role["host"]}/wday/cxs/{role["tenant"]}/{role["site"]}'
    attempts=[]
    result={"name":role["name"],"req":reqid,"state":"UNVERIFIED",
        "official_web_url":f'https://{role["host"]}/{role["site"]}{role["path"]}',
        "attempts":[]}
    candidates=[base+role["path"]]
    # Alternative Workday site-case route only when first fails.
    for link in candidates:
        try:
            response=fetch(link)
            job=response.get("jobPostingInfo")
            if not isinstance(job,dict):raise ValueError("missing jobPostingInfo")
            if job.get("jobReqId")!=reqid:raise ValueError("req mismatch")
            desc=str(job.get("jobDescription") or "")
            result.update(
                state="LIVE_OFFICIAL_APPLY" if job.get("canApply") is True and desc else
                    "NOT_ACCEPTING" if job.get("canApply") is False else "JD_OR_APPLY_UNVERIFIED",
                title=job.get("title"),
                canApply=job.get("canApply"),jobReqId=job.get("jobReqId"),
                location=job.get("location"),timeType=job.get("timeType"),
                startDate=job.get("startDate"),postedOn=job.get("postedOn"),
                externalUrl=job.get("externalUrl"),jobDescription=desc,
                description_chars=len(desc),
                fieldNames=sorted(job.keys()))
            attempts.append({"url":link,"state":"DETAIL_MATCHED"})
            break
        except Exception as e:
            attempts.append({"url":link,"state":type(e).__name__,"error":str(e)[:160]})
    result["attempts"]=attempts
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    r={"checked_at":datetime.now(timezone.utc).isoformat(),"results":[verify(z) for z in ROLES]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(r,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    for z in r["results"]:
        print(json.dumps({k:v for k,v in z.items() if k!="jobDescription"},ensure_ascii=False),flush=True)

if __name__=="__main__":
    main()
