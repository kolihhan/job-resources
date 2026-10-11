# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 00:32 MYT` — healthy, `first_seq=1`, `last_seq=1899`; page index matches `first_seq=1 / last_seq=1899`; no cursor gap. Backlog is 1681 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1899. Feed advanced by 72 events since the prior receipt. Fresh-head page 1851–1899 was requested, but the current GitHub connector again truncated the JSONL response before the full page could be safely evaluated; no promotion was made from incomplete evidence. Cursor remains 218 because seq 219 remains unresolved; no cursor jump across unresolved history.`

## Current receipt

- completed run time: `2026-10-12 02:48 MYT`
- SG lanes tried: `targeted direct-ATS/Lever backend and AI-adjacent software gap search; routine FreeHire broad coverage was not recreated`
- SG coverage: `3 candidates / 3 employers / 2 source families / 1 deep-verified`
- CN lanes tried: `latest CN Discovery artifact endpoint attempted first but connector rejected the artifact-list endpoint; native fallback searched current 智联校园/智联 and direct-web surfaces for 2026 graduate / 0–3 YOE software, backend and AI-application roles`
- CN coverage: `7 candidates / 7 employers / 2 source families / 2 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG Portcast Backend Engineer was live on exact Lever route but hard-rejected for mandatory 5+ YOE plus senior system-ownership expectations; CSIT senior software role explicitly requires Singapore citizenship. CN results included current graduate/AI roles, but serious candidates were either cohort-mismatched (2027-only), research/doctoral-heavy, or outside the target engineering lane; no candidate cleared all fit/freshness/route gates strongly enough for promotion.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a six-hour overlap; recent recruiting mail was already-reconciled automated application receipts or platform/discovery noise, with no new HUMAN_REPLY, ACTION_REQUIRED, REJECTION_OR_CLOSURE, OA or interview evidence. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct ATS industrial software/B2B SaaS/data infrastructure and graduate-friendly product employers. CN should rotate toward BOSS/51job/direct-employer social-hire pages for Shanghai/Shenzhen/Hangzhou backend/platform/software roles, avoiding 2027-only campus lanes; inspect cn-raw artifact first if connector support becomes available.`
