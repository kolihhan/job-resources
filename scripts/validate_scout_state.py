#!/usr/bin/env python3
"""Check scout state ownership and basic invariants before/after GitHub writes.

This intentionally validates structure rather than hiring decisions. Run:
    python scripts/validate_scout_state.py
    python scripts/validate_scout_state.py --self-test
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PLATFORMS = {"SG": 5, "CN": 7, "MY": 5}
OWNERS = {"SG": 5, "CN": 6, "MY": 6}
QUERIES = {"SG": 5, "CN": 6, "MY": 5}


def check(kind: str, market: str, data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["not a JSON object"]
    if data.get("market") != market:
        errors.append(f"market must be {market}")
    if not isinstance(data.get("version"), int):
        errors.append("missing integer version")

    if kind == "fresh":
        required = ("platform_cycle", "next_platform_index", "next_owner_bucket",
                    "next_query_bucket", "run_counter")
        for key in required:
            if not isinstance(data.get(key), int) or data[key] < 0:
                errors.append(f"{key}: missing/nonnegative integer required")
        for key, bound in (("next_platform_index", PLATFORMS[market]),
                           ("next_owner_bucket", OWNERS[market]),
                           ("next_query_bucket", QUERIES[market])):
            value = data.get(key)
            if isinstance(value, int) and not 0 <= value < bound:
                errors.append(f"{key}: out of range [0,{bound})")
        if market == "SG":
            value = data.get("next_research_bucket")
            if not isinstance(value, int) or not 0 <= value < 5:
                errors.append("next_research_bucket: invalid SG research index")
        if not isinstance(data.get("last_completed_at"), str):
            errors.append("last_completed_at: missing string")
        if not isinstance(data.get("last_platforms"), list):
            errors.append("last_platforms: missing list")
        if "receipts" in data:
            errors.append("fresh state contains retry receipts (wrong file?)")
        if "last_consumed_candidate_seq" in data:
            errors.append("fresh state contains triage cursor (wrong file?)")

    elif kind == "retry":
        receipts = data.get("receipts")
        if not isinstance(receipts, list):
            errors.append("retry state requires receipts list (wrong file?)")
        else:
            for i, item in enumerate(receipts):
                if not isinstance(item, dict):
                    errors.append(f"receipts[{i}]: not an object")
                    continue
                for field in ("role_key", "reason_code", "next_retry_at"):
                    if not isinstance(item.get(field), str) or not item[field]:
                        errors.append(f"receipts[{i}].{field}: missing string")
                for field in ("candidate_seq", "attempts"):
                    if not isinstance(item.get(field), int) or item[field] < 0:
                        errors.append(f"receipts[{i}].{field}: invalid integer")
        if "next_platform_index" in data or "last_consumed_candidate_seq" in data:
            errors.append("retry state contains fresh/triage fields (wrong file?)")

    elif kind == "triage":
        seq = data.get("last_consumed_candidate_seq")
        if not isinstance(seq, int) or seq < 0:
            errors.append("triage state requires nonnegative consumption cursor")
        if "receipts" in data or "next_platform_index" in data:
            errors.append("triage state contains fresh/retry fields (wrong file?)")
    else:
        errors.append(f"unknown state kind {kind}")
    return errors


def self_test() -> None:
    good_fresh = {"market": "SG", "version": 2, "platform_cycle": 3,
                  "next_platform_index": 1, "next_owner_bucket": 0,
                  "next_query_bucket": 2, "next_research_bucket": 2,
                  "run_counter": 8, "last_completed_at": "2026-11-06T20:00:00+08:00",
                  "last_platforms": ["LinkedIn", "JobStreet"]}
    good_retry = {"market": "SG", "version": 1, "receipts": [
        {"role_key": "freehire:example", "reason_code": "retry",
         "candidate_seq": 3, "attempts": 1, "next_retry_at": "2026-11-07"}]}
    good_triage = {"market": "SG", "version": 1, "last_consumed_candidate_seq": 3}
    assert not check("fresh", "SG", good_fresh)
    assert not check("retry", "SG", good_retry)
    assert not check("triage", "SG", good_triage)
    assert check("fresh", "SG", good_retry), "swapped fresh/retry must fail"
    assert check("retry", "SG", good_fresh), "swapped retry/fresh must fail"
    assert check("fresh", "SG", {**good_fresh, "next_platform_index": 5})
    assert check("triage", "SG", good_retry)
    print("PASS: valid files accepted; swapped files and bad counters rejected")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--market", choices=("sg", "cn", "my"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0

    failures = []
    for market in ([args.market.upper()] if args.market else PLATFORMS):
        for kind in ("fresh", "retry", "triage"):
            path = args.root / "discovery-state" / f"{kind}-{market.lower()}.json"
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                failures.append(f"{path}: cannot read JSON: {exc}")
                continue
            failures.extend(f"{path}: {msg}" for msg in check(kind, market, data))

    if failures:
        print("FAIL: scout state contract violated")
        for failure in failures:
            print(" -", failure)
        return 1
    print("PASS: fresh/retry/triage state shapes valid for selected markets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
