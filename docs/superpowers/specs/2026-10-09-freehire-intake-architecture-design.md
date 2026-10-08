# FreeHire Intake Architecture Design

Date: 2026-10-09
Status: design approved in chat; implementation not started

## Goal

Increase SG/CN discovery recall from FreeHire without making `job-resources` another software project, exposing private job-search data, or making the existing maintainer repeatedly read thousands of raw listings.

The system must remain free to operate, simple to recover, conservative about false rejects, and consistent with `RULES.md`:

- GitHub Issues remain the only live opportunity state.
- Gmail remains recruiting evidence and targeted dedupe evidence.
- `DISCOVERY_STATE.md` remains only a receipt/cursor, never a second tracker.
- No second database, dashboard, scoring engine, agent framework, or personal-data mirror.
- No application or external contact without explicit user authorization.
- ChatGPT scheduled tasks run in Chat mode with high reasoning effort, not Work mode.

## Architecture

There are exactly three operational roles.

```text
FreeHire public API
        |
        v
1. PUBLIC WORKER — kolihhan/freehirefetch
   GitHub Actions, free standard public runner
   fetch -> validate -> conservative machine filter -> exact machine dedupe
        |
        | public job data only
        v
2. PRIVATE FREEHIRE INTAKE SCHEDULER
   read NEW/CHANGED candidates -> GitHub-history dedupe -> official verification
   -> fit/cohort/work-auth -> targeted Gmail x2 dedupe -> exact route
        |
        | serious survivors only
        v
   existing job-resources Issues (APPLY/CHECK)
        |
        v
3. EXISTING JOB INBOX MAINTAINER
   Gmail lifecycle + existing Issue maintenance + non-FreeHire discovery lanes
```

Do not add a fourth orchestration layer.

## 1. Public worker: `kolihhan/freehirefetch`

### Responsibility

The public repository is a stateless/public-data worker plus minimal public ingestion state. It knows nothing about the candidate.

It may contain only:

- FreeHire public API client;
- pagination/retry logic;
- public job fields;
- conservative machine-filter flags;
- exact dedupe fingerprints;
- run health/coverage metadata;
- tests and workflow definitions.

It must never contain:

- Gmail data or message IDs;
- application/rejection history;
- candidate profile, sponsorship history, recruiter notes, or private resume data;
- private `job-resources` Issue state;
- secrets that are not required by the public FreeHire API.

### Fetch modes

**Bootstrap:** one maximum-page scan for SG and CN, bounded by the FreeHire API deep-page limit. The bootstrap seeds machine state but does not emit the entire historical inventory to ChatGPT.

**Hourly delta:** the normal path. Prefer FreeHire's first-seen freshness filter (`open_within_days`) and newest-first ordering. Pagination may continue to the API maximum if the filtered result set requires it; do not impose an arbitrary small page cap.

**Daily full backstop:** one maximum-page SG+CN scan per day to detect ingestion drift, missed jobs, classification changes, or API behavior changes. It is a recovery/validation path, not an instruction to send every old job downstream again.

Suggested schedule:

- hourly delta: minute `17` of every hour;
- daily full backstop: once per day away from the top-of-hour peak.

The exact UTC cron is an implementation detail; the user-facing contract is hourly delta plus one daily full backstop.

### API validation

Every run must validate the API boundary before publishing output:

- HTTP response succeeds;
- expected `data` and `meta` structures exist;
- requested country/freshness/category filters were not silently ignored;
- page/offset behavior remains within documented limits;
- malformed records do not poison the whole feed;
- transient failures use bounded retry/backoff;
- permanent/contract failures fail the run rather than publishing misleading data.

A failed run must not advance dedupe state or replace the last known-good downstream feed.

### Conservative machine filtering

The worker optimizes recall, not final precision.

Hard machine drops should be limited to highly explicit title-level mismatches such as:

- Senior / Staff / Principal / Lead;
- Director / Head / Manager when clearly managerial;
- Internship / Intern.

FreeHire enrichment fields such as inferred seniority, years of experience, employer type, work authorization, or category are hints. They may create `flags`, but they must not by themselves become hard rejects when employer-controlled evidence has not been checked.

Examples of flags:

- `experience_5_plus_hint`;
- `agency_or_outstaff_hint`;
- `seniority_hint`;
- `visa_hint`;
- `classification_uncertain`.

This preserves the existing `RULES.md` rule that aggregator metadata is discovery evidence, not employer truth.

### Machine dedupe

Machine dedupe is deliberately exact and non-personal.

Primary identity:

