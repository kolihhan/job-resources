# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing.`

## Current receipt

- completed run: `2026-10-25 08:49 MYT scheduled 08 window`.
- maintenance: `Read current README/PROFILE/RULES/DISCOVERY_STATE; fully inspected ACTION/APPLY/CHECK; checked both Gmail accounts with overlap from 2026-10-24. No new mappable employer lifecycle transition. Reconciled nine newly-opened APPLY Issues (#652-#660) that had been created under a non-source-of-truth broad-throughput rationale: all were closed/skipped because they are generic SWE/systems/test or lower-level AI infrastructure roles outside the current PROFILE/RULES direction.`
- ACTION review: `#297 Maxify remains substantive with requested materials due about 2026-10-25 and still requires explicit authorization before reply; #220 remains an outstanding employer-invited first-round video Q&A; #419/#468/#536/#575/#595/#599 remain explicitly authorized applications with submission pending and satisfy ACTION until real submission evidence exists.`
- discovery: `SG direct/targeted evaluation + Agent/RAG gap search; CN official/campus + 51job/智联/猎聘-oriented web/native-source rotation; MY TOP spot-check. Shopee Agent Reliability & Evaluation is highly aligned but hard-requires 1 year full-time industry production LLM-Agent experience, so rejected. Manus Agent Evaluation is strongly aligned but the candidate already applied to two materially adjacent Manus Agent roles (AI Agent Engineer and Agent Harness Engineer); suppressed rather than adding a third same-employer application. Other surfaced items were MCF-only, senior/mature, contract/intern, 2027-only, weak-source, or direction mismatches. No serious new survivor created.`
- coverage: `SG evaluation/retrieval/Agent gap search completed with non-MCF route/seniority screening; CN official/campus plus 51job/智联/猎聘 keyword rotation completed; MY TOP small spot-check completed. FreeHire broad intake was not re-scraped; cursor preserved per dedicated-lane rules.`
- serious survivors: `none`.
- failures: `none on required GitHub/Gmail reads or receipt write. FreeHire historical cursor limitation remains unchanged from the preserved cursor section.`
- next rotation: `SG direct employer/ATS gap search across AI-native product/backend and RAG application teams; CN rotate BOSS + official/campus + 牛客 for 2026-compatible Agent/RAG/evaluation roles; MY TOP small parallel pass.`
