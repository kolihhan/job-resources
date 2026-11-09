#!/usr/bin/env python3
"""Free, read-only, API-first discovery for SG/MY/CN; no HTML scraping.

FreeHire + AI Dev Jobs return source leads. Only exact employer ATS/native job
URLs enter the EXISTING market queues. No automated fit verdict, Issue or apply.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from platform_index_queue import canonical

MARKETS = {"SG": "Singapore", "MY": "Malaysia", "CN": "China"}
QUERIES = ("AI Engineer", "LLM", "Research Engineer")
CN_EXTRA = ("大模型", "算法工程师")
TITLE = re.compile(
    r"\b(?:AI|ML|LLM|NLP|RAG|agentic|agents?|machine learning|"
    r"applied scientist|research engineer|research assistant|"
    r"research associate|data scientist|retrieval|ranking)\b"
    r"|人工智能|大模型|智能体|算法|机器学习|检索|研究工程师", re.I)
LOCATIONS = {
    "SG": re.compile(r"\bsingapore\b|新加坡", re.I),
    "MY": re.compile(r"\bmalaysia\b|kuala lumpur|petaling jaya|selangor|"
                     r"penang|johor|cyberjaya|putrajaya|bayan lepas|槟城|马来西亚", re.I),
    "CN": re.compile(r"\bchina\b|beijing|shanghai|shenzhen|guangzhou|hangzhou|"
                     r"chengdu|wuhan|nanjing|suzhou|tianjin|中国|北京|上海|深圳|广州|杭州|成都|南京|武汉", re.I),
}
MAX_BYTES = 3_000_000
LIMIT = 50


def get_json(url):
    req = Request(url, headers={"Accept": "application/json",
                                 "User-Agent": "JobResourcesAPIOnlyDiscovery/1.0"})
    with urlopen(req, timeout=18) as response:
        raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("API response exceeds size bound")
    return json.loads(raw)


def canonical_apply(url, market):
    """Strip an exact Ashby application suffix, not arbitrary URL paths."""
    p = urlsplit(str(url or "").strip())
    if p.scheme != "https" or not p.hostname or p.username or p.password:
        return None
    if p.hostname == "jobs.ashbyhq.com" and p.path.endswith("/application"):
        path = p.path[:-len("/application")]
        p = p._replace(path=path, query="", fragment="")
    return canonical(urlunsplit(p), market)


def normalized(title, company, url, market, *, source, key, uid, location, excerpt):
    if not (title and company and uid and TITLE.search(title)):
        return None
    exact = canonical_apply(url, market)
    if not exact:
        return None
    return {
        "market": market, "ats": "external-api",
        "company": str(company)[:150], "title": str(title)[:180],
        "job_id": str(uid)[:128], "key": str(key)[:180],
        "url": exact, "location": str(location or "")[:150],
        "source": source, "source_listing_url": "",
        "evidence": "listing_only", "lane": "AI", "triage_priority": "MEDIUM",
        "description_excerpt": str(excerpt or "")[:240],
    }


def normalize_freehire(row, market):
    if not isinstance(row, dict):
        return None
    countries = row.get("countries") or []
    if isinstance(countries, str):
        countries = [countries]
    codes = {str(c).strip().upper() for c in countries}
    aliases = {"SG": {"SG", "SINGAPORE"},
               "MY": {"MY", "MALAYSIA"},
               "CN": {"CN", "CHINA"}}
    if codes and not (codes & aliases[market]):
        return None
    location = str(row.get("location") or "")
    if not codes and not LOCATIONS[market].search(location):
        return None
    job = normalized(str(row.get("title") or ""),
                     str(row.get("company") or ""), row.get("url"), market,
                     source=f"freehire:public-api:{market}",
                     uid=row.get("public_slug"), key="freehire|"+str(row.get("public_slug") or ""),
                     location=location, excerpt=row.get("description"))
    if job and not str(row.get("public_slug") or "").strip():
        return None
    return job


def normalize_aidevboard(row, market):
    if not isinstance(row, dict):
        return None
    loc = str(row.get("location") or "")
    if not LOCATIONS[market].search(loc):
        return None
    if row.get("job_type") in ("contract", "part-time", "internship"):
        if not re.search(r"\bresearch\b|研究", str(row.get("title") or ""), re.I):
            return None
    uid = str(row.get("id") or "")
    if not uid:
        return None
    job = normalized(str(row.get("title") or ""), str(row.get("company_name") or ""),
                     row.get("apply_url"), market,
                     source=f"aidevboard:public-api:{market}",
                     uid=uid, key="aidevboard|"+uid,
                     location=loc, excerpt=row.get("description"))
    if job:
        job["source_listing_url"] = str(row.get("url") or "")[:300]
    return job


def request_page(provider, market, query, page, fetch):
    if provider == "freehire":
        url = "https://freehire.me/api/v1/jobs/search?" + urlencode({
            "countries": market, "q": query, "limit": LIMIT, "offset": (page-1)*LIMIT,
        })
        payload = fetch(url)
        if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
            raise ValueError("FreeHire data[] missing")
        meta = payload.get("meta") or {}
        if not isinstance(meta, dict) or not isinstance(meta.get("total"), int):
            raise ValueError("FreeHire total missing")
        ignored = meta.get("ignored_params") or []
        if "countries" in str(ignored).lower():
            raise ValueError("FreeHire geography filter ignored")
        total = meta["total"]
        if total < 0:
            raise ValueError("negative total")
        start = (page-1)*LIMIT
        rows = payload["data"]
        if rows and start >= total:
            raise ValueError("FreeHire page outside total")
        # A suspicious short/empty page must not be silently called exhausted.
        if not rows and start < total:
            raise ValueError("FreeHire inconsistent empty page")
        return rows, (start + len(rows) < total), normalize_freehire

    url = "https://aidevboard.com/api/v1/jobs?" + urlencode({
        "q": query, "location": MARKETS[market], "limit": LIMIT, "page": page,
    })
    payload = fetch(url)
    if not isinstance(payload, dict) or not isinstance(payload.get("jobs"), list):
        raise ValueError("AI Dev Jobs jobs[] missing")
    if not isinstance(payload.get("has_next"), bool):
        raise ValueError("AI Dev Jobs has_next missing")
    if payload.get("degraded"):
        raise ValueError("AI Dev Jobs degraded response")
    return payload["jobs"], payload["has_next"], normalize_aidevboard


def collect(market, *, fetch=get_json, max_pages=2):
    if market not in MARKETS or max_pages < 1:
        raise ValueError("unsupported market or page budget")
    jobs = {}
    reports = {}
    queries = QUERIES + (CN_EXTRA if market == "CN" else ())
    for provider in ("freehire", "aidevboard"):
        successful_pages, errors, windows, seen_urls = 0, [], [], set()
        for q in queries:
            rows_seen, truncated = 0, False
            for page in range(1, max_pages+1):
                try:
                    rows, has_next, converter = request_page(provider,market,q,page,fetch)
                    successful_pages += 1
                    rows_seen += len(rows)
                    signatures = set()
                    for row in rows:
                        cand = converter(row,market)
                        if cand:
                            signatures.add(cand["url"])
                            jobs.setdefault(cand["url"], cand)
                            seen_urls.add(cand["url"])
                    if page > 1 and signatures and signatures.issubset(previous_urls):
                        raise ValueError("repeated API page")
                    previous_urls = signatures
                    if not has_next:
                        break
                    if page == max_pages:
                        truncated = True
                except (OSError, ValueError, TypeError, json.JSONDecodeError) as e:
                    errors.append(f"{q}:page{page}:{type(e).__name__}:{str(e)[:110]}")
                    truncated = True
                    # Shared GitHub runner IP might already be throttled.
                    # Do NOT retry 429 across every query window.
                    if isinstance(e, HTTPError) and e.code == 429:
                        windows.append({"q":q,"rows":rows_seen,"truncated":True})
                        break
                    break
            else:
                truncated = True
            if not windows or windows[-1].get("q") != q:
                windows.append({"q":q,"rows":rows_seen,"truncated":truncated})
            if errors and "HTTPError:HTTP Error 429" in errors[-1]:
                break
        reports[provider] = {
            "status": ("UNAVAILABLE" if not successful_pages else
                       "PARTIAL" if errors or any(w["truncated"] for w in windows)
                       else "COMPLETE"),
            "successful_pages": successful_pages, "accepted_exact_urls": len(seen_urls),
            "queries": windows, "errors": errors,
        }
    return {"market":market,"jobs":list(jobs.values()),"providers":reports}


def run(out_dir, *, fetch=get_json, max_pages=2):
    out_dir.mkdir(parents=True, exist_ok=True)
    health = {}
    for market in MARKETS:
        result = collect(market,fetch=fetch,max_pages=max_pages)
        health[market] = result["providers"]
        (out_dir / f"{market}.json").write_text(
            json.dumps({"market":market, "jobs":result["jobs"]},indent=2,ensure_ascii=False)+"\n")
        for provider, stats in result["providers"].items():
            print(f"API {market} {provider}: {stats['status']}, "
                  f"trusted exact employer URLs={stats['accepted_exact_urls']}, "
                  f"successful pages={stats['successful_pages']}, "
                  f"first_error={stats['errors'][:1]}")
    (out_dir / "health.json").write_text(json.dumps(health,indent=2)+"\n")
    if all(health[m][p]["status"] == "UNAVAILABLE"
           for m in MARKETS for p in ("freehire", "aidevboard")):
        raise RuntimeError("All API markets unavailable; NOT a zero-job result")
    return health


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out-dir",type=Path,required=True)
    p.add_argument("--max-pages",type=int,choices=(1,2,3),default=2)
    args=p.parse_args()
    run(args.out_dir,max_pages=args.max_pages)


if __name__=="__main__":
    main()
