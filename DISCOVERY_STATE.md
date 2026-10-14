# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-14 ~10:41 MYT`
- run type: `bounded SG/CN discovery — rotated to data platform + search/retrieval; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- SG gap lanes tried: `direct/employer and Greenhouse data-platform/search-retrieval gap search; current Singapore data-engineering listings; sponsorship-oriented gap search outside recently saturated employers`
- CN native/direct lanes tried: `牛客 search/recommendation/data-platform; Shanghai 2026/2027 campus and direct-employer data-platform/search lanes; international-employer Shanghai data-engineering search`
- SG coverage: `9 candidates / 8 employers / 4 source families / 2 deep-verified`
- CN coverage: `8 candidates / 6 employers / 4 source families / 0 deep-verified`
- serious survivors: `none`
- notable rejects/dedupes: `SG: Workato Analytics Engineer is fresh and live-looking but requires 2+ years specifically in analytics engineering/data warehousing plus expert dbt and modern cloud-warehouse experience, a material hard-fit gap. Nscale Forward Deployed Data Engineer has an attractive sponsor hint and salary band, but the exact JD requires deep hands-on Palantir Foundry/ontology/pipeline experience and its application asks whether the candidate already has work rights without sponsorship; this is too specialized/speculative for promotion. Thales data platform is hard 5+ YOE; OCBC data/AI platform is closed; KPMG KDB+ role is experienced-hire/manager-track; senior/principal results were rejected cheaply. CN: current search/data-platform results were dominated by incompatible 2027 cohorts (Xpeng, Ctrip, Moonton, Alibaba) or ended 2026 Ctrip roles. No current <=30d compatible-2026 full-time role with enough employer/work-permit realism survived.`
- Gmail finalist dedupe: `not run; no candidate survived final promotion gate. No GitHub Issue mutation was required.`
- external side effects: `No Issue created/updated; no application, recruiter message, employer contact or sponsorship inquiry sent. Receipt updated only.`
- next rotation: `SWE/SDE + backend. SG: direct ATS/employer early-career backend/SWE outside recent saturated clusters, emphasizing explicit sponsorship-compatible forms/pass evidence. CN: native/direct 2026-compatible backend/SWE roles, especially Shanghai/international employers with foreign-candidate or work-permit evidence; avoid 2027-only campus cohorts.`
