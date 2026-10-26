# Operating Rules

## 1. North star

Maximize the probability of getting a **permanent full-time AI-related offer the candidate would genuinely accept**.

Do not optimize raw application count, Issue count, callback count, interview count, or discovery volume in isolation. Those are funnel signals only.

Active battlefields:

- `SG-ENG`
- `SG-RES`
- `CN-ENG`
- `CN-RES`
- `MY-ENG`
- `MY-RES`

Hong Kong is paused until explicitly reactivated.

Engineering and research are both valid outcomes. Optimize for the combined probability of a good accepted offer:

**role quality × eligibility/work-auth feasibility × screen probability × interview probability × technical environment × compensation/WLB where evidenced × growth/portability × willingness to accept**.

Any application, recruiter outreach, or other employer-facing action requires explicit user authorization for that exact action or an unambiguous authorized batch.

---

## 2. Source of truth

- GitHub Issues = the only live operational opportunity state.
- Gmail = receipts, recruiter/OA/interview/deadline/rejection evidence and targeted dedupe.
- `PROFILE.md` = stable candidate facts + battlefield/market strategy.
- `RULES.md` = detailed execution policy.
- `DISCOVERY_STATE.md` = compact machine efficiency state only: source watermarks/cursors, bounded recent-seen cache, and migration receipts.
- Old spreadsheet = legacy/read-only.

Do not create another dashboard, database, spreadsheet mirror, score file, candidate inbox, knowledge graph, or parallel tracker.

Scheduler prompts must read the repo contract rather than maintain private copies of policy.

---

## 3. Battlefield contract

### SG-ENG

Quality-first early-career Applied AI, GenAI, LLM/Agent/RAG, AI software/backend/product, ML/NLP/search/retrieval/evaluation and FDE roles.

Singapore requires employer-supported EP or S Pass. Sponsorship `UNKNOWN` may reach APPLY. Explicit no-sponsorship/local-right-to-work-only wording is BLOCKED. MCF-only routes are blocked unless a separate usable route exists.

### SG-RES

MSc-compatible Research Engineer, Applied Scientist, AI/NLP/Retrieval/Agent research and realistic applied-research roles.

Hard PhD, postdoc, hard publication-record, or mature independent-research requirements not met are blockers.

### CN-ENG

Higher-throughput 2026-compatible AI应用、大模型、Agent/RAG、AI后端、AI软件、算法/ML/NLP、检索/推荐/评测 roles.

Use employer first-party recruiting plus native/direct routes. BOSS and 牛客 remain especially valuable when they expose recruiter reach or a usable direct action. Employer willingness to support a Mainland China foreign work permit may remain UNKNOWN until engagement; explicit blockers do block.

### CN-RES

MSc-compatible Research Engineer, AI研究/应用研究, Applied Scientist, NLP/Retrieval/Agent research. Prestige never overrides degree/publication/seniority/foreign-hire hard blockers.

### MY-ENG

**TOP / destination-quality only.** Strong MNC/regional tech, serious AI product/R&D, strong banks/digital banks, and high-upside AI companies with meaningful AI ownership and career upside.

Malaysia is not a generic fallback lane. Ordinary low-upside local roles, shallow AI wrappers, and weak outsourcing/bodyshop roles do not enter the queue merely because they are local or AI-labelled.

### MY-RES

**TOP / destination-quality only** research/research-engineering environments with credible technical peers, meaningful applied research, and career portability.

---

## 4. Target role and hard-filter rules

Target families include:

- Applied AI / AI Application / Generative AI;
- LLM / RAG / Agent / Coding Agent / Agent Harness;
- AI Backend / AI Software / AI-native Product Engineering;
- ML Engineer / NLP / Search / Retrieval / Ranking when genuinely ML-oriented;
- Agent/LLM evaluation / AI quality / AI testing where AI systems are the object of the work;
- Research Engineer / AI Researcher / Applied Scientist / Research Scientist when requirements are realistic;
- AI/ML-heavy Data Scientist.

