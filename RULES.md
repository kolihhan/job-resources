# Operating Rules

## 1. Goal and priority

Get interviews and offers for a **permanent full-time** engineering role without turning the search into another software project.

Current execution mode is **broad-throughput application generation** across Singapore, Mainland China and Malaysia.

Priority order:

1. advance active employer responses, OA, interviews, recruiter conversations and real deadlines;
2. reconcile GitHub/Gmail lifecycle state before discovering more jobs;
3. find and verify realistically applicable roles across **SG + CN + MY**;
4. prioritize stronger companies/teams, Applied-AI fit and low-friction routes first, but do not use those as baseline eligibility gates;
5. keep Hong Kong paused until the user explicitly reactivates it.

Optimize for:

**realistic interview probability × application throughput × technical plausibility × engineering environment × career portability**.

Applied AI / LLM / RAG / Agent / AI backend remains the preferred lane, but general backend, full-stack, software engineer, test-development/SDET/QA automation, Python/Java/PHP application engineering and adjacent early-career software roles are active lanes too.

**Company quality determines priority, not eligibility.** An ordinary credible employer may still produce a useful interview or offer.

Do not reject a role merely because:

- it is not Applied AI;
- the employer is not a famous/TOP company;
- the JD lists a learnable secondary stack as preferred/bonus;
- the role is generic SWE/backend/full-stack/test rather than AI-specific.

Do reject cheaply when a hard blocker is visible: closed/expired, duplicate/already applied, prohibited employment type, explicit work-auth blocker, incompatible cohort, hard mature-YOE floor, clearly mature ownership, or substantial mandatory technical/domain mismatch.

Do not restart portfolio work, strategy research, application-count experiments or another tracking system unless a concrete application or repeated employer feedback proves it is needed.

Any application, recruiter outreach or other employer-facing action requires explicit user authorization for that exact action or an unambiguous authorized batch such as `go all ACTION applications`.

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

### Singapore — active broad target

Search early-career roles across:

- Applied AI / Agent / RAG / AI backend / evaluation;
- backend / software engineering;
- full-stack / application engineering;
- test-development / SDET / QA automation;
- adjacent early-career engineering where hard requirements are realistically compatible.

Work authorization:

- employer-supported EP or S Pass is required;
- `UNKNOWN` sponsorship willingness is allowed at APPLY;
- explicit no-sponsorship / local-right-to-work-only wording is `BLOCKED`;
- MyCareersFuture is evidence-only for this candidate;
- **MCF-only route = blocked/closed** unless a separate verified non-MCF route exists.

Use FreeHire as broad radar when its intake is healthy/readable, plus direct employer/ATS and targeted LinkedIn/JobStreet/Indeed gaps.

### Mainland China — active broad target

Search 2026-compatible:

- Applied AI / Agent / RAG / LLM application roles;
- backend / software development;
- test-development / SDET;
- Python / Java / PHP and other realistically compatible application engineering;
- search/retrieval/data/platform work when the mandatory stack and ownership level are plausible.

Work authorization:

- employer-supported Mainland China foreign work permit is required;
- employer willingness may remain `UNKNOWN` until engagement;
- UNKNOWN alone does not block APPLY.

Use native sources first for coverage: BOSS, official/campus portals, 牛客, 51job, 智联, 猎聘. FreeHire and other feeds are supplementary radar.

### Malaysia — active broad target

Malaysia has no foreign-work-permit friction for this candidate.

Search broadly across Applied AI and general early-career engineering. Prefer TOP companies/teams and stronger Applied-AI roles first, but **TOP is not a gate**. Ordinary credible SWE/backend/full-stack/test/AI roles may reach APPLY when live, permanent and truthfully applicable.

Do not spend search time verifying Malaysian sponsorship.

### Hong Kong — paused

Hong Kong is **paused as of 2026-10-23**.

- Do not discover new HK roles.
- Do not create or promote new HK APPLY/ACTION items.
- Existing submitted `WAIT` items remain open so employer replies are not lost.
- If an existing HK employer replies, process that lifecycle event normally.
- Roles closed only because HK was paused may be reconsidered only after explicit reactivation and fresh validation.

### Web3 / crypto

