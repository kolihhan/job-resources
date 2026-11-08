#!/usr/bin/env python3
"""Bounded read-only SG/MY first-party ATS coverage pilot; never applies or creates Issues."""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
from html import unescape
import json,re,time
from pathlib import Path
from urllib.request import Request,urlopen

SOURCES=(
 ("SG","Stripe","greenhouse","stripe"),
 ("MY","New Era Technology","greenhouse","neweratech"),
 ("SG","NCS","smartrecruiters","NCS3"),
 ("MY","Bjak","ashby","bjakcareer"),
)
SIGNAL=re.compile(r"\b(?:LLM|RAG|NLP|GenAI|AI|ML|MLOps|agentic|agents?|retrieval|embedding|evaluation|machine learning|artificial intelligence|generative ai)\b",re.I)
TITLE=re.compile(r"\b(?:AI|ML|NLP|LLM|RAG|MLOps|agentic|agents?|machine learning|artificial intelligence|research engineer|applied scientist)\b",re.I)
ENGINEERING=re.compile(r"(?:software|backend|back.end|full.stack|platform|data)\s+(?:engineer|developer)|fullstack",re.I)
SENIOR=re.compile(r"\b(?:senior|lead|staff|principal|manager|director|head|architect)\b",re.I)
NONTECH=re.compile(r"\b(?:account executive|sales representative|account manager|business development|sales director|sales manager)\b",re.I)
MAX_BYTES=24_000_000  # First Bjak Ashby trial exceeded 8MB; bounded 24MB diagnostic retry.

def fetch_json(url):
    req=Request(url,headers={"User-Agent":"JobResourcesReadOnlyATSFeasibility/1.0","Accept":"application/json"})
    with urlopen(req,timeout=18) as resp:
        if resp.status!=200:raise ValueError("HTTP "+str(resp.status))
        data=resp.read(MAX_BYTES+1)
    if len(data)>MAX_BYTES:raise ValueError("response exceeds size bound")
    obj=json.loads(data.decode("utf-8"))
    if not isinstance(obj,dict):raise ValueError("JSON object expected")
    return obj

def in_market(market,location,country=""):
    l=str(location or "").lower()
    c=str(country or "").lower()
    if c in ("sg","singapore"):return market=="SG"
    if c in ("my","malaysia"):return market=="MY"
    if market=="SG":return "singapore" in l
    return any(x in l for x in ("malaysia","kuala lumpur","petaling jaya","shah alam","penang","selangor","cyberjaya","putrajaya","johor"))

def text_of(value):
    if isinstance(value,str):return value
    if isinstance(value,list):return " ".join(text_of(v) for v in value)
    if isinstance(value,dict):return " ".join(text_of(v) for v in value.values())
    return ""

def role(market,company,provider,board,id_,title,location,jd):
    jobid=str(id_ or "").strip();title=str(title or "").strip()
    if not jobid or not title or not location:return None
    if provider=="greenhouse":
        if not jobid.isdigit():return None
        url=f"https://job-boards.greenhouse.io/{board}/jobs/{jobid}"
    elif provider=="ashby":
        if not re.fullmatch(r"[0-9a-fA-F-]{36}",jobid):return None
        url=f"https://jobs.ashbyhq.com/{board}/{jobid}"
    else:
        if not re.fullmatch(r"[0-9A-Za-z-]{8,60}",jobid):return None
        url=f"https://jobs.smartrecruiters.com/{board}/{jobid}"
    full=unescape(re.sub(r"<[^>]+>"," ",jd))
    keywords=set(m.group(0).lower() for m in SIGNAL.finditer(full))
    direct=bool(TITLE.search(title))
    if NONTECH.search(title):return None  # An 'AI' customer/account role is not AI engineering.
    if not direct and not (ENGINEERING.search(title) and len(keywords)>=2):return None
    return {"market":market,"company":company,"ats":provider,"board":board,
        "source_id":jobid,"title":title[:180],"location":str(location)[:140],"url":url,
        "jd_chars":len(full),"jd_verified":bool(full),
        "senior_title_flag":bool(SENIOR.search(title)),
        "jd_ai_signal_count":len(keywords),
        "signal":"ai_title" if direct else "generic_engineering_with_AI_JD"}

