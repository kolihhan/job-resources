# Discovery State

## FreeHire intake cursor

- cursor: `382`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-17 18:11 MYT` — worker healthy, `first_seq=1`, `last_seq=5897`; page index agrees on the current feed range; no cursor gap. Worker reports the latest delta run (`new=2356`, `changed=0`) completed at `2026-10-17T06:55:17Z`.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 5897 with no producer delta. Fresh-head page remains the same bounded head previously inspected; no new head event required promotion. Historical catch-up processed seq 382 (JPMorganChase Software Engineer III) as terminal after current verification showed the Software Engineer III family requires 3+ years applied experience and seasoned/mid-level scope, with role-specific Java/full-stack or payments/trading requirements; GitHub had no exact prior Software Engineer III Issue. Contiguous cursor advanced 381→382 and was written for read-back.`

## Current receipt

- completed run time: `2026-10-17 ~16:55 MYT`
- run type: `scheduled maintenance + bounded SG-gap/CN-native discovery — SWE/SDE + backend rotation`
- maintenance: `Read current README.md, PROFILE.md, RULES.md and DISCOVERY_STATE.md first; fully inspected current ACTION/APPLY/CHECK queues and checked recent lifecycle evidence in both Gmail accounts before discovery. #90 OPPO, #184 Ant and #304 安利 still satisfy ACTION semantics because each has a genuine employer-requested action/deadline or confirmed interview. Recent direct CN applications visible in Gmail were already reconciled into GitHub WAIT Issues (#345–#352 and updated #187); no new lifecycle message required another transition in this overlap window.`
- SG gap lanes tried: `Targeted direct-ATS/careers and selective current-web gaps around early-career SWE/backend at product/fintech/startup employers, without routine FreeHire rescan. Wise graduate SWE is removed. A Crypto.com Singapore Software Developer - Early Career lead surfaced through an old indexed ATS list, but the exact Lever requisition now returns 404, so it failed current-liveness/route verification. Other surfaced SG results were senior, stale, internship-only, or generic board noise and did not survive the cheap screen.`
- CN native/direct lanes tried: `Rotated 牛客/campus-indexed plus direct/current web discovery around 2026 SWE/backend. 众安 2026 backend is explicitly ended. 京东 2026 LLM-backend mirror is ended. PingCAP 2026 campus window is historical/ended. 新时达 surfaced conflicting 2026-era university material, while the current employer recruiting cycle is 2027-only (2026-09 to 2027-07 graduates), so a 2026 graduate is not currently eligible. 神州信息 2026 campus material was historical rather than a clean current exact role. No candidate survived to finalist verification.`
- SG coverage: `6 candidates / 6 employers / 3 source families / 1 deep-verified`
- CN coverage: `8 candidates / 6 employers / 4 source families / 1 deep-verified`
- serious survivors: `none`
- Gmail finalist/lifecycle reconciliation: `Both Gmail accounts completed recent lifecycle overlap search before discovery. Recent CN direct-application sent mail maps to existing WAIT Issues and does not create new state changes. No new OA/interview/recruiter progression or explicit rejection requiring a live Issue transition was found. No discovery candidate reached the finalist gate requiring new exact-ID Gmail dedupe.`
- access/search failures: `No required Gmail/GitHub access or write failure. Some CN native surfaces remain uneven/index-dependent; multiple source/employer lanes were varied. Crypto.com exact Lever route returned 404 and was rejected rather than guessed live.`
- external side effects: `No application, feedback form, recruiter message, employer contact or assessment submission was sent by this maintenance/discovery run.`
- next rotation: `platform/infra/systems + ML systems/AI infra/inference/evaluation. SG: targeted direct employer/ATS gaps among product/cloud/data/AI-platform employers not recently covered; FreeHire remains dedicated-lane. CN: rotate BOSS/official-direct/牛客/51job/智联/猎聘 around 2026-eligible platform, infra, inference and evaluation roles, avoiding repeated ended campus mirrors.`
