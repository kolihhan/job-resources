# Maintainer Reliability Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add four small reliability guardrails to the existing job-search maintainer: auditable discovery coverage, hard-vs-soft requirement parsing, same-window discovery idempotency, and retry-safe ambiguous GitHub issue creation.

**Architecture:** Keep the existing repo contract intact. `RULES.md` remains the only detailed policy source; `DISCOVERY_STATE.md` remains one rolling receipt; scheduler prompts remain thin. Verification is done through exact file read-back, automation read-back, and concrete regression scenarios rather than a new test framework.

**Tech Stack:** Markdown policy files, GitHub Issues, ChatGPT Automations, Gmail evidence, web/job discovery sources.

**Spec:** `docs/superpowers/specs/2026-10-08-maintainer-reliability-hardening-design.md`

## Global Constraints

- Do not create a second tracker, database, dashboard, score, scraper framework, knowledge graph, or agent framework.
- Do not change the hourly maintainer cadence or the `00/04/08/12/16/20` MYT discovery schedule.
- Do not introduce minimum candidate/employer/source/survivor quotas.
- Do not weaken freshness, dedupe, sponsorship, cohort, seniority, or route gates.
- Keep detailed policy in `RULES.md`; automation prompts only point to and enforce that contract.
- Do not submit applications or contact anyone.

## Review Focus

1. **Counter inflation:** duplicate mirrors of one job must not count as multiple candidates; regression is owned by Task 1.
2. **Soft-to-hard distortion:** `preferred`, `familiarity`, coursework/self-study/personal-project wording must not become fabricated professional-experience blockers; regression is owned by Task 1 and Task 4.
3. **Interactive/scheduled collision:** a narrow interactive lookup must not suppress a scheduled full run, while a full compliant interactive SG+CN run in the same window should; regression is owned by Task 1 and Task 4.
4. **Ambiguous write duplication:** timeout/5xx after `create_issue` must trigger search/read-back before any retry; regression is owned by Task 1 and Task 4.
5. **Policy drift:** maintainer and health-watch prompts must not copy the new rules in detail; regression is owned by Task 2 and Task 4.

---

### Task 1: Add the four guardrails to the canonical repo contract

**Files:**
- Modify: `RULES.md`
- Read for consistency only: `README.md`, `NEXT_CHAT_PROMPT.md`, `PROFILE.md`

**Interfaces:**
- Consumes: approved design in `docs/superpowers/specs/2026-10-08-maintainer-reliability-hardening-design.md`.
- Produces: the sole detailed policy that later tasks and automations obey.

- [ ] **Step 1: Capture pre-change assertions from `RULES.md`**

Verify and record that the current file lacks all four complete behaviors: compact coverage-count definitions, explicit hard-vs-soft wording, four-hour same-window completion semantics, and ambiguous-create search-before-retry behavior.

Expected: at least one element of each behavior is absent or incomplete; otherwise stop and reconcile before editing.

- [ ] **Step 2: Update discovery receipt rules**

Add compact coverage fields for SG/CN and optional Web3: candidates cheap-screened, distinct employers, source families, and deep-verified. Define candidate/employer/source-family/deep-verified exactly as in the spec and state explicitly that there is no numeric minimum or quota.

- [ ] **Step 3: Update cheap-screen requirement parsing**

State that only genuine hard blockers may cause cheap rejection. Preserve `preferred`, `familiarity`, `exposure`, coursework, self-study, personal-project, willingness-to-learn, and ambiguous wording for Stage 2 unless the surrounding JD makes them mandatory.

- [ ] **Step 4: Add same-window discovery idempotency**

Define the six four-hour MYT windows. A valid full SG+CN receipt in the current window causes later scheduled maintainer runs in that window to do maintenance only. Narrow interactive probes do not consume the window; a full compliant interactive run may.

- [ ] **Step 5: Add ambiguous-create retry safety**

For create operations with possible duplicate side effects: one create attempt; on timeout/connection error/transient 5xx, search recent Issues by exact req and employer+role fingerprint before retry; adopt an existing delayed creation; otherwise retry once; persistent ambiguity stops and is reported.

- [ ] **Step 6: Read back `RULES.md` and run textual regressions**

Verify all assertions:
- duplicate mirrors count once;
- no coverage minimum exists;
- `5+ years required` remains a cheap blocker;
- coursework/self-study familiarity is not treated as professional experience;
- `00:18` full compliant discovery blocks ordinary `00:30` scheduled rediscovery;
- a narrow `00:18` role lookup does not;
- ambiguous create says search/read-back before retry and caps retry at one.

- [ ] **Step 7: Commit**

Commit only the canonical rule change with a focused message such as `Harden maintainer discovery reliability`.

---

### Task 2: Keep automation prompts thin while making health checks aware of the new contract

**Files / surfaces:**
- Inspect/update automation: `Job Inbox Maintainer` (`6abbe77330788191b8b4fb0c7f48d1b8`)
- Inspect/update automation: `Job System Health Watch` (`6ac50fc29be48191928e83d82f6ca2af`)
- Read only: `NEXT_CHAT_PROMPT.md`

