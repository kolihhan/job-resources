# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-15 05:55 MYT` — healthy, `first_seq=1`, `last_seq=2737`; page index matches `first_seq=1 / last_seq=2737`; no cursor gap. Backlog is 2519 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2737; latest full run added 55 NEW and 26 changed events across MY/SG/CN. Fresh-head inspected the safely exposed head of newest page 2701–2737: seq 2701–2711 were obvious sales, MCF-only, 5+ hint, or contract/agency mismatches, with no serious survivor. Connector output truncates the remainder of the page, so seq 2712–2737 were not guessed. Sequential page 201–250 remains unresolved because connector output cannot safely expose seq 219; cursor stays 218 with no jump across history. No Gmail finalist lookup or Issue write was needed.`

## Current receipt

- completed run time: `2026-10-15 ~04:40 MYT`
- run type: `scheduled maintenance + bounded SG-gap/CN-native discovery — platform/infra/systems + ML systems/AI infra/inference/evaluation rotation`
- maintenance: `Fully inspected current ACTION/APPLY/CHECK. #184 Ant International remains ACTION for coding assessment + confirmed 2026-10-23 interview; #220 remains ACTION for an interview invitation; #304 remains ACTION for a time-bounded OA. Re-evaluated ACTION semantics rather than preserving procedural tasks by default. Both Gmail lifecycle overlap searches completed; the new Boehringer Principal System Analyst and TÜV SÜD procedural reminders map to already-closed SKIP Issues #278/#273 and do not reopen them. No new state-changing evidence for the live ACTION/APPLY/CHECK set.`
- SG gap lanes tried: `direct employer/ATS and targeted platform/infra gaps around Apple, Airwallex, ByteDance, Singtel/NCS, DXC and smaller cloud/data-infra surfaces. Apple/Airwallex results were senior; ByteDance 2026 graduate infra roles surfaced as explicitly no longer accepting or only stale secondary copies; DXC GRIT is old; Singtel surfaced additional platform/software roles but an active same-employer CHECK #309 already owns the unresolved exact-route problem and no second materially stronger role justified another active CHECK. No routine FreeHire rescan performed.`
- CN native/direct lanes tried: `BOSS, 牛客, 51job, 猎聘 and direct employer/campus searches for platform/infra/SRE/AI-infra with 2026/应届/0-3 YOE signals. 牛客 PDD/Ctrip/Huawei variants were ended or not yet live; BOSS surfaced 2026 Shanghai software/platform leads but only generic/indexed pages without current exact-role liveness; 51job surfaced early-career Linux/C++ leads but no exact employer-controlled current role proof; 猎聘 AI SRE required 3+ years plus large GPU-cluster operations. Existing Huawei AI Infra #308 remains the relevant CHECK rather than duplicating it.`
- SG coverage: `8 candidates / 6 employers / 4 source families / 0 deep-verified`
- CN coverage: `10 candidates / 7 employers / 5 source families / 0 deep-verified`
- serious survivors: `none`
- Gmail finalist dedupe: `No new finalist reached Stage 2, so no per-role Gmail dedupe was needed. Both recent lifecycle overlap searches completed successfully.`
- access/search failures: `No required Gmail/GitHub write failure. CN native public indexing remains uneven; generic BOSS/51job index pages were not treated as current role-level proof.`
- external side effects: `No application, recruiter message, employer contact or assessment submission sent.`
- next rotation: `data platform + search/retrieval, then Applied AI only where it adds a genuinely different employer/role lane. SG: direct employer/ATS gaps and smaller product/data/search employers not duplicated by FreeHire. CN: rotate direct employer/campus plus 智联/51job/猎聘/BOSS data-platform/search keywords; prioritize 2026 graduate/recent-graduate or 0-3 YOE exact-role evidence.`
