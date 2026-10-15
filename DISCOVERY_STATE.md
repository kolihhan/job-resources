# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-15 10:18 MYT` — healthy, `first_seq=1`, `last_seq=2878`; page index matches `first_seq=1 / last_seq=2878`; no cursor gap. Backlog is 2660 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2878; latest delta added 10 NEW and 0 changed events across MY/SG/CN. The newest indexed page is 2851–2878, but the GitHub connector truncates its JSONL payload before seq 2869–2878, so the 10 newly-added records cannot be safely screened from current accessible evidence. Historical page 201–250 likewise remains unresolved because seq 219 cannot be safely exposed through the connector. No records were guessed and no cursor jump was made. Cursor stays 218. No finalist could reach Stage 2 from the inaccessible new tail, so no Gmail lookup or Issue write was performed.`

## Current receipt

- completed run time: `2026-10-15 ~12:55 MYT`
- run type: `scheduled maintenance + bounded SG-gap/CN-native discovery — Applied AI / different-employer rotation`
- maintenance: `Fully inspected current ACTION/APPLY/CHECK. #184 Ant International remains ACTION for coding assessment + confirmed 2026-10-23 interview; #220 remains ACTION for a real interview invitation; #304 remains ACTION for a time-bounded OA due 2026-10-20. Both Gmail lifecycle overlap searches completed. No new state-changing evidence was found. Automated reminders for closed #278 Boehringer Principal System Analyst and #273 TÜV SÜD business-development trainee do not override the newer skip decisions and were not reopened.`
- SG gap lanes tried: `targeted current JobStreet/direct-employer/web gaps for entry-level Applied AI and AI-software roles, including SHOKZ, Nippon Paint SG, PEBBLEROAD, EGIS Healthcare, TOPPAN Ecquaria, Kaplan and smaller product employers; OpenAI Codex and Sapient roles were senior/hard-experience mismatches. SHOKZ looked technically strong and current on JobStreet, but targeted Gmail dedupe found the candidate already applied to Shokz AI Engineer in August and received a direct HR background-mismatch rejection; same-family repost suppressed rather than creating a new Issue. No routine FreeHire rescan performed.`
- CN native/direct lanes tried: `猎聘 + 牛客 + direct/current web gaps for 2026/recent-graduate Applied-AI/Agent/backend roles. 立邦中国 AI Agent开发工程师（26年应届生） remains live on exact Liepin route and is an unusually strong fit, but it is closed #61 with an explicit user no/skip decision, so it was not reopened. Huawei 2027 Applied-AI roles surfaced but are already represented by current Huawei CHECK #308 and do not justify another same-employer active CHECK. Older Huawei/Xiaomi 2026 pages are ended. Other indexed AI-app leads lacked stronger current exact-role proof or were 2027-only.`
- SG coverage: `10 candidates / 9 employers / 4 source families / 1 deep-verified`
- CN coverage: `8 candidates / 6 employers / 4 source families / 1 deep-verified`
- serious survivors: `none`
- Gmail finalist dedupe: `Both recent lifecycle overlap searches completed. SHOKZ finalist dedupe in both Gmail accounts found an August 2026 prior Shokz AI Engineer application and direct HR rejection; suppressed as same-family history. No CN finalist required new Gmail dedupe because the strongest live role was already terminally skipped in GitHub.`
- access/search failures: `No required Gmail/GitHub access or write failure. CN native-source indexing remains uneven; mirror/search recency was not promoted into liveness. Some SG JobStreet search surfaces expose current listings without a stable exact-role URL, so they were not promoted to APPLY.`
- external side effects: `No application, recruiter message, employer contact or assessment submission sent.`
- next rotation: `SWE/backend. SG: direct employer/ATS and smaller product/B2B/fintech backend gaps not duplicated by FreeHire; avoid SHOKZ same-family reposts and already-resolved Singtel family. CN: rotate BOSS/智联/51job/direct-employer recent-graduate or 0-3 YOE backend/SDE, changing employer cluster away from Huawei and ended 2026 campus pages.`
