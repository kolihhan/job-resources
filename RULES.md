# Operating Rules

## Goal

Get interviews and offers for a suitable engineering role without turning the search into another software project.

Priority order:

1. advance active employer responses, OA, interviews and recruiter conversations;
2. create more strong **Singapore + Mainland China** opportunities;
3. use Malaysia as a practical backup without displacing SG/CN search;
4. opportunistically keep credible Web3 / crypto engineering work, including useful part-time, contract or remote work.

Use the current resume and project evidence. Change them only for a concrete application need or repeated relevant employer feedback. Do not restart portfolio work, strategy research, application-count experiments, or another tracking system.

For unusually strong verified roles, selective recruiter/alumni/team contact research is allowed when it could help. Do not require networking for every role. Any external contact or application still requires explicit user authorization for that exact action.

## Source of truth

- GitHub Issues = current operational opportunity state.
- Gmail = evidence for receipts, recruiter messages, OA/interviews, deadlines, rejections, and targeted dedupe.
- `PROFILE.md` = stable candidate facts and search scope.
- `RULES.md` = the **only detailed execution-policy source**.
- `DISCOVERY_STATE.md` = one rolling discovery receipt/cursor only; it is **not** job state and must never become a second tracker or rulebook.
- The old Library spreadsheet = legacy/read-only reference.

Scheduler prompts and `NEXT_CHAT_PROMPT.md` must point back to this contract rather than keeping private copies of discovery, freshness or dedupe policy.

Do not create a second live tracker, dashboard, database, spreadsheet mirror, scoring engine, scraper framework, knowledge graph, or agent framework.

### Dedicated FreeHire lane

Routine FreeHire ingestion is owned by the public `kolihhan/freehirefetch` worker plus the private `FreeHire Intake` scheduler.

- `freehirefetch` may publish only public job data, exact machine-dedupe state and compact health metadata. It must not contain Gmail, application history, candidate profile data or other private recruiting state.
- The public FreeHire feed is **Stage 1 discovery evidence only**. FreeHire enrichment, timestamps and classifications are hints and never satisfy freshness, employer requirements or application-route gates by themselves.
- For **Singapore**, a healthy current FreeHire feed is the primary broad-discovery radar. The normal maintainer should not repeat a full LinkedIn / JobStreet / Indeed / generic-web sweep merely to recreate coverage that the FreeHire worker already supplied. Singapore non-FreeHire discovery should be targeted gap search: employer/source families FreeHire is not covering well, direct employer/ATS opportunities, fresh-graduate pages, smaller product/startup employers, or a concrete missing role lane.
- For **Mainland China**, FreeHire is supplementary only. BOSS, official/campus channels, 牛客, 51job, 智联, 猎聘 and direct employer discovery remain the primary discovery surface because FreeHire coverage is materially thinner there.
- `FreeHire Intake` uses two complementary passes when unseen backlog exists. First, inspect a bounded **fresh-head** set of recent unseen/changed events so a large historical backlog cannot delay newly opened jobs; this pass may inspect events beyond the sequential cursor but does **not** advance the cursor over unprocessed history. Then use remaining capacity to continue strict ascending cursor catch-up. GitHub/Gmail dedupe keeps the two passes idempotent.
- The fresh-head pass must still use the normal cheap hard filter, GitHub-history dedupe and Stage 2 verification. It is not permission to weaken freshness, fit, work-authorization, Gmail-dedupe or exact-route gates.
- Cursor advancement remains conservative: advance only through the largest contiguous prefix whose events reached a stable terminal result. Seeing or promoting a newer event in the fresh-head pass does not by itself move the sequential cursor.
- The `Job Inbox Maintainer` must not routinely rescan FreeHire. It owns lifecycle maintenance, **Singapore gap discovery**, and **Mainland-China native discovery**. Explicit interactive FreeHire probes requested by the user remain allowed.
- Preserve the compact `FreeHire intake cursor` section in `DISCOVERY_STATE.md` when the normal scheduled-discovery receipt is updated. The cursor is receipt state only, not a job tracker.
- A real FreeHire cursor gap exists only when `cursor + 1 < health.first_seq`. If the worker is stale/failed or a real gap exists, stop normal FreeHire intake and report/resync deliberately rather than silently jumping ahead or inventing another scraper.

