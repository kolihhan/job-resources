# Operating Rules

## 1. Goal and priority

Get interviews and offers for a strong **permanent full-time** engineering role without turning the search into another software project.

Priority order:

1. advance active employer responses, OA, interviews, recruiter conversations and real deadlines;
2. reconcile GitHub/Gmail lifecycle state before discovering more jobs;
3. create strong **Singapore + Mainland China** opportunities;
4. run **Malaysia TOP-only** in parallel;
5. keep Hong Kong paused until the user explicitly reactivates it.

For the main search, optimize for:

**realistic interview probability × Applied-AI fit × engineering environment × company/team quality × career portability**.

Primary technical direction:

- Applied AI / AI Application Engineer;
- LLM / RAG / Agent engineering;
- AI Backend / AI Software Engineer;
- LLM / Agent evaluation and AI quality engineering;
- Search / Retrieval / RAG engineering;
- AI-native product/backend roles where LLM/Agent work is a real part of the job.

Default deprioritize/skip:

- pure computer vision / robotics / image-model roles;
- traditional ML without meaningful LLM/application overlap;
- generic MLOps;
- model-serving / inference / GPU / distributed AI infrastructure;
- deep platform / middleware / distributed-systems ownership;
- mature FDE / solution-architecture / customer-deployment ownership;
- generic SWE that would require a separate interview-prep track and does not compound the Applied-AI direction.

A strong company name alone does not override role-direction mismatch.

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

### Singapore — active target

Search strong early-career roles centered on:

- Applied AI / Agent / RAG;
- AI backend / AI-native product engineering;
- LLM/Agent evaluation;
- search/retrieval when tied to LLM/RAG;
- strong backend/SWE only when it clearly reinforces the same direction.

Work authorization:

- employer-supported EP or S Pass;
- `UNKNOWN` sponsorship willingness is allowed at APPLY;
- explicit no-sponsorship / local-right-to-work-only wording is `BLOCKED`;
- MyCareersFuture is evidence-only for this candidate;
- **MCF-only route = blocked/closed** unless a separate verified non-MCF route exists.

Use FreeHire as broad radar, but normal discovery should focus on direct employer/ATS and targeted coverage gaps rather than recreating a broad scrape.

### Mainland China — active target

Search:

- AI-native product companies and developer tools;
- Agent/RAG/LLM application engineering;
- AI backend;
- evaluation / AI quality;
- search/retrieval / context engineering;
- strong enterprise AI application teams.

Work authorization:

- employer-supported Mainland China foreign work permit;
- willingness may remain `UNKNOWN` until engagement;
- UNKNOWN alone does not block APPLY.

Seniority/cohort:

- favor `2026届`, recent graduate and 0–3 YOE;
- selective 2–4 YOE stretches survive only when actual scope is still early-career realistic and fit is unusually strong;
- clearly 2027-only roles are filtered unless official wording explicitly includes this 2026 graduate or an applicable overseas-graduate window.

Use native sources first: BOSS, official/campus portals, 牛客, 51job, 智联, 猎聘.

### Hong Kong — paused

Hong Kong is **paused as of 2026-10-23**.

- Do not discover new HK roles.
- Do not create or promote new HK APPLY/ACTION items.
- Existing submitted `WAIT` items remain open so employer replies are not lost.
- If an existing HK employer replies, process the lifecycle event normally.
- Roles closed only because HK was paused may be reconsidered only after the user explicitly reactivates HK, followed by fresh liveness/route verification.

### Malaysia — TOP-only parallel lane

- Malaysian candidate; do not spend search time on sponsorship verification.
- **TOP is role-level, not logo-level.**
- Prefer strong Applied AI / Agent / RAG / evaluation / AI backend roles with credible engineering depth, compensation/WLB/growth when knowable, mentorship and career portability.
- Strong general SWE/backend may survive only when the employer/team is genuinely TOP and the role offers excellent engineering growth without pulling the candidate into an unrelated direction.
- A famous bank, GLC, consultancy or MNC name alone does not make a role TOP.
- Generic operations, low-depth IT support, bodyshop/outsourcing, weak consulting implementation, generic traditional ML or ordinary fallback roles should not crowd the queue.

### Web3 / crypto

Web3 is not a primary discovery lane. While the permanent-only rule is active, only consider credible **permanent full-time** roles that are technically strong and useful for the same backend/AI engineering direction.

Do not create a separate contract/part-time/project lane.

---

## 4. Employment-type hard rule

For this search, **permanent full-time is a hard filter**.

