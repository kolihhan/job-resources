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

- completed run: `2026-10-25 interactive AI-career scope correction`.
- user correction: `Target is an AI-related career, not broad generic tech employment. Researcher/research-engineering roles are explicitly acceptable.`
- canonical policy: `README.md`, `PROFILE.md`, and `RULES.md` now require material AI/ML/research relevance. Active families include Applied AI, GenAI, LLM/RAG/Agent, AI software/backend, ML/NLP/search/retrieval/evaluation, AI-heavy data science, Research Engineer, AI Researcher, Applied Scientist and Research Scientist when hard requirements are realistic. Generic SWE/backend/full-stack/test roles survive only when the actual JD/team/product is materially AI-related.`
- research rule: `MSc-compatible research and research-engineering roles are active. Hard PhD/publication/independent-research requirements remain literal blockers. Do not invent publications or professional research YOE.`
- queue reconciliation: `Closed #652 foodpanda Junior Fullstack, #653 Alta Software Engineer, #654 Combuilder Software Engineer, #655 ByteDance generic backend/server, #656 新毅东 generic software application engineer, #658 亚信安全 general test development, and #659 上证信息 general test development because their verified core work was not materially AI-related. #657 Huawei Cloud AI Software and #660 积加科技 AI Test Agent-related role remain in-scope.`
- research/ML recovery: `Reopened #291 Apple Machine Learning Engineer, Strategic Data Solutions after current Apple evidence showed the live role's 3-year practical-experience minimum may be acquired through work, independent projects or academic research. Reopened #521 交叉科技 大模型Agent研究工程师 after current Nowcoder evidence showed the role live at 1–3 YOE with Agent/RAG research + engineering, fine-tuning and Agentic-RL work and no PhD-only gate.`
- historical research review: `Do not reopen Microsoft Researcher #31/#51 because the user explicitly declined those reference-request paths. Keep Clera research roles closed where specific applied-research/synthetic-data experience floors remain unmet. Keep NTU/HK research roles closed when employment type is non-permanent. Keep Shanghai AI Lab research/engineering roles blocked where employer foreign-national hiring is explicitly unavailable.`
- FreeHire interpretation: `The public firehose may remain broader than the final AI target because AI companies often use generic SWE/backend titles. Raw feed inclusion does not create queue eligibility; actual JD/team/product AI relevance must be verified before Issue creation or retention.`
- employer-facing actions: `none.`
- next rotation: `SG/CN/MY AI-only search: Applied AI + LLM/Agent/RAG + AI software/backend + ML/NLP/search/retrieval/evaluation + research/research-engineering. Strong company is a priority signal; meaningful AI/ML/research work is the direction gate.`
