# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- preferred fresh-review surface: `kolihhan/freehirefetch/feed/candidates.json`. It is a derived machine artifact, not a second human tracker.
- incremental behavior: `feed/candidates.json` now contains only AI/ML/research jobs that emitted `NEW` or `CHANGED` in the latest ingestion run. Unchanged old jobs are not repeated. Each candidate carries `event_kind` + monotonic `event_seq`, a short JD excerpt and deterministic AI-relevance signals.
- candidate hard reduction: explicit contract/fixed-term/temporary/part-time/freelance/internship/trainee employment is removed before the snapshot; the snapshot is capped at 10 candidates per market (30 total), while normal hourly delta runs should usually be much smaller.
- public health verified before the incremental change: `2026-10-25` — latest recorded worker state was healthy at `first_seq=1`, `last_seq=14372`; latest recorded delta completed at `2026-10-25T01:08:20.431674Z` with `new=10`, `changed=0` (`SG fetched=531`, `CN=66`, `MY=203`).
- worker correction: `2026-10-25` — `kolihhan/freehirefetch` PR #4 merged as `eb56a4f323652659ae374b16de2257c2b8a5423a`. `Senior` titles are downstream review hints rather than source-level hard drops; Staff/Principal/Lead/Manager/Director/Intern remain title hard drops. Singapore raw discovery is split into four engineering category windows and exact-deduped. This is a raw radar implementation only; category inclusion does not imply job-resources eligibility.
- first efficiency layer: `2026-10-25` — `kolihhan/freehirefetch` PR #5 merged as `9ff25a32bf17c0b86d7db5bf1dff45e91f6a36e9`, adding the bounded AI candidate snapshot.
- incremental efficiency layer: `2026-10-25` — `kolihhan/freehirefetch` PR #7 merged as `12e2f90f5213012a53cfc3562a8c44d41d61424a`. TDD RED was observed on CI #43; implementation CI #45 succeeded; post-merge main CI #47 succeeded. This removes repeated unchanged-candidate review and makes fresh AI intake event-driven.
- earlier worker correction: `2026-10-09` — stale-NEW regression fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`.
- intake mode: FreeHire ingestion runs hourly. Historical cursor catch-up remains preserved at 513 rather than guessed; fresh AI discovery should now consume the incremental candidate surface rather than traversing historical JSONL pages.

## Current receipt

- completed run: `2026-10-25 16:42 MYT scheduled maintenance + SG-gap/CN-native discovery`.
- maintenance: `ACTION remains 0. Inspected current APPLY/CHECK and both Gmail accounts for recent lifecycle evidence. New LinkedIn receipts showed several user-submitted applications after the prior receipt.`
- lifecycle reconciliation: `Created #668 WAIT for Nas Company — AI Product Engineer - Nas.com (Suzhou, LinkedIn 4464328185) and #669 WAIT for BOKE Technology / 波克科技 — AI应用工程师 (Shanghai, LinkedIn 4466163556), both from exact LinkedIn application confirmations dated 2026-10-25. ThoughtFull AI Engineer acknowledgement is not a rejection and remains WAIT. NCS Python Developer is generic/non-AI from the available receipt and was not added to the AI queue. Xiaomi 算法工程师 receipt lacks enough JD evidence in this run to assert material AI relevance, so no new Issue was guessed.`
- discovery: `Completed SG-gap + CN-native searches for Applied AI / LLM-Agent-RAG / evaluation / research-engineering. No new verified survivor. NTU R00025937 is an exact duplicate of closed #597 and remains blocked by contract employment evidence. TOPPAN Ecquaria AI Engineer is already #214 WAIT. CN native results were predominantly 2027-only or already-ended; no 2026-compatible new survivor cleared the full gate.`
- FreeHire: `Preferred feed/candidates.json returned 404 during this run. Per RULES, did not guess or advance cursor; cursor remains 513. Direct SG gap and CN-native discovery continued independently.`
- employer-facing actions by this run: `none. No applications or messages were submitted.`
- next rotation: `Resolve the four CHECK blockers cheaply; continue SG direct/ATS AI evaluation/research + CN native 2026-compatible Applied-AI/Agent/search-retrieval lanes. Re-test FreeHire candidates.json only as the RULES-defined radar surface; do not infer cursor progress from the 404.`