Generic SWE/backend/full-stack/QA titles survive only when the actual team/product/JD is materially AI-related. **Do not title-gate at the cheap screen when source metadata, snippet, team name, or product context already contains strong Agent/LLM/RAG/MCP/Coding-Agent/AI-first signals; preserve the candidate long enough to read the actual JD.**

Cheap hard blockers include:

- paused/wrong market;
- explicit non-permanent employment;
- hard mature seniority or 4+/5+ professional-YOE floor without a real alternative route;
- incompatible graduation/cohort window;
- explicit citizenship/no-sponsorship/right-to-work blocker where relevant;
- clearly unmet hard PhD/publication/research requirement;
- substantial mandatory stack/domain mismatch;
- clearly closed/expired listing;
- exact duplicate/already applied.

For campus, graduate, trainee, named-program, or year-coded hiring (for example `2027`, `AIDU`, graduate programme), **program/campaign eligibility is part of the hard requirements**. If the exact role page omits the graduation window, inspect the employer-controlled campaign/program page before promotion. Exact-JD silence is not evidence of cohort compatibility. An explicit incompatible campaign window is BLOCKED.

A Senior title alone is a review flag, not automatic rejection. A mandatory `3+ years` is a real negative, but generic engineering wording may truthfully use paid part-time/intern production work when employer wording permits it. Never convert study/projects/internships/part-time work into fictitious conventional full-time YOE.

Do not strengthen `preferred`, `plus`, `bonus`, `nice to have`, `familiarity`, `exposure`, coursework, self-study, or personal-project wording into hard requirements.

---

## 5. Employment type

Permanent full-time is a hard outcome filter.

- `CONFIRMED` — role explicitly says permanent/regular indefinite employment.
- `PROBABLE` — normal full-time/regular hiring with no contradictory non-permanent signal.
- `CONFLICT` — credible current sources disagree.
- `BLOCKED` — evidence establishes contract/fixed-term/temp/part-time/freelance/internship/trainee/project-only/staffing or another prohibited type.

CONFIRMED or PROBABLE may reach APPLY. CONFLICT may use CHECK only when it is the one remaining material blocker. BLOCKED closes/skips.

---

## 6. Lifecycle and authorization

Open states:

- ACTION = concrete recruiting action now/soon, including OA/interview/recruiter reply/deadline or an authorized application awaiting execution.
- APPLY = verified live opportunity ready for user review; not submission permission.
- CHECK = liveness proven and exactly one material blocker/decision remains.
- WAIT = already submitted/contacted and waiting.

Rejected, expired, duplicate, blocked, paused-market, direction-mismatch, withdrawn, or user-skipped roles are closed.

Transitions:

- official application receipt or user-confirmed `applied` → WAIT;
- OA/interview/recruiter reply/useful deadline → ACTION;
- authorized application pending execution → ACTION with `AUTHORIZED APPLICATION; submission pending`;
- confirmed rejection/expired/duplicate/user skip/hard blocker → close;
- silence is not rejection;
- newer evidence overrides older evidence.

Only explicit authorization for the exact role/action permits an application or external contact. `go` on one role does not authorize another role at the same employer.

### Direct-email application review gate

When the verified application route is an employer/recruiter email, use a mandatory **prepare → humanizer skill → user review → send** flow. A general `go` or permission to apply authorizes preparation of the package, not silent email transmission before the user has reviewed the exact package.

Before any direct-email send:

