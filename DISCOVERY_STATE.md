# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~12:43 MYT`
- run type: `bounded SG gap + CN native discovery; search/retrieval/platform/SWE rotation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- material change: `Created and read-back verified CHECK #289 Booking.com — Software Engineer II, China Tech (Req 30347). No APPLY promotion and no external application/contact.`
- SG lanes: `direct employer/ATS + targeted backend/search/ML-systems sponsorship gap search. Exa Backend is explicitly sponsor-positive but Gmail shows a prior Exa application receipt from 2026-08-27 and exact prior role mapping is unresolved, so it was not promoted. HUD sponsor-positive roles are already represented by existing #275; Singtel/Nxera AI Solutions Engineer is fresh but has a hard 3–5 YOE requirement; Together AI FDE explicitly requires Singapore PR/citizenship.`
- CN lanes: `Shanghai/Shenzhen direct employer, multinational SWE/backend, foreign-work-permit/visa-targeted search, native/direct role surfaces. Booking.com Req 30347 survived; ShopBack Shenzhen backend is stale on original posting despite fresh mirrors; Google 2026 graduate role is closed; current HSBC/ByteDance results were senior-level; stale Randstad roles were rejected.`
- SG coverage: `7 candidates / 6 employers / 3 source families / 3 deep-verified`
- CN coverage: `10 candidates / 8 employers / 4 source families / 4 deep-verified`
- survivor: `#289 Booking.com Software Engineer II, China Tech — Shanghai, official jobs index currently lists exact Req 30347 and current role record is dated 2026-10-10. Strong backend/distributed-systems career capital; stretch is minimum 3 years + 2 server-side languages. Prior Booking.com Full Stack SWE I application was rejected in July, but no prior Req 30347 application was found. TECHNICAL FUNNEL = DISCOVERY/CHECK. WORK-AUTH FUNNEL = UNKNOWN: multinational/relocation/work-visa benefit signals exist, but no exact-role China permit commitment was verified. Final employer candidate form could not be opened due 403, so CHECK not APPLY.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub write: CHECK #289 plus this receipt.`
- next rotation: `Move away from backend-first toward platform/infra/systems or search/retrieval. Prefer new employers and explicit SG sponsorship / CN foreign-work-permit evidence; avoid repeated LLM/Agent title searches and stale mirror reposts.`