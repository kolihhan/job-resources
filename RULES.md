# Operating Rules

## 1. Goal and priority

Get interviews and offers for a **permanent full-time AI-related role** without turning the search itself into another software project.

Current execution mode is **high-throughput AI-career search** across Singapore, Mainland China and Malaysia.

Priority order:

1. advance active employer responses, OA, interviews, recruiter conversations and real deadlines;
2. reconcile GitHub/Gmail lifecycle state before discovering more jobs;
3. find and verify realistically applicable **AI/ML-related** roles across SG + CN + MY;
4. prioritize stronger companies/teams and low-friction routes when role fit is otherwise comparable;
5. keep Hong Kong paused until explicitly reactivated.

Optimize for:

**realistic interview probability × AI-career relevance × application throughput × technical plausibility × engineering/research environment × career portability**.

Active target families include:

- Applied AI / AI Application / Generative AI;
- LLM / RAG / Agent / Coding Agent / Agent Harness;
- AI Backend / AI Software Engineer / AI-native Product Engineer;
- ML Engineer / NLP / Search / Retrieval / Ranking where work is materially AI/ML;
- Agent/LLM evaluation / AI quality / AI testing where AI systems are the actual object of the work;
- **Research Engineer / AI Researcher / Applied Scientist / Research Scientist** when hard requirements are realistic;
- data science when the core work is materially ML/AI rather than generic BI/analytics.

A generic title such as Software Engineer, Backend Engineer, Full-stack Engineer or QA/SDET may survive **only when the actual team/product/JD is materially AI-related**. Pure generic software work is not a target merely because the candidate could perform it.

Research is explicitly allowed. Do not reject a role merely because it is research-oriented. Read the actual requirements: MSc-compatible research/research-engineering roles are active; hard PhD/publication/independent-research requirements the candidate does not satisfy remain blockers.

Company quality determines priority, not eligibility. A smaller credible AI company/research team with meaningful AI work may be preferable to a famous employer offering unrelated generic software work.

Any application, recruiter outreach or other employer-facing action requires explicit user authorization for that exact action or an unambiguous authorized batch.

---

## 2. Source of truth

- GitHub Issues = live operational opportunity state.
- Gmail = receipts, recruiter messages, OA/interviews, deadlines, rejections and targeted dedupe evidence.
- `PROFILE.md` = stable candidate facts and current market/role scope.
- `RULES.md` = detailed execution policy.
- `DISCOVERY_STATE.md` = one rolling discovery receipt/cursor + next rotation only.
- Old spreadsheet = legacy/read-only.

Scheduler prompts and `NEXT_CHAT_PROMPT.md` must point back to these files rather than copying policy.

Do not create another dashboard, database, spreadsheet mirror, scoring engine, scraper framework, knowledge graph or agent framework.

---

## 3. Current market contract

### Singapore — active AI target

Search early-career roles across:

- Applied AI / GenAI / LLM / Agent / RAG;
- AI software/backend/product engineering;
- ML/NLP/search/retrieval/evaluation;
- Research Engineer / Applied Scientist / realistic AI research roles.

Generic SWE/backend/full-stack/test titles may survive only when the actual JD/team/product is materially AI-related.

Work authorization:

- employer-supported EP or S Pass is required;
- `UNKNOWN` sponsorship willingness is allowed at APPLY;
- explicit no-sponsorship / local-right-to-work-only wording is `BLOCKED`;
- MCF-only route = blocked/closed unless a separate verified non-MCF route exists.

Use FreeHire as broad raw radar because AI jobs may use generic engineering titles, but promotion requires actual JD/team/product AI relevance. Fill gaps with direct employer/ATS + targeted LinkedIn/JobStreet/Indeed.

### Mainland China — active AI target

Search 2026-compatible:

- AI应用 / 大模型应用 / Agent / RAG;
- AI后端 / AI软件开发;
- 算法 / ML / NLP / 检索 / 推荐 / 评测;
- Research Engineer / AI研究 / 应用研究 when requirements are realistic.

Pure generic backend/software/test roles are not target opportunities unless the actual team/product/JD is materially AI-related.

Work authorization:

- employer-supported Mainland China foreign work permit is required;
- employer willingness may remain `UNKNOWN` until engagement;
- UNKNOWN alone does not block APPLY.

Use native sources first for coverage: BOSS, official/campus portals, 牛客, 51job, 智联, 猎聘. FreeHire/other feeds are supplementary radar.

