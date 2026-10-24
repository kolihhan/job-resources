# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing. No serious survivor reached finalist Gmail dedupe and no Issue was created. No application or employer contact was performed.`

## Current receipt

- completed run date: `2026-10-24 MYT` — interactive Grill remediation followed by live queue migration. `RULES.md` commit `e4e0ae688952a1ffdeee11abad0129f393173025` was read back after write.
- policy migration: `Employment evidence now uses CONFIRMED / PROBABLE / CONFLICT / BLOCKED. Normal full-time/social/campus hiring with no contradictory non-permanent signal may reach APPLY; absence of the literal word Permanent alone is not a CHECK blocker. A narrow senior-title exception now exists only for unusually strong, genuinely junior-compatible JDs. Authorized application ACTION bodies must carry authorization state directly. SG FreeHire degraded mode is enabled when fresh intake cannot be screened.`
- queue migration: `13 permanence-only CHECKs were promoted to APPLY: #624 Agently, #625 ARRK, #627 Scinetics, #628 Jump Trading, #633 AI Singapore Evaluation, #634 广晟数科, #635 广电运通, #636 Coremail AI测试, #637 粤数网络, #638 Tencent WorkBuddy, #639 Shopee, #640 Oppstar, #643 NTT DATA.`
- remaining CHECK count: `2 genuine CHECKs remain: #641 Sunway Digital because current sources conflict on full-time vs contract employment; #647 Michael Page AI Software Engineer because the anonymized client/team still has to clear the Malaysia TOP role-level quality gate.`
- authorization sync: `Application ACTIONs #419, #468, #536, #575, #595 and #599 now explicitly say AUTHORIZED APPLICATION; submission pending and preserve the user's 2026-10-23 batch authorization. #220 is an interview ACTION and #297 is a recruiter materials ACTION; neither was part of that application authorization.`
- current queue counts: `ACTION 8; APPLY 20; CHECK 2. WAIT remains lifecycle/history and was not bulk-modified in this remediation.`
- FreeHire state: `Cursor remains 513. Fresh-head/history intake is still unreadable in this runtime because of truncation, so SG degraded mode is active: broader targeted LinkedIn/JobStreet/Indeed/direct-employer coverage is permitted until fresh FreeHire intake is screenable again.`
- execution: `No application, recruiter outreach, interview response, phone call, or other employer-facing action was performed in this remediation.`
- next rotation: `Handle #220 and #297 lifecycle actions first. Execute already-authorized application ACTIONs in a browser-capable session without re-asking go. Then review APPLY; resolve only #641 and #647 as CHECK. SG/CN remain active; MY stays TOP-only; HK stays paused.`
