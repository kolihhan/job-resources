#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile

import build_known_role_index as known_index

_MARKETS = ("SG", "CN", "MY")


def _candidate_weak_key(candidate: dict) -> str | None:
    company = known_index._norm_text(candidate.get("company"))
    title = known_index._norm_text(candidate.get("title"))
    if not company or not title:
        return None
    return f"{company}|{title}"


def _exact_match(candidate: dict, strong_urls: set[str], freehire_slugs: set[str]) -> tuple[bool, str | None]:
    slug = str(candidate.get("public_slug") or "").strip().lower()
    if slug and slug in freehire_slugs:
        return True, "freehire_slug"

    for field in ("source_url", "freehire_url"):
        normalized = known_index.normalize_url(str(candidate.get(field) or ""))
        if normalized and normalized in strong_urls:
            return True, field
    return False, None


def filter_coldstart(coldstart: dict, known: dict, generated_at: str) -> dict:
    strong = known.get("strong") if isinstance(known.get("strong"), dict) else {}
    weak = known.get("weak") if isinstance(known.get("weak"), dict) else {}
    strong_urls = {known_index.normalize_url(url) for url in strong.get("urls", []) if known_index.normalize_url(url)}
    freehire_slugs = {str(slug).strip().lower() for slug in strong.get("freehire_slugs", []) if str(slug).strip()}
    weak_company_title = {str(key) for key in weak.get("company_title", []) if str(key)}

    market_stats = {
        market: {"source": 0, "known_exact": 0, "suspected_known": 0, "unseen": 0}
        for market in _MARKETS
    }
    kept: list[dict] = []
    known_exact_count = 0
    suspected_known_count = 0
    unseen_count = 0

    candidates = coldstart.get("candidates") if isinstance(coldstart.get("candidates"), list) else []
    for source_candidate in candidates:
        if not isinstance(source_candidate, dict):
            continue
        candidate = dict(source_candidate)
        market = str(candidate.get("market") or "").upper()
        if market not in market_stats:
            market_stats[market] = {"source": 0, "known_exact": 0, "suspected_known": 0, "unseen": 0}
        market_stats[market]["source"] += 1

        exact, exact_basis = _exact_match(candidate, strong_urls, freehire_slugs)
        if exact:
            known_exact_count += 1
            market_stats[market]["known_exact"] += 1
            continue

        weak_key = _candidate_weak_key(candidate)
        if weak_key and weak_key in weak_company_title:
            candidate["known_status"] = "suspected_known"
            candidate["known_match_basis"] = "company_title"
            suspected_known_count += 1
            market_stats[market]["suspected_known"] += 1
        else:
            candidate["known_status"] = "unseen"
            candidate["known_match_basis"] = None
            unseen_count += 1
            market_stats[market]["unseen"] += 1
        kept.append(candidate)

    source_count = len([candidate for candidate in candidates if isinstance(candidate, dict)])
    return {
        "version": 1,
        "generated_at": generated_at,
        "source_generated_at": coldstart.get("generated_at"),
        "source_count": source_count,
        "known_exact_count": known_exact_count,
        "suspected_known_count": suspected_known_count,
        "unseen_count": unseen_count,
        "review_count": len(kept),
        "markets": market_stats,
        "candidates": kept,
    }


def _atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coldstart", required=True)
    parser.add_argument("--known", default="discovery-state/known-role-index.json")
    parser.add_argument("--output", default="discovery-state/freehire-coldstart.json")
    args = parser.parse_args(argv)

    coldstart = json.loads(Path(args.coldstart).read_text(encoding="utf-8"))
    known = json.loads(Path(args.known).read_text(encoding="utf-8"))
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    result = filter_coldstart(coldstart, known, generated_at=generated_at)
    _atomic_write_json(Path(args.output), result)
    print(
        json.dumps(
            {
                "source_count": result["source_count"],
                "known_exact_count": result["known_exact_count"],
                "suspected_known_count": result["suspected_known_count"],
                "unseen_count": result["unseen_count"],
                "review_count": result["review_count"],
                "markets": result["markets"],
                "output": args.output,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
