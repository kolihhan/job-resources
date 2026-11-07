# Scout Run Metrics

Durable audit contract for SG/CN/MY scout runs. GitHub Issues remain the only live opportunity queue.

## Log location

Append exactly one compact JSON object per completed run to:

- `discovery-metrics/YYYY-MM-DD/sg.jsonl`
- `discovery-metrics/YYYY-MM-DD/cn.jsonl`
- `discovery-metrics/YYYY-MM-DD/my.jsonl`

Use Asia/Kuala_Lumpur date boundaries. Legacy monthly files are read-only.

## Non-negotiable completion gate

A scout run that inspects a single page/snippet set, cannot obtain page two or an evidenced exhaustion signal, or skips current FreeHire due/batch processing **must not be called DONE**. It may write a truthful partial-run metrics row, but the user-facing report must say `INCOMPLETE / PARTIAL_COVERAGE` with the exact next step and unfinished counts. Source attempts are not market coverage. A zero-new-role result without inspectable evidence is **UNKNOWN**, never "no jobs".

For each attempted platform, include `source_probes` entries with the source path, query/topic, pagination page/cursor or explicit unavailability, distinct exact role identifiers/URLs (bounded sample), total unique rows from that page, and whether end-of-results is proven. Separate native rows from indexed/ATS fallback rows; indexed search hits are not platform-native pagination. If a source is undercovered, the matching entry in market-owned `fresh-<market>.json:coverage_debt` must identify a next probe. A run must document at least one previous debt attempted or explain why it was blocked.

Set `phase_a_completed` and `phase_b_completed` booleans in each metrics record. `COMPLETE` is permitted **only** if both are true, current required source attempts and durable handoffs are evidenced, current sources have real page/exhaustion/substitute evidence, and there is no material unworked coverage debt. Otherwise `PARTIAL_COVERAGE` (or `BLOCKED_STATE` if state integrity failed). A metrics row recording an incomplete run is an honest checkpoint, **not an achievement or completion receipt**. Before persisting, validate these rules using `scripts/validate_scout_metrics.py` when executable; without Python do the equivalent explicit invariant checks. Never mark COMPLETE merely because the metrics JSON was appended.

## Required evidence

Every run should preserve enough evidence to answer:

- which fresh platforms, owner groups, query families and SG research buckets were attempted, and how many actual identifiable rows were inspected per source;
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
    "batch_candidates": 200,
    "strong_known_duplicates": 4,
    "weak_suspected_checked": 2,
    "cheap_hard_rejects": 70,
    "full_jd_reads": 25,
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

- run_quality: COMPLETE or PARTIAL_COVERAGE or BLOCKED_STATE. This is **not** inferred from the number of new Issues. COMPLETE requires separately verified deep source coverage (multiple pages or proved exhausted/independent substitutes), mandatory source attempts, both A/B phases, all durable handoffs and read-back validation. A 0-row or 1-page pass is a partial checkpoint, not completion.
- coverage_gaps: concrete blocked/weak sources and their actual inspected rows, not a generic statement of no listings.
- fallback_sources: source families used to compensate for blocked native pages, with separately counted rows (avoid duplicates).
- retry_new_evidence: number of retries that yielded a new substantive JD, route, or eligibility fact; distinguish from attempts/reschedules.
- fresh_bucket_coverage: attempted owner/query/research bucket names and exact unique roles per attempted platform. Include `source_probes` with inspected page/cursor/URL and sampled exact job identities. Do not infer coverage from hit totals.
- coverage_debt_remaining: count of material persisted `fresh-<market>.json:coverage_debt` entries after run and which older entry was investigated; a nonzero value prevents COMPLETE when a relevant required scope is still unworked.
- phase_a_completed / phase_b_completed: mandatory booleans for new records; the second must only be true if FreeHire manifest/retry obligations were actually dispositioned, or a proven empty queue was reconciled. Do not treat an unattempted batch as empty.
- retry_no_progress: due retries that still produced no new substantive evidence (optional additive field); report separately from newly deferred candidates and retry_new_evidence.
- budget_pressure: whether the expanded candidate/JD ceilings, unread backlog or runtime constraints caused any PARTIAL_COVERAGE or budget deferral.
- recall_spotcheck (daily review, not every hourly run): independent fresh roles sampled, matches in all Issue history, verified missed eligible roles, and root cause. Small samples indicate **possible** false negatives, not a statistically valid market recall estimate.

**Pre-write and post-write invariant:** Validate all market-owned discovery files with python scripts/validate_scout_state.py (or equivalent structural checks if the runtime lacks Python). In particular fresh-<market>.json must contain rotation counters, retry-<market>.json must contain a receipt array, and triage-<market>.json must contain the consumption cursor. A read-back that only compares bytes can falsely certify a file written to the **wrong path**. On any shape mismatch: stop changing market state, report BLOCKED_STATE, and preserve the original data for repair. Never advance a cursor or say the cycle completed when validation fails.

## Reporting

Human-facing summaries should include both throughput and recall evidence, for example:

`FreeHire: 200 candidates / 138 cheap rejects / 25 normal JD reads / reject audit 5 with 0 false negatives / 4 survivors / cursor 100→300.`

Do not say "scout done" or "no jobs" when the record is PARTIAL_COVERAGE; report exactly which page/query/role count was verified and what remains. Do not describe a filter as "good" merely because it rejects many candidates. Repeated reject-audit evidence is required before tightening it further.

## Failure handling

A run is not fully complete until required market state and metrics are persisted and read back. A transient candidate failure may move to retry without freezing the cursor; failure to persist required retry state is an infrastructure blocker.
