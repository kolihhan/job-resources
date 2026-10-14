# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~10:41 MYT`; policy/state reconciliation completed `~12:02 MYT`
- run type: `bounded SG/CN discovery — rotated to data platform + search/retrieval`
- policy note: `The original run used the then-carried <=30d/sponsorship-heavy interpretation. Current RULES supersede that interpretation: freshness is a ranking signal, UNKNOWN SG/CN work-auth may reach APPLY, and exact-ID GitHub + both-Gmail dedupe is required before CHECK/APPLY promotion.`
- SG gap lanes tried: `direct/employer and Greenhouse data-platform/search-retrieval gap search; current Singapore data-engineering listings; sponsorship-oriented gap search outside recently saturated employers`
- CN native/direct lanes tried: `牛客 search/recommendation/data-platform; Shanghai 2026/2027 campus and direct-employer data-platform/search lanes; international-employer Shanghai data-engineering search`
- SG coverage: `9 candidates / 8 employers / 4 source families / 2 deep-verified`
- CN coverage: `8 candidates / 6 employers / 4 source families / 0 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG: Workato Analytics Engineer required 2+ years specifically in analytics engineering/data warehousing plus expert dbt and modern cloud-warehouse experience, a material fit gap. Nscale Forward Deployed Data Engineer required deep hands-on Palantir Foundry/ontology/pipeline experience and asked about existing work rights; it was too specialized/speculative for promotion. Thales data platform was hard 5+ YOE; OCBC data/AI platform was closed; KPMG KDB+ was experienced-hire/manager-track. CN: current search/data-platform results were dominated by incompatible 2027 cohorts or ended roles. No compatible 2026 early-career survivor was promoted in that run.`
- Gmail finalist dedupe: `not run in the 10:41 discovery because no candidate survived that run's final gate. Subsequent audit found prior exact-ID dedupe false-negatives on Intel #298 and WeRide #302; both were corrected to WAIT, and current RULES now require exact-ID GitHub + both-Gmail dedupe before CHECK/APPLY promotion.`
- reconciliation: `hard-3+ routine stretches #300, #294, #289, #286 and #265 were closed/deprioritized after preference recalibration; #291 and #295 were rewritten so UNKNOWN sponsorship is not a CHECK blocker.`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent during discovery or reconciliation.`
- next rotation: `SWE/SDE + backend. SG: direct ATS/employer graduate/0–3 YOE backend/SWE and strong product engineering gaps; treat work-auth CONFIRMED/PROBABLE as prioritization bonuses and UNKNOWN as allowed. CN: native/direct 2026-compatible graduate/0–3 YOE backend/SWE, including international employers; reject incompatible cohorts and hard seniority rather than waiting for public permit wording.`
