# Fresh Discovery coverage — independent source/consumer research (2026-11-09 MYT)

## Decision

**Verified root cause is multi-layered, not insufficient prompt length.** Original SG/MY/CN native search pages do not reliably yield query-matched page-two job IDs in the unattended GitHub Actions host; the available unattended first-party producers are concentrated in a tiny employer set; the resulting verified first-party JD candidates frequently wait without a complete human/agent fit and hiring-route decision. FreeHire cursor/checkpoint work can consume an hourly Chat Scout run even when current official discovery was not persisted. **Do not interpret any absence of new Issues as proof of job-market exhaustion.**

This document is a bounded research evidence record. It is NOT another opportunities queue; GitHub Issues remain the sole actionable APPLY/CHECK/WAIT state.

## Direct evidence — system baseline

1. **12 native HTML job-board probes → 0 sources passed query-relevant, distinct page-two coverage in this host**. LinkedIn challenge page, JobStreet/Indeed 403, Hiredly/MCF shells; Chinese sources partial/repeated pages. See [platform feasibility](platform-feasibility-2026-11-07.md) and [independent action rerun](https://github.com/kolihhan/job-resources/actions/runs/42350155908). This is a host-and-endpoint result, not a claim all native sites are universally blocked.
2. **Fresh-state / actual execution drift (read 2026-11-09):** SG fresh source checkpoint last completed 2026-11-07 10:57 MYT with 9 coverage debts despite subsequent official-JD research and FreeHire checkpoints. MY last completed 2026-11-08 09:18 with 5 debts. CN last completed 2026-11-08 20:10 with 7 debts. Calendar-based scheduling and a source attempt are not source coverage or state advancement.
3. **Source producer concentration:** SG official queue has 17 NTU JD-verified pending and 1 aggregator pending; MY official queue has 2 Gen Digital/MoneyLion JD-verified pending. Those are technical *source candidates*, not eligibility decisions. Source-producing workflows run, but `FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW` is deliberately not an Issue ack. See [live first-party consumer architecture](firstparty-consumer-health-2026-11-07.md).
4. **Metrics evidence:** 2026-11-07 and 2026-11-08 scout JSONL records are overwhelmingly `PARTIAL_COVERAGE`; SG Fresh Discovery remains difficult to durably finish, and verified new APPLY/CHECK in those tracked automated runs was 0. Later Chat-created Issues #872/#873/#874 are independent and must not be credited to those Scout runs. Current retry counts/FreeHire cursor changes are not discovery success.
5. **Blind source breadth remains missing:** keyless Bing RSS/DDG source experiment obtained 0 normalized exact-job links across 12 requests. The installed interactive Indeed app returned 10 jobs from a query showing 274 available, but this is one-query UI evidence, *not* a paginated unattended feed; the sample included older/irrelevant postings. Do not represent a UI widget or result-total as durable native platform breadth.

## Independent first-party ATS proof (actual Actions runs)

Official vendor contracts: [Greenhouse public Job Board GET](https://docs.greenhouse.io/job-board), [Ashby public Job Posting GET](https://developers.ashbyhq.com/docs/public-job-posting-api), [SmartRecruiters public Posting API](https://developers.smartrecruiters.com/docs/endpoints). These are **company-board feeds**, not a global job index. GET lists are public; applicant submissions and authentication are separate. Only public GET used.

- Code: `scripts/probe_firstparty_ats_coverage.py`
- Regression tests: `tests/test_firstparty_ats_coverage.py`
- Read-only evidence artifact / Actions run: [final rerun 42499694425](https://github.com/kolihhan/job-resources/actions/runs/42499694425). **8 tests passed, 4 bounded public company-board probes executed.**
- Independent original pilot: [42499355527](https://github.com/kolihhan/job-resources/actions/runs/42499355527). Follow-up [42499673460](https://github.com/kolihhan/job-resources/actions/runs/42499673460) independently repeated live source outcomes. These probes do not modify user/applicant or opportunity state.

| Market / source | Public board rows observed | Local technical title signals | JD-probed role signals | Real source assessment |
|---|---:|---:|---:|---|
| SG Stripe / Greenhouse | 766 global | 3 | **0** after disqualifying an AI sales/account role | API and complete list proven; very low targeted engineering yield |
| MY New Era / Greenhouse | 77 global | 2 | **2** | Complete list and JDs proven; exact 8870366002 was *already* CHECK #872, 8829792002 is a Data Engineer title not yet a verified North-Star survivor |
| SG NCS / SmartRecruiters | 200 from first 2 pages | 45 | **12** with JDs | Strong source feasibility, but **partial pagination/deep-read budget**; titles include generic graduate SWE/analytics/consulting. Need actual JD gates, not keyword promotion |
| MY Bjak / Ashby | Unknown | Unknown | 0 | **SOURCE_ERROR**: entire public payload exceeded 8 MB, and a 24 MB bounded retry also exceeded cap; do not count as scanned or zero vacancies |

**The NCS 12 and New Era 2 are source-derived, not newly eligible jobs.** Exact GitHub Issues ID history checks of the 15 original signals found prior New Era #872 and no exact ID matches for the remaining probes, but unknown IDs do NOT imply 14 actionable vacancies. For example NCS's "[Nov 2026 & Jan 2027 Intake] AI Software Engineer" employer full JD is mostly generic web software development, despite title; its campaign dates/foreign hiring eligibility require their own verification. A related NCS Fullstack AI Applications employer JD lists junior 2–4 years and real cloud AI deployment requirements. This supports full-JD technical classification before issue promotion, not blanket source acceptance.

## Causal model and counter-hypotheses

- **Blocked native platform coverage → repeated weak indexed snippets / no reliable pagination.** Changing a Chat instruction cannot force a blocked source to return page-two identities. Independent official ATS, permissioned native search/search-index provider or a suitable connector are credible alternatives; the tested free public indices are not.
- **Employer-board under-diversification → successful but narrow discovery.** NTU + Gen Digital have good producer reliability yet systematically miss most SG/MY companies, regardless of scanning frequency. Stripe negative control shows broad API availability alone is not enough.
- **Producer-consumer disconnect → new identities are not reliably converted.** Current first-party queues already contain multiple fully JD-verified roles awaiting a bounded fit/eligibility reviewer. Scheduling more feeds without resolving this handoff risks a larger unresolved queue, not higher viable yield.
- **Task budget is split into incompatible obligations.** Native two-page probes often impossible; FreeHire shard/retry and strict completeness rules take time. Mandatory source-depth accounting is useful for honesty, but do not force a blocked page into a repeated full-run blocker when an independently verified official substitute can make actual candidate decisions.
- **Alternative explanation still plausible:** even with better first-party coverage, many actual roles may be experienced-hire, content-weak, already applied, have cohort restrictions, or lack foreign-work-pass routes. Do NOT assume source throughput automatically raises APPLY yield. This needs a prospective pilot with independent employers and rejected-case audits.

## Recommended production repair — gated, not prematurely deployed

1. **Source collection:** retain the tested four-source pilot as read-only. Select new official boards based on demonstrated **local, substantial, early-career AI/Agent/RAG work**, not job-row total, logo, or a single matching title; include *at least one unrelated company/board on an independent run* to guard against overfitting to NCS/New Era. Never add an automatic repeating source before live list, detail, region, freshness and publisher rights/limits are checked.
2. **Machine intake:** use existing `platform-index-{sg,my}.json` and `platform_index_queue.py` only after canonical URL support for a proven new ATS is added with tests. Keep official source identity, exact posting ID, employer URL, source timestamp and pending state. An uncertain role survives; source and Issue history cannot be conflated. Keep a per-source cursor or content hash; no second user-visible job tracker.
3. **Consumer handoff FIRST:** process the existing SG 17 / MY 2 official-JD-verified pending cases with high-value-first bounded *actual* full-JD + hard-requirement/route review; terminally acknowledge only evidence-backed rejection/duplicate; write an Issue for a newly viable role only after all RULES gates and Gmail dedupe. Preserve others as pending. An official JD verified stage is not DONE.
4. **Native coverage gaps:** do not claim first-party NCS coverage solves LinkedIn/JobStreet/Indeed/BOSS breadth. For blocked native pages, use an actually authorized indexed search connector or credible employer ATS role details as a **named substitute source**; record original native page `0`, substitute source exact IDs and the remaining debt. The interactive Indeed app proves a possible manual query path only, not a recurring unattended index feed.
5. **Source-selection governance:** maintain a source-specific `local exact roles → JD read → fit-qualified → unique APPLY/CHECK` funnel in existing metrics, with separate count of recurring identity overlaps, hard YOE/cohort blockers, false-positive title matches, source error and page-depth debt. No artificial Issue target.

### Acceptance & failure criteria

- **Pilot must deliver** at least one independent, real NEW exact-requisition sourced from a previously undercovered employer, an employer-authored substantive JD, verified current apply route and a GitHub/Gmail identity check, ending with a correctly read-back APPLY/CHECK **or** an evidenced hard-reject/no-survivor decision. It must do so without relaxing hard role/employment/visa gates.
- **Coverage proof** means truthful page/offset/exhaustion from official source + source-local exact IDs, not raw 200 rows, 403/challenge HTML, generic index hit totals or a successful workflow exit.
- **Generalization test:** compare at least two independent post-change source/market rotations and sample rejected/undercovered engineering and research candidates. If only NCS returns jobs, if historical applicants reappear as NEW, or if CHECK is inflated by multiple blockers, this experiment has **not** improved usable coverage.
- **Current verdict (2026-11-09):** first-party API feasibility improved and tested; **no source expansion scheduled, no new automated APPLY/CHECK produced, native full-market breadth and pending-review handoff remain unresolved.** Do not report the system as fixed.

## Immediate decision

**GO on producer/consumer handoff and a source-owner diversity trial. NO-GO on blindly expanding FreeHire, retry loops, unsupported HTML pagination, or auto-promoting ATS title matches.** The four-source read-only pilot is a verified experimental instrument, not a production discovery fix.