1. FreeHire `public_slug` when present;
2. otherwise an exact normalized public fingerprint such as employer + title + market/location + source/external ID.

For each identity, keep a content fingerprint over the public fields that matter for downstream review.

Classification:

- unseen identity -> `NEW`;
- same identity, changed meaningful fingerprint -> `CHANGED`;
- same identity, unchanged fingerprint -> no downstream event.

Do not implement semantic same-company/near-role-family dedupe in the public worker. That requires candidate history and belongs in the private intake stage.

### Public data surfaces

Keep the contract small. Prefer three machine-readable surfaces:

- `feed/events.jsonl` — ordered `NEW` / `CHANGED` events;
- `state/seen.json` — minimal exact machine-dedupe state;
- `health.json` — latest successful run metadata.

Each event must include a monotonically increasing `seq` plus enough public data to identify and verify the listing, for example:

```json
{
  "seq": 10523,
  "kind": "NEW",
  "market": "SG",
  "public_slug": "...",
  "company": "...",
  "title": "...",
  "location": "...",
  "source_url": "...",
  "freehire_url": "...",
  "detected_at": "...",
  "fingerprint": "...",
  "flags": []
}
```

`health.json` should expose only compact observability such as last successful run, mode, SG/CN rows fetched, new/changed counts, filtered counts, ignored-parameter detection, and duration.

Avoid storing hourly full raw snapshots in Git history. Public Git state is a transport/receipt surface, not a job archive.

## 2. Private `FreeHire Intake` scheduler

### Responsibility

Create one dedicated ChatGPT automation whose only discovery source is the public `freehirefetch` worker.

It must run in Chat mode with high reasoning effort and must not invoke Work mode.

Suggested cadence: hourly, after the GitHub Action has normally completed, for example minute `35` of each hour.

### Run flow

For each run:

1. Read the current `job-resources` `README.md`, `PROFILE.md`, `RULES.md`, and `DISCOVERY_STATE.md`.
2. Read `freehirefetch/health.json` and verify the worker is not stale or failed.
3. Read public feed events with `seq` greater than the private FreeHire cursor.
4. Process events in sequence and in bounded batches if the backlog is large.
5. Apply cheap GitHub-history dedupe using the existing `RULES.md` contract:
   - exact requisition/job ID;
   - same employer + same or near-identical role family;
   - explicit prior application/user history.
6. For survivors, perform Stage 2 only:
   - employer-controlled exact JD/current liveness;
   - cohort/seniority/hard requirements;
   - fit and material work-authorization blockers;
   - targeted dedupe in both Gmail accounts;
   - exact usable application route.
7. Create/update `APPLY` or `CHECK` Issues only when the existing promotion rules are satisfied.
8. Advance the FreeHire cursor only through events whose processing reached a stable terminal result for this intake run.
9. Read back any GitHub write before claiming success.

The scheduler must not perform broad LinkedIn, JobStreet, Indeed, BOSS, 牛客, 51job, 智联, 猎聘, Telegram, or general-web discovery. Those remain outside this scheduler.

### Cursor

Use the existing receipt/cursor concept rather than inventing a tracker.

`DISCOVERY_STATE.md` may carry one compact line/field such as:

```text
FreeHire intake cursor: 10523
```

This cursor means all public events through that sequence were safely consumed or intentionally suppressed under the current rules.

Do not create `freehire.db`, a second CSV tracker, a FreeHire dashboard, or FreeHire-specific Issues for raw candidates.

### Backlog behavior

A large bootstrap or outage backlog must not cause the scheduler to deep-verify thousands of jobs in one run.

Order work by:

1. newest `NEW` events;
2. meaningful `CHANGED` events;
3. market/role relevance under the current SG/CN rules.

Machine-level obvious rejects and GitHub-history duplicates can be consumed cheaply. Expensive official/Gmail verification should be bounded to a practical survivor batch per run.

If backlog remains, keep the cursor before the first unprocessed event and continue next run. Do not skip silently.

## 3. Existing `Job Inbox Maintainer`

The existing maintainer remains the system owner for:

- recruiting-email lifecycle reconciliation;
- OA/interview/recruiter/deadline/rejection state changes;
- consistency of existing Issues;
- scheduled discovery from non-FreeHire source families;
- `DISCOVERY_STATE.md` scheduled-discovery receipt/rotation.

After FreeHire Intake is live, normal scheduled discovery must stop actively re-scanning FreeHire to avoid duplicate work. Interactive FreeHire lookup remains allowed when explicitly requested or when the worker is stale/broken and the user asks for a probe.

FreeHire Intake creates opportunities; the maintainer continues to own their later lifecycle after they become Issues.

