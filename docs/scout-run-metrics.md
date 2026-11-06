# Scout Run Metrics

Durable audit contract for SG/CN/MY scout runs. GitHub Issues remain the only live opportunity queue.

## Log location

Append exactly one compact JSON object per completed run to:

- `discovery-metrics/YYYY-MM-DD/sg.jsonl`
- `discovery-metrics/YYYY-MM-DD/cn.jsonl`
- `discovery-metrics/YYYY-MM-DD/my.jsonl`

Use Asia/Kuala_Lumpur date boundaries. Legacy monthly files are read-only.

## Required evidence

Every run should preserve enough evidence to answer:

- which fresh platforms were attempted and how many rows were actually inspected;
- how many candidates were exact duplicates or cheap rejects;
- how many substantive JDs were read;
- how many cheap rejects were independently audited and how many were false negatives;
- how many retries/deferred candidates were processed/preserved;
- how many verified APPLY/CHECK survivors were created;
- where the market FreeHire cursor ended.

Unknown counts must be `null`, never guessed.

## Required record shape

```json
{
  "completed_at": "2026-11-03T13:00:00+08:00",
  "market": "CN",
  "platform_cycle": 6,
  "platform_attempts": [],
  "owner_bucket": "Alibaba / Tencent",
  "query_bucket": "RAG / knowledge / retrieval",
  "research_bucket": null,
  "fresh_totals": {
    "results_inspected": 40,
    "global_unique_candidates": 30,
    "issue_duplicates": 8,
    "cheap_hard_rejects": 18,
    "full_jd_reads": 4,
    "verified_survivors": 1,
    "apply_created": 1,
    "check_created": 0
  },
  "freehire_triage": {
    "cursor_start": 100,
    "cursor_end": 200,
    "batch_candidates": 100,
    "strong_known_duplicates": 4,
    "weak_suspected_checked": 2,
    "cheap_hard_rejects": 70,
    "full_jd_reads": 15,
    "reject_audit_sampled": 5,
    "reject_audit_false_negatives": 0,
    "retries_due": 3,
    "retries_processed": 3,
    "retries_created_or_updated": 10,
    "verified_survivors": 4,
    "apply_created": 3,
    "check_created": 1,
    "next_candidate_seq": 201
  },
  "blocker": null
}
```

For CN/MY, `research_bucket` may be null.

## Counting rules

Fresh phase:

- `results_inspected`: rows/cards actually inspected enough to derive candidate identity, never platform-advertised totals.
- `issue_duplicates`: exact/current-history duplicates killed before deep work.
- `cheap_hard_rejects`: terminal cheap-screen rejects.
- `full_jd_reads`: substantive JDs opened/read for normal candidate verification.
- `verified_survivors`: candidates that reached durable APPLY/CHECK handoff.

FreeHire phase:

- `batch_candidates`: compact metadata candidates actually processed from the reconciled manifest/shards.
- `strong_known_duplicates`: exact historical identity suppressions.
- `weak_suspected_checked`: weak company/title suspicions explicitly resolved; weak identity never auto-drops.
- `cheap_hard_rejects`: terminal cheap rejects before normal deep verification.
- `full_jd_reads`: normal survivor/retry substantive JD reads; **exclude reject-audit-only reads** from this field.
- `reject_audit_sampled`: cheap rejects independently re-opened against substantive JD evidence to estimate false-negative risk.
- `reject_audit_false_negatives`: audited rejects whose cheap terminal decision was wrong and which therefore required normal candidate gates.
- `retries_*`: due retry work and new/updated durable receipts, including `budget_deferred`.
- `verified_survivors`: candidates durably handed off to APPLY/CHECK.
- `cursor_start` / `cursor_end`: market triage sequence before/after the run.

A false-negative audit survivor may also increment normal survivor/APPLY/CHECK fields after it passes the same final gates; the audit fields remain separate so recall can be measured.

## Coverage and correctness diagnostics (additive fields)

For new records, also report:

- run_quality: COMPLETE or PARTIAL_COVERAGE or BLOCKED_STATE. This is **not** inferred from the number of new Issues. COMPLETE requires the scheduled source attempts, bounded alternate-source recovery for weak/zero-row attempts, all mandatory durable handoffs, and read-back validation. It does not promise market exhaustiveness.
- coverage_gaps: concrete blocked/weak sources and their actual inspected rows, not a generic statement of no listings.
- fallback_sources: source families used to compensate for blocked native pages, with separately counted rows (avoid duplicates).
- retry_new_evidence: number of retries that yielded a new substantive JD, route, or eligibility fact; distinguish from attempts/reschedules.
- recall_spotcheck (daily review, not every hourly run): independent fresh roles sampled, matches in all Issue history, verified missed eligible roles, and root cause. Small samples indicate **possible** false negatives, not a statistically valid market recall estimate.

**Pre-write and post-write invariant:** Validate all market-owned discovery files with python scripts/validate_scout_state.py (or equivalent structural checks if the runtime lacks Python). In particular fresh-<market>.json must contain rotation counters, retry-<market>.json must contain a receipt array, and triage-<market>.json must contain the consumption cursor. A read-back that only compares bytes can falsely certify a file written to the **wrong path**. On any shape mismatch: stop changing market state, report BLOCKED_STATE, and preserve the original data for repair. Never advance a cursor or say the cycle completed when validation fails.

## Reporting

Human-facing summaries should include both throughput and recall evidence, for example:

`FreeHire: 100 candidates / 68 cheap rejects / 15 normal JD reads / reject audit 5 with 0 false negatives / 4 survivors / cursor 100→200.`

Do not describe a filter as "good" merely because it rejects many candidates. Repeated reject-audit evidence is required before tightening it further.

## Failure handling

A run is not fully complete until required market state and metrics are persisted and read back. A transient candidate failure may move to retry without freezing the cursor; failure to persist required retry state is an infrastructure blocker.
