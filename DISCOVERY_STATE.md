# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~02:55 MYT`
- run type: `bounded SG/CN discovery — rotated to data platform + search/retrieval; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct employer/ATS search for data/search/software engineering, JobStreet/Indeed data-platform gap search, sponsorship-oriented search, product/international employer search`
- CN native/direct lanes tried: `Shanghai data-platform/search/recommendation discovery, campus/native role pages, direct-employer route/work-permit checks, international-employer search`
- SG coverage: `10 candidates / 8 employers / 4 source families / 1 deep-verified`
- CN coverage: `12 candidates / 10 employers / 5 source families / 1 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG: Hitachi Rail Software Engineer R1012313 is fresh on the official page (2026-09-25) with an exact Workday Apply route, but the exact JD requires 3+ years with a master's and substantial Kubernetes/datalake/ELK/Spark/DevSecOps depth; this is beyond the candidate's selective stretch despite employer-level foreign-hiring plausibility. Shopee data-infrastructure internship explicitly prioritizes candidates with current Singapore work rights/no sponsorship. Persol AI Search route resolves to MCF and is blocked. Other data-platform results were recruiter/intermediary, senior, stale, or lacked enough role-level evidence. CN: Shanghai Oriental Chip Port/XGIC Big Data Engineer is technically attractive and dated 2026-09-17, with employer email/PC application routes, but the current campus campaign targets 2027 graduates with graduation 2026-10 through 2027-12; candidate graduated earlier in 2026, so cohort is incompatible. Cognizant AP Data Engineer exact role is dated 2026-09-10, outside the <=30d gate by this run. Search/recommendation results were predominantly senior/hard 3–5+ YOE or stale. Legal Shanghai work-permit plausibility was not treated as employer willingness.`
- Gmail finalist dedupe: `not run; no candidate survived cheap freshness/cohort/fit/work-auth screening far enough to justify mailbox lookup.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. No opportunity Issue created or mutated. Discovery receipt updated only.`
- next rotation: `SWE/SDE + backend lane. SG: fresh <=30d direct ATS/product-company backend/SWE roles, especially 0–3 YOE/equivalent-experience with explicit pass/relocation or credible foreign-hiring evidence. CN: fresh <=30d direct/native backend/SDE roles at international or foreign-hiring-capable employers, with 2026-graduate-compatible cohort and employer work-permit evidence where available.`
