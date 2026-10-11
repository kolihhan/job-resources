# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-11 10:36 MYT` — healthy, `first_seq=1`, `last_seq=1808`; page index matches `first_seq=1 / last_seq=1808`; no cursor gap. Backlog is 1590 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 1808. Fresh head 1806–1808 inspected: 1806 is a stale August FPT listing with a 5+ YOE hint; 1807 is a 5+ YOE Java/mobile role; 1808 is an IO Tech Solutions Java investment-bank remote-China listing and does not clear the direct-employer/fit promotion gate. No survivor promoted. Cursor remains 218 because seq 219 is still unresolved; no cursor jump across unresolved history.`

## Current receipt

- completed run time: `2026-10-11 16:53 MYT`
- SG lanes tried: `targeted direct-ATS fintech/enterprise SaaS/data-platform and fresh-graduate backend/software gap searches; routine FreeHire broad coverage was not recreated`
- SG coverage: `limited current search; 0 serious candidates reached deep verification / 0 deep-verified`
- CN lanes tried: `attempted latest CN Discovery artifact endpoint first; connector still rejected the Actions artifact-list endpoint, then native-source fallback searched current 牛客/direct-web surfaces for Shanghai backend/full-stack/platform/AI roles and early-career social-hire listings`
- CN coverage: `6 distinct candidates / 5 employers / 3 source families / 0 deep-verified`
- serious-survivor Issues created/updated: `none`
- concrete filters / regressions exercised: `CN exact results included a current 九方云 AI/full-stack role explicitly restricted to 2027 graduates, a 齐柏林 Go backend role requiring 3+ years plus Go, and a 声网 data-platform campus role already ended; other native results were stale, agency-led, hard-seniority mismatches, or outside the target role/market lane. SG targeted gap queries produced no new candidate that cleared cheap freshness/fit/dedupe gates; this is limited gap coverage, not evidence that the SG market is empty.`
- concrete access/write issues: `CN Discovery artifact listing remains unavailable through the current GitHub connector, so native-source fallback was used. Both Gmail accounts were checked with a four-hour overlap: lihhanko526 had only a Ping An assessment-login OTP, classified account/assessment access activity with no lifecycle state change; lihhanko3 had LinkedIn job alerts plus unrelated mail, classified DISCOVERY_NOISE. FreeHire Intake task 6ac7cca721b881919e1ebf120cc777d7 was verified enabled at run start. No application or outreach was performed.`
- next rotation: `FreeHire Intake continues its dedicated lane. SG gap search should rotate toward direct ATS healthtech/industrial software/cloud infrastructure and smaller product employers not already represented in Issues. CN should rotate toward 智联/51job and direct-employer social-hire pages for Shanghai/Shenzhen/Nanjing backend/platform/software roles, with 牛客社招 as secondary; inspect cn-raw artifact first if connector support becomes available.`
