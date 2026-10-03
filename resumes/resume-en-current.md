# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> Text mirror of the current approved English resume, synced 2026-10-03 from `resume-en-current.pdf`.

Software engineer with production backend/full-stack experience and hands-on work building and evaluating LLM systems across Text-to-SQL, hybrid retrieval, and tool-using multimodal agents.

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Primary developer for a production feedback platform, owning submission workflows, automated notifications, and administrative features from implementation through production support.
- Maintained and extended Laravel/Vue.js production applications, shipping business features and debugging application and database issues.
- Handled deployments and server operations, including upgrades, Laravel queues/workers, SSL maintenance, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained full-stack features for production POS applications using Laravel and Vue.js.

## Projects

### [Semantic Text-to-SQL Agent](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite**

- Built a local Text-to-SQL service with deterministic SQL verification, read-only execution, bounded repair, and one-pass clause-guided semantic review.
- On a frozen 100-query BIRD DEV run, guarded repair recovered 19 failed executions (63% → 82% execution success); official BIRD EX rose from 31% to 34%.

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen Embeddings · RRF · FastAPI**

- Built a local hybrid retriever with BM25, Qwen dense retrieval, RRF fusion, and per-result rank provenance.
- On 64 Confluence-compatible queries over 5,189 documents, hybrid RRF reached 0.7630 Recall@10, 0.7418 MRR@20, and 0.8438 Hit@10.

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- Built a local video-QA agent that uses transcript evidence first and inspects frames/clips only when needed, with visible tool traces and abstention.
- On a frozen 12-question self-authored paired fixture, multimodal tools raised visual-required full pass from 0% to 66.7%, with no unnecessary visual calls on transcript-answerable cases.

## Skills

- **AI / LLM:** LLM Agents, RAG, Tool Calling, Retrieval & LLM Evaluation, Embeddings, LangGraph
- **Programming / Backend:** Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js, React
- **Cloud / Data:** AWS, MySQL, Redis, SQLite, Linux
- **Other:** Java, C/C++, Git, pytest | Chinese (Native), English (Fluent), Malay (Intermediate)

## Education

### National Tsing Hua University | M.S., Information Systems & Applications
**2024 - 2026**

GPA 4.09/4.3 | Taiwan | Thesis: *Interpreting Implicit Intent through Workplace Hierarchies and Context*

### Chung Hua University | B.S., Computer Science & Information Engineering
**2022 - 2024**

GPA 3.9/4.0 | Taiwan
