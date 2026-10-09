# Discovery State

## FreeHire intake cursor

- cursor: `213`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-10 05:34 MYT` — healthy, `first_seq=1`, `last_seq=1603`, `SG 529 / CN 15`; page index matches `first_seq=1 / last_seq=1603`; no cursor gap. Bounded fresh-head inspection covered newly unseen seq 1601–1603 before sequential catch-up.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Fresh-head seq 1601–1603 was inspected first. Danaher Sales Engineer and Arrow Field Sales Engineer were terminally screened as outside the primary engineering role families. Manulife Back End Software Engineer (Chengdu, JR26091108) survived the cheap screen and GitHub-history dedupe, but no independent exact current employer-controlled liveness + usable application-route evidence could be established in this run; FreeHire metadata alone was not treated as proof, so it was not promoted. Sequential cursor remains 213 because no later historical event was advanced across unresolved/uninspected history. No application or outreach was performed.`

## Current receipt

- completed run time: `2026-10-10 04:47 MYT`
- SG lanes tried: `targeted direct-employer/ATS junior software-engineering gap search plus current SG surfaces; routine FreeHire broad coverage was not recreated`
- SG coverage: `6 distinct candidates / 6 employers / 3 source families / 1 deep-verified`
- CN lanes tried: `51job current/indexed Shanghai and Shenzhen Python/backend/data/AI-application surfaces; attempted latest CN Discovery artifact inspection first, but the available GitHub connector rejected the Actions-artifact endpoint, so artifact rows were not used and discovery fell back to native sources`
- CN coverage: `14 distinct candidates / 13 employers / 1 source family / 0 deep-verified`
- serious-survivor Issues created/updated: `#194 Eureka Robotics — Software Engineer (APPLY)`
- concrete filters / regressions exercised: `SG: current MCF-only roles were blocked unless a separate route existed; recruiter/staffing and senior 6+ YOE results were rejected. Eureka Robotics was independently verified on the employer Breezy ATS with a live Singapore Software Engineer opening, fresh-graduate eligibility and an active non-MCF Apply action; GitHub and both Gmail accounts showed no prior application/contact, so #194 was promoted. CN: 51job surfaces produced multiple 3+ YOE, outsourcing/staffing, domain-heavy or otherwise weaker candidates; none cleared the full Stage 2 gate this window.`
- concrete access/write issues: `Latest CN Discovery GitHub Actions artifact could not be inspected because the available GitHub connector rejected the artifact-list endpoint; native-source fallback was used. Both Gmail accounts were checked with a small overlap window: one had no new mail; the other had one LinkedIn saved-job reminder, classified DISCOVERY_NOISE, with no lifecycle state change. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate away from Eureka/direct robotics toward direct product/ATS healthtech, B2B SaaS and industrial-software employers not already covered. CN should rotate from this 51job-heavy Shanghai/Shenzhen pass to 猎聘/direct-employer/智联 0–3 year backend/full-stack/AI-application roles in 上海/深圳/南京, and inspect the CN Discovery artifact first when connector access permits.`
