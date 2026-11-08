# FreeHire Triage Consumption

This is the canonical downstream contract for hourly SG/CN/MY FreeHire triage. Other active docs should reference this file instead of restating throughput numbers.

The old raw `feed/pages/*.jsonl` sequence-recovery path is audit/rebuild history only.

## Pipeline

`full current FreeHire scan with substantive JD text -> conservative machine candidate set -> private strong-history dedupe -> stable candidate_seq -> compact metadata batch -> hourly scout -> authoritative JD only when needed`

GitHub Issues remain the only live human opportunity state.

## Why transport is compact

The full cold-start snapshot keeps substantive job text because the machine filter needs it for recall. Hourly scout shards do **not** carry JD bodies or arbitrary raw payload fields. They carry only compact identity/screening metadata such as:

- `candidate_seq`, `role_key`, `public_slug`;
- company/title/location/market;
- source/source URL/external ID;
- known-history status/basis;
- AI score/signals and machine flags;
- employment type and relevant timestamps.

The scout opens the authoritative or best available source URL for substantive JD verification. Connector safety comes from bounded metadata payload, **not** from assuming a fixed number of full-JD records is always small enough.

## Machine state

Derived by the repo workflow:

- `discovery-state/freehire-review-registry.json`
- `discovery-state/freehire-batch-{sg,cn,my}.json` — manifests only
- manifest-listed `freehire-batch-<market>-NN.json` — compact candidate metadata shards
- `discovery-state/freehire-coldstart-summary.json`

Market-owned mutable state:

- `discovery-state/triage-<market>.json`
- `discovery-state/retry-<market>.json`

These files are machine-efficiency state, not a second opportunity tracker.

## Identity

`freehire:<public_slug> -> candidate_seq`

`candidate_seq` is a stable private consumption sequence, not a cross-source canonical role identity. Strong cross-source/history suppression still follows `docs/source-routing.md` and the final all-Issue-history gate. Weak company/title matches are suspicion only and never auto-suppress.

## Hourly budget

Per market run:

- process up to **15 due retries**, prioritizing actionable new evidence and `budget_deferred` candidates;
- cheap-screen up to **200** current batch candidates;
- perform at most **25 normal substantive full-JD reads** for plausible candidates;
- audit up to **5 cheap rejects** with independent full-JD reads to estimate false-negative risk.

The reject-audit reads are separate from the 25 normal deep-read budget because they measure the cheap filter rather than serve candidate promotion.

If more than 25 plausible candidates survive the cheap gate, preserve every extra candidate as a durable `budget_deferred` retry receipt. Never silently skip it and never freeze later candidates merely because the deep-read budget is exhausted.

## 1. Due retries

Process up to 15 receipts whose `next_retry_at` is due. Prioritize `budget_deferred` (especially previously unread), changed authoritative evidence, impending deadlines, and high North-Star relevance before old repeatedly blocked receipts. Reserve at least 10 of the 15 slots for those actionable categories when that many are due; at most 5 slots should go to repeated no-new-evidence cases. An inaccessible old source is not automatically higher priority merely because its receipt is oldest. `budget_deferred` is normal backlog work, not an infrastructure failure.

Resolve/remove a receipt when the role becomes an exact historical duplicate, reaches a terminal disposition, or a verified APPLY/CHECK Issue is created and read back.

## Read-only JD source probe (bounded preflight)

For plausible candidates **after** the exact all-Issue-history gate and cheap hard screening, prefer the repository helper `scripts/jd_source_probe.py` when a Python execution environment is available:

```bash
python scripts/jd_source_probe.py --self-test
python scripts/jd_source_probe.py --input discovery-state/freehire-batch-sg-01.json --limit 10
python scripts/jd_source_probe.py --input discovery-state/freehire-batch-sg-01.json --limit 10 --fetch
```

Run against an actual manifest-listed shard (or a bounded JSON candidate list); do not assume a fixed shard number or number of candidates. The helper removes tracking parameters, labels official/native vs radar sources, identifies explicit ATS requisition hints, attempts supported public SmartRecruiters/Greenhouse JSON endpoints before the original link, and emits exact-title/ID fallback searches. It uses **only read-only GET**, bounded size/time and a strict source-host allowlist. If the scout runtime cannot execute Python or lacks network, perform the equivalent bounded official/ATS search using available tools; never claim the script ran.

