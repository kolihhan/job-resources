# Discovery State

## FreeHire intake cursor

- cursor: `513`
- public feed: `kolihhan/freehirefetch/feed/index.json` + sequence-addressable `feed/pages/*.jsonl`; legacy `feed/events.jsonl` remains worker state but is not used for routine private intake
- public health verified: `2026-10-25` — latest recorded worker state is healthy at `first_seq=1`, `last_seq=14372`; latest recorded delta completed at `2026-10-25T01:08:20.431674Z` with `new=10`, `changed=0` (`SG fetched=531`, `CN=66`, `MY=203`).
- worker correction: `2026-10-25` — `kolihhan/freehirefetch` PR #4 merged as `eb56a4f323652659ae374b16de2257c2b8a5423a`. `Senior` titles are downstream review hints rather than source-level hard drops; Staff/Principal/Lead/Manager/Director/Intern remain title hard drops. Singapore raw discovery is split into four engineering category windows and exact-deduped. This is a raw radar implementation only; category inclusion does not imply job-resources eligibility.
- earlier worker correction: `2026-10-09` — stale-NEW regression fixed in `kolihhan/freehirefetch` commit `05a0553e2899e3b8c88d7aa77598746eb6452f45`.
- intake mode: `FreeHire Intake` is enabled hourly. Fresh-head inspection beyond the cursor must not move the cursor over unprocessed history.
- last intake limitation: `Historical cursor catch-up remains blocked by connector truncation of one-line JSONL pages. Cursor is deliberately preserved at 513 rather than guessing.`

## Current receipt

- completed run: `2026-10-25 14:38 MYT interactive AI-only repo-skills pass`.
- workflow: `Used current kolihhan/kolihhan router: Claude-like Workflow + Research Mode Heavy. Audited premise, read actual JDs, checked counter-evidence/hard gates, then GitHub/Gmail dedupe before Issue writes.`
- target contract: `Permanent full-time AI-related careers only across SG + CN + MY. Research Engineer / AI Researcher / Applied Scientist / Research Scientist are explicitly in scope when hard requirements are realistic. Generic SWE/backend/full-stack/test survives only when the actual work is materially AI/ML/research-related.`
- queue correction: `Closed #660 积加科技 测试开发工程师 after re-reading the live JD. Its core work is general AIoT test development; AI Test Agent is only one exploratory responsibility and therefore does not clear the AI-direction gate.`
- new APPLY: `#662 Mentix Full Stack AI Developer (MY) — full-time AI-first product role with LLMs, agents, vector DBs, AI orchestration and knowledge graphs; #663 AEON Bank Machine Learning Engineer (MY) — full-time ML/AI systems role covering production ML, Agentic RAG, MLOps and AI infrastructure; experience wording allows relevant engineering experience, so it is a truthful selective stretch rather than a hard YOE rejection.`
- new CHECK: `#664 TAPiO AI Developer (MY) — excellent retrieval/evaluation/application fit; only unresolved material gate is employment type because the official role page does not state full-time/permanent/contract. #665 Kuailu Software LLM Evaluation Engineer (SG) — unusually strong evaluation fit; MCF is unusable for this candidate, so the one remaining gate is a verified exact non-MCF application flow from the current LinkedIn/JobStreet surfaces. #666 Bjak Applied AI Engineer - AI Finance Agent (MY) — strong live Ashby role, but an official Bjak application receipt from 2026-08-19 does not expose the prior role title; resolve same-company exact/near-duplicate history before promotion.`
- rejected research/AI leads: `A*STAR current IAIC Research Engineer roles surfaced in this pass were not promoted because current evidence showed contract employment and/or mature experience requirements. Bitdeer Agent Evaluation / inference/model-efficiency research roles were not promoted where mandatory implementation depth (model routing/uncertainty/cascading, low-level inference/C++, or model-efficiency methods) materially exceeded the candidate's evidence. Research being in scope does not override literal hard requirements.`
- dedupe notes: `Lenovo fresh/junior AI roles were suppressed because #456 and #332 already record two recent Lenovo AI applications. Bjak was not treated as clean because Gmail contains a real employer receipt. AEON Bank/TAPiO/Mentix/Kuailu targeted GitHub + Gmail checks found no application receipt/process duplicate; an AEON Bank mention in Gmail was only an AWS marketing event email.`
- employer-facing actions: `none. No application, recruiter message, or external employer contact was sent.`
- next rotation: `Continue net-new SG/CN/MY AI-only discovery, emphasizing early-career/research-compatible AI roles and direct/non-MCF routes. Resolve CHECK #664 employment type, #665 non-MCF route, and #666 Bjak prior-role identity before creating replacements or duplicates.`
