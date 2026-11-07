#!/usr/bin/env python3
"""Bounded, read-only SG/MY job-feed availability pilot.

Tests real structured job feeds from official documented public APIs.
No employer-facing actions. Does not treat schema success, generic totals
or remote jobs outside target geography as SG/MY vacancy coverage.
"""
from __future__ import annotations
import json
import time
import argparse
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError

QUERIES=[
    ("devglobal","SG","AI"),
    ("devglobal","MY","AI"),
    ("himalayas","SG","AI"),
    ("himalayas","MY","AI"),
    ("devglobal","SG","research engineer"),
    ("devglobal","MY","machine learning"),
]
KEYWORDS=("ai ","ai/","ai-","agent","llm","rag","nlp","machine learning","deep learning",
          "research engineer","research scientist","applied scientist","ml engineer","genai","artificial intelligence")
MAX_JSON_BYTES=3_500_000

def url_for(provider,market,keyword):
    if provider=="devglobal":
        return "https://devglobaljobs.com/api/v1/jobs?"+urlencode({
            "country":market.lower(),"search":keyword,"limit":50,"offset":0})
    if provider=="himalayas":
        return "https://himalayas.app/jobs/api/search?"+urlencode({
            "country":market,"q":keyword,"sort":"recent","page":1})
    raise ValueError("unknown provider")

def get_json(url,timeout=17):
    req=Request(url,headers={"Accept":"application/json","User-Agent":"JobSearchSourceFeasibility/1.0"})
    with urlopen(req,timeout=timeout) as f:
        if f.status!=200:raise ValueError("HTTP "+str(f.status))
        body=f.read(MAX_JSON_BYTES+1)
    if len(body)>MAX_JSON_BYTES:raise ValueError("response oversized")
    return json.loads(body.decode("utf-8"))

def records(provider,data):
    if isinstance(data,list):
        return data
    if not isinstance(data,dict):
        raise ValueError("unexpected top-level JSON")
    for key in ("jobs","data","results","items"):
        x=data.get(key)
        if isinstance(x,list):
            return x
        if isinstance(x,dict):
            for k in ("jobs","items","results"):
                if isinstance(x.get(k),list):return x[k]
    return []

def normalize(provider,market,data):
    out=[]
    for j in records(provider,data):
        if not isinstance(j,dict):continue
        title=j.get("title") or j.get("job_title") or ""
        company=j.get("companyName") or j.get("company") or j.get("organisation") or j.get("organization") or ""
        if isinstance(company,dict):
            company=company.get("name","")
        loc=j.get("location") or j.get("locationRestrictions") or j.get("country") or ""
        if isinstance(loc,(list,dict)):
            loc=json.dumps(loc,ensure_ascii=False)
        url=j.get("applicationLink") or j.get("url") or j.get("link") or j.get("job_url") or ""
        jid=j.get("guid") or j.get("id") or ""
        if not isinstance(title,str) or not title or not isinstance(url,str) or not url.startswith("https://"):
            continue
        # Remote country=SG/MY results might include worldwide jobs; don't claim
        # they are physically located in Singapore or Malaysia.
        out.append({"source":provider,"market_filter":market,"id":str(jid)[:100],
                    "title":title[:160],"company":str(company)[:120],
                    "location":str(loc)[:180],"url":url[:500],
                    "relevant_title":any(w in (" "+title.lower()+" ") for w in KEYWORDS)})
    return out

def run(fetch=get_json):
    result={"generated_at":datetime.now(timezone.utc).isoformat(),
            "source_kind":"aggregator_api_not_native_platform",
            "queries":[]}
    for source,market,term in QUERIES:
        row={"provider":source,"market_filter":market,"term":term,"state":"UNTESTED",
             "raw_count":0,"with_exact_urls":0,"relevant_titles":0,
             "sample":[]}
        url=url_for(source,market,term)
        try:
            data=fetch(url)
            raw=records(source,data)
            obs=normalize(source,market,data)
            row.update(state="STRUCTURED_JOBS" if obs else "EMPTY_OR_NO_ROLE_LINKS",
                raw_count=len(raw),with_exact_urls=len(obs),
                relevant_titles=sum(r["relevant_title"] for r in obs),
                source_schema=list(data)[:12] if isinstance(data,dict) else ["array"],
                sample=obs[:5])
        except HTTPError as e:
            row.update(state="HTTP_"+str(e.code))
        except (URLError,TimeoutError) as e:
            row.update(state="NETWORK_ERROR",error=str(e)[:140])
        except Exception as e:
            row.update(state="INVALID_JSON_OR_SCHEMA",error=type(e).__name__+": "+str(e)[:140])
        result["queries"].append(row)
        print(json.dumps({"source":source,"market":market,"query":term,
            "state":row["state"],"exact_url_jobs":row["with_exact_urls"],
            "relevant_titles":row["relevant_titles"],"schema":row.get("source_schema")}),flush=True)
        time.sleep(0.35)
    return result

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    r=run()
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(r,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