def probe(source,get=fetch_json,pace=False,max_details=12):
    market,company,provider,board=source
    out={"market":market,"company":company,"provider":provider,"board":board,
         "status":"SOURCE_UNVERIFIED","pages":[],"errors":[],"items":[]}
    rows=[]
    try:
        if provider=="greenhouse":
            data=get(f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs")
            rows=data.get("jobs")
            if not isinstance(rows,list):raise ValueError("missing Greenhouse jobs[]")
            out["pages"].append({"page":1,"rows":len(rows),"end":True})
        elif provider=="ashby":
            data=get(f"https://api.ashbyhq.com/posting-api/job-board/{board}")
            all_rows=data.get("jobs")
            if not isinstance(all_rows,list):raise ValueError("missing Ashby jobs[]")
            rows=[x for x in all_rows if isinstance(x,dict) and x.get("isListed") is not False]
            out["pages"].append({"page":1,"rows":len(rows),"end":True})
        else:
            for page in range(2):
                offset=page*100
                data=get(f"https://api.smartrecruiters.com/v1/companies/{board}/postings?limit=100&offset={offset}")
                result=data.get("content")
                if not isinstance(result,list):raise ValueError("missing SmartRecruiters content[]")
                rows.extend(result)
                end=len(result)<100 or (isinstance(data.get("totalFound"),int) and offset+len(result)>=data["totalFound"])
                out["pages"].append({"page":page+1,"rows":len(result),"end":end})
                if end:break
                if pace:time.sleep(.2)
    except Exception as err:
        out["errors"].append("LIST:"+type(err).__name__+":"+str(err)[:130])
        out["status"]="PARTIAL_COVERAGE" if out["pages"] else "SOURCE_ERROR"
        return out
    out["source_rows"]=len(rows);out["end_proven"]=bool(out["pages"] and out["pages"][-1]["end"])
    plausible=[];seen=set()
    for item in rows:
        if not isinstance(item,dict):continue
        if provider=="greenhouse":
            id_=item.get("id");title=item.get("title")
            location=(item.get("location") or {}).get("name") or "";country=""
        elif provider=="ashby":
            id_=item.get("id");title=item.get("title")
            location=item.get("location") or ""
            country=((item.get("address") or {}).get("postalAddress") or {}).get("addressCountry") or ""
        else:
            id_=item.get("id");title=item.get("name")
            loc=item.get("location") or {}
            location=" ".join(str(loc.get(k) or "") for k in ("city","country"))
            country=loc.get("country") or loc.get("countryCode") or ""
        if not in_market(market,location,country) or not id_ or str(id_) in seen:continue
        seen.add(str(id_))
        if not (TITLE.search(str(title or "")) or ENGINEERING.search(str(title or ""))):continue
        desc=text_of(item.get("descriptionPlain") or item.get("descriptionHtml") or "") if provider=="ashby" else ""
        plausible.append((id_,title,location,desc))
    # Rank obvious AI roles first; do not silently discard senior/adjacent rows.
    plausible.sort(key=lambda x:(not bool(TITLE.search(str(x[1]))),bool(SENIOR.search(str(x[1])))))
    out["local_title_signals"]=len(plausible)
    for id_,title,location,desc in plausible[:max_details]:
        if not desc:
            try:
                if provider=="greenhouse":
                    detail=get(f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs/{id_}")
                    if str(detail.get("id"))!=str(id_):raise ValueError("job ID mismatch")
                    desc=text_of(detail.get("content") or "")
                else:
                    detail=get(f"https://api.smartrecruiters.com/v1/companies/{board}/postings/{id_}")
                    if str(detail.get("id"))!=str(id_):raise ValueError("job ID mismatch")
                    desc=text_of(detail.get("jobAd") or detail.get("description") or "")
            except Exception as err:
                out["errors"].append("DETAIL:"+str(id_)+":"+type(err).__name__+":"+str(err)[:95])
        x=role(market,company,provider,board,id_,title,location,desc)
        if x:out["items"].append(x)
        if pace:time.sleep(.2)
    out["details_deferred"]=max(0,len(plausible)-max_details)
    out["jd_unverified_candidates"]=sum(not x["jd_verified"] for x in out["items"])
    out["status"]="BOUNDED_SOURCE_END" if out["end_proven"] and not out["errors"] and not out["details_deferred"] and not out["jd_unverified_candidates"] else "PARTIAL_COVERAGE"
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True,type=Path)
    args=ap.parse_args()
    result={"observed_at":datetime.now(timezone.utc).isoformat(),
        "mode":"READ_ONLY_PILOT_NOT_APPLY_OR_FULL_MARKET_COVERAGE",
        "sources":[probe(src,pace=True) for src in SOURCES]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for src in result["sources"]:
        print(json.dumps({"market":src["market"],"source":src["company"],"status":src["status"],
            "listed":src.get("source_rows"),"title_signals":src.get("local_title_signals"),
            "exact_candidates":len(src["items"]),"ids":[x["source_id"] for x in src["items"][:8]],
            "errors":src["errors"][:3]},ensure_ascii=False))

if __name__=="__main__":main()
