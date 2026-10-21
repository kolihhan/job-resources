# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing. No serious survivor reached finalist Gmail dedupe and no Issue was created. No application or employer contact was performed.`

## Current receipt

- completed run time: `2026-10-22 ~00:55 MYT`
- run type: `scheduled maintenance + SG-gap/CN-native discovery — data platform + search/retrieval rotation`
- maintenance: `Read current README.md, PROFILE.md, RULES.md and DISCOVERY_STATE.md first; fully inspected current ACTION/APPLY/CHECK and searched both Gmail accounts with a recent lifecycle overlap before discovery. Re-evaluated ACTION under current RULES meaning: #184 Ant remains ACTION for the confirmed 2026-10-23 interview; #220 杭州赢云 remains ACTION for the employer-requested first-round video interview. Recent receipts for Sea, Nintex, WATI, Coca-Cola, NUS and Intel JR0285837 map to existing WAIT history and did not create duplicate live opportunities. No new rejection, OA, interview, recruiter reply or exact-role receipt required a GitHub lifecycle change.`
- SG gap lanes tried: `Targeted direct/current data-platform, search/retrieval and RAG-infrastructure gaps rather than routine FreeHire/board recreation. ByteDance Libra Platform 2026 and Data Management Suite/Data Ingestion 2026 are explicitly no longer accepting applications. TikTok Search PhD role is cohort-incompatible; other TikTok data-warehouse mirrors were stale/expired or carried Singapore-work-right-only secondary evidence. No new SG survivor cleared the full gate.`
- CN native/direct lanes tried: `Rotated 牛客/current-web plus BOSS/Zhaopin-oriented search around 2026-eligible retrieval, RAG data engineering, search and ranking. 群核科技 2026 DevOps/AI role is explicitly ended. 广联达 AI数据开发工程师 is technically excellent but explicitly 27届; 中国电子云 AI Coding is also 2027 campus. Other search/retrieval hits were stale, closed, cohort-incompatible or already represented by current GitHub opportunities. No new CN survivor cleared the full gate.`
- SG coverage: `6 candidates / 2 employers / 3 source families / 1 deep-verified`
- CN coverage: `8 candidates / 6 employers / 4 source families / 1 deep-verified`
- serious survivors: `none`
- Gmail finalist/lifecycle reconciliation: `Both connected Gmail accounts completed recent lifecycle overlap search before discovery. No discovery finalist reached CHECK/APPLY promotion, so no additional exact-ID finalist Gmail dedupe was required.`
- access/search failures: `No required Gmail/GitHub access or write failure. Normal discovery did not rescan FreeHire, per RULES. Some SG data-platform/search results were third-party mirrors; explicit closure/cohort evidence prevented promotion without unnecessary deep verification.`
- external side effects: `No application, form, assessment, recruiter message or employer contact was sent by this run.`
- next rotation: `SWE/SDE + backend. SG: targeted direct-employer/ATS gaps outside routine FreeHire coverage, especially junior product/backend roles at strong engineering employers. CN: rotate BOSS/牛客/智联/official-direct/51job/猎聘 around 2026-eligible SWE/SDE/backend and AI-backend roles, expanding beyond familiar big-tech duplicates.`
