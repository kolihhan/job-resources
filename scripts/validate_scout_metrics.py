#!/usr/bin/env python3
"""Reject unsupported scout completion claims; do not score job relevance.

New run records use this before appending their daily JSONL entry:
    python scripts/validate_scout_metrics.py --path /tmp/new-scout-record.json
This is deliberately stricter for COMPLETE than for honest PARTIAL_COVERAGE.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


MARKETS = {"SG", "CN", "MY"}
RUN_QUALITIES = {"COMPLETE", "PARTIAL_COVERAGE", "BLOCKED_STATE"}


def _valid_role_refs(probe: dict) -> bool:
    refs = probe.get("job_refs")
    return isinstance(refs, list) and all(
        isinstance(ref, str) and bool(ref.strip()) for ref in refs
    )


def validate(record: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["run record must be a JSON object"]

    if record.get("market") not in MARKETS:
        errors.append("market must be SG, CN, or MY")
    quality = record.get("run_quality")
    if quality not in RUN_QUALITIES:
        errors.append("run_quality must be COMPLETE, PARTIAL_COVERAGE, or BLOCKED_STATE")

    for flag in ("phase_a_completed", "phase_b_completed"):
        if not isinstance(record.get(flag), bool):
            errors.append(f"{flag} must be an explicit boolean")

    debt = record.get("coverage_debt_remaining")
    if not isinstance(debt, int) or isinstance(debt, bool) or debt < 0:
        errors.append("coverage_debt_remaining must be a nonnegative integer")

    attempts = record.get("platform_attempts")
    if not isinstance(attempts, list):
        errors.append("platform_attempts must be a list")
        attempts = []
    probes = record.get("source_probes")
    if not isinstance(probes, list):
        errors.append("source_probes must be a list, even if empty")
        probes = []

    for index, probe in enumerate(probes):
        if not isinstance(probe, dict):
            errors.append(f"source_probes[{index}]: not an object")
            continue
        for key in ("platform", "source_kind", "query_family", "page_key"):
            if not isinstance(probe.get(key), str) or not probe[key].strip():
                errors.append(f"source_probes[{index}].{key}: missing string")
        if not _valid_role_refs(probe):
            errors.append(f"source_probes[{index}].job_refs: invalid refs")
        if not isinstance(probe.get("end_of_results"), bool):
            errors.append(f"source_probes[{index}].end_of_results: missing boolean")

    if quality == "COMPLETE":
        if record.get("phase_a_completed") is not True:
            errors.append("COMPLETE requires phase_a_completed=true")
        if record.get("phase_b_completed") is not True:
            errors.append("COMPLETE requires phase_b_completed=true")
        if debt != 0:
            errors.append("COMPLETE requires zero unresolved relevant coverage debt")
        if len(attempts) < 4:
            errors.append("COMPLETE requires four scheduled platform families")
        if record.get("coverage_gaps"):
            errors.append("COMPLETE cannot carry material coverage_gaps")
        freehire = record.get("freehire_triage")
        if not isinstance(freehire, dict) or freehire.get("manifest_reconciled") is not True:
            errors.append("COMPLETE requires read-back-reconciled FreeHire manifest")
        for attempt in attempts:
            if not isinstance(attempt, dict):
                errors.append("COMPLETE requires object platform attempts")
                continue
            platform = attempt.get("platform")
            if not isinstance(platform, str) or not platform:
                errors.append("COMPLETE requires named platform")
                continue
            same = [p for p in probes if isinstance(p, dict) and p.get("platform") == platform]
            if not same:
                errors.append(f"{platform}: no page/query/source evidence")
                continue
            identities = {str(ref) for p in same for ref in (p.get("job_refs") or [])}
            page_keys = {str(p.get("source_kind")) + ":" + str(p.get("page_key")) for p in same}
            native_pages = sum(p.get("source_kind") == "native" for p in same)
            independent_sources = {str(p.get("source_kind")) for p in same if p.get("job_refs")}
            is_exhausted = any(p.get("end_of_results") is True for p in same)
            if len(page_keys) < 2 and not is_exhausted:
                errors.append(f"{platform}: single page is insufficient without proven exhaustion")
            if native_pages < 2 and not is_exhausted and len(independent_sources) < 2:
                errors.append(f"{platform}: native pagination or two independent fallback source kinds required")
            if not identities and not is_exhausted:
                errors.append(f"{platform}: no concrete job identities or exhausted-source evidence")
            if len(identities) < 20 and not is_exhausted:
                errors.append(f"{platform}: below 20 identifiable jobs without source exhaustion")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, type=Path, help="One new JSON record, not legacy JSONL")
    args = parser.parse_args(argv)
    try:
        record = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"BLOCKED_STATE: cannot read new run record: {exc}", file=sys.stderr)
        return 1
    errors = validate(record)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print(f"PASS: {record['market']} {record['run_quality']} claim is structurally supported")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
