# Job Search Consolidation — Design

Date: 2026-10-07
Status: proposed for implementation after user review
Repository: `kolihhan/job-resources`

## Goal

Keep the existing GitHub-Issues job-search system, but make it more reliable and broader without turning it into another large agent project.

The system must improve two things at the same time:

1. **Recall:** search a meaningfully wider set of companies, role families and sources before concluding that few jobs exist.
2. **Precision:** stale, duplicate, already-applied, obvious-mismatch and unusable-route jobs must not enter the active inbox.

The existing architecture remains: GitHub Issues are operational state, Gmail is evidence, repo Markdown is the operating contract, and scheduled tasks execute that contract.

## Evidence from real failures

Recent failures show that the core architecture is workable but the operating contract drifted:

- stale listing regression: an exact role page was retrievable from an old crawl but the user confirmed the position was closed;
- exact-ID dedupe regression: new Huawei and Autodesk requisitions were surfaced even though the user had already applied to the same employer / nearby role family;
- policy drift: `RULES.md`, scheduler prompts, `NEXT_CHAT_PROMPT.md` and `DISCOVERY_STATE.md` began carrying overlapping but non-identical rules;
- context bloat: many `WAIT` Issues are useful historical evidence but do not need to be loaded in full on every hourly run;
- discovery recall remains weak: after strict filtering, too few genuinely new jobs survive because upstream company/source/keyword coverage is still too narrow.

These are implementation-discipline problems, not evidence that GitHub Issues should be replaced with a database or custom application.

## Non-goals

Do not add:

- a database;
- a dashboard;
- a second tracker;
- a scoring engine;
- a custom scraper framework;
- a knowledge graph for this repository;
- a company blacklist that prevents materially different roles from the same employer;
- a fixed quota that forces the system to invent or surface low-quality jobs.

`Understand-Anything`-style codebase knowledge graphs may be useful for larger code repositories, but this repository is primarily Markdown + Issues and does not justify that complexity.

## Source-of-truth model

### `PROFILE.md` — stable candidate facts

Contains only durable candidate facts, truthful experience boundaries, target role families, market priorities and work-authorization constraints.

### `RULES.md` — the only execution-policy source

All discovery, freshness, dedupe, promotion, state, authorization and maintenance rules live here.

Scheduler prompts and next-chat prompts must not copy detailed policy. They should point to `RULES.md` and require it to be read before work begins.

### GitHub Issues — live opportunity state

Only current operational states belong here:

- `ACTION`
- `APPLY`
- `CHECK`
- `WAIT`

Closed issues remain useful as history and dedupe evidence.

### `DISCOVERY_STATE.md` — rotation cursor only

Contains only the latest discovery receipt and next rotation. It is not a second rulebook and not a second tracker.

When a newly-created survivor is later invalidated in the same interactive session (for example duplicate or stale), the receipt must be reconciled so it no longer presents that role as a live survivor.

## Discovery architecture

Use a wide top-of-funnel and a strict bottom-of-funnel.

```text
broad discovery
    ↓
cheap hard mismatch filter
    ↓
cheap dedupe
    ↓
freshness proof
    ↓
fit / cohort / work authorization
    ↓
targeted Gmail dedupe
    ↓
exact application route verification
    ↓
GitHub Issue
```

### Why dedupe moves earlier

A candidate already applied to the same employer / nearby role family should normally be stopped before expensive JD, policy and route research.

This prevents work like deeply researching a third Huawei AI-application requisition only to discover that two nearby Huawei applications already exist.

## Dedupe model

Use three levels.

### Level 1 — exact requisition

`market + company + requisition/job ID`

An exact prior application is a hard duplicate.

### Level 2 — employer + role family

If the user recently applied to the same employer in the same or near-identical role family, suppress a new requisition by default.

Examples of likely same-family duplicates:

- `AI应用工程师`
- `AI应用开发工程师`
- `AI应用平台开发工程师`