## Every maintenance run

1. Read `README.md`, `PROFILE.md`, this file and `DISCOVERY_STATE.md`.
2. Fully inspect current `ACTION`, `APPLY` and `CHECK` Issues.
3. Inspect `WAIT` only when it changed recently, is triggered by Gmail, or is needed for exact company / role-family dedupe or reconciliation. Do **not** load all historical WAIT Issues in full every run.
4. Check both Gmail accounts for recent state-changing recruiting evidence, using a small overlap window.
5. Update existing Issues before discovery.
6. Official application receipt or user-confirmed `applied` → `WAIT`.
7. OA / interview / recruiter reply / genuinely useful requested action / time-sensitive deadline → `ACTION`.
8. Confirmed rejection / expired / duplicate / user `skip` → close the Issue.
9. Keep title, status label, body and next action synchronized.
10. Respect newer evidence over older evidence. Silence is not a rejection.

### Gmail reconciliation order

State-changing recruiting mail must be processed separately from job alerts/newsletters so discovery noise cannot crowd out lifecycle evidence.

Prioritize direct employer / ATS / recruiter messages representing application receipts, rejections/closed outcomes, OA/assessment, interview/recruiter contact, action-required deadlines, or application-status updates.

Read the actual message when metadata does not make the state change explicit. Reconcile concrete state changes to the matching GitHub Issue **before discovery**.

If exact company+role/req mapping is genuinely unresolved, record/report the ambiguity rather than guessing.

Job-alert/newsletter mail is discovery input only. Gmail should be searched narrowly: recent windows for maintenance and exact company/role/req lookups for dedupe. Do not broad-audit the entire mailbox every run.

Verify material GitHub writes by reading them back. If Gmail/GitHub access or a required write fails, report the exact incomplete step rather than claiming success.

For create operations where a timeout, connection error or transient 5xx could hide a successful side effect, do **not** immediately retry. Search/read back recent Issues using the intended exact requisition and employer + role fingerprint first. If the intended Issue already exists, adopt it. If it still does not exist, retry once only, then read back again. Persistent ambiguity must stop and be reported rather than looping or risking another duplicate.

## Chat decision sync

A clear user decision to skip, drop, ignore or withdraw an exact tracked role is authoritative and must be mirrored to GitHub when write access exists. Older Gmail evidence must not reopen it unless the user explicitly reverses the decision.

A direct user statement that they already applied is valid application-history evidence even when Gmail has no receipt. Missing email evidence is not proof that no application happened.

## Discovery schedule

During MYT hours `00/04/08/12/16/20`, run incremental discovery after maintenance. Explicit interactive searches can run at any time.

Scheduled discovery uses six MYT windows:

- `00:00-03:59` → `00`;
- `04:00-07:59` → `04`;
- `08:00-11:59` → `08`;
- `12:00-15:59` → `12`;
- `16:00-19:59` → `16`;
- `20:00-23:59` → `20`.

Before scheduled discovery, inspect the latest `DISCOVERY_STATE.md` receipt. If the current window already contains a completed **SG gap + CN native** discovery that satisfies the current contract and whose receipt was written and read back successfully, do maintenance only and skip duplicate scheduled discovery for that window.

A narrow interactive role lookup or probe does **not** consume the scheduled window. An explicit interactive run may count for the current window only when it intentionally completed the current Singapore gap-discovery and Mainland-China native-discovery contract and wrote a valid receipt. If a prior run was incomplete, skipped a main market, had a required write failure, or lacked a verified receipt, the window remains incomplete.

**SG + CN are the main discovery markets.** Malaysia is backup. Web3 is an opportunistic secondary lane, not a replacement for SG/CN full-time search.

Do not restart the whole market every run. Rotate source families, employer clusters and role keywords. Do not repeatedly search the same familiar companies when recent runs already covered them. In Singapore, use FreeHire coverage as the default broad radar and spend normal-discovery effort on gaps rather than recreating the same board coverage. In Mainland China, continue rotating native sources broadly.

## Discovery receipt / rotation memory

Before every scheduled discovery run, read `DISCOVERY_STATE.md` and use its `next rotation` to avoid repeating the same lane.

