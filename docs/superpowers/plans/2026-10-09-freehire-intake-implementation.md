# FreeHire Intake Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a free public FreeHire ingestion worker, connect it to one dedicated private hourly intake scheduler, and remove duplicate FreeHire discovery from the existing maintainer without creating a second job tracker.

**Architecture:** `kolihhan/freehirefetch` owns public API ingestion, exact machine dedupe, bounded public state, and GitHub Actions scheduling. A dedicated private ChatGPT automation consumes only new/changed feed events and performs the existing `job-resources` Stage-2 verification. The existing Job Inbox Maintainer continues Gmail lifecycle and non-FreeHire discovery.

**Tech Stack:** Python 3 standard library, unittest, GitHub Actions public standard runner, GitHub repository files as bounded public transport state, ChatGPT automations, existing GitHub/Gmail connectors.

**Spec:** `docs/superpowers/specs/2026-10-09-freehire-intake-architecture-design.md`

## Global Constraints

- Public worker must remain free: no paid API, no private runner, no required secret, no browser automation.
- Public worker must contain no Gmail, application history, private Issues, candidate profile, sponsorship history, recruiter notes, or private resume data.
- Bootstrap reaches FreeHire's documented deep-page limit when enough rows exist; initial emitted events are limited to jobs FreeHire first saw within 7 days.
- Hourly delta uses `open_within_days=2`; daily full scan is a recovery/state-refresh backstop.
- FreeHire enrichment fields are hints only; they may produce flags but not hard reject by themselves.
- Public event and seen-state retention is 30 days; event sequence numbers are globally monotonic and never renumbered.
- `DISCOVERY_STATE.md` remains a receipt/cursor only; GitHub Issues remain the only live opportunity state.
- Private intake consumes events in ascending sequence and advances only a contiguous processed cursor.
- Private intake deep-verifies at most 20 serious survivors per run.
- Existing maintainer stops normal repeated FreeHire discovery after handoff.
- No application or external contact occurs without explicit user authorization.
- Scheduled ChatGPT tasks run in Chat mode with high reasoning effort and must not invoke Work mode.

## Review Focus

1. **FreeHire silently ignores a requested filter** — worker must fail without publishing new state/feed; Task 1 tests `ignored_params` and Task 2 validates failed workflow behavior.
2. **The hourly job reruns the same recent rows** — exact identity/fingerprint logic must emit no duplicate event and remain idempotent; Task 1 tests NEW/unchanged/CHANGED classification.
3. **Feed retention overtakes the private cursor** — private scheduler must detect `cursor < health.first_seq` and stop normal consumption; Task 3 acceptance covers cursor-gap handling.
4. **A GitHub write times out after actually succeeding** — private intake must search/read back before retry so it cannot create duplicate Issues; Task 3 prompt explicitly preserves the existing write-safety rule.
5. **A large backlog contains many cheap duplicates before a few valid survivors** — intake must consume cheap terminal events while preserving sequence and stop before the 21st Stage-2 survivor; Task 3 acceptance tests contiguous cursor advancement and the 20-survivor budget.

---

### Task 1: Build the public FreeHire worker core

**Files:**
- Create: `kolihhan/freehirefetch/freehire_fetch.py`
- Create: `kolihhan/freehirefetch/tests/test_freehire_fetch.py`
- Create: `kolihhan/freehirefetch/state/seen.json`
- Create: `kolihhan/freehirefetch/feed/events.jsonl`
- Create: `kolihhan/freehirefetch/health.json`
- Create: `kolihhan/freehirefetch/README.md`

**Interfaces:**
- Consumes: FreeHire public `GET /api/v1/jobs/search`; CLI mode `bootstrap|delta|full`.
- Produces: `feed/events.jsonl`, `state/seen.json`, `health.json`; exit code `0` only after a complete valid run.
- Required CLI: `python freehire_fetch.py --mode {bootstrap,delta,full}`.
- `delta` uses `open_within_days=2`; bootstrap emission cutoff is 7 days; page size is 100 and deep-page cap is 10,000 rows per market.

- [ ] **Step 1: Write failing pagination/API-contract tests**

