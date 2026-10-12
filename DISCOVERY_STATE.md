# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 09:34 MYT` — healthy, `first_seq=1`, `last_seq=2040`; page index matches `first_seq=1 / last_seq=2040`; no cursor gap. Backlog is 1822 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-12 20:53 MYT`
- SG lanes tried: `direct employer/ATS and sponsorship-keyword gap search across B2B SaaS/data infrastructure/backend/platform/SWE; routine FreeHire broad coverage was not recreated`
- SG coverage: `5 candidates / 5 employers / 3 source families / 1 deep-verified`
- CN lanes tried: `Shanghai AI/backend/Agent with foreign-hire evidence; direct employer/Moka surfaces; Beijing/Hangzhou Agent engineering; Shenzhen platform/AI application`
- CN coverage: `9 candidates / 8 employers / 4 source families / 3 deep-verified`
- serious-survivor Issues created/updated: `#279 DeepSeek — Agent Harness 研发工程师`
- concrete filters / regressions exercised: `SG Agoda GenAI is Staff and explicitly no-sponsorship; no new SG gap candidate combined early-career fit with a realistic pass path strongly enough to promote. CN Randstad Python AI Agent is duplicate existing #144; Randstad Shenzhen AI role asks 3+ YOE plus project leadership; Huawei 2026 role is already closed; multiple current campus surfaces are 2027-only. DeepSeek official careers still lists Agent Harness; exact Moka role route is available, role is highly aligned, and Harness lead publicly stated there is no rule against hiring foreigners. Exact work-permit sponsorship remains unconfirmed, so #279 is WORK-AUTH PROBABLE, not CONFIRMED.`
- concrete access/write issues: `No blocking access failure. Targeted DeepSeek finalist dedupe was clean in GitHub and both connected Gmail accounts. No application or outreach was performed.`
- next rotation: `SG gap search toward industrial software/fintech/search-retrieval and graduate-friendly non-AI SWE/backend roles with explicit future-sponsorship acceptance. CN rotate toward Shanghai international product employers and direct ATS roles with explicit 外籍/外国人 evidence, then Shenzhen/Hangzhou backend/platform employers; avoid repeating DeepSeek/Randstad and 2027-only campus surfaces.`
