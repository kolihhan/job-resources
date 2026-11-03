#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile

_MARKETS = ("SG", "CN", "MY")
_DEFAULT_BATCH_SIZE = 100
_DEFAULT_SHARD_SIZE = 25  # record-count ceiling; byte budget is the safety boundary
_DEFAULT_MAX_SHARD_BYTES = 8_000
_TRANSPORT_FIELDS = (
    "market",
    "public_slug",
    "company",
    "title",
    "location",
    "source",
    "source_url",
    "external_id",
    "known_status",
    "known_match_basis",
    "ai_score",
    "ai_signals",
    "flags",
    "employment_type",
    "posted_at",
)


def _role_key(candidate: dict) -> str | None:
    slug = str(candidate.get("public_slug") or "").strip().lower()
    if not slug:
        return None
    return f"freehire:{slug}"


def _seq(value: object, default: int = 0) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default
    return max(default, parsed)


def _compact_candidate(candidate: dict) -> dict:
    return {key: candidate.get(key) for key in _TRANSPORT_FIELDS if key in candidate}


def _normalize_registry(registry: dict | None) -> dict:
    source = registry if isinstance(registry, dict) else {}
    source_roles = source.get("roles") if isinstance(source.get("roles"), dict) else {}
    roles: dict[str, dict] = {}
    max_seen = 0
    for role_key, record in source_roles.items():
        if not isinstance(role_key, str) or not isinstance(record, dict):
            continue
        candidate_seq = _seq(record.get("candidate_seq"))
        if candidate_seq <= 0:
            continue
        max_seen = max(max_seen, candidate_seq)
        roles[role_key] = {
            "candidate_seq": candidate_seq,
            "market": str(record.get("market") or "").upper(),
            "public_slug": str(record.get("public_slug") or ""),
        }
    next_candidate_seq = max(_seq(source.get("next_candidate_seq"), 1), max_seen + 1, 1)
    return {"version": 1, "next_candidate_seq": next_candidate_seq, "roles": roles}


def build_batches(
    coldstart: dict,
    registry: dict | None,
    cursors: dict[str, dict] | None,
    batch_size: int = _DEFAULT_BATCH_SIZE,
    generated_at: str | None = None,
) -> tuple[dict, dict[str, dict]]:
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")

    normalized = _normalize_registry(registry)
    roles = normalized["roles"]
    next_candidate_seq = normalized["next_candidate_seq"]
    current: dict[str, tuple[int, dict]] = {}
    missing_identity_count = 0

    candidates = coldstart.get("candidates") if isinstance(coldstart.get("candidates"), list) else []
    for source_candidate in candidates:
        if not isinstance(source_candidate, dict):
            continue
        market = str(source_candidate.get("market") or "").upper()
        if market not in _MARKETS:
            continue
        role_key = _role_key(source_candidate)
        if not role_key:
            missing_identity_count += 1
            continue

        record = roles.get(role_key)
        if record is None:
            record = {
                "candidate_seq": next_candidate_seq,
                "market": market,
                "public_slug": str(source_candidate.get("public_slug") or ""),
            }
            roles[role_key] = record
            next_candidate_seq += 1

        candidate = _compact_candidate(source_candidate)
        candidate["role_key"] = role_key
        candidate["candidate_seq"] = record["candidate_seq"]
        current[role_key] = (record["candidate_seq"], candidate)

    normalized["next_candidate_seq"] = next_candidate_seq
    normalized["source_generated_at"] = coldstart.get("source_generated_at")
    normalized["current_candidate_count"] = len(current)
    normalized["missing_identity_count"] = missing_identity_count
    normalized["generated_at"] = generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    cursor_map = cursors if isinstance(cursors, dict) else {}
    batches: dict[str, dict] = {}
    for market in _MARKETS:
        cursor = _seq(
            (cursor_map.get(market) or {}).get("last_consumed_candidate_seq")
            if isinstance(cursor_map.get(market), dict)
            else 0
        )
        available = sorted(
            (
                pair
                for pair in current.values()
                if str(pair[1].get("market") or "").upper() == market and pair[0] > cursor
            ),
            key=lambda pair: pair[0],
        )
        selected = [candidate for _, candidate in available[:batch_size]]
        max_candidate_seq = max((candidate["candidate_seq"] for candidate in selected), default=cursor)
        batches[market] = {
            "version": 3,
            "transport": "compact_metadata_byte_bounded_v1",
            "generated_at": normalized["generated_at"],
            "source_generated_at": coldstart.get("source_generated_at"),
            "market": market,
            "cursor_before": cursor,
            "batch_size": batch_size,
            "candidate_count": len(selected),
            "remaining_after_batch": max(0, len(available) - len(selected)),
            "max_candidate_seq": max_candidate_seq,
            "candidates": selected,
        }

    return normalized, batches


