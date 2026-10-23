# Operating Rules

## 1. Goal and priority

Get interviews and offers for a strong engineering role without turning the search into another software project.

Priority order:

1. advance active employer responses, OA, interviews, recruiter conversations and real deadlines;
2. reconcile GitHub/Gmail lifecycle state before discovering more jobs;
3. create strong **Singapore + Mainland China + Hong Kong** opportunities;
4. run **Malaysia TOP-only** in parallel;
5. keep credible Web3 / crypto engineering work as an opportunistic secondary lane.

For the main first-job search, optimize for:

**realistic interview probability × engineering environment × work interest × company/team quality × career portability**.

Prefer permanent full-time employment. Applied AI is a differentiator, not a substitute for engineering quality.

Do not restart portfolio work, strategy research, application-count experiments or another tracking system unless a concrete application or repeated employer feedback proves it is needed.

Any application, recruiter outreach or other employer-facing action requires explicit user authorization for that exact action.

---

## 2. Source of truth

- **GitHub Issues** = live operational opportunity state.
- **Gmail** = application receipts, recruiter messages, OA/interviews, deadlines, rejections and targeted dedupe evidence.
- **`PROFILE.md`** = stable candidate facts, current positioning and market scope.
- **`RULES.md`** = the only detailed execution-policy source.
- **`DISCOVERY_STATE.md`** = one rolling discovery receipt/cursor + next rotation only; never a second job tracker or rulebook.
- Old spreadsheet = legacy/read-only reference.

Scheduler prompts and `NEXT_CHAT_PROMPT.md` must point back to these files rather than copying policy.

Do not create another dashboard, database, spreadsheet mirror, scoring engine, scraper framework, knowledge graph or agent framework.

---

## 3. Current market contract

### Singapore — active target

- Search strong early-career SWE/backend/platform/data/search/AI roles.
- Work authorization: employer-supported EP or S Pass.
- `UNKNOWN` sponsorship willingness is allowed at APPLY.
- Explicit no-sponsorship / local-right-to-work-only wording is `BLOCKED`.
- MyCareersFuture is evidence-only for this candidate. **MCF-only route = blocked/closed** unless a separate verified non-MCF route exists.
- Use FreeHire as the broad radar; normal discovery focuses on coverage gaps and direct employer/ATS opportunities.

### Mainland China — active target

- Search product engineering, AI-native startups, enterprise AI, developer tools, backend/platform, search/retrieval, RAG/Agent and ML-systems roles.
- Work authorization: employer-supported Mainland China foreign work permit.
- Employer willingness may remain `UNKNOWN` until engagement; UNKNOWN alone does not block APPLY.
- Favor `2026届`, recent graduate, 0–3 YOE and unusually strong 2–4 YOE stretch opportunities.
- Clearly 2027-only roles are filtered unless official wording explicitly includes this 2026 graduate or an applicable overseas-graduate window.
- Use native sources first: BOSS, official/campus portals, 牛客, 51job, 智联, 猎聘.

### Hong Kong — active target

- Search strong engineering, AI, fintech, digital-bank, product and research-to-product roles.
- Work authorization: employer-supported **General Employment Policy (GEP)** route.
- `UNKNOWN` GEP sponsorship willingness is allowed at APPLY.
- Explicit local-right-to-work / no-sponsorship wording is `BLOCKED`.
- Do not substitute TTPS or another unrelated immigration path for employer-route verification.
- Prefer permanent full-time employment. A fixed-term research appointment may remain `CHECK` only when it is unusually strong and the one remaining decision is whether the user accepts that exact fixed-term exception.

### Malaysia — TOP-only parallel lane

- Malaysian candidate; do not spend search time on sponsorship verification.
- **TOP is role-level, not logo-level.**
- Prefer strong AI/application/backend/platform/SWE roles with credible engineering depth, compensation/WLB/growth when knowable, mentorship and career portability.
- A famous bank, GLC, consultancy or MNC name alone does not make a role TOP.
- Generic operations, low-depth IT support, bodyshop/outsourcing or weak consulting implementation roles should not crowd the queue.

