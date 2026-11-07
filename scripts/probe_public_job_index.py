#!/usr/bin/env python3
"""Read-only search-index transport feasibility for public hiring platforms.

No login, credentials, proxy, CAPTCHA bypass or applications. Search results
are candidate *signals*, not live/current JDs. Only exact-platform role URLs
with stable IDs count; index search hit totals never count.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
import urllib.error
from urllib.parse import urlparse, parse_qs, urlencode, unquote
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

QUERIES = [
    {"market":"MY","platform":"JobStreet","site":"my.jobstreet.com/job/","terms":"AI Engineer RAG LLM"},
    {"market":"SG","platform":"JobStreet","site":"sg.jobstreet.com/job/","terms":"AI Engineer RAG Agent"},
    {"market":"MY","platform":"Hiredly","site":"my.hiredly.com/jobs/","terms":"AI engineer agent"},
    {"market":"SG","platform":"LinkedIn","site":"sg.linkedin.com/jobs/view/","terms":"research engineer NLP LLM"},
    {"market":"MY","platform":"Indeed","site":"malaysia.indeed.com/viewjob","terms":"AI Engineer"},
    {"market":"SG","platform":"Indeed","site":"sg.indeed.com/viewjob","terms":"LLM Engineer"},
]
PROVIDERS = ("bing_rss", "ddg_html")
MAX_BYTES = 1_400_000

def make_query(spec: dict) -> str:
    return f'site:{spec["site"]} {spec["terms"]}'

def provider_url(provider: str, query: str) -> str:
    if provider == "bing_rss":
        return "https://www.bing.com/search?" + urlencode({"q": query, "format": "rss", "setlang": "en"})
    if provider == "ddg_html":
        return "https://html.duckduckgo.com/html/?" + urlencode({"q": query})
    raise ValueError("unknown provider")

class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)

def candidate_url(url: str, market: str) -> str | None:
    # Unwrap only transparent public search redirect arguments.
    p = urlparse(url)
    if p.hostname in ("duckduckgo.com", "www.duckduckgo.com", "html.duckduckgo.com"):
        v = parse_qs(p.query).get("uddg", [])
        if not v:
            return None
        url = unquote(v[0])
        p = urlparse(url)
    if p.scheme not in ("http", "https") or not p.hostname:
        return None
    host = p.hostname.lower().removeprefix("www.")
    seg = p.path.rstrip("/")
    jobstreet = re.fullmatch(r"/job/(\d{6,12})", seg, re.I)
    linkedin = re.search(r"/jobs/view/(?:[^/?]*-)?(\d{7,13})$", seg, re.I)
    indeed = re.fullmatch(r"/viewjob", seg, re.I)
    hiredly = re.fullmatch(r"/jobs/(?:[^/?]+/)?([\w-]{7,})", seg, re.I)
    if market == "MY":
        if host == "my.jobstreet.com" and jobstreet:
            return f"https://my.jobstreet.com/job/{jobstreet.group(1)}"
        if host in ("my.linkedin.com", "linkedin.com") and linkedin:
            return f"https://www.linkedin.com/jobs/view/{linkedin.group(1)}"
        if host in ("malaysia.indeed.com", "my.indeed.com") and indeed:
            jk = parse_qs(p.query).get("jk", [""])[0]
            if re.fullmatch("[a-zA-Z0-9]{12,24}", jk):
                return f"https://malaysia.indeed.com/viewjob?jk={jk}"
        if host == "my.hiredly.com" and hiredly:
            return f"https://my.hiredly.com{seg}"
    if market == "SG":
        if host == "sg.jobstreet.com" and jobstreet:
            return f"https://sg.jobstreet.com/job/{jobstreet.group(1)}"
        if host in ("sg.linkedin.com", "linkedin.com") and linkedin:
            return f"https://www.linkedin.com/jobs/view/{linkedin.group(1)}"
        if host == "sg.indeed.com" and indeed:
            jk = parse_qs(p.query).get("jk", [""])[0]
            if re.fullmatch("[a-zA-Z0-9]{12,24}", jk):
                return f"https://sg.indeed.com/viewjob?jk={jk}"
    return None

def parse_results(provider: str, content: bytes, market: str) -> list[str]:
    found = []
    if provider == "bing_rss":
        root = ET.fromstring(content)
        for item in root.findall(".//item"):
            link = item.findtext("link")
            if link:
                found.append(link)
    elif provider == "ddg_html":
        h = Anchors()
        h.feed(content.decode("utf-8", "replace"))
        found = h.hrefs
    else:
        raise ValueError("unknown provider")
    ids = {candidate_url(u, market) for u in found}
    return sorted(x for x in ids if x)

def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent":"Mozilla/5.0 (compatible; PublicJobIndexPilot/1.0)",
        "Accept":"application/rss+xml,application/xml,text/html", "Accept-Language":"en-US,en;q=0.8"})
    with urlopen(req, timeout=11) as response:
        data = response.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError("oversized response")
        return data

def run_one(spec: dict, provider: str) -> dict:
    query = make_query(spec)
    result = {"market":spec["market"],"platform":spec["platform"],"provider":provider,
              "query":query,"state":"NO_VERIFIED_JOB_IDS","ids":[]}
    try:
        raw = fetch(provider_url(provider, query))
        ids = parse_results(provider, raw, spec["market"])
        result["ids"] = ids[:25]
        result["state"] = "INDEX_JOB_IDS" if ids else "NO_VERIFIED_JOB_IDS"
        result["response_bytes"] = len(raw)
    except urllib.error.HTTPError as e:
        result["state"] = "HTTP_" + str(e.code)
    except Exception as e:
        result["state"] = "UNAVAILABLE_OR_INVALID"
        result["error"] = type(e).__name__ + ":" + str(e)[:100]
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    results=[]
    for spec in QUERIES:
        for provider in PROVIDERS:
            rec=run_one(spec,provider)
            results.append(rec)
            print(json.dumps({"market":rec["market"],"platform":rec["platform"],
                "provider":provider,"state":rec["state"],"jobs":len(rec["ids"])}),flush=True)
            time.sleep(0.4)
    out={"generated_at":datetime.now(timezone.utc).isoformat(),"kind":"source_pilot_not_live_jobs",
         "results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
if __name__=="__main__":
    main()
