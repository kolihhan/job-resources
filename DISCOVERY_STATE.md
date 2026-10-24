# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing. No serious survivor reached finalist Gmail dedupe and no Issue was created. No application or employer contact was performed.`

## Current receipt

- completed run time: `2026-10-25 00:45 MYT` — scheduled `00` window completed and read-back required.
- maintenance: `Read README.md, PROFILE.md, RULES.md and prior DISCOVERY_STATE.md; inspected all current ACTION/APPLY/CHECK. Both Gmail accounts were reconciled with overlap from 2026-10-23. No new exact-role lifecycle transition was safely attributable: Kredivo/Okudu/UIC LinkedIn confirmations lack exact role/req mapping in the available message surface, so no guessed WAIT issue was created. Existing ACTION meanings remain valid: #220 interview, #297 recruiter materials request, and #419/#468/#536/#575/#595/#599 authorized applications pending actual submission evidence.`
- discovery: `SG degraded-mode targeted gap search plus CN-native search completed. SG serious survivor: #651 Prudential AI Engineer req 26050211 — official exact Workday route live, Applied-AI/RAG/AI-backend fit, no hard mature-YOE blocker surfaced, employment PROBABLE, work auth UNKNOWN allowed; exact GitHub + both-Gmail finalist dedupe clean. SATS AI Engineer rejected at cheap filter for 3–5 years AI/backend. OpenMIA rejected as internship. Sea role rejected as Senior/mature ownership. CN search surfaced stale/closed or already-covered role families; no additional serious survivor promoted.`
- coverage counters: `SG targeted candidates screened: 5; SG serious survivors: 1; CN targeted candidates screened: 5; CN serious survivors: 0; MY lifecycle-only this window; HK discovery skipped because paused.`
- serious-survivor Issues: `created #651 Prudential — AI Engineer — 26050211; no other Issue created or promoted.`
- FreeHire state: `Cursor remains 513. Fresh-head/history intake remains unreadable in this runtime under the previously recorded truncation condition, so SG degraded mode remains active.`
- execution: `No application, recruiter outreach, interview response, phone call, or other employer-facing action was performed.`
- next rotation: `Maintenance first; then SG Agent/evaluation + AI-native product gap search, CN native Agent/RAG/evaluation rotation, and a small MY TOP pass. Resolve #641/#647 only if their sole blockers can be proven without employer contact.`
