# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> Text mirror of the current fact-audited English resume, synced 2026-10-03 from `resume-en-current.pdf`.

Software engineer with production Laravel/Vue.js experience and hands-on work building local AI systems in Python, including Text-to-SQL, retrieval, and tool-using agents.

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Built and maintained core workflows for a production feedback platform, including submissions, automated notifications, and admin tools.
- Shipped Laravel/Vue.js features and resolved application and database issues across production systems.
- Supported deployments and server operations, including upgrades, Laravel queues/workers, SSL renewal, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Built and maintained Laravel/Vue.js features for production POS applications.

## Projects

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- Built a local NL-to-SQL service with XiYanSQL 7B, schema grounding, SQL validation, read-only execution, and bounded repair.
- Benchmarked XiYanSQL 7B on a frozen 100-case BIRD slice, reaching 58/100 execution-set matches under the repo's frozen evaluator; used error analysis to test schema-linking variants.

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- Built a local hybrid retrieval service with BM25, Qwen3 embeddings, RRF fusion, and rank provenance exposed through FastAPI.
- On 64 EnterpriseRAG-Bench queries over 5,189 documents, RRF improved Recall@10 from 0.7341 to 0.7630 and MRR@20 from 0.6792 to 0.7418 versus BM25.

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- Built a local video-QA agent that searches transcripts first and inspects frames or clips only when visual evidence is needed.
- On a frozen 12-question paired test, multimodal mode improved overall full-pass from 16.7% to 50.0%; visual-required cases reached 66.7%.

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
