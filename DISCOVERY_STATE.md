# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~04:40 MYT`
- run type: `bounded SG/CN discovery — rotated to platform/infra/systems + ML systems/AI infra/inference/evaluation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct employer/ATS platform/ML-platform search, inference/AI-infra gap search, sponsorship-oriented systems search`
- CN native/direct lanes tried: `Shanghai AI-infra/platform native search, Tencent direct careers, foreign-work-permit-oriented platform discovery`
- SG coverage: `8 candidates / 7 employers / 3 source families / 0 deep-verified`
- CN coverage: `7 candidates / 6 employers / 3 source families / 0 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG: Together AI FDE is explicit Singapore citizen/PR plus 5+ YOE; Clera Platform Engineer had strong visa/relocation evidence but exact listing closed Sep 19 and was not reopened from mirrors; CoreWeave inference result is Staff/8–12+ YOE; Airwallex current ML platform/infra roles are Senior/Lead or hard 5–6+ YOE. ByteDance Production Engineer / Applied ML Engine surfaced with a fresh 2026-10-02 mirror and junior-associate metadata, but no exact employer-controlled current role/application route was verified in this run and work-auth remained UNKNOWN, so freshness/route hard gates were not met. CN: Huawei AI Infra native listings are explicitly 2027 cohort and incompatible with a 2026 graduate; Tencent current platform/AI roles surfaced hard 3+ or 5+ YOE requirements; other Shanghai systems/inference results were stale or lacked employer-controlled <=30d freshness plus employer-level foreign-work-permit evidence and an exact usable route.`
- Gmail finalist dedupe: `not run; no new candidate survived cheap freshness/cohort/fit/work-auth/route screening far enough to justify mailbox lookup.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. No opportunity Issue created or mutated. Discovery receipt updated only.`
- next rotation: `data platform + search/retrieval. SG: fresh <=30d direct ATS search/data-platform/retrieval roles with 0–3 YOE/equivalent-experience and credible pass/relocation evidence. CN: fresh <=30d native/direct search/retrieval/data-platform roles at international or foreign-hiring-capable employers, avoiding 2027-only cohorts and requiring employer-level work-permit evidence before strong promotion.`
