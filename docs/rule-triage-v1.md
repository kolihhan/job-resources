# Rule-based Scout Triage V1 — Dataset Audit + Safety Contract

## Why this exists

As of 2026-11-10, the three market Scouts consume a capped, lossy source
transport and spend substantial time repeatedly opening partial employer
listings. The highest-value workload reduction is **deterministic evidence
routing**, not synthetic eligibility scores or automatic Issue creation.

**Ownership:** `freehirefetch` discovers public jobs and batches public full
JDs. Only `job-resources` may compare those source facts with private user
requirements, prior Issue/Gmail history and disposition records. This module
adds no public candidate profile, private source export, new database, live
opportunity list or alternative tracker.

## Dataset survey (snapshot before implementation, 2026-11-10)

Read from default-branch `discovery-state/platform-index-{sg,my,cn}.json`:

| Market | Pending | Verified stored full JD | No verified stored full JD | Source excerpt HTML-marked | Terminal history |
|---|---:|---:|---:|---:|---:|
| SG | 45 | 27 | 18 | 22 | 46 |
| MY | 45 | 0 | 45 | 44 | 36 |
| CN | 42 | 3 | 39 | 21 | 21 |
| **Total** | **132** | **30** | **102** | **87** | **103** |

- All three Pending queues can fill to 45. This is a **capacity-censored
  active queue**, NOT a market-representative sample or accurate platform
  recall denominator. New ingestion changes counts between audit runs.
- MY: 44/45 Pending come from `freehire:public-api:MY`, one from public ATS.
  Source `description_excerpt` is generally HTML and capped near 240 chars.
  It is useful for a risk hint or source route, **not** a complete official JD.
- SG: 24 official ATS and 4 NTU/CXS Pending; 15 FreeHire and 2 DevGlobal.
  SG has the overwhelming majority of already verified full JD content.
- CN: 16 native Liepin, 23 FreeHire, 2 ATS, 1 AI Dev Jobs Pending in this
  snapshot; only 3 have current stored complete employer JD.
- Historical terminal dispositions are *not calibrated outcome labels*.
  Reasonless hard reject records existed in SG **3**, MY **16**, CN **5** in
  the initial survey. `HARD_REJECT` and `HARD_REJECTED` are used as separate
  historical strings in CN. `ISSUE_VERIFIED` does not distinguish APPLY from
  WAIT without live Issue readback. Never infer precision/recall from these
  noisy records or silently train a classifier against them.

## First independent real-queue dry-run (2026-11-10 14:48 UTC)

