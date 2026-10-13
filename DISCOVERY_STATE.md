# Discovery State

## FreeHire intake cursor

- cursor: `218`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-12 23:19 MYT` — healthy, `first_seq=1`, `last_seq=2194`; page index matches `first_seq=1 / last_seq=2194`; no cursor gap. Backlog is 1976 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index healthy at seq 2040. Feed advanced by 7 events since the prior receipt. Recent unseen page 2001–2040 was requested first; visible events remain old CHANGED SG listings with explicit no-sponsorship/right-to-work blockers, while the GitHub connector truncated the JSONL before the full bounded fresh-head set could be safely evaluated. Sequential page 201–250 was then requested for cursor catch-up, but connector truncation again prevented safe resolution of seq 219. Cursor remains 218; no cursor jump across unresolved history and no Issue promotion from incomplete evidence.`

## Current receipt

- completed run time: `2026-10-13 ~17:43 MYT`
- run type: `bounded SG gap + CN native/direct discovery; ML-systems/AI-infra/inference/evaluation rotation; <=30d freshness, exact-route, dedupe and sponsor/work-permit precision preserved`
- material change: `none — no genuinely useful survivor met the full promotion gates; no opportunity Issue created or updated.`
- SG lanes: `Direct employer/ATS plus targeted gap search for ML systems, AI infrastructure and platform roles. Genesis Networks AI Infrastructure Engineer was current but MCF-only, so blocked. Motional ML Infrastructure was Senior. SAP Associate AI Developer was an excellent 0–3 YOE fit but its exact employer page is dated 2026-08-27, outside the <=30d hard freshness gate; current search/listing presence does not override that exact-role date. SAP Forward Deployed AI Developer requires 4–8 YOE and SAP AI Full Stack Developer requires 6+ YOE.`
- CN lanes: `Native/direct AI-infra, inference, search/retrieval and systems search across 牛客 plus direct multinational/employer surfaces. Huawei 27-only AI Infra roles were cohort-incompatible; Huawei 26 AI Infra was explicitly ended. Intel surfaced a fresh 2026-10-12 campus AI Software Developer listing and external campaign evidence says the current campus campaign accepts 2026/2027 graduates, but GitHub already contains a rejected same-title Intel AI Software Development Engineer plus two active Intel AI/LLM applications, so this near-identical employer/role-family opportunity was suppressed rather than creating another Intel CHECK. Apple Search & Knowledge Platform was fresh but has a hard 5+ YOE requirement. Tencent TIONE AI Infra requires 3+ years plus deep Go/Kubernetes/GPU-platform experience and was not strong enough as an early-career stretch.`
- SG coverage: `7 candidates / 4 employers / 3 source families / 1 deep-verified`
- CN coverage: `8 candidates / 5 employers / 4 source families / 2 deep-verified`
- survivor: `none`
- external side effects: `No application, recruiter message, employer contact or sponsorship inquiry sent. GitHub write: this receipt only.`
- next rotation: `Move away from ML-systems/AI-infra-first toward search/retrieval or data-platform/SWE; prioritize SG exact-role pages posted/updated within 30 days with a non-MCF route and realistic pass evidence, and CN direct employers/native roles with explicit foreign-candidate/work-permit infrastructure. Avoid another Intel role-family promotion unless materially different from existing Intel history.`
