# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing.`

## Current receipt

- completed run: `2026-10-25 04:46 MYT scheduled 04 window`.
- maintenance: `Read current README/PROFILE/RULES/DISCOVERY_STATE; fully inspected ACTION/APPLY/CHECK; checked both Gmail accounts with overlap from 2026-10-24. No new mappable employer lifecycle transition. MOZAT sent application and KUKA/Swisslog receipt were already reflected in WAIT state from prior maintenance.`
- ACTION review: `Current ACTION items remain substantive under RULES: #297 Maxify has requested materials due about 2026-10-25 and still requires explicit authorization before reply; #220 has an outstanding employer-invited first-round video Q&A; #419/#468/#536/#575/#595/#599 are explicitly authorized applications with submission still pending and correctly remain ACTION until real submission evidence exists.`
- discovery: `SG targeted Agent/RAG/AI-backend gap search + CN native-source Agent/RAG/AI-application rotation; MY TOP spot-check. Search surfaced mostly 2027-only, ended/intern, existing employer-family/exact duplicates, or weak MY-TOP candidates. Huawei/牛客 466025 was rediscovered but is exact prior application #121 WAIT. No serious new survivor created.`
- coverage: `SG targeted gap search completed; CN 牛客/native search completed with multiple role queries and duplicate/cohort filtering; MY TOP spot-check completed. FreeHire broad intake was not re-scraped; cursor preserved per dedicated lane rules.`
- serious survivors: `none`.
- failures: `none on required GitHub/Gmail reads or receipt write. FreeHire historical cursor limitation remains unchanged from the preserved cursor section.`
- next rotation: `SG direct employer/ATS gap search across evaluation/retrieval/AI-native product teams; CN rotate official/campus + 51job/智联/猎聘 for 2026-compatible AI application/backend/search-retrieval roles; MY TOP small parallel pass.`
