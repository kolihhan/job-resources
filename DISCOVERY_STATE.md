# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~03:46 MYT`
- run type: `bounded SG/CN discovery — rotated to SWE/SDE + backend; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct employer/ATS SWE/backend, Indeed/JobStreet gap search, sponsorship-oriented backend search, product/startup employers`
- CN native/direct lanes tried: `Shanghai/Beijing/Shenzhen fresh backend/SWE search, 应届生/51job-style native discovery, direct/international-employer search, foreign-work-permit signal search`
- SG coverage: `9 candidates / 8 employers / 4 source families / 1 deep-verified`
- CN coverage: `10 candidates / 9 employers / 5 source families / 1 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG: Padlet Software Engineer is a live exact employer role but exact req eb909049-fbc3-4510-9b55-c02b97bbf4f7 is already WAIT #42 after application/receipt, so no duplicate. Neutron Backend Engineer (Junior) is fresh but the full JD requires 3–5+ years and cybersecurity/platform depth; Portcast Backend Engineer requires minimum 4+ years plus demonstrated scaled-system ownership; Klook/Shopee results explicitly prioritize current Singapore work rights/no sponsorship. Other surfaced roles were intermediaries/outsourcing-heavy or lacked sufficient exact-role freshness/route evidence. CN: fresh Shanghai backend discovery surfaced 沪上灵犀 with technically plausible requirements, but only mirror-level evidence was available and employer work-permit willingness plus exact official candidate route were unproven, so it was not promoted. Current campus results were predominantly 2027-cohort roles incompatible with a 2026 graduate; ByteDance AI-backend result was senior; Tencent Meetings backend requires 3+ years plus leading medium/large production systems. Legal work-permit plausibility was not treated as employer willingness.`
- Gmail finalist dedupe: `not run; no new candidate survived cheap freshness/cohort/fit/work-auth/route screening far enough to justify mailbox lookup.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. No opportunity Issue created or mutated. Discovery receipt updated only.`
- next rotation: `platform/infra/systems + ML systems/AI infra/inference/evaluation. SG: fresh <=30d direct ATS roles with 0–3 YOE/equivalent-experience and credible pass/relocation evidence. CN: fresh <=30d direct/native systems/platform roles at international or foreign-hiring-capable employers, avoiding 2027-only cohorts and requiring employer-level work-permit evidence before strong promotion.`