### Malaysia — active AI target

Malaysia has no foreign-work-permit friction for this candidate.

Search AI/ML/GenAI/LLM/Agent/AI software/evaluation and realistic AI-research/research-engineering roles. Strong companies/teams are preferred, but meaningful AI work is the direction gate.

Do not spend search time verifying Malaysian sponsorship.

### Hong Kong — paused

Hong Kong remains paused as of 2026-10-23. Do not discover new HK roles. Existing submitted WAIT items remain so employer replies are not lost.

### Web3 / crypto

Not a primary lane. Consider only when permanent full-time, credible, and the actual role is materially AI/ML-related.

---

## 4. Employment-type hard rule

For this search, **permanent full-time remains a hard outcome filter**.

Close/skip when current evidence positively indicates fixed-term, temporary, contract, staffing/bodyshop/dispatch, project-only, internship, or trainee/graduate programme without a credible regular permanent-employment path.

Employment evidence:

- `CONFIRMED` — exact role/employer explicitly says permanent/regular indefinite employment;
- `PROBABLE` — normal full-time/social/campus regular hiring with no contradictory non-permanent signal;
- `CONFLICT` — credible current sources disagree;
- `BLOCKED` — current evidence establishes a prohibited non-permanent type.

CONFIRMED or PROBABLE may reach APPLY. CONFLICT may use CHECK only when it is the one remaining material blocker. BLOCKED closes/skips.

---

## 5. Seniority, research and experience-shape rules

The candidate is early-career.

Default target:

- new graduate / 0–3 YOE;
- 1–3 YOE is normal target/stretch territory;
- reasonable 2–4 YOE may survive when hard requirements and actual ownership remain plausible.

Hard/near-hard negatives:

- hard 4+/5+ professional-YOE floor without a real alternative route;
- Staff / Principal / Lead / Manager / Director / Head of or clearly mature ownership;
- specialized professional-experience floor the candidate cannot truthfully satisfy;
- research role with hard PhD requirement the candidate does not meet;
- hard publication-record / independent-research / postdoc requirement not met.

A Senior title alone is a review flag, not automatic rejection. Read the JD.

Mandatory `3+ years` is a meaningful negative signal, but generic software-engineering wording may truthfully use paid part-time/intern production work when employer wording permits it. Do not reinterpret specialized floors such as `2+ years professional production GenAI` as generic software experience.

For research roles, MSc thesis/research can truthfully support research-experience claims, but do not invent publications, PhD-level depth, or conventional full-time research YOE.

Never convert master's study, projects, internships or part-time work into fictitious conventional full-time professional YOE.

---

## 6. Every maintenance run

Before discovery:

1. read README / PROFILE / RULES / DISCOVERY_STATE;
2. fully inspect current ACTION / APPLY / CHECK;
3. inspect WAIT only when recent, Gmail-triggered or needed for dedupe;
4. check both Gmail accounts for recent state-changing recruiting evidence;
5. update existing Issues before creating new opportunities.

State transitions:

- official application receipt or user-confirmed `applied` → WAIT;
- OA / interview / recruiter reply / useful requested action / deadline → ACTION;
- explicitly authorized application awaiting execution may remain ACTION until real submission evidence exists;
- confirmed rejection / expired / duplicate / user skip / paused market / hard blocker / clear AI-direction mismatch → close;
- silence is not rejection;
- newer evidence overrides older evidence.

**Pure generic SWE/test/backend is now a valid direction-mismatch reason unless the actual JD/team/product is materially AI-related.**

Keep title, status label, body and next action synchronized.

For an authorized application-type ACTION, the Issue body must say `AUTHORIZED APPLICATION; submission pending`; do not ask for authorization again for that exact unchanged role.

---

## 7. Discovery schedule and rotation

Scheduled MYT windows remain 00 / 04 / 08 / 12 / 16 / 20.

Before scheduled discovery, read DISCOVERY_STATE. If the current window already has a completed run satisfying the current contract, do maintenance only and skip duplicate discovery.

Operational cadence:

- SG + CN remain high-frequency baseline lanes;
- MY remains active;
- SG = FreeHire raw radar + targeted direct/ATS/platform AI gaps;
- CN = native-source-first AI rotation + supplementary feeds;
- MY = AI/ML/GenAI/research roles via official careers, LinkedIn, JobStreet/Hiredly and direct employers;
- HK remains out of discovery rotation.