### Web3 / crypto — opportunistic secondary lane

Credible full-time, part-time, contract or remote/project engineering work may survive when it provides useful engineering experience, income or network value. Prefer backend/API, infrastructure, wallets/custody, exchanges/trading infra, developer tooling/SDK, data/indexing and credible AI × Web3 work.

Reject unverifiable teams, payment/purchase requirements, requests for credentials/secrets, pure shilling/community roles or unclear fake-company signals.

---

## 4. Every maintenance run

Before discovery:

1. read `README.md`, `PROFILE.md`, `RULES.md` and `DISCOVERY_STATE.md`;
2. fully inspect current `ACTION`, `APPLY` and `CHECK` Issues;
3. inspect `WAIT` only when recent, Gmail-triggered or needed for exact company/role-family dedupe;
4. check **both Gmail accounts** for recent state-changing recruiting evidence using a small overlap window;
5. update existing Issues before creating new opportunities.

State transitions:

- official application receipt or user-confirmed `applied` → `WAIT`;
- OA / interview / recruiter reply / genuinely useful requested action / time-sensitive deadline → `ACTION`;
- confirmed rejection / expired / duplicate / user `skip` → close;
- silence is not rejection;
- newer evidence overrides older evidence.

Keep title, status label, body and next action synchronized.

### Gmail reconciliation

Process direct employer/ATS/recruiter mail before job-alert/newsletter discovery noise.

Prioritize:

- application receipts;
- rejection/closed outcomes;
- OA/assessment;
- interview/recruiter contact;
- action-required deadlines;
- application-status updates.

Read the actual message when metadata does not make the state change explicit. If exact company+role/req mapping is unresolved, record the ambiguity instead of guessing.

A direct user statement that they already applied is valid application-history evidence even without an email receipt.

---

## 5. Discovery schedule and rotation

Scheduled MYT windows remain:

- `00:00-03:59` → `00`
- `04:00-07:59` → `04`
- `08:00-11:59` → `08`
- `12:00-15:59` → `12`
- `16:00-19:59` → `16`
- `20:00-23:59` → `20`

Explicit interactive searches may run at any time.

Before scheduled discovery, read `DISCOVERY_STATE.md`. If the current window already has a completed run satisfying the current contract and the receipt was written/read back successfully, do maintenance only and skip duplicate scheduled discovery.

Do not restart the whole market every run. Rotate employer clusters, source families and role keywords.

Operational cadence:

- **SG + CN remain high-frequency baseline lanes.**
- SG normal discovery = targeted gap search, because FreeHire owns broad SG radar.
- CN normal discovery = native-source-first broad rotation.
- **HK and MY TOP are active rotating lanes**, not out-of-scope. Add one of them when practical according to the current `next rotation`, or search them directly when the user asks.
- A narrow interactive lookup does not consume a scheduled window unless it intentionally completes the scheduled contract and writes the receipt.

If an initial lane yields only duplicates/hard rejects, expand to another useful employer/source cluster before concluding the market is sparse when practical.

### Discovery receipt

After a scheduled run, preserve any FreeHire cursor section and update only the rolling `Current receipt` with:

- completed run time in MYT;
- markets/source families/employer or role lanes actually tried;
- compact coverage counters for markets searched;
- serious-survivor Issue numbers created/updated, or `none`;
- concrete access/search failures;
- next rotation.

Counter meanings:

- **candidate** = one distinct employer + role + location/market considered far enough for cheap-screen decision;
- **distinct employer** = canonical employer/client;
- **source family** = materially different channel, not query count;
- **deep-verified** = candidate that passed cheap hard filter + cheap GitHub dedupe and entered Stage 2.

Counts are observability only, never quotas or scores.

Do not put raw rejected candidates, long search logs or duplicated policy into `DISCOVERY_STATE.md`.

---

## 6. Discovery pipeline

Use this pipeline:

