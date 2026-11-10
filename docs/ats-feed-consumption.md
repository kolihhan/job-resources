# Public Source Batches → Private Fit Decisions

This is the production interface contract between `kolihhan/freehirefetch` and
`kolihhan/job-resources`. The higher-level `README.md`, `PROFILE.md`, and
`RULES.md` always govern applicant eligibility and Issue lifecycle.

## Source boundary: freehirefetch owns ALL generic batches

- Public FreeHire / AI Dev Jobs API collection: `freehirefetch/market_api_collect.py`
  and `feed/market-api/{SG,MY,CN}.json`, plus current `health.json`.
- Public first-party employer ATS board discovery: `freehirefetch/ats_discovery.py`
  and `feed/ats/markets/{SG,MY,CN}.json`, plus `feed/ats/health.json`.
- Public full-JD batches: `feed/ats/jd/index.json` **v2** maps exact role URL,
  title, market, source freshness and shard path to
  `feed/ats/jd/{SG,MY,CN}-NNN.json`. Match exact source key as well as URL/title.
- `feed/ats/changes.json` is ephemeral and NOT the lossless source snapshot.
- A FreeHire/AI Dev Jobs hit is an API-proxy signal, NOT proof that JobStreet,
  LinkedIn, Indeed, BOSS, 牛客 etc were scanned natively.
- Published public data must never include candidate profile, Gmail/Issue
  history, resume, applicant-specific model scores, work-right inference,
  application submissions or disposition.

`job-resources` must NOT independently re-fetch ATS boards or public job API
batches inside its default recurring intake workflow. Legacy one-off probes
may exist for manual diagnostics, but they do not count as the active source.

## Value boundary: job-resources owns ALL applicant decisions

The existing `.github/workflows/official-ats-intake.yml` imports upstream
snapshots into the **existing**
`discovery-state/platform-index-{sg,my,cn}.json` transport and publishes a
disposable review dispatch. Its `enrich_pending_public_ats.py` reads already
published full-JD shards; it does not contact employer APIs. Importing an
upstream JD is only evidence of role content, NEVER APPLY readiness.

`reconcile_pending_exact_issue.py` privately checks *all* live and closed
GitHub Issues before admitting more raw source candidates:
- An exact role URL + company + role title match to a single Issue may receive
  `DUPLICATE_CONFIRMED` terminal source ACK.
- A different platform URL with a matching company/title receives at most
  `consumer_review.possible_prior_issue` as a **REVIEW HINT**, not an automatic
  ACK. Identically named vacancies can have distinct requisitions and outcomes.
- A reviewer must independently match requisition, location, employer source,
  description or recruiting receipt before resolving a cross-platform alias.
- If the GitHub API is unavailable, leave Pending intact and do not infer
  no matches, empty market, or successful reconciliation.

Hourly SG/MY/CN Scouts convert *existing* Pending into value:
1. Read the pending queue FIRST, prefer actual full-JD entries, 0–3-year
   substantive Agent/LLM/RAG/evaluation/AI backend and MSc RA/RE equally.
2. Cheap-screen exact history and prior reviewer signals before further web
   searches or Gmail reads.
3. Verify current employer-authored exact JD, qualifications, candidate fit,
   employment, work rights and a usable apply route. `preferred` is not
   `required`; don't fabricate production AI years/cloud/ML systems experience.
4. Check both Gmail accounts for plausible APPLY promotions and any
   cross-platform prior-application hints. KEEP sibling requisitions distinct.
5. Create and READ BACK one authentic `[APPLY]` or one-blocker `[CHECK]`
   Issue with its matching status label; or record a reason-coded hard reject,
   exact history duplicate, or scoped retry. Then ACK ONLY handled source IDs.
6. Report distinct employers, exact employer JDs/route checks, newly verified
   APPLY/CHECK links, exact terminal ACK and unresolved older Pending. Do not
   claim source volume, tests, or a full queue as application value.

The default upstream and downstream market caps (including 45 Pending per
market) are backpressure limits, not success targets. When Pending is full,
increase **review/decision throughput** and preserve remaining upstream source
IDs rather than expanding private queues or creating another tracker.

## Hard cases to preserve

- **MY JobStreet:** a public job ID without a complete employer-authored JD
  is an unverified lead. An indexed summary may help locate the exact role, but
  do not infer detailed eligibility, high employer quality, or permission to
  create APPLY. Native website may block automated exact-page reads.
- **MY TOP:** only destination-quality technical teams / serious AI ownership
  or strong research value. Do not pad MY with generic AI-branded roles.
- **SG:** unknown EP/S Pass support may survive if no explicit prohibition;
  a role explicitly requiring candidates *already based in Singapore* is a
  location blocker for a Malaysia-based candidate.
- **CN source migration verified 2026-11-10:** `freehirefetch` public `feed/cn-native/` now publishes 3-hourly rotating Liepin and job-pro raw batches; `job-resources` reads those batches and builds only private Issue-aware source receipts and candidate decisions. Neither producer's 164 Liepin IDs nor 1,231 candidate handoff IDs are automatically APPLY; the private 45 Pending cap still limits queue admission.
- **CN:** native Liepin/BOSS/牛客 and academic HR/PI research coverage remains
  independently important. Foreign work-permit and campus cohort eligibility
  need verified employer policy; no forced PhD or work contract fiction.
- **Cross-platform duplicates:** Oppstar #640 (applied WAIT) and MIMOS #833
  (active CHECK) were separately surfaced through MY JobStreet on 2026-11-10.
  Their source aliases were manually ACKed with independent evidence. This
  justifies a *hint* mechanism, NOT fuzzy auto-merging for all employers.

## Success criterion

Count net-new, **not previously applied**, live and eligible APPLY/CHECK Issues
that pass role-content and employer-eligibility gates. Record reasons and queue
ageing separately; never claim the aspirational 100 as achieved from source
snapshots. Applicant submissions/contact are only permitted with explicit
user authorization.
