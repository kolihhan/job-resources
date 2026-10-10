# Discovery State

## FreeHire intake cursor

- cursor: `216`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-10 15:31 MYT` — healthy, `first_seq=1`, `last_seq=1635`; page index matches `first_seq=1 / last_seq=1635`; no cursor gap. Backlog is 1419 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1635. Fresh seq 1630–1635 inspected: 1633–1635 were obvious lane/route mismatches; 1630 was confirmed hard 5+ YOE; 1631 lacked verified exact current employer evidence; 1632 Skinlab Full-Stack is a strong fit but did not satisfy the employer-controlled freshness/route hard gate, so no Issue was created. Sequential catch-up resolved seq 214–216: 214 hard 3–5 YOE DevOps/infrastructure mismatch; 215 Kaplan Artificial Intelligence Engineer passed fit/freshness/dedupe but has one unresolved non-MCF route blocker and was promoted to CHECK #197; 216 staffing/Oracle-integration mismatch. Cursor advanced conservatively only through seq 216.`

## Current receipt

- completed run time: `2026-10-10 18:45 MYT`
- SG lanes tried: `targeted direct-ATS gap search for junior/new-grad software/backend roles on Lever/Greenhouse and employer-controlled surfaces; routine FreeHire broad coverage was not recreated`
- SG coverage: `2 distinct candidates / 2 employers / 2 source families / 0 deep-verified`
- CN lanes tried: `attempted latest CN Discovery Actions/artifact access first; artifact payload remained unavailable through the current connector, then native-source fallback searched current 牛客 plus targeted 智联/猎聘-style web surfaces for 上海/深圳 0–3 year backend/AI-application roles`
- CN coverage: `9 distinct candidates / 7 employers / 3 source families / 0 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG gap search produced no sufficiently verified new early-career direct-ATS survivor beyond already-tracked roles. CN current surfaces included 2027-only roles, internships, ended 2025/2026-campus postings, hard stack mismatches, and already-tracked Agora #195; no raw candidate passed cheap filter + dedupe into Stage 2.`
- concrete access/write issues: `CN Discovery artifact payload could not be read through the available GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a small overlap window: no new recruiting lifecycle evidence; one account contained only unrelated GitHub CI notices, LinkedIn discovery noise, user-sent recruiter outreach, and the already-reconciled Micron JR102768 rejection. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward smaller product/startup and enterprise-software direct ATS employers not well represented by FreeHire. CN should rotate away from 牛客-heavy campus results toward direct-employer, 猎聘 and 智联 social-hire 0–3 year backend/full-stack/platform roles in 深圳/上海/南京; inspect cn-raw artifact contents first if connector support becomes available.`
