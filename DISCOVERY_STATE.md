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

## Hourly scout incremental state

This section is **efficiency state only**, not opportunity/application state. GitHub Issues remain the job state. Hourly scouts may update only the bounded object below; they must preserve the rest of this file.

Candidate-key priority: `source + exact job/requisition ID` → canonical exact-role URL → normalized `company|title|location` fallback.

Rules:

- use source-native cursor / updated-after / posted-after / event sequence when available;
- otherwise inspect only a shallow fresh head and compare candidate keys before opening full JDs;
- unchanged seen key → skip before deep research / Gmail checks;
- deep research only `NEW` or materially `CHANGED` candidates;
- **record inspected candidate keys regardless of outcome**: survivor, hard reject, duplicate, low-quality reject, or route failure all count as seen, so rejected jobs are not researched again next hour unless a material CHANGED signal appears;
- `recent_seen_keys` is fallback-only, FIFO, maximum 200 keys per market;
- all existing open/closed GitHub Issues are an additional seen-history baseline and should be checked by exact ID/URL/role identity before deep research;
- update this state only when something changed; no heartbeat-only commit.

<!-- hourly-scout-state:start -->
```json
{
  "version": 1,
  "initialized_on": "2026-10-25",
  "SG": {
    "last_success_at": "2026-10-26T00:56:30+08:00",
    "source_watermarks": {
      "freehire_event_seq": 14762
    },
    "recent_seen_keys": [
      "whatjobs-sg:data engineer:94036733",
      "whatjobs-sg:full stack developer:94031129",
      "whatjobs-sg:data engineer:94039940",
      "whatjobs-sg:data engineer:94031203",
      "whatjobs-sg:data engineer:94037158",
      "whatjobs-sg:backend developer:93853710",
      "whatjobs-sg:data engineer:94037851",
      "whatjobs-sg:data engineer:94027800",
      "linkedin:4322726898",
      "astar:3152",
      "fireworks:ai-field-engineer-singapore",
      "xora:agentic-ai-engineer-singapore"
    ]
  },
  "CN": {
    "last_success_at": "2026-10-26T03:08:51+08:00",
    "source_watermarks": {},
    "recent_seen_keys": [
      "nowcoder:444729",
      "nowcoder:415407",
      "nowcoder:463573",
      "nowcoder:464143",
      "nowcoder:460621",
      "nowcoder:466398",
      "nowcoder:462852",
      "nowcoder:466025",
      "nowcoder:459899",
      "nowcoder:409608",
      "nowcoder:465596",
      "nowcoder:458229",
      "nowcoder:460226",
      "nowcoder:437310",
      "nowcoder:466220",
      "nowcoder:462883",
      "nowcoder:418881",
      "nowcoder:411836",
      "nowcoder:460589",
      "nowcoder:408899",
      "nowcoder:464472",
      "nowcoder:419262",
      "nowcoder:421060",
      "nowcoder:417978",
      "nowcoder:421328",
      "nowcoder:417625",
      "nowcoder:415292",
      "nowcoder:413288",
      "nowcoder:464026",
      "nowcoder:405945",
      "nowcoder:424052",
      "nowcoder:417210",
      "nowcoder:445261",
      "nowcoder:459127",
      "nowcoder:461407",
      "nowcoder:470103",
      "nowcoder:466492",
      "nowcoder:465204",
      "nowcoder:467154",
      "nowcoder:467328",
      "nowcoder:464528"
    ]
  },
  "MY": {
    "last_success_at": "2026-10-26T04:17:00+08:00",
    "source_watermarks": {},
    "recent_seen_keys": [
      "joblum:2286754",
      "hiredly:tapway:junior-agentic-ai-engineer",
      "freehire:sepap:ukitcgbv",
      "randstad:91M0274336_9952230152993994517",
      "gen-digital:ai-applied-scientist:kuala-lumpur",
      "jobstreet:94937679",
      "thoughtfull-world:ai-engineer:kuala-lumpur",
      "jobstreet:95115259",
      "freehire:techstreet:sumafrol",
      "jobstreet:g-asiapacific:ai-engineer",
      "linkedin:4479792500",
      "linkedin:4477988506"
    ]
  }
}
```
<!-- hourly-scout-state:end -->

