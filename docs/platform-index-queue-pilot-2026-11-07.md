# SG/MY Platform Index → Durable Candidate Queue: pilot 2026-11-07

**Status: deterministic ingestion and evidence-backed consumption tested; unattended search-index source NOT deployed.**

This is machine-only source checkpoint state, **not a second human application tracker**. Only verified GitHub Issues are actionable APPLY/CHECK. Current records are public job identifiers/URLs, never applicant data.

## Evidence: source accessibility

- GitHub native platform benchmark (12 routes): https://github.com/kolihhan/job-resources/actions/runs/42350155908
  - SG/MY JobStreet/Indeed blocked at HTTP 403 from this runner; LinkedIn/Hiredly/MCF returned HTML but no independently proven source-specific page-2 job identities. CN Zhaopin exposed 20 source-local links but returned essentially the same set / generic query.
- Keyless search-index pilot (Bing RSS + DDG HTML): https://github.com/kolihhan/job-resources/actions/runs/42350561189
  - 6 targeted SG/MY platform queries × 2 public index providers = **12 calls**, HTTP response bodies received, **0 normalized exact-role job URLs**. This collector **must not** run as a purported working scheduled source.
  - These particular results do not prove all paid search APIs, all query wording, or alternative browser/connector providers will fail. They do establish that the tested free transport is **not an operational feed**.
- The web-side manual index handoff used four exact-role source links observed and rechecked this turn. Inputs are pinned under `tests/fixtures/platform-index-{sg,my}-2026-11-07.json` only for reproducible tests. They are NOT automatically refreshed.

## Durable queue, tested with actual GitHub Action pushes

- Intake: https://github.com/kolihhan/job-resources/actions/runs/42351067020
- Consumer acknowledgements: https://github.com/kolihhan/job-resources/actions/runs/42351276237
- Queue state: `discovery-state/platform-index-sg.json`, `discovery-state/platform-index-my.json`.
- Script: `scripts/platform_index_queue.py`, test: `tests/test_platform_index_queue.py`.
- Original observed source IDs: SG LinkedIn 4456087297 and JobStreet 95566693; MY Indeed 3375a1020f56547c and LinkedIn 4474680448.
- Each market received 2 machine-unverified observations. Strong known-history URL matches are auto-dispositioned only when exact; weak company/title matches are **not** silently discarded. Reingestion is idempotent, candidate seq is stable.
- **SG:** Tech Aalto JobStreet 95566693 hard rejected with employer-authored 5-year experience requirement; PERSOL APAC LinkedIn 4456087297 remains pending.
- **MY:** Coca-Cola AI Engineer LinkedIn 4474680448 (separate from already-applied junior role) hard rejected with employer-authored 5–7 year expectation; Oxydata Indeed 3375a1020f56547c remains pending.
- Both persisted queues have `next_unacknowledged_seq=1`, one terminal evidenced hard reject, one pending candidate. The consumed second row cannot advance past the unresolved first row.
- Terminations require evidence URLs and detailed reasons. Duplicate/Issue promotions require actual live GitHub Issue API readback verifying the exact candidate URL in the Issue body; a model-generated boolean cannot acknowledge work. Workflow pushes are optimistic, merging fresh state on conflict, then re-reading from origin.

## How to operate next

The hourly SG/MY Scout prompts now explicitly read the machine queue **before** their wider search rotation. This is an instruction, **not a technical guarantee**: the independent source of truth is the `pending` records and their verified receipts, not Scheduler's final message. If a scout skips a pending row, the row survives; the next run gets the same pending seq. When it finishes a candidate, it must submit a valid receipt to the deterministic script, and persist the resulting state with read-back. No Issue can be created from an index snippet alone.

`python scripts/platform_index_queue.py next --state discovery-state/platform-index-sg.json --limit 20`

`python scripts/platform_index_queue.py ack --state discovery-state/platform-index-sg.json --receipt receipt.json`

