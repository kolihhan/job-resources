#!/usr/bin/env python3
"""Import exact public ATS JD evidence produced in freehirefetch.

No ATS API calls, batch sourcing, LLM scoring, applicant data export, or employer
contact. Candidate eligibility, GitHub/Gmail dedupe and APPLY/CHECK remain the
downstream Scouts' responsibility. A public JD is not a submission receipt.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

from platform_index_queue import MARKETS, atomic_write, canonical, validate_state

PUBLIC_SOURCE = "https://raw.githubusercontent.com/kolihhan/freehirefetch/main/feed/ats/jd/"
PART_NAME = re.compile(r"^(?:SG|MY|CN)-[0-9]{3}\.json$")
MAX_BYTES = 2_000_000
MAX_PARTS = 36
MAX_ROWS = 80
MAX_JD_CHARS = 12_000
FRESHNESS = timedelta(hours=48)


def get_public_json(name):
    """Only read explicitly allowlisted public upstream source files."""
    if name != "index.json" and not PART_NAME.fullmatch(name):
        raise ValueError("untrusted freehirefetch source file")
    req = Request(PUBLIC_SOURCE + name, headers={
        "User-Agent": "JobResourcesPublicEvidenceConsumer/2.0",
        "Accept": "application/json",
    })
    with urlopen(req, timeout=18) as response:
        payload = response.read(MAX_BYTES + 1)
        if len(payload) > MAX_BYTES:
            raise ValueError("public evidence shard too large")
    obj = json.loads(payload.decode("utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("public batch schema is not an object")
    return obj


def normal_title(text):
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", str(text or "").casefold())


def parse_date(raw):
    try:
        return datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def enrich_market(state, manifest, fetch=get_public_json, *, now=None, max_parts=MAX_PARTS,
                  max_rows=MAX_ROWS):
    market = state["market"]
    validate_state(state, market)
    if market not in MARKETS or max_parts < 1 or max_rows < 1:
        raise ValueError("invalid public consumer bounds")
    report = {"market": market, "pending": len(state["pending"]),
              "matched_exact": 0, "full_jd_imported": 0, "already_complete": 0,
              "skipped_stale": 0, "unmatched": 0, "partial_or_invalid": 0,
              "parts_fetched": 0, "parts_failed": 0, "source_state": "AVAILABLE"}
    if manifest.get("version") != 2 or not isinstance(manifest.get("jobs"), list):
        report["source_state"] = "INCOMPATIBLE_BATCH_INDEX"
        return report
    utc_now = now or datetime.now(timezone.utc)
    if utc_now.tzinfo is None:
        raise ValueError("now must have timezone")
    keys = {}
    for item in manifest["jobs"]:
        if not isinstance(item, dict) or item.get("market") != market:
            continue
        url = canonical(item.get("url"), market)
        part = item.get("part")
        if not url or not isinstance(part, str) or not part.startswith(market + "-") or not PART_NAME.fullmatch(part):
            continue
        keys.setdefault(url, []).append(item)
    groups = {}
    processed = 0
    for row in state["pending"]:
        if processed >= max_rows:
            break
        review = row.get("consumer_review") or {}
        if review.get("full_jd_complete") is True and review.get("full_jd_text"):
            report["already_complete"] += 1
            continue
        url = canonical(row.get("url"), market)
        options = keys.get(url, [])
        matching = [x for x in options if normal_title(x.get("title")) == normal_title(row.get("title"))]
        if len(matching) != 1:
            report["unmatched"] += 1
            continue
        lookup = matching[0]
        report["matched_exact"] += 1
        processed += 1
        groups.setdefault(lookup["part"], []).append((row, lookup))
    if len(groups) > max_parts:
        allowed = set(list(groups)[:max_parts])
        report["partial_or_invalid"] += sum(len(v) for k, v in groups.items() if k not in allowed)
        groups = {k: v for k, v in groups.items() if k in allowed}
    for part, rows in groups.items():
        try:
            chunk = fetch(part)
            if chunk.get("version") != 1 or not isinstance(chunk.get("jobs"), list):
                raise ValueError("incompatible source JD shard")
            by_key = {x.get("key"): x for x in chunk["jobs"] if isinstance(x, dict)}
            report["parts_fetched"] += 1
        except (OSError, ValueError, TypeError, KeyError, TimeoutError) as exc:
            report["parts_failed"] += 1
            report["partial_or_invalid"] += len(rows)
            continue  # retries preserve Pending: never silently terminal-ACK.
        for row, meta in rows:
            source = by_key.get(meta.get("key"))
            if (not source or source.get("url") != meta.get("url") or
                    normal_title(source.get("title")) != normal_title(row.get("title")) or
                    source.get("description_truncated") is not False or
                    meta.get("description_truncated") is not False):
                report["partial_or_invalid"] += 1
                continue
            description = source.get("description_text")
            if not isinstance(description, str) or not 350 <= len(description) <= MAX_JD_CHARS:
                report["partial_or_invalid"] += 1
                continue
            checked = parse_date(meta.get("checked_at"))
            if (checked is None or checked.tzinfo is None or
                    checked > utc_now + timedelta(minutes=5) or
                    utc_now - checked > FRESHNESS):
                # A stale public listing can help research but cannot justify
                # "verified current" status or newly queue-ready job decisions.
                report["skipped_stale"] += 1
                continue
            prior = row.get("consumer_review") or {}
            row["consumer_review"] = {
                **prior,
                "stage": "FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW",
                "source_kind": "freehirefetch public first-party ATS batch",
                "checked_at": checked.isoformat(),
                "full_jd_complete": True,
                "full_jd_text": description,
                "jd_chars": len(description),
                "jd_sha256": hashlib.sha256(description.encode("utf-8")).hexdigest(),
                "source_verified_can_apply": False,
                "review_flags": sorted(set(prior.get("review_flags") or []) |
                                       {"CHECK_CANDIDATE_FIT_ROUTE_AND_GMAIL_HISTORY"}),
                "note": "Upstream employer-listed full JD; exact role route and applicant eligibility require Scout verification.",
            }
            report["full_jd_imported"] += 1
    validate_state(state, market)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--max-parts", type=int, default=MAX_PARTS)
    parser.add_argument("--max-rows", type=int, default=MAX_ROWS)
    args = parser.parse_args()
    report = {"mode": "PUBLIC_SOURCE_JD_IMPORT_NOT_SCOUT_FIT_OR_APPLY", "markets": {}}
    try:
        manifest = get_public_json("index.json")
    except (OSError, ValueError, TypeError, KeyError, TimeoutError) as exc:
        manifest = {}
        report["upstream_error"] = type(exc).__name__
    for market in ("SG", "MY", "CN"):
        path = args.repo / "discovery-state" / f"platform-index-{market.lower()}.json"
        state = json.loads(path.read_text(encoding="utf-8"))
        result = enrich_market(state, manifest, max_parts=args.max_parts, max_rows=args.max_rows)
        report["markets"][market] = result
        if result["full_jd_imported"]:
            atomic_write(path, state)
        print(f'{market}: imported {result["full_jd_imported"]} JDs from '
              f'{result["parts_fetched"]} public batches, '
              f'stale {result["skipped_stale"]}, unknown {result["unmatched"]}')
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
