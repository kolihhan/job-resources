# Canonical Source Routing

This is a focused execution supplement to `RULES.md` section 15. `RULES.md` remains authoritative if anything here conflicts with it.

## Goal

Increase **unique high-quality job recall per unit of scout work** by making sources complementary instead of repeatedly discovering the same employer/role through several boards.

Across source families, prioritize `PROFILE.md`'s LLM/NLP research archetypes through **bounded rotation**: retrieval/ranking + LLM/memory, KG + LLM, knowledge-enhanced language understanding, agent tool use/reasoning/planning/evaluation, and RA/RO/RE/Applied Scientist + LLM/NLP. Context/dialogue queries must directly target NLP/language-model research; rotate subsets, not every family each run. Employer ownership is a discovery-efficiency rule, not a prestige ranking. Malaysia's broader SWE pass remains a bounded secondary option under `docs/my-swe-scope.md`; preserve the market gap floors without letting generic roles crowd out the North Star.

The default should be:

> **known employer -> canonical first-party discovery owner**
>
> **unknown employer -> native/radar discovery -> resolve first-party owner once -> official source owns future discovery**

Do not create a second opportunity tracker. GitHub Issues remain the only live opportunity state. Source-routing memory is machine-efficiency state only and belongs in `DISCOVERY_STATE.md`.

---

## 1. Separate three concepts

Never conflate these:

- **Job identity** — whether two observations are the same underlying role.
- **Discovery owner** — the source the scout should routinely scan for that employer.
- **Application route** — the route the user may eventually use to apply/contact; this may differ from the discovery owner.

Example: Grab's official ATS can own discovery while a current LinkedIn Easy Apply or recruiter route remains the lower-friction application route.

`source` is provenance, **not job identity**. GOLD content classification uses employer-authored JD evidence under `PROFILE.md`, including faithful exact-role reproductions; canonical URL resolution, liveness and usable route remain separate normal verification gates.

---

## 2. Canonical discovery ownership

A verified employer-controlled careers/ATS surface may become that employer's **canonical discovery owner**.

Examples: Workday, Greenhouse, Ashby, Lever, SmartRecruiters, Feishu Hire, Moka, Beisen, or an employer's own recruiting API/portal.

Once an employer has a healthy canonical owner:

1. Routine first-party discovery for that employer goes through the owner only.
2. Do **not** independently deep-research the same employer from LinkedIn, JobStreet, Indeed, FreeHire, WhatJobs, generic search, or mirrors.
3. Lower-tier observations for that employer become **gap signals or route-enrichment signals**, not parallel discovery lanes.
4. A lower-tier observation may trigger one cheap owner check when it appears to expose a genuinely unseen requisition.
5. A transient owner failure does not erase ownership. Use a fallback for that run if needed and retry the owner later. Change ownership only when there is evidence the employer migrated portals or the old owner is no longer authoritative.

This is source routing, not source banning. Tier-2/Tier-3 sources remain useful where they add new coverage.

---

## 3. Unknown-employer promotion

When Tier 2/3 surfaces an employer that has no known canonical owner:

1. Cheap-screen the metadata first; do not resolve an official portal for obvious hard rejects.
2. For a plausible survivor, make **one bounded canonical-source resolution attempt** using the employer's own careers page / ATS / official recruiting portal.
3. If a current official source is found:
   - re-anchor verification to that official source;
   - use the official requisition ID/URL when available;
   - persist the verified source-owner mapping in bounded machine state when the employer is likely to recur (core watch target or repeated discovery).
4. If no usable official source can be established cheaply, keep the current Tier-2/Tier-3 observation eligible under normal `RULES.md` verification. Do not turn source resolution into an endless research task.

The desired learning loop is:

`aggregator finds company once -> official source discovered -> future scans go direct`

---

## 4. Job identity across sources

Cross-source safety remains necessary because fallbacks and route-enrichment will still occasionally observe the same role.

Use the cheapest stable identity in this order:

