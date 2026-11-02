# Discovery Pipeline v2 Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace raw FreeHire-sequence reasoning with a lossless cross-source-ready candidate feed plus private historical identity index, so hourly SG/CN/MY scouts spend expensive work only on plausible unseen roles.

**Architecture:** `kolihhan/freehirefetch` remains a public collector and gains canonical identity-v2, conservative filtering and an uncapped paged candidate-event feed. `kolihhan/job-resources` privately builds a strong-key index from all Issue history. Hourly scouts consume candidate events, cheap-skip strong known matches, retry transient verification failures without blocking later candidates, and keep Issues as the only live opportunity state.

**Tech Stack:** Python 3.13 standard library, unittest, GitHub Actions, repository JSON/JSONL transport state, existing ChatGPT automations.

**Spec:** `docs/superpowers/specs/2026-11-02-discovery-pipeline-v2-design.md`

## Global Constraints

- `freehirefetch` remains public and contains no personal Issue/Gmail/profile/application state.
- GitHub Issues remain the only live opportunity state.
- Strong role identity may suppress; weak employer/title/location fingerprint may only flag suspicion.
- FreeHire enrichment remains hint-only unless the actual source/JD proves the fact.
- Explicit fixed-term/contract research must survive public filtering for downstream `RESEARCH_EXCEPTION` review.
- Candidate feed is lossless within its retention window and has no 10-per-market cap.
- A transient candidate verification failure cannot stall later candidate sequences.
- Scheduler final Issue creation still performs exact Issue-history dedupe and readback.
- No application/contact is authorized by this work.

## Review Focus

1. **False cross-source merge** — two same-title/location openings at one employer must remain separate without a strong req ID/canonical role URL.
2. **Identity migration loss** — existing `public_slug` seen state must not cause every current FreeHire job to re-emit as new after identity-v2 rollout.
3. **Research recall regression** — fixed-term RA/RE/research roles must survive machine filtering even though ordinary non-permanent engineering is low-value.
4. **Queue blocker** — one unreadable candidate must become retry state while later candidate sequences continue.
5. **Private-history leakage** — known-role index must stay in `job-resources`; public `freehirefetch` output must not contain Issue numbers/statuses or personal dedupe data.

---

### Task 1: Add canonical cross-source identity-v2 to `freehirefetch`

**Files:**
- Create: `kolihhan/freehirefetch/identity.py`
- Create: `kolihhan/freehirefetch/tests/test_identity.py`
- Modify: `kolihhan/freehirefetch/freehire_fetch.py`
- Modify: `kolihhan/freehirefetch/candidate_snapshot.py`

**Interfaces:**
- Produces `normalize_employer_name(value: object) -> str`.
- Produces `normalize_title(value: object) -> str`.
- Produces `normalize_location(value: object) -> str`.
- Produces `extract_identity_keys(job: dict) -> dict` containing `strong_role_key | None`, `source_aliases`, and `weak_fingerprint`.
- Produces `canonical_role_identity(job: dict) -> str` that uses strong key when available and otherwise preserves a source-local identity.

- [ ] **Step 1: Write failing identity tests**

Tests must prove:
- employer-issued `req_id` at the same employer collapses across FreeHire/ATS observations;
- tracking parameters are removed from a canonical employer role URL;
- LinkedIn/MCF/source listing IDs are aliases, not global requisition IDs;
- same employer/title/location without strong evidence yields only the same weak fingerprint, not an automatic canonical merge;
- parent/subsidiary names do not merge unless explicitly aliased.

- [ ] **Step 2: Run targeted tests and verify RED**

Run: `python -m unittest tests.test_identity -v`

Expected: FAIL because identity-v2 does not exist.

- [ ] **Step 3: Implement identity-v2**

Keep ATS/source-specific URL/ID extraction in small pure functions. Prefer `req:<employer_key>:<req_id>`, then normalized employer-controlled role URL, then source-local identity. Preserve `weak_fingerprint` separately.

