# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 07:44 MYT`
- run type: `bounded SG+CN discovery; primary rotation platform/infra/systems; <=30d freshness, sponsor/work-permit precision and exact-route gates preserved`
- material changes: `Zero new APPLY/CHECK promotions. No existing opportunity Issue changed.`
- SG platforms / lanes actually searched: `targeted Indeed/public-web gap search plus direct-role evidence; platform/infra/systems and normal SWE/backend lanes; sponsorship-specific queries.`
- SG coverage: `12 candidates / 10 employers / 3 source families / 2 deep-verified`.
- SG result: `Zero survivor. HUD platform role is Senior and therefore hard-rejected despite explicit visa sponsorship. Clera platform evidence is sponsor-positive but does not override the existing closed Clera role/current-route history; no new exact fresh employer-controlled requisition with verified final route was established. Other junior/fresh-grad results lacked exact employer sponsorship evidence and/or exact verified final routes, so UNKNOWN was not padded into Issues.`
- CN platforms / lanes actually searched: `direct/MNC career indexing, 牛客 campus/native search, 猎聘/public foreign-hire queries; backend/platform/data/storage lanes in Shanghai and other major engineering hubs.`
- CN coverage: `11 candidates / 8 employers / 4 source families / 3 deep-verified`.
- CN result: `Zero survivor. Current indexed 2026-campus backend/data roles from 众安/UCloud/携程/华为 were stale or explicitly ended on their exact/native role pages despite current crawler activity. A fresh 2027-only AI/full-stack internship was cohort-incompatible. Bosch Shanghai software roles are current but require embedded/power-electronics experience and several years, a hard domain/seniority mismatch. Booking.com Shanghai 2027 graduate programme remains not yet open; official early-careers page says applications open 2026-10-15 and accepts 2026/2027 graduates, so it remains a high-value recheck rather than a live Issue today.`
- route / evidence discipline exercised: `Crawler/search-result freshness did not override older exact-role dates or ended status. Visa-search-category membership was not treated as exact-role sponsorship. Technical and work-auth signals remained separate; no automated progression was used as sponsor evidence.`
- access / search issues: `Exact employer-specific CN foreign-work-permit wording remains sparse. Several SG aggregator results did not expose a trustworthy employer-controlled final application route.`
- external side effects: `No application, recruiter message, employer email or sponsorship inquiry sent. No opportunity Issue state changed. GitHub write limited to this receipt.`
- next rotation: `SG: rotate to search/retrieval + data-platform employers outside HUD/Clera, prioritizing exact sponsor/pass language and direct ATS routes. CN: rotate to search/retrieval + ML-systems/AI-infra at fresh direct employers/native sources with explicit foreign-candidate/work-permit evidence; recheck Booking.com Shanghai graduate programme on 2026-10-15.`
