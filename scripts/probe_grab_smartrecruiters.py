#!/usr/bin/env python3
"""Pilot Grab's official public SmartRecruiters Posting API by market.

Read-only and bounded: exact IDs, source location and one detail call per
candidate. No login, application, tracking bypass or implied eligibility.
"""
from __future__ import annotations
import argparse,json,re,time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen

HOST="https://api.smartrecruiters.com/v1/companies/grab/postings"
COUNTRIES=("MY","SG")
PAGE=100
MAX_PAGES=2
MAX_DETAIL_PER_MARKET=12
TITLE=re.compile(r"(?i)(?:\bAI\b|machine learning|deep learning|\bML\b|genai|llm|rag|NLP|research|data scientist|data science|agentic)")
GENERIC_ENGINEERING=re.compile(r"(?i)(?:software|backend|platform|full.?stack|site reliability|data) engineer")
SENIOR=re.compile(r"(?i)\b(?:senior|principal|lead|staff|manager|director)\b")
MAX_BYTES=4_000_000

def fetch(url):
    req=Request(url,headers={"User-Agent":"JobResourcesPublicCareers/1.0",
                             "Accept":"application/json"})
    with urlopen(req,timeout=17) as r:
        if r.status!=200:raise ValueError("HTTP "+str(r.status))
        data=r.read(MAX_BYTES+1)
    if len(data)>MAX_BYTES:raise ValueError("response exceeds bound")
    result=json.loads(data.decode("utf-8"))
    if not isinstance(result,dict):raise ValueError("expected JSON object")
    return result

def location_country(loc):
    if not isinstance(loc,dict):return ""
    country=loc.get("country") or loc.get("countryCode") or ""
    if isinstance(country,dict):
        country=country.get("code") or country.get("countryCode") or ""
    return str(country).upper()

def records(result):
    a=result.get("content")
    if not isinstance(a,list):
        raise ValueError("SmartRecruiters content[] list missing")
    return a

def filter_listing(row,market):
    if not isinstance(row,dict):return None
    if location_country(row.get("location"))!=market:return None
    jobid=str(row.get("id") or "")
    title=str(row.get("name") or "")
    if not re.fullmatch(r"\d{5,20}",jobid) or not title:return None
    department=row.get("department") or {}
    dep=str(department.get("label") or department.get("name") or "") if isinstance(department,dict) else str(department)
    tech_title=bool(TITLE.search(title))
    tech_dept=bool(TITLE.search(dep)) and bool(GENERIC_ENGINEERING.search(title))
    if not (tech_title or tech_dept):return None
    return {"source_id":jobid,"market":market,"title":title[:150],
        "city":str((row.get("location") or {}).get("city") or "")[:70],
        "department":dep[:90],"seniority_flag":bool(SENIOR.search(title)),
        "url":"https://jobs.smartrecruiters.com/Grab/"+jobid}

def scan_market(market,get=fetch,pause=True):
    pages=[]; found={};errors=[]
    for pg in range(MAX_PAGES):
        u=HOST+"?"+urlencode({"limit":PAGE,"offset":pg*PAGE,"country":market})
        try:
            j=get(u)
            rows=records(j)
            matches=[]
            for row in rows:
                item=filter_listing(row,market)
                if item:
                    found[item["source_id"]]=item
                    matches.append(item["source_id"])
            total=j.get("totalFound")
            pages.append({"offset":pg*PAGE,"response_count":len(rows),
                          "ids":len(matches),"sample_ids":matches[:7],
                          "reported_total":total})
            if len(rows)<PAGE:break
        except Exception as ex:
            errors.append({"offset":pg*PAGE,"error":type(ex).__name__+": "+str(ex)[:110]})
            break
        if pause:time.sleep(0.35)
    verified=[]
    for row in list(found.values())[:MAX_DETAIL_PER_MARKET]:
        try:
            detail=get(HOST+"/"+row["source_id"])
            if str(detail.get("id") or "")!=row["source_id"]:
                raise ValueError("detail job ID mismatch")
            # Independent source detail and country required; never assume a
            # country-filtered search always enforces that filter.
            if location_country(detail.get("location"))!=market:
                raise ValueError("detail location country mismatch")
            if not detail.get("name"):
                raise ValueError("missing first-party title")
            row["source_detail_verified"]=True
            row["description_chars"]=len(str(detail.get("jobAd") or detail.get("description") or ""))
            verified.append(row)
        except Exception as ex:
            errors.append({"job_id":row["source_id"],"error":type(ex).__name__+": "+str(ex)[:110]})
        if pause:time.sleep(0.2)
    unexamined=max(0,len(found)-MAX_DETAIL_PER_MARKET)
    bounded_end=bool(pages and pages[-1]["response_count"]<PAGE and not errors and unexamined==0)
    return {"market":market,"status":"BOUNDED_SOURCE_END" if bounded_end else "PARTIAL_OR_UNAVAILABLE",
        "source":"grab:official-smartrecruiters:"+market,
        "pages":pages,"errors":errors,"observed_title_location_ids":len(found),
        "detail_verified":len(verified),"unverified_detail_budget":unexamined,
        "items":verified}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    data={"observed_at":datetime.now(timezone.utc).isoformat(),
          "provenance":"Grab first-party SmartRecruiters public Posting API",
          "results":[scan_market(m) for m in COUNTRIES]}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    for r in data["results"]:
        print(json.dumps({k:v for k,v in r.items() if k!="items"},ensure_ascii=False),flush=True)
        print("ROLE_IDS",json.dumps(r["items"],ensure_ascii=False),flush=True)

if __name__=="__main__":main()
