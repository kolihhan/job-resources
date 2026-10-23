# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing. No serious survivor reached finalist Gmail dedupe and no Issue was created. No application or employer contact was performed.`

## Current receipt

- completed run date: `2026-10-24 MYT`
- run type: `interactive application reconciliation + CHECK resolution + hard APPLY pruning`
- active-market contract: `Hong Kong remains paused. Active search is Singapore + Mainland China with Malaysia TOP-only in parallel. Permanent full-time remains mandatory. Primary lane remains Applied AI / LLM / RAG / Agent / AI backend / evaluation / search-retrieval.`
- application-history reconciliation: `Moved confirmed already-applied roles out of APPLY/CHECK into WAIT using Gmail receipts or direct user Issue comments: Howden #619, Accenture #621, TT语音 #576, rednote #388, Huawei SG #370 and Deriv #525. Mintel #263 moved to BLOCKED because the candidate reported the final route as not found and no verified exact employer application form was recovered.`
- CHECK resolution: `0 CHECK remain. U Mobile #617, Maxis #618, Allianz #620 and AirAsia #622 were closed after fit/permanence review rather than left as indefinite blockers.`
- hard APPLY pruning: `APPLY reduced from 40 to 9. Survivors are #554 Altera, #537 NavInfo, #535 PuppyOne, #476 乐信圣文 Aurora, #469 Kuaishou context engineering, #454 Baidu AI test/evaluation, #451 Alibaba QoderWake, #424 Hikvision LLM application and #386 Quark/Qwen Agent application. These are the only current unsubmitted APPLY candidates intended for the next deliberate execution batch.`
- current live queue snapshot: `9 APPLY (all CN); 8 ACTION total = 7 previously authorized application actions + #220 interview action; 0 CHECK. Submitted opportunities remain WAIT and are not to be duplicated.`
- authorization boundary: `The prior user instruction 'go all ACTION applications' still authorizes the seven application-type ACTION items that were current at that time (#599, #595, #575, #536, #468, #463, #419). It does not authorize the newly retained nine APPLY survivors. #220 is an interview action, not part of application authorization.`
- direct-route note: `Prefer employer-controlled ATS/portals for surviving APPLY where available (Altera, NavInfo, 乐信圣文, Baidu, Alibaba, Hikvision, Quark/Qwen). PuppyOne is a current Nowcoder recruiter/chat route. Kuaishou has the exact BOSS target plus official general recruiting/AI-team contact channels; any outreach still requires explicit authorization.`
- employer-facing actions this run: `None. This run only reconciled evidence, changed GitHub statuses and pruned the queue.`
- next rotation: `Do not refill APPLY back to dozens of merely-good jobs. New discoveries should beat the current shortlist on fit × callback realism × career value, or be closed/ignored. Continue SG + CN with MY TOP only; no HK unless explicitly reactivated.`
