# Job Search Inbox Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the private `kolihhan/job-resources` repository into a minimal GitHub-Issues job inbox that is maintained hourly from two Gmail accounts and receives incremental SG + Mainland China discovery every four hours.

**Architecture:** GitHub Issues are the only operational state. Gmail is evidence. The repo itself contains only three small operating documents plus the approved spec/plan. No database, dashboard, spreadsheet mirror, or application code is added.

**Tech Stack:** GitHub Issues + GitHub Markdown + Gmail connector + ChatGPT Scheduled Task + web research.

**Spec:** `docs/superpowers/specs/2026-09-29-job-search-inbox-design.md`

## Global Constraints

- Repository remains private.
- Open Issue states are only `ACTION`, `APPLY`, `CHECK`, `WAIT`, encoded in the Issue title; no extra state taxonomy.
- One serious role/action = one Issue.
- GitHub Issues are the operational source of truth; Gmail is evidence; `/Job Applications/JOB_TRACKER.xlsx` becomes legacy/read-only reference.
- Never copy full email bodies, auth links/tokens, secrets, or unnecessary personal data into Issues.
- Exact application submission still requires user authorization for that exact role; `APPLY` is not permission to submit.
- Hourly maintenance runs every hour; full discovery only on MYT hours `00/04/08/12/16/20`.
- Scheduler/model routing may not guarantee GPT-5.6 Sol High; do not claim that it does.
- No custom app code unless GitHub Issues later proves inadequate in real use.

## Review Focus

- Same requisition found under a changed title: reuse/update the existing Issue, do not create another.
- Gmail receipt arrives for an `APPLY` Issue: change to `WAIT` without requiring manual `applied`.
- Gmail OA/interview/recruiter deadline arrives for a `WAIT` Issue: change to `ACTION` and preserve the role identity.
- Search finds a good role already applied from either Gmail account: create nothing new.
- Hourly run outside discovery hours: maintain state only; do not restart market research.

---

### Task 1: Initialize the minimal repository contract

**Files:**
- Create: `README.md`
- Create: `PROFILE.md`
- Create: `RULES.md`

**Interfaces:**
- Consumes: approved design spec.
- Produces: stable human-readable instructions that every later hourly run can read before touching Issues.

- [ ] **Step 1: Create `README.md`**

State that the user opens GitHub Issues as the primary UI, explain `ACTION/APPLY/CHECK/WAIT`, and document `go`, `applied`, `skip` comments. Keep it under roughly 120 lines.

- [ ] **Step 2: Create `PROFILE.md`**

Include only stable search facts: 2026 NTHU CS master's new graduate, Malaysian, SG needs employer-supported EP/S Pass, CN needs employer-supported foreign work permit, target role families, early-career seniority, career-capital-first preference, and truthful experience boundaries.

- [ ] **Step 3: Create `RULES.md`**

Encode the hourly maintenance order, four-hour discovery hours, issue qualification gate, dedupe key, privacy rule, company/JD research fields, and exact-role authorization boundary. Do not reproduce the full spec.

- [ ] **Step 4: Verify repository remains minimal**

Read repository root. Expected: `README.md`, `PROFILE.md`, `RULES.md`, and `docs/`; no app/database/dashboard files.

- [ ] **Step 5: Commit/read-back verification**

Fetch all three files and confirm they agree on the same four states and source-of-truth rule.

---

### Task 2: Migrate only current useful state into GitHub Issues

**Files:**
- No new files.
- Create/update: GitHub Issues only.

**Interfaces:**
- Consumes: both Gmail accounts, legacy tracker as read-only reference, `PROFILE.md`, `RULES.md`.
- Produces: the initial clean operational inbox.

- [ ] **Step 1: Reconcile current evidence**

Search both Gmail accounts for recent application receipts, OA/assessment invitations, interview/recruiter messages, rejections, and deadlines. Use the legacy tracker only to recover a role identity when Gmail evidence is insufficient.

- [ ] **Step 2: Build the migration set**

