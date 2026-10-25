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

- completed run: `2026-10-25 15:29 MYT maintenance reconciliation after user confirmed all stale ACTION items were already handled`.
- workflow: `Reconciled GitHub operational state against the user's latest direct confirmation and Gmail evidence instead of treating stale Issue labels as real pending work.`
- target contract: `Permanent full-time AI-related careers only across SG + CN + MY. Research Engineer / AI Researcher / Applied Scientist / Research Scientist are explicitly in scope when hard requirements are realistic.`
- queue reconciliation: `Moved #599 StarHub, #595 AI Singapore AI Products, #575 Huawei 大模型Agent, #536 ChinaAMC, #468 Tencent PCG Agent, #419 iFLYTEK J14502, #297 Maxify and #220 杭州赢云 from stale ACTION to WAIT. Open ACTION is now 0.`
- Maxify correction: `#297 is one existing pipeline, not a new second process. The 2026-10-23 Next Step email to lihhanko526 duplicated the earlier screening stage already completed through lihhanko3. GPA/start timing/PrinciplesYou had been sent in September; prototype ZIP was submitted 2026-10-21 and followed up 2026-10-23. Current state is WAIT for a real post-prototype response.`
- iFLYTEK note: `Gmail contains official 科大讯飞 application acknowledgement on 2026-10-22, but the email does not expose requisition J14502. User confirmation establishes the ACTION was handled; do not claim the receipt proves that exact req ID.`
- current open queue snapshot: `ACTION 0 / APPLY 28 / CHECK 4`.
- current CHECK: `#641 Sunway Digital employment-type conflict; #664 TAPiO employment type unresolved; #665 Kuailu exact usable non-MCF route unresolved; #666 Bjak prior application identity unresolved.`
- employer-facing actions in this reconciliation: `none. This run only corrected GitHub state; it did not submit applications, send recruiter messages, or contact employers.`
- next rotation: `Do not infer a pending-action backlog from stale labels. With ACTION=0, the next useful work is to (a) resolve the four CHECK blockers cheaply, (b) prune/rank the 28 APPLY items by value × fit × callback realism × friction, and (c) continue fresh AI-only discovery only where it adds genuinely better opportunities rather than duplicates.`
