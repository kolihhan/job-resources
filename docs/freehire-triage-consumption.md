# FreeHire Triage Consumption

This is the active downstream contract for hourly SG/CN/MY scouts.

It replaces raw FreeHire event-sequence recovery as the normal reasoning path. `docs/freehire-gap-recovery.md` is retained only as historical/audit documentation.

## Purpose

The public `kolihhan/freehirefetch` collector periodically performs a full current-job scan with substantive job text and publishes `feed/coldstart.json`. The private `kolihhan/job-resources` workflow then:

1. rebuilds `discovery-state/known-role-index.json` from all GitHub Issues, open and closed;
2. subtracts only strong historical matches from the current FreeHire cold-start set;
3. preserves weak company/title matches as `suspected_known` rather than suppressing them;
4. assigns a stable private `candidate_seq` to each FreeHire `public_slug`;
5. publishes one bounded 100-candidate head batch per market.

Hourly scouts reason over those bounded market batches instead of raw FreeHire sequence pages or the multi-megabyte cold-start file.

## Machine state

These files are machine-efficiency state only. They are not a second human opportunity queue, and they never replace GitHub Issues.

Derived by the hourly repo workflow:

- `discovery-state/freehire-review-registry.json`
- `discovery-state/freehire-batch-sg.json`
- `discovery-state/freehire-batch-cn.json`
- `discovery-state/freehire-batch-my.json`
- `discovery-state/freehire-coldstart-summary.json`

Market-owned mutable state:

- SG: `discovery-state/triage-sg.json`, `discovery-state/retry-sg.json`
- CN: `discovery-state/triage-cn.json`, `discovery-state/retry-cn.json`
- MY: `discovery-state/triage-my.json`, `discovery-state/retry-my.json`

Each scout may update only its own market-owned files.

## Candidate identity and sequence

`freehire-review-registry.json` maps source-local FreeHire identity to a stable private sequence:

`freehire:<public_slug> -> candidate_seq`

A candidate keeps the same `candidate_seq` when the upstream cold-start ordering changes. Reappearing source roles therefore do not get a new sequence merely because the source reordered its response.

This sequence is a private consumption cursor, not a cross-source canonical role identity. Exact cross-source suppression still requires the strong identity rules in `docs/source-routing.md` and the final all-Issue-history gate.

## Per-run FreeHire phase

After the normal fresh-platform phase, the market scout performs this independent FreeHire phase.

### Throughput budget

The normal hourly target is deliberately asymmetric:

- cheap-screen up to **100** batch candidates per market run;
- perform at most **15 substantive full-JD reads** in that run;
- process up to **10 due retries** before the normal batch.

The 100-candidate budget is for cheap identity/history/policy screening. The 15-JD cap prevents a noisy batch from consuming the whole run in expensive browsing and reasoning.

If more than 15 candidates survive the cheap gate, do not drop them and do not freeze the main cursor. Preserve every extra plausible candidate as a durable retry receipt with `reason_code=budget_deferred`, a near-term `next_retry_at`, and the usual compact identity/source fields. Once those receipts are persisted and read back, the main cursor may continue.

### 1. Due retries

Read the market retry file first. Process up to 10 receipts whose `next_retry_at` is due, oldest first. `budget_deferred` receipts are normal backlog work, not failures.

A retry receipt contains only machine state such as:

```json
{
  "role_key": "freehire:example-slug",
  "candidate_seq": 123,
  "reason_code": "verification_transient",
  "attempts": 2,
  "next_retry_at": "2026-11-03T12:00:00+08:00"
}
```

Resolve/remove a receipt when the role becomes an exact historical duplicate, reaches a terminal RULES disposition, or a verified APPLY/CHECK Issue is successfully created and read back.

### 2. Current bounded batch

Read only the market's `freehire-batch-<market>.json`. Process candidates in ascending `candidate_seq`. The generated batch contains at most 100 candidates.

For each candidate:

1. run the exact all-Issue-history dedupe gate before expensive work;
2. if `known_status=suspected_known`, explicitly check the weak employer/title suspicion; weak identity alone never suppresses;
3. apply the normal cheap hard screen from `RULES.md`;
4. open/read the authoritative or best available full JD only for candidates that survive the cheap gate, subject to the 15-JD per-run cap;
5. verify liveness, cohort/degree/seniority/stack, employment type, SG work-pass or CN foreign-hire constraints where relevant, and the usable application route;
6. run targeted Gmail dedupe only for a serious survivor;
7. create only a new verified APPLY/CHECK Issue, then read it back before treating the survivor as durably handed off.

Candidates beyond the 15-JD budget that otherwise survive the cheap gate must be durably receipted as `budget_deferred`; they are never silently skipped.

Do not submit applications, contact employers, modify Gmail, or silently change existing opportunity Issues.

## Non-blocking retry rule

A transient candidate verification failure or a deep-read budget deferral must not stall later candidates.

If the candidate is otherwise worth preserving but a transient source/route/liveness/verification problem or the per-run deep-read budget prevents a terminal disposition, upsert a retry receipt with:

- `role_key`;
- `candidate_seq`;
- a compact `reason_code`;
- incremented `attempts`;
- `next_retry_at`;
- compact company/title/source URL fields needed for retry.

Once the retry receipt is durably written and read back, the main triage cursor may advance past that candidate and processing continues.

A failure to persist the retry receipt itself is an infrastructure blocker: do not advance the cursor past a candidate whose required durable receipt cannot be established.

## Cursor advancement

`triage-<market>.json` stores `last_consumed_candidate_seq`.

After the batch:

- advance to the highest processed batch `candidate_seq` only when every earlier candidate in that market batch was either terminally handled, durably handed off to an Issue, or durably moved into retry state;
- persist the cursor and retry file separately;
- read both back before claiming the FreeHire phase completed.

The cursor can advance over transient verification failures and deep-read budget deferrals only because those candidates have durable retry receipts.

## Relationship to fresh discovery

FreeHire remains Tier-3 radar.

The FreeHire batch never satisfies the market's fresh-platform requirements:

- SG still performs its broad-platform and research/lab rotation;
- CN still performs official-owner plus native-platform rotation;
- MY still performs its destination-quality broad-platform rotation and MY research recall.

Fresh discovery and FreeHire triage have separate metrics.

## Current bridge and future collector work

The current consumer is built from the full-current FreeHire cold-start snapshot because that snapshot contains enough substantive job text to avoid the recall loss of the old compact event log. The public raw event log remains available for audit/rebuild.

A future public cross-source triage event feed may replace this bridge once canonical identity-v2 and additional ATS adapters are proven. The private cursor/retry semantics should remain compatible: bounded candidate batches, strong-history suppression, weak suspicion only, and non-blocking retries.
