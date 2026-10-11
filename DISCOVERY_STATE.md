# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-11 06:31 MYT` — healthy, `first_seq=1`, `last_seq=1805`; page index matches `first_seq=1 / last_seq=1805`; no cursor gap. Backlog is 1587 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1805. Fresh head 1801–1805 inspected; 1801–1802 are stale August agency listings and 1803–1805 are MCF-only discovery routes (two also agency/recruiter listings), so none passed the promotion gate. Cursor remains 218 because seq 219 is still unresolved; no cursor jump across unresolved history.`

## Current receipt

- completed run time: `2026-10-11 08:48 MYT`
- SG lanes tried: `smaller product/healthtech and cloud/data/backend gap search across direct employer/ATS-oriented web surfaces plus current fresh-graduate indexes; routine FreeHire broad coverage was not recreated`
- SG coverage: `10 distinct candidates / 10 employers / 4 source families / 2 deep-verified`
- CN lanes tried: `attempted latest CN Discovery artifact endpoint first; connector again rejected the Actions artifact-list endpoint, then native-source fallback searched current 牛客/direct-web surfaces for Shanghai/Shenzhen backend/platform/full-stack/AI roles outside familiar employer families`
- CN coverage: `15 distinct candidates / 12 employers / 3 source families / 1 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG current results included a Doctor Anywhere junior backend role whose exact current board now says no longer accepting applications, a DXC junior Java role with Java mandatory plus security-clearance/site-access eligibility, stale/aggregator-only leads, and senior/lead roles; none cleared all fit/freshness/route gates. CN results were dominated by ended 2026-campus listings, explicit 2027-only cohorts, cohort windows excluding a pre-September-2026 graduate, hard stack/domain mismatches, or ended role surfaces; none cleared Stage 2.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a four-hour overlap: lihhanko526 had no new mail; lihhanko3 had one JobStreet AI-engineer alert classified DISCOVERY_NOISE, with no lifecycle state change. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct ATS fintech/enterprise SaaS/data-platform employers and fresh graduate backend/platform roles, avoiding already-covered BlackScore/Pave/Eureka/Reluvate/ChronoAI families. CN should rotate toward current direct-employer social-hire pages, 智联/51job and 牛客社招 for Shanghai/Shenzhen/Nanjing backend/platform/full-stack, avoiding expired campus pools; inspect cn-raw artifact first if connector support becomes available.`
