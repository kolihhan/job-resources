# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 06:49 MYT`
- run type: `bounded scheduled discovery — SG fintech/cloud/B2B sponsor-positive gap + CN Shanghai/Suzhou foreign-hire rotation; <=30d freshness and exact-route gates`
- material changes: `No new Issue created or promoted. No existing opportunity Issue mutated.`
- SG platforms / lanes actually searched: `JobStreet/SEEK sponsor-keyword lane; Indeed sponsor-keyword lane; LinkedIn current role evidence; direct employer career pages/ATS; targeted public-web fintech/cloud/B2B search.`
- SG coverage: `12 candidates / 8 employers / 5 source families / 2 deep-verified`.
- SG result: `Zero survivors. MiAO AI Software Engineer, AI Agents has explicit visa sponsorship and strong fit but is exact prior application #177, so deduped. MSD Specialist, Machine Learning Engineer surfaced as fresh with apparent sponsorship evidence, but the exact official MSD requisition R380863 currently says the job is filled; rejected as dead exact route despite fresh mirrors/reposts. YouTrip backend is current but requires 4 years backend experience; Google/Agoda/ByteDance/Klook surfaced explicit no-sponsorship/right-to-work priority or seniority blockers; other board results lacked enough sponsor precision or fit.`
- CN platforms / lanes actually searched: `Shanghai/Suzhou foreign-candidate and foreign-work-permit keyword search; foreign-invested employer lane; 智联/native indexed results; direct/public employer evidence where surfaced.`
- CN coverage: `7 candidates / 6 employers / 3 source families / 0 deep-verified`.
- CN result: `Zero survivors. Search surfaced foreign-talent/work-permit policy and service pages, stale generic board collections, or non-technical vacancies rather than an exact <=30d AI/backend/SWE role with employer-specific foreign-hire willingness. 汇川 2027 campus material was cohort-incompatible for this 2026 graduate. No BOSS access-fighting or mass promotion performed.`
- route / evidence discipline exercised: `Exact employer route overrode fresh aggregator evidence for MSD; prior exact MiAO application suppressed a sponsor-positive repost; search-result dates did not override employer-controlled liveness; CN legal/area foreigner infrastructure was not treated as employer willingness.`
- access / search issues: `CN native public indexing remained weak for exact fresh foreign-candidate technical vacancies; no absence-of-market claim. No candidate justified Gmail search except MSD finalist; both Gmail accounts had no MSD/Merck application-history match.`
- external side effects: `No application, recruiter message, employer email or sponsorship inquiry sent. No opportunity Issue write performed; only this discovery receipt was updated.`
- next rotation: `SG: rotate to enterprise software, healthtech/biotech tech, developer tooling and data-platform employers with explicit pass/relocation evidence; avoid MiAO/MSD/YouTrip repeats. CN: rotate to Shanghai multinational R&D centers, international SaaS/cloud/data employers, and direct employer foreign-talent channels in Shanghai/Suzhou; require exact <=30d role plus employer-specific foreign-candidate/work-permit signal before promotion.`
