# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing. No serious survivor reached finalist Gmail dedupe and no Issue was created. No application or employer contact was performed.`

## Current receipt

- completed run time: `2026-10-22 ~04:55 MYT`
- run type: `scheduled maintenance + SG-gap/CN-native discovery — SWE/SDE + backend rotation`
- maintenance: `Read current README.md, PROFILE.md, RULES.md and DISCOVERY_STATE.md first; fully inspected current ACTION/APPLY/CHECK and searched both Gmail accounts with a recent lifecycle overlap before discovery. Re-evaluated ACTION under current RULES meaning: #184 Ant remains ACTION for the confirmed 2026-10-23 interview; #220 杭州赢云 remains ACTION for the employer-requested first-round video interview. Recent Sea, Nintex, Intel, MetLife, WATI, NUS, Coca-Cola and zCloak application evidence is already represented in GitHub history; zCloak FDE is explicitly canonicalized to #225 with duplicate outreach suppressed. No new rejection, OA, interview, recruiter reply or exact-role receipt required a lifecycle write.`
- SG gap lanes tried: `Targeted current junior/graduate product/backend and direct-employer/ATS gaps outside routine FreeHire coverage. Singtel/NCS Fusion is a work-study/polytechnic degree programme rather than the target permanent graduate lane; Grab hit was internship-only; ByteDance ByteRec 2026 backend is explicitly no longer accepting applications; remaining broad current surfaces did not provide a new serious survivor with verified current exact route and better fit than existing opportunities.`
- CN native/direct lanes tried: `Rotated 牛客/current-web and Zhaopin-oriented SWE/SDE/backend/AI-backend searches. Huawei 2026 backend/software listings surfaced as ended; ByteDance/PDD 2026 backend listings surfaced as ended; Huawei Cloud's current Data+AI backend listing is 2027-only. 北森 J14527 remains a current-looking 2026 backend surface but is already canonical #117 WAIT from the user's confirmed application, so it was deduped rather than recreated. No new CN survivor cleared the full gate.`
- SG coverage: `6 candidates / 5 employers / 3 source families / 0 deep-verified`
- CN coverage: `9 candidates / 5 employers / 3 source families / 1 deep-verified`
- serious survivors: `none`
- Gmail finalist/lifecycle reconciliation: `Both connected Gmail accounts completed recent lifecycle overlap search before discovery. No new discovery finalist reached CHECK/APPLY promotion, so no additional exact-ID finalist Gmail dedupe was required.`
- access/search failures: `No required Gmail/GitHub access or write failure. Normal discovery did not rescan FreeHire, per RULES. Search coverage was intentionally targeted rather than a generic SG board sweep.`
- external side effects: `No application, form, assessment, recruiter message or employer contact was sent by this run.`
- next rotation: `platform/infra/systems + ML systems/AI infra/inference/evaluation. SG: targeted direct-employer/ATS gaps outside routine FreeHire, emphasizing junior platform/reliability/AI-platform roles. CN: rotate BOSS/牛客/智联/official-direct/51job/猎聘 around 2026-eligible platform, inference, evaluation and AI-infrastructure roles, expanding beyond familiar big-tech duplicates.`