`ISSUE_VERIFIED` and `DUPLICATE_CONFIRMED` use a fresh GitHub API check of `receipt.issue_url` and its exact job identity. The script needs `GITHUB_TOKEN` for that case.

## Critical remaining dependency: genuinely unattended SG/MY platform index

Bing RSS and DuckDuckGo HTML were empirically unsuitable for this deployment. The source must supply exact-role job URLs in a permitted, machine-readable format and with acceptable storage rights. A compliant indexed-search API/connector or a provider-supported jobs API is required; **no key or contract was connected in this pilot**. Do not schedule a no-op scraper, pretend that source attempts equal market coverage, or turn on a credentialed search service without explicit authorization and its own terms review.

Next source integration acceptance: obtain at least 20 unique exact-role URLs across independent fresh SG/MY platform queries, track per-query result-page novelty and date, write queue with all-history strong URL suppression, and show at least one fully verified non-duplicate handoff to APPLY/CHECK (or a reproducible, complete reason for no survivor). Never use search result totals as a proxy.

## Live SG/MY structured-feed collector: production source, not native platform (2026-11-07)

- Public JSON discovery source: [Dev Global Jobs](https://devglobaljobs.com), visibly attributed as *Powered by Dev Global Jobs*; separate Tier-3 / aggregator family, not a native LinkedIn/JobStreet Hiredly/Indeed sweep.
- Verified source-pilot: https://github.com/kolihhan/job-resources/actions/runs/42355276934 ; verified intake: https://github.com/kolihhan/job-resources/actions/runs/42355824573 ; scheduled workflow checked at https://github.com/kolihhan/job-resources/actions/runs/42356158073 .
- Active bounded schedule in `.github/workflows/sg-my-structured-feed-intake.yml`: `40 2,14 * * *` UTC (10:40 and 22:40 MYT). Deterministic two 50-row API pages maximum per market/search; "BOUNDED_SOURCE_END" is only an end marker for the *given API query*, never broad job market coverage.
- Actual SG query `AI`: **67 source rows across offsets 0 and 50**, **9 distinct source-ID role observations** after technical-title, non-senior-title and Singapore-location screening. MY: **2 raw rows, zero matching AI engineering titles**. Inputs are not proof of fresh live employer requisitions or sponsorship.
- Normalized source IDs `devglobaljobs.com/jobs/detail/<id>` are persisted under `discovery-state/platform-index-sg.json`. Idempotent re-observation fills missing company names (confirmed OpenAI 7, Binance 2) without resetting existing candidate seq/disposition. This is a real, scheduled source, not a fixture-only test. It is **not** an automated native platform index.
- Following first-party JD research, **six of nine** newly ingested SG roles failed explicit senior technical experience / specialism / non-permanent internship gates: OpenAI Codex applied engineer, Korean and weekend support, Mandarin Startups applied engineer, Cyber applied engineer, and the Binance Tech Seeds accelerator internship. The corresponding exact-key, official-JD linked rejection receipts were consumed in successful Actions run https://github.com/kolihhan/job-resources/actions/runs/42356566732 and independently read back.
- **Three remaining pending seq values: 6, 7, 9**. Seq 6 Binance AI Agent Engineer resembles existing [APPLY Issue #861](https://github.com/kolihhan/job-resources/issues/861) (official requisition 5002667101), but cross-source matching has **not yet proven the DevGlobal identity points to exactly that requisition**, so do not mark as duplicate based on title alone. Seq 7 OpenAI AI Support and seq 9 OpenAI Applied AI Engineer require authoritative exact-JD/experience checks before terminal disposition. The pending cursor is `6`. No new APPLY/CHECK Issues created from the feed.
- This feed has poor junior/research yield relative to raw volume; retained to supply real source candidates, but it does not solve JobStreet/LinkedIn native coverage nor show that Malaysia platform recall improved. Measure **verified net-new strong survivors**, not the raw nine. Keep original documented blockage of the keyless platform index.
