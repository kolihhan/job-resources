# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-11 03:31 MYT` — healthy, `first_seq=1`, `last_seq=1716`; page index matches `first_seq=1 / last_seq=1716`; no cursor gap. Backlog is 1498 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1716. Fresh head 1701–1716 inspected; ChronoAI AI Full Stack Engineer passed Stage 2 and was promoted as #202 CHECK with sponsorship as the single blocker. Sequential catch-up advanced 216→218; seq 219 remains unresolved, so no cursor jump across it.`

## Current receipt

- completed run time: `2026-10-11 05:49 MYT`
- SG lanes tried: `industrial/software infrastructure and fresh-graduate backend/software targeted gap search across direct/ATS-oriented web surfaces plus current JobStreet-indexed gaps; routine FreeHire broad coverage was not recreated`
- SG coverage: `9 distinct candidates / 9 employers / 4 source families / 2 deep-verified`
- CN lanes tried: `attempted latest CN Discovery artifact endpoint first; connector still rejected the Actions artifact-list endpoint, then native-source fallback searched current 牛客/智联/direct-web surfaces for Shanghai/Shenzhen backend/platform/software/AI roles`
- CN coverage: `10 distinct candidates / 9 employers / 3 source families / 0 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG candidates included an explicit citizen/PR-only graduate role, an expired no-sponsorship Wise graduate role, an already-covered BlackScore role (#131 WAIT), stale/MCF-derived Wotransfer evidence without a newly verified employer-controlled route, and aggregator-only leads lacking exact employer-controlled route proof. CN current results were dominated by ended 2026-campus roles, explicit 2027-only cohorts, hard 3+ YOE/domain mismatches, or stale index surfaces; none passed Stage 2.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a two-hour overlap window and returned no new messages, hence no unreconciled recruiting lifecycle evidence. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward smaller direct-ATS B2B SaaS/healthtech/product employers and cloud/data infrastructure roles, avoiding already-covered BlackScore/Pave/Eureka/Reluvate families. CN should rotate toward current direct-employer/social-hire pages and 牛客 roles outside expired 2026-campus pools, especially Shanghai/Shenzhen/Nanjing backend/platform/full-stack; inspect cn-raw artifact first if connector support becomes available.`
