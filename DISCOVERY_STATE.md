# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 06:31 MYT` — healthy, `first_seq=1`, `last_seq=2033`; page index matches `first_seq=1 / last_seq=2033`; no cursor gap. Backlog is 1815 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2033. Feed advanced by 58 events since the prior receipt. Recent unseen page 2001–2033 was requested first; visible events were old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-12 08:46 MYT`
- SG lanes tried: `targeted graduate/backend/direct-employer gap search plus current JobStreet gap evidence; routine FreeHire broad coverage was not recreated`
- SG coverage: `3 candidates / 3 employers / 2 source families / 1 deep-verified`
- CN lanes tried: `latest CN Discovery artifact endpoint attempted first but connector rejected the artifact-list endpoint; native fallback rotated across Shenzhen/Hangzhou/Shanghai Python/backend/AI-application surfaces and direct/campus evidence`
- CN coverage: `8 candidates / 7 employers / 4 source families / 3 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG Shopee 2026 graduate backend evidence explicitly prioritizes candidates with existing Singapore work rights/no visa sponsorship; other SG gap hits were senior/consulting-style or lacked a sufficiently strong exact current employer route. CN Randstad Shenzhen Agent roles require 3+ years and technical leadership; several 2026 graduate roles are already closed. Shanghai东方芯港 application/AI roles are strong technical fits, but the current 2027 campus campaign explicitly limits graduation to 2026-10 through 2027-12, which does not safely establish cohort eligibility for this candidate, so no promotion.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a three-hour overlap: one JobStreet AI Engineer alert was DISCOVERY_NOISE and the other account had no new mail; no new HUMAN_REPLY, ACTION_REQUIRED, REJECTION_OR_CLOSURE, APPLICATION_RECEIPT requiring reconciliation, OA or interview evidence was found. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct ATS B2B SaaS/data infrastructure/industrial software employers not well represented by the feed. CN should rotate toward BOSS/direct-employer Shenzhen/Hangzhou backend/platform plus Shanghai non-2027-only direct-employer AI application roles; inspect cn-raw artifact first if connector support becomes available.`
