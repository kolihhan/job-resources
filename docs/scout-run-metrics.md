# Scout Run Metrics

This is the durable audit contract for every SG/CN/MY scout run. It is machine/audit history only, not opportunity state. GitHub Issues remain the only live opportunity queue.

## Goal

Every completed scout run must leave enough evidence to answer:

- which fresh platforms were actually searched;
- how many result rows/cards were actually inspected;
- how many unique candidate keys were derived;
- how many candidates died at Issue-history dedupe or cheap hard filters;
- how many full JDs were read;
- how many verified survivors were found;
- how many APPLY/CHECK Issues were created;
- how many FreeHire triage candidates/retries were processed and where the market cursor ended.

Do not report platform-advertised totals as scanned volume. `results_inspected` means rows/cards actually inspected in this run.

## Durable log location

Append exactly one compact JSON object per completed run to the **daily market shard**:

- `discovery-metrics/YYYY-MM-DD/sg.jsonl`
- `discovery-metrics/YYYY-MM-DD/cn.jsonl`
- `discovery-metrics/YYYY-MM-DD/my.jsonl`

Use Asia/Kuala_Lumpur date boundaries. A daily shard contains at most the runs for one market on one local calendar day, keeping each file small enough for safe whole-file fetch/append/read-back through the GitHub connector.

If the daily file does not exist, create it. If it exists, fetch it completely, append one newline-delimited JSON object, write the full file back, then fetch it again and verify the final line matches this run. Each market writes only its own file.

The legacy monthly files under `discovery-metrics/YYYY-MM/{sg,cn,my}.jsonl` are historical/read-only. Do not append new runs to them and do not migrate or rewrite them merely to satisfy this contract.

Metrics logging is required even when the run finds zero survivors or hits a blocker.

## Required run record

Each line must contain these keys:

```json
{
  "completed_at": "2026-11-03T01:10:00+08:00",
  "market": "SG",
  "platform_cycle": 2,
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
  "freehire_triage": {
    "cursor_start": 0,
    "cursor_end": 30,
    "batch_candidates": 30,
    "strong_known_duplicates": 4,
    "weak_suspected_checked": 2,
    "cheap_hard_rejects": 18,
    "full_jd_reads": 6,
    "retries_due": 1,
    "retries_processed": 1,
    "retries_created_or_updated": 1,
    "verified_survivors": 2,
    "apply_created": 1,
    "check_created": 1,
    "next_candidate_seq": 31
  },
  "blocker": null
}
```

For CN/MY omit `research_bucket` or set it to null.

## Counting rules

Fresh phase:

- `queries_run`: actual distinct search queries executed on that platform.
- `results_inspected`: result rows/cards actually looked at enough to derive title/employer/location/ID or candidate key.
- `unique_candidates`: unique candidate keys within that platform attempt.
- `global_unique_candidates`: candidates remaining after cross-platform identity collapse for the whole fresh phase.
- `issue_duplicates`: exact/current-history duplicates killed before full-JD research.
- `cheap_hard_rejects`: terminal cheap-screen rejects before full-JD research where possible.
- `full_jd_reads`: candidates whose substantive JD was opened/read for verification.
- `verified_survivors`: candidates that survived verification far enough to merit durable APPLY/CHECK handoff in this run.
- `apply_created` / `check_created`: Issues actually created and read back successfully.

FreeHire triage phase:

- `cursor_start` / `cursor_end`: market `last_consumed_candidate_seq` before and after the run.
- `batch_candidates`: candidates actually taken from the bounded market batch in this run.
- `strong_known_duplicates`: candidates killed by exact all-Issue-history identity before full-JD work.
- `weak_suspected_checked`: `known_status=suspected_known` candidates for which the weak suspicion was explicitly checked; this is never an automatic drop count.
- `cheap_hard_rejects`: terminal RULES rejects from batch metadata/snippet/known campaign evidence before deeper JD research.
- `full_jd_reads`: batch/retry candidates whose substantive authoritative or best available JD was actually read.
- `retries_due`: retry receipts due at the start of the run.
- `retries_processed`: due retry receipts actually attempted.
- `retries_created_or_updated`: transient candidates durably moved into retry state or whose receipt was updated.
- `verified_survivors`: FreeHire candidates that reached durable APPLY/CHECK handoff.
- `next_candidate_seq`: next market candidate sequence expected after cursor advancement, or null when no batch remains.

Unknown counts must be `null`, never guessed.

Fresh-platform counts and FreeHire-triage counts must remain separate even when they identify the same role. Cross-source exact dedupe prevents duplicate Issue creation.

## Reporting

The human-facing run result should include a compact summary such as:

`Fresh: 2 platforms / 37 rows inspected / 21 global unique / 9 duplicates / 7 hard rejects / 5 full JDs / 2 survivors (1 APPLY, 1 CHECK). FreeHire triage: 30 batch candidates / cursor 120→150 / 3 exact duplicates / 18 cheap rejects / 7 full JDs / 1 retry / 1 survivor.`

Also name each fresh platform and its `results_inspected` count. The durable JSONL record is authoritative for audit history.

## Failure handling

A run is not fully complete until fresh-state persistence, market triage/retry persistence, and metrics-log persistence/read-back are verified.

A transient candidate verification failure is not a reason to freeze the main FreeHire cursor if a durable retry receipt was successfully written and read back. Failure to persist the retry receipt itself is an infrastructure blocker; do not advance beyond that candidate.

If metrics persistence fails, report that explicitly and do not claim the audit record was saved. Do not alter opportunity state merely to repair metrics.