**Interfaces:**
- Consumes: finalized `RULES.md` from Task 1.
- Produces: schedulers that defer to the repo contract without becoming a second copy of it.

- [ ] **Step 1: Read current automation definitions**

Use automation read-back and verify the maintainer remains a thin pointer to `README.md`, `PROFILE.md`, `RULES.md`, and `DISCOVERY_STATE.md`.

- [ ] **Step 2: Decide whether maintainer prompt needs any edit**

If it already says to execute under current repo rules and does not contain conflicting old same-window behavior, leave it unchanged. Do not add the four detailed rules to the prompt.

- [ ] **Step 3: Add only health invariants that are not policy copies**

Health Watch may flag: malformed/missing coverage fields after a scheduled discovery; repeated scheduled discovery within an already-complete current window; or automation behavior contradicting current `RULES.md`. Phrase these as invariant checks and point back to `RULES.md`.

- [ ] **Step 4: Read back both automations**

Verify:
- no detailed hard-vs-soft list is copied into either prompt;
- no numeric coverage minimum is introduced;
- maintainer cadence is unchanged;
- health watch is still `condition_watch` and quiet when healthy.

---

### Task 3: Migrate the rolling discovery receipt without inventing historical counts

**Files:**
- Modify: `DISCOVERY_STATE.md` only when a new real discovery run is performed.

**Interfaces:**
- Consumes: receipt schema in `RULES.md`.
- Produces: the first compliant coverage-aware receipt used by same-window idempotency.

- [ ] **Step 1: Do not backfill guessed counts**

Read the current receipt. Preserve its historical truth; do not estimate counters for a past run from qualitative prose.

- [ ] **Step 2: Run one controlled full discovery when execution reaches an eligible window or explicit interactive validation run**

Cover both SG and CN under the normal wide-search/strict-promotion contract; Web3 is optional. Track the four counters during the run from actual candidates inspected.

- [ ] **Step 3: Write the new receipt**

Include run time, source/employer/role lanes, compact SG/CN coverage counters, optional Web3 counters, survivors, concrete blockers/errors, and next rotation. Do not include a raw candidate dump.

- [ ] **Step 4: Read back and sanity-check counts**

Verify candidate counts are deduped across mirrors, distinct employer counts do not exceed candidates, deep-verified does not exceed candidates, and source-family counts reflect materially distinct channels.

- [ ] **Step 5: Verify same-window completion semantics**

If the controlled run was full and compliant, confirm a later scheduled run in the same four-hour window would be maintenance-only according to the receipt timestamp and `RULES.md`.

---

### Task 4: Run end-to-end regression checks against real examples

**Files / surfaces:**
- Read: `RULES.md`, `DISCOVERY_STATE.md`, relevant Issues and Gmail evidence
- Search current web/job sources for regression examples
- No application or outreach writes

**Interfaces:**
- Consumes: Tasks 1-3.
- Produces: evidence that the four guardrails work without reducing freshness/dedupe precision.

- [ ] **Step 1: Hard-vs-soft control — Qore3-type wording**

Use a current fresh-graduate-compatible Web3/JD example with wording equivalent to coursework/self-study/personal-project familiarity. Expected: it survives cheap filtering on that dimension and proceeds to normal freshness/fit/dedupe/route checks; this does **not** imply automatic Issue creation.

- [ ] **Step 2: Hard-requirement control**

Use a role with unambiguous `5+ years required` or equivalent mandatory production experience. Expected: cheap reject remains allowed.

- [ ] **Step 3: Freshness control**

Use a search result/mirror whose official role is expired or whose current application flow cannot be proven. Expected: it still does not become `CHECK`/`APPLY` merely because the search result is fresh.

- [ ] **Step 4: Dedupe control**

Use a known same-employer/same-role-family application history (for example Huawei AI-family or Autodesk SWE-family history). Expected: early suppression still occurs before expensive research unless the new role is materially different with an explicit reason.

- [ ] **Step 5: Same-window control**

Evaluate the actual current receipt/window. If a full compliant discovery already completed in the current window, the next scheduled maintainer should skip discovery; if the latest activity was only a narrow probe, it should not.

- [ ] **Step 6: Ambiguous-write control without creating a disposable Issue**

Inspect the historical Chainlabs `#156/#157` incident and verify the new rule would have forced search/read-back before retry. Do not intentionally create another duplicate just to test the rule.

- [ ] **Step 7: Whole-system read-back**

Verify:
- `RULES.md` is still the only detailed policy source;
- README/NEXT_CHAT_PROMPT remain thin/pointer-oriented;
- automations are enabled with original cadence/modes;
- `DISCOVERY_STATE.md` is compact and current;
- no new tracker/framework/file family was created beyond spec/plan history;
- no applications or external contacts were sent.

- [ ] **Step 8: Report only evidence-backed residual risks**

If coverage is still low, report the measured counters rather than immediately adding a quota. If false-negative parsing still appears, capture the exact JD wording and failure before proposing another rule.
