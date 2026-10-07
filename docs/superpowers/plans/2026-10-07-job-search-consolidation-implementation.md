# Job Search Consolidation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consolidate the current job-search workflow so it searches wider, dedupes earlier, keeps one authoritative policy source, supports opportunistic Web3/PT/contract work, and avoids stale or duplicate leads without adding new infrastructure.

**Architecture:** Keep the current GitHub Issues + Gmail + small Markdown contract architecture. Move all execution policy into `RULES.md`, reduce scheduler/continuation prompts to thin bootstrap pointers, keep `DISCOVERY_STATE.md` as a cursor only, and load `WAIT` history on demand rather than in full every run.

**Tech Stack:** GitHub Issues, GitHub Markdown, Gmail connector, ChatGPT scheduled tasks, web research.

**Spec:** `docs/superpowers/specs/2026-10-07-job-search-consolidation-design.md`

## Global Constraints

- Do not add a database, dashboard, second tracker, scoring engine, scraper framework, or knowledge graph.
- GitHub Issues remain live opportunity state; Gmail remains evidence.
- `RULES.md` is the only detailed execution-policy source.
- SG + Mainland China full-time search remains primary; Web3 is secondary/opportunistic.
- Web3 may include credible full-time, part-time, contract, remote and project-based engineering work.
- Do not weaken freshness, dedupe or fit standards to increase job count; increase upstream search coverage instead.
- Do not treat same-company history as a permanent company blacklist; materially different roles may survive with an explicit reason.
- User-confirmed prior application history is valid dedupe evidence even without a Gmail receipt.
- Never submit an application or contact anyone without explicit authorization for that exact action.
- Verify every material repo, Issue and automation write by reading it back.

## Review Focus

- Same employer + similar role family + new requisition: suppress by default unless the role is materially different and the reason is recorded.
- Same employer + genuinely different role family: allow it to survive; do not over-dedupe into a company blacklist.
- Fresh-looking search/index result with stale underlying page: do not promote without current role-level liveness proof.
- Web3 PT/contract lead: allow employment-type flexibility but still reject anonymous, token-only, pay-to-work, seed-phrase or unverifiable opportunities.
- Large WAIT history: keep it queryable for dedupe while avoiding full reload on every hourly run.

---

### Task 1: Consolidate the authoritative repo contract

**Files:**
- Modify: `RULES.md`
- Modify: `PROFILE.md`

**Interfaces:**
- Consumes: approved consolidation spec and existing repo contract.
- Produces: one authoritative policy source plus stable candidate-scope facts used by all later tasks.

- [ ] **Step 1: Fetch the latest `RULES.md` and `PROFILE.md` and record their current blob SHAs.**

Expected: both files resolve on the default branch; abort this task on unresolved/conflicting versions rather than overwriting blindly.

- [ ] **Step 2: Update `RULES.md` with the approved discovery/promotion order.**

Required order:

`broad discovery → cheap hard filter → cheap dedupe → freshness proof → fit/cohort/work-auth → targeted Gmail dedupe → exact route → Issue`

Also add:
- broader source / employer / role-family rotation;
- zero-survivor stopping rule requiring meaningful lane variation;
- no fixed survivor quota;
- exact requisition dedupe;
- employer + role-family dedupe;
- materially-different-role exception;
- user-confirmed application evidence;
- selective WAIT loading;
- DISCOVERY_STATE reconciliation after a same-session survivor is invalidated;
- Web3 secondary lane with PT/contract/remote allowed and safety/quality filters.

- [ ] **Step 3: Update `PROFILE.md` only with stable scope, not execution rules.**

Add that credible Web3 engineering work may be considered opportunistically, including part-time/contract/remote work, while SG/CN full-time engineering remains the main objective.

Do not duplicate freshness, dedupe or source-rotation policy here.

- [ ] **Step 4: Read back both files and verify source-of-truth separation.**

