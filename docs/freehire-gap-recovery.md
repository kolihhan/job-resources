# FreeHire Lossless Gap Recovery

This is a focused execution supplement to `README.md`, `RULES.md`, `DISCOVERY_STATE.md`, and `docs/source-routing.md`. It defines how hourly scouts recover a lagging FreeHire sequence watermark without turning radar intake into an unbounded crawl.

## Purpose

`feed/candidates.json` is a capped fast path. `feed/pages/*.jsonl` plus `feed/index.json:last_seq` are the lossless recovery path.

A market scout must not leave a known FreeHire backlog indefinitely stale. When that market's `freehire_event_seq` is behind upstream `last_seq`, every run must perform one bounded contiguous recovery slice in addition to the market's normal first-party/native/broad-platform discovery floor.

## Recovery slice

For market `M` with current watermark `W` and upstream head `H`:

1. If `W >= H`, no backlog recovery is needed.
2. If `W < H`, set the run boundary to `B = min(W + 500, H)`.
3. Read every FreeHire sequence event in `(W, B]` from `feed/pages/*.jsonl`.
4. Events clearly belonging only to other markets may be cheap-skipped without JD research.
5. For events relevant to `M`, apply the normal pipeline in the existing repo contract: exact Issue-history dedupe -> cheap hard screen -> full JD only for survivors -> liveness/employment/work-auth/cohort/route verification -> targeted Gmail dedupe -> durable APPLY/CHECK Issue or terminal disposition.
6. Do not deep-research obvious title/domain/seniority mismatches just because they are in the recovery slice.

The `500` limit is a maximum global-sequence span per market run, not a target number of JDs to research.

## Sequence-page read method

Each `feed/pages/*.jsonl` file contains exactly one sequence event per line, in sequence order. Do **not** fetch a whole 50-event JSONL page when the connector may truncate long text.

For a page whose filename/range is `FIRST-LAST`:

- line number for sequence `S` is `S - FIRST + 1`;
- read the page in small contiguous line ranges (normally 10 lines or fewer);
- if a small range is still truncated or ambiguous, fall back to a single-line read for the exact sequence;
- verify the returned JSON object's `seq` equals the expected sequence before treating it as read;
- only classify a sequence as unreadable after the narrow-range/single-line fallback also fails.

Connector response-size truncation of a whole page is therefore a retrieval-method problem, not by itself a valid reason to leave the watermark permanently blocked.

## Watermark advancement

Advance `freehire_event_seq` to `B` only when every relevant event through `B` is either:

- terminally handled by the existing rules; or
- a verified serious survivor whose APPLY/CHECK Issue was successfully created and read back.

Never advance past:

- an unreadable/missing required sequence after narrow-range/single-line fallback;
- an unresolved relevant candidate that the rules require preserving;
- an ambiguous/failed Issue write/readback;
- a transient verification failure that prevents a required disposition.

When blocked, keep the watermark at the last fully handled sequence and report the first blocking sequence plus the reason.

## Relationship to other discovery floors

FreeHire is Tier-3 radar only.

- SG still must execute its broad-platform gap floor.
- MY still must execute its broad-platform gap floor and destination-quality rules.
- CN still must execute both official-owner rotation and its native-platform recall floor.

FreeHire recovery does not replace, weaken, or satisfy those floors. It is an additional bounded lossless-recall obligation while a backlog exists.

## Catch-up behavior

Repeat one bounded slice per hourly run until the market watermark reaches upstream head. After catch-up, use the same rule for any future gap that appears; do not reset or guess cursors forward.
