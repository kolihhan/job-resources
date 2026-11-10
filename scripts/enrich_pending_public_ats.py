#!/usr/bin/env python3
"""Bounded first-party Ashby/Greenhouse JD enrichment of EXISTING Pending queues.

Only public GET APIs, no scraping or employer interaction. A published employer
description is an input to human/Scout fit review, never an APPLY decision.
Unknown/failed/mismatched evidence leaves Pending unchanged.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from platform_index_queue import MARKETS, atomic_write, validate_state

UUID = re.compile(r"^[a-f0-9]{8}(?:-[a-f0-9]{4}){3}-[a-f0-9]{12}$", re.I)
BOARD = re.compile(r"^[A-Za-z0-9_.-]{2,80}$")
GREENHOUSE = re.compile(r"^/([A-Za-z0-9_-]{2,80})/jobs/(\d{5,12})/?$")
MAX_BYTES = 4_000_000
MAX_JD = 24_000
MARKET_HINT = {
    "SG": re.compile(r"\bsingapore\b|新加坡", re.I),
    "MY": re.compile(r"\bmalaysia\b|\bkuala lumpur\b|\bpenang\b|\bselangor\b|\bpetaling jaya\b|\bjohor\b|\bcyberjaya\b|马来西亚|槟城", re.I),
    "CN": re.compile(r"\bchina\b|\bshanghai\b|\bbeijing\b|\bshenzhen\b|\bguangzhou\b|\bhangzhou\b|\bchengdu\b|\bwuxi\b|\bnanjing\b|\bwuhan\b|中国|上海|北京|深圳|广州|杭州|成都|无锡|南京|武汉", re.I),
}


def source_of(url):
    """Allowlist-only endpoint construction, never fetch arbitrary queue URLs."""
    p = urlsplit(str(url or ""))
    if p.scheme != "https" or p.username or p.password or p.port not in (None, 443):
        return None
    if p.hostname == "jobs.ashbyhq.com":
        pieces = p.path.strip("/").split("/")
        if len(pieces) == 2 and BOARD.fullmatch(pieces[0]) and UUID.fullmatch(pieces[1]):
            return ("ashby", pieces[0], pieces[1].lower())
    if p.hostname in ("job-boards.greenhouse.io", "job-boards.eu.greenhouse.io"):
        match = GREENHOUSE.fullmatch(p.path)
        if match:
            return ("greenhouse", match.group(1), match.group(2))
    return None


def api_url(provider, board):
    if provider == "ashby":
        return f"https://api.ashbyhq.com/posting-api/job-board/{board}?includeCompensation=false"
    if provider == "greenhouse":
        return f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs?content=true"
    raise ValueError("unapproved provider")


def fetch_json(url):
    req = Request(url, headers={"Accept": "application/json",
                                "User-Agent": "JobResourcesOfficialATSReview/1.0"})
    with urlopen(req, timeout=12) as resp:
        if resp.status != 200:
            raise ValueError(f"HTTP {resp.status}")
        payload = resp.read(MAX_BYTES + 1)
    if len(payload) > MAX_BYTES:
        raise ValueError("oversized public ATS response")
    data = json.loads(payload.decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("jobs"), list):
        raise ValueError("missing published jobs list")
    return data


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(value):
    if not isinstance(value, str):
        return ""
    text = unescape(unescape(value))
    if "<" in text and ">" in text:
        parser = PlainText()
        parser.feed(text)
        text = " ".join(parser.parts)
    return " ".join(text.split())


def normal_title(s):
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", str(s or "").casefold())


def location_text(job):
    loc = job.get("location")
    parts = [loc if isinstance(loc, str) else loc.get("name", "") if isinstance(loc, dict) else ""]
    addr = job.get("address")
    if isinstance(addr, dict):
        p = addr.get("postalAddress") if isinstance(addr.get("postalAddress"), dict) else addr
        parts.extend(str(p.get(k) or "") for k in ("addressCountry", "addressLocality", "addressRegion"))
    for alt in job.get("secondaryLocations") or []:
        if isinstance(alt, dict):
            parts.append(str(alt.get("location") or ""))
            a = alt.get("address") or {}
            if isinstance(a, dict):
                parts.extend(str(a.get(k) or "") for k in ("addressCountry", "addressLocality"))
    return " ".join(parts)


def exact_match(job, row, provider, market):
    if not isinstance(job, dict) or normal_title(job.get("title")) != normal_title(row.get("title")):
        return False
    if not MARKET_HINT[market].search(location_text(job)):
        return False  # Unlocated/remote is not proof of market eligibility.
    if provider == "ashby" and job.get("isListed") is False:
        return False  # Unlisted may be direct-link-only; leave unresolved.
    return True


def enrich_market(state, *, fetch=fetch_json, checked_at=None, max_boards=6, max_rows=30):
    validate_state(state, state["market"])
    if state["market"] not in MARKETS or max_boards < 1 or max_rows < 1:
        raise ValueError("invalid enrichment bounds")
    market = state["market"]
    now = checked_at or datetime.now(timezone.utc).isoformat()
    groups = defaultdict(list)
    for row in state["pending"]:
        review = row.get("consumer_review") or {}
        if review.get("stage") == "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW" and review.get("full_jd_complete"):
            continue
        identified = source_of(row.get("url"))
        if identified:
            provider, board, job_id = identified
            groups[(provider, board)].append((row, job_id))
    counts = {"market": market, "pending": len(state["pending"]), "candidate_boards": len(groups),
              "boards_attempted": 0, "api_errors": 0, "verified_full_jd": 0,
              "unresolved_rows": 0, "skipped_budget": 0, "errors": []}
    remaining = max_rows
    for (provider, board), rows in list(groups.items())[:max_boards]:
        if remaining <= 0:
            break
        chosen = rows[:remaining]
        remaining -= len(chosen)
        counts["boards_attempted"] += 1
        try:
            payload = fetch(api_url(provider, board))
            entries = payload["jobs"]
            indexed = {str(x.get("id") or ""): x for x in entries if isinstance(x, dict)}
        except Exception as exc:
            counts["api_errors"] += 1
            counts["unresolved_rows"] += len(chosen)
            counts["errors"].append(f"{provider}:{board}:{type(exc).__name__}"[:120])
            continue
        for row, job_id in chosen:
            job = indexed.get(job_id)
            if not job or not exact_match(job, row, provider, market):
                counts["unresolved_rows"] += 1
                continue
            text = plain(job.get("descriptionPlain") if provider == "ashby" else job.get("content"))
            if not text and provider == "ashby":
                text = plain(job.get("descriptionHtml"))
            if not 350 <= len(text) <= MAX_JD:
                counts["unresolved_rows"] += 1
                continue
            old = row.get("consumer_review") or {}
            row["consumer_review"] = {
                **old,
                "stage": "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW",
                "source_kind": f"{provider} first-party public published board",
                "checked_at": now,
                "full_jd_complete": True,
                "full_jd_text": text,
                "jd_chars": len(text),
                "jd_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                "source_verified_can_apply": True,
                "review_flags": sorted(set(old.get("review_flags") or []) |
                                       {"HUMAN_FIT_AND_WORK_AUTHORIZATION_REQUIRED"}),
                "employment_time_type": str(job.get("employmentType") or "")[:40],
                "note": "Published exact ATS role and full JD verified; NOT candidate eligibility or submitted application.",
            }
            counts["verified_full_jd"] += 1
    counts["skipped_budget"] = sum(len(x) for x in list(groups.values())[max_boards:]) + max(0, sum(len(x) for x in list(groups.values())[:max_boards]) - max_rows)
    validate_state(state, market)
    return counts


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", type=Path, default=Path("."))
    p.add_argument("--max-boards", type=int, default=6)
    p.add_argument("--max-rows", type=int, default=30)
    p.add_argument("--report", type=Path, required=True)
    args = p.parse_args()
    report = {"mode": "PUBLIC_OFFICIAL_ATS_JD_ENRICHMENT_NOT_FIT_OR_APPLICATION", "markets": {}}
    for market in ("SG", "MY", "CN"):
        path = args.repo / "discovery-state" / f"platform-index-{market.lower()}.json"
        state = json.loads(path.read_text(encoding="utf-8"))
        summary = enrich_market(state, max_boards=args.max_boards, max_rows=args.max_rows)
        report["markets"][market] = summary
        if summary["verified_full_jd"]:
            atomic_write(path, state)
        print(f'{market}: new full JDs {summary["verified_full_jd"]}; '
              f'board attempts {summary["boards_attempted"]}; API errors {summary["api_errors"]}')
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
