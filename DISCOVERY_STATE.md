# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~14:47 MYT`
- run type: `bounded SG gap + CN native/direct discovery; ML systems/inference/evaluation rotation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- material change: `Created and read-back verified CHECK #291 Apple — Machine Learning Engineer, Strategic Data Solutions (Singapore). No APPLY promotion and no external application/contact.`
- SG lanes: `ML systems/evaluation/data-science engineering gap search plus Apple/direct-employer surfaces. Apple role 200659354-3278 survived: exact employer listing dated 2026-10-07 and live, with 3 years practical experience explicitly allowing work, independent projects or academic research. Other Apple AI results were manager/senior or non-engineering. No final signed-in candidate form was verified, so CHECK only.`
- CN lanes: `ML systems/inference/evaluation native/direct search across Tencent, Huawei, MiniMax, Meituan and Shenzhen AI-infra surfaces. Huawei 2026 AI Infra and MiniMax 2026 ML-systems campus listings are marked ended; Tencent current infra roles were mostly hard 3+ YOE or already overlap an unresolved active Tencent application; Meituan inference role was internship/stale. No CN survivor promoted.`
- SG coverage: `6 candidates / 4 employers / 3 source families / 1 deep-verified`
- CN coverage: `9 candidates / 6 employers / 5 source families / 2 deep-verified`
- survivor: `#291 Apple Machine Learning Engineer, Strategic Data Solutions — Singapore. TECHNICAL FUNNEL = DISCOVERY/CHECK. WORK-AUTH FUNNEL = PROBABLE at employer level only: Apple has Singapore immigration/global-mobility infrastructure, but no exact-role EP/S Pass commitment was verified and nationality/work-auth need has not been disclosed. GitHub exact role and Apple+role-family dedupe were clean; both Gmail accounts had no exact role-number receipt.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub write: CHECK #291 plus this receipt.`
- next rotation: `Move away from ML-systems-first toward search/retrieval or backend/SWE. Prefer new employers, explicit SG sponsorship / CN foreign-work-permit evidence, and avoid repeating Apple/Tencent/Microsoft unless materially stronger new evidence appears.`