Close/skip:

- fixed-term;
- temporary;
- contract;
- staffing/bodyshop;
- project-only;
- internship;
- trainee/graduate programme when permanent employment is not established.

Do not infer permanence from `full-time` alone. If the employment type is materially ambiguous and permanence cannot be established, use `CHECK` only when this is the one remaining blocker and the opportunity is otherwise unusually strong; otherwise skip.

No fixed-term exception should be created unless the user explicitly changes this policy.

---

## 5. Seniority and experience-shape rules

The candidate is early-career.

Default target:

- new graduate / 0–3 YOE;
- 1–3 YOE is normal stretch territory when the role is relevant;
- 2–4 YOE only when fit/company are unusually strong and scope is still realistic.

Skip by default:

- Senior / Staff / Lead / Manager;
- hard 4+/5+ professional-YOE roles without an explicit alternative qualification route;
- roles whose actual responsibilities clearly assume mature enterprise/platform/customer ownership even when numeric YOE is weak or absent.

Experience wording must be interpreted literally and honestly:

- generic software-engineering experience can use truthful paid part-time/intern production work when the employer wording permits it;
- academic research/projects may count only when the employer explicitly allows them or asks for practical/project experience;
- specialized floors such as `2+ years professional AI application/service development`, `2+ years FDE`, or `3+ years production GenAI` cannot be satisfied by unrelated software work plus academic AI projects.

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
- confirmed rejection / expired / duplicate / user `skip` / market paused / direction mismatch → close;
- silence is not rejection;
- newer evidence overrides older evidence.

Keep title, status label, body and next action synchronized.

### Gmail reconciliation

Process direct employer/ATS/recruiter mail before job-alert/newsletter noise.

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

Do not restart the whole market every run. Rotate employer clusters, source families and role keywords.

Operational cadence:

- **SG + CN remain high-frequency baseline lanes.**
- SG normal discovery = targeted gap search, because FreeHire owns broad SG radar.
- CN normal discovery = native-source-first rotation.
- **MY TOP** is a smaller active parallel rotation.
- **HK is out of discovery rotation while paused.**
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

Counts are observability only, never quotas or scores.

Do not put raw rejected candidates, long search logs or duplicated policy into `DISCOVERY_STATE.md`.

---

## 8. Discovery pipeline

Use:

`broad discovery → cheap hard filter → cheap GitHub dedupe → current liveness/eligibility → direction/seniority/work-auth classification → exact-ID Gmail dedupe → exact application route → Issue`

Raw discovery candidates do **not** become Issues.

### Stage 1 — target role families

Primary search families:

- Applied AI / AI Software Engineer;
- LLM Application / RAG / Agent engineering;
- AI Backend / Agent Backend;
- Agent/LLM Evaluation / AI Quality;
- Search / Retrieval / Context Engineering tied to LLM/RAG;
- AI-native Product Engineer / Backend Engineer;
- Coding Agent / Agent Harness roles when application/backend oriented.

Secondary only when clearly useful:

- general backend/SWE at high-quality AI-native teams;
- application-oriented AI platform work where Agent/RAG/evaluation remains central.

Do not routinely search pure CV/robotics, traditional ML, generic MLOps, model serving, inference, GPU systems, deep distributed infra or generic platform engineering.

Rotate employer clusters such as AI-native startups, fintech, enterprise software, developer tools, B2B SaaS, consumer AI product and selected healthtech/industrial teams where the actual role remains Applied-AI oriented.

### Cheap hard filter

Reject cheaply for:

- wrong market/location for the lane;
- paused HK market;
- non-permanent employment type;
- seniority/experience mismatch under Section 5;
- explicit incompatible graduation/cohort window;
- explicit citizenship / no-sponsorship / right-to-work-only blocker where relevant;
- substantial mandatory stack/domain mismatch;
- role-direction mismatch under the current profile;
- clearly closed/expired/unusable listing.

Do **not** strengthen soft wording into hard requirements. `Preferred`, `plus`, `bonus`, `nice to have`, `familiarity`, `exposure`, coursework, self-study, personal projects and willingness to learn are non-hard unless the JD clearly says otherwise.

At Stage 1, do not waste time on detailed salary/WLB, exact ATS routing, both Gmail accounts or deep sponsorship research for every raw lead.

---

## 9. Cheap dedupe before expensive research

Before Stage 2, check GitHub history in this order:

1. exact requisition/job ID;
2. same employer + same/near-identical role family;
3. explicit user-confirmed prior application history.