After every scheduled discovery run, preserve any `FreeHire intake cursor` section and overwrite only the normal `Current receipt` with:

- completed run time in MYT;
- SG **gap** source families / employer or role lanes actually tried;
- CN native source families / employer or role lanes actually tried;
- optional Web3 lane tried, if any;
- compact SG/CN coverage counters, plus optional Web3 counters when that lane was searched;
- serious-survivor Issue numbers created/updated, or `none`;
- concrete access/search failures, if any;
- next source / keyword / employer rotation.

Coverage counters use exactly these meanings:

- **candidate** = one distinct employer + role + location/market opportunity considered far enough to make a cheap-screen decision; repeated mirrors/copies of the same opportunity count once;
- **distinct employer** = the canonical employer/client when known, not every board or recruiter mirror;
- **source family** = a materially different discovery channel such as official employer/ATS, FreeHire/public job-feed aggregator, LinkedIn, JobStreet, Indeed, 牛客, 智联, BOSS, 51job, 猎聘, or a selective Web3/TG feed; multiple queries inside one channel still count as one family;
- **deep-verified** = a candidate that passed the cheap hard filter and cheap GitHub dedupe and therefore entered Stage 2 verification.

Compact format:

`SG coverage: N candidates / N employers / N source families / N deep-verified`

`CN coverage: N candidates / N employers / N source families / N deep-verified`

`Web3 coverage: N candidates / N employers / N source families / N deep-verified` when used.

These counts are **observability only**. They are not quotas, scores, history tables, success targets or minimums. A run with many screened candidates and zero survivors may be healthy; a low-coverage run is not automatically wrong, but its limited search effort must be visible.

For Singapore, zero survivors from the maintainer's gap search can be healthy when the FreeHire worker/intake is current and the gap lanes were meaningfully varied; the maintainer does not need to reproduce the entire SG market every window. For Mainland China, a zero-survivor run is healthy only after meaningful variation in source, employer and role-keyword lanes. If a source is blocked or weak, try another useful lane in that market before concluding the market is sparse when practical.

Do not put raw rejected candidates, long search logs, dashboards, scores or duplicated policy in `DISCOVERY_STATE.md`.

If a newly-created survivor is later invalidated in the same interactive or scheduled run—for example stale or duplicate—reconcile `DISCOVERY_STATE.md` before finishing so it no longer presents that role as live.

For a scheduled discovery window, the run is not fully complete until the receipt is updated and read back successfully.

## Discovery pipeline

Use a wide top-of-funnel and strict promotion gate:

`broad discovery → cheap hard filter → cheap dedupe → freshness proof → fit/cohort/work-auth → targeted Gmail dedupe → exact application route → Issue`

### Stage 1 — broad discovery

Search broadly across employers and role families before spending expensive verification effort. In Singapore, broadness is primarily supplied by the dedicated FreeHire worker; the maintainer fills coverage gaps. In Mainland China, broadness still comes primarily from native job platforms and direct employer/campus channels.

Role families include:

- Software Engineer / SDE;
- Backend Engineer;
- Full-stack Engineer;
- Platform / Infrastructure / Systems;
- Data Platform;
- Search / Retrieval;
- ML Systems / AI Platform / Inference / Evaluation;
- Applied AI / AI Software Engineer;
- LLM Application / RAG / Agent / NLP engineering.

Do not over-index on `AI Engineer`, `LLM` or `Agent` titles.

Rotate employer clusters such as fintech, enterprise software, cloud/data infrastructure, B2B SaaS, consumer products, industrial software, healthtech, credible AI startups and other product-engineering employers.

Cheap-screen only obvious hard mismatches:

- wrong country for the SG/CN full-time lane;
- Senior / Staff / Lead / Manager or hard 5+ YOE without a graduate exception;
- explicit incompatible graduation/cohort window;
- explicit citizenship / no-sponsorship blocker where relevant;
- substantial hard stack/domain mismatch;
- clearly stale/closed listing.

Only genuine hard requirements may trigger cheap rejection. Wording such as `preferred`, `plus`, `bonus`, `nice to have`, `familiarity with`, `exposure to`, `coursework`, `self-study`, `personal projects`, or `willingness to learn` is non-hard by default unless the surrounding JD clearly makes it mandatory. Preserve ambiguous wording for Stage 2 verification instead of strengthening it by inference.

