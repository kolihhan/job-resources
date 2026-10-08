#!/usr/bin/env python3
"""Fetch a broad SG/CN engineering slice from FreeHire.

Uses only the Python standard library. The public FreeHire search API allows
100 rows/page and offset + limit <= 10000, so the default reaches the API's
maximum deep-page window (100 pages / 10,000 rows) per market.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Callable, Iterable
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_URL = "https://freehire.me/api/v1/jobs/search"
API_MAX_ROWS = 10_000
API_MAX_PAGE_SIZE = 100
DEFAULT_CATEGORIES = (
    "backend",
    "fullstack",
    "data_engineering",
    "ml_ai",
    "ai_engineering",
    "solutions_engineering",
    "devops",
    "sre",
)
HARD_SENIORITY = {"senior", "lead", "staff", "principal", "c_level"}
HARD_COMPANY_TYPES = {"outsource", "outstaff", "agency"}
TITLE_BLOCKERS = (
    "senior ",
    "staff ",
    "lead ",
    "principal ",
    "director ",
    "manager ",
    "head of ",
    "intern",
)


def page_offsets(max_rows: int = API_MAX_ROWS, page_size: int = API_MAX_PAGE_SIZE) -> list[int]:
    if page_size < 1 or page_size > API_MAX_PAGE_SIZE:
        raise ValueError(f"page_size must be 1..{API_MAX_PAGE_SIZE}")
    max_rows = max(0, min(max_rows, API_MAX_ROWS))
    return list(range(0, max_rows, page_size))


def build_params(country: str, offset: int, page_size: int = API_MAX_PAGE_SIZE, open_within_days: int | None = None) -> dict:
    params = {
        "countries": country.upper(),
        "category": ",".join(DEFAULT_CATEGORIES),
        "sort": "created_at",
        "order": "desc",
        "limit": page_size,
        "offset": offset,
    }
    if open_within_days is not None:
        params["open_within_days"] = open_within_days
    return params


def http_fetch(params: dict, timeout: int = 30, retries: int = 2) -> dict:
    url = f"{API_URL}?{urlencode(params)}"
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = Request(url, headers={"User-Agent": "job-resources-freehire/1.0"})
            with urlopen(req, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"FreeHire request failed after {retries + 1} attempts: {last_error}")


def fetch_market(
    fetch_json: Callable[[dict], dict],
    country: str,
    max_rows: int = API_MAX_ROWS,
    page_size: int = API_MAX_PAGE_SIZE,
    open_within_days: int | None = None,
) -> list[dict]:
    jobs: list[dict] = []
    for offset in page_offsets(max_rows=max_rows, page_size=page_size):
        payload = fetch_json(build_params(country, offset, page_size, open_within_days))
        meta = payload.get("meta") or {}
        ignored = meta.get("ignored_params") or []
        if ignored:
            raise RuntimeError(f"FreeHire ignored requested params: {', '.join(map(str, ignored))}")

        page = payload.get("data") or []
        jobs.extend(page)

        total = int(meta.get("total", len(jobs)))
        if not page or len(jobs) >= total or len(jobs) >= max_rows:
            break
    return jobs[:max_rows]


def _reject_reason(job: dict) -> str | None:
    title = (job.get("title") or "").strip().lower()
    enrichment = job.get("enrichment") or {}

    if any(blocker in title for blocker in TITLE_BLOCKERS):
        return "title_seniority_or_intern"
    if enrichment.get("seniority") in HARD_SENIORITY:
        return "seniority"
    if enrichment.get("employment_type") == "internship":
        return "internship"
    if enrichment.get("company_type") in HARD_COMPANY_TYPES:
        return "company_type"

    years = enrichment.get("experience_years_min")
    if isinstance(years, (int, float)) and years >= 5:
        return "experience_5_plus"
    return None


def cheap_screen(jobs: Iterable[dict]) -> tuple[list[dict], list[dict]]:
    kept: list[dict] = []
    rejected: list[dict] = []
    for job in jobs:
        reason = _reject_reason(job)
        if reason is None:
            kept.append(job)
        else:
            copy = dict(job)
            copy["cheap_reject_reason"] = reason
            rejected.append(copy)
    return kept, rejected


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def run_country(country: str, output_dir: Path, max_rows: int, open_within_days: int | None) -> dict:
    fetcher = lambda params: http_fetch(params)
    raw = fetch_market(fetcher, country=country, max_rows=max_rows, open_within_days=open_within_days)
    kept, rejected = cheap_screen(raw)

    write_jsonl(output_dir / f"freehire-{country.lower()}-raw.jsonl", raw)
    write_jsonl(output_dir / f"freehire-{country.lower()}-screened.jsonl", kept)
    write_jsonl(output_dir / f"freehire-{country.lower()}-rejected.jsonl", rejected)

    summary = {
        "country": country,
        "raw": len(raw),
        "screened": len(kept),
        "rejected": len(rejected),
        "max_rows": max_rows,
        "open_within_days": open_within_days,
    }
    (output_dir / f"freehire-{country.lower()}-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch FreeHire SG/CN jobs up to the API's 10,000-row window per market.")
    parser.add_argument("--country", action="append", choices=["SG", "CN"], help="Market to fetch; repeatable. Defaults to both.")
    parser.add_argument("--output-dir", default=".freehire", help="Output directory (default: .freehire)")
    parser.add_argument("--max-rows", type=int, default=API_MAX_ROWS, help="Rows per market, capped at 10000 (default: 10000)")
    parser.add_argument("--open-within-days", type=int, default=None, help="Optional FreeHire first-seen freshness window for incremental runs")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    countries = args.country or ["SG", "CN"]
    max_rows = max(1, min(args.max_rows, API_MAX_ROWS))
    output_dir = Path(args.output_dir)

    for country in countries:
        summary = run_country(country, output_dir, max_rows, args.open_within_days)
        print(json.dumps(summary, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    sys.exit(main())