## Failure and recovery rules

### Public worker failure

- Do not publish partial/misleading replacement feed.
- Do not advance machine dedupe state.
- Preserve the last known-good feed/state.
- Mark the workflow failed; next run retries from durable state.

### Private intake failure

- Do not advance the cursor past unprocessed/ambiguous events.
- For ambiguous GitHub create failures, follow existing search/read-back-before-retry rules.
- Reprocessing must be idempotent: GitHub history, Gmail dedupe, exact role identity, and the cursor prevent duplicate Issues.

### Stale worker

If `health.json`/latest workflow evidence shows the public worker has not completed successfully for a material period, the intake scheduler should report one concrete system failure rather than pretending there are no new jobs. It should not automatically fall back to a new scraping framework.

## Security and privacy

- Public worker uses only unauthenticated public FreeHire data.
- No candidate or Gmail data crosses into the public repository.
- GitHub Actions permissions should be minimum necessary; repository content write access is allowed only if needed to publish feed/state.
- No browser automation, CAPTCHA bypass, credential reuse, BOSS login, private cookies, or paid third-party API.
- No application/contact action is permitted by either worker or scheduler.

## Observability

Keep observability compact and operational.

Public worker:

- last success;
- delta/full mode;
- SG/CN fetched counts;
- NEW/CHANGED counts;
- title-hard-drop count;
- contract/filter error status;
- duration.

Private intake:

- last consumed `seq`;
- events considered;
- cheap duplicates suppressed;
- Stage-2 candidates entered;
- Issues promoted/updated;
- concrete verification failures.

Do not turn these counters into quotas, scores, or a dashboard.

## Testing strategy

Public worker tests must cover at minimum:

- maximum pagination boundaries;
- early stop when API total is lower;
- ignored-filter detection;
- retry/failure behavior;
- conservative title hard-drop vs enrichment hint behavior;
- exact NEW / unchanged / CHANGED fingerprint classification;
- durable-state update only after successful complete processing;
- delta and full modes;
- output schema/sequence monotonicity.

Workflow validation must prove:

- scheduled and manual dispatch both work;
- public standard runner only;
- no required paid service/secret;
- failed fetch does not publish a false successful feed;
- state/feed writes are idempotent.

Private scheduler acceptance must prove on a small real sample:

- it reads only events after the cursor;
- known application/rejection duplicates are suppressed before deep verification;
- aggregator metadata alone does not satisfy liveness/route gates;
- a genuine survivor can reach the existing `APPLY`/`CHECK` Issue contract;
- cursor does not advance across an unresolved failure;
- rerunning the same events does not create duplicate Issues.

## Rollout

### Phase 1 — public worker

Implement and manually run one bootstrap/max-page probe. Verify API contract, output schema, filter conservatism, dedupe behavior, and runtime cost. Do not enable hourly schedule until the manual run is healthy.

### Phase 2 — hourly public ingestion

Enable hourly delta plus daily full backstop. Observe at least several runs for stability and reasonable event volume.

### Phase 3 — private FreeHire Intake scheduler

Create the dedicated hourly ChatGPT automation. Start from a known cursor and process a bounded real sample. Verify GitHub/Gmail dedupe quality before allowing normal unattended intake.

### Phase 4 — maintainer handoff

Update the existing maintainer contract so FreeHire is no longer a normal repeated discovery lane. It continues lifecycle maintenance and non-FreeHire discovery.

## Acceptance criteria

The design is successful when:

1. `freehirefetch` runs on a public standard GitHub runner with no paid service or private candidate data.
2. Bootstrap can reach FreeHire's documented maximum pagination window for SG and CN when the API has that many filtered rows.
3. Normal hourly runs are incremental; daily full scan provides a recovery/backstop path.
4. Public machine filtering does not hard-reject roles solely from uncertain FreeHire enrichment.
5. Exact machine duplicates do not repeatedly reach ChatGPT.
6. The dedicated private scheduler consumes only unseen/changed public events and performs existing Stage-2 verification.
7. `DISCOVERY_STATE.md` remains only receipt/cursor state, not a job tracker.
8. Existing GitHub Issues remain the only operational opportunity state.
9. Existing maintainer no longer repeats normal FreeHire discovery.
10. No application or external contact occurs without explicit user authorization.

## Non-goals

Do not add:

- Supabase/SQL database;
- Airflow or another orchestrator;
- agentic GitHub workflow frameworks;
- browser automation;
- paid scraping/API services;
- semantic/vector dedupe service;
- a public or private job dashboard;
- a second opportunity tracker;
- auto-apply.
