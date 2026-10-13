# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~00:55 MYT`
- run type: `bounded SG/CN discovery — rotated to SWE/SDE + backend; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct employer/current web gap search plus sponsorship-oriented SWE/backend discovery; smaller product employers and current 0–3 YOE/fresh-grad listings checked`
- CN native/direct lanes tried: `Shanghai SWE/backend direct-employer/native discovery, including international employers and foreign-work-permit terms`
- SG coverage: `9 candidates / 8 employers / 3 source families / 1 deep-verified`
- CN coverage: `8 candidates / 7 employers / 4 source families / 1 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `Titansoft Software Developer is a strong 0–2 YOE/fresh-grad match but exact prior application already exists as WAIT #205, so no duplicate pursuit. Padlet Software Engineer – Frontend/Backend/Fullstack is currently live on the employer site and technically plausible, but the exact role page exposes no role-specific <=30d posted/updated date; freshness is therefore unproven under the hard gate, and separate evidence indicates Padlet Singapore roles may lack visa sponsorship, so it was not promoted. ShopeePay 2027 Graduate explicitly prioritizes candidates with current Singapore work rights/no sponsorship. YouTrip asks 4 years. Clera/HUD infrastructure roles are senior-shaped despite sponsorship. Mettler-Toledo Shanghai req 23264 is fresh and officially live (posted 2026-09-23) with an exact employer Apply route, but hard-requires 2+ years embedded-software experience and substantial industrial/PLC/device integration, a major domain mismatch. Randstad Shanghai Java role is fresh but is an intermediary/consulting route and does not establish foreign-work-permit willingness. Other CN results were stale, 5+ YOE, or lacked role-specific freshness/work-permit evidence.`
- Gmail finalist dedupe: `not run; no new candidate survived freshness/fit/work-auth screening far enough to justify mailbox lookup. Existing Titansoft duplicate was resolved from GitHub first.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. No opportunity Issue created or mutated. Discovery receipt updated only.`
- next rotation: `platform/infra/systems + ML systems/AI infra lane. SG: direct ATS/startup-product gap search with explicit pass/relocation support and early-career/equivalent wording. CN: fresh <=30d Shanghai/international-employer systems/platform/inference roles with concrete foreign-candidate or work-permit evidence; rotate away from industrial embedded roles.`
