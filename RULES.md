# Operating Rules

## 1. Goal and priority

North star: maximize the probability of getting a **permanent full-time AI-related offer the candidate would genuinely accept**.

Do not optimize raw application count, Issue count, callback count or interview count in isolation. Use them only as funnel evidence.

Current execution mode is **divide-and-conquer AI-career search** across six battlefields:

- `SG-ENG`
- `SG-RES`
- `CN-ENG`
- `CN-RES`
- `MY-ENG`
- `MY-RES`

Priority order:

1. advance active employer responses, OA, interviews, recruiter conversations and real deadlines;
2. reconcile GitHub/Gmail lifecycle state before creating new queue items;
3. find and verify realistically applicable AI/ML/research roles across the six battlefields;
4. allocate effort toward battlefields producing the best combination of role quality and real progression;
5. keep Hong Kong paused until explicitly reactivated.

Optimize for the combined probability of a good accepted offer:

**role quality × eligibility/work-auth feasibility × screen probability × interview probability × engineering/research environment × compensation/WLB where evidenced × career growth/portability × willingness to accept**.

Engineering and research are both valid outcomes. Research is not a downgrade or exception lane.

Active target families include:

- Applied AI / AI Application / Generative AI;
- LLM / RAG / Agent / Coding Agent / Agent Harness;
- AI Backend / AI Software Engineer / AI-native Product Engineer;
- ML Engineer / NLP / Search / Retrieval / Ranking where work is materially AI/ML;
- Agent/LLM evaluation / AI quality / AI testing where AI systems are the actual object of the work;
- Research Engineer / AI Researcher / Applied Scientist / Research Scientist when hard requirements are realistic;
- data science when the core work is materially ML/AI rather than generic BI/analytics.

Generic Software Engineer / Backend / Full-stack / QA/SDET titles survive only when the actual team/product/JD is materially AI-related.

Any application, recruiter outreach or other employer-facing action requires explicit user authorization for that exact action or an unambiguous authorized batch.

---

## 2. Source of truth

- GitHub Issues = live operational opportunity state.
- Gmail = receipts, recruiter messages, OA/interviews, deadlines, rejections and targeted dedupe evidence.
- `PROFILE.md` = stable candidate facts + current battlefield/market strategy.
- `RULES.md` = detailed execution policy.
- `DISCOVERY_STATE.md` = compact verified discovery/maintenance receipt, FreeHire cursor, and bounded hourly-scout incremental state only.
- Old spreadsheet = legacy/read-only.

Scheduler prompts and `NEXT_CHAT_PROMPT.md` must read these files rather than carry private copies of strategy/policy.

Do not create another dashboard, database, spreadsheet mirror, score file, knowledge graph, application framework or parallel tracker.

---

## 3. Battlefield contract

### `SG-ENG` — quality-first AI engineering

Search early-career Applied AI, GenAI, LLM/Agent/RAG, AI software/backend/product, ML/NLP/search/retrieval/evaluation and FDE roles.

Singapore requires employer-supported EP or S Pass. `UNKNOWN` sponsorship willingness may reach APPLY. Explicit no-sponsorship/local-right-to-work-only wording is BLOCKED. MCF-only routes are blocked unless a separate usable route exists.

Because work-pass friction is real, prioritize roles with enough technical/career upside to justify it. Do not compensate for sponsorship friction by spraying low-quality generic roles.

### `SG-RES` — MSc-compatible research

Search Research Engineer, Applied Scientist, AI/NLP/Retrieval/Agent research and realistic applied-research roles.

Hard PhD, hard publication-record, postdoc or mature independent-research requirements the candidate does not meet are blockers. MSc thesis/research may truthfully support research-experience claims where wording permits.

### `CN-ENG` — higher-throughput native AI search

Search 2026-compatible AI应用、大模型、Agent/RAG、AI后端、AI软件、算法/ML/NLP、检索/推荐/评测 and related AI engineering roles.

Employer-supported Mainland China foreign work permit is required. Employer willingness may remain UNKNOWN until engagement; UNKNOWN alone does not block APPLY. Explicit citizenship/foreign-hire/cohort blockers do.

Use native routes first for coverage and human reach: BOSS, official/campus portals, 牛客, 51job, 智联, 猎聘. Direct recruiter/employer routes are valuable when verified.

### `CN-RES` — MSc-compatible research

Search Research Engineer, AI研究/应用研究, Applied Scientist, NLP/Retrieval/Agent research where requirements are realistic.

Do not let employer prestige override foreign-hire, degree, publication, seniority or technical hard blockers.