Web3 is not a primary discovery lane. While the permanent-only rule is active, consider it only when the role is credible, permanent full-time and technically compatible.

---

## 4. Employment-type hard rule

For this search, **permanent full-time remains a hard outcome filter**, evaluated with a negative-evidence gate. Do not turn absence of the literal word `Permanent` into research debt.

Close/skip when current evidence positively indicates:

- fixed-term;
- temporary;
- contract;
- staffing/bodyshop/dispatch;
- project-only;
- internship;
- trainee/graduate programme without a credible regular permanent-employment path.

Classify employment evidence as:

- `CONFIRMED` — exact role/employer explicitly says permanent/regular indefinite employment;
- `PROBABLE` — normal full-time/social/campus regular hiring with no contradictory non-permanent signal;
- `CONFLICT` — credible current sources disagree;
- `BLOCKED` — current evidence establishes a prohibited non-permanent type.

`CONFIRMED` or `PROBABLE` may reach APPLY. `CONFLICT` may use CHECK only when it is the one remaining material blocker. `BLOCKED` closes/skips.

No fixed-term exception exists unless the user explicitly changes this policy.

---

## 5. Seniority and experience-shape rules

The candidate is early-career.

Default target:

- new graduate / 0–3 YOE;
- 1–3 YOE is normal target/stretch territory;
- reasonable 2–4 YOE roles may survive when hard requirements and actual ownership remain plausible.

Hard/near-hard negative signals:

- hard 4+/5+ professional-YOE floor without an explicit alternative qualification route the candidate truly satisfies;
- `Staff`, `Principal`, `Lead`, `Manager`, `Director`, `Head of` or clearly mature enterprise/platform/customer ownership;
- specialized professional-experience floors the candidate cannot truthfully satisfy.

A **Senior title alone is not an automatic terminal rule**. It is a review flag. Read the actual JD:

- if the role has a hard mature-YOE floor or mature ownership, skip;
- if the real requirements remain plausible for this candidate, it may survive as a stretch.

Mandatory `3+ years` is a meaningful negative signal, but generic software-engineering wording may truthfully use paid part-time/intern production work when the employer wording permits it. Do not reinterpret specialized floors such as `2+ years professional production GenAI` as generic software experience.

Never convert master's study, projects, internships or part-time work into fictitious conventional full-time professional YOE.

---

## 6. Every maintenance run

Before discovery:

1. read `README.md`, `PROFILE.md`, `RULES.md` and `DISCOVERY_STATE.md`;
2. fully inspect current `ACTION`, `APPLY` and `CHECK` Issues;
3. inspect `WAIT` only when recent, Gmail-triggered or needed for exact company/role-family dedupe;
4. check both Gmail accounts for recent state-changing recruiting evidence using a small overlap window;
5. update existing Issues before creating new opportunities.

State transitions:

- official application receipt or user-confirmed `applied` → `WAIT`;
- OA / interview / recruiter reply / useful requested action / real deadline → `ACTION`;
- explicitly authorized application that still awaits execution may remain `ACTION` until actual submission evidence exists;
- confirmed rejection / expired / exact duplicate / user `skip` / market paused / hard blocker → close;
- **do not close solely because a role is generic SWE/test/backend or because the employer is not TOP**;
- silence is not rejection;
- newer evidence overrides older evidence.

Keep title, status label, body and next action synchronized.

For an authorized application-type `ACTION`, the Issue body itself must say **`AUTHORIZED APPLICATION; submission pending`**, record the authorization scope/date when known, and state that the agent must not ask for `go` again for that exact role unless the role materially changes.

### Gmail reconciliation

Process direct employer/ATS/recruiter mail before job-alert/newsletter noise.

Prioritize application receipts, rejections/closed outcomes, OA/assessment, interview/recruiter contact, action-required deadlines and status updates. Read the actual message when metadata does not make the state change explicit.

A direct user statement that they already applied is valid application-history evidence even without an email receipt.

---

## 7. Discovery schedule and rotation

Scheduled MYT windows remain:

- `00:00-03:59` → `00`
- `04:00-07:59` → `04`
- `08:00-11:59` → `08`
- `12:00-15:59` → `12`
- `16:00-19:59` → `16`
- `20:00-23:59` → `20`

