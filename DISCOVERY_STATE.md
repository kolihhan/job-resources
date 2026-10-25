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

- completed run: `2026-10-25 six-battlefield strategy migration + active-queue reconciliation`.
- canonical strategy: `README.md`, `PROFILE.md` and `RULES.md` now define the North Star and six battlefields: `SG-ENG`, `SG-RES`, `CN-ENG`, `CN-RES`, `MY-ENG`, `MY-RES`. Singapore is quality-first, Mainland China supports higher-throughput native/direct discovery after hard filtering, and Malaysia is TOP / destination-quality only. Engineering and realistic research/research-engineering are both valid target outcomes.
- automation architecture: `SG AI Scout`, `CN AI Scout` and `MY TOP AI Scout` run hourly as read-only reconnaissance; `Recruiting Signal Watch` checks both Gmail accounts hourly for meaningful progression; `AI Job Strategy Review` compares all six battlefields weekly and recommends adaptive allocation. Scheduler prompts read the repo contract rather than maintaining a private copy of policy.
- verified active queue snapshot: `ACTION 0 / APPLY 31 / CHECK 7`.
- APPLY battlefield snapshot: `SG-ENG 5 / SG-RES 1 / CN-ENG 17 / CN-RES 2 / MY-ENG 6 / MY-RES 0`.
- CHECK battlefield snapshot: `CN-ENG 3 / MY-ENG 3 / MY-RES 1`; no current SG CHECK was found in this pass.
- Malaysia cleanup: `#664 TAPiO` and `#662 Mentix` were closed because current evidence showed good AI fit but did not clear the new MY destination-quality bar. `#647 Michael Page AI Software Engineer` moved APPLY→CHECK because the role is permanent and well-paid but the confidential end-client/team is the one remaining quality blocker. `#479 MoneyLion / Gen Digital Applied AI Scientist` was restored to the real CHECK queue with missing labels repaired and classified `MY-RES`.
- Mainland China cleanup: cold-outreach-only leads `#502 ThinkingAI` and `#495 DeepWisdom` were closed because no exact materially AI-related live opportunity was established. Real one-blocker CHECK items `#503 MGI`, `#496 RayNeo` and `#494 XrayBot` had missing labels repaired and remain `CN-ENG`.
- label/state repair: previously title-only active Issues including `#501 Genoria`, `#493 亨通数字智能`, `#492 容知日新` and `#491 SimpleAI` were given the correct `status:apply` + `market:cn` labels. Open title markers and labels now drive the same operational queue rather than separate counts.
- priority cleanup: all ad-hoc `[TOP]` title markers were removed. Strategic priority now comes from battlefield fit, exact evidence and weekly funnel review rather than a static Top-10 list.
- deadline note: `#492 容知日新 — 大模型应用/智能体开发工程师` currently records an application deadline of `2026-10-28`; it remains APPLY because no exact application authorization has been given.
- prior lifecycle evidence preserved: submitted WAIT history remains intact; this pass deliberately did not bulk-clean WAIT because silence is not rejection and WAIT is historical/application evidence rather than the execution queue.
- FreeHire note: the prior scheduled run observed `feed/candidates.json` returning 404. Cursor remains `513`; do not infer progress from that failure or create a replacement tracker.
- employer-facing actions: `none`. No application, recruiter message, email or other employer contact was sent during this migration/cleanup.
- next rotation: hourly scouts continue net-new read-only discovery by battlefield. New queue mutations require verified evidence and the repo contract; employer-facing actions still require exact user authorization. Weekly strategy review should reallocate effort from real funnel progression rather than raw Issue or application counts.
