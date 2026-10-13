# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~21:45 MYT`
- run type: `bounded SG/CN discovery — rotated from backend-first toward ML systems/evaluation + early-career product SWE; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct/current employer-role search plus LinkedIn/Indeed gap evidence for ML systems/evaluation, software/backend and graduate roles; sponsor-specific discovery used only as a lead, not as automatic proof`
- CN native/direct lanes tried: `Shanghai/Hangzhou/Shenzhen early-career SWE/ML systems with foreign-hire/work-visa terms; international-employer/direct-role searches plus current CN job surfaces`
- SG coverage: `9 candidates / 8 employers / 4 source families / 2 deep-verified`
- CN coverage: `8 candidates / 7 employers / 4 source families / 2 deep-verified`
- serious survivors: `#296 MSD Specialist, Machine Learning Engineer (Singapore) — 2+ relevant years, Python/GenAI/agentic evaluation overlap; role-level mirrored data explicitly says VISA Sponsorship: Yes, so WORK-AUTH PROBABLE, but final employer-controlled candidate route was not independently opened and responsible-AI/governance is a real fit gap; kept CHECK.`
- notable rejects/dedupes: `SAP Associate AI Developer 447781 is an exact prior rejection (#115), so not reopened despite current live listing. SG senior/5+ roles and explicit no-sponsorship roles rejected. CN Cadence Shanghai 0–3 YOE systems role had attractive employer-level visa evidence but exact role date 2026-09-06 violates <=30d freshness. WeRide 2026 new-grad roles remain live but original posting dates are June and therefore fail the current freshness gate. Microsoft senior/principal results rejected on seniority; Booking.com 30347 is already tracked (#289).`
- Gmail finalist dedupe: `Both connected accounts searched for MSD/Merck + Specialist/Machine Learning Engineer; no exact application history found.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub writes only: created/read-back #296 CHECK and updated/read-back this discovery receipt.`
- next rotation: `search/retrieval + data-platform lane. SG: direct employer ATS and smaller product/data/search employers with 0–3 YOE/equivalent wording and explicit work-pass support where possible. CN: fresh <=30d Shanghai/Hangzhou/Shenzhen search/retrieval/data-platform roles at international/direct employers with explicit foreign-candidate/work-permit evidence; avoid repeating Microsoft/Booking/WeRide unless a materially new requisition appears.`