1. choose the communication language from the employer/recruiter context: normally Simplified Chinese for Mainland-China recruiting and English for Singapore/Malaysia/international recruiting, unless the actual employer communication clearly indicates otherwise;
2. draft for the actual email genre, then apply the **language-specific humanizer skill**, not an improvised generic “make it natural” pass:
   - **English:** `amanmaqsood/prose-humanizer`, catalog-reviewed `SKILL.md` SHA `e68d004810aa40b6510ff66506f6b3d26861e2ab`. Use its Draft/email guidance: build a silent evidence ledger from the JD/Issue/resume, make the minimum effective edit for the email channel, preserve semantics and claim strength, and run an independent evidence diff before delivery. Do not invent specifics, motives, results, or “human” texture.
   - **Simplified Chinese:** `Hyacehila/humanizer-zh-next`, catalog-reviewed `SKILL.md` SHA `fe895ce0e4ba91c6fe4a96a9d1d4f8e9c2c32092`. Use its email/书信 guidance: remove empty/template phrasing while preserving meaning, facts, claim strength, useful politeness, requests, dates and commitments.
   If the required skill instructions cannot be loaded, or the available `SKILL.md` differs from the pinned reviewed hash, do not pretend the named skill was used and do not silently substitute a generic humanizer; surface the mismatch to the user before sending.
3. treat the email as an **opener, not a second resume or cover letter**. Default to a short application statement, one or two plain sentences about the candidate's broad background/direction, any required work-pass note, and the attachment/closing. Do not list project names, benchmarks, frameworks, or a stack inventory merely to prove JD keyword overlap. Do not paraphrase the JD back to the employer. Mention a specific project/technology/result only when it is genuinely useful as the single strongest hook or the employer explicitly asks for it. Experience may be summarized broadly and truthfully, for example software-engineering background plus recent Applied AI/Agent work, without turning local/academic projects into professional production-AI experience. Avoid generic praise, “passionate/excited” filler, mission flattery, and over-explaining why every bullet matches;
4. for work authorization in direct email, disclose it briefly and politely near the end rather than leading with it or turning the first email into a visa negotiation:
   - **Mainland China:** state that the candidate is Malaysian and, if the process moves forward, would need the company to assist with the foreign work permit / visa process. Preferred natural reference: `另外，我是马来西亚籍，如果后续顺利推进，工作许可和签证方面可能需要公司协助处理。` Adapt to the actual email rather than forcing this sentence verbatim.
   - **Singapore:** state that the candidate is Malaysian and would need company support with the relevant Singapore work-pass process if things move forward. Keep it to one sentence and adapt naturally to the recipient.
   - **Malaysia:** normally omit work-authorization wording because the candidate is a Malaysian citizen, unless the employer specifically asks.
   Do not open with `Do you sponsor visas?` unless the employer explicitly asks for work-authorization details at that stage;
5. after humanization, fact-check the draft against the exact JD/Issue and current resume evidence. Keep it concise, specific to the role, understated and non-corporate; use only a few relevant strengths rather than copying the whole resume or JD. Never inflate professional YOE, production-AI experience, skills, work authorization, or employer facts;
6. **attach only the canonical current resume from this repo.** English applications must use `resumes/resume-en-current.pdf`; Chinese applications must use `resumes/resume-zh-current.pdf`. The attachment bytes must come from the current repo asset used for this application execution. Never substitute a Downloads copy, renamed/versioned backup, older generated PDF, local cache, prior email attachment, or another file merely because its content appears similar. Before presenting the review package, verify the selected attachment is the current canonical repo asset; when tooling exposes hashes/content identity, compare them, otherwise fetch/materialize the canonical repo file again for the send. If the exact canonical attachment cannot be established, stop before send and surface the problem. If a material resume change is genuinely needed, update the repo source-of-truth resume in place and regenerate the stable PDF first; do not create an ad-hoc application-only resume. Preserve the canonical filename unless the user explicitly approves a different display filename as part of the exact reviewed package;
7. present the user with one complete review package: **recipient, subject, exact humanized email body, selected canonical resume attachment, and any other requested attachment**;
8. do not send until the user has reviewed that exact package and explicitly approves sending it. If any material wording, recipient, subject, or attachment changes after approval, present the changed package again before sending.

Once the exact reviewed package is approved for send, transmit that package without silent rewriting or attachment substitution. Preserve sent-message evidence in the matching Issue after a successful send.