Add tests named:
- `test_page_offsets_cover_10000_rows_exactly`
- `test_fetch_stops_when_reported_total_is_exhausted`
- `test_fetch_fails_when_requested_filter_is_ignored`
- `test_delta_params_use_open_within_days_2`

Assertions must pin page size `100`, final offset `9900`, and `open_within_days == 2`.

- [ ] **Step 2: Run the pagination/API-contract tests and verify RED**

Run: `python -m unittest tests.test_freehire_fetch.FreeHireWorkerTests -v`

Expected: failures because the worker functions do not yet exist.

- [ ] **Step 3: Implement API pagination and validation**

In `freehire_fetch.py`, define:
- `page_offsets(max_rows: int = 10_000, page_size: int = 100) -> list[int]`
- `build_params(country: str, mode: str, offset: int) -> dict[str, object]`
- `fetch_market(fetch_json, country: str, mode: str) -> list[dict]`

Use bounded retry/backoff in the real HTTP adapter; raise on ignored requested filters or malformed contract-level responses.

- [ ] **Step 4: Run the pagination/API-contract tests and verify GREEN**

Run: `python -m unittest tests.test_freehire_fetch.FreeHireWorkerTests -v`

Expected: the four API-contract tests pass.

- [ ] **Step 5: Write failing conservative-filter and fingerprint tests**

Add tests named:
- `test_title_hard_drop_rejects_explicit_senior_and_intern`
- `test_enrichment_5_years_becomes_flag_not_reject`
- `test_same_identity_same_fingerprint_emits_nothing`
- `test_same_identity_changed_fingerprint_emits_changed`
- `test_unseen_identity_emits_new`

- [ ] **Step 6: Run the new tests and verify RED**

Run: `python -m unittest tests.test_freehire_fetch.FreeHireWorkerTests -v`

Expected: failures because classification/state logic is missing.

- [ ] **Step 7: Implement machine classification**

Define:
- `machine_flags(job: dict) -> tuple[bool, list[str]]` where the boolean means explicit title hard-drop.
- `job_identity(job: dict) -> str`
- `content_fingerprint(job: dict) -> str`
- `classify_events(jobs: list[dict], seen: dict, now_iso: str, bootstrap: bool) -> tuple[list[dict], dict]`

Only explicit title-level Senior/Staff/Principal/Lead/Director/Head/Manager/Intern mismatches may hard-drop. Enrichment-derived experience/seniority/employer-type/work-auth values only add flags.

- [ ] **Step 8: Run classification tests and verify GREEN**

Run: `python -m unittest tests.test_freehire_fetch.FreeHireWorkerTests -v`

Expected: all classification tests pass.

- [ ] **Step 9: Write failing retention and atomic-publication tests**

Add tests named:
- `test_bootstrap_old_rows_seed_seen_without_emitting_event`
- `test_events_retention_is_30_days_without_renumbering`
- `test_seen_retention_keeps_current_or_recent_only`
- `test_failed_market_fetch_does_not_replace_state_or_feed`
- `test_health_exposes_first_seq_last_seq_and_counts`

- [ ] **Step 10: Run retention/publication tests and verify RED**

Run: `python -m unittest tests.test_freehire_fetch.FreeHireWorkerTests -v`

Expected: failures because durable publication is missing.

- [ ] **Step 11: Implement durable state publication and CLI**

Define:
- `load_public_state(root: Path) -> tuple[dict, list[dict], dict]`
- `apply_retention(seen: dict, events: list[dict], now: datetime) -> tuple[dict, list[dict]]`
- `run(mode: str, root: Path, fetch_json) -> dict`
- `main(argv: list[str] | None = None) -> int`

Build all new state in memory first; write `seen.json`, `events.jsonl`, and `health.json` only after both SG and CN complete successfully. Preserve globally monotonic `seq` across retention.

- [ ] **Step 12: Run the full worker suite**

Run: `python -m unittest discover -s tests -v`

Expected: all tests pass with zero failures/errors.

- [ ] **Step 13: Commit the public worker core**

Commit in `kolihhan/freehirefetch` with message: `feat: add FreeHire ingestion worker`.