Explicit interactive searches may run at any time.

Before scheduled discovery, read `DISCOVERY_STATE.md`. If the current window already has a completed run satisfying the current contract and the receipt was written/read back successfully, do maintenance only and skip duplicate scheduled discovery.

Do not restart the whole market every run. Rotate source families and role lanes.

Operational cadence:

- **SG + CN remain high-frequency baseline lanes.**
- **MY is also active** and should receive a regular broad engineering pass, not TOP-only filtering.
- SG normal discovery = FreeHire broad radar plus targeted direct/ATS/platform gaps.
- If FreeHire fresh-head intake is materially unreadable/stale/blocked, use targeted LinkedIn/JobStreet/Indeed/direct-employer sweep and record degraded mode.
- CN normal discovery = native-source-first rotation plus supplementary feeds.
- HK remains out of discovery rotation while paused.

If a lane yields only duplicates/hard rejects, expand to another useful role/source cluster before concluding the market is sparse when practical.

### Discovery receipt

After a scheduled run, preserve any FreeHire cursor section and update only the rolling `Current receipt` with:

- completed run time in MYT;
- markets/source families/role lanes actually tried;
- compact coverage counters;
- serious-survivor Issue numbers created/updated, or `none`;
- concrete access/search failures;
- next rotation.

Counts are observability only, never quotas or scores. Do not put raw rejected candidates, long search logs or duplicated policy into `DISCOVERY_STATE.md`.

---

## 8. Discovery pipeline

Use:

`broad discovery → cheap hard filter → cheap GitHub dedupe → read actual JD → current liveness/eligibility → exact-ID Gmail dedupe → exact application route → Issue`

Raw discovery candidates do **not** become Issues.

### Stage 1 — active role families

Preferred first:

- Applied AI / AI Software Engineer;
- LLM Application / RAG / Agent engineering;
- AI Backend / Agent Backend;
- Agent/LLM Evaluation / AI Quality;
- Search / Retrieval / Context Engineering;
- AI-native Product Engineer / Backend Engineer;
- Coding Agent / Agent Harness.

Also active:

- general backend / software engineer;
- full-stack / application engineer;
- test-development / SDET / QA automation;
- Python / Java / PHP software roles;
- adjacent data/platform/infra roles when hard requirements are realistically compatible.

Do not routinely spend time on clearly unrelated specialist roles such as deep C++/CUDA/kernel, specialist networking/security, pure research scientist, or mature customer/solution-architecture ownership unless the actual JD provides a plausible route.

### Cheap hard filter

Reject cheaply only for material hard blockers such as:

- wrong/paused market;
- explicit non-permanent employment under Section 4;
- hard mature seniority/experience mismatch under Section 5;
- explicit incompatible graduation/cohort window;
- explicit citizenship / no-sponsorship / right-to-work-only blocker where relevant;
- substantial **mandatory** stack/domain mismatch;
- clearly closed/expired/unusable listing;
- exact duplicate/already applied.

Do **not** strengthen soft wording into hard requirements. `Preferred`, `plus`, `bonus`, `nice to have`, `familiarity`, `exposure`, coursework, self-study, personal projects and willingness to learn are non-hard unless the JD clearly says otherwise.

Do not reject at Stage 1 because the company is ordinary or the role is not AI.

At Stage 1, do not waste time on detailed salary/WLB, exact ATS routing, both Gmail accounts or deep sponsorship research for every raw lead.

---

## 9. Cheap dedupe before expensive research

Before Stage 2, check GitHub history in this order:

1. exact requisition/job ID;
2. same employer + same/near-identical role family;
3. explicit user-confirmed prior application history.

A same-employer role-family hit is a comparison flag, not an automatic duplicate.

Suppress when it is the exact prior application, demonstrably near-identical repost/team/scope, an employer application limit makes another submission inappropriate, or spraying would clearly damage a stronger active application.

A changed job ID alone is not enough to make an opportunity new. A same-company role may survive when team/scope/location/level is materially different.

---

## 10. Stage 2 — verify serious survivors

For plausible survivors verify:

1. exact/full JD and current role-level liveness;
2. employment classification under Section 4;
3. graduation/cohort, seniority and **hard** requirements;
4. realistic candidate fit;
5. work-authorization classification where relevant;
6. targeted Gmail dedupe in both accounts, using exact requisition/job ID first when available;
7. ATS/candidate history only when materially available;
8. exact usable application route.

Do not write a long company research essay before deciding whether a role is simply eligible to apply. Salary/WLB/company-depth research is optional unless decision-relevant.

A role does not need the literal word `Permanent` to reach APPLY. `PROBABLE` regular full-time employment is sufficient when no contradictory non-permanent evidence exists.

### Exact-ID invariant

Before creating/promoting any CHECK or APPLY with a requisition/job ID, search that exact ID in GitHub and both Gmail accounts.

Exact employer receipt or user-confirmed prior application → WAIT, not a new opportunity.

---

## 11. Work authorization classification

Use:

- `CONFIRMED` — current employer/role evidence supports the needed path;
- `PROBABLE` — meaningful employer evidence makes support credible but not confirmed for this exact candidate;
- `UNKNOWN` — no reliable yes/no evidence yet;
- `BLOCKED` — explicit no-sponsorship/right-to-work/citizenship constraint or another confirmed legal/employer blocker.

**UNKNOWN is allowed to reach APPLY. BLOCKED is not.**

Legal eligibility alone does not imply employer willingness, and lack of public sponsorship wording is not itself a CHECK blocker.

For SG/CN, employer realism is a prioritization signal, not a prerequisite for entering APPLY when no explicit blocker exists.

---

## 12. Freshness and current-liveness gate

Freshness is a ranking signal, not a 30-day death sentence.

Prefer newly posted/recently updated roles, but an older/undated role may survive when current application acceptance is proven.

Current liveness is required before a new Issue is created. Strong proof includes an active exact-role form/ATS action, an official current role page with active apply action, a current application window, or employer-controlled ATS status showing the requisition open/published.

Search snippets, mirrors, crawler timestamps and stale Apply buttons are discovery evidence only. Newer closed/expired evidence overrides older liveness evidence immediately.

---

## 13. Application-route hard gate

APPLY requires a current usable exact-role application route.

Valid proof includes:

1. exact candidate form renders and is usable;
2. employer-controlled ATS exact requisition exposes a real start/submit action;
3. platform-native exact-role application/contact flow is usable;
4. employer-controlled instruction to send the application/resume to an exact recruiting email address.

LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客, 猎聘 or similar platform-native routes may count when the exact-role action is usable.

If tooling prevents route verification, use CHECK only when liveness is independently proven and route verification is the one remaining blocker.

Fresh-check the exact route again immediately before acting on a user `go`.

---

## 14. When to create an Issue

Create an Issue only for a verified plausible survivor deserving user attention.

It must have:

- realistic early-career fit;
- active-market fit;
- no obvious cohort/seniority/mandatory-stack hard block;
- current role-level liveness proof;
- employment classification `CONFIRMED` or `PROBABLE`, or exactly one `CONFLICT` blocker on an otherwise useful role;
- no established duplicate;
- either a verified exact application route or exactly one material blocker remaining other than sponsorship/work-permit UNKNOWN.

**Do not require prestigious company quality or Applied-AI alignment merely to create APPLY.** Those decide ordering and recommendation strength.

Bad, closed, obvious-mismatch or raw candidates create nothing.

---

## 15. Issue states

Only four open states:

- `ACTION`
- `APPLY`
- `CHECK`
- `WAIT`

Meanings:

- `ACTION` = concrete recruiting action worth attention now/soon, including OA/interview/recruiter reply/deadline or an explicitly authorized application pending execution.
- `APPLY` = verified, live, realistically applicable role ready for user review with usable exact route. **APPLY is not submission permission.**
- `CHECK` = liveness proven; exactly one material blocker or user decision remains.
- `WAIT` = already submitted/contacted and waiting for employer activity.

Rejected, expired, duplicate, blocked, market-paused, hard-mismatch, withdrawn or user-skipped roles are closed.

### Labels and consistency

Every open opportunity must have exactly one market label and exactly one status label. Closed intentional outcomes may use `status:skipped` or `status:blocked`; MCF-only SG roles may also use `blocked:mcf`.