def _make_shard(batch: dict, market: str, shard_index: int, candidates: list[dict]) -> dict:
    seqs = [_seq(candidate.get("candidate_seq")) for candidate in candidates if isinstance(candidate, dict)]
    return {
        "version": batch.get("version", 3),
        "transport": batch.get("transport", "compact_metadata_byte_bounded_v1"),
        "generated_at": batch.get("generated_at"),
        "source_generated_at": batch.get("source_generated_at"),
        "market": market,
        "shard_index": shard_index,
        "candidate_count": len(candidates),
        "min_candidate_seq": min(seqs) if seqs else batch.get("cursor_before"),
        "max_candidate_seq": max(seqs) if seqs else batch.get("cursor_before"),
        "candidates": candidates,
    }


def _serialized_size(payload: dict) -> int:
    return len(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8"))


def shard_batch(
    batch: dict,
    shard_size: int = _DEFAULT_SHARD_SIZE,
    max_shard_bytes: int = _DEFAULT_MAX_SHARD_BYTES,
) -> tuple[dict, list[dict]]:
    if shard_size <= 0:
        raise ValueError("shard_size must be positive")
    if max_shard_bytes <= 0:
        raise ValueError("max_shard_bytes must be positive")

    candidates = batch.get("candidates") if isinstance(batch.get("candidates"), list) else []
    market = str(batch.get("market") or "").upper()
    shards: list[dict] = []
    current: list[dict] = []

    for candidate in candidates:
        proposed = current + [candidate]
        proposed_payload = _make_shard(batch, market, len(shards) + 1, proposed)
        if current and (len(proposed) > shard_size or _serialized_size(proposed_payload) > max_shard_bytes):
            shards.append(_make_shard(batch, market, len(shards) + 1, current))
            current = [candidate]
        else:
            current = proposed

        singleton_or_current = _make_shard(batch, market, len(shards) + 1, current)
        if _serialized_size(singleton_or_current) > max_shard_bytes:
            seq = candidate.get("candidate_seq") if isinstance(candidate, dict) else None
            raise ValueError(f"candidate_seq {seq} exceeds max_shard_bytes={max_shard_bytes}")

    if current:
        shards.append(_make_shard(batch, market, len(shards) + 1, current))

    manifest = {key: value for key, value in batch.items() if key != "candidates"}
    manifest["shard_size"] = shard_size
    manifest["max_shard_bytes"] = max_shard_bytes
    manifest["shard_count"] = len(shards)
    manifest["shards"] = [
        f"freehire-batch-{market.lower()}-{index:02d}.json" for index in range(1, len(shards) + 1)
    ]
    return manifest, shards


def _read_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else default


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


def _write_sharded_batch(
    state_dir: Path,
    market: str,
    batch: dict,
    shard_size: int,
    max_shard_bytes: int,
) -> dict:
    market_key = market.lower()
    for stale in state_dir.glob(f"freehire-batch-{market_key}-*.json"):
        stale.unlink()

    manifest, shards = shard_batch(batch, shard_size=shard_size, max_shard_bytes=max_shard_bytes)
    _atomic_write_json(state_dir / f"freehire-batch-{market_key}.json", manifest)
    for index, shard in enumerate(shards, start=1):
        _atomic_write_json(state_dir / f"freehire-batch-{market_key}-{index:02d}.json", shard)
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coldstart", default="discovery-state/freehire-coldstart.json")
    parser.add_argument("--registry", default="discovery-state/freehire-review-registry.json")
    parser.add_argument("--state-dir", default="discovery-state")
    parser.add_argument("--batch-size", type=int, default=_DEFAULT_BATCH_SIZE)
    parser.add_argument("--shard-size", type=int, default=_DEFAULT_SHARD_SIZE)
    parser.add_argument("--max-shard-bytes", type=int, default=_DEFAULT_MAX_SHARD_BYTES)
    args = parser.parse_args(argv)

    state_dir = Path(args.state_dir)
    coldstart = _read_json(Path(args.coldstart), {})
    registry_path = Path(args.registry)
    registry = _read_json(registry_path, {})
    cursors = {
        market: _read_json(state_dir / f"triage-{market.lower()}.json", {"last_consumed_candidate_seq": 0})
        for market in _MARKETS
    }

    new_registry, batches = build_batches(
        coldstart,
        registry=registry,
        cursors=cursors,
        batch_size=args.batch_size,
    )
    _atomic_write_json(registry_path, new_registry)
    manifests = {
        market: _write_sharded_batch(
            state_dir,
            market,
            batch,
            shard_size=args.shard_size,
            max_shard_bytes=args.max_shard_bytes,
        )
        for market, batch in batches.items()
    }

    print(
        json.dumps(
            {
                "registry_roles": len(new_registry["roles"]),
                "next_candidate_seq": new_registry["next_candidate_seq"],
                "missing_identity_count": new_registry["missing_identity_count"],
                "batches": {
                    market: {
                        "cursor_before": manifest["cursor_before"],
                        "candidate_count": manifest["candidate_count"],
                        "remaining_after_batch": manifest["remaining_after_batch"],
                        "max_candidate_seq": manifest["max_candidate_seq"],
                        "shard_count": manifest["shard_count"],
                        "max_shard_bytes": manifest["max_shard_bytes"],
                    }
                    for market, manifest in manifests.items()
                },
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