### `MY-ENG` — TOP / destination-quality only

Malaysia has no foreign-work-permit friction for this candidate.

Search strong MNC/regional tech, serious AI product/R&D teams, strong banks/digital banks and high-upside AI companies for meaningful AI engineering work.

**Malaysia is not a generic fallback lane.** Ordinary low-upside generic SWE, shallow AI-wrapper roles, weak outsourcing/bodyshop and roles that would not plausibly be worth choosing over continuing SG/CN should not enter APPLY/CHECK merely because they are local.

### `MY-RES` — TOP / destination-quality only

Search strong research/research-engineering environments with meaningful applied research, credible technical peers/mentorship and career portability.

Local work authorization is an advantage, not a reason to lower the quality bar.

### Hong Kong — paused

Do not discover new HK roles. Existing submitted WAIT items remain only so employer replies are not lost.

### Web3 / crypto

Not a primary lane. Consider only when permanent full-time, credible and materially AI/ML-related.

---

## 4. Employment-type hard rule

For this search, **permanent full-time is a hard outcome filter**.

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
- 1–3 YOE normal target/stretch territory;
- reasonable 2–4 YOE may survive when hard requirements and ownership remain plausible.

Hard/near-hard negatives:

- hard 4+/5+ professional-YOE floor without a real alternative route;
- Staff / Principal / Lead / Manager / Director / Head of or clearly mature ownership;
- specialized professional-experience floor the candidate cannot truthfully satisfy;
- research role with hard PhD requirement not met;
- hard publication-record / independent-research / postdoc requirement not met.

A Senior title alone is a review flag, not automatic rejection. Read the JD.

Mandatory `3+ years` is a meaningful negative signal, but generic software-engineering wording may truthfully use paid part-time/intern production work when employer wording permits it. Do not reinterpret specialized floors such as `2+ years professional production GenAI` as generic software experience.

Never convert master's study, projects, internships or part-time work into fictitious conventional full-time professional YOE.

---

## 6. Maintenance and lifecycle

Before changing queue state:

1. read README / PROFILE / RULES / DISCOVERY_STATE;
2. inspect current ACTION / APPLY / CHECK relevant to the task;
3. inspect WAIT only when recent, Gmail-triggered or needed for dedupe;
4. check both Gmail accounts when lifecycle/dedupe evidence is needed;
5. update existing Issues before creating new opportunities.

State transitions:

- official application receipt or user-confirmed `applied` → WAIT;
- OA / interview / recruiter reply / useful requested action / deadline → ACTION;
- explicitly authorized application awaiting execution may remain ACTION until submission evidence exists;
- confirmed rejection / expired / duplicate / user skip / paused market / hard blocker / clear AI-direction mismatch → close;
- silence is not rejection;
- newer evidence overrides older evidence.

Keep title, status label, body and next action synchronized.

For an authorized application-type ACTION, the Issue body must say `AUTHORIZED APPLICATION; submission pending`; do not ask authorization again for that exact unchanged role.

---

## 7. Automation and discovery cadence

Automation is reconnaissance and feedback, not autonomous execution.

Runtime baseline:

- Singapore scout runs hourly and covers `SG-ENG` + `SG-RES`;
- Mainland China scout runs hourly and covers `CN-ENG` + `CN-RES`;
- Malaysia TOP scout runs hourly and covers `MY-ENG` + `MY-RES`;
- recruiting signal watch checks both Gmail accounts hourly but notifies only on meaningful recruiting progression;
- weekly strategy review compares all six battlefields and recommends next-week effort allocation.

Exact runtime timestamps live in the automation definitions. Do not duplicate exact minute offsets in repo policy.

Hourly scouts are **read-only for opportunity/application state**. They do not submit applications, contact employers, modify Gmail, or mutate GitHub Issues. They may update only the bounded hourly-scout cursor / recent-seen receipt inside `DISCOVERY_STATE.md` so repeated unchanged search results can be skipped cheaply across runs.

A scout-state write is allowed only when the cursor/watermark/recent-seen set materially changed. Do not create heartbeat commits. If the state write cannot be completed safely, report the exact limitation and continue with GitHub-history dedupe rather than inventing state.

Do not force equal discovery volume across battlefields. SG is quality-first, CN may run higher-throughput after hard filtering, and MY must clear the destination-quality bar.

Weekly allocation is adaptive. Evaluate real funnel evidence separately for each battlefield:

`application → meaningful human/recruiter response → OA/challenge → interview → later round → offer`

Automated receipts are not meaningful progression. GitHub WAIT counts are not clean application denominators.