`broad discovery → cheap hard filter → cheap GitHub dedupe → current liveness/eligibility → fit/work-auth classification → exact-ID Gmail dedupe → exact application route → Issue`

Raw discovery candidates do **not** become Issues.

### Stage 1 — broad discovery

Search role families beyond just `AI Engineer` / `LLM` / `Agent`:

- Software Engineer / SDE;
- Backend / Full-stack;
- Platform / Infrastructure / Systems;
- Data Platform;
- Search / Retrieval;
- ML Systems / AI Platform / Inference / Evaluation;
- Applied AI / AI Software Engineer;
- LLM Application / RAG / Agent / NLP engineering.

Rotate employer clusters such as fintech, enterprise software, cloud/data infra, B2B SaaS, consumer product, industrial software, healthtech and credible AI startups.

### Cheap hard filter

Reject cheaply only for genuine hard mismatches:

- wrong market/location for the lane;
- Senior / Staff / Lead / Manager or hard 5+ YOE without a graduate/early-career exception;
- explicit incompatible graduation/cohort window;
- explicit citizenship / no-sponsorship / right-to-work-only blocker where relevant;
- substantial mandatory stack/domain mismatch;
- clearly closed/expired/unusable listing;
- main-lane fixed-term contract, staffing/bodyshop or project-only employment without an explicit user-approved exception.

Do **not** strengthen soft wording into hard requirements. `Preferred`, `plus`, `bonus`, `nice to have`, `familiarity`, `exposure`, coursework, self-study, personal projects and willingness to learn are non-hard unless the JD clearly says otherwise.

Mandatory `3+ years` is a meaningful negative signal but **not an automatic reject**. Deep-verify only when company/work/fit are strong enough to justify the stretch.

Never convert master's study, projects, internships or part-time work into fictitious full-time professional YOE.

At Stage 1, do not waste time on detailed salary/WLB, exact ATS routing, both Gmail accounts or deep sponsorship research for every raw lead.

---

## 7. Cheap dedupe before expensive research

Before Stage 2, check GitHub history in this order:

1. exact requisition/job ID;
2. same employer + same/near-identical role family;
3. explicit user-confirmed prior application history.

A same-employer role-family hit is a comparison flag, not an automatic duplicate.

Suppress when:

- it is the exact prior application;
- it is a demonstrably near-identical team/scope/repost;
- an employer's documented application limit makes another submission inappropriate.

A changed job ID alone is **not** enough to make an opportunity new.

A same-company role may survive when the engineering family, team/scope, location/level is materially different or the opportunity is unusually stronger. If promoted, the Issue must say why another application at this employer is worth pursuing.

---

## 8. Stage 2 — verify serious survivors

For serious survivors verify:

1. exact/full JD and current role-level liveness;
2. graduation/cohort, seniority, employment type and hard requirements;
3. candidate fit and work-authorization classification;
4. targeted Gmail dedupe in **both accounts**, using exact requisition/job ID first when available;
5. ATS/candidate history only when materially available;
6. exact usable application route.

### Exact-ID invariant

Before creating/promoting any `CHECK` or `APPLY` with a requisition/job ID, search that exact ID in:

- GitHub;
- `lihhanko526@gmail.com`;
- `lihhanko3@gmail.com`.

Exact employer receipt or user-confirmed prior application → `WAIT`, not a new opportunity.

---

## 9. Work authorization classification

Use:

- `CONFIRMED` — current employer/role evidence supports the needed path;
- `PROBABLE` — meaningful employer evidence makes support credible but not confirmed for this exact candidate;
- `UNKNOWN` — no reliable yes/no evidence yet;
- `BLOCKED` — explicit no-sponsorship/right-to-work/citizenship constraint or another confirmed legal/employer blocker.

**UNKNOWN is allowed to reach APPLY. BLOCKED is not.**

Legal eligibility alone does not imply employer willingness, and lack of public sponsorship wording is not by itself a CHECK blocker.

For SG/CN/HK, employer realism is a prioritization signal: explicit support, prior foreign hiring, graduate/0–3 YOE hiring, mature HR, international operations and pass-compatible compensation when known are positive evidence. Company size alone is weak evidence.