Expected:
- `RULES.md` contains detailed execution policy;
- `PROFILE.md` contains only stable candidate/search scope facts;
- no new tracker/state file appears.

---

### Task 2: Thin the continuation and scheduler prompts

**Files:**
- Modify: `NEXT_CHAT_PROMPT.md`
- External config: automation `Job Inbox Maintainer` (`6abbe77330788191b8b4fb0c7f48d1b8`)

**Interfaces:**
- Consumes: Task 1 authoritative `RULES.md`.
- Produces: bootstrap-only prompts that restore state and defer execution details to repo policy.

- [ ] **Step 1: Rewrite `NEXT_CHAT_PROMPT.md` as a thin continuation pointer.**

It should require a new chat to:
- read `README.md`, `PROFILE.md`, `RULES.md`, `DISCOVERY_STATE.md`, and relevant Issues;
- check both Gmail accounts when required by the repo contract;
- execute the current repo rules;
- never reconstruct policy from the prompt itself;
- never submit/contact without exact authorization.

Remove duplicated source lists, dedupe logic, freshness logic, market-search instructions and other policy already in `RULES.md`.

- [ ] **Step 2: Read back `NEXT_CHAT_PROMPT.md` and verify it no longer carries a private copy of discovery policy.**

Expected: it behaves as a bootstrap pointer, not a second rulebook.

- [ ] **Step 3: Update `Job Inbox Maintainer` to the same thin-bootstrap shape.**

The prompt should instruct the task to:
- read the current repo contract first;
- execute one maintenance/discovery cycle under it;
- load only Issue context required by the contract;
- verify material writes;
- stay quiet unless user action/failure/unusually strong genuinely new opportunities require surfacing;
- never submit/contact without explicit authorization.

Do not duplicate the detailed company-family dedupe or Web3 rules into the scheduler prompt.

- [ ] **Step 4: Read back the automation configuration and compare it with `RULES.md`.**

Expected: scheduler contains pointers and safety boundary only; detailed search/dedupe/freshness policy lives in `RULES.md`.

---

### Task 3: Reconcile discovery runtime state and health monitoring

**Files:**
- Modify: `DISCOVERY_STATE.md`
- External config: automation `Job System Health Watch` (`6ac50fc29be48191928e83d82f6ca2af`)

**Interfaces:**
- Consumes: Task 1 contract and current Issue outcomes.
- Produces: a truthful next-rotation cursor and a health checker that detects drift without becoming another policy source.

- [ ] **Step 1: Reconcile `DISCOVERY_STATE.md` with the latest outcomes.**

Required correction:
- #151 Huawei and #152 Autodesk must no longer be presented as live serious survivors because both were closed as duplicates.

Keep only:
- latest completed-run receipt;
- broad source/employer/role lanes actually tried;
- real surviving Issues, if any;
- concrete failures;
- next rotation.

The next rotation should expand new-company/source/role-family coverage and may include an opportunistic Web3 engineering lane without displacing SG/CN.

- [ ] **Step 2: Read back `DISCOVERY_STATE.md` and verify it contains no policy prose and no stale live-survivor claim.**

- [ ] **Step 3: Update `Job System Health Watch` to enforce invariants, not re-specify policy.**

It should detect:
- maintainer stopped/stale;
- Gmail/GitHub state mismatch;
- new CHECK/APPLY violating current repo freshness/dedupe/state rules;
- same-company/same-role-family duplicate regressions when existing history clearly conflicts;
- closed/open-state title-label inconsistency;
- discovery receipt not reconciled after a survivor is invalidated;
- policy drift where scheduler/continuation behavior materially contradicts `RULES.md`.

It should still read current `RULES.md` rather than embedding detailed copies of those rules.

- [ ] **Step 4: Read back the health-watch configuration and confirm it is an invariant checker, not a second rulebook.**

---

### Task 4: Fix only current state inconsistencies exposed by the audit