---

## 7. Automation contract

Automation is reconnaissance + durable queue maintenance, not autonomous application execution.

Runtime baseline:

- Singapore scout hourly: `SG-ENG` + `SG-RES`.
- Mainland China scout hourly: `CN-ENG` + `CN-RES`.
- Malaysia TOP scout hourly: `MY-ENG` + `MY-RES`.
- Recruiting Signal Watch hourly over both Gmail accounts.
- AI Job Strategy Review **daily** across all six battlefields.

Exact minute offsets live in automation definitions, not repo policy.

Hourly scouts may:

1. search, cheap-screen, dedupe, and verify candidates;
2. create a **new APPLY or CHECK GitHub Issue only for a verified serious survivor that satisfies sections 10–14**;
3. update only their bounded efficiency state in `DISCOVERY_STATE.md`.

Hourly scouts may **not**:

- submit applications or contact employers;
- modify Gmail;
- move/close/reopen/update existing opportunity Issues automatically;
- create Issues for raw/unverified candidates.

If a previously existing Issue has materially changed discovery evidence, scouts report it for maintenance rather than silently changing its lifecycle state.

The **Recruiting Signal Watch** is the narrow exception for lifecycle reconciliation. It may update an existing opportunity Issue only when Gmail provides high-confidence lifecycle evidence and the message maps to exactly one Issue by exact requisition/job ID or an unambiguous company + role match. Eligible evidence is limited to OA/assessment, interview scheduling/invite, human recruiter reply/request, useful deadline/action-required message, offer, or explicit rejection/withdrawal/role-closed outcome. Ordinary receipts, alerts, marketing, stale duplicates, ambiguous matches, or silence do not mutate GitHub.

When it updates an Issue, change only the lifecycle state/title/status label, minimal evidence, next action, and a compact `Furthest stage` field/line needed to reflect the newer event. `Furthest stage` is monotonic: a later administrative or waiting message must not erase a more advanced stage already reached. Do not copy unnecessary private email body text. Read the Issue back after the write. If mapping or write outcome is ambiguous, stop and report the mismatch instead of guessing or retrying blindly. Recruiting Signal Watch never sends replies, submits forms, contacts employers, or modifies Gmail.

A new survivor is not durably handed off until the Issue create succeeds **and the created Issue is read back**. If create/write outcome is ambiguous, search/read back before retrying. If persistence is not proven, do not mark that survivor handled and do not advance a source watermark past it.

---

## 8. Lossless discovery pipeline

Use this order:

`battlefield scout → first-party/source delta or bounded fresh head → derive candidate key → exact-ID/Issue-history gate → recent-seen gate → cheap hard filter → ONLY for net-new/changed candidates read actual JD/team/product → AI/research relevance → liveness/eligibility → targeted Gmail dedupe → exact route → durable APPLY/CHECK Issue or terminal disposition → advance watermark`

Dedupe is a **pre-research gate**. Do not deeply research an unchanged candidate merely to discover at the end that it already existed.

Raw discovery candidates never become Issues. **Verified serious survivors do become Issues automatically** so that good jobs cannot disappear inside an ephemeral scheduler run.

The core invariant is:

> **duplicate/reject must die early; a GOLD survivor must not disappear.**

A candidate is considered handled only when one of these is true:

- exact/near-exact existing Issue history establishes duplicate/prior disposition;
- a terminal hard/quality rejection is established and recorded in the bounded seen cache;
- a new verified APPLY/CHECK Issue was created and read back successfully.

Transient tool failure, uncertain route failure, ambiguous create, or an unpersisted survivor is **not handled**.

---

## 9. Candidate key and exact Issue-history gate

Derive the cheapest stable key available, in this order:

1. `source + exact requisition/job ID`;
2. canonical exact-role URL;
3. normalized `company | title | location` fallback.

Do not open the full JD merely to derive a key when result metadata already exposes one.

### Exact-ID hard gate