Include only:
- active time-sensitive `ACTION` items;
- credible current `WAIT` applications that are still useful to track;
- already-researched current `APPLY`/`CHECK` roles that remain live.

Exclude old rejected, expired, duplicate, stale, low-quality, and purely historical roles.

- [ ] **Step 3: Dedupe before every Issue creation**

Search existing Issues by primary fingerprint `market + company + req/job ID`; if no ID exists, use `company + role + location`.

Expected: no two open Issues represent the same requisition.

- [ ] **Step 4: Create Issues with complete decision context**

Each `APPLY`/`CHECK` Issue contains: direct apply link, checked date, company background that matters, actual role work, hard requirements, candidate fit/gaps, work-authorization evidence, supported salary/WLB evidence when available, two-Gmail dedupe result, and exactly one next action.

Each `ACTION`/`WAIT` Issue stores only the operational facts needed to act/track.

- [ ] **Step 5: Verify the morning view**

List open Issues. Expected: every open Issue starts with exactly one of `[ACTION]`, `[APPLY]`, `[CHECK]`, `[WAIT]`, and there are no obvious duplicates or historical clutter.

---

### Task 3: Create the hourly maintainer automation

**Files:**
- No repo files changed unless `RULES.md` needs a factual correction discovered during setup.

**Interfaces:**
- Consumes: private `kolihhan/job-resources` Issues + `README.md`/`PROFILE.md`/`RULES.md`, both Gmail accounts, public web research.
- Produces: hourly Issue maintenance and incremental discovery on MYT `00/04/08/12/16/20`.

- [ ] **Step 1: Create one hourly condition-watch task**

Schedule: `RRULE:FREQ=HOURLY`.

Prompt requirements:
- read repo rules/profile first;
- read open Issues;
- check both Gmail accounts;
- update existing Issues before discovery;
- receipt → `WAIT`;
- OA/interview/recruiter/time-sensitive deadline → `ACTION`;
- rejection/expired/duplicate/skip → close;
- outside MYT discovery hours, stop after maintenance;
- during MYT `00/04/08/12/16/20`, run incremental SG + CN discovery;
- prioritize established engineering/product employers and SWE/backend/platform/systems/ML-systems/Applied-AI families;
- deep-research only serious survivors;
- exact dedupe against both Gmail accounts + GitHub Issues before creating anything;
- never submit an application without exact-role user authorization;
- notify only for meaningful user action; otherwise stay quiet.

- [ ] **Step 2: Verify automation configuration**

Expected: one enabled hourly automation, not separate maintenance/discovery automations.

- [ ] **Step 3: Verify model-honesty boundary**

Confirm the task does not claim or depend on guaranteed GPT-5.6 Sol High routing.

---

### Task 4: Run one manual end-to-end cycle and clean up

**Files:**
- Modify only `README.md`, `PROFILE.md`, or `RULES.md` if the real run exposes a genuine rule ambiguity.

**Interfaces:**
- Consumes: completed Tasks 1-3.
- Produces: verified operating loop ready for unattended hourly maintenance.

- [ ] **Step 1: Run maintenance first**

Read open Issues and both Gmail accounts. Update any current receipts/outcomes/deadlines before searching for new roles.

- [ ] **Step 2: Run one discovery pass**

Find a small number of strong SG + CN candidates. Deep-check only survivors. Create Issues only for clean `APPLY`/`CHECK` candidates.

- [ ] **Step 3: Exercise duplicate protection**

Take one known applied requisition from Gmail and confirm the workflow creates no new Issue for it.

- [ ] **Step 4: Exercise state transition**

For one current application with official receipt evidence, verify the corresponding Issue is `WAIT`; for one current OA/deadline item, verify it is `ACTION`.

- [ ] **Step 5: Final read-back**

Open the Issues list as the user would in the morning. Expected: time-sensitive work is obvious, new good roles are reviewable, waiting applications are tracked, and no second tracker is needed.

- [ ] **Step 6: Stop adding architecture**

If the loop works, ship it. Do not add Projects, Actions workflows, a database, custom dashboard, or application code without a concrete failure that GitHub Issues cannot handle.
