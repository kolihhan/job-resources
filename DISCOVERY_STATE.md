# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~06:40 MYT`
- run type: `bounded SG/CN discovery — rotated to data platform + search/retrieval; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct/employer-oriented search/retrieval and data-platform gap search; sponsorship-oriented retrieval/platform search; current aggregator evidence used only for cheap screening`
- CN native/direct lanes tried: `牛客 Shanghai search/retrieval/data-platform; direct/international-employer search; Shanghai foreign-work-permit-oriented discovery`
- SG coverage: `6 candidates / 5 employers / 3 source families / 0 deep-verified`
- CN coverage: `8 candidates / 6 employers / 3 source families / 0 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG: Momcozy current data-platform roles are Staff/Senior with hard 5–8+ YOE and explicit no-sponsorship; HUD platform result is Senior and its Sep 17 exact-role date is outside the <=30d gate by this run; other search/retrieval results lacked an employer-controlled <=30d exact role plus usable route/work-auth evidence. CN: Ctrip 2026 search/recommendation roles are explicitly ended; current Eagle Big Data is a 2027-graduate cohort (Sep 2026–Aug 2027 graduation) and not safely compatible with this 2026 graduate profile; Shopee current search role is 2027 cohort while 2026 data/ML roles are ended; Tuhu 2026 search/platform roles are ended; current PDD search roles surfaced as 3–5 YOE; Randstad Shanghai data/LLM roles had exact dates older than 30 days. Shanghai foreign-work-permit policy establishes legal pathways only and was not treated as employer willingness.`
- Gmail finalist dedupe: `not run; no new candidate survived cheap freshness/cohort/fit/work-auth/route screening far enough to justify mailbox lookup.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. No opportunity Issue created or mutated. Discovery receipt updated only.`
- next rotation: `SWE/SDE + backend. SG: fresh <=30d direct ATS junior/equivalent-experience backend/SDE roles with credible pass/relocation evidence, focusing product/B2B/fintech employers not recently covered. CN: fresh <=30d native/direct backend/SDE roles at international or demonstrably foreign-hiring-capable employers; avoid 2027-only cohorts and require employer-level permit evidence for strong promotion.`
