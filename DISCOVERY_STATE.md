# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~18:47 MYT`
- run type: `bounded SG gap + CN native/direct discovery; search/retrieval + data-platform/SWE rotation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- material change: `none — no genuinely useful new survivor met the promotion gates; no opportunity Issue created or updated.`
- SG lanes: `Targeted direct-employer/ATS and JobStreet/web gap search across search/retrieval, data platform and backend/SWE. Singtel/Nxera AI Solutions Engineer is fresh (official page dated 2026-10-04) and technically strong, but requires 3–5 years; targeted Gmail dedupe found the candidate already applied to the same AI Solutions Engineer family (req 175668) on 2026-08-20 and was rejected on 2026-09-21, so the October repost was suppressed rather than promoted. Its Apply link also redirected to the generic Singtel careers home in current verification, failing the exact-route APPLY gate. Coinbase Data Platform appeared on JobStreet but is absent from Coinbase's current official Singapore engineering openings, so it was not promoted. Other surfaced SG data-platform roles were senior, contract/recruiter-heavy, or lacked enough value to justify sponsor-UNKNOWN deep verification.`
- CN lanes: `Native 牛客 plus direct/web search across search/retrieval, data-platform and backend/SWE. Current search surfaced multiple technically relevant 2026-campus roles, but exact 牛客 pages were explicitly 已结束 (Huawei AI software, ByteDance data platform, TuHu algorithm platform/search+RAG, DeepRoute backend/data platform, Shopee big-data). A ByteDance settlement-backend listing had contradictory 2026 metadata versus a hard 2027 JD requirement and was rejected on cohort evidence. No fresh <=30d direct role with a verified usable route and meaningful foreign-work-permit evidence survived.`
- SG coverage: `8 candidates / 6 employers / 3 source families / 2 deep-verified`
- CN coverage: `10 candidates / 8 employers / 3 source families / 2 deep-verified`
- survivor: `none`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub write: this receipt only.`
- next rotation: `Move away from search/retrieval + data-platform-first toward backend/SWE or Applied-AI product engineering; SG: target direct ATS/startup/product employers with exact <=30d role dates and non-MCF routes, avoiding repeat Singtel AI Solutions family. CN: rotate away from ended 2026 campus listings toward fresh social/direct-employer roles with 0–3 YOE or explicit graduate flexibility and foreign-candidate/work-permit infrastructure.`