**Files:**
- Modify: current GitHub Issues only when their present state contradicts the authoritative state definitions.

**Interfaces:**
- Consumes: Task 1 state definitions.
- Produces: a clean current-action view without broad historical cleanup.

- [ ] **Step 1: Inspect all current `ACTION`, `APPLY`, and `CHECK` Issues plus recently changed WAIT items only.**

Do not broad-clean historical WAIT/closed Issues.

- [ ] **Step 2: Reclassify Issue #123 if its current content still says the role is a substantial mismatch and only a user continue/skip decision remains.**

Expected state under the approved model: `CHECK`, not `ACTION`, because there is no high-value employer action that deserves urgent attention; the blocker is a user decision.

Do not close it as skipped without an explicit user skip decision.

- [ ] **Step 3: Leave genuine deadline/action items such as #122 as `ACTION` if their current evidence still supports that state.**

- [ ] **Step 4: Read back every Issue changed in this task.**

Expected: title, market label, status label, body, next action and open/closed state agree.

---

### Task 5: Run one end-to-end discovery smoke test under the consolidated contract

**Files:**
- Modify: GitHub Issues and `DISCOVERY_STATE.md` only if genuinely warranted by the run.

**Interfaces:**
- Consumes: Tasks 1-4 completed state.
- Produces: evidence that the new rules improve both recall and precision in real use.

- [ ] **Step 1: Restore runtime state using the thin-context rule.**

Fully load ACTION/APPLY/CHECK; load WAIT/closed history only when triggered by Gmail or exact employer/role-family dedupe.

- [ ] **Step 2: Run broad SG + CN discovery with meaningful variation in source, employer cluster and role family.**

Do not stop after one or two familiar employers or one platform.

- [ ] **Step 3: Include one opportunistic Web3 engineering search lane.**

Allow credible FT/PT/contract/remote backend/infra/tooling/data/AI×Web3 opportunities; do not lower verification standards.

- [ ] **Step 4: Exercise the early-dedupe regression cases.**

Expected:
- another Huawei AI-application-family role is suppressed before expensive research unless materially different;
- another Autodesk same-family SWE role is suppressed before expensive research unless materially different;
- a genuinely different same-company role may continue only with a recorded reason.

- [ ] **Step 5: Exercise freshness discipline on at least one candidate whose current liveness cannot be proven.**

Expected: it remains raw discovery and creates no CHECK/APPLY Issue.

- [ ] **Step 6: Create/update Issues only for genuine serious survivors, if any.**

Zero survivors is acceptable if the run demonstrably broadened source/employer/role lanes and preserved the strict promotion gate.

- [ ] **Step 7: Update and read back `DISCOVERY_STATE.md` with the real run receipt and next rotation.**

If a newly-created survivor is invalidated during the same run, reconcile the receipt before finishing.

---

### Task 6: Final consistency verification

**Files:**
- Read-only verification across repo files, current Issues and automations.

**Interfaces:**
- Consumes: all previous tasks.
- Produces: evidence that the system is consolidated and ready to resume normal maintenance.

- [ ] **Step 1: Read `README.md`, `PROFILE.md`, `RULES.md`, `NEXT_CHAT_PROMPT.md`, `DISCOVERY_STATE.md`, the approved spec, and this plan.**

Verify there is one detailed execution-policy source: `RULES.md`.

- [ ] **Step 2: Read current ACTION/APPLY/CHECK Issue list and verify state consistency.**

- [ ] **Step 3: Read both active job-search automation configs.**

Expected:
- Job Inbox Maintainer = thin bootstrap executor;
- Job System Health Watch = invariant checker;
- neither duplicates detailed repo policy.

- [ ] **Step 4: Verify no new database, dashboard, tracker, score file, code framework or knowledge-graph artifact was introduced.**

- [ ] **Step 5: Report only concrete outcomes and any remaining blocker.**

Do not claim the system is fixed unless the read-back evidence confirms the repo, Issue state and automations agree.