Whenever state changes, update title, labels, body and next action together. After close/relabel/reopen, read back the resulting state.

### APPLY / CHECK content

Store enough to decide without repeating research:

- exact role link/route or the one CHECK blocker;
- req/job ID and verification date when available;
- liveness evidence;
- employment classification/evidence;
- plain-language work;
- hard requirements / early-career fit;
- specific strengths/gaps;
- work-auth classification/evidence;
- targeted GitHub/Gmail dedupe result;
- same-company materially-different reason when applicable;
- exactly one next action.

Salary, WLB and deep company background are optional unless decision-relevant.

---

## 16. Authorization

APPLY means recommended for review, not permission to submit.

Only explicit authorization for that exact role/action permits an application or external contact.

A clearly scoped batch authorization such as `go all ACTION applications` permits all current application-type ACTION items in that batch, but does not authorize interview/OA actions or unrelated future roles.

`go` on one exact role does not authorize other roles at the same employer.

When authorization is granted but execution is not yet possible, keep the application in ACTION and synchronize the body to `AUTHORIZED APPLICATION; submission pending`; do not ask for authorization again for that exact unchanged role.

If the current chat lacks the ability to complete a website form, do not claim submission. Move to WAIT only after real submission/contact evidence exists.

---

## 17. Dedicated FreeHire lane

Routine FreeHire ingestion is owned by public `kolihhan/freehirefetch` plus the private `FreeHire Intake` scheduler.

- FreeHire contains public job data and machine-dedupe/health metadata only; never Gmail/application/private candidate state.
- FreeHire is **Stage 1 discovery evidence only**. Its enrichment/timestamps/classifications do not satisfy employer requirements, liveness or route gates.
- SG: FreeHire is the primary broad radar while fresh intake is healthy/readable; direct/ATS/platform searches fill gaps.
- CN: FreeHire is supplementary; native sources remain primary.
- MY: FreeHire is useful broad radar alongside direct/platform sources.
- If fresh intake cannot be read/screened because of connector/truncation/worker failure, use direct/platform substitute coverage and record degraded mode.
- Fresh-head inspection may look beyond the sequential cursor but must not move the cursor over unprocessed history.
- Cursor advances only through the largest contiguous processed prefix.
- A real cursor gap exists only when `cursor + 1 < health.first_seq`.
- Preserve the FreeHire cursor section when updating `DISCOVERY_STATE.md`.

---

## 18. Source-specific notes

### Singapore

Use FreeHire + direct employer/ATS + LinkedIn/JobStreet/Indeed gaps. Rotate broad lanes: Applied AI, backend/SWE, full-stack, QA/SDET/test automation and adjacent plausible engineering.

### Mainland China

Rotate BOSS → official/campus → 牛客 → 51job → 智联 → 猎聘, with feeds supplementary. Rotate both AI and general software/backend/test-development keywords. Do not let CN discovery collapse because one source is hard to inspect.

### Hong Kong

Paused. Do not run HK discovery until explicitly reactivated.

### Malaysia

Use official careers, LinkedIn, JobStreet/Hiredly, direct employers and broad radar. Prefer strong companies/teams first but do not apply a TOP-only gate.

### Telegram / DeJob

Discovery source only, never authoritative proof. Independently verify company, exact role/JD, liveness, requirements, dedupe and route before Issue creation.

---

## 19. GitHub write safety

Verify material GitHub writes by reading them back.

If Gmail/GitHub access or a required write fails, report the exact incomplete step rather than claiming success.

For create operations where a timeout/connection error/transient 5xx could hide a successful side effect:

1. do not immediately retry;
2. search/read back using exact req + employer/role fingerprint;
3. adopt the Issue if it already exists;
4. if still absent, retry once;
5. read back again;
6. persistent ambiguity stops the write loop.

---

## 20. Privacy and keep-it-small rule

Store only operational facts. Do not copy credentials, authentication material or unnecessary personal identifiers into Issues.

Do not add Projects, another database/dashboard/frontend/spreadsheet, score file, knowledge graph or new application framework unless repeated real failures prove the current GitHub-Issues model inadequate.