1. **`normalized employer + employer requisition/job ID`** when the ID is issued by the employer/ATS and is stable across observations.
2. Canonical employer-controlled exact-role URL after removing tracking/query noise that does not identify a distinct requisition.
3. `normalized employer | normalized title | normalized location` as a **suspected-duplicate fingerprint only**.

Important:

- Do **not** prefix a stable employer requisition ID with the discovery source. `freehire:Grab:JR123` and `workday:Grab:JR123` must collapse to the same underlying identity `grab|JR123` when `JR123` is genuinely the employer requisition ID.
- A board-specific listing ID (for example a LinkedIn/WhatJobs internal ID) is provenance only and must **not** be treated as a global employer requisition ID.
- The fallback fingerprint must not auto-merge roles when the employer may have several openings with the same title/location. Use a cheap role-page/ID comparison first.

Exact GitHub Issue-history dedupe in `RULES.md` still applies before expensive JD research.

---

## 5. When lower-tier sources are still allowed for an owned employer

A canonical owner suppresses **redundant routine discovery**, not all lower-tier use.

A Tier-2/Tier-3 observation for an owned employer is worth work only when at least one applies:

- it exposes an exact requisition/job ID not present in the latest owner delta;
- the owner is temporarily unavailable or incomplete;
- it appears to be a platform-exclusive role/recruiter posting;
- it provides a materially better human-visible application route (for example BOSS/牛客 recruiter chat, LinkedIn Easy Apply, or an employer-published recruiter contact);
- it is evidence that the employer changed ATS/careers platform.

Otherwise stop at the cheap routing gate. Do not open the full JD merely to prove a duplicate.

---

## 6. Market routing

### Singapore

Routine order:

`canonical employer ATS/portal -> targeted native gap discovery -> radar for unknown employers/gaps`

For employers with a verified ATS owner, LinkedIn/JobStreet/Indeed should mainly supply application-route enrichment or gap signals rather than parallel full discovery.

#### SG broad-platform gap floor

Do not let a Singapore scout complete from owned-employer ATS rotation alone. Before reporting no new survivors, run one bounded broad-platform gap slice.

- Rotate at least **one broad discovery family per run** among LinkedIn Jobs, JobStreet, Indeed, MyCareersFuture, recruiter/team posts, or another credible Singapore hiring surface.
- Use these surfaces to discover unknown employers, materially new requisitions, hidden AI work behind generic titles, and lower-friction routes; do not repeatedly deep-read duplicate owned-employer jobs.
- Rotate query families across Applied AI / GenAI / Agent / RAG / LLM evaluation, AI software/backend/platform, ML/NLP/search/retrieval, and MSc-compatible research-engineering terms rather than relying only on `AI Engineer`.
- MyCareersFuture may be used as discovery/evidence, but an MCF-only application route remains blocked when `RULES.md` says so.
- Re-anchor plausible survivors to a first-party employer page where one is cheaply available, then continue through normal Singapore sponsorship, employment, seniority and dedupe gates.
- Name the broad-platform source family searched in the run result so a missed gap pass is visible.

#### SG-RES lab-source gap pass

University/research-lab hiring can bypass or lag the normal ATS delta. For `SG-RES`, use a **bounded gap pass**, not a parallel tracker:

