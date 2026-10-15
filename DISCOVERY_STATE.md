# Discovery State

## FreeHire intake cursor

- cursor: `234`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-15 15:24 MYT` — healthy, `first_seq=1`, `last_seq=2895`; page index matches `first_seq=1 / last_seq=2895`; no cursor gap. Backlog is 2661 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2895; latest delta added 17 NEW and 0 changed events across MY/SG/CN. Bounded fresh-head screened the newly-added tail; no serious survivor reached Stage 2, so no Gmail finalist dedupe or Issue write was warranted. Historical catch-up is no longer connector-blocked at seq 219: seq 219–234 were safely exposed and reached stable terminal results under RULES, advancing the contiguous cursor from 218 to 234. Catch-up stopped conservatively before seq 235 rather than inferring later records. Cursor is 234.`

## Current receipt

- completed run time: `2026-10-15 ~16:45 MYT`
- run type: `scheduled maintenance + bounded SG-gap/CN-native discovery — SWE/backend rotation`
- maintenance: `Fully inspected current ACTION/APPLY/CHECK. #184 Ant International remains ACTION for coding assessment + confirmed 2026-10-23 interview; #220 remains ACTION for a real interview invitation; #304 remains ACTION for a time-bounded OA due 2026-10-20; #275 HUD remains CHECK for the existing application-allocation decision. Both Gmail lifecycle overlap searches completed. New Micron Workday closure for DATA SCIENTIST JR100232 was reconciled into closed family history #100, bringing that family to five recent rejected/closed requisitions. Singtel also confirmed Data & AI Operations Engineer #AIDA is no longer available; no matching live Issue existed, so this remains application-history evidence rather than creating a dead-role Issue.`
- SG gap lanes tried: `direct employer/ATS + targeted current web gaps for SWE/backend and graduate engineering. ByteDance 2026 backend graduate search result is explicitly no longer accepting. NCS Nov-2026/Jan-2027 AI Software Engineer remains current on official SmartRecruiters but is an exact previously applied/rejected role already recorded in #94, so suppressed. Singtel Fusion Poly Graduate is a polytechnic-specific programme and not a suitable master's-graduate lane. No routine FreeHire rescan performed.`
- CN native/direct lanes tried: `牛客 + 智联/51job indexed gaps + direct/current web for 2026/recent-graduate backend/SDE. ByteDance settlement/backend and Douyin-life-service 2026 listings are marked ended; Shopee Shanghai 2026 backend is ended; 招银网络 2026 backend is ended; 神策 2026 backend is ended. 北森 J14527 produced contradictory 牛客 surfaces (one internship-style page exposing an apply window while the campus exact-role page is marked ended), so liveness was not strengthened by the weaker surface and it was not promoted.`
- SG coverage: `4 candidates / 3 employers / 3 source families / 0 deep-verified`
- CN coverage: `6 candidates / 6 employers / 4 source families / 0 deep-verified`
- serious survivors: `none`
- Gmail finalist dedupe: `Both recent lifecycle overlap searches completed. No new finalist required exact-ID Gmail dedupe; NCS was suppressed at GitHub cheap-dedupe because #94 is the exact same programme/application history.`
- access/search failures: `No required Gmail/GitHub access or write failure. CN native indexing remains uneven; contradictory or ended 牛客 surfaces were not promoted into liveness.`
- external side effects: `No application, recruiter message, employer contact or assessment submission sent.`
- next rotation: `platform/infra/systems + ML systems/AI infra/inference/evaluation. SG: direct employer/ATS and smaller product/cloud/data-infra gaps outside already-resolved ByteDance/NCS/Singtel families. CN: rotate BOSS/猎聘/direct-employer and fresh 0-3 YOE platform/infra/ML-systems roles, changing employer cluster away from ended 2026 campus pages.`