Unambiguous mandatory professional-experience language such as `5+ years required` or `must have production experience in X` can remain a hard blocker. A soft gap is a later fit consideration, not fabricated professional YOE.

Do **not** reject Web3 secondary-lane work merely because it is part-time, contract, remote or project-based.

At broad-discovery stage do not stop to research salary/WLB, unknown SG sponsorship, unknown CN permit willingness, exact ATS routing, both Gmail accounts, detailed company history or networking contacts for every raw candidate.

Public unauthenticated job feeds may be used as broad-discovery inputs. FreeHire is the primary aggregated broad-discovery input for Singapore and a supplementary input for Mainland China. Treat feed-enriched seniority, freshness and classification as hints rather than employer truth. Do not strengthen ambiguous feed metadata into a hard rejection unless the employer-controlled JD supports it. Routine FreeHire ingestion is the dedicated lane above and must not also be repeated by normal scheduled discovery.

Raw discovery candidates do not become GitHub Issues.

### Cheap dedupe before expensive research

Before deep JD/policy/route research, run cheap GitHub-history dedupe:

1. exact requisition/job ID;
2. same employer + same or near-identical role family;
3. explicit user-confirmed prior application history.

If recent history already shows the same employer + same/near-identical role family, suppress the new requisition by default before expensive research.

A changed job ID alone is **not** enough to make the opportunity new.

This is not a company blacklist. A same-company role may continue when it is materially different or unusually stronger—for example a different engineering family, team/scope, location/level or substantially better fit. If it survives, the eventual Issue must explicitly state **why another application at this employer is worth pursuing despite prior company history**.

### Stage 2 — verify serious survivors

For candidates that survive the cheap screen and early dedupe, verify:

1. exact/full JD and current liveness under the freshness gate;
2. graduation/cohort, seniority and hard requirements;
3. candidate fit and any material work-authorization blocker;
4. targeted Gmail dedupe in both accounts by company/role/req;
5. ATS/candidate history only when materially available;
6. exact usable application route.

For aggregator-discovered survivors, prefer the employer-controlled official role page or public ATS posting/API for the exact requisition when available. Aggregator/feed data by itself never satisfies the freshness or application-route hard gates; an ATS source counts only when it maps to the exact role and meets the same current-run liveness/route requirements below.

Only serious survivors reach GitHub Issues.

Do not run expensive mailbox-wide dedupe for raw candidates.

## Singapore — primary

Use a **FreeHire-first, gap-search-second** strategy:

1. dedicated FreeHire worker/intake for broad current-market radar;
2. official company careers / ATS for direct-employer gaps, fresh-graduate pages and exact verification;
3. LinkedIn, JobStreet and Indeed only for targeted gaps, unusual strong leads, or when FreeHire coverage is stale/weak—not as a routine full duplicate sweep;
4. selected credible startup / product-company sources that are poorly represented in aggregated feeds;
5. selective secondary feeds such as DeJob / Telegram as discovery inputs only.

MyCareersFuture is evidence-only for this candidate. If the only verified route is MCF, block/close the role unless a separate current non-MCF exact route exists.

Unknown sponsorship is **not** a discovery-stage rejection. Explicit no-sponsorship is.

## Mainland China — primary

Use a **native-source-first** strategy. Rotate across:

1. BOSS直聘;
2. official company careers / campus portals / useful recruiting WeChat pages;
3. 牛客;
4. 51job / 前程无忧;
5. 智联招聘 / 智联校园;
6. 猎聘;
7. FreeHire and other public unauthenticated feeds as supplementary discovery only;
8. LinkedIn and selective DeJob / Telegram secondary feeds as discovery inputs.

The candidate graduated in **2026**. Favor evidence such as `2026届`, `往届可投`, `毕业两年内`, `应届/往届`, `0-1年`, `0-3年`, `初级`, `海外留学生`, `recent graduate` or `recently completed`.

Clearly 2027-only roles are normally filtered unless official wording explicitly includes a 2026 graduate or applicable overseas-graduate window.

Do not equate legal foreign-work-permit possibility with employer willingness to hire a foreign fresh graduate. Employer willingness may remain unknown until engagement.

