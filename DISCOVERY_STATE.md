# Discovery State

## FreeHire intake cursor

- cursor: `213`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-10 00:33 MYT` — healthy, `first_seq=1`, `last_seq=1497`, `SG 484 / CN 12`; page index matches `first_seq=1 / last_seq=1497`; no cursor gap. Bounded fresh-head inspection covered newly unseen seq 1451–1462 before sequential catch-up.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Fresh-head seq 1451–1462 was inspected first. Obvious AVP/5+ YOE, recruiter/agency, infra/DBA, customer-service and MCF-only candidates were terminally screened; FPT M01 AI Engineer, NCS Full Stack Software Engineers and YWVISION Python Backend Developer were retained for normal evidence checks but no employer-controlled exact current liveness + usable route was established in this run, so none was promoted. Sequential seq 213 (Wonderful — Deployment Strategist) is outside the primary engineering role families and reached a stable terminal reject. Cursor advanced 212→213 only; no unresolved history was crossed. No application or outreach was performed.`

## Current receipt

- completed run time: `2026-10-10 00:46 MYT`
- SG lanes tried: `targeted gap search only: direct ATS/Lever/Greenhouse junior and graduate software/backend surfaces; routine FreeHire broad coverage was not recreated`
- SG coverage: `4 distinct candidates / 4 employers / 2 source families / 0 deep-verified`
- CN lanes tried: `native-source-first 牛客 plus 智联 current/indexed Shanghai backend, full-stack and AI-application surfaces; attempted latest CN Discovery artifact inspection first, but the available GitHub connector rejected the Actions-artifact endpoint, so artifact rows were not used and discovery fell back to native sources`
- CN coverage: `8 distinct candidates / 7 employers / 2 source families / 1 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG gap results did not produce a new exact current early-career role strong enough to enter Stage 2. CN: 九方云 B端工具平台/多端全栈, 快手 Java and 亿通国际 Java were explicit 2027-only cohort mismatches; 嬴彻 L4 and 信也 2026 roles were already ended; 齐柏林 Go required 3+ years and a hard Go stack; 新毅东 J10492 was current but C++/embedded-heavy and weaker than the target lane, so no promotion. Existing CHECK #193 remains unresolved and was not duplicated.`
- concrete access/write issues: `Latest CN Discovery GitHub Actions artifact could not be inspected because the available GitHub connector rejected the artifact-list endpoint; native-source fallback was used. Both Gmail accounts were checked with a small overlap window: Sonar receipt and Elekta receipt/account-verification messages were already reconciled in Issues #183/#182; remaining mail was non-recruiting noise. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues fresh-head plus sequential catch-up from seq 213. SG gap search should rotate to direct product/ATS healthtech, B2B SaaS and industrial-software employers. CN should rotate away from the 2027-heavy 牛客 cluster toward 猎聘/51job/direct-employer 0–3 year backend/full-stack/AI-application roles in 上海/深圳/南京, and inspect the CN Discovery artifact first when connector access permits.`