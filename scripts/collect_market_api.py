#!/usr/bin/env python3
"""Read-only, no-key jobs API supplement to the existing ATS feed.

Uses Active Vacancies' public REST API, not HTML scraping. Only employer-owned
exact ATS links enter the established pending queue; API records are *leads*,
never verified eligibility, applications, or permission to contact employers.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from platform_index_queue import canonical

BASE = "https://activevacancies.com/api/v1/jobs"
MARKETS = {"SG": "Singapore", "MY": "Malaysia", "CN": "China"}
QUERIES = ("AI Engineer", "LLM", "Research Engineer", "Machine Learning Engineer")
CN_EXTRA = ("大模型", "算法工程师")
TITLE = re.compile(
    r"\b(?:AI|ML|LLM|NLP|RAG|agentic|agents?|machine learning|"
    r"applied scientist|research engineer|research assistant|"
    r"research associate|data scientist|retrieval|ranking)\b"
    r"|人工智能|大模型|智能体|算法|机器学习|检索|研究工程师", re.I)
REGIONS = {
    "SG": re.compile(r"\bsingapore\b|新加坡", re.I),
    "MY": re.compile(r"\bmalaysia\b|kuala lumpur|petaling jaya|selangor|"
                     r"penang|johor|cyberjaya|putrajaya|bayan lepas|槟城|马来西亚", re.I),
    "CN": re.compile(r"\bchina\b|beijing|shanghai|shenzhen|guangzhou|hangzhou|"
                     r"chengdu|wuhan|nanjing|suzhou|tianjin|中国|北京|上海|深圳|广州|杭州|成都|南京|武汉", re.I),
}
MAX_BYTES = 3_000_000


def get_json(url):
    req = Request(url, headers={"Accept": "application/json",
                                 "User-Agent": "JobResourcesAPIOnlyDiscovery/1.0"})
    with urlopen(req, timeout=18) as response:
        raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("API response exceeds size bound")
    return json.loads(raw)


def page_url(market, query, *, page=1, cursor=None, limit=50):
    params = {"q": query, "location": MARKETS[market], "limit": limit}
    if cursor:
        params["after"] = cursor
    else:
        params["page"] = page
    return BASE + "?" + urlencode(params)


def normalize(row, market):
    if not isinstance(row, dict):
        return None
    title = str(row.get("title") or "").strip()
    loc = str(row.get("location") or "").strip()
    company = row.get("company") or {}
    name = (company.get("name") if isinstance(company, dict) else company)
    apply = str(row.get("applyUrl") or "").strip()
    if not (title and name and TITLE.search(title) and REGIONS[market].search(loc)):
        return None
    # An aggregator's claim of a direct route is not enough: only a strict
    # verified ATS URL shape is admitted. MCF and untrusted hosts fail closed.
    exact_url = canonical(apply, market)
    if not exact_url:
        return None
    if str(row.get("employmentType") or "").lower() in ("contract", "internship", "part_time"):
        # Research exceptions are determined by Scouts, so preserve research.
        if not re.search(r"\bresearch\b|研究", title, re.I):
            return None
    uid = str(row.get("id") or row.get("slug") or "").strip()
    if not uid:
        return None
    return {
        "market": market, "ats": "public-api", "company": str(name)[:150],
        "title": title[:180], "job_id": uid[:128],
        "key": "activevacancies|" + uid[:128],
        "url": exact_url, "location": loc[:150],
        "source": f"activevacancies:public-api:{market}",
        "source_listing_url": str(row.get("url") or "")[:300],
        "evidence": "listing_only", "lane": "AI",
        "triage_priority": "MEDIUM", "description_excerpt": "",
    }


def collect(market, *, fetch=get_json, max_pages=2):
    """Scan named query windows; explicit truncation/failures, no invented zero."""
    result = {"market": market, "provider": "ActiveVacancies",
              "queries": [], "errors": [], "jobs": [],
              "coverage": "UNAVAILABLE"}
    jobs = {}
    queries = QUERIES + (CN_EXTRA if market == "CN" else ())
    successes = 0
    for query in queries:
        cursor, previous_page_ids = None, None
        read, truncated = 0, False
        for page in range(1, max_pages + 1):
            try:
                payload = fetch(page_url(market, query, page=page, cursor=cursor))
                if not isinstance(payload, dict) or payload.get("success") is not True:
                    raise ValueError("API success envelope missing")
                data = payload.get("data")
                pager = payload.get("pagination")
                if not isinstance(data, list) or not isinstance(pager, dict) or not isinstance(pager.get("hasNextPage"), bool):
                    raise ValueError("API data/pagination contract changed")
                ids = [str(v.get("id")) for v in data if isinstance(v, dict)]
                if ids and ids == previous_page_ids:
                    raise ValueError("repeated pagination page")
                previous_page_ids = ids
                successes += 1
                read += len(data)
                for raw in data:
                    entry = normalize(raw, market)
                    if entry:
                        jobs[entry["url"]] = entry
                more = pager["hasNextPage"]
                cursor = pager.get("nextCursor") or None
                if not more:
                    break
                if page == max_pages:
                    truncated = True
            except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
                result["errors"].append(f"{query}:page{page}:{type(exc).__name__}: {str(exc)[:110]}")
                truncated = True
                break
        result["queries"].append({"query": query, "rows": read, "truncated": truncated})
    result["jobs"] = sorted(jobs.values(), key=lambda x: (x["company"].lower(), x["url"]))
    result["coverage"] = ("PARTIAL" if result["errors"] or any(q["truncated"] for q in result["queries"])
                          else "COMPLETE") if successes else "UNAVAILABLE"
    return result


def run(out_dir, *, fetch=get_json, max_pages=2):
    out_dir.mkdir(parents=True, exist_ok=True)
    health = {}
    for market in MARKETS:
        result = collect(market, fetch=fetch, max_pages=max_pages)
        health[market] = {key: result[key] for key in ("provider", "coverage", "queries", "errors")}
        health[market]["accepted_exact_ats_urls"] = len(result["jobs"])
        # Exactly one disposable snapshot/market for the unified existing intake.
        (out_dir / f"{market}.json").write_text(
            json.dumps({"market": market, "jobs": result["jobs"]}, indent=2) + "\n")
        print(f"API {market}: {health[market]['coverage']} "
              f"trusted employer URLs={len(result['jobs'])} "
              f"query failures={len(result['errors'])} "
              f"first_error={result['errors'][:1]}")
    (out_dir / "health.json").write_text(json.dumps(health, indent=2) + "\n")
    if all(health[m]["coverage"] == "UNAVAILABLE" for m in MARKETS):
        raise RuntimeError("All API markets unavailable; NOT a zero-job result")
    return health


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--max-pages", type=int, choices=(1, 2, 3), default=2)
    args = parser.parse_args()
    run(args.out_dir, max_pages=args.max_pages)


if __name__ == "__main__":
    main()
