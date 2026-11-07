#!/usr/bin/env python3
"""Read-only hiring-board access and pagination feasibility on a GitHub runner.

A successful HTTP request is not a successful source scan. Counts are limited
to concrete links to job detail pages found in returned HTML; embedded JSON
without a detail URL, advertised totals and search snippets do not count.

No login/cookies/CAPTCHA bypass, employer contact, or application actions.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlencode
from urllib.request import Request, urlopen

MAX_BYTES = 2_500_000
TIMEOUT = 11

PLATFORMS = [
    {"id": "SG_LINKEDIN", "market": "SG", "host": "linkedin.com",
     "urls": ["https://sg.linkedin.com/jobs/ai-engineer-jobs", "https://sg.linkedin.com/jobs/ai-engineer-jobs?start=25"]},
    {"id": "SG_JOBSTREET", "market": "SG", "host": "jobstreet.com",
     "urls": ["https://sg.jobstreet.com/ai-engineer-jobs?page=1", "https://sg.jobstreet.com/ai-engineer-jobs?page=2"]},
    {"id": "SG_INDEED", "market": "SG", "host": "indeed.com",
     "urls": ["https://sg.indeed.com/jobs?q=AI+Engineer&l=Singapore&start=0", "https://sg.indeed.com/jobs?q=AI+Engineer&l=Singapore&start=10"]},
    {"id": "SG_MCF", "market": "SG", "host": "mycareersfuture.gov.sg",
     "urls": ["https://www.mycareersfuture.gov.sg/search?search=AI%20Engineer&sortBy=new_posting_date&page=0", "https://www.mycareersfuture.gov.sg/search?search=AI%20Engineer&sortBy=new_posting_date&page=1"]},
    {"id": "MY_LINKEDIN", "market": "MY", "host": "linkedin.com",
     "urls": ["https://my.linkedin.com/jobs/ai-engineer-jobs", "https://my.linkedin.com/jobs/ai-engineer-jobs?start=25"]},
    {"id": "MY_JOBSTREET", "market": "MY", "host": "jobstreet.com",
     "urls": ["https://my.jobstreet.com/AI-engineer-jobs?page=1", "https://my.jobstreet.com/AI-engineer-jobs?page=2"]},
    {"id": "MY_INDEED", "market": "MY", "host": "indeed.com",
     "urls": ["https://malaysia.indeed.com/jobs?q=AI+Engineer&start=0", "https://malaysia.indeed.com/jobs?q=AI+Engineer&start=10"]},
    {"id": "MY_HIREDLY", "market": "MY", "host": "hiredly.com",
     "urls": ["https://my.hiredly.com/jobs?search=AI%20Engineer&page=1", "https://my.hiredly.com/jobs?search=AI%20Engineer&page=2"]},
    {"id": "CN_BOSS", "market": "CN", "host": "zhipin.com",
     "urls": ["https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%A8%A1%E5%9E%8B&city=101280600&page=1",
              "https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%A8%A1%E5%9E%8B&city=101280600&page=2"]},
    {"id": "CN_NOWCODER", "market": "CN", "host": "nowcoder.com",
     "urls": ["https://www.nowcoder.com/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B&page=1",
              "https://www.nowcoder.com/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B&page=2"]},
    {"id": "CN_ZHAOPIN", "market": "CN", "host": "zhaopin.com",
     "urls": ["https://sou.zhaopin.com/?kw=%E5%A4%A7%E6%A8%A1%E5%9E%8B&page=1",
              "https://sou.zhaopin.com/?kw=%E5%A4%A7%E6%A8%A1%E5%9E%8B&page=2"]},
    {"id": "CN_51JOB", "market": "CN", "host": "51job.com",
     "urls": ["https://we.51job.com/pc/search?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B&pageNum=1",
              "https://we.51job.com/pc/search?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B&pageNum=2"]},
]

PATTERNS = {
    "linkedin.com": re.compile(r"/jobs/view/(?:[^/?#]*-)?\d{7,}(?:/|\?|$)", re.I),
    "jobstreet.com": re.compile(r"/job/\d{6,}(?:/|\?|$)", re.I),
    "indeed.com": re.compile(r"(?:/viewjob\?|/rc/clk\?|/pagead/clk\?|[?&]jk=[a-z0-9]{12,})", re.I),
    "mycareersfuture.gov.sg": re.compile(r"/job/(?:[^/?#]+/)*[^/?#]+-[a-f0-9]{20,}", re.I),
    "hiredly.com": re.compile(r"/jobs/(?:[^/?#]+/)?[a-z0-9][^/?#]*", re.I),
    "zhipin.com": re.compile(r"/job_detail/[^/?#]+", re.I),
    "nowcoder.com": re.compile(r"/jobs/detail/[^/?#]+", re.I),
    "zhaopin.com": re.compile(r"/jobdetail/[^/?#]+|/jobs/[^/?#]+", re.I),
    "51job.com": re.compile(r"/job/\d{6,}", re.I),
}

class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []
        self.title = ""
        self._title = False
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self._title = True
        if tag == "a":
            for key, value in attrs:
                if key == "href" and value:
                    self.hrefs.append(value)
                    break
    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._title = False
    def handle_data(self, data: str) -> None:
        if self._title:
            self.title += data[:300]


def recognized_job_links(html: str, base_url: str, expected_host: str) -> tuple[list[str], str]:
    p = LinkParser()
    p.feed(html)
    refs: set[str] = set()
    for href in p.hrefs:
        full = urljoin(base_url, href)
        parsed = urlsplit(full)
        if not (parsed.netloc == expected_host or parsed.netloc.endswith("." + expected_host)):
            continue
        if PATTERNS[expected_host].search(parsed.path + ("?" + parsed.query if parsed.query else "")):
            # Query may carry the Indeed identity. Else ignore tracking parameters.
            key = parsed.path
            if expected_host == "indeed.com":
                m = re.search(r"[?&]jk=([a-zA-Z0-9]{12,})", "?" + parsed.query)
                if m:
                    key = "indeed:jk:" + m.group(1)
                elif "/viewjob" in parsed.path or "/rc/clk" in parsed.path:
                    continue  # Link without a stable job key is not proof of identity.
            refs.add(key)
    return sorted(refs), p.title.strip()[:160]


def fetch_html(url: str) -> dict:
    start = time.monotonic()
    req = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; PublicPlatformFeasibility/1.0)",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.8",
    })
    try:
        with urlopen(req, timeout=TIMEOUT) as response:
            data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                return {"state": "OVERSIZED_RESPONSE", "http_status": response.status, "elapsed_ms": int((time.monotonic()-start)*1000)}
            ct = response.headers.get("Content-Type", "")
            if "html" not in ct.lower():
                return {"state": "NON_HTML_RESPONSE", "http_status": response.status, "content_type": ct[:90], "elapsed_ms": int((time.monotonic()-start)*1000)}
            body = data.decode("utf-8", "replace")
            lower = body[:100_000].lower()
            challenge = any(term in lower for term in ("captcha", "verify you are human", "cf-chl", "unusual traffic", "access denied"))
            return {"state": "CHALLENGE_HTML" if challenge else "HTML_FETCHED",
                    "http_status": response.status, "html_bytes": len(data),
                    "elapsed_ms": int((time.monotonic()-start)*1000),
                    "html": body, "final_url": response.url}
    except HTTPError as exc:
        return {"state": "BLOCKED_HTTP" if exc.code in (401,403,429) else "HTTP_ERROR",
                "http_status": exc.code, "elapsed_ms": int((time.monotonic()-start)*1000)}
    except (URLError, TimeoutError, OSError) as exc:
        return {"state": "NETWORK_ERROR", "error": str(exc)[:120],
                "elapsed_ms": int((time.monotonic()-start)*1000)}


def probe_platform(spec: dict, fetch=fetch_html) -> dict:
    result = {"id": spec["id"], "market": spec["market"], "host": spec["host"],
              "page_probes": [], "all_unique_job_identities": 0,
              "page2_new_identifiable_jobs": 0, "page2_novelty_ratio": 0,
              "query_scope_verified": False, "coverage": "NOT_PROVEN"}
    per_page = []
    for n, url in enumerate(spec["urls"], start=1):
        outcome = fetch(url)
        refs, title = [], ""
        if outcome.get("html") and outcome["state"] == "HTML_FETCHED":
            refs, title = recognized_job_links(outcome["html"], outcome.get("final_url") or url, spec["host"])
        per_page.append(set(refs))
        result["page_probes"].append({
            "page": n, "url": url, "state": outcome["state"],
            "http_status": outcome.get("http_status"), "html_bytes": outcome.get("html_bytes"),
            "elapsed_ms": outcome.get("elapsed_ms"), "title": title,
            "identifiable_job_count": len(refs), "sample_ids": refs[:5],
            "error": outcome.get("error"),
        })
        if n == 1 and outcome["state"] not in ("HTML_FETCHED", "CHALLENGE_HTML"):
            # Still probe page two? No. It would usually amplify blocked requests.
            break
        time.sleep(0.35)
    result["all_unique_job_identities"] = len(set().union(*per_page))
    if len(per_page) == 2:
        result["page2_new_identifiable_jobs"] = len(per_page[1] - per_page[0])
        result["page2_novelty_ratio"] = round(result["page2_new_identifiable_jobs"] / max(1, len(per_page[1])), 3)
    topic_terms = spec.get("topic_terms") or (["大模型", "llm"] if spec["market"] == "CN" else ["ai", "artificial intelligence"])
    result["query_scope_verified"] = any(
        any(term.lower() in p["title"].lower() for term in topic_terms)
        for p in result["page_probes"] if p["state"] == "HTML_FETCHED"
    )
    # A nominal page-2 response that repeats 19/20 IDs, or a generic
    # "popular jobs" page that ignores the query, is NOT a search coverage win.
    if (len(per_page) == 2 and result["query_scope_verified"]
            and result["page2_new_identifiable_jobs"] >= max(2, (len(per_page[1]) + 3) // 4)):
        result["coverage"] = "TWO_PAGES_WITH_DISTINCT_ROLE_IDS"
    elif result["all_unique_job_identities"] > 0:
        result["coverage"] = "ROLE_LINKS_BUT_QUERY_OR_PAGE_2_UNVERIFIED"
    elif any(p["state"] == "BLOCKED_HTTP" for p in result["page_probes"]):
        result["coverage"] = "BLOCKED_FROM_RUNNER"
    else:
        result["coverage"] = "NO_VERIFIED_ROLE_IDS"
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    results = []
    for spec in PLATFORMS:
        item = probe_platform(spec)
        results.append(item)
        print(json.dumps({"source": item["id"], "coverage": item["coverage"],
                          "role_ids": item["all_unique_job_identities"],
                          "page2_new": item["page2_new_identifiable_jobs"],
                          "http": [p["http_status"] for p in item["page_probes"]]}))
        time.sleep(0.5)
    payload = {"generated_at": datetime.now(timezone.utc).isoformat(), "runner": "github-actions",
               "scope": "Native public HTML only; 2 bounded pages per platform; no login or search-index fallback",
               "results": results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
