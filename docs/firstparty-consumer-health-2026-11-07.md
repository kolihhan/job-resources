# SG / MY first-party producer, conservative consumer & health — 2026-11-07

## Operational outcome (live GitHub Actions, not a simulated plan)

### SG — official NTU research careers
- Source: NTU Workday CXS `scripts/collect_ntu_llm_source.py`, scheduled daily at 09:35 MYT; produces exact first-party requisition URLs and explicit `canApply` checks.
- Machine state: `discovery-state/platform-index-sg.json`; GitHub Issues are **the sole APPLY/CHECK/WAIT state**.
- Consumer: `scripts/consume_platform_queue.py`, workflow `.github/workflows/sg-conservative-consumer.yml`, 4 runs/day at 05:20/11:20/17:20/23:20 MYT. Uses GitHub complete Issue history before asserting exact-ID uniqueness; confirms exact Issue via authenticated readback, then acknowledges; verifies authoritative Workday `jobReqId`, `canApply`, and full JD.
- **Evidence of first real run:** https://github.com/kolihhan/job-resources/actions/runs/42366491294 — 12 considered, 11 first-party JDs verified, one third-party link classified as needing an employer-controlled route, zero errors. Persisted state readback succeeded. No promotions/APPLY were fabricated.
- Terminal auto-actions are restricted to exact employer `canApply=false` with matching requisition or live-verified exact GitHub Issue. All others remain pending with `consumer_review` evidence, stage and content hash. No application is sent.

### MY TOP — Gen Digital / MoneyLion, Ashby
- Official public employer Ashby board API: `scripts/probe_gen_digital_ashby.py`; official source observed 107 current board jobs, 9 MY technical-title signals including 6 mature title roles.
- Quality-first producer `scripts/collect_gen_digital_my.py`, scheduled daily 11:35 MYT in `.github/workflows/my-gen-digital-intake.yml`. It retains full source evidence in the Actions artifact, sends 3 non-mature role IDs to the **existing MY machine queue**, and suppresses exact strong URL history duplicates. Senior/manager title exclusions are a *source focus choice*, not a universal hard reject: raw records remain inspectable.
- **Live producer evidence:** https://github.com/kolihhan/job-resources/actions/runs/42367485843 — 3 observed source identities accounted for, one matched existing history and 2 new pending with exact IDs:
  - Machine Learning Engineer — MoneyLion: `2f170362-7e3b-48a2-956e-1bac730a7d1d`
  - AI Applied Scientist — Gen Digital: `c35bae67-de6c-45b7-b116-4c30a8c6ac73`
- MY consumer `scripts/consume_my_ashby_queue.py`, workflow `.github/workflows/my-conservative-consumer.yml`, twice daily at 00:15/12:15 MYT. Reads public official complete Ashby board plus full GitHub Issue history; verifies exact job identity, location, source URL and substantive JD, persists review data, leaves unknowns pending.
- **Real consumer evidence:** https://github.com/kolihhan/job-resources/actions/runs/42367727977 — 2 first-party JDs verified, 0 errors, 2 pending for human-level fit judgment, no auto-application.

### Platform coverage feasibility guard
- Grab official SmartRecruiters pilot: https://github.com/kolihhan/job-resources/actions/runs/42366991468 .
- Public API returns 448 unfiltered roles; the country parameter returned 0 even though the source contains MY/SG jobs. Client-side source-country verification recovered 6 MY + 12 SG exact official details in a 300-row bounded slice per market.
- Most were mature Data Scientist/People Analytics roles. **This pilot is not scheduled as a productive MY/SG North-Star source**, and none of the 18 are claimed as newly eligible APPLY roles.
- LinkedIn/JobStreet/Indeed original platform index remains unproven as a stable unattended feed; do not generalize first-party ATS success to native job boards.

## Pipeline health without a second tracker
- Script: `scripts/report_job_pipeline_health.py`.
- Workflow: `.github/workflows/job-pipeline-health.yml`, daily 20:05 MYT, read-only, with GitHub Actions summary and temporary evidence artifact.
- **Verified report run:** https://github.com/kolihhan/job-resources/actions/runs/42367934121 .
- Snapshot after first SG+MY consumer runs:
  - SG: **18 pending** source IDs, **11 official JDs fit-review-ready**, **6 uninspected**, **0 source errors**; pending cursor `6`.
  - MY: **2 pending**, **2 first-party JDs fit-review-ready**, **0 uninspected**, **0 source errors**; pending cursor `4`.
- Reports source concentrations, oldest pending age, source vs review state, last source ingestion and actual Actions run conclusions. It **distinguishes scheduled-execution evidence from merely having a cron definition**, and explicitly excludes CN state from SG/MY queue figures. It does not measure whole-market recall or make "X jobs available" assertions.

## Why this design is conservative
- Source IDs are **candidate signals**. Only exact, live employer evidence can establish requisition identity and current JD; eligibility, North-Star fit, term quality, work rights and genuine application route still need the RULES.md review.
- `consumer_review.stage=FIRST_PARTY_JD_VERIFIED_NEEDS_FIT_REVIEW` is **not a terminal ack**. It leaves the candidate in the persisted queue for AI/human technical judgment. This is intentional fail-closed behavior, not a completed autonomous APPLY pipeline.
- GitHub Issue history is fetched through the authenticated API, paged and fail-closed. An unavailable API cannot be interpreted as "no duplicate." Issue promotions/duplicate acks require fresh exact Issue readback.
- No external applications, recruiter messages or Gmail mutations occur in these Actions workflows.

## Remaining engineering work
1. Bounded fit reviewer for official, already-JD-verified pending roles; preserve role-specific mandatory-gate evidence. Do not map regex matches directly to APPLY/REJECT.
2. More **independent, high-fit first-party** sources for SG and MY beyond NTU and Gen Digital. A broad source feed whose output is mostly senior roles is not a recall breakthrough.
3. CN durable source consumer/queue and native platform gaps remain separate; the SG/MY health report must not be treated as complete coverage.
4. Track verified *net-new* APPLY/CHECK, genuine application actions, response and interview outcomes over time; source counts alone are not success metrics.

## Reproducible controls
- `python scripts/consume_platform_queue.py --state discovery-state/platform-index-sg.json --output artifacts/sg-consumer.json --limit 12` (GitHub token required)
- `python scripts/consume_my_ashby_queue.py --state discovery-state/platform-index-my.json --output artifacts/my-consumer.json --limit 12` (GitHub token required)
- `python scripts/report_job_pipeline_health.py --out artifacts/health.json --summary artifacts/health.md` (GitHub token required)

Successful test runs demonstrate exact identity, conservative failure handling and queue persistence, **not** that the system has applied for any position.