---

## 10. Freshness and current-liveness gate

Freshness is a **ranking signal, not a 30-day death sentence**.

- Prefer newly posted/recently updated exact roles, especially <=30 days.
- A >30-day or undated exact role may still reach `CHECK`/`APPLY` when it is **currently accepting applications**, the candidate is currently eligible and the opportunity is strong enough.
- Never use crawler/search/mirror recency to pretend an old role is new.
- Never infer current cohort eligibility from historical wording.

Current liveness is a hard requirement before a new Issue is created.

Strong current-run liveness proof requires at least one of:

1. explicit application/validity/closing window covering the current date;
2. actual exact-role candidate form or employer ATS start/submit flow renders and is usable;
3. official exact role page exposes a current active application action with no contradictory closed/expired signal;
4. employer-controlled ATS response explicitly marks the exact requisition open/published and accepting applications.

Search snippets, mirror copies, generic career pages, crawler timestamps and stale Apply buttons are discovery evidence only. If tools cannot distinguish live from cache, require another current role-level signal.

A current user report or employer/platform signal that the role is closed/expired overrides older evidence immediately.

---

## 11. Application-route hard gate

`APPLY` requires a current usable exact-role application route.

Valid final-route proof includes:

1. exact candidate form renders and is usable;
2. employer-controlled ATS exact requisition exposes a real start/submit action with no unresolved redirect;
3. platform-native exact-role application/contact flow is directly usable with no unresolved external redirect.

Platform-native LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客, 猎聘 or similar may count when the exact-role action is usable.

If login/JavaScript/cookies/bot protection/tool limits prevent route verification, use `CHECK` only when liveness is independently proven and route verification is the **one** remaining blocker.

Removed/expired/ambiguous final destination → blocked/closed as appropriate.

Before presenting an APPLY as ready, and again immediately before acting on a user `go`, fresh-check the exact application route.

---

## 12. When to create an Issue

Create an Issue only for a serious survivor deserving user attention.

It must have:

- plausible early-career fit;
- no obvious cohort/seniority hard block;
- credible role/company/team quality;
- current role-level liveness proof;
- acceptable main-lane employment type or explicit user-approved exception;
- no established duplicate under the dedupe model;
- either a verified exact application route or exactly one material blocker remaining **other than sponsorship/work-permit UNKNOWN**.

Bad, closed, obvious-mismatch or raw candidates create nothing.

---

## 13. Issue states

Only four open states:

- `ACTION`
- `APPLY`
- `CHECK`
- `WAIT`

Meanings:

- `ACTION` = concrete recruiting action worth attention now/soon: OA, interview, recruiter reply, useful requested form/document or real deadline.
- `APPLY` = verified serious survivor ready for user review with usable exact route. Work auth may be CONFIRMED/PROBABLE/UNKNOWN. **APPLY is not submission permission.**
- `CHECK` = liveness proven; exactly one material blocker or user decision remains, with exactly one next action. Unknown sponsorship alone is not a CHECK blocker.
- `WAIT` = already submitted/contacted and waiting for employer activity; do not duplicate.

Rejected, expired, duplicate, blocked, withdrawn or user-skipped roles are closed.

### Labels and consistency

Every open opportunity must have:

- exactly one market label: `market:sg`, `market:cn`, `market:hk`, or `market:my`;
- exactly one matching status label: `status:action`, `status:apply`, `status:check`, or `status:wait`.

Closed intentional outcomes may use `status:skipped` or `status:blocked`; MCF-only SG roles may also use `blocked:mcf`.

Whenever state changes, update title, labels, body and next action together.

Maintenance invariants:

- no closed Issue keeps an open status label/title;
- SG MCF-only route → blocked/closed unless a separate current non-MCF route exists;
- user `skip` / `no` / `don't want` → terminal skipped state;
- confirmed unusable route → terminal blocked state;
- exact prior application found → WAIT;
- an HK role previously closed **only** because HK was out-of-scope may be reconsidered, but must be revalidated for current liveness/route before reopening;
- after close/relabel/reopen, read back title, labels, body/outcome and state.