A same-employer role-family hit is a comparison flag, not an automatic duplicate.

Suppress when:

- it is the exact prior application;
- it is a demonstrably near-identical team/scope/repost;
- an employer's documented application limit makes another submission inappropriate;
- another live role at the same employer is materially stronger and spraying would reduce application quality.

A changed job ID alone is **not** enough to make an opportunity new.

A same-company role may survive when the team/scope/location/level is materially different or the opportunity is clearly stronger. If promoted, the Issue must say why another application is worth pursuing.

---

## 10. Stage 2 — verify serious survivors

For serious survivors verify:

1. exact/full JD and current role-level liveness;
2. permanent employment type;
3. graduation/cohort, seniority and hard requirements;
4. technical-direction fit;
5. candidate fit and work-authorization classification;
6. targeted Gmail dedupe in both accounts, using exact requisition/job ID first when available;
7. ATS/candidate history only when materially available;
8. exact usable application route.

### Exact-ID invariant

Before creating/promoting any `CHECK` or `APPLY` with a requisition/job ID, search that exact ID in:

- GitHub;
- `lihhanko526@gmail.com`;
- `lihhanko3@gmail.com`.

Exact employer receipt or user-confirmed prior application → `WAIT`, not a new opportunity.

---

## 11. Work authorization classification

Use:

- `CONFIRMED` — current employer/role evidence supports the needed path;
- `PROBABLE` — meaningful employer evidence makes support credible but not confirmed for this exact candidate;
- `UNKNOWN` — no reliable yes/no evidence yet;
- `BLOCKED` — explicit no-sponsorship/right-to-work/citizenship constraint or another confirmed legal/employer blocker.

**UNKNOWN is allowed to reach APPLY. BLOCKED is not.**

Legal eligibility alone does not imply employer willingness, and lack of public sponsorship wording is not by itself a CHECK blocker.

For SG/CN, employer realism is a prioritization signal: explicit support, prior foreign hiring, graduate/0–3 YOE hiring, mature HR, international operations and pass/work-permit-compatible compensation when known are positive evidence. Company size alone is weak evidence.

HK work-auth research is unnecessary while HK is paused unless an existing WAIT employer actively re-engages.

---

## 12. Freshness and current-liveness gate

Freshness is a **ranking signal, not a 30-day death sentence**.

- Prefer newly posted/recently updated exact roles, especially <=30 days.
- A >30-day or undated exact role may still reach `CHECK`/`APPLY` when it is currently accepting applications, the candidate is currently eligible and the opportunity is strong enough.
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

## 13. Application-route hard gate

`APPLY` requires a current usable exact-role application route.

Valid final-route proof includes:

1. exact candidate form renders and is usable;
2. employer-controlled ATS exact requisition exposes a real start/submit action with no unresolved redirect;
3. platform-native exact-role application/contact flow is directly usable with no unresolved external redirect;
4. employer-controlled instruction to send the application/resume to an exact recruiting email address.

Platform-native LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客, 猎聘 or similar may count when the exact-role action is usable.

If login/JavaScript/cookies/bot protection/tool limits prevent route verification, use `CHECK` only when liveness is independently proven and route verification is the **one** remaining blocker.

Removed/expired/ambiguous final destination → blocked/closed as appropriate.

Before presenting an APPLY as ready, and again immediately before acting on a user `go`, fresh-check the exact application route.

---

## 14. When to create an Issue

Create an Issue only for a serious survivor deserving user attention.

It must have:

- plausible early-career fit;
- current target-market fit;
- current technical-direction fit;
- no obvious cohort/seniority hard block;
- credible role/company/team quality;
- current role-level liveness proof;
- permanent full-time employment established or exactly one material permanence blocker on an otherwise exceptional role;
- no established duplicate under the dedupe model;
- either a verified exact application route or exactly one material blocker remaining other than sponsorship/work-permit UNKNOWN.

Bad, closed, obvious-mismatch or raw candidates create nothing.

---

## 15. Issue states

Only four open states:

- `ACTION`
- `APPLY`
- `CHECK`
- `WAIT`

Meanings:

- `ACTION` = concrete recruiting action worth attention now/soon: OA, interview, recruiter reply, useful requested form/document or real deadline. It may also temporarily hold an explicitly authorized application pending execution.
- `APPLY` = verified serious survivor ready for user review with usable exact route. Work auth may be CONFIRMED/PROBABLE/UNKNOWN. **APPLY is not submission permission.**
- `CHECK` = liveness proven; exactly one material blocker or user decision remains, with exactly one next action. Unknown sponsorship alone is not a CHECK blocker.
- `WAIT` = already submitted/contacted and waiting for employer activity; do not duplicate.

