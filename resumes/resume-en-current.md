# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> Text mirror of the current English resume.

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Primary developer for a production feedback platform, implementing submission workflows, automated notifications, and administrative features.
- Maintained and extended a separate Laravel/Vue.js career platform, shipping business features and resolving production application and database issues.
- Supported production operations across deployments, server migrations/upgrades, Linux/SSL maintenance, Laravel queues/workers, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained Laravel/Vue.js features for production POS applications.

## Projects

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- Built a local Text-to-SQL pipeline around XiYanSQL 7B with schema/value grounding, SQL validation, read-only execution, and bounded repair.
- Reached a 58% execution-match rate on 100 BIRD questions; schema-linking changes fixed 7 failed cases but regressed 7 others, exposing the trade-offs for the next iteration.

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- Built a hybrid retrieval pipeline combining BM25, Qwen3 embeddings, and RRF, served through FastAPI with retrieval/ranking provenance for debugging.
- On 64 EnterpriseRAG-Bench queries over 5,189 documents, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- Built a tool-using video-QA agent that routes between transcript, frame, and clip evidence instead of invoking vision for every question.
- On 12 paired questions, multimodal routing raised overall full-pass from 16.7% to 50.0%; visual-required questions reached 66.7% with no unnecessary visual calls on transcript-answerable cases.

## Skills

- **AI / LLM:** LLM Systems, RAG, Tool Calling, Retrieval & Evaluation, LangGraph
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
