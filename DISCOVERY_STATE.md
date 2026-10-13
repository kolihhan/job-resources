# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~23:55 MYT`
- run type: `bounded SG/CN discovery — rotated to search/retrieval + data-platform; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct employer/ATS and current web gap search for search/retrieval, data-platform and backend/platform roles; explicit sponsorship terms checked before deep verification`
- CN native/direct lanes tried: `current Shanghai/Hangzhou/Beijing search/recommendation, data-platform and platform-development roles via native/campus/direct discovery; foreign-candidate/work-permit terms included in discovery`
- SG coverage: `8 candidates / 7 employers / 4 source families / 1 deep-verified`
- CN coverage: `9 candidates / 7 employers / 4 source families / 1 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `Exa Research Engineer, Generalist has excellent explicit Singapore visa sponsorship and strong retrieval fit, but the exact role is about 8 months old, so it fails the <=30d freshness hard gate despite remaining open. Salesforce Forward Deployed Engineer JR349138 is current but senior/lead-shaped with 5+ years in current mirrored evidence and substantial Salesforce-specific depth. OKX data-platform roles explicitly prioritize current Singapore work rights/no sponsorship. Singtel AI Solutions Engineer is closed. CN Huawei/Tuhu/Xiaomi 2026 cohort search/platform roles are closed/stale; Huawei/JD current campus roles target 2027 cohorts and are incompatible; Alibaba search/recommendation listings surfaced without sufficiently fresh exact-role evidence and no employer willingness for a foreign fresh graduate was established.`
- Gmail finalist dedupe: `not run; no candidate survived freshness/cohort/fit/work-auth screening far enough to justify mailbox lookup`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. No opportunity Issue created or mutated. Discovery receipt updated only.`
- next rotation: `SWE/SDE + backend lane. SG: direct employer ATS and smaller/mid-size product employers with 0–3 YOE/equivalent wording and explicit work-pass support where possible. CN: fresh <=30d direct/native SWE/backend roles, especially international employers or Shanghai employers with concrete foreign-hire/work-permit evidence; avoid 2027-only campus cohorts.`
