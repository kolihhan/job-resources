# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 00:32 MYT` — healthy, `first_seq=1`, `last_seq=1899`; page index matches `first_seq=1 / last_seq=1899`; no cursor gap. Backlog is 1681 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1899. Feed advanced by 72 events since the prior receipt. Fresh-head page 1851–1899 was requested, but the current GitHub connector again truncated the JSONL response before the full page could be safely evaluated; no promotion was made from incomplete evidence. Cursor remains 218 because seq 219 remains unresolved; no cursor jump across unresolved history.`

## Current receipt

- completed run time: `2026-10-11 22:54 MYT`
- SG lanes tried: `targeted direct-ATS healthtech/cloud-infrastructure/smaller-product backend and software searches; routine FreeHire broad coverage was not recreated`
- SG coverage: `1 candidate / 1 employer / 3 source families / 0 deep-verified`
- CN lanes tried: `attempted latest CN Discovery artifact endpoint first; connector rejected the Actions artifact-list endpoint, then native-source fallback searched current 51job/智联/牛客/direct-web surfaces for Shanghai/Shenzhen/Nanjing backend/full-stack/platform/AI roles`
- CN coverage: `12 candidates / 11 employers / 4 source families / 1 deep-verified`
- serious-survivor Issues created/updated: `#224 中芯国际 — AI全栈工程师 (J13244) → CHECK`
- concrete filters / regressions exercised: `SG targeted gap search surfaced only an expired Senior Backend role and no candidate clearing the cheap fit/freshness gate. CN native search surfaced multiple current early-career-looking roles; many were hard 3–10 YOE, contractor/agency, stale campus postings, or lacked sufficient exact-role evidence. J13244 was deep-verified against a current exact 51job route plus current role detail, then GitHub and both Gmail accounts were deduped; only foreign-work-permit employer willingness remains unresolved.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a six-hour overlap. SimplifyNext sent a data-retention consent extension after its prior rejection; classified PLATFORM_SIGNAL/non-progression and existing rejected #96 was not reopened. Other recent recruiting mail was already-reconciled application receipts/interview evidence or job-alert DISCOVERY_NOISE. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct ATS industrial software/B2B SaaS/data infrastructure and fresh-graduate employer pages not already represented in Issues. CN should rotate toward BOSS/智联/direct-employer social-hire pages for Shanghai/Shenzhen/Hangzhou backend/platform/software roles, with 51job AI/full-stack results used only when exact role evidence remains current; inspect cn-raw artifact first if connector support becomes available.`