A changed job ID alone is not enough to create a fresh opportunity.

### Level 3 — materially different role exception

A second role at the same company may survive when the scope is materially different or clearly stronger.

Examples:

- AI application engineer vs database-kernel engineer;
- backend product engineer vs research scientist;
- a substantially better location/team/level/fit.

When keeping a same-company role, the Issue must explicitly state **why this additional application is worth pursuing despite prior company history**.

This is not a company blacklist.

### User-confirmed application evidence

The user's direct confirmation that they already applied is sufficient dedupe evidence even when Gmail contains no receipt.

Do not treat missing email evidence as proof that no application happened.

## Freshness model

Search/index/aggregator results are discovery evidence only.

A role reaches GitHub only after current role-level liveness is proven under the existing freshness gate, such as:

- an explicit current application window;
- a currently usable exact role form / employer ATS action;
- a genuinely current role-level status/posting/update signal plus active application action.

An exact URL being retrievable is not enough.

Keep a false-negative bias rather than repeatedly surfacing stale jobs.

## Broad discovery / recall

Do not improve quantity by weakening freshness or dedupe.

Improve quantity by searching more upstream candidates.

### Singapore source rotation

Rotate across:

- official employer ATS / careers;
- LinkedIn;
- JobStreet;
- Indeed;
- selected startup / product-company sources;
- secondary feeds only as discovery inputs.

### Mainland China source rotation

Rotate across:

- official / campus portals;
- BOSS直聘;
- 牛客;
- 51job / 前程无忧;
- 智联招聘 / 智联校园;
- 猎聘;
- secondary public feeds as discovery inputs.

### Role-family rotation

Do not over-index on `AI Engineer`, `LLM` or `Agent` titles.

Search broadly across:

- Software Engineer / SDE;
- Backend Engineer;
- Full-stack Engineer;
- Platform / Infrastructure / Systems;
- Data Platform;
- Search / Retrieval;
- ML Systems / AI Platform / Inference / Evaluation;
- Applied AI;
- LLM Application;
- RAG / Agent / NLP engineering.

### Employer rotation

Do not repeatedly search the same famous companies when recent runs already covered them.

Rotate employer clusters such as:

- fintech;
- enterprise software;
- cloud / data infrastructure;
- B2B SaaS;
- consumer product companies;
- industrial software;
- healthtech;
- credible AI startups;
- other product-engineering employers.

A zero-survivor run is acceptable only after meaningful variation in source, employer and keyword lanes. Do not stop after checking only one or two familiar employers/platforms.

### No survivor quota

There is no requirement to create a fixed number of Issues per run.

The system should maximize broad candidate coverage upstream while keeping the promotion gate strict downstream.

## Web3 / crypto opportunity lane

Web3 is an **opportunistic secondary lane**, not a replacement for the SG/CN full-time search.

The main career objective remains strong full-time software / backend / platform / Applied-AI work.

However, discovery may also retain credible Web3 opportunities when they provide useful engineering work, income, network or experience.

### Employment types allowed

Web3 opportunities may include:

- full-time;
- part-time;
- contract;
- remote project-based engineering work.

Do not apply the normal `full-time only` cheap filter to this secondary lane.

### Preferred Web3 work

Prioritize engineering-heavy roles such as:

- backend / APIs;
- blockchain infrastructure;
- wallets / custody;
- exchanges / trading infrastructure;
- developer tooling / SDKs;
- data / indexing;
- smart-contract-adjacent backend work;
- AI × Web3 where the engineering scope is credible.

### Web3 quality / safety filters

De-prioritize or reject:

- anonymous or unverifiable teams;
- token-only or highly speculative compensation with no credible base arrangement;
- roles requiring the candidate to deposit money, purchase tokens or pay fees;
- pure community / shilling / influencer / BD roles when the goal is engineering;
- unclear employment arrangement or fake-company signals;
- projects with no verifiable product/team/activity;
- obvious scam or wallet-credential / seed-phrase requests.