Rejected, expired, duplicate, blocked, market-paused, direction-mismatch, withdrawn or user-skipped roles are closed.

### Labels and consistency

Every open opportunity must have:

- exactly one market label: `market:sg`, `market:cn`, `market:hk`, or `market:my`;
- exactly one matching status label: `status:action`, `status:apply`, `status:check`, or `status:wait`.

`market:hk` may remain on historical HK WAIT items while discovery is paused.

Closed intentional outcomes may use `status:skipped` or `status:blocked`; MCF-only SG roles may also use `blocked:mcf`.

Whenever state changes, update title, labels, body and next action together.

Maintenance invariants:

- no closed Issue keeps an open status label/title;
- SG MCF-only route → blocked/closed unless a separate current non-MCF route exists;
- user `skip` / `no` / `don't want` → terminal skipped state;
- confirmed unusable route → terminal blocked state;
- exact prior application found → WAIT;
- unsubmitted HK APPLY/ACTION/CHECK → close while HK is paused;
- existing HK WAIT remains open until employer outcome or user explicitly asks to withdraw/ignore it;
- an HK role previously closed only because HK was paused may be reconsidered only after explicit HK reactivation and fresh validation;
- after close/relabel/reopen, read back title, labels, body/outcome and state.

### APPLY / CHECK content

Store enough to decide without repeating research:

- exact role link/route or the one CHECK blocker;
- req/job ID and verification date when available;
- liveness/age evidence where useful;
- permanent employment evidence;
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

## 16. Authorization

`APPLY` means recommended for review, not permission to submit.

Only explicit authorization for that exact role/action permits an application or external contact.

A clearly scoped batch authorization such as `go all ACTION applications` permits all current **application-type** ACTION items in that batch, but does not authorize interview/OA actions or unrelated future roles.

`go` on one exact role does not authorize other roles at the same employer.

If the current chat lacks the ability to complete a website form, do not claim submission. Record authorization and the exact execution blocker; move to WAIT only after real submission/contact evidence exists.

---

## 17. Dedicated FreeHire lane

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

## 18. Source-specific notes

### Singapore

Use FreeHire-first + direct-employer/ATS gap search. LinkedIn/JobStreet/Indeed are targeted gap tools rather than a routine duplicate broad sweep.

Primary keywords/lanes: Applied AI, AI Engineer, AI Software Engineer, Agent, RAG, LLM application, evaluation, retrieval/search, AI backend, AI-native product engineering.

### Mainland China

Rotate BOSS → official/campus → 牛客 → 51job → 智联 → 猎聘, with LinkedIn/other feeds supplementary.

Primary keywords/lanes: AI应用, 大模型应用, Agent, RAG, 检索, 上下文工程, 评测, AI后端, Coding Agent, Agent Harness.

Do not let CN discovery collapse simply because sources are harder to inspect; change source/employer/keyword lanes before declaring it sparse.

### Hong Kong

Paused. Do not run HK discovery until explicitly reactivated.

### Malaysia

Prefer official careers, LinkedIn, JobStreet/Hiredly and direct employers. Apply the `PROFILE.md` TOP + AI-first filter before deep verification so ordinary fallback roles do not fill the live queue.

### Telegram / DeJob

Discovery source only, never authoritative proof. For a survivor first found there:

- add `[TG]` after the market tag in the title;
- record source + public source link;
- independently verify company, exact role/JD, liveness, requirements, dedupe and route;
- anonymous/recruiter-only/unclear-company leads do not reach GitHub unless independently verified.

---

## 19. GitHub write safety

Verify material GitHub writes by reading them back.

If Gmail/GitHub access or a required write fails, report the exact incomplete step rather than claiming success.

For create operations where a timeout/connection error/transient 5xx could hide a successful side effect:

1. do not immediately retry;
2. search/read back recent Issues using exact req + employer/role fingerprint;
3. adopt the Issue if it already exists;
4. if still absent, retry once;
5. read back again;
6. persistent ambiguity stops the write loop.

---

## 20. Privacy and keep-it-small rule

Store only operational facts. Do not copy credentials, authentication material or unnecessary personal identifiers into Issues.

Do not add Projects, another database/dashboard/frontend/spreadsheet, score file, custom scraper, knowledge graph or new application framework unless repeated real failures prove the current GitHub-Issues model inadequate.
