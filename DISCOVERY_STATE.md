# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~07:50 MYT`
- run type: `bounded SG/CN discovery — rotated to SWE/SDE + backend; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct/employer SWE/backend gap search; sponsorship-oriented Indeed/JobStreet gap search; Google current early-career SWE family checked directly`
- CN native/direct lanes tried: `direct international-employer backend/SDE search; 2026 campus/new-grad discovery; Shanghai foreign-hire plausibility follow-up`
- SG coverage: `9 candidates / 8 employers / 3 source families / 0 deep-verified`
- CN coverage: `5 candidates / 4 employers / 3 source families / 1 deep-verified`
- serious survivors: `#302 WeRide — New Grads 2026 Algorithm Software Engineer (CHECK)`
- notable rejects/dedupes: `SG: current Google early-career SWE roles (Wallet Multimodal Intelligence, Ads, Content Safety and Payments/Growth) explicitly prioritize candidates with current Singapore work rights who do not require visa sponsorship, so they are BLOCKED despite strong technical fit; Klook/Shopee graduate results likewise state no-sponsorship preference or incompatible 2027 cohort; recruiter/bodyshop and hard-senior backend results were rejected cheaply. CN: Xsolla Shanghai backend openings are Senior/Middle-Senior; Randstad LLM backend role is dated 2026-09-03 and fails <=30d. WeRide exact 2026 new-grad Lever role is live and directly usable, but the exact page exposes no role-specific posted/updated date, so freshness remains UNPROVEN and it stays CHECK; employer-specific foreign-work-permit willingness is also UNKNOWN.`
- Gmail finalist dedupe: `not run; #302 remains CHECK because freshness/work-auth are unresolved and GitHub exact-role dedupe found no prior Issue.`
- external side effects: `Created #302 CHECK and read it back. No application, recruiter message, employer contact or sponsorship inquiry sent.`
- next rotation: `platform/infra/systems + ML systems/AI infra. SG: direct ATS roles outside Google/Shopee/Klook with explicit pass/relocation evidence or credible sponsorship-compatible forms. CN: native/direct platform/infra/ML-systems roles at international or demonstrably foreign-hiring-capable employers; prioritize exact employer dates <=30d and foreign-graduate/work-permit evidence.`
