# Source Adapter Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand `kolihhan/freehirefetch` from FreeHire-only ingestion into a replaceable set of public ATS/source adapters while preserving the Discovery Pipeline v2 observation, identity, filtering and candidate-feed contracts.

**Architecture:** Each adapter fetches one source family and emits normalized `Observation` records only. Shared identity/filter/feed code owns all dedupe and candidate decisions. Add sources incrementally in reliability order; authenticated/anti-bot job boards remain scheduler gap sources unless a stable permitted machine interface is verified.

**Tech Stack:** Python 3.13 standard library, unittest, GitHub Actions, public unauthenticated ATS APIs/pages where available.

**Spec:** `docs/superpowers/specs/2026-11-02-discovery-pipeline-v2-design.md`

## Global Constraints

- Execute only after the core pipeline plan is green.
- No adapter may introduce a second identity/filter implementation.
- No required private cookie, browser automation, CAPTCHA bypass, paid service or personal account session.
- A source failure must fail/isolate that adapter according to policy without corrupting previously published feed state.
- Source data is provenance; canonical role identity comes from shared identity-v2.
- Prefer employer-controlled ATS APIs/pages over broad-board scraping.
- Public collector remains non-personal.

## Review Focus

1. source pagination misses roles beyond page one;
2. tenant/job-board configuration maps the wrong employer to a requisition ID;
3. adapter emits HTML/tracking noise that causes false CHANGED events;
4. one broken source prevents healthy unrelated sources from preserving their prior state;
5. ATS-specific req IDs collide because employer/tenant namespace was omitted.

---

### Task 1: Add adapter protocol and source registry

**Files:**
- Create: `kolihhan/freehirefetch/sources/__init__.py`
- Create: `kolihhan/freehirefetch/sources/base.py`
- Create: `kolihhan/freehirefetch/sources/registry.py`
- Create: `kolihhan/freehirefetch/sources/registry.json`
- Create: `kolihhan/freehirefetch/tests/test_source_registry.py`
- Modify: `kolihhan/freehirefetch/firehose_fetch.py`

**Interfaces:**
- Adapter consumes a public source locator/config and returns normalized observation dictionaries.
- Registry entry names employer key, adapter type and public locator/tenant/site information.

- [ ] Write failing tests for adapter registration, duplicate employer mapping, malformed locators and deterministic observation fields.
- [ ] Verify RED.
- [ ] Implement minimal adapter protocol/registry without changing candidate logic.
- [ ] Run full suite.
- [ ] Commit: `feat: add pluggable source adapter registry`.

---

### Task 2: Add Greenhouse adapter

**Files:**
- Create: `kolihhan/freehirefetch/sources/greenhouse.py`
- Create: `kolihhan/freehirefetch/tests/test_greenhouse_source.py`

**Required tests:**
- board pagination/listing extraction;
- stable job/requisition identity extraction;
- canonical role URL;
- HTML/JD normalization;
- closed/malformed response behavior.

Use public Greenhouse job-board interfaces only. Emit observations into shared identity/filter pipeline.

Commit: `feat: add Greenhouse source adapter`.

---

### Task 3: Add Lever adapter

**Files:**
- Create: `kolihhan/freehirefetch/sources/lever.py`
- Create: `kolihhan/freehirefetch/tests/test_lever_source.py`

Pin posting UUID, canonical URL, location/workplace metadata and description normalization.

Commit: `feat: add Lever source adapter`.

---

### Task 4: Add Ashby adapter

**Files:**
- Create: `kolihhan/freehirefetch/sources/ashby.py`
- Create: `kolihhan/freehirefetch/tests/test_ashby_source.py`

Pin public board identifier, job posting ID, canonical URL and structured/JD normalization.

Commit: `feat: add Ashby source adapter`.

---

### Task 5: Add SmartRecruiters adapter

**Files:**
- Create: `kolihhan/freehirefetch/sources/smartrecruiters.py`
- Create: `kolihhan/freehirefetch/tests/test_smartrecruiters_source.py`

Test pagination, stable job ID, employer namespace and canonical posting URL.

Commit: `feat: add SmartRecruiters source adapter`.

---

### Task 6: Add Workday CXS adapter only after tenant-contract reconnaissance

**Files:**
- Create: `kolihhan/freehirefetch/sources/workday.py`
- Create: `kolihhan/freehirefetch/tests/test_workday_source.py`
- Extend: `sources/registry.json` with explicit tenant/site locators.

Before implementation, verify several real target employers because Workday endpoint/site layout varies. Do not create one guessed generic parser.

Tests must cover:
- tenant/site namespacing;
- pagination/offset behavior;
- requisition ID extraction;
- canonical URL construction;
- changed site/404 behavior.

Commit: `feat: add verified Workday source adapter`.

---

### Task 7: Evaluate CN ATS adapters individually

Candidate families: Moka, Feishu Hire, Beisen.

For each family:

- first perform read-only reconnaissance on target employers;
- document whether a stable unauthenticated API/page exists;
- implement only if deterministic pagination + stable role identity + usable JD data are verified;
- otherwise leave that family to CN scheduler/native-platform gap discovery.

Do not treat login-protected or redirect-loop pages as a reason to build brittle bypass logic.

Each accepted adapter gets its own file + fixture tests + commit.

---

### Task 8: Integrate source health and metrics

**Files:**
- Modify: `kolihhan/freehirefetch/health.json` schema through worker code
- Modify: `kolihhan/freehirefetch/README.md`
- Modify: `kolihhan/job-resources/docs/scout-run-metrics.md` only if the scheduler needs source-attribution reporting changes

Per source/market expose:
- fetched;
- normalized;
- strong exact merges;
- candidate events emitted;
- hard drops by reason;
- errors and last successful fetch.

A candidate merged from several sources must retain compact provenance rather than duplicating queue entries.

Run full test suite and verify one live ingestion for every enabled adapter before considering it part of normal scheduled coverage.

Commit: `feat: expose multi-source ingestion health`.

---

## Job boards / platform policy

LinkedIn, JobStreet, Indeed, MyCareersFuture, BOSS, 牛客, 猎聘, 智联, 51job and 脉脉 are separate from ATS adapters.

- MyCareersFuture or other platforms may be machine-ingested when a stable public interface is already supplied indirectly by FreeHire or a verified public endpoint.
- Do not build the core around authenticated scraping, session cookies, anti-bot bypass or fragile browser selectors.
- Until a platform gets a verified adapter, retain it in the SG/CN/MY scheduler platform sweep as a gap source.
- When an adapter becomes healthy, reduce redundant scheduler discovery for that source; preserve a bounded gap check if the platform still exposes recruiter-only/platform-exclusive roles.

## Rollout order

`Greenhouse -> Lever -> Ashby -> SmartRecruiters -> Workday -> individually verified CN ATS`.

After each source, measure incremental **unique** candidate roles after cross-source dedupe. Do not add a source merely to increase raw fetch count.