Interpret evidence conservatively:
- `JD_CONTENT_FOUND` means a substantive, title-matching JD was retrieved, **not** that the position is still open, early-career eligible, permanent or directly applicable.
- `SOURCE_UNVERIFIED`, `NOT_FETCHED`, `RADAR_OR_UNKNOWN`, and transient HTTP failures require an authoritative alternate source or a durable retry. Never turn a JS application shell or a generic company home page into a verified JD.
- Separately confirm (1) exact requisition identity, (2) current vacancy, (3) **full JD and hard requirements**, (4) appropriate contract/work authorization, and (5) real application route. For an explicit hard mismatch in a current full JD, make the normal terminal decision; do not indefinitely retry that candidate as an "unreadable JD".
- The helper is a preflight aid, not an independent candidate database; do not write its JSONL output as a second inbox. Only canonical GitHub Issues, terminal dispositions and existing retry/cursor state may hold decisions.

Use the expanded **25 substantive JD reads / 15 due retries** trial limit. Count a true alternate-source substantive JD as evidence; do not count a 200/302 response, another mirrored snippet, or a retry increment as progress.

## 2. Current batch — resumable contiguous-prefix processing

1. Read `discovery-state/freehire-batch-<market>.json` and the market triage/retry cursors. Identify the **first candidate not terminally handled, durably receipted or already handed off**. Do not repeatedly read already-consumed shards merely to recreate an aggregate count.
2. Read the manifest-listed shards containing the **next contiguous unhandled candidate prefix** in manifest order, in batches of at most 8 files per connector call. Verify each read shard's identity, count and candidate sequence. **Process that prefix immediately** through exact Issue-history dedupe, cheap hard screens and a bounded selection of substantive JDs; do not defer all candidate decisions until after all 24+ shards are fetched.
3. As candidate decisions accumulate, persist terminal dispositions, verified Issue handoffs and required `budget_deferred`/unverified retry receipts with read-back. Advance the triage cursor **only through a fully resolved or durably receipted contiguous prefix**; validate the cursor and retry file independently before claiming progress. An incomplete last shard must not be marked consumed.
4. After a validated checkpoint, continue with the next unread shard/prefix only if tool/runtime capacity remains. The **200 cheap screens / 25 normal JD reads / 15 due retries / 5 reject audits are ceilings, not preconditions to getting useful work done**. Prioritize finishing at least one substantive eligible-candidate decision and a meaningful contiguous prefix over reading a whole manifest without dispositions.
5. Only when **all manifest-listed shards** have been read, counts reconciled, and every candidate terminally handled/durably receipted may the run claim the full batch reconciled/consumed. Otherwise record the actual shards/candidates processed, prefix cursor, remaining batch size and PARTIAL_COVERAGE; never call the batch empty/exhausted or imply missing shards were processed.
6. If a shard is missing, truncated, unreadable, mismatched or the state write fails, do not advance past unread/unpersisted candidates. Preserve the blocker and resume from the last validated cursor next run. Never guess forward.

For each candidate:

1. exact all-Issue-history dedupe before expensive work;
2. explicitly resolve `known_status=suspected_known` rather than auto-dropping it;
3. apply only high-confidence cheap hard screens from `RULES.md` using compact metadata/signals/known campaign evidence;
4. open the authoritative or best available full JD for candidates that survive, subject to the 25 normal deep-read budget;
5. verify liveness, eligibility, cohort/degree/seniority/stack, employment type, work authorization constraints, and usable route;
6. run targeted Gmail dedupe only for serious survivors;
7. create/read back only a new verified APPLY/CHECK Issue.

Do not submit applications, contact employers, or modify Gmail automatically.

## 3. Reject audit — anti-overfit / recall check

A high cheap-reject count proves throughput, not recall. Each run with enough cheap rejects must audit up to 5 of them.

Choose a small stratified sample rather than only the easiest rejects. Prefer coverage across:

- different reject reasons;
- different sources;
- generic titles with AI signals;
- borderline AI scores/signals;
- research vs engineering titles where present.

