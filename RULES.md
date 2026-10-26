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

Use native/direct routes first: BOSS, official/campus, 牛客, 51job, 智联, 猎聘. Employer willingness to support a Mainland China foreign work permit may remain UNKNOWN until engagement; explicit blockers do block.

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

Generic SWE/backend/full-stack/QA titles survive only when the actual team/product/JD is materially AI-related.

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

---

## 7. Automation contract

Automation is reconnaissance + durable queue maintenance, not autonomous application execution.

Runtime baseline:

- Singapore scout hourly: `SG-ENG` + `SG-RES`.
- Mainland China scout hourly: `CN-ENG` + `CN-RES`.
- Malaysia TOP scout hourly: `MY-ENG` + `MY-RES`.
- Recruiting Signal Watch hourly over both Gmail accounts.
- AI Job Strategy Review weekly across all six battlefields.

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

If a previously existing Issue has materially changed evidence, report it for maintenance rather than silently changing its lifecycle state.

A new survivor is not durably handed off until the Issue create succeeds **and the created Issue is read back**. If create/write outcome is ambiguous, search/read back before retrying. If persistence is not proven, do not mark that survivor handled and do not advance a source watermark past it.

---

## 8. Lossless discovery pipeline

Use this order:

`battlefield scout → source delta/fresh head → derive candidate key → exact-ID/Issue-history gate → recent-seen gate → cheap hard filter → ONLY for net-new/changed candidates read actual JD/team/product → AI/research relevance → liveness/eligibility → targeted Gmail dedupe → exact route → durable APPLY/CHECK Issue or terminal disposition → advance watermark`

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

FreeHire is Stage-1 discovery evidence only. SG uses it as broad radar; CN/MY use it as supplementary discovery.

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

A role does not need the literal word `Permanent` to reach APPLY. PROBABLE regular full-time is sufficient when no contradictory evidence exists.

Work authorization uses CONFIRMED / PROBABLE / UNKNOWN / BLOCKED. UNKNOWN may reach APPLY; BLOCKED may not. Lack of public sponsorship wording alone is not a CHECK blocker.

---

## 13. Liveness and application route

Current role-level liveness is required before a new APPLY/CHECK Issue is created. Strong proof includes an active exact-role form/ATS action, employer-controlled current role page, active application window, or employer-controlled ATS status.

Search snippets, mirrors, aggregator pages, and crawler timestamps are discovery evidence only. Newer closed/expired evidence overrides older liveness evidence.

APPLY requires a current usable exact-role route: exact form, employer ATS requisition, usable platform-native flow, or employer-controlled recruiting email instruction.

LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客, 猎聘 or similar count when the exact-role action is usable.

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

Every new Issue must have exactly one `market:*` label and one `status:*` label. Store: battlefield, company/title/location, exact ID/URL, liveness, employment evidence, plain-language work, hard requirements, AI relevance, strengths/gaps, work auth, dedupe result, exact route/blocker, and one next action.

After create, read back the Issue. **Only after successful readback may the candidate key be cached and its source watermark advanced.**

Do not use `[TOP]` title markers. Priority comes from battlefield strategy and current evidence.

---

## 15. Source-specific notes

### Singapore

FreeHire + direct employer/ATS + LinkedIn/JobStreet/Indeed gaps. Quality and work-pass plausibility matter more than volume.

### Mainland China

Rotate BOSS → official/campus → 牛客 → 51job → 智联 → 猎聘. Prefer source-native newest/updated/posted filters and persist a real watermark when available. Otherwise use a shallow fresh head + bounded terminal/durable cache.

### Malaysia

Official careers, LinkedIn, JobStreet/Hiredly, direct employers, and supplementary FreeHire. Surface only destination-quality opportunities. Persist source-native posted/updated cursor state when available.

### Telegram / DeJob

Discovery only, never authoritative proof. Independently verify exact role/JD, AI relevance, liveness, hard requirements, dedupe, and route.

---

## 16. GitHub write safety

Verify material GitHub writes by reading them back.

If a create/update times out or could have succeeded ambiguously, search/read back before retrying. Persistent ambiguity stops the write loop.

Hourly scout write scope is deliberately narrow:

- create a **new** verified APPLY/CHECK Issue after section-14 gates pass;
- update only its own bounded state object in `DISCOVERY_STATE.md`.

Scouts do not automatically modify/close/reopen existing opportunity Issues. They do not submit applications or contact employers.

---

## 17. Weekly strategy and funnel evidence

Do not force equal discovery volume across battlefields. SG is quality-first, CN may be higher-throughput after hard filters, and MY is destination-quality only.

Evaluate each battlefield using the real funnel:

`application → meaningful human/recruiter response → OA/challenge → interview → later round → offer`

Automated receipts are not meaningful progression. WAIT counts are not clean application denominators. One unusual event must not rewrite strategy; reallocation follows repeated or materially strong evidence.

---

## 18. Privacy and keep-it-small rule

Store only operational facts. Do not copy credentials, authentication material, unnecessary personal identifiers, OTPs, or private email bodies into Issues.

Do not add another tracker/framework unless repeated real failures prove the GitHub-Issues model inadequate.
