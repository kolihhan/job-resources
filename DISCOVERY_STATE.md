# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~12:46 MYT`
- run type: `scheduled maintenance + bounded SG-gap/CN-native discovery — SWE/SDE + backend rotation`
- maintenance: `Both Gmail accounts checked with overlap. Closed #226 GRC Construction AI Engineer and #239 K Digitech AI FDE after new JobStreet unlikely-to-progress updates. Created #304 for Amway China 2027-campus OA due 2026-10-20 15:01 MYT; exact applied role and cohort eligibility remain unresolved. New Micron JR107801 closure had no matching live GitHub Issue. Existing user-skipped 阳光保险 assessment remained closed despite newer reminder.`
- SG gap lanes tried: `direct employer/ATS backend/SWE; graduate/early-career gap search; targeted product/platform employers. Singtel Software Developer was technically plausible and current, but the employer Apply action redirected to the generic careers home in this verification environment, so no Issue was promoted. ByteDance 2026 graduate backend results surfaced as no longer accepting; Shopee graduate infra carried an explicit no-sponsorship/right-to-work preference.`
- CN native/direct lanes tried: `牛客 2026 backend/SWE; direct Tencent experienced-hire search; international/large-employer backend search. Current native results were dominated by ended 2026 listings, incompatible 2027-only cohorts, or harder experienced roles; no new serious survivor.`
- SG coverage: `6 candidates / 5 employers / 3 source families / 1 deep-verified`
- CN coverage: `9 candidates / 7 employers / 3 source families / 0 deep-verified`
- serious survivors: `none from discovery; lifecycle ACTION #304 created during maintenance`
- Gmail finalist dedupe: `Singtel Software Developer exact role/job identifier checked in both Gmail accounts; no exact prior application receipt found. No other discovery candidate reached finalist promotion.`
- access/search failures: `Singtel exact Apply action redirected to generic careers home, so final candidate route could not be verified. Several CN 牛客 listings were explicitly ended despite recent crawling and were rejected on exact listing state.`
- external side effects: `No application, recruiter message, employer contact or assessment submission sent.`
- next rotation: `platform/infra/systems + ML systems/AI infra/inference/evaluation. SG: direct ATS/employer gaps not well covered by FreeHire, especially early-career cloud/platform/reliability/ML-platform roles. CN: native/direct 2026-compatible platform/infrastructure/ML-systems roles; rotate away from ended 牛客 campus mirrors toward official/campus and other native sources.`