- [ ] **Step 4: Add migration compatibility for existing FreeHire `public_slug` state**

When an existing seen record is keyed by `public_slug`, treat that slug as a source alias during rollout so unchanged jobs do not mass re-emit.

- [ ] **Step 5: Run identity + existing worker tests**

Run:
- `python -m unittest tests.test_identity -v`
- `python -m unittest discover -s tests -v`

Expected: zero failures/errors.

- [ ] **Step 6: Commit**

Commit in `kolihhan/freehirefetch`: `feat: add canonical role identity v2`.

---

### Task 2: Replace capped candidate snapshot as the downstream contract with a lossless triage feed

**Files:**
- Create: `kolihhan/freehirefetch/triage_feed.py`
- Create: `kolihhan/freehirefetch/tests/test_triage_feed.py`
- Modify: `kolihhan/freehirefetch/firehose_fetch.py`
- Modify: `kolihhan/freehirefetch/feed_pages.py`
- Modify: `kolihhan/freehirefetch/health.json` schema through worker code
- Modify: `kolihhan/freehirefetch/.github/workflows/freehire.yml`
- Modify: `kolihhan/freehirefetch/README.md`

**Interfaces:**
- Produces append-only candidate events with monotonic `candidate_seq`.
- Produces `feed/triage/index.json` and bounded `feed/triage/pages/*.jsonl`.
- Keeps `feed/candidates.json` only as an optional bounded debug/latest snapshot.

- [ ] **Step 1: Write failing feed tests**

Tests must prove:
- 25 valid SG candidates all survive even when the debug snapshot limit is 10;
- candidate sequence is monotonic across runs and retention;
- same canonical role observed through two strong-equivalent sources emits one role event;
- same weak fingerprint without strong proof does not silently collapse;
- a material JD/route change emits `CHANGED`; unchanged content emits nothing;
- pages can be read in small line ranges without needing one giant file.

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_triage_feed -v`.

- [ ] **Step 3: Implement triage event persistence and paging**

Use build-in-memory-then-atomic-write semantics consistent with the existing worker. Expose first/last candidate sequence and per-market emission counts in health metadata.

- [ ] **Step 4: Preserve the current raw event feed for audit/rebuild**

Do not delete `feed/events.jsonl` or its pages during this task. The new triage feed becomes the reasoning contract only after cutover.

- [ ] **Step 5: Run full `freehirefetch` suite**

Run: `python -m unittest discover -s tests -v`.

Expected: zero failures/errors.

- [ ] **Step 6: Commit**

Commit: `feat: publish lossless triage candidate feed`.

---

### Task 3: Make machine filtering conservative and research-safe

**Files:**
- Create: `kolihhan/freehirefetch/triage_filter.py`
- Create: `kolihhan/freehirefetch/tests/test_triage_filter.py`
- Modify: `kolihhan/freehirefetch/candidate_snapshot.py`
- Modify: `kolihhan/freehirefetch/firehose_fetch.py`

**Interfaces:**
- Produces `classify_observation(job: dict) -> TriageDecision` with `keep`, `hard_drop_reason | None`, `signals`, and extracted hints.
- Does not make APPLY/CHECK decisions.

- [ ] **Step 1: Write failing recall/safety tests**

Pin these cases:
- Staff/Principal/Director/Manager/Head/Lead -> hard drop;
- Intern/trainee -> hard drop;
- Senior -> flag, not automatic drop;
- enrichment-only `experience_years_min=5` -> flag, not automatic hard drop;
- Software Engineer + multiple material Agent/RAG/retrieval/eval signals -> keep;
- one casual AI mention in generic backend JD -> not promoted to AI triage;
- fixed-term Research Engineer/RA with material AI/NLP work -> keep with employment flag;
- knowledge graph / retrieval / ranking / agent-memory / evaluation signals are recognized;
- 2027/PhD/cohort hints are extracted but not converted to campaign eligibility without exact evidence.

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_triage_filter -v`.

