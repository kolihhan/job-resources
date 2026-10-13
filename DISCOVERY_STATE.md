# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~13:50 MYT`
- run type: `bounded SG gap + CN native/direct discovery; platform/infra/systems rotation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- material change: `Created and read-back verified CHECK #290 Microsoft — Service Engineer 2 (Shanghai). No APPLY promotion and no external application/contact.`
- SG lanes: `platform/infra/search sponsorship-targeted gap search plus direct employer surfaces. Clera Platform Engineer was explicitly sponsor-positive but exact listing is closed; HUD platform role is senior and already represented by existing HUD opportunity; Airwallex platform/ML-platform roles were senior or hard 5+/6+ YOE. No SG survivor promoted.`
- CN lanes: `Shanghai/Shenzhen platform/search/infra + multinational direct-employer search. Microsoft Service Engineer 2 survived with exact employer route and 2+ required experience; Microsoft Shanghai Core AI has hard 5+ YOE and was rejected; Beijing Core AI is 3–5+ stretch and lower priority; Huawei/Tuhu 2026 campus search-platform roles are closed; Ctrip data-platform Agent role is 2027-cycle with graduation window starting Sep 2026 and was not inferred compatible.`
- SG coverage: `5 candidates / 4 employers / 3 source families / 2 deep-verified`
- CN coverage: `8 candidates / 6 employers / 4 source families / 3 deep-verified`
- survivor: `#290 Microsoft Service Engineer 2 — Shanghai. Microsoft careers shows update 2026-10-08 and exact candidate route job 1970393557022790 is open. Required 2+ relevant technical experience OR equivalent; Python/SQL/API/automation/production-debugging overlap is credible, while cloud/distributed/observability depth is a gap. TECHNICAL FUNNEL = DISCOVERY/CHECK. WORK-AUTH FUNNEL = UNKNOWN: Microsoft's application form explicitly asks whether work-visa/work-permit sponsorship is required, but no exact-role China permit commitment was verified. Both Gmail accounts showed no application receipt for this exact role.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub write: CHECK #290 plus this receipt.`
- next rotation: `Move away from platform/infra-first toward data platform or ML systems/inference/evaluation. Prefer new employers and explicit SG sponsorship / CN foreign-work-permit evidence; avoid repeating Microsoft/Airwallex/HUD unless materially stronger new evidence appears.`