For each sampled reject, open/read the authoritative or best available substantive JD and ask whether the original cheap terminal decision was still correct under current `PROFILE.md`/`RULES.md`.

Record:

- `reject_audit_sampled`;
- `reject_audit_false_negatives`.

If an audited reject is actually a serious eligible survivor, count one false negative and route it through the **normal** exact-history, liveness, eligibility, Gmail and APPLY/CHECK gates. Do not silently change the cheap filter from one anecdote. Repeated false negatives with the same mechanism are evidence for a later rule change.

Exact-history duplicates are not part of the reject-audit sample because they test dedupe, not fit recall.

## Retry rule

### Retry escalation — stop repeating the same inaccessible URL

A persisted retry is not proof of progress. For each due receipt, retain the stable job identity and prior evidence while choosing a **new verification route** when the previous route failed:

- First failed authoritative open: try the employer careers/ATS search by exact requisition ID or exact title/location; use one faithful full-JD reproduction if needed.
- On a repeated same-blocker retry, do **not** consume another deep-read slot re-opening exactly the same failed URL without new evidence. Switch to another source, employer contact/route discovery (read-only), or defer the record with an explicit source-specific blocker.
- After three attempts with no new substantive evidence, use a longer retry interval (at least 24 hours) unless a published closing date or exceptional GOLD research signal makes immediate alternate-route investigation worthwhile. After five **no-progress** attempts, require at least 72 hours between routine retries and a materially different verification path or new source signal before spending another substantive deep-read slot. Keep all unverified roles safely receipted; do not auto-reject an eligible unknown or repeatedly research the same broken page.
- For legacy high-attempt receipts, inspect the stored history: if no new substantive evidence or alternate source exists, reschedule rather than reopening the same page. Do not rewrite the entire historical backlog merely to apply this policy.
- Prioritize due retries with **new evidence, upcoming deadlines, or high North-Star content**, then oldest receipts among otherwise comparable candidates. Keep the 15-slot cap; avoid starving new discovery to exhaust an inert backlog. Avoid spending the whole verification budget repeatedly on inert aggregator mirrors.

Every retry records whether **new substantive evidence** was obtained (yes/no) and the alternate source attempted. Do not mark a verification completed merely because the URL was opened, the attempt counter increased, or a new next_retry_at was saved. Deduped/terminal/verified candidates still exit through the existing normal gates.


Transient verification failures and deep-read budget deferrals must not stall later candidates. Persist a compact receipt containing at least:

- `role_key` / `candidate_seq`;
- reason code / attempts / `next_retry_at`;
- compact company/title/source URL identity.

After the receipt is written and read back, the main cursor may continue. Failure to persist a required receipt is an infrastructure blocker.

## Cursor advancement

Advance `triage-<market>.json:last_consumed_candidate_seq` only when every earlier batch candidate is one of:

- terminally handled;
- durably handed off to an Issue;
- durably moved into retry state.

Persist/read back cursor and retry state before claiming completion.

## Fresh discovery remains independent

FreeHire is Tier-3 radar and never satisfies fresh-platform obligations. SG/MY/CN continue their market rotations in `docs/fresh-discovery-rotation.md`.

## Throughput and recall evaluation

These larger limits are trial ceilings, not targets or guaranteed improvements. In the existing scout run metrics record, report actual cheap-screen count, normal substantive reads, retry cases by new evidence vs repeated no-progress, deferred backlog, platform overlap/dedupe, discovered unique new identities, and final durable APPLY/CHECK handoffs. Track budget exhaustion, timeouts, and PARTIAL_COVERAGE. Compare at least SG and MY or a later independent run before treating the trial as an improvement. If tools/runtime are exhausted, stop truthfully, preserve all unresolved candidates through durable receipts, and never mark unfinished exploration complete.

## Validation principle

Do not declare a transport/filter change successful from the market or batch used to design it. After a change:

- verify tests/derived state in GitHub Actions;
- validate on another market or later batch;
- inspect reject-audit false negatives before tightening cheap filters.

The current compact-transport change should therefore be validated first on SG/MY, where the previous full-payload shards actually truncated, rather than using the earlier successful CN batch as self-confirmation.