When an exact requisition/job ID exists, search **GitHub Issues, open and closed**, for that ID before opening the full JD. Use Issue search/history, not repository code search.

- Exact unchanged Issue match → stop immediately.
- Exact prior application/WAIT evidence → do not create another opportunity.
- Exact closed SKIP/duplicate/blocker → skip unless a material CHANGED/reopened signal could change the prior verdict.
- Same employer but genuinely different requisition remains eligible.

Then compare against:

- market source watermark/cursor;
- bounded recent-seen cache;
- current-run keys to collapse mirrors.

A reviewer/search snippet saying “no duplicate” is not proof unless the Issue-history query was actually run when an exact ID was available.

---

## 10. Incremental state and seen-cache semantics

Deep verification is reserved for a genuinely NEW candidate or a materially CHANGED/reopened candidate. A crawler timestamp alone is not a material change.

Prefer source-native incremental state whenever available: monotonic event sequence, `updated_at`, posted-after watermark, cursor/page token, or equivalent.

For a source with no reliable delta interface:

- inspect only a shallow fresh head;
- derive keys before opening results;
- use the bounded fallback recent-seen cache;
- persist a source `updated_at`/posted-after/cursor watermark whenever the source actually exposes a trustworthy one.

`recent_seen_keys` is **terminal-or-durable only**:

- cache a hard reject, duplicate, low-quality rejection, or other stable terminal disposition;
- cache a verified survivor **only after** its APPLY/CHECK Issue exists and readback confirms it;
- do not cache a transient fetch failure, unresolved ambiguity, or survivor whose durable handoff failed.

Fallback cache maximum: **500 keys per market**, FIFO. It stores keys only, never job descriptions or a second opportunity list.

`DISCOVERY_STATE.md` records `last_state_change_at`, not runtime health. A successful no-change scout run should not create a heartbeat commit. Actual scheduler health comes from automation runtime metadata.

---

## 11. FreeHire: fast path + lossless gap recovery

`kolihhan/freehirefetch` owns public ingestion.

FreeHire is Stage-1 discovery evidence only. It is a **Tier-3 radar**, not a primary market source. SG/CN/MY should first spend discovery effort on the market-specific first-party and direct/native lanes in section 15.

Routine consumption:

1. read `feed/index.json` and the market's stored `freehire_event_seq` watermark;
2. read `feed/candidates.json` as the **fast path**;
3. inspect `counts` vs `matched_counts` for market snapshot overflow;
4. if the stored watermark is behind the public `last_seq`, the scout was delayed/missed, or snapshot overflow means candidates could have been omitted, recover the unhandled range from sequence-addressable `feed/pages/*.jsonl` for `(watermark, last_seq]`;
5. filter cheaply by market/key/AI signals before expensive JD work;
6. advance the market `freehire_event_seq` only after every relevant candidate through that sequence boundary is terminally handled or durably persisted as an Issue.

`candidates.json` is therefore a speed optimization, **not a lossless queue**. Never assume the latest capped snapshot covers all events since the prior scout.

Historical page traversal is not routine broad re-analysis; it is bounded gap recovery from the last stored sequence.

---

## 12. Verify serious survivors

For a plausible net-new/changed survivor verify:

1. exact/full JD and current role-level liveness;
2. material AI/ML/research relevance;
3. battlefield fit, including the MY destination-quality bar;
4. employment classification;
5. cohort, seniority, and hard requirements;
6. realistic candidate fit;
7. work authorization where relevant;
8. targeted Gmail dedupe in both accounts using exact requisition/job ID first when available;
9. exact usable application route.

For campus/graduate/program hiring, verification in item 5 includes the **employer-controlled campaign/program eligibility**, not only the exact role page. If a role is year-coded or clearly attached to a named graduate campaign and the exact JD omits its graduation window, resolve that window before promotion. If campaign compatibility cannot be established and it is the only remaining material blocker, CHECK may be used; an explicit incompatible window is BLOCKED.

