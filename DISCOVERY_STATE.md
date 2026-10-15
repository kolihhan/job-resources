# Discovery State

## FreeHire intake cursor

- cursor: `234`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-15 21:24 MYT` — healthy, `first_seq=1`, `last_seq=3121`; page index matches `first_seq=1 / last_seq=3121`; no cursor gap. Backlog is 2887 events.
- worker correction: `2026-10-09` — stale-NEW regression reproduced by a failing test and fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`; focused CI passed. Daily full backstop now seeds stale unseen jobs without emitting them as NEW. Existing pre-fix backlog remains historical feed state and must not block current-job inspection.
- intake mode: `FreeHire Intake` is enabled hourly. Current `RULES.md` requires a bounded fresh-head pass before sequential cursor catch-up when backlog exists; fresh inspection beyond the cursor does not move the cursor over unprocessed history.
- last intake: `Worker/index remain healthy and consistent at seq 3121 with no newer feed delta since the prior intake. Retried the previously blocked finalist Manulife — Associate Full-stack Software Engineer (MY, JR26100119): exact-ID Gmail dedupe completed cleanly in both accounts, GitHub dedupe remained clean, and the current employer Workday page still exposes an active Apply route with end date 2026-12-31 and explicit fresh-graduate eligibility. Promoted as APPLY Issue #310 and read back successfully. Historical seq 235 still could not be safely exposed from the sequence page through the connector, so the contiguous cursor remains 234.`

## Current receipt

- completed run time: `2026-10-15 ~20:45 MYT`
- run type: `scheduled maintenance + bounded SG-gap/CN-native discovery — platform/infra/systems + ML systems/AI infra/inference/evaluation rotation`
- maintenance: `Fully inspected current ACTION/APPLY/CHECK. #184 Ant International remains ACTION for coding assessment + confirmed 2026-10-23 interview; #220 remains ACTION for a real interview invitation; #304 remains ACTION for the time-bounded OA due 2026-10-20. Existing APPLY/CHECK states remain consistent with current RULES. Both Gmail lifecycle overlap searches completed. LinkedIn confirmations for RMA Consultants and Filigrain map to existing WAIT #280/#281, so no state change was needed. No newer lifecycle evidence displaced current Issue state.`
- SG gap lanes tried: `direct employer/ATS + targeted product/startup/AI-infra gaps. TikTok A225056 is a live official graduate AI Infrastructure requisition and technically strong, but existing WAIT #13/#14 already consume TikTok's stated two-position graduate application limit, so it was suppressed before promotion. Pokee AI's official AI Infrastructure role is current on the employer site but has a hard 3+ years ML-infrastructure requirement and substantial systems/GPU/Kubernetes requirements, so it did not justify a selective stretch. No routine FreeHire rescan performed.`
- CN native/direct lanes tried: `牛客 + 智联 + 51job indexed gaps + BOSS/猎聘 targeted search for platform/infra/inference roles. PDD 2027 AI Infra and backend roles are explicitly 2027-only; 九方云 current platform/AI roles are also 2027-only. Huawei AI Infra remains represented by existing CHECK #308 rather than opening a duplicate. 智联/51job surfaced several 1-3 YOE Python/AI/platform leads, but the stronger exact roles were either outside the current platform/infra lane, stale index surfaces, staffing/client arrangements, or lacked enough current exact-role evidence to justify Stage 2.`
- SG coverage: `4 candidates / 4 employers / 3 source families / 1 deep-verified`
- CN coverage: `9 candidates / 8 employers / 5 source families / 0 deep-verified`
- serious survivors: `none`
- Gmail finalist dedupe: `Both recent lifecycle overlap searches completed. TikTok A225056 passed technical/liveness inspection but was suppressed by existing GitHub application-limit history before finalist Gmail dedupe; no new finalist required exact-ID Gmail dedupe.`
- access/search failures: `No required Gmail/GitHub access or write failure. BOSS/猎聘 public indexing was weak in this rotation, so 牛客/智联/51job/direct evidence was used to avoid treating source weakness as market exhaustion.`
- external side effects: `No application, recruiter message, employer contact or assessment submission sent.`
- next rotation: `data platform + search/retrieval. SG: direct employer/ATS and smaller product/data/search gaps outside saturated TikTok/ByteDance families. CN: rotate official/direct + 牛客/智联/51job/BOSS/猎聘 toward 2026/recent-graduate or 0-3 YOE data-platform/search/retrieval roles, avoiding 2027-only campus pages.`