- [ ] **Step 3: Implement filter and signal extraction**

Remove the current blanket non-permanent drop from the authoritative triage path. Keep any debug snapshot behavior aligned with the new classifier.

- [ ] **Step 4: Run focused + full tests**

Run:
- `python -m unittest tests.test_triage_filter -v`
- `python -m unittest discover -s tests -v`

- [ ] **Step 5: Commit**

Commit: `fix: preserve uncertain and research candidates in triage`.

---

### Task 4: Build the private known-role index from all `job-resources` Issue history

**Files:**
- Create: `kolihhan/job-resources/scripts/build_known_role_index.py`
- Create: `kolihhan/job-resources/tests/test_known_role_index.py`
- Create: `kolihhan/job-resources/.github/workflows/known-role-index.yml`
- Create/generated: `kolihhan/job-resources/discovery-state/known-role-index.json`
- Modify: `kolihhan/job-resources/docs/source-routing.md`

**Interfaces:**
- Consumes all Issues, open + closed, through GitHub REST.
- Produces strong keys, source aliases, weak fingerprints and Issue references only.
- Does not copy Gmail/profile/resume/recruiter notes into the index.

- [ ] **Step 1: Write parser tests from representative Issue fixtures**

Fixtures must cover:
- employer requisition ID;
- LinkedIn job ID;
- MCF UUID;
- Workday/Greenhouse/Lever/Ashby exact URLs;
- issue with only employer/title/location fallback;
- multiple aliases for one Issue;
- malformed/legacy Issue that yields no strong key.