---

### Task 2: Add and live-verify the free GitHub Actions workflow

**Files:**
- Create: `kolihhan/freehirefetch/.github/workflows/freehire.yml`
- Modify: `kolihhan/freehirefetch/README.md`

**Interfaces:**
- Consumes: Task 1 CLI.
- Produces: scheduled repository updates to `feed/events.jsonl`, `state/seen.json`, and `health.json`.
- Triggers: `workflow_dispatch`, hourly delta at minute `17`, daily full backstop away from the top of hour.

- [ ] **Step 1: Add workflow contract checks to the test suite**

Add a test or static validation that asserts:
- workflow contains `workflow_dispatch`;
- hourly cron is minute `17`;
- scheduled hourly path invokes `--mode delta`;
- one daily path invokes `--mode full`;
- permissions are minimum necessary and include only repository content write needed for publishing;
- no secret/API-key reference is required.

- [ ] **Step 2: Run the workflow contract check and verify RED**

Run the targeted test/static validator.

Expected: FAIL because `.github/workflows/freehire.yml` does not exist.

- [ ] **Step 3: Implement the workflow**

Use a public standard Ubuntu runner. Install no third-party Python dependencies. Run the worker, run unit tests before publish, commit only when feed/state/health changed, and avoid triggering on push so the workflow cannot self-loop.

- [ ] **Step 4: Run local/static validation and full unit suite**

Run: `python -m unittest discover -s tests -v`

Expected: PASS.

- [ ] **Step 5: Commit the workflow**

Commit in `kolihhan/freehirefetch` with message: `ci: schedule FreeHire ingestion`.

- [ ] **Step 6: Manually dispatch bootstrap and verify the real API**

Dispatch `workflow_dispatch` with bootstrap mode. Verify from GitHub Actions logs/readback:
- SG and CN requests succeed;
- max-page behavior is accepted up to the documented limit when enough rows exist;
- requested filters are not ignored;
- outputs are written only after complete success;
- `health.json` has `first_seq`, `last_seq`, counts, duration, and successful mode;
- initial events contain only first-seen <= 7-day jobs while older rows may exist in `seen.json`.

- [ ] **Step 7: Manually dispatch delta again and verify idempotency**

Run a second manual delta without changing source data expectations. Confirm exact unchanged jobs do not re-emit events and sequence remains monotonic.

- [ ] **Step 8: Enable scheduled behavior only after both manual runs are healthy**

Keep the workflow committed as scheduled only if bootstrap + delta live verification pass. If FreeHire's actual contract differs from docs, stop here and update the spec/plan instead of working around it silently.

---

### Task 3: Add the private intake cursor contract and dedicated automation

**Files:**
- Modify: `kolihhan/job-resources/RULES.md`
- Modify: `kolihhan/job-resources/DISCOVERY_STATE.md`
- Create/update: ChatGPT automation `FreeHire Intake`

**Interfaces:**
- Consumes: public `kolihhan/freehirefetch/health.json` and `feed/events.jsonl` from Task 2.
- Produces: existing `APPLY`/`CHECK` Issues only for verified survivors; compact `FreeHire intake cursor: <seq>` in `DISCOVERY_STATE.md`.
- Deep-verification budget: at most 20 serious survivors per run.

- [ ] **Step 1: Update `RULES.md` minimally**

Add only the ownership contract:
- normal FreeHire ingestion is owned by `freehirefetch` + `FreeHire Intake`;
- existing maintainer must not routinely rescan FreeHire once handoff is live;
- public feed is Stage-1 discovery evidence only;
- intake cursor remains receipt/cursor state, not a tracker;
- worker stale/cursor-gap behavior stops intake and reports the concrete failure.

Do not duplicate the architecture spec or scheduler prompt into `RULES.md`.

- [ ] **Step 2: Seed the FreeHire cursor in `DISCOVERY_STATE.md`**

Use the current public `health.first_seq`/`last_seq` and rollout decision to establish the initial cursor explicitly. Do not guess or silently skip retained events.

- [ ] **Step 3: Read back both files and verify contract consistency**

