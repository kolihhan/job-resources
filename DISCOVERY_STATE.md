# Discovery State

## FreeHire intake cursor

- cursor: `213`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-10 09:31 MYT` — healthy, `first_seq=1`, `last_seq=1632`; page index matches `first_seq=1 / last_seq=1632`; no cursor gap. Backlog is 1419 events. The producer added seq 1630–1632 since the prior receipt, but the available GitHub connector truncated the tail of the current JSONL page before those rows, so those fresh events were not treated as inspected or terminally resolved.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker and index are healthy and aligned at seq 1632. Fresh seq 1630–1632 could not be safely inspected because the available GitHub connector truncated the current page before those rows; no inference was made from FreeHire metadata not actually retrieved. Sequential cursor remains 213 and no Issue/application/outreach action was performed.`

## Current receipt

- completed run time: `2026-10-10 12:48 MYT`
- SG lanes tried: `targeted gap search for fresh-graduate/junior B2B SaaS, healthtech and industrial-software roles; direct employer/current web surfaces were prioritized and routine FreeHire broad coverage was not recreated`
- SG coverage: `3 distinct candidates / 3 employers / 2 source families / 0 deep-verified`
- CN lanes tried: `latest successful CN Discovery Actions run/artifact metadata inspected first (run 37930819660, cn-raw-37930819660); raw archive contents were not readable through the available connector, so native-source fallback searched current 牛客 plus targeted 猎聘/智联-style web surfaces for 0–3 year backend/AI-application roles`
- CN coverage: `8 distinct candidates / 4 employers / 3 source families / 0 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG: current Synapxe HAP software-engineer surface was identified but no new role was promoted without completing exact eligibility/work-auth verification; other surfaced graduate leads lacked sufficiently verified exact employer routes. CN: multiple current-looking AI roles were already ended, 2027-only, internship-only, or Huawei same-employer/same-role-family duplicates; Huawei 牛客 466025 was confirmed already tracked/applied as #121 and was not resurfaced.`
- concrete access/write issues: `Latest CN Discovery run and artifact metadata are now accessible, but the cn-raw ZIP payload itself could not be read through the available GitHub connector; native-source fallback was therefore used. Both Gmail accounts were checked with a small overlap window and returned no new mail/lifecycle evidence. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct ATS product/startup and enterprise-software employers not well represented by FreeHire. CN should rotate away from Huawei/牛客-heavy results toward direct-employer, 猎聘 and 智联 0–3 year backend/full-stack/platform roles in 深圳/上海/南京; inspect cn-raw artifact contents first if connector support becomes available.`