Assertions must prove weak fingerprints are marked non-authoritative.

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_known_role_index -v`.

- [ ] **Step 3: Implement deterministic index builder**

Prefer structured Issue body fields when present; parse title only as fallback. Namespace requisition IDs by normalized employer. Never infer that a board ID is an employer requisition ID.

- [ ] **Step 4: Add workflow contract**

Trigger on `workflow_dispatch`, relevant Issue lifecycle events, and an hourly backstop. Permissions: `issues: read`, `contents: write`. Commit only when derived index changes.

- [ ] **Step 5: Run tests and one dry/live read**

Verify the generated index includes known current Issues and contains no Gmail addresses, resume text or application notes beyond Issue number/identity aliases.

- [ ] **Step 6: Commit**

Commit in `kolihhan/job-resources`: `feat: add private known role identity index`.

---

### Task 5: Add per-market triage cursors and non-blocking retry receipts

**Files:**
- Create: `kolihhan/job-resources/discovery-state/triage-sg.json`
- Create: `kolihhan/job-resources/discovery-state/triage-cn.json`
- Create: `kolihhan/job-resources/discovery-state/triage-my.json`
- Create: `kolihhan/job-resources/discovery-state/retry-sg.json`
- Create: `kolihhan/job-resources/discovery-state/retry-cn.json`
- Create: `kolihhan/job-resources/discovery-state/retry-my.json`
- Modify: `kolihhan/job-resources/RULES.md`
- Modify: `kolihhan/job-resources/README.md`
- Modify: `kolihhan/job-resources/docs/scout-run-metrics.md`

**Interfaces:**
- Triage cursor stores only last consumed `candidate_seq` per market.
- Retry file is a bounded machine receipt list: `role_key`, `candidate_seq`, `reason_code`, `attempts`, `next_retry_at`.

- [ ] **Step 1: Update contract docs before automation cutover**

Explicitly state candidate/retry state is machine efficiency state, not a live opportunity inbox, and GitHub Issues remain canonical.

- [ ] **Step 2: Define retry advancement semantics**

A transient verification failure creates/updates a retry receipt and allows the main candidate cursor to advance. CHECK is still used only when existing CHECK rules are satisfied.

- [ ] **Step 3: Extend metrics**

Replace raw FreeHire recovery metrics with: candidate events read, strong known duplicates, weak suspected duplicates checked, cheap rejects, full JDs, retries created/resolved, APPLY/CHECK created.

- [ ] **Step 4: Read back all contract files and verify no parallel-human-tracker language was introduced**

- [ ] **Step 5: Commit**

Commit: `docs: define triage cursor and retry contract`.

---

### Task 6: Migrate SG/CN/MY hourly scouts to the triage feed in shadow mode

**Files/State:**
- Update the three existing ChatGPT automations only; do not create duplicate scouts.
- Read: public `freehirefetch/feed/triage/index.json` + pages.
- Read: private `discovery-state/known-role-index.json` and market triage/retry state.

**Interfaces:**
- Candidate path: triage event -> strong known index check -> cheap policy screen -> full JD only if needed -> liveness/eligibility/work-auth -> Gmail -> final exact Issue search -> APPLY/CHECK Issue + readback.

- [ ] **Step 1: Add shadow consumption without disabling old raw recovery**

The scout records what the triage path would do but does not double-create Issues. Use role identity to reconcile both paths.

- [ ] **Step 2: Verify current fast-path candidates appear in triage feed**

Every role in the current `feed/candidates.json` that is not a deliberate new filter rejection must be represented by a triage candidate event.

- [ ] **Step 3: Verify historical-known suppression**

Use at least one known exact role (for example a current WAIT/APPLY role) and confirm strong index match prevents full-JD work while final Issue gate would also find it.

- [ ] **Step 4: Verify retry does not stall**

Use a transiently unreadable role followed by a normal role. Persist the first into retry and process the later candidate sequence.

- [ ] **Step 5: Compare old/new paths for serious-survivor recall**

Do not cut over if old raw recovery finds a plausible serious survivor that the new triage feed machine-dropped without an explicit approved hard-drop reason.

---

### Task 7: Replay retained FreeHire history through the new pipeline and cut over

**Files:**
- Create: `kolihhan/freehirefetch/rebuild_triage.py`
- Create: `kolihhan/freehirefetch/tests/test_rebuild_triage.py`
- Modify: `kolihhan/freehirefetch/.github/workflows/freehire.yml` to permit manual rebuild mode if appropriate
- Modify after acceptance: `kolihhan/job-resources/docs/freehire-gap-recovery.md`
- Modify after acceptance: three scout automation prompts

**Interfaces:**
- Consumes retained raw FreeHire event history.
- Rebuilds candidate feed deterministically without using personal data.

- [ ] **Step 1: Test replay idempotency**

Replaying the same retained raw feed twice must produce identical role/candidate content and sequence assignment under a clean rebuild target.

- [ ] **Step 2: Run historical rebuild**

Generate the candidate feed from retained events, then let each market scout apply the private known-role index while consuming.

- [ ] **Step 3: Verify funnel metrics**

Record raw observations -> globally deduped roles -> triage candidates -> historical known duplicates -> policy rejects -> full JD -> survivors.

- [ ] **Step 4: Cut over only after acceptance criteria pass**

Remove raw FreeHire gap recovery from hourly scout obligations. Keep raw public events for audit/rebuild. Mark `docs/freehire-gap-recovery.md` superseded rather than deleting history immediately.

- [ ] **Step 5: Run final verification**

`freehirefetch`: `python -m unittest discover -s tests -v` => zero failures/errors.

`job-resources`: run all repository tests/static checks applicable to new scripts/contracts. Verify all three automation definitions read the new triage contract and no longer scan raw FreeHire pages.

- [ ] **Step 6: Commit final cutover docs/state**

Commit: `feat: cut hourly scouts over to triage candidate feed`.

---

## Execution Order

Do Tasks 1-4 first. Do not modify scout behavior until identity, triage feed and private known-role index are independently green. Tasks 5-7 are the operational cutover.

The ATS/source expansion is intentionally separate; execute `2026-11-02-source-adapter-expansion.md` only after this core pipeline is verified on FreeHire data.