One unusual event must not rewrite strategy. Reallocation should follow repeated or materially strong evidence.

---

## 8. Discovery pipeline

Use:

`battlefield scout → source delta/fresh head → derive candidate key → incremental seen filter → cheap hard filter → cheap GitHub dedupe → ONLY for net-new/changed candidates read actual JD/team/product → AI/research relevance → liveness/eligibility → targeted Gmail dedupe → exact route → recommend survivor`

**Do not open and deeply research an unchanged candidate merely to discover at the end that it was already seen.** Dedupe is a pre-research gate.

Raw discovery candidates do not become Issues automatically.

Active role families:

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

Not routine targets:

- pure generic backend/SWE/full-stack with no AI work;
- ordinary QA/SDET/test automation unrelated to AI systems;
- generic DevOps/SRE/security/networking;
- BI/reporting analytics;
- unrelated specialist systems roles;
- research positions with clearly unmet hard PhD/publication requirements.

Cheap hard blockers include:

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

---

## 9. Incremental discovery and cheap dedupe before expensive research

Every hourly scout must behave incrementally.

### Candidate key

Derive the cheapest stable key available, in this order:

1. `source + exact requisition/job ID`;
2. canonical exact-role URL when no stable ID exists;
3. fallback normalized `company | title | location` fingerprint.

Do not spend tokens opening the full JD merely to derive a key when search-result metadata already exposes one.

### Cross-run seen gate

Before deep research, compare the candidate key against:

1. `DISCOVERY_STATE.md` source watermark / bounded recent-seen cache for that market;
2. all relevant GitHub Issues, including closed history, using exact req/job ID first and then exact/near-identical employer-title identity;
3. current-run candidates so the same role from multiple mirrors is collapsed before verification.

If the exact candidate was seen before and the source does **not** indicate a material change, skip immediately. Do not re-open the JD, re-check Gmail, or re-run full eligibility research.

A same-employer but materially different role remains eligible for comparison; this rule suppresses unchanged role repeats, not legitimate distinct requisitions.

### NEW / CHANGED rule

Deep verification is reserved for:

- a genuinely new candidate key; or
- a previously seen candidate for which the source provides a meaningful `CHANGED`/updated signal, new exact requisition identity, changed employment/seniority/location/JD, reopened status, or other material evidence that could change the verdict.

A crawler timestamp alone is not a material change.

### Source cursor / recent-seen state

Prefer source-native incremental state when available: monotonic event sequence, `updated_at`, posted-after watermark, source cursor, page token, or equivalent.

When a source has no reliable delta API/filter:

- inspect only a shallow fresh head rather than repeating a broad historical sweep every hour;
- compare search-result keys to the bounded recent-seen cache before opening results;
- keep the fallback cache bounded to **at most 200 candidate keys per market**, evicting oldest entries first;
- do not store job descriptions or duplicate the Issue tracker in the cache.

`DISCOVERY_STATE.md` stores only compact discovery efficiency state: last successful scout time, useful source watermarks/cursors, and the bounded fallback seen keys. It is not opportunity state and must not become a second job list.

### FreeHire

For FreeHire, consume `feed/candidates.json` / event sequence as the incremental surface. Unchanged jobs are already suppressed upstream; do not traverse historical pages during routine hourly scouting.

---

## 10. Verify serious survivors

For plausible net-new/changed survivors verify:

1. exact/full JD and current role-level liveness;
2. material AI/ML/research relevance;
3. battlefield fit, including the MY destination-quality bar;
4. employment classification;
5. cohort, seniority and hard requirements;
6. realistic candidate fit;
7. work authorization where relevant;
8. targeted Gmail dedupe in both accounts using exact requisition/job ID first when available;
9. exact usable application route.

A role does not need the literal word Permanent to reach APPLY. PROBABLE regular full-time employment is sufficient when no contradictory non-permanent evidence exists.

Before creating/promoting CHECK or APPLY with a requisition/job ID, search that exact ID in GitHub and both Gmail accounts. Exact prior application → WAIT.

---

## 11. Work authorization classification

Use CONFIRMED / PROBABLE / UNKNOWN / BLOCKED.

UNKNOWN is allowed to reach APPLY. BLOCKED is not. Lack of public sponsorship wording alone is not a CHECK blocker.

---

## 12. Freshness and current-liveness gate

Freshness is a ranking signal, not a 30-day death sentence.