- periodically rotate through current **NUS / NTU / A*STAR / SMU / SUTD** research and AI surfaces with a bounded **full-live snapshot**, not delta-only;
- within those institutions, keep a small rotating set of high-signal labs/PIs/centres whose current work materially overlaps LLM, Agent, evaluation, NLP, retrieval, knowledge graphs or AI systems; do not create a separate tracker or crawl every lab;
- treat official lab/centre pages, PI `Join Us` pages, and active lab GitHub org/README recruiting notices as **gap signals** that can reveal a live RA/RE/Research Associate/Research Officer opening or a PI-managed route;
- when a lab signal exposes an employer requisition ID or official university/research-agency career URL, re-anchor identity, liveness and normal verification to that canonical employer route immediately;
- if an employer-published PI/lab email is genuinely the application route, it may remain the route after the normal employment, seniority, work-authorization and dedupe checks; it does not create a second opportunity state;
- for a university/research-lab role, `Full time` is schedule evidence only and must **not** be used by itself to infer permanent/regular indefinite employment. When term/duration is not stated, classify the role as `TERM_UNKNOWN` under `RULES.md`; this does not by itself block APPLY, but the term must be resolved before offer acceptance and a later confirmed fixed term must pass `RESEARCH_EXCEPTION`;
- a lab page or GitHub recruiting notice by itself does **not** waive PhD/publication, fit, work-pass or quality gates. Fixed-term research is not auto-rejected or auto-admitted: only a role that positively passes `RULES.md` section 5 as `RESEARCH_EXCEPTION` may remain an acceptable fixed-term outcome;
- when fixed-term status is visible, verify the actual PI/lab/project, substantive work, portable output path and terms needed by the research-exception gate rather than killing the candidate at metadata stage;
- do not repeatedly crawl every lab. Prioritize labs/centres with direct target overlap and stop once the official requisition/route is resolved.

The intended loop is:

`lab/PI/GitHub signal -> exact university/research requisition or verified PI-managed opening -> normal RULES pipeline -> GitHub Issue`

### Malaysia

Because MY is destination-company first, canonical source ownership should be aggressive for core/top employers. Broad boards should primarily discover strong employers outside the current watch universe and fill genuine official-source gaps.

#### MY broad-platform gap floor

Do not let a Malaysia scout complete from the destination-employer watch list alone. Before reporting no new survivors, run one bounded broad-platform gap slice.

- Rotate at least **one discovery family per run** among JobStreet, LinkedIn Jobs, Indeed, Hiredly, recruiter/team posts, or another credible Malaysia hiring surface.
- The gap slice exists to find strong employers outside the current watch universe, materially new requisitions at owned employers, and hidden high-quality SWE/AI work behind generic titles. It does **not** lower the MY TOP / destination-quality bar.
- Rotate both AI-native terms (Applied AI, Agent, GenAI, RAG, LLM, ML/NLP/evaluation) and the Malaysia-only destination-quality SWE families allowed by the current repo contract (backend, platform, data engineering, cloud/software infrastructure, software-heavy DevOps/SRE/SDET, full-stack/product engineering).
- Re-anchor plausible survivors to the employer-controlled exact role where one is cheaply available, then apply the normal Malaysia employment, seniority, stack-fit, exact-history and Gmail gates.
- Name the broad-platform source family searched in the run result so a missed gap pass is visible.

Research-lab pages may be used as bounded gap signals for destination-quality research environments (for example MIMOS or strong university/industry labs). Fixed-term MY-RES roles must clear the MY-TOP and `RULES.md` section-5 research quality/terms gates; GOLD academic roles are not penalized for fixed-term status.

### Mainland China

Official social/campus/company portals own role truth where available. BOSS/牛客 remain strategically important for recruiter reach and platform-only roles, so they are **not disabled** for an owned employer.

For a BOSS/牛客 role at an owned employer:

- if the same requisition exists officially, treat the platform observation as route enrichment;
- if it appears absent officially, perform one bounded official-gap check, then allow the platform-only role to proceed under normal verification if still credible/current.

51job/智联/猎聘 and radar sources should be more strongly suppressed for already-owned employers unless they reveal a real gap.

#### CN native-platform recall floor

Do not let a CN scout complete from first-party employer rotation alone. Before reporting no new survivors, every run must include both a bounded official-owner rotation **and** a bounded native/platform-wide fresh-head pass.