A role does not need the literal word `Permanent` to reach APPLY. PROBABLE regular full-time is sufficient when no contradictory evidence exists.

Work authorization uses CONFIRMED / PROBABLE / UNKNOWN / BLOCKED. UNKNOWN may reach APPLY; BLOCKED may not. Lack of public sponsorship wording alone is not a CHECK blocker.

---

## 13. Liveness and application route

Current role-level liveness is required before a new APPLY/CHECK Issue is created. Strong proof includes an active exact-role form/ATS action, employer-controlled current role page, active application window, or employer-controlled ATS status.

Search snippets, mirrors, aggregator pages, and crawler timestamps are discovery evidence only. Newer closed/expired evidence overrides older liveness evidence.

APPLY requires a current usable exact-role route: exact form, employer ATS requisition, usable platform-native flow, or employer-controlled recruiting email instruction.

LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客, 猎聘 or similar count when the exact-role action is usable.

For a high-quality survivor, prefer the lowest-friction credible route after role verification: employer ATS, employer-controlled recruiting email, native recruiter chat, or native apply. A better route improves execution priority but does not weaken eligibility or quality gates.

If tooling prevents route verification, CHECK is allowed only when liveness is independently proven and route verification is the one remaining blocker.

Fresh-check the route immediately before acting on a user `go`.

---

## 14. Issue creation and queue hygiene

Create a new Issue only for a verified serious survivor that deserves user attention.

Required:

- material AI/ML/research relevance;
- realistic early-career fit;
- active battlefield fit;
- no obvious cohort/seniority/hard-requirement block;
- current exact-role liveness proof;
- employment CONFIRMED or PROBABLE, or exactly one CONFLICT blocker on an otherwise strong role;
- exact GitHub Issue-history dedupe completed;
- targeted Gmail dedupe completed when required;
- verified exact route, or exactly one material blocker remaining other than sponsorship/work-permit UNKNOWN.

For MY, the role must also clear the TOP/destination-quality bar.

Issue states:

- APPLY when all promotion gates pass.
- CHECK only when liveness is proven and exactly one material blocker remains.

Every new Issue must have exactly one `market:*` label and one `status:*` label. Store: battlefield, company/title/location, exact ID/URL, liveness, employment evidence, plain-language work, hard requirements, AI relevance, strengths/gaps, work auth, dedupe result, **Discovery source (specific source + tier), Application route / route type**, exact route/blocker, and one next action. These source/route fields are required so later strategy learning can measure source yield instead of guessing.

After create, read back the Issue. **Only after successful readback may the candidate key be cached and its source watermark advanced.**

Do not use `[TOP]` title markers. Priority comes from battlefield strategy and current evidence.

---

## 15. Source strategy: first-party first

The source hierarchy is about **where to look first**, not which employers are allowed. The target-company universe is a priority watch list, **not a whitelist**. A strong company/role outside the list may still enter APPLY/CHECK if all normal gates pass.

### Global source tiers

**Tier 1 — first-party / direct**

- employer-controlled career page or exact ATS (Workday, Greenhouse, Ashby, Lever, SmartRecruiters, Moka/北森/自研 ATS, etc.);
- official university/research-lab career portal for the actual employer/team;
- official campus/social-recruiting portal;
- employer-controlled recruiting email or named recruiter route published by the employer.

**Tier 2 — high-signal native/direct platforms**

- Singapore/Malaysia: LinkedIn exact-role/native apply, JobStreet, Hiredly, Indeed when the exact role and action are current;
- Mainland China: BOSS and 牛客 first because recruiter reach/direct chat can materially improve execution; 51job, 智联 and 猎聘 are secondary native coverage.

**Tier 3 — radar / aggregation**

- FreeHire, WhatJobs, generic job indexes, search-engine snippets, Telegram/DeJob and other mirrors.

Tier 3 is discovery only. It must resolve to authoritative/current exact-role evidence before promotion. Do not spend broad-sweep effort on Tier 3 while obvious Tier-1 target-company coverage is still missing.