Current liveness is required before a new APPLY/CHECK Issue is created. Strong proof includes an active exact-role form/ATS action, official current role page with active apply action, current application window, or employer-controlled ATS status showing the requisition open/published.

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
- active battlefield fit;
- no obvious cohort/seniority/hard-requirement block;
- current role-level liveness proof;
- employment CONFIRMED or PROBABLE, or exactly one CONFLICT blocker on an otherwise strong role;
- no established duplicate;
- either a verified exact route or exactly one material blocker remaining other than sponsorship/work-permit UNKNOWN.

For MY-ENG/MY-RES, it must also clear the destination-quality bar. Ordinary low-upside local roles create nothing.

Bad, closed, generic-non-AI, obvious-mismatch or raw candidates create nothing.

---

## 15. Issue states and queue hygiene

Only four open states: ACTION / APPLY / CHECK / WAIT.

- ACTION = concrete recruiting action now/soon, including OA/interview/recruiter reply/deadline or authorized application pending execution.
- APPLY = verified, live, materially AI-related role ready for user review. APPLY is not submission permission.
- CHECK = liveness proven; exactly one material blocker or user decision remains.
- WAIT = already submitted/contacted and waiting.

Rejected, expired, duplicate, blocked, market-paused, AI-direction-mismatch, withdrawn or user-skipped roles are closed.

Every open opportunity must have exactly one market label and exactly one status label. Whenever state changes, update title, labels, body and next action together and read back the result.

APPLY/CHECK should store exact route/blocker, req ID, liveness, employment evidence, plain-language work, hard requirements, AI relevance, strengths/gaps, work auth, dedupe result and exactly one next action.

Do **not** encode strategic priority using ad-hoc title markers such as `[TOP]`. The status prefix and market are operational state; priority comes from battlefield strategy and current evidence.

---

## 16. Authorization

APPLY means recommended for review, not permission to submit.

Only explicit authorization for that exact role/action permits an application or external contact. `go` on one exact role does not authorize other roles at the same employer.

When authorization is granted but execution is not yet possible, keep it in ACTION and mark `AUTHORIZED APPLICATION; submission pending`. Move to WAIT only after real submission/contact evidence exists.

---

## 17. FreeHire lane

Routine public FreeHire ingestion is owned by `kolihhan/freehirefetch`.

- FreeHire contains public job data and machine-dedupe/health metadata only.
- FreeHire is Stage 1 discovery evidence only.
- Its raw search may remain broader than the final target because AI companies may use generic engineering titles.
- Raw FreeHire category inclusion does not imply queue eligibility.
- SG: useful broad radar plus direct/ATS/platform gap search.
- CN: supplementary; native sources remain primary.
- MY: supplementary; destination-quality filtering still applies.
- Routine hourly consumption uses the incremental `feed/candidates.json` surface; historical page traversal is for explicit catch-up/audit only.
- Preserve the FreeHire cursor section when updating DISCOVERY_STATE.

---

## 18. Source-specific notes

### Singapore

Use FreeHire + direct employer/ATS + LinkedIn/JobStreet/Indeed gaps. Rotate engineering and research lanes. Quality and work-pass plausibility matter more than raw volume.

### Mainland China

Rotate BOSS → official/campus → 牛客 → 51job → 智联 → 猎聘. Search AI应用、大模型、Agent、RAG、AI后端、算法/ML/NLP、检索/推荐/评测 and research/research-engineering. Keep native/direct human routes prominent.

For hourly CN discovery, prefer source update/posted filters or a shallow fresh head. Do not re-open the same 牛客/智联/BOSS/official role every hour after its candidate key has been seen unchanged.

### Malaysia

Use official careers, LinkedIn, JobStreet/Hiredly and direct employers, but only surface opportunities that clear the TOP/destination-quality bar.

### Hong Kong

Paused.

### Telegram / DeJob

Discovery source only, never authoritative proof. Independently verify company, exact role/JD, AI relevance, liveness, requirements, dedupe and route before Issue creation.

---

## 19. GitHub write safety

Verify material GitHub writes by reading them back.

If a create/update action times out or could have succeeded ambiguously, search/read back before retrying. Persistent ambiguity stops the write loop.

Scout automation may write only its compact cursor/recent-seen receipt inside `DISCOVERY_STATE.md`; it may not mutate Issues. Preserve unrelated receipt sections when updating that file.

---

## 20. Privacy and keep-it-small rule

Store only operational facts. Do not copy credentials, authentication material or unnecessary personal identifiers into Issues.

Do not add Projects, another database/dashboard/frontend/spreadsheet, score file, knowledge graph or new application framework unless repeated real failures prove the current GitHub-Issues model inadequate.