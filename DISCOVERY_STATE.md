# Discovery State

## FreeHire intake cursor

- cursor: `213`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-10 09:31 MYT` — healthy, `first_seq=1`, `last_seq=1632`; page index matches `first_seq=1 / last_seq=1632`; no cursor gap. Backlog is 1419 events. The producer added seq 1630–1632 since the prior receipt, but the available GitHub connector truncated the tail of the current JSONL page before those rows, so those fresh events were not treated as inspected or terminally resolved.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker and index are healthy and aligned at seq 1632. Fresh seq 1630–1632 could not be safely inspected because the available GitHub connector truncated the current page before those rows; no inference was made from FreeHire metadata not actually retrieved. Sequential cursor remains 213 and no Issue/application/outreach action was performed.`

## Current receipt

- completed run time: `2026-10-10 10:53 MYT`
- SG lanes tried: `targeted fresh-graduate/junior software-engineering gap search across direct/employer-site surfaces plus current JobStreet, Indeed, LinkedIn and Glassdoor discovery surfaces; routine FreeHire broad coverage was not recreated`
- SG coverage: `8 distinct candidates / 8 employers / 4 source families / 0 deep-verified`
- CN lanes tried: `牛客 current Shanghai campus/backend/platform/AI-application roles; latest CN Discovery artifact inspection was attempted first but the available GitHub connector again rejected the Actions workflow/artifact endpoint, so native-source fallback was used`
- CN coverage: `10 distinct candidates / 8 employers / 1 source family / 1 deep-verified`
- serious-survivor Issues created/updated: `#195 声网 Agora — 校招-云平台开发工程师 (CHECK)`
- concrete filters / regressions exercised: `SG: surfaced fresh-graduate roles were either recruiter/staffing/consulting-like, citizenship-blocked, 2027-only, weak-fit/domain-heavy, or lacked an independently verified exact employer-controlled route; none cleared Stage 2. CN: current 牛客 results included multiple 2027-only cohort mismatches and ended/old roles. 声网 cloud-platform role is live with exact 牛客 apply action and is materially distinct from existing #191, but its campus-recruiting cohort eligibility is not stated; #195 remains CHECK rather than guessing eligibility.`
- concrete access/write issues: `Latest CN Discovery GitHub Actions artifact could not be inspected because the available GitHub connector rejected the workflow/artifact endpoint; native-source fallback was used. Both Gmail accounts were checked with a small overlap window: one had no new mail; the other contained LinkedIn/JobStreet alerts and unrelated newsletter content only, classified DISCOVERY_NOISE, with no lifecycle state change. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct product/ATS B2B SaaS, healthtech and industrial-software employers rather than generic graduate-board surfaces. CN should rotate away from this 牛客-heavy Shanghai pass to 猎聘/智联/direct-employer 0–3 year backend/full-stack/AI-application roles in 深圳/南京/上海, and inspect the CN Discovery artifact first when connector access permits.`
