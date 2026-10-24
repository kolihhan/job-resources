# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-18 21:19 MYT` — worker healthy, `first_seq=1`, `last_seq=6030`; page index agrees on the current feed range; no cursor gap. Latest delta run reports `new=6`, `changed=0`, completed at `2026-10-18 17:35 MYT` (`2026-10-18T09:35:35.620494Z`).
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy at seq 6030 with no cursor gap. Retried both historical and newest sequence-addressable pages. UTF-8 fetch still truncates each one-line JSONL page; base64 fetch exposes more bytes but is likewise truncated before seq 514 and seq 6025-6030, and exact code search for seq 514 returns no result. Raw GitHub retrieval through the web path is unavailable in this runtime. Therefore historical catch-up cannot safely advance beyond seq 513 and seq 6025-6030 remain unscreened. Cursor deliberately preserved at 513 rather than guessing.`

## Current receipt

- completed run: `2026-10-25 interactive broad-throughput search`.
- strategy correction: `User explicitly corrected prior over-filtering. Current objective is mass application / interview generation across Singapore + Mainland China, with better companies prioritized but not required for entry into the queue. Do not restrict discovery to GOLD or Applied-AI-perfect roles.`
- active role scope: `Applied AI / Agent / RAG / evaluation remain preferred, but general backend, full-stack, software engineer, test-development / SDET, Python/Java/PHP software roles and other technically plausible early-career engineering jobs are now active discovery lanes.`
- cheap hard skips only: `clear Senior/Staff/Lead/Manager or hard mature 4+/5+ YOE; explicit contract/temp/intern when permanent employment is required; explicit citizenship/right-to-work/no-sponsorship blocker; clearly incompatible cohort; completely unrelated technical stack; closed/expired; exact duplicate/already applied.`
- JD rule: `Read the actual JD carefully before deciding. Do not reject because the role is imperfect or requires a learnable secondary stack. Separate hard requirements from preferred/bonus wording. 0–3 YOE and reasonable 2–4 YOE stretches may survive if the candidate can apply truthfully.`
- efficiency rule: `Search broad batches by source and role family; cheap hard-filter + GitHub dedupe first; only serious survivors get Gmail dedupe / route verification. Do not write long company-research essays before deciding whether a role is simply eligible to apply.`
- SG first batch added: `#652 Delivery Hero/foodpanda Junior Fullstack Software Engineer; #653 Alta Software Engineer; #654 Combuilder Software Engineer (Go/Python). Strong-looking AMD/Xilinx and GlobalFoundries roles were correctly suppressed as already-applied history. Kaplan AI Engineer was not promoted because current surfaces conflict on employment type.`
- CN first batch added: `#655 ByteDance general backend role family; #656 新毅东 software R&D application engineer; #657 Huawei Cloud 2026 AI software engineer; #658 AsiaInfo Security test development; #659 SSE Information test development; #660 积加科技 test development.`
- execution: `No employer-facing application/contact was submitted in this pass. New APPLY issues still require user authorization under the existing application-action rule.`
- next rotation: `Continue high-throughput SG + CN search. SG: junior/backend/full-stack/software/AI/test automation across Indeed/JobStreet/LinkedIn/direct ATS, including ordinary employers and agencies when the role itself is plausible. CN: 2026-compatible campus + 0–3 YOE social roles across backend/software/test/AI on 牛客/BOSS/official/51job/智联/猎聘. Prefer stronger companies, but do not discard ordinary companies solely for weak brand.`
