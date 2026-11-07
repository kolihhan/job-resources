# Source feasibility pilot — 2026-11-07

## Objective

Test whether **GitHub-hosted** public-source discovery works in reality, not whether a workflow exits 0. This is an engineering evidence note, **not** a second candidate inbox. GitHub Issues remain the sole live opportunity state, and PROFILE/RULES still govern every hiring decision.

### Evidence

- Pilot GitHub Actions run: https://github.com/kolihhan/job-resources/actions/runs/42347724795
- Pilot artifact: `source-feasibility`, including `source-feasibility.json`, `liepin-feasibility.json` and the collector log
- Scripts: `scripts/probe_source_feasibility.py` and `scripts/liepin_discovery.mjs`
- The probe is read-only, bounded, and uses public GET API endpoints / the existing read-only Liepin adapter. The role counts are **observed public listing identities**, not unique eligible jobs or applications.

| Public feed | List identities | Target region locations in sampled result | Detail | Evidence/routing decision |
|---|---:|---|---|---|
| Stripe Greenhouse | 765 | SG 48 | GET full JD JSON works | **Actions-ready for bounded SG source ownership**; dedupe and eligibility still required |
| Binance Lever | 4 | SG 0 / MY 0 / CN 0 | GET detail works | Endpoint works, but this board has no relevant observed local supply; don't assign MY/SG/CN broad-scout coverage to it |
| Ramp Ashby | 171 | SG 0 / MY 0 / CN 0 | Inline description works | Endpoint works but no observed target-region jobs; no routine coverage credit |
| Visa SmartRecruiters | 0 | n/a | not tested | Returned `totalFound=0`; **not proof of IP blocking**; check canonical company board identifier / whether board is currently empty before routing |
| Bosch SmartRecruiters | 0 | n/a | not tested | Same as above; do not mark source as healthy |
| Liepin Shenzhen / 大模型 | 82 | CN Shenzhen | **not** tested; list metadata only | Page 1: 40, page 2: 42 distinct, server reports 10 total pages. **Actions can fetch genuine second-page results** for this query; remaining 8 pages were not read |

The benchmark found actual AI candidate titles in Liepin metadata, but did not validate hard JD requirements, posting liveness, foreign-hire feasibility, exact historical dedupe or an application route. Do not create APPLY/CHECK Issues solely from these observations.

## Counter-evidence and failure modes

- Increasing the old CN collection to a one-shot **3 cities × 6 queries × 2 pages** resulted in `Liepin response flag=0` and failed the run: https://github.com/kolihhan/job-resources/actions/runs/42347942068.
- A subsequent small Beijing/AI-engineer slice reported `fetch failed`: https://github.com/kolihhan/job-resources/actions/runs/42348230144.
- Neither error alone proves permanent IP banning or that GitHub can never fetch these regions. **Source × city × query × time × request volume matters**. Preserve failures and try official ATS/alternate paths, never loop the same failed request indefinitely.

## Routing decision (pilot)

1. **Automate proven public ATS feeds** with a source-owned canonical company/ATS identity. Greenhouse/Lever/Ashby are API *types*, not a blanket guarantee for all employers or markets; onboard actual employers only after live locale and detail checks.
2. **CN Liepin:** use small bounded, rotated collection slices and capture every page's source IDs and the next page / failure; do not run a large 36-request burst. Missing pages remain coverage debt.
3. **Native blocked / empty sources:** mark the exact source/query `BLOCKED_SOURCE` or `EMPTY_UNVERIFIED`, switch to official careers/ATS and indexed exact-role discovery. A 0-row result is not a market-wide no-jobs conclusion.
4. **Job promotion remains separate:** programmatic cheap-screen and exact historical Issue check first, then authoritative full JD, hard requirements, liveness, work-pass/foreign-hire gate, employer application route and targeted Gmail dedupe; only verified serious survivors may become GitHub Issues.

## Candidate handoff and acceptance

The CN workflow builds `cn-source-manifest.json` plus 25-row `cn-source-candidates-*.json` shards **inside the same expiring GitHub Actions artifact**, while retaining `liepin-raw.json` and `jobpro-raw.json` for audit. The manifest reports distinct source IDs, considered candidates, low-signal rows retained in raw evidence, and an identity SHA-256. Its explicit status is `AWAITING_VERIFICATION`, **never DONE or APPLY**.

**Remaining gap:** this ephemeral artifact is a verified *producer handoff*, not a durable consumed queue. No scout may advance a source-consumption watermark on artifact creation alone. Before full rollout, implement minimal producer/consumer acknowledgement in existing market-owned discovery state: `run_id`, artifact hash, candidate count, last consumed ID or offset, pending count, and expiry; require actual successful handoff/terminal disposition per candidate. Do not create a second human application tracker. The receiver must read manifest-listed shards and perform Issue-history dedupe with read-back, retry/error receipts and metrics, rather than promise to process them in a prompt.

**Acceptance gates:** nonzero exact role identity (or truthful BLOCKED); page two or proven exhaustion where available; bounded failures with source evidence; artifact and manifest count/hash reconciliation; consumer acknowledgement before DONE; and a real verified APPLY/CHECK increase (or explicit no eligible survivors after actual JDs). Workflow success or number of attempted sites alone does not satisfy these gates.

## Follow-up CN production trial — verified

Run: https://github.com/kolihhan/job-resources/actions/runs/42348597735

- The previously monolithic 36-request collection was replaced by a deterministic nine-slot rotation: one city, two query families, up to two pages each per execution. The schedule runs every three hours; a complete query-family rotation requires nine *successful* slots, not just nine workflow invocations.
- This run obtained **162 distinct Liepin jobs** from Shanghai Agent/Python backend, with two actual pages for each query. Each query reported 10 total pages: **pagination coverage remains incomplete**.
- The official-company adapter produced **1,263** unique source jobs, with **11 failed adapter calls**. It is a separate source family with partial failures; it cannot stand in for full job liveness/eligibility.
- Together the source collections yielded **1,425 unique source identities** (before exact GitHub Issue-history checks).
- The candidate handoff emitted **1,176 metadata candidates in 48 bounded 25-row shards**, with **70 known URL hints**. The manifest and all shards passed identity count/uniqueness/SHA-256 reconciliation.
- Raw job observations remain available in the expiring 30-day GitHub Actions artifact; the handoff is marked **AWAITING_VERIFICATION**. No full-JD candidate promotion or AI consumer acknowledgement occurred. **This must not be reported as 1,176 new APPLY opportunities.**

**Immediate downstream work:** Consume shards through a deterministic, durable consumer offset, prioritizing North-Star signals and full exact-identity dedupe, then authoritative JD and visa/application-route checks. Writing the manifest is **producer completion only**; do not mark the discovery-to-APPLY loop completed before the consumer has persisted verified outcomes. A 48-shard artifact is not an acceptable human-facing queue.
