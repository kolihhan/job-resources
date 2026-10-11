# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 06:31 MYT` — healthy, `first_seq=1`, `last_seq=2033`; page index matches `first_seq=1 / last_seq=2033`; no cursor gap. Backlog is 1815 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2033. Feed advanced by 58 events since the prior receipt. Recent unseen page 2001–2033 was requested first; visible events were old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-12 04:45 MYT`
- SG lanes tried: `targeted direct-ATS software/backend gap search; routine FreeHire broad coverage was not recreated`
- SG coverage: `1 candidate / 1 employer / 1 source family / 1 deep-verified`
- CN lanes tried: `latest CN Discovery artifact endpoint attempted first but connector rejected the artifact-list endpoint; native fallback searched current 51job/Zhaopin surfaces for Shanghai backend/Python/AI-application roles with early-career bands`
- CN coverage: `8 candidates / 8 employers / 2 source families / 2 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `SG CSIT Software Engineer (Cybersecurity) matched 1–3 YOE/Python/FastAPI but explicitly accepts Singapore Citizens only, so hard-rejected. CN surfaces exposed early-career Python/backend and AI-adjacent roles, but serious candidates either had explicit 2+ professional Python/LLM requirements, weak/staffing-style employer quality, stale category evidence, or lacked sufficiently strong exact current role-level evidence to clear promotion gates.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with an eight-hour overlap: new mail consisted of automated application receipts already represented in WAIT, platform/discovery noise, and an OpenAI acknowledgement that does not identify the exact role; no new HUMAN_REPLY, ACTION_REQUIRED, REJECTION_OR_CLOSURE, OA or interview evidence was found. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct ATS industrial software/B2B SaaS/data infrastructure and graduate-friendly product employers. CN should rotate toward BOSS/direct-employer pages in Shenzhen/Hangzhou plus Shanghai direct-employer backend/platform roles, avoiding weak staffing mirrors; inspect cn-raw artifact first if connector support becomes available.`