Do not let CN discovery collapse into SG simply because CN sources are harder to inspect. Change CN employer/source/keyword lanes in the same run before concluding the market is sparse.

## Malaysia — backup

Do not let Malaysia consume the main SG/CN search budget.

Search Malaysia when SG/CN remains sparse after reasonable broadening, or when an unusually strong Malaysian opportunity appears naturally.

Lean more toward AI Engineer / Applied AI / AI Software Engineer / LLM / RAG / Agent / AI backend-platform roles, while keeping strong normal SWE/backend roles when their engineering environment is better than a weak AI-titled job.

Do not apply SG/CN foreign-work-authorization blockers to Malaysia. Do not assume future internal transfer without evidence.

## Web3 / crypto — opportunistic secondary lane

Credible Web3 work may be kept when it offers useful engineering work, income, network or experience. Allowed employment types include full-time, part-time, contract, and remote/project-based engineering work.

Prefer engineering-heavy work such as backend/APIs, blockchain infrastructure, wallets/custody, exchanges/trading infrastructure, developer tooling/SDKs, data/indexing, smart-contract-adjacent backend work, and AI × Web3 with credible engineering scope.

De-prioritize or reject unverifiable teams, compensation arrangements with no credible base, roles that require payments/purchases or access secrets, pure community/shilling/influencer/BD work when the goal is engineering, and unclear fake-company signals.

For PT/contract roles, record the real employment/contract arrangement when known. Do not invent tax, legal, payment or work-authorization conclusions.

Web3 candidates use the same freshness, dedupe and evidence standards as other roles.

## Telegram / DeJob source marking

Telegram/DeJob is a discovery source, not authoritative proof.

For any Issue first discovered there:

- prefix the title with `[TG]` after the market tag;
- record `Source: TG / DeJob` and the public source link;
- independently verify company, exact role/JD, liveness, requirements, dedupe and route;
- keep anonymous, recruiter-only, unclear-company or otherwise unverifiable leads out of GitHub unless they survive verification.

## Company / role quality

Prefer established engineering/product employers and credible product startups with clear engineering work.

De-prioritize staffing/bodyshop/outsourcing unless there is unusually strong evidence of direct, high-quality engineering work.

Do not reject a strong role because of missing nice-to-haves. Distinguish hard requirements from preferences.

Never convert part-time work, internships, projects or master's study into fictitious full-time professional YOE.

## Freshness hard gate before Issue creation

A role must pass this gate **before** a new `CHECK` or `APPLY` Issue is created. `CHECK` is not a quarantine state for possibly stale jobs.

An exact URL being retrievable today does **not** prove the employer is still accepting applications today.

Current liveness requires at least one strong current-run role-level signal:

1. explicit application / validity / closing window including the current date; or
2. the actual exact-role candidate form or employer-controlled ATS start/submit flow renders and is usable now; or
3. an official role page has a genuinely current role-level status/post/update timestamp from the last 7 days **and** an active role-level application action.

These are discovery evidence only, not liveness proof by themselves:

- search result / indexed snippet;
- mirror / aggregator copy;
- old cached/crawled exact page;
- stale Apply button;
- generic careers page;
- undated role page when current application flow cannot be established.

If the exact page is older than 7 days and there is no explicit still-valid window or usable live exact flow, liveness is unproven. Keep it raw; do not create `CHECK` merely to ask whether it is closed.

If tools cannot distinguish live from cache, require a second independent current role-level signal. Prefer a false negative over repeatedly surfacing stale jobs.

A user report such as `closed position`, `expired` or equivalent current employer/platform evidence overrides older evidence immediately.

## Application-route hard gate

`APPLY` requires a fresh, usable, end-to-end exact-role application route.

Search results, cached/indexed copies, mirrors and generic career/search/location pages are discovery evidence only. Follow intermediary Apply buttons far enough to identify the final destination.

Final-route proof requires at least one of:

1. the actual candidate application form for the exact role renders and is usable;
2. an employer-controlled ATS page for the exact requisition exposes a real start/submit action with no unresolved redirect;
3. a platform-native exact-role application/contact flow is directly usable with no unresolved external redirect.

