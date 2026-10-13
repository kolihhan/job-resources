# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~16:47 MYT`
- run type: `bounded SG gap + CN native/direct discovery; backend/SWE + platform/data-infra rotation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- material change: `none — no genuinely useful survivor met the full promotion gates; no opportunity Issue created or updated.`
- SG lanes: `Backend/SWE and platform/data-infra gap search across direct employer/ATS, LinkedIn/Indeed gap surfaces and sponsorship-keyword probes. Garena Engineer, Backend Engineering is a strong 2-year stretch on the current official careers site (Go/Python/SQL, APIs, reliability, AI integration), but the official exact-role page exposes no role-specific <=30-day posted/updated date; LinkedIn copies are old/closed, so freshness is UNPROVEN and it was not promoted. Shopee data-infra result was closed and explicitly prioritized candidates not requiring visa sponsorship. First Circle surfaced as 4-5 YOE/mid-senior and was rejected.`
- CN lanes: `Native/direct backend/SWE and platform search across 牛客, 51job, 智联 plus foreign-candidate/work-permit keyword probes. Huawei/ByteDance/众安 2026 backend results were explicitly marked ended despite current crawling. 中城交 Shanghai backend/AI role looked technically strong (FastAPI, asyncio, RAG/Agent/vector DB), but the native listing was marked ended and the employer's own current careers page requires 3+ backend YOE, so it was rejected rather than promoted from stale board evidence. 上海森瑶 had a technically close 2026-grad Agent/FastAPI role but only a generic native-board route and no credible foreign-work-permit evidence; insufficient value for speculative promotion.`
- SG coverage: `6 candidates / 5 employers / 3 source families / 1 deep-verified`
- CN coverage: `9 candidates / 7 employers / 4 source families / 2 deep-verified`
- survivor: `none`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub write: this receipt only.`
- next rotation: `Move away from backend/SWE-first toward platform/infra/systems or ML-systems/AI-infra/evaluation; prioritize SG exact-role pages with role-specific <=30d dates plus sponsorship-compatible evidence, and CN direct employers with explicit foreign-candidate/work-permit infrastructure. Do not repeat Garena unless exact-role freshness becomes provable.`