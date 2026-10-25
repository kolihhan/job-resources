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

- completed run: `2026-10-25 16:50 MYT manual queue reconciliation + execution-priority review`.
- maintenance: `ACTION verified at 0. The earlier stale ACTION batch had already been handled by the user and remains WAIT. Maxify remains WAIT after the 2026-10-21 prototype submission; the 2026-10-23 lihhanko526 screening email was a duplicate earlier-stage message, not a new pipeline.`
- CHECK resolution: `#664 TAPiO promoted CHECK→APPLY because the employer's own Employment/Current opportunities structure, with internships separately listed and no non-permanent signal, satisfies RULES.md PROBABLE regular-employment standard. #665 Kuailu promoted CHECK→APPLY after fresh LinkedIn/JobStreet non-MCF surfaces were verified. #666 Bjak remains CHECK because the exact AI Finance Agent role was already public in Aug 2026 and a Bjak receipt exists on 2026-08-19 with no title, creating real duplicate risk. #641 Sunway Digital remains CHECK because current JobStreet says Full time while another current source says Contract; no employer-controlled exact role was found to settle the conflict.`
- current queue snapshot: `ACTION 0 / APPLY 30 / CHECK 2. Ten APPLY Issues are explicitly marked [TOP] in the title so the user does not need to treat all APPLY items as equal.`
- current TOP execution set: `#640 Oppstar AI Agent Engineer (MY); #633 AI Singapore/NTU AI Engineer (Evaluation) (SG); #648 ByteDance 后端开发工程师-大模型应用 (CN); #636 Coremail 2026 AI测试工程师 (CN); #643 NTT DATA AI Solutions Engineer (MY); #651 Prudential AI Engineer (SG); #665 Kuailu LLM Evaluation Engineer (SG); #649 Huawei 软件开发 LLM/Agent平台 (CN); #646 Michael Page GenAI Software Engineer (MY); #638 Tencent CSIG WorkBuddy Agent Harness (CN).`
- prior scheduled maintenance preserved: `#668 Nas Company — AI Product Engineer - Nas.com and #669 BOKE Technology / 波克科技 — AI应用工程师 were created as WAIT from exact LinkedIn application confirmations dated 2026-10-25. ThoughtFull remains WAIT. No generic NCS role was added; Xiaomi receipt remained unresolved rather than guessed.`
- FreeHire note: `feed/candidates.json returned 404 in the prior scheduled run. Cursor remains 513; do not infer progress or create a replacement tracker.`
- employer-facing actions in this reconciliation: `none. No application, recruiter message, or employer contact was sent. This run only corrected/re-ranked GitHub state.`
- next rotation: `Use the ten [TOP] APPLY Issues as the execution shortlist. Do not create another dashboard or scoring system. Resolve Bjak/Sunway only when stronger evidence appears; ordinary discovery should add only genuinely better AI opportunities or replace weaker shortlist items.`