### APPLY / CHECK content

Store enough to decide without repeating research:

- exact role link/route or the one CHECK blocker;
- req/job ID and verification date when available;
- liveness/age evidence where useful;
- employment type;
- plain-language work;
- hard requirements / early-career fit;
- specific strengths/gaps;
- work-auth classification/evidence;
- targeted GitHub/Gmail dedupe result;
- same-company materially-different reason when applicable;
- exactly one next action;
- source links.

Salary, WLB, company background and networking research are optional unless decision-relevant.

---

## 14. Authorization

`APPLY` means recommended for review, not permission to submit.

Only explicit authorization for that exact role/action permits an application or external contact. Never mass-submit or automatically send outreach.

`go` on one exact role does not authorize other roles at the same employer.

---

## 15. Dedicated FreeHire lane

Routine FreeHire ingestion is owned by public `kolihhan/freehirefetch` plus the private `FreeHire Intake` scheduler.

- FreeHire contains public job data and machine-dedupe/health metadata only; never Gmail/application/private candidate state.
- FreeHire is **Stage 1 discovery evidence only**. Its enrichment/timestamps/classifications do not satisfy employer requirements, liveness or route gates.
- SG: FreeHire is the primary broad radar; normal maintainer discovery should not recreate the same full LinkedIn/JobStreet/Indeed sweep.
- CN: FreeHire is supplementary only; native sources remain primary.
- Fresh-head inspection may look beyond the sequential cursor but must not move the cursor over unprocessed history.
- Cursor advances only through the largest contiguous processed prefix.
- A real cursor gap exists only when `cursor + 1 < health.first_seq`. If worker health is stale/failed or a real gap exists, stop normal intake and report/resync rather than guessing.
- Preserve the FreeHire cursor section when updating `DISCOVERY_STATE.md`.

---

## 16. Source-specific notes

### Singapore

Use FreeHire-first + direct-employer/ATS gap search. LinkedIn/JobStreet/Indeed are targeted gap tools rather than a routine duplicate broad sweep.

### Mainland China

Rotate BOSS → official/campus → 牛客 → 51job → 智联 → 猎聘, with LinkedIn/other feeds supplementary.

Do not let CN discovery collapse simply because sources are harder to inspect; change source/employer/keyword lanes before declaring it sparse.

### Hong Kong

Prefer official employer/ATS, LinkedIn/JobsDB and direct fintech/product/AI/research employers. Verify GEP willingness only as far as evidence allows; unknown is acceptable, explicit blocker is not.

### Malaysia

Prefer official careers, LinkedIn, JobStreet/Hiredly and direct employers. Apply the `PROFILE.md` TOP filter before deep verification so ordinary fallback roles do not fill the live queue.

### Telegram / DeJob

Discovery source only, never authoritative proof. For a survivor first found there:

- add `[TG]` after the market tag in the title;
- record source + public source link;
- independently verify company, exact role/JD, liveness, requirements, dedupe and route;
- anonymous/recruiter-only/unclear-company leads do not reach GitHub unless independently verified.

---

## 17. GitHub write safety

Verify material GitHub writes by reading them back.

If Gmail/GitHub access or a required write fails, report the exact incomplete step rather than claiming success.

For create operations where a timeout/connection error/transient 5xx could hide a successful side effect:

1. do **not** immediately retry;
2. search/read back recent Issues using exact req + employer/role fingerprint;
3. adopt the Issue if it already exists;
4. if still absent, retry once;
5. read back again;
6. persistent ambiguity stops the write loop.

---

## 18. Privacy and keep-it-small rule

Store only operational facts. Do not copy credentials, authentication material or unnecessary personal identifiers into Issues.

Do not add Projects, another database/dashboard/frontend/spreadsheet, score file, custom scraper, knowledge graph or new application framework unless repeated real failures prove the current GitHub-Issues model inadequate.
