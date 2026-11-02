# Scout Run Metrics

This is the durable audit contract for every SG/CN/MY scout run. It is machine/audit history only, not opportunity state. GitHub Issues remain the only live opportunity queue.

## Goal

Every completed scout run must leave enough evidence to answer:

- which platforms were actually searched;
- how many result rows/cards were actually inspected;
- how many unique candidate keys were derived;
- how many candidates died at Issue-history dedupe or cheap hard filters;
- how many full JDs were read;
- how many verified survivors were found;
- how many APPLY/CHECK Issues were created;
- how far FreeHire recovery advanced and why it stopped.

Do not report platform-advertised totals (for example `1,484 AI jobs`) as scanned volume. `results_inspected` means rows/cards actually inspected in this run.

## Durable log location

Append exactly one compact JSON object per completed run to the market/month log:

- `discovery-metrics/YYYY-MM/sg.jsonl`
- `discovery-metrics/YYYY-MM/cn.jsonl`
- `discovery-metrics/YYYY-MM/my.jsonl`

Use Asia/Kuala_Lumpur month boundaries. If the monthly file does not exist, create it. If it exists, fetch it, append one newline-delimited JSON object, write the full file back, then read it back and verify the final line matches this run. Each market writes only its own file.

Metrics logging is required even when the run finds zero survivors or hits a blocker.

## Required run record

Each line must contain these keys:

```json
{
  "completed_at": "2026-11-02T22:30:00+08:00",
  "market": "SG",
  "platform_cycle": 1,
  "platform_attempts": [
    {
      "platform": "LinkedIn Jobs Singapore",
      "queries_run": 2,
      "results_inspected": 20,
      "unique_candidates": 14,
      "issue_duplicates": 6,
      "cheap_hard_rejects": 5,
      "full_jd_reads": 3,
      "verified_survivors": 1
    }
  ],
  "owner_bucket": "Sea / SAIL / Shopee / Grab / Singtel",
  "query_bucket": "NLP / search / retrieval / ranking / knowledge graph",
  "research_bucket": "A*STAR",
  "fresh_totals": {
    "results_inspected": 40,
    "unique_candidates_before_cross_source_dedupe": 28,
    "global_unique_candidates": 22,
    "issue_duplicates": 10,
    "cheap_hard_rejects": 8,
    "full_jd_reads": 4,
    "verified_survivors": 2,
    "apply_created": 1,
    "check_created": 1
  },
  "freehire": {
    "start_seq": 16120,
    "end_seq": 16200,
    "advanced": 80,
    "events_read": 80,
    "market_relevant": 7,
    "issue_duplicates": 2,
    "cheap_hard_rejects": 4,
    "full_jd_reads": 1,
    "verified_survivors": 0,
    "next_seq": 16201
  },
  "blocker": null
}
```

For CN/MY omit `research_bucket` or set it to null.

## Counting rules

- `queries_run`: actual distinct search queries executed on that platform.
- `results_inspected`: result rows/cards actually looked at enough to derive title/employer/location/ID or candidate key. Never use a platform's displayed total-result count.
- `unique_candidates`: unique candidate keys within that platform attempt.
- `global_unique_candidates`: candidates remaining after cross-platform identity collapse for the whole fresh phase.
- `issue_duplicates`: exact/current-history duplicates killed before full-JD research.
- `cheap_hard_rejects`: terminal cheap-screen rejects such as seniority/cohort/domain/employment mismatch before full-JD research where possible.
- `full_jd_reads`: candidates whose substantive JD was opened/read for verification.
- `verified_survivors`: candidates that survived verification far enough to merit durable APPLY/CHECK handoff in this run.
- `apply_created` / `check_created`: Issues actually created and read back successfully.
- FreeHire counts refer only to the lossless recovery phase and must not be mixed into fresh-platform totals.
- If the same candidate appears on two platforms, it may count once in each platform's local `unique_candidates`, but only once in `global_unique_candidates`.
- Unknown counts must be `null`, never guessed.

## Reporting

The human-facing run result must include a compact summary such as:

`Fresh: 2 platforms / 37 rows inspected / 21 global unique / 9 duplicates / 7 hard rejects / 5 full JDs / 2 survivors (1 APPLY, 1 CHECK). FreeHire: +80 seq, 7 market-relevant.`

Also name each platform and its `results_inspected` count. The durable JSONL record is authoritative for audit history.

## Failure handling

A run is not fully complete until both fresh-state persistence and metrics-log persistence/read-back are verified. If metrics persistence fails, report that explicitly and do not claim the audit record was saved. Do not alter opportunity state merely to repair metrics.