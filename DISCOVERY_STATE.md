# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 09:34 MYT` — healthy, `first_seq=1`, `last_seq=2040`; page index matches `first_seq=1 / last_seq=2040`; no cursor gap. Backlog is 1822 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-12 16:48 MYT`
- SG lanes tried: `direct/aggregated sponsorship-keyword gap search across AI/SWE/backend plus current employer/ATS mirrors; routine FreeHire broad coverage was not recreated`
- SG coverage: `5 candidates / 5 employers / 3 source families / 2 deep-verified`
- CN lanes tried: `native/direct search across Shenzhen research/AI application, Shanghai Agent/platform, Hangzhou AI application and current 2026/2027 campus surfaces`
- CN coverage: `7 candidates / 6 employers / 4 source families / 3 deep-verified`
- serious-survivor Issues created/updated: `#270 深圳市大数据研究院 — 大模型研发工程师`
- concrete filters / regressions exercised: `SG HUD Full-Stack RL remains a duplicate of existing #219 with explicit visa support; EGIS AI Engineer is already applied/#75; TALENTSIS requires hard 5+ YOE; other SG hits lacked enough new value or exact sponsor evidence. CN 米哈游 Agent role has a hard Go/C++/Rust requirement not evidenced by the current profile; 物产中大 26 AI application role requires a 2026 PhD; multiple ByteDance/杭州 hits are 2027-only. 深圳市大数据研究院 role is current, explicitly allows excellent fresh graduates despite 1–3 YOE, and the institute publicly recruits global/overseas talent; exact-role work-permit willingness remains unconfirmed, so #270 is CHECK with WORK-AUTH PROBABLE rather than CONFIRMED.`
- concrete access/write issues: `No blocking access failure. Finalist Gmail dedupe for #270 was clean in both connected accounts. No application or outreach was performed.`
- next rotation: `SG gap search toward direct ATS B2B SaaS/data infrastructure/industrial software and non-AI-title SOL-compatible backend/platform roles with pass-feasible compensation. CN rotate toward Shanghai non-campus AI application/backend employers with foreign/overseas hiring evidence, then Shenzhen/Hangzhou direct-employer backend/platform roles; avoid repeating 2027-only campus surfaces.`