### Bounded target rotation

Do not full-sweep every target employer every hour. Each hourly scout should inspect a bounded subset of first-party targets plus source-native deltas/fresh heads, rotating across the core watch universe. Prefer sources exposing reliable updated/posted filters or requisition feeds. Repeatedly reloading unchanged career homepages is not useful work.

If a target employer has no current plausible early-career AI role, record no new opportunity state; move on. The watch list exists to improve signal quality, not to force an Issue from every company.

### Singapore — quality-first first-party watch

Core first-party target groups:

- **AI / research:** AI Singapore / NTU, A*STAR (especially IAIC/IHPC/CFAR), Sea AI Lab;
- **frontier / product AI:** OpenAI Singapore, Sea/Shopee, Grab, ByteDance/TikTok;
- **strong engineering / industry AI:** Micron, Apple, Google, Microsoft, Singtel;
- **selected finance/fintech where the exact work is real AI:** DBS, Prudential, Visa and similarly strong teams.

Source order:

`official employer/ATS or research portal → direct recruiter/employer route if published → LinkedIn/JobStreet/Indeed exact-role gaps → FreeHire/aggregator radar`.

Quality and work-pass plausibility matter more than volume. Unknown sponsorship may still reach APPLY, but do not compensate for work-pass friction by padding SG with mediocre roles.

### Mainland China — official + recruiter-reach first

Core first-party target groups:

- **large AI/product platforms:** Alibaba, Tencent, ByteDance, Huawei/Huawei Cloud, Baidu, Meituan, JD, Xiaohongshu;
- **AI-native/model companies with official recruiting surfaces:** DeepSeek, Moonshot/Kimi, Zhipu AI, StepFun and similarly strong current AI-native employers;
- **high-signal smaller AI/product teams:** role-triggered first-party/direct employers such as current Agent/Harness/AI4S companies may be added when their exact role quality is strong.

Source order:

`official social/campus career portal → BOSS/牛客 direct recruiter/native action → 51job/智联/猎聘 → FreeHire/aggregator radar`.

Use BOSS/牛客 aggressively for human reach, but do not let a platform listing outrank a contradictory employer-controlled JD. Prefer 2026-compatible and 0–3 YOE roles; kill explicit foreign-hire/cohort blockers cheaply.

### Malaysia — destination-company first

Malaysia is intentionally **company-first and TOP-only**, not a broad AI-board sweep.

Core first-party target groups:

- **regional/product tech:** Sea/Shopee, Grab;
- **fintech/digital-bank/AI product:** Gen Digital/MoneyLion, AEON Bank, GXBank and similarly strong product teams;
- **strong MNC engineering/R&D:** Keysight, AMD, Intel, Dell and similarly strong Malaysia engineering hubs;
- **high-upside local/regional AI teams:** YTL AI Labs and other teams only when the exact role clears the destination-quality bar.

Role-triggered exceptions outside the core watch list are allowed when the exact role itself is unusually strong on AI ownership, compensation, engineering environment and growth. A famous company with shallow work is not automatically MY TOP; a lesser-known company with exceptional role/team evidence can still pass.

Source order:

`official employer/ATS → employer-controlled recruiter/direct route → LinkedIn/JobStreet/Hiredly exact-role → selective recruiter agency when the role/client quality is evidentially strong → FreeHire/aggregator radar`.

Do not spend meaningful MY search time on ordinary local generic AI/SWE listings merely because work authorization is easy.

### GOLD route enrichment

For an unusually strong verified opportunity, after the exact role is established, spend a small bounded amount of effort checking whether there is a better human-visible route:

- named recruiter/talent partner;
- employer-published recruiting email;
- BOSS/牛客 recruiter chat;
- hiring manager or clearly relevant same-team contact when publicly identifiable;
- credible alumni/warm path when naturally available.

This is route enrichment, not authorization to contact anyone. Do not invent relationships, spam employees, or use people-search as a substitute for applying to the role.

