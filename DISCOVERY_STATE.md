# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~15:45 MYT`
- run type: `bounded SG gap + CN native/direct discovery; search/retrieval + backend/SWE rotation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- material change: `none — no genuinely useful survivor met the full promotion gates; no Issue created or updated.`
- SG lanes: `Search/retrieval and backend/SWE gap search across direct/ATS-targeted web, LinkedIn and graduate-role surfaces. Shopee Backend Engineer, Search (2026 Graduate) was technically excellent (distributed indexing/query processing, RAG, Agentic Search; Python/Go/C++) but the surfaced exact-role evidence did not prove a <=30-day employer-controlled posting/update date or a verified final non-MCF candidate route, so it was not promoted. ByteDance search graduate results were either closed or PhD-specific; NUS AI Agent role was closed; Singtel result was senior.`
- CN lanes: `Native/direct search across 牛客, 智联, 51job and employer/campus surfaces for search/retrieval/backend/SWE. Huawei and ByteDance 2026 backend/AI/search listings surfaced by native boards were explicitly marked ended despite crawler recency. Ctrip search/NLP internship listings were ended; current-looking Ctrip 2026 full-time LLM result was algorithm/model-heavy and its native page was marked ended, so no promotion. Generic 51job/Zhaopin category pages lacked exact-role freshness/route proof.`
- SG coverage: `5 candidates / 4 employers / 3 source families / 1 deep-verified`
- CN coverage: `8 candidates / 5 employers / 4 source families / 1 deep-verified`
- survivor: `none`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub write: this receipt only.`
- next rotation: `Move away from search/retrieval-first toward backend/SWE or data-platform/platform systems, prioritizing new employers and explicit SG sponsorship / CN foreign-work-permit evidence; do not repeat Shopee unless an employer-controlled fresh exact route/date becomes verifiable.`