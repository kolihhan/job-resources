# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~01:40 MYT`
- run type: `bounded SG/CN discovery — rotated to platform/infra/systems + ML systems/AI infra; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `current JobStreet/Indeed infrastructure and AI-infrastructure gap search, direct-employer career pages, fresh-graduate/0–3 YOE systems and DevOps lanes, sponsorship-oriented searches`
- CN native/direct lanes tried: `Shanghai platform/inference/AI-infrastructure searches, international-employer direct-career searches, foreign-candidate/work-permit terms`
- SG coverage: `12 candidates / 10 employers / 4 source families / 0 deep-verified`
- CN coverage: `9 candidates / 8 employers / 4 source families / 0 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG infrastructure results were dominated by IT support/network administration, recruiters/system integrators, senior infrastructure ownership, or public-safety/security-sector roles without usable sponsorship evidence. Fresh-grad DevOps/cloud listings surfaced through Talentsis and similar intermediary routes but did not justify deep verification under the bodyshop/intermediary and work-auth filters. Singtel current infrastructure lane is senior-heavy. CN direct/native searches did not produce a <=30d early-career platform/inference role with sufficiently strong exact-role evidence and employer work-permit realism. Randstad Fullstack Developer - LLM is technically strong but exact role date is 2026-09-03, outside the <=30d hard gate; its older inference-framework role is expired. Legal Shanghai work-permit eligibility was not treated as employer willingness.`
- Gmail finalist dedupe: `not run; no candidate survived cheap freshness/fit/work-auth screening far enough to justify mailbox lookup.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. No opportunity Issue created or mutated. Discovery receipt updated only.`
- next rotation: `data platform + search/retrieval lane. SG: direct ATS/product-company search for early-career data/backend/search engineering with explicit pass/relocation or credible foreign-hiring evidence. CN: <=30d Shanghai/international-employer data platform, search/recommendation/retrieval engineering with foreign-candidate/work-permit evidence; avoid generic data analyst and algorithm-research roles.`
