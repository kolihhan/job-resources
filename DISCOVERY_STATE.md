# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~08:55 MYT`
- run type: `bounded SG/CN discovery — rotated to platform/infra/systems + ML systems/AI infra; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct/employer platform/data-platform/AI-infra search; sponsorship-oriented JobStreet/Indeed gap search; current Workday/ATS role follow-up`
- CN native/direct lanes tried: `牛客/current campus AI-infra search; direct/campus Shanghai ML-systems and platform search; international-employer Shanghai infra search`
- SG coverage: `8 candidates / 7 employers / 4 source families / 1 deep-verified`
- CN coverage: `7 candidates / 5 employers / 4 source families / 1 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG: Visa REF088915W Data Engineer is fresh (exact employer Workday says Posted 3 Days Ago) and technically strong across Python/SQL, data platform, RAG/vector retrieval, agents, evaluation and observability, but Visa already has active CHECK #283 for the materially stronger Applied AI role; same-employer active-CHECK rule therefore suppresses a second weaker speculative Visa pursuit. Clera platform role is closed; Google GenAI FDE explicitly prioritizes existing SG work rights/no sponsorship; ByteDance cloud-platform result likewise states no visa sponsorship; recruiter/bodyshop and senior platform results were rejected cheaply. CN: PDD AI Infra is strong technically but its published cohort requires degree obtained 2026.9–2027.8, incompatible with the candidate's 2026 graduation timing; Huawei 2026 AI software/compute roles surfaced as ended, while the live AI Infra result is 2027 cohort; Intel/SAP/AMD results were internships or expired. No CN candidate combined current <=30d role evidence, compatible cohort/full-time status, and enough foreign-work-permit/employer-willingness evidence to justify promotion.`
- Gmail finalist dedupe: `not run; no candidate survived final promotion gate. GitHub exact req/title dedupe was run for Visa REF088915W and found no exact prior Issue, but employer saturation against active Visa #283 prevented promotion.`
- external side effects: `No Issue created/updated; no application, recruiter message, employer contact or sponsorship inquiry sent. Receipt updated only.`
- next rotation: `data platform + search/retrieval. SG: direct ATS/employer search outside currently saturated Visa/HUD/Clera/Plaud/UOBKH; prioritize early-career search/data/platform roles with explicit sponsorship-compatible forms or relocation/pass evidence. CN: native/direct search-retrieval/data-platform roles with compatible 2026 graduate windows; prioritize Shanghai/international employers and exact foreign-candidate/work-permit evidence.`