After implementing V1 and testing a real hidden failure, GitHub Actions run
[42837740726](https://github.com/kolihhan/job-resources/actions/runs/42837740726)
passed the complete **187-test** Python suite and produced this evidence:

| Market | Pending | JD_READY | HARD_REQUIREMENT_REVIEW | HISTORY_CHECK | LOW_PRIORITY_SOURCE_GAP | SOURCE_GAP |
|---|---:|---:|---:|---:|---:|---:|
| SG | 45 | 23 | 1 | 5 | 2 | 14 |
| MY | 45 | 0 | 0 | 3 | 6 | 36 |
| CN | 44 | 2 | 1 | 1 | 8 | 32 |
| **Total** | **134** | **25** | **2** | **9** | **16** | **82** |

- The two hard-condition *review flags* are **Grab People Research Scientist**
  (senior 8–12 years in JD) and **Pragmatike AI Hardware Engineer**
  (explicit workplace Hong Kong on CN source). They are NOT automatic
  `HARD_REJECTED` receipts.
- The first real replay incorrectly flagged NCS `#EG AI Developer
  (Agentic AI Systems)` because its JD says **2–5 years** and the original
  expression interpreted only the upper limit **5 years**. Fixed in
  `rule_triage.py` and added range tests (`2–5`, `2-5`, `2 — 5`,
  `3 to 5`). That role now stays `JD_READY` rather than being hidden.
- Historical `ISSUE_VERIFIED` controls are **not clean positive labels**;
  nevertheless the replay over 8 SG, 2 MY, and 2 CN terminal controls
  raised **zero** `HARD_REQUIREMENT_REVIEW` warnings. This does NOT prove
  deployment precision or future safety.
- The run did **zero automatic rejections, source terminal ACKs, applications
  or Issue creation**. `HISTORY_CHECK` 9, `LOW_PRIORITY_SOURCE_GAP` 16,
  `SOURCE_GAP` 82 are *routing outcomes*, not jobs filtered out of source
  history. Rule workpack scheduling is active; realized Scout throughput
  improvement remains unmeasured.

## Implementation: private deterministic screening

`scripts/rule_triage.py` reads the **existing** Pending/terminal source state.
It classifies every Pending item into one non-terminal work lane:

- `JD_READY`: fresh, recorded full first-party JD and material AI/LLM/research
  signals; prioritize one-pass fit+route review.
- `HARD_REQUIREMENT_REVIEW`: **fresh full employer JD** quotes an unusually
  strong negative condition: explicit existing-local-residence restriction,
  mandatory PhD, 4+ professional years plus requirement language, or explicit
  outside-market Hong Kong workplace for a CN source. **REVIEW REQUIRED,
  NOT AUTOMATIC REJECT**; inspect alternatives and full original JD.
- `HISTORY_CHECK`: previously seen *potential* Issue alias; requires exact
  requisition and Gmail history verification. No fuzzy automatic dedupe.
- `SCOPE_REVIEW`: source JD exists but target AI content isn't clearly proven.
- `SOURCE_GAP`: incomplete/absent/stale first-party JD; upstream evidence
  recovery before applicant eligibility decision.
- `LOW_PRIORITY_SOURCE_GAP`: no full JD and title hints at non-core or
  non-permanent work (e.g. robotics, hardware, presales, nonresearch ordinary
  contract); still preserved, never terminal ACK. Academic RA/RE contract
  exceptions remain active, as do soft 3+ year stretch roles.

Rules emit *literal employer-source quotes*, evidence type and code, not
unfounded probability, job-worth scores or eligibility verdicts. No rule
rejects on the absence of keywords in a 240-character snippet, company
marketing, broad AI title, Senior title alone or 3+ generic software years.

The existing `build_review_dispatch.py` now records per-market V1 lane
counts across **all** durable Pending and attaches the selected candidates'
rules and literal evidence to the **existing derived review-dispatch**.
The scheduled `Official ATS Durable Source Intake` workflow also emits an
ephemeral `artifacts/rule-triage.json` audit and reports its counts. This
artifact is NOT a second candidate tracker or permanent state.

## Testing and rollout decision

- `tests/test_rule_triage.py` covers required-vs-preferred, generic 3+ year
  stretch, 5+ explicit years, MSc-or-PhD alternatives, explicit residency,
  company HQ vs actual work location, CN Hong Kong case, non-core title,
  internship/contract research exception, stale JD, Issue alias, prompt
  injection as source text and noisy historical terminal labels.
- Whole Python suite in CI must pass; run the script against **the real
  active queue**, inspect lane counts and examples rather than tuning to a
  single replay or fabricated ideal sample.
- Keep `auto_reject=False`, `auto_ack=False` until separately evaluated
  positive controls and hard-blocker examples from independent time/source
  windows. Any eventual auto-ACK must have stronger exact employer evidence
  and preserve proper Issue/Gmail checks; do not enable from this V1.
- Success is fewer repeated JD fetches, more evidence-backed Scout dispositions
  per run, greater verified net-new APPLY/CHECK, and no new false exclusions.
  A successful CI run or high `SOURCE_GAP` count is **not** success on its own.

## Actual output

```bash
python scripts/rule_triage.py --repo . --output artifacts/rule-triage.json
```

The output says `PRIVATE_RULE_TRIAGE_DRY_RUN_NO_MUTATIONS`; no external
contact, source terminal change, application or GitHub Issue is made.