Rotate role families, not just sources: Applied AI, LLM/Agent/RAG, AI backend/software, ML/NLP/search/retrieval, evaluation, and research/research-engineering.

If a lane yields only duplicates/hard rejects, expand to another **AI-related** role/source cluster before concluding the market is sparse.

After a scheduled run, preserve any FreeHire cursor section and update one compact current receipt with time, markets/sources/role lanes, serious survivors, failures and next rotation.

---

## 8. Discovery pipeline

Use:

`broad raw discovery → cheap hard filter → read actual JD/team/product → AI-relevance gate → cheap GitHub dedupe → liveness/eligibility → exact-ID Gmail dedupe → exact route → Issue`

Raw discovery candidates do **not** become Issues.

### Stage 1 — active role families

Active:

- Applied AI / AI Software Engineer / GenAI Engineer;
- LLM Application / RAG / Agent engineering;
- AI Backend / Agent Backend;
- Agent/LLM Evaluation / AI Quality / AI testing;
- Search / Retrieval / Context Engineering;
- ML Engineer / NLP / recommendation/ranking when genuinely ML-oriented;
- AI-native Product Engineer / Backend Engineer;
- Coding Agent / Agent Harness;
- Research Engineer / AI Researcher / Applied Scientist / Research Scientist when requirements are realistic;
- AI/ML-heavy Data Scientist.

Generic-title roles are only active when the actual JD/team/product shows material AI/ML work.

Not routine targets:

- pure generic backend/SWE/full-stack with no AI work;
- ordinary QA/SDET/test automation unrelated to AI systems;
- generic DevOps/SRE/security/networking;
- BI/reporting analytics;
- unrelated specialist systems roles;
- research positions with clearly unmet hard PhD/publication requirements.

### Cheap hard filter

Reject cheaply for material hard blockers such as:

- wrong/paused market;
- explicit non-permanent employment;
- hard mature seniority/experience mismatch;
- incompatible graduation/cohort window;
- explicit citizenship/no-sponsorship/right-to-work blocker where relevant;
- clearly unmet hard PhD/publication/research requirement;
- substantial mandatory stack/domain mismatch;
- clearly closed/expired listing;
- exact duplicate/already applied.

Do not strengthen `preferred`, `plus`, `bonus`, `nice to have`, `familiarity`, `exposure`, coursework, self-study or personal-project wording into hard requirements.

Do not reject because company is ordinary. **Do reject when the work itself is not materially AI-related.**

---

## 9. Cheap dedupe before expensive research

Before Stage 2, check GitHub history in this order:

1. exact requisition/job ID;
2. same employer + same/near-identical role family;
3. explicit user-confirmed prior application history.

A same-employer role-family hit is a comparison flag, not automatic duplicate. Suppress exact or demonstrably near-identical repeats, or when spraying would clearly damage a stronger active application.

---

## 10. Stage 2 — verify serious survivors

For plausible survivors verify:

1. exact/full JD and current role-level liveness;
2. material AI/ML/research relevance;
3. employment classification;
4. cohort, seniority and hard requirements;
5. realistic candidate fit;
6. work authorization where relevant;
7. targeted Gmail dedupe in both accounts using exact requisition/job ID first;
8. exact usable application route.

A role does not need the literal word Permanent to reach APPLY. PROBABLE regular full-time employment is sufficient when no contradictory non-permanent evidence exists.

Before creating/promoting CHECK or APPLY with a requisition/job ID, search that exact ID in GitHub and both Gmail accounts. Exact prior application → WAIT.

---

## 11. Work authorization classification

Use CONFIRMED / PROBABLE / UNKNOWN / BLOCKED.

UNKNOWN is allowed to reach APPLY. BLOCKED is not. Lack of public sponsorship wording alone is not a CHECK blocker.

---

## 12. Freshness and current-liveness gate

Freshness is a ranking signal, not a 30-day death sentence.

Current liveness is required before a new Issue is created. Strong proof includes an active exact-role form/ATS action, official current role page with active apply action, current application window, or employer-controlled ATS status showing the requisition open/published.

Search snippets, mirrors and crawler timestamps are discovery evidence only. Newer closed/expired evidence overrides older liveness evidence.

---

## 13. Application-route hard gate

APPLY requires a current usable exact-role route: exact candidate form, employer ATS requisition, usable platform-native flow, or employer-controlled recruiting email instruction.

LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客, 猎聘 or similar may count when exact-role action is usable.