### Telegram / DeJob / other mirrors

Discovery only, never authoritative proof. Independently verify exact role/JD, AI relevance, liveness, hard requirements, dedupe, and route.

---

## 16. GitHub write safety

Verify material GitHub writes by reading them back.

If a create/update times out or could have succeeded ambiguously, search/read back before retrying. Persistent ambiguity stops the write loop.

Hourly scout write scope is deliberately narrow:

- create a **new** verified APPLY/CHECK Issue after section-14 gates pass;
- update only its own bounded state object in `DISCOVERY_STATE.md`.

Scouts do not automatically modify/close/reopen existing opportunity Issues. They do not submit applications or contact employers.

Recruiting Signal Watch may make only the narrow deterministic lifecycle updates authorized in section 7. Every such update must be read back; ambiguous role mapping or write outcome stops mutation and is reported instead.

---

## 17. Daily strategy, adaptive learning, and execution

Do not force equal discovery volume across battlefields. SG is quality-first, CN may be higher-throughput after hard filters, and MY is destination-quality only.

Evaluate each battlefield using the real funnel:

`application → meaningful human/recruiter response → OA/challenge → interview → later round → offer`

Also compare **source yield**, not just market yield: first-party/direct, native/direct platform, and radar/aggregator should be judged by how many serious survivors and meaningful recruiting progressions they produce. Source-yield conclusions require actual `Discovery source` and `Application route` evidence; do not infer the source from company or Issue age.

Automated receipts are not meaningful progression. WAIT counts are not clean application denominators. Do not penalize an unexecuted APPLY, a recent application that has not had a reasonable chance to progress, or silence alone. Do not reward a market/source merely because it received more applications or because local work authorization is easier.

### Controlled adaptive learning

Continuous observation is allowed; strategy mutation is deliberately slower. Change soft search strategy only when either:

1. at least **two independent meaningful outcomes** support the same directional signal; or
2. one directly verified recall/precision failure reveals a deterministic screening bug that would predictably recur.

One rejection, interview, employer, or unusual event must not rewrite the strategy by itself.

When the learning threshold is met, update only `## Adaptive learning memory` in `PROFILE.md`:

- keep at most **8 current bullets**;
- each bullet states scope/battlefield, observed signal, concrete evidence, soft search-priority adjustment, and a review/expiry condition;
- replace or delete stale/contradicted bullets instead of accumulating history;
- hard RULES always override adaptive memory.

Adaptive memory may reweight source emphasis, query/title recall, employer rotation, route preference, and search effort. It must **not** change stable candidate facts, permanent/full-time policy, active market scope, work-authorization facts, truthful-experience rules, employer-facing authorization requirements, or turn sponsorship/work-permit `UNKNOWN` into a hard blocker without explicit user instruction.

Preserve bounded exploration. Adaptive learning may reweight active battlefields, but it must not zero one out merely because another lane recently performed better. Continue enough exploration to detect regime changes and hidden GOLD.

### Execution governor

Lossless opportunity storage and human attention are different problems. Keep all verified survivors in GitHub Issues, but when the user asks `what now`, when a strategy review runs, or when the APPLY queue is materially larger than practical execution capacity, **derive rather than persist** a small execution view:

- `APPLY NOW` — the top **3–5** opportunities to act on next;
- `NEXT` — strong opportunities after the immediate set;
- `SELECTIVE` — worthwhile stretches or lower-callback options.

Rank from current Issue evidence using the north-star factors plus deadline/urgency and application friction. Do not create `[TOP]` labels, another priority tracker, or a score file. This derived view does not change APPLY eligibility and does not authorize submission.

---

## 18. Privacy and keep-it-small rule

Store only operational facts. Do not copy credentials, authentication material, unnecessary personal identifiers, OTPs, or private email bodies into Issues.

Do not add another tracker/framework unless repeated real failures prove the GitHub-Issues model inadequate.