- Rotate through at least **two distinct source families per run** from BOSS直聘, 牛客招聘, 猎聘, 智联招聘, 前程无忧/51job, 脉脉/team-direct recruiting signals, or another credible China-native surface. Do not require every platform on every run; rotate them so coverage expands without turning the scout into an unbounded crawl.
- If a native platform cannot be read directly, bounded indexed/site-specific search may be used as a **discovery signal**. It does not by itself prove liveness, employment type, cohort eligibility, or application-route usability.
- Rotate query families rather than relying on generic `AI工程师`: include Agent/智能体/Agent平台, AI应用/大模型应用/AI Native, Coding Agent/AI Coding/MCP/Skills/Harness, RAG/知识库/知识图谱/NL2SQL/Data Agent, 大模型评测/Agent评测/AI质量, NLP/检索/搜索/推荐, and AI后端/算法开发/研发工程师. Preserve title-hidden AI work when team/product/snippet evidence is strong enough to justify reading the JD.
- Prioritize strong AI hubs such as Beijing, Shanghai, Shenzhen, Hangzhou and Chengdu when a platform supports location filtering, but do not hard-code discovery to only those cities.
- A native/platform candidate must still pass the normal cheap hard filters, exact Issue-history gate, cohort check, liveness/employment/work-auth verification, Gmail dedupe and route verification. Re-anchor to the employer-controlled exact role when one is found.
- After one bounded official-gap check, a credible platform-only role may continue under the normal Tier-2/Tier-3 verification path instead of being discarded solely because the employer has not indexed the role publicly.
- The scout result should name the native/platform source families actually searched so a coverage failure is observable rather than hidden behind a generic `no new roles` result.

Research-lab/team pages for strong AI-native or industrial-research groups (for example model, Agent, NLP or evaluation teams) may act as gap signals, but exact employer hiring pages/native recruiter routes should own actionable role truth. Foreign-work-permit feasibility remains a normal hard/early-triage concern; lab prestige does not override it. Fixed-term CN-RES roles still require the `RULES.md` section-5 research-exception gate.

---

## 7. Bounded source-owner state

`DISCOVERY_STATE.md` may keep a compact `canonical_sources` map as machine-efficiency state.

Persist only verified mappings that are likely to save repeated work:

- core target/watch employers; or
- employers that have appeared repeatedly and have a stable official portal.

Suggested fields per entry:

```json
{
  "company_key": "grab",
  "display_name": "Grab",
  "owner_type": "workday",
  "owner_locator": "<stable portal identifier or official careers URL>",
  "verified_on": "YYYY-MM-DD"
}
```

Rules:

- store no JD/body, candidate decision, or application state here;
- no parallel job list;
- one employer has at most one routine discovery owner at a time;
- aliases may normalize into the same `company_key`;
- a temporary fetch failure does not delete the mapping;
- replace the mapping only after verifying a real portal migration/ownership change;
- keep this bounded and useful rather than trying to catalogue the whole internet.

---

## 8. Hourly scout order

Within each market's existing bounded budget:

1. **Owned first-party delta** — rotate through canonical owners / official target-company sources.
2. **Native/direct fresh head** — search for unknown employers, platform-exclusive roles, recruiter reach, and real gaps; cheap-suppress routine duplicates for owned employers.
3. **Radar fresh head / gap recovery** — prioritize unknown employers and missing coverage; do not re-deep-research owned-company roles without a gap signal.
4. For research battlefields, use the bounded lab-source gap pass described above when the current rotation reaches a research institution/lab; once an exact requisition or verified PI-managed opening is found, return to canonical verification rather than continuing lab-page browsing.
5. Then follow the existing `RULES.md` pipeline: identity/Issue-history gate -> hard screen -> JD verification -> Gmail dedupe -> route -> durable Issue/terminal disposition -> watermark.

The market-specific recall floors above make step 2 observable: do not report `no new survivors` when the required bounded native/broad-platform gap slice for that market was skipped.

The router should reduce overlap **before** JD fetches, LLM-style reasoning, Gmail checks, and Issue work.

---

## 9. What success looks like

Do not optimize raw source count.

The intended improvements are:

- more **unique** serious roles found per run;
- higher first-party coverage for recurring/core employers;
- fewer full-JD reads for roles already visible elsewhere;
- fewer repeated cross-source duplicates reaching deep verification;
- aggregators increasingly discovering **new employers/gaps** instead of repeatedly rediscovering known employers.

No new dashboard or tracker is required to measure this. Use concrete scout evidence and the existing daily strategy review when a source-routing failure is material.