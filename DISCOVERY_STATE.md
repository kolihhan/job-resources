# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-25` — pre-sharding latest worker state is healthy at `first_seq=1`, `last_seq=14372`; page index agrees on the same range and there is no cursor gap. Latest recorded delta completed at `2026-10-25T01:08:20.431674Z` with `new=10`, `changed=0` (`SG fetched=531`, `CN=66`, `MY=203`). This health snapshot predates the SG-sharding merge below; do not claim live sharded-fetch counts until a subsequent worker run records them.
- worker correction: `2026-10-25` — `kolihhan/freehirefetch` PR #4 merged as `eb56a4f323652659ae374b16de2257c2b8a5423a`. `Senior` titles are now downstream review hints rather than source-level hard drops; Staff/Principal/Lead/Manager/Director/Intern remain title hard drops. Singapore broad discovery is split into four engineering category windows (SWE, AI+Data, QA, Infra), unioned and exact-deduped by job identity; DevRel/technical-writing categories were removed from the broad engineering firehose. PR CI and post-merge main CI both passed; live worker ingestion under the new code has not yet been observed in `health.json`.
- earlier worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop seeds stale unseen jobs without emitting them as NEW.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake limitation: `Historical cursor catch-up remains blocked by connector truncation of one-line JSONL pages. Cursor is deliberately preserved at 513 rather than guessing. The public feed itself is healthy through seq 14372.`

## Current receipt

- completed run: `2026-10-25 12:44 MYT` — scheduled maintenance + discovery under current broad-throughput contract.
- maintenance: `Read README/PROFILE/RULES/DISCOVERY_STATE; inspected all open ACTION/APPLY/CHECK; checked both Gmail accounts with overlap for lifecycle evidence. No new employer lifecycle transition was established. Reconciled obsolete policy drift in #647: MY TOP/company identity is no longer an eligibility gate, so exact permanent Michael Page AI Software Engineer JN-072026-7065693 moved CHECK -> APPLY after exact-ID dedupe was clean in both Gmail accounts.`
- discovery coverage: `SG direct/web + current LinkedIn-alert gap pass across Applied AI/FDE/SWE; CN native/web Agent/application-engineering pass; MY broad AI/software web pass. Serious survivors: #661 Agnes AI Forward Deployed Engineer / Software Engineer (SG) created APPLY; #647 promoted APPLY. CN surfaced 鼎捷 Agent role but current evidence did not establish a better verified new survivor in this pass; obvious mature 3-5/5-YOE results were screened out.`
- FreeHire: `Cursor preserved at 513. Attempt to read feed/health.json returned 404, so no post-merge live sharded-fetch count is claimed and no cursor movement was guessed.`
- employer-facing actions: `none. No application, recruiter message, or other external employer action was sent.`
- failures/limits: `FreeHire health-path read failed with 404; historical cursor limitation remains. No required job-resources GitHub write failed.`
- next rotation: `SG general SWE/backend/full-stack + QA/SDET/test automation and direct ATS gaps; CN native-source 2026-compatible backend/software/test-development plus AI; MY broad early-career SWE/backend/full-stack/test with Applied AI prioritized. Re-check FreeHire public health/index path after the next worker run before claiming sharded runtime coverage.`