Confirm `DISCOVERY_STATE.md` is still a compact receipt/cursor and `RULES.md` still states GitHub Issues are the only live opportunity state.

- [ ] **Step 4: Create the hourly `FreeHire Intake` automation**

Schedule at minute `35` hourly. Prompt requirements:
- Chat mode only; no Work mode; high reasoning effort;
- read current `README.md`, `PROFILE.md`, `RULES.md`, `DISCOVERY_STATE.md` first;
- verify public worker freshness and cursor gap before consuming;
- consume ascending `seq` only;
- cheap GitHub history dedupe first;
- Stage-2 official JD/liveness/cohort/fit/work-auth + targeted Gmail x2 + exact route;
- max 20 serious Stage-2 survivors per run;
- advance only contiguous terminal prefix;
- read back GitHub writes;
- never apply/contact anyone;
- no broad non-FreeHire discovery.

- [ ] **Step 5: Run one small real acceptance cycle**

Use current public events and verify:
- only post-cursor events are considered;
- known duplicate/application/rejection examples suppress before expensive verification;
- FreeHire metadata alone never satisfies liveness/route;
- no duplicate Issue is created on a repeated event;
- cursor only advances through contiguous completed events.

- [ ] **Step 6: Verify cursor-gap and Stage-2-budget behavior using controlled test evidence**

Confirm the automation prompt/logic explicitly stops on `cursor < first_seq` and stops before a 21st serious survivor rather than jumping ahead.

- [ ] **Step 7: Commit private contract changes**

Commit in `kolihhan/job-resources` with message: `feat: add FreeHire intake contract`.

---

### Task 4: Hand FreeHire ownership off from the existing maintainer and verify the whole system

**Files:**
- Modify: active `Job Inbox Maintainer` automation prompt only as needed to point to current `RULES.md` ownership.
- Read/verify: `kolihhan/job-resources/RULES.md`, `DISCOVERY_STATE.md`, recent Issues, both active automation definitions, `kolihhan/freehirefetch/health.json`.

**Interfaces:**
- Consumes: working Tasks 1-3.
- Produces: non-overlapping scheduler responsibilities and one operational end-to-end system.

- [ ] **Step 1: Remove routine FreeHire discovery responsibility from the maintainer**

Keep its existing rule-first design. It continues Gmail lifecycle, existing Issue maintenance, and non-FreeHire SG/CN source rotation. Do not duplicate FreeHire Intake policy inside the maintainer prompt.

- [ ] **Step 2: Verify automation separation**

Check live definitions:
- `FreeHire Intake` = FreeHire only, hourly;
- `Job Inbox Maintainer` = lifecycle + other sources;
- neither applies or contacts anyone;
- both remain Chat mode / high reasoning, not Work mode.

- [ ] **Step 3: Verify public/private boundary**

Search/read the public `freehirefetch` repo and confirm there is no Gmail identifier, private Issue state, candidate profile data, recruiter history, or secret.

- [ ] **Step 4: Verify a full real data path**

Evidence chain must exist for one run:
`FreeHire API -> public worker health/feed -> FreeHire Intake post-cursor consumption -> cheap dedupe -> Stage 2 or terminal suppression -> cursor readback`.

A promoted job is not required for success; a healthy zero-survivor run is acceptable if the path is verified.

- [ ] **Step 5: Run regression checks on `job-resources` invariants**

Confirm:
- GitHub Issues remain only live opportunity state;
- Gmail remains evidence, not mirrored data;
- `DISCOVERY_STATE.md` remains compact;
- scheduled non-FreeHire discovery windows still work;
- FreeHire no longer counts as repeated maintainer work;
- no existing authorization/privacy guardrail was weakened.

- [ ] **Step 6: Final verification before completion claim**

Run/read fresh evidence for:
- public worker unit suite: zero failures;
- latest manual/scheduled GitHub Action: success;
- public `health.json`: fresh and coherent;
- dedicated intake automation: enabled with expected schedule/prompt;
- maintainer: enabled with non-overlapping ownership;
- private `RULES.md`/`DISCOVERY_STATE.md`: readback matches contract.

Only then report completion.