## Current receipt

- completed run: `2026-10-25 incremental hourly-scout efficiency migration`.
- incremental correction: hourly scouts must now derive candidate keys and dedupe against `DISCOVERY_STATE.md` + all GitHub Issue history **before** expensive JD/Gmail verification. Unchanged candidates are skipped; only net-new or materially changed candidates receive deep research.
- reject-cache correction: candidate keys are retained in the bounded cache even when the candidate is rejected, duplicated or fails a quality gate. This prevents hourly re-research of the same bad job.
- bounded persistence: scouts may update only the `Hourly scout incremental state` object in this file. They remain read-only for GitHub Issues, Gmail and employer-facing actions. The fallback cache is capped at 200 keys per market and must not become a second job tracker.
- canonical strategy: `README.md`, `PROFILE.md` and `RULES.md` define the North Star and six battlefields: `SG-ENG`, `SG-RES`, `CN-ENG`, `CN-RES`, `MY-ENG`, `MY-RES`. Singapore is quality-first, Mainland China supports higher-throughput native/direct discovery after hard filtering, and Malaysia is TOP / destination-quality only. Engineering and realistic research/research-engineering are both valid target outcomes.
- automation architecture: `SG AI Scout`, `CN AI Scout` and `MY TOP AI Scout` run hourly reconnaissance; `Recruiting Signal Watch` checks both Gmail accounts hourly for meaningful progression; `AI Job Strategy Review` compares all six battlefields weekly and recommends adaptive allocation. Scheduler prompts read the repo contract rather than maintaining a private copy of policy.
- verified active queue snapshot from the prior reconciliation: `ACTION 0 / APPLY 31 / CHECK 7`.
- APPLY battlefield snapshot from the prior reconciliation: `SG-ENG 5 / SG-RES 1 / CN-ENG 17 / CN-RES 2 / MY-ENG 6 / MY-RES 0`.
- CHECK battlefield snapshot from the prior reconciliation: `CN-ENG 3 / MY-ENG 3 / MY-RES 1`; no current SG CHECK was found in that pass.
- Malaysia cleanup: `#664 TAPiO` and `#662 Mentix` were closed because current evidence showed good AI fit but did not clear the new MY destination-quality bar. `#647 Michael Page AI Software Engineer` moved APPLY→CHECK because the role is permanent and well-paid but the confidential end-client/team is the one remaining quality blocker. `#479 MoneyLion / Gen Digital Applied AI Scientist` was restored to the real CHECK queue with missing labels repaired and classified `MY-RES`.
- Mainland China cleanup: cold-outreach-only leads `#502 ThinkingAI` and `#495 DeepWisdom` were closed because no exact materially AI-related live opportunity was established. Real one-blocker CHECK items `#503 MGI`, `#496 RayNeo` and `#494 XrayBot` had missing labels repaired and remain `CN-ENG`.
- label/state repair: previously title-only active Issues including `#501 Genoria`, `#493 亨通数字智能`, `#492 容知日新` and `#491 SimpleAI` were given the correct `status:apply` + `market:cn` labels. Open title markers and labels now drive the same operational queue rather than separate counts.
- priority cleanup: all ad-hoc `[TOP]` title markers were removed. Strategic priority now comes from battlefield fit, exact evidence and weekly funnel review rather than a static Top-10 list.
- deadline note: `#492 容知日新 — 大模型应用/智能体开发工程师` currently records an application deadline of `2026-10-28`; it remains APPLY because no exact application authorization has been given.
- prior lifecycle evidence preserved: submitted WAIT history remains intact; silence is not rejection and WAIT is historical/application evidence rather than the execution queue.
- employer-facing actions: `none` during this incremental-scout migration.
- next rotation: hourly scouts consume only net-new/changed source deltas where possible and use the bounded recent-seen fallback otherwise. New queue mutations still require separate verified execution under the repo contract; employer-facing actions require exact user authorization.