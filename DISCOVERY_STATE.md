# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-15 03:21 MYT` — healthy, `first_seq=1`, `last_seq=2656`; page index matches `first_seq=1 / last_seq=2656`; no cursor gap. Backlog is 2438 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2656; latest delta added 13 NEW events across MY/SG/CN. Fresh-head inspected the newest complete page 2651–2656: three SG MCF/contract roles, one CN senior sales role and one MY L3 infrastructure role were cheap hard rejects; SG Native DevOps was the only plausible fresh-head candidate, but its exact Trakstar page was inaccessible and targeted search did not independently verify the exact role, so it was not promoted. The preceding 2601–2650 page remains connector-truncated before seq 2644–2650, so those unseen records were not guessed. Sequential page 201–250 remains unresolved because connector output cannot safely expose seq 219; cursor stays 218 with no jump across history. No Gmail finalist lookup or Issue write was needed.`

## Current receipt

- completed run time: `2026-10-15 ~00:48 MYT`
- run type: `scheduled maintenance + bounded SG-gap/CN-native discovery — SWE/backend + smaller product/B2B/industrial rotation`
- maintenance: `Inspected current ACTION/APPLY/CHECK. #184 Ant International remains ACTION for coding assessment + confirmed 2026-10-23 interview; #220 remains ACTION for an interview invitation; #304 remains ACTION for a time-bounded OA. Both Gmail lifecycle overlap searches completed. New Micron Workday evidence says DATA SCIENTIST JR107801 was closed and cannot proceed; reconciled into closed Micron data-science-family history #100. No newer state change found for the current ACTION/APPLY/CHECK set.`
- SG gap lanes tried: `direct employer/ATS and product-company SWE/backend gaps, including Singtel, ShopBack, Palantir, ByteDance and CSIT. Singtel Software Developer is live on the exact employer page, has no numeric YOE minimum and fits backend/platform engineering, but its Apply action redirects to the generic careers homepage; promoted as #309 CHECK with exact route as the sole blocker. ShopBack Senior / Software Engineer is unusually suitable and explicitly welcomes fresh graduates, but exact prior application #83 suppresses it. ByteDance graduate infrastructure roles surfaced as closed; CSIT roles explicitly require Singapore citizenship. No duplicate board-wide FreeHire rescan performed.`
- CN native/direct lanes tried: `51job/智联/猎聘-targeted web discovery plus 牛客 and direct/campus employer searches for SWE/backend roles compatible with a 2026 overseas graduate. Current visible 牛客 leads from ByteDance, UCloud, Huawei Cloud, Shopee China and China Electronics Cloud were explicitly ended, historical, or cohort-incompatible; broader 51job/智联/猎聘 indexing did not yield a current exact-role survivor with enough role-level evidence. No new CN survivor.`
- SG coverage: `6 candidates / 5 employers / 3 source families / 1 deep-verified`
- CN coverage: `8 candidates / 6 employers / 4 source families / 0 deep-verified`
- serious survivors: `#309 created CHECK; #100 closed history updated with Micron JR107801 closure`
- Gmail finalist dedupe: `Both accounts searched for Singtel + exact role ID/title; no prior exact application receipt found. Both recent lifecycle overlap searches completed successfully.`
- access/search failures: `No required Gmail/GitHub write failure. CN native public indexing remains uneven; no claim that sparse indexed results represent the full CN market.`
- external side effects: `No application, recruiter message, employer contact or assessment submission sent.`
- next rotation: `platform/infra/systems + ML systems/AI infra/inference/evaluation. SG: direct employer/ATS gaps and smaller product/cloud/data-infra employers not duplicated by FreeHire. CN: rotate direct employer/campus plus BOSS/51job/智联/猎聘 platform/infra keywords; prefer 2026-overseas-graduate or 0-3 YOE evidence and avoid recycling ended 牛客 listings.`