For contract / part-time work, record the actual employment/contract arrangement when known. Do not invent tax, legal, payment or work-authorization conclusions.

Web3 discoveries use the same freshness, dedupe and evidence standards as other roles.

## Maintenance context loading

Do not load every historical `WAIT` Issue in full on every hourly run.

Default hourly context:

- fully inspect `ACTION`;
- fully inspect `APPLY`;
- fully inspect `CHECK`;
- inspect recently changed or Gmail-triggered `WAIT` items;
- retrieve older `WAIT` / closed history on demand for exact company / role-family dedupe or state reconciliation.

This reduces context dilution without deleting application history.

## State discipline

`ACTION` is reserved for a concrete employer/recruiting action that is actually worth the user's attention now or soon.

A clearly out-of-lane, low-value application should not remain `ACTION` merely because an optional questionnaire can still be completed.

The implementation pass should review obvious state contradictions exposed by the audit, including low-value `ACTION` items that the Issue itself recommends skipping.

## Thin prompts

### Hourly maintainer

The scheduler prompt should be a thin bootstrap:

1. read `README.md`, `PROFILE.md`, `RULES.md`, `DISCOVERY_STATE.md`;
2. execute the repo contract;
3. read only the operational Issue context required by `RULES.md`;
4. verify material writes;
5. never submit/contact without explicit authorization.

Detailed freshness, dedupe and search policy belongs in `RULES.md`, not duplicated in the automation prompt.

### `NEXT_CHAT_PROMPT.md`

Reduce it to a lightweight continuation pointer that tells a new chat to restore state from the repo and execute the current contract.

It must not preserve a stale private copy of discovery rules.

## Implementation scope

The implementation should make only the smallest durable changes:

1. update `RULES.md` with:
   - wider discovery coverage / stopping rule;
   - cheap dedupe before expensive verification;
   - exact + employer/role-family dedupe;
   - materially-different-role exception;
   - user-confirmed application evidence;
   - Web3 secondary lane including part-time / contract / remote;
   - selective `WAIT` loading;
   - receipt reconciliation after invalidated survivors;
2. update `PROFILE.md` only where needed to record Web3 as a secondary/opportunistic engineering lane and permit credible PT/contract work without changing the main full-time objective;
3. shrink `NEXT_CHAT_PROMPT.md` to a thin pointer;
4. reconcile `DISCOVERY_STATE.md` with the closed Huawei / Autodesk duplicates and keep it cursor-only;
5. shrink the hourly `Job Inbox Maintainer` prompt so it defers to repo rules rather than duplicating policy;
6. align `Job System Health Watch` with the single-source contract, including detection of policy drift / company-family duplicate regressions where useful;
7. review obvious current Issue-state inconsistencies exposed by this audit, without broad historical cleanup unrelated to current user attention;
8. verify every material repo / automation write by reading it back.

Do not create new tracker files or application code.

## Success criteria

The consolidation succeeds if:

1. a new chat or scheduled run reads one authoritative operating policy instead of reconstructing rules from duplicated prompts;
2. fresh discovery searches substantially broader company/source/role lanes before concluding that the market is sparse;
3. already-applied same-family employer roles are filtered cheaply before expensive research unless a concrete materially-different exception exists;
4. stale/index-only roles do not reach `CHECK` / `APPLY`;
5. credible Web3 engineering opportunities, including PT/contract/remote work, can surface without displacing the SG/CN full-time search;
6. `WAIT` history remains usable for dedupe but does not dominate every hourly context;
7. `DISCOVERY_STATE.md` stays a cursor rather than becoming policy/state duplication;
8. the system remains GitHub Issues + Gmail + small Markdown contract files, with no new framework.

## Explicit design principle

Use rigorous verification at promotion boundaries and aggressive simplicity everywhere else:

**search wide → filter cheaply → dedupe early → prove freshness → verify deeply only for real survivors → keep one source of truth.**