If login/JavaScript/cookies/bot protection/tool limits prevent verifying the route, use `CHECK` only when liveness is independently proven. If the final destination is removed, expired, ambiguous or MCF-only, close/block as appropriate.

Platform-native actions such as LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客 or 猎聘 may count when the actual exact-role action is directly usable and does not redirect to a blocked channel.

Before presenting an `APPLY` as ready, and again immediately before acting on a user `go`, fresh-check the exact application route.

## Dedupe

Use three levels:

### Level 1 — exact requisition

Primary fingerprint:

`market + company + requisition/job ID`

An established prior application to the exact requisition is a hard duplicate.

### Level 2 — employer + role family

A recent application to the same employer in the same or near-identical role family suppresses a new requisition by default even when the job ID differs.

Examples such as `AI应用工程师`, `AI应用开发工程师` and `AI应用平台开发工程师` normally belong to the same broad AI-application family unless current scope proves a material difference.

### Level 3 — materially different exception

A same-company role may survive when the engineering family/scope/team/level/location is materially different or the opportunity is unusually stronger. Record the concrete reason before promoting it.

For serious survivors that pass cheap dedupe, check:

1. existing open/closed GitHub Issues;
2. targeted `lihhanko526@gmail.com`;
3. targeted `lihhanko3@gmail.com`;
4. ATS/candidate history when materially available.

User-confirmed prior application history is valid even without a receipt.

## When to create an Issue

Create an Issue only for a serious survivor that deserves user attention.

It must have:

- plausible early-career fit;
- no obvious cohort/seniority hard block;
- credible role/company quality;
- current role-level liveness proof;
- no established duplicate application under the three-level dedupe model;
- either a verified exact application route or exactly one material blocker remaining **other than liveness**.

Bad/stale/obvious-mismatch raw candidates create nothing.

## Issue states

Only four open states:

- `ACTION`
- `APPLY`
- `CHECK`
- `WAIT`

Meanings:

- `ACTION` = a concrete employer/recruiting action worth the user's attention now or soon: OA, interview, recruiter reply, useful requested form/document, or real deadline. Do not use `ACTION` merely because an out-of-lane application could optionally be continued.
- `APPLY` = verified serious survivor ready for user review, with a usable exact application route. It is not submission permission.
- `CHECK` = liveness is proven; exactly one other material blocker or user decision remains, with exactly one next action.
- `WAIT` = already submitted/contacted and waiting for employer activity; do not duplicate.

## Labels and consistency

Every open opportunity Issue must have exactly one market label (`market:sg`, `market:cn`, or `market:my`) and one matching operational status label.

Closed intentional outcomes may keep `status:skipped` or `status:blocked`; MCF-only SG roles may also use `blocked:mcf`.

Whenever state changes, update title, status label, body and next action together.

Maintenance invariants:

- no closed Issue retains `status:action`, `status:apply`, `status:check` or `status:wait`;
- no closed Issue title remains `[ACTION]`, `[APPLY]`, `[CHECK]` or `[WAIT]`;
- SG route resolving only to MCF → blocked/closed unless a separate current non-MCF route exists;
- user `skip` / `no` / `don't want` → terminal skipped state;
- confirmed unusable route → terminal blocked state;
- after any close/relabel, read back title, labels, body/outcome and state.

## APPLY / CHECK content

Store enough to make a decision without repeating research:

- exact role link / route or the one CHECK blocker;
- req/job ID and verification date when available;
- freshness proof;
- plain-language work;
- hard requirements / early-career fit;
- specific strengths/gaps;
- material work-authorization evidence when known;
- targeted GitHub/Gmail dedupe result;
- same-company materially-different reason when applicable;
- exactly one next action;
- source links.

Salary, WLB, company background and networking research are optional and should be added only when decision-relevant.

## Authorization

`APPLY` means recommended for user review, not permission to submit.

Only explicit authorization for that exact role/action permits an application or external contact. Never mass apply or automatically send outreach.

## Privacy

Store only operational facts. Do not copy authentication material, private access credentials, or unnecessary personal identifiers into Issues.

## Keep it small

Do not add Projects, another database/dashboard/frontend/spreadsheet, a score file, custom scraper, knowledge graph, or new application framework unless repeated real failures prove the current GitHub-Issues model inadequate.