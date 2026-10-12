# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 04:41 MYT`
- run type: `bounded scheduled discovery — SG sponsor-positive gap rotation + CN explicit foreign-work-permit rotation; <=30d freshness and exact-route gates`
- material changes: `No new Issue created or promoted. No existing opportunity Issue mutated.`
- SG platforms / lanes actually searched: `Indeed sponsor-keyword discovery; JobStreet/SEEK fresh junior SWE/AI lanes; FreeHire gap evidence; LinkedIn exact-role history; direct/company evidence for Codex Solutions; targeted public-web sponsorship checks.`
- SG coverage: `14 candidates / 10 employers / 5 source families / 3 deep-verified`.
- SG result: `Zero survivors. Zero Byte Labs AI Engineer/FDE are fresh and excellent technical fits but retained route resolves to MCF-only, so blocked. Codex Solutions Software Engineer/AI Software Engineer are strong early-career fits and current board surfaces show fresh reposts, but older exact-role LinkedIn evidence makes original-requisition <=30d freshness unproven; work-auth also remains UNKNOWN and security-clearance sensitivity adds uncertainty. ByteDance low-code explicitly prioritizes candidates not requiring sponsorship. Other surfaced roles were senior, outsourcing/recruiter-heavy, weak-domain, or sponsorship-UNKNOWN without enough career value to justify promotion.`
- CN platforms / lanes actually searched: `targeted public-web/direct-employer search for 外籍/外国人/工作许可/Work Visa + AI/backend in Shanghai/Hangzhou; direct employer page for 上海网洋智能; foreign-work-permit policy cross-check only as legal context.`
- CN coverage: `6 candidates / 5 employers / 2 source families / 1 deep-verified`.
- CN result: `Zero survivors. 上海网洋智能 AI Engineer is live on the employer site and technically strong, but requires 3+ years software development plus 1+ year LLM/Agent/RAG delivery with no graduate exception, and no employer-specific foreign-work-permit willingness was found. Other search results were policy/service pages rather than exact technical vacancies, stale/weak-fit roles, or lacked employer-specific foreign-hire evidence.`
- route / evidence discipline exercised: `MCF-only SG roles blocked even when fresh and technically strong. Search-result/repost freshness did not override older exact-role evidence. Legal CN work-permit eligibility was not treated as employer willingness. No sponsorship inference from employer size, salary, international operations, application availability, or security-clearance wording.`
- access / search issues: `Native CN indexing remained sparse for exact fresh foreign-candidate technical roles; no absence-of-market claim. Some SG board Apply destinations could not establish a stronger employer-controlled route, so they were not promoted.`
- external side effects: `No application, recruiter message, employer email or sponsorship inquiry sent. No opportunity Issue write performed; only this discovery receipt was updated.`
- next rotation: `SG: rotate away from Codex/Zero Byte/HUD/Clera toward fintech, cloud/data infrastructure and B2B SaaS employers with explicit pass/relocation evidence and employer-controlled ATS roles first seen >=2026-09-13. CN: rotate to Shanghai/Suzhou foreign-invested product/software employers and direct foreign-talent technical boards; require exact fresh role plus employer-specific foreign-candidate/work-permit signal before promotion.`
