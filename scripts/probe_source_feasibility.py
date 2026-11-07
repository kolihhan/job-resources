#!/usr/bin/env python3
"""Read-only, bounded GitHub runner feasibility probe for public ATS job feeds.

No credentials, login bypass, applications, or employer contact.
Outputs public job metadata only; runtime transport and target market matching
are separate from job eligibility/liveness/visa verification.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time
import urllib.error
import urllib.request

SOURCES = [
    {"id": "lever_binance", "kind": "lever", "slug": "binance", "markets": ["SG", "MY", "CN"]},
    {"id": "greenhouse_stripe", "kind": "greenhouse", "slug": "stripe", "markets": ["SG"]},
    {"id": "ashby_ramp", "kind": "ashby", "slug": "ramp", "markets": ["SG"]},
    {"id": "smartrecruiters_visa", "kind": "smartrecruiters", "slug": "Visa", "markets": ["SG", "MY"]},
    {"id": "smartrecruiters_bosch", "kind": "smartrecruiters", "slug": "Bosch", "markets": ["MY", "CN"]},
]
MARKET_TERMS = {
    "SG": ("singapore",),
    "MY": ("malaysia", "kuala lumpur", "penang", "selangor", "cyberjaya", "johor", "petaling jaya", "puchong", "subang", "georgetown", "bayan lepas"),
    "CN": ("china", "shenzhen", "beijing", "shanghai", "hangzhou", "guangzhou", "chengdu", "suzhou", "nanjing", "北京", "上海", "深圳", "杭州", "广州", "成都", "苏州", "南京"),
}
MAX_BYTES = 7_000_000
PAGE_SIZE = 50


def list_url(kind: str, slug: str, page: int = 0) -> str:
    if kind == "lever":
        return f"https://api.lever.co/v0/postings/{slug}?mode=json&limit={PAGE_SIZE}&skip={page * PAGE_SIZE}"
    if kind == "greenhouse":
        return f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
    if kind == "ashby":
        return f"https://api.ashbyhq.com/posting-api/job-board/{slug}"
    if kind == "smartrecruiters":
        return f"https://api.smartrecruiters.com/v1/companies/{slug}/postings?limit={PAGE_SIZE}&offset={page * PAGE_SIZE}"
    raise ValueError(f"Unknown kind: {kind}")


def detail_url(kind: str, slug: str, job_id: str) -> str | None:
    if kind == "lever":
        return f"https://api.lever.co/v0/postings/{slug}/{job_id}?mode=json"
    if kind == "greenhouse":
        return f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs/{job_id}"
    if kind == "smartrecruiters":
        return f"https://api.smartrecruiters.com/v1/companies/{slug}/postings/{job_id}"
    return None  # Ashby can include full descriptions in the list feed.


def parse_page(kind: str, payload: object) -> tuple[list[dict], int | None]:
    if kind == "lever":
        if not isinstance(payload, list):
            raise ValueError("Lever list is not JSON array")
        rows = payload
        total = None
    else:
        if not isinstance(payload, dict):
            raise ValueError("API root not JSON object")
        field = {"greenhouse": "jobs", "ashby": "jobs", "smartrecruiters": "content"}[kind]
        rows = payload.get(field)
        if not isinstance(rows, list):
            raise ValueError(f"{kind} has no {field} array")
        total = payload.get("totalFound") if kind == "smartrecruiters" else None
        if total is not None and (not isinstance(total, int) or total < 0):
            total = None
    out = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        j_id = r.get("id")
        title = r.get("text") if kind == "lever" else (r.get("name") or r.get("title")) if kind == "smartrecruiters" else r.get("title")
        if not j_id or not isinstance(title, str) or not title.strip():
            continue
        if kind == "lever":
            loc = (r.get("categories") or {}).get("location", "")
            url = r.get("hostedUrl", "")
        elif kind == "greenhouse":
            loc = (r.get("location") or {}).get("name", "")
            url = r.get("absolute_url", "")
        elif kind == "ashby":
            loc = r.get("location", "")
            url = r.get("jobUrl", "")
        else:
            loc = (r.get("location") or {}).get("city", "")
            country = (r.get("location") or {}).get("country", "")
            loc = f"{loc} {country}".strip()
            url = f"https://jobs.smartrecruiters.com/{(r.get('company') or {}).get('identifier', '')}/{j_id}"
        if not isinstance(loc, str):
            loc = str(loc or "")
        if not isinstance(url, str):
            url = ""
        out.append({"id": str(j_id), "title": title[:160], "location": loc[:160], "url": url[:500],
                    "inline_jd": bool(r.get("descriptionHtml") or r.get("descriptionPlain"))})
    return out, total


def market_counts(rows: list[dict]) -> dict[str, int]:
    return {market: sum(any(term in r["location"].lower() for term in terms) for r in rows)
            for market, terms in MARKET_TERMS.items()}


def get_json(url: str, *, timeout: int = 14) -> object:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; PublicJobsFeasibility/1.0)", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status != 200:
            raise ValueError(f"HTTP {response.status}")
        mime = response.headers.get("Content-Type", "").lower()
        data = response.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError("response exceeds 7 MB bounded limit")
        if "json" not in mime and data.lstrip().startswith(b"<"):
            raise ValueError("HTML/challenge rather than JSON")
    return json.loads(data.decode("utf-8"))


def failure_kind(error: Exception) -> str:
    if isinstance(error, urllib.error.HTTPError):
        return ("BLOCKED_HTTP" if error.code in (401, 403, 429) else
                "NOT_FOUND" if error.code == 404 else "HTTP_ERROR")
    if isinstance(error, (urllib.error.URLError, TimeoutError)):
        return "NETWORK_ERROR"
    if isinstance(error, (json.JSONDecodeError, UnicodeDecodeError)):
        return "INVALID_JSON"
    return "INVALID_RESPONSE"


def probe(spec: dict, fetch=get_json) -> dict:
    kind, slug = spec["kind"], spec["slug"]
    outcome = {"id": spec["id"], "kind": kind, "slug": slug,
               "target_markets": spec["markets"], "state": "UNTESTED",
               "pages": [], "list_unique_jobs": 0, "market_matches": {},
               "detail": "NOT_TESTED", "pagination": "NOT_TESTED", "samples": []}
    try:
        payload = fetch(list_url(kind, slug, 0))
        rows, total = parse_page(kind, payload)
        outcome["pages"].append({"page": 1, "unique_ids": len({r["id"] for r in rows}), "total_reported": total})
        if not rows:
            outcome.update(state="EMPTY_OR_UNPARSABLE", pagination="UNKNOWN")
            return outcome
        all_rows = rows[:]
        if kind in ("lever", "smartrecruiters"):
            should_page = len(rows) >= PAGE_SIZE or (total is not None and total > len(rows))
            if should_page:
                # Two pages is a feasibility check, not a claim of full-board exhaustion.
                time.sleep(0.35)
                next_rows, second_total = parse_page(kind, fetch(list_url(kind, slug, 1)))
                new_ids = {r["id"] for r in next_rows} - {r["id"] for r in rows}
                outcome["pages"].append({"page": 2, "unique_ids": len({r["id"] for r in next_rows}),
                                         "new_unique_ids": len(new_ids), "total_reported": second_total})
                outcome["pagination"] = "PAGE_2_DISTINCT" if new_ids else "PAGE_2_EMPTY_OR_DUPLICATE"
                all_rows += next_rows
            else:
                outcome["pagination"] = "FIRST_PAGE_BELOW_LIMIT"
        else:
            outcome["pagination"] = "WHOLE_BOARD_ENDPOINT"
        unique = {r["id"]: r for r in all_rows}
        outcome["list_unique_jobs"] = len(unique)
        outcome["market_matches"] = market_counts(list(unique.values()))
        outcome["samples"] = [{k: r[k] for k in ("id", "title", "location", "url")}
                              for r in list(unique.values())[:5]]
        exemplar = next(iter(unique.values()))
        if kind == "ashby":
            outcome["detail"] = "INLINE_DESCRIPTION" if exemplar["inline_jd"] else "NO_INLINE_DESCRIPTION"
        else:
            url = detail_url(kind, slug, exemplar["id"])
            try:
                detail = fetch(url)
                if isinstance(detail, dict) and detail.get("id") is not None:
                    outcome["detail"] = "DETAIL_JSON_ID_PRESENT"
                elif isinstance(detail, dict) and (detail.get("content") or detail.get("description")):
                    outcome["detail"] = "DETAIL_TEXT_PRESENT"
                else:
                    outcome["detail"] = "DETAIL_SCHEMA_UNVERIFIED"
            except Exception as e:
                outcome["detail"] = f"{failure_kind(e)}"
        outcome["state"] = "LIST_AND_DETAIL" if outcome["detail"] in ("DETAIL_JSON_ID_PRESENT", "DETAIL_TEXT_PRESENT", "INLINE_DESCRIPTION") else "LIST_ONLY"
    except Exception as e:
        outcome["state"] = failure_kind(e)
        outcome["error"] = f"{type(e).__name__}: {str(e)[:180]}"
    return outcome


def liepin_probe(path: Path | None, status_path: Path | None) -> dict:
    if not path or not path.exists():
        explanation = status_path.read_text(encoding="utf-8")[-350:] if status_path and status_path.exists() else "No Liepin output file"
        return {"id": "liepin_cn", "state": "COLLECTOR_FAILED", "error": explanation}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        pages = payload.get("searches")
        jobs = payload.get("jobs")
        if not isinstance(pages, list) or not isinstance(jobs, list):
            raise ValueError("Missing searches or jobs")
        return {"id": "liepin_cn", "state": "LIST_OBTAINED" if jobs else "EMPTY",
                "pages": [{"page": p.get("page"), "count": p.get("count"), "total_pages": p.get("totalPage")} for p in pages],
                "list_unique_jobs": len({str(j.get("sourceId")) for j in jobs if j.get("sourceId")}),
                "samples": [{"id": str(j.get("sourceId")), "title": j.get("title"), "location": j.get("location"), "url": j.get("url")} for j in jobs[:5]],
                "detail": "NOT_TESTED"}
    except Exception as e:
        return {"id": "liepin_cn", "state": "INVALID_RESULT", "error": str(e)[:180]}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--liepin-json", type=Path)
    p.add_argument("--liepin-status", type=Path)
    args = p.parse_args()
    result = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "runner": "github-actions", "scope": "bounded public read-only feasibility, not eligible-job validation",
              "sources": []}
    for spec in SOURCES:
        outcome = probe(spec)
        result["sources"].append(outcome)
        print(json.dumps({"id": outcome["id"], "state": outcome["state"], "list_unique_jobs": outcome["list_unique_jobs"],
                          "pagination": outcome["pagination"], "detail": outcome["detail"], "market_matches": outcome["market_matches"]}))
        time.sleep(0.5)
    result["sources"].append(liepin_probe(args.liepin_json, args.liepin_status))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Written {args.output} (no application actions)")


if __name__ == "__main__":
    main()
