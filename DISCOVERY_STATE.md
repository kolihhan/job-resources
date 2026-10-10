# Discovery State

## FreeHire intake cursor

- cursor: `216`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-10 15:31 MYT` — healthy, `first_seq=1`, `last_seq=1635`; page index matches `first_seq=1 / last_seq=1635`; no cursor gap. Backlog is 1419 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1635. Fresh seq 1630–1635 inspected: 1633–1635 were obvious lane/route mismatches; 1630 was confirmed hard 5+ YOE; 1631 lacked verified exact current employer evidence; 1632 Skinlab Full-Stack is a strong fit but did not satisfy the employer-controlled freshness/route hard gate, so no Issue was created. Sequential catch-up resolved seq 214–216: 214 hard 3–5 YOE DevOps/infrastructure mismatch; 215 Kaplan Artificial Intelligence Engineer passed fit/freshness/dedupe but has one unresolved non-MCF route blocker and was promoted to CHECK #197; 216 staffing/Oracle-integration mismatch. Cursor advanced conservatively only through seq 216.`

## Current receipt

- completed run time: `2026-10-10 20:51 MYT`
- SG lanes tried: `targeted smaller-product/startup and enterprise-software direct-employer gap search; routine FreeHire broad coverage was not recreated`
- SG coverage: `5 distinct candidates / 5 employers / 2 source families / 1 deep-verified`
- CN lanes tried: `attempted latest CN Discovery artifact endpoint first; connector could not expose the Actions artifact listing, then native-source fallback searched current 猎聘/智联/51job-style and direct web surfaces for 深圳/上海/南京 0–3 year backend/full-stack/AI-application roles`
- CN coverage: `7 distinct candidates / 7 employers / 3 source families / 0 deep-verified`
- serious-survivor Issues created/updated: `#200 Reluvate Backend Engineer (APPLY)`
- concrete filters / regressions exercised: `SG direct-employer search found Reluvate's current employer-controlled Backend Engineer role with explicit email application route and no hard YOE requirement; GitHub and both Gmail accounts showed no prior Reluvate history. Other SG results were board-only, senior, or insufficiently verified. CN results were mostly stale month-index pages, hard 2–3+ year requirements, internships, or insufficient current exact employer-controlled role evidence; none passed into Stage 2.`
- concrete access/write issues: `CN Discovery artifact listing was not available through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a small overlap window: no new unreconciled recruiting lifecycle evidence; Michael Page and LinkedIn alerts were DISCOVERY_NOISE, GitHub CI notices unrelated, and the TikTok rejection had already been reconciled as closed #199. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward healthtech/industrial/B2B SaaS direct ATS employers and graduate software roles not covered well by FreeHire. CN should rotate toward direct-employer and current social-hire pages for Shanghai/Shenzhen/Nanjing backend/platform/full-stack roles, with less reliance on stale 51job month indexes; inspect cn-raw artifact first if connector support becomes available.`
