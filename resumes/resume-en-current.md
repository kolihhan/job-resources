# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> Text mirror of the current fact-audited English resume, synced 2026-10-03 from `resume-en-current.pdf`.

Software engineer with production backend/full-stack experience and hands-on work building and evaluating AI systems across Text-to-SQL, hybrid retrieval, and multimodal tool use.

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Primary developer for a production feedback platform, owning submission workflows, automated notifications, and administrative features from implementation through production support.
- Maintained and extended Laravel/Vue.js production applications, shipping business features and resolving application and database issues.
- Handled deployments and server operations, including server upgrades, Laravel queues/workers, SSL maintenance, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained full-stack features for production POS applications using Laravel and Vue.js.

## Projects

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- Built a local Text-to-SQL system with grounded schema context, deterministic SQL verification, read-only execution, and bounded repair.
- Evaluated lexical vs DGSL grounding with XiYanSQL 7B on a frozen 100-case BIRD slice; both reached 58/100 execution-set matches under the project-local scorer (7 gains / 7 regressions).

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- Built a local hybrid retriever combining BM25 and Qwen dense retrieval with RRF fusion and per-result rank provenance.
- On 64 official Confluence-compatible EnterpriseRAG-Bench v1.0.0 queries over 5,189 documents, RRF improved Recall@10 from 0.7341 to 0.7630 and MRR@20 from 0.6792 to 0.7418 over BM25.

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- Built a local video-QA agent that starts with transcript evidence and escalates to frame/clip inspection only when needed, with visible evidence and abstention.
- On a frozen 12-question self-authored paired fixture, multimodal mode improved overall full-pass from 16.7% to 50.0% and reached 66.7% on visual-required questions, with no unnecessary visual calls on transcript-answerable cases.

## Skills

- **AI / LLM:** LLM Agents, RAG, Tool Calling, Retrieval & Evaluation, LangGraph
- **Programming / Backend:** Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js, React
- **Data / Infra:** AWS, MySQL, Redis, SQLite, Linux, Git, pytest
- **Other:** Java, C/C++ | Chinese (Native), English (Fluent), Malay (Intermediate)

## Education

### National Tsing Hua University | M.S., Information Systems & Applications
**Sep 2024 - Jun 2026**

GPA 4.09/4.3 | Taiwan | Thesis: *Interpreting Implicit Intent through Workplace Hierarchies and Context*

### Chung Hua University | B.S., Computer Science & Information Engineering
**Sep 2022 - Jun 2024**

GPA 3.9/4.0 | Taiwan
