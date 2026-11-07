#!/usr/bin/env python3
"""Pilot Gen Digital/MoneyLion's official public Ashby job board API.

This is a direct employer source, NOT a listing-aggregator or proof of
candidate eligibility. It records exact Ashby UUID, location, and job URLs.
"""
from __future__ import annotations
import argparse,json,re
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen

URL="https://api.ashbyhq.com/posting-api/job-board/gen-digital"
DOMAIN="https://jobs.ashbyhq.com/gen-digital/"
ROLE=re.compile(r"(?i)(?:\bAI\b|machine learning|genai|generative AI|LLM|RAG|agentic|NLP|applied scientist|research scientist|MLOps|AI engineer)")
UUID=re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",re.I)
MAX_BYTES=5_000_000

def get(url=URL):
    req=Request(url+"?includeCompensation=false",
       headers={"User-Agent":"JobResourcesFirstPartyCareers/1.0",
                "Accept":"application/json"})
    with urlopen(req,timeout=20) as f:
        if f.status!=200:raise ValueError("non-200 response")
        raw=f.read(MAX_BYTES+1)
    if len(raw)>MAX_BYTES:raise ValueError("source too large")
    data=json.loads(raw.decode("utf-8"))
    if not isinstance(data,dict):raise ValueError("not object")
    return data

def parse_jobs(payload):
    entries=payload.get("jobs")
    if not isinstance(entries,list):
        raise ValueError("Ashby jobs list absent")
    observed=[]
    for entry in entries:
        if not isinstance(entry,dict):continue
        id=str(entry.get("id") or "")
        title=str(entry.get("title") or "")
        location=str(entry.get("location") or "")
        if not(UUID.fullmatch(id) and title and ROLE.search(title)):
            continue
        if not any(x in location.lower() for x in ("malaysia","mys","kuala lumpur","petaling jaya","selangor","penang")):
            continue
        link=entry.get("jobUrl") or entry.get("jobPostingUrl") or ""
        canonical=DOMAIN+id
        if not isinstance(link,str) or not link.startswith(DOMAIN):
            link=canonical
        body=str(entry.get("descriptionPlain") or entry.get("descriptionHtml") or "")
        observed.append({"market":"MY","platform":"Gen Digital official Ashby",
             "company":"Gen Digital / MoneyLion","title":title[:180],
             "location":location[:120],"url":canonical,"source_id":id,
             "source_kind":"official_employer","title_technical_signal":True,
             "jd_chars":len(body),"public_board_url":link,
             "explicit_employment_type":entry.get("employmentType")})
    return observed

def run(fetch=get):
    result={"source":"gen-digital:official-ashby:MY",
            "observed_at":datetime.now(timezone.utc).isoformat(),
            "status":"UNVERIFIED","total_listed":0,"items":[]}
    try:
        payload=fetch()
        jobs=payload.get("jobs")
        if not isinstance(jobs,list):
            raise ValueError("no jobs list")
        items=parse_jobs(payload)
        result.update(status="OFFICIAL_BOARD_OBSERVED",
          total_listed=len(jobs),technical_my_ids=len(items),items=items)
    except Exception as e:
        result.update(status="SOURCE_ERROR",error=type(e).__name__+": "+str(e)[:140])
    return result

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args()
    data=run()
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print(json.dumps(data,ensure_ascii=False),flush=True)
