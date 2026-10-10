# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-11 03:31 MYT` — healthy, `first_seq=1`, `last_seq=1716`; page index matches `first_seq=1 / last_seq=1716`; no cursor gap. Backlog is 1498 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1716. Fresh head 1701–1716 inspected; ChronoAI AI Full Stack Engineer passed Stage 2 and was promoted as #202 CHECK with sponsorship as the single blocker. Sequential catch-up advanced 216→218; seq 219 remains unresolved, so no cursor jump across it.`

## Current receipt

- completed run time: `2026-10-11 02:53 MYT`
- SG lanes tried: `healthtech/industrial/B2B SaaS and graduate-software targeted gap search; routine FreeHire broad coverage was not recreated`
- SG coverage: `6 distinct candidates / 6 employers / 3 source families / 0 deep-verified`
- CN lanes tried: `attempted latest CN Discovery artifact endpoint first; connector rejected the Actions artifact-list endpoint, then native-source fallback searched current 牛客/智联/51job-style/direct web surfaces for 上海/深圳/南京 graduate backend/software/AI roles`
- CN coverage: `8 distinct candidates / 8 employers / 4 source families / 0 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG results were cohort-incompatible, MCF-only/aggregator-only, senior, stale, or lacked current exact employer-controlled route evidence; Synapxe Jan/Feb 2027 explicitly targets Dec-2026 graduates, while the candidate is already a 2026 graduate. CN results included 2026-campus mirrors that were stale/ended or not currently launchable, hard 3+ YOE roles, and generic index pages without exact current role-level evidence; none passed Stage 2.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a small overlap window: no new unreconciled recruiting lifecycle evidence; PDD password-reset mail is account activity, Indeed/LinkedIn alerts are DISCOVERY_NOISE, NUSX receipts were already reconciled as #201 WAIT, and unrelated GitHub CI notices were ignored. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward industrial software, cloud/data infrastructure and smaller direct-ATS product employers with 0–3 YOE roles. CN should rotate toward direct-employer/current campus or social-hire pages for Shanghai/Shenzhen/Nanjing backend/platform/full-stack roles and avoid stale month-index pages; inspect cn-raw artifact first if connector support becomes available.`