If tooling prevents route verification, use CHECK only when liveness is independently proven and route verification is the one remaining blocker.

Fresh-check route immediately before acting on a user `go`.

---

## 14. When to create an Issue

Create an Issue only for a verified serious survivor that deserves user attention.

It must have:

- material AI/ML/research relevance;
- realistic early-career fit;
- active-market fit;
- no obvious cohort/seniority/hard-requirement block;
- current role-level liveness proof;
- employment CONFIRMED or PROBABLE, or exactly one CONFLICT blocker on an otherwise strong role;
- no established duplicate;
- either a verified exact route or exactly one material blocker remaining other than sponsorship/work-permit UNKNOWN.

Company prestige is not required. **AI relevance is.**

Bad, closed, generic-non-AI, obvious-mismatch or raw candidates create nothing.

---

## 15. Issue states

Only four open states: ACTION / APPLY / CHECK / WAIT.

- ACTION = concrete recruiting action now/soon, including OA/interview/recruiter reply/deadline or authorized application pending execution.
- APPLY = verified, live, materially AI-related role ready for user review. APPLY is not submission permission.
- CHECK = liveness proven; exactly one material blocker or user decision remains.
- WAIT = already submitted/contacted and waiting.

Rejected, expired, duplicate, blocked, market-paused, AI-direction-mismatch, withdrawn or user-skipped roles are closed.

Every open opportunity must have exactly one market label and exactly one status label. Whenever state changes, update title, labels, body and next action together and read back the result.

APPLY/CHECK should store exact route/blocker, req ID, liveness, employment evidence, plain-language work, hard requirements, AI relevance, strengths/gaps, work auth, dedupe result and exactly one next action.

---

## 16. Authorization

APPLY means recommended for review, not permission to submit.

Only explicit authorization for that exact role/action permits an application or external contact. `go` on one exact role does not authorize other roles at the same employer.

When authorization is granted but execution is not yet possible, keep it in ACTION and mark `AUTHORIZED APPLICATION; submission pending`. Move to WAIT only after real submission/contact evidence exists.

---

## 17. Dedicated FreeHire lane

Routine FreeHire ingestion is owned by public `kolihhan/freehirefetch` plus the private FreeHire Intake scheduler.

- FreeHire contains public job data and machine-dedupe/health metadata only.
- FreeHire is Stage 1 discovery evidence only.
- Its raw search may remain broader than the final AI target because many AI companies use generic SWE/backend titles.
- **Raw FreeHire category inclusion does not imply queue eligibility.** JD/team/product AI relevance must be checked before Issue creation.
- SG: FreeHire is primary broad raw radar while healthy/readable; direct/ATS/platform searches fill AI-specific gaps.
- CN: FreeHire is supplementary; native sources remain primary.
- MY: FreeHire is supplementary broad radar alongside direct/platform AI searches.
- Preserve the FreeHire cursor section when updating DISCOVERY_STATE.

---

## 18. Source-specific notes

### Singapore

Use FreeHire + direct employer/ATS + LinkedIn/JobStreet/Indeed gaps. Rotate Applied AI, LLM/Agent/RAG, AI software/backend, ML/NLP/search/retrieval/evaluation and research-engineering lanes.

### Mainland China

Rotate BOSS → official/campus → 牛客 → 51job → 智联 → 猎聘. Search AI应用、大模型、Agent、RAG、AI后端、算法/ML/NLP、检索/推荐/评测 and AI research/research-engineering. Do not let CN discovery collapse because one source is hard to inspect.

### Hong Kong

Paused.

### Malaysia

Use official careers, LinkedIn, JobStreet/Hiredly and direct employers for AI/ML/GenAI/LLM/Agent/AI software/evaluation/research roles. Strong companies are preferred but not required.

### Telegram / DeJob

Discovery source only, never authoritative proof. Independently verify company, exact role/JD, AI relevance, liveness, requirements, dedupe and route before Issue creation.

---

## 19. GitHub write safety

Verify material GitHub writes by reading them back.

If a create action times out or could have succeeded ambiguously, search/read back before retrying. Persistent ambiguity stops the write loop.

---

## 20. Privacy and keep-it-small rule

Store only operational facts. Do not copy credentials, authentication material or unnecessary personal identifiers into Issues.

Do not add Projects, another database/dashboard/frontend/spreadsheet, score file, knowledge graph or new application framework unless repeated real failures prove the current GitHub-Issues model inadequate.
