# FreeHire Lossless Gap Recovery

This is a focused execution supplement to `README.md`, `RULES.md`, `DISCOVERY_STATE.md`, and `docs/source-routing.md`. It defines how hourly scouts recover a lagging FreeHire sequence watermark without turning radar intake into an unbounded crawl.

## Purpose

`feed/candidates.json` is a capped fast path. `feed/pages/*.jsonl` plus `feed/index.json:last_seq` are the lossless recovery path.

A market scout must not leave a known FreeHire backlog indefinitely stale. When that market's `freehire_event_seq` is behind upstream `last_seq`, every run must perform one bounded contiguous recovery slice in addition to the market's normal first-party/native/broad-platform discovery floor.

## Authoritative cursor files

To avoid concurrent whole-file rewrites of `DISCOVERY_STATE.md`, the mutable FreeHire cursor for each market lives in one small market-owned file:

- SG: `discovery-state/freehire-sg.json`
- CN: `discovery-state/freehire-cn.json`
- MY: `discovery-state/freehire-my.json`

For FreeHire recovery only, these files are authoritative. The older `freehire_event_seq` values embedded in `DISCOVERY_STATE.md` are legacy migration/history snapshots and must not be used once the market cursor file exists.

Each scout may update only its own FreeHire cursor file. Do not rewrite another market's cursor file.

## Recovery slice

For market `M` with current authoritative watermark `W` and upstream head `H`:

1. If `W >= H`, no backlog recovery is needed.
2. If `W < H`, set a target boundary `B = min(W + 500, H)`.
3. Read sequence events forward from `W + 1`, never skipping a sequence, up to `B` or until the run's bounded execution window is exhausted.
4. Events clearly belonging only to other markets may be cheap-skipped without JD research.
5. For events relevant to `M`, apply the normal pipeline in the existing repo contract: exact Issue-history dedupe -> cheap hard screen -> full JD only for survivors -> liveness/employment/work-auth/cohort/route verification -> targeted Gmail dedupe -> durable APPLY/CHECK Issue or terminal disposition.
6. Do not deep-research obvious title/domain/seniority mismatches just because they are in the recovery slice.

The `500` limit is a maximum target span per market run, not a requirement to finish all 500 before persisting progress and not a target number of JDs to research.

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

Persist progress to the market's authoritative cursor file after a contiguous prefix has been fully handled; completing the entire target `(W, B]` is **not** required.

A sequence is fully handled when it is either:

- irrelevant to the current market and safely cheap-skipped;
- terminally handled by the existing rules; or
- a verified serious survivor whose APPLY/CHECK Issue was successfully created and read back.

If the run reaches sequence `P` and every sequence in `(W, P]` is fully handled, update the market cursor to `P` even when `P < B`. This prevents repeated work across hourly runs.

Never advance past:

- an unreadable/missing required sequence after narrow-range/single-line fallback;
- an unresolved relevant candidate that the rules require preserving;
- an ambiguous/failed Issue write/readback;
- a transient verification failure that prevents a required disposition.

When blocked, persist only through the last fully handled sequence and report the first blocking sequence plus the reason. When the run simply exhausts its bounded execution window, persist the last fully handled sequence and report the next sequence to resume from; do not call normal time exhaustion a data blocker.

## Relationship to other discovery floors

FreeHire is Tier-3 radar only.

- SG still must execute its broad-platform gap floor.
- MY still must execute its broad-platform gap floor and destination-quality rules.
- CN still must execute both official-owner rotation and its native-platform recall floor.

FreeHire recovery does not replace, weaken, or satisfy those floors. It is an additional bounded lossless-recall obligation while a backlog exists.

## Catch-up behavior

Repeat bounded forward recovery every hourly run until the market cursor reaches upstream head. After catch-up, use the same rule for any future gap that appears; do not reset or guess cursors forward.
