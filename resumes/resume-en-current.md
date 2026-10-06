# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Built and maintained a production feedback platform from initial implementation through deployment, centralizing submissions, automated notifications, and admin workflows.
- Integrated a GPT-SoVITS speech-generation API into an existing application and added checks for dropped text and pronunciation output.
- Maintained and shipped features for a separate Laravel/Vue.js career platform, debugging production application and database issues.
- Handled production operations for the career platform, including server migrations/upgrades, Laravel queues/workers/schedulers, SSL renewal, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained Laravel/Vue.js features for a production POS application.

## Projects

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · Qwen3.5 9B · LangGraph · FastAPI · SQLite**

- Built a local Text-to-SQL pipeline with schema/value grounding, deterministic SQL verification, read-only execution, and bounded repair.
- On a frozen 100-query BIRD DEV slice, guarded verification + repair improved official EX from 33% to 39% and conservative execution success from 75% to 90%, with no correct-to-wrong EX regressions.

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- Built a FastAPI hybrid retriever combining BM25, Qwen3 embeddings, and RRF, exposing lexical, dense, and fused ranks per result.
- On a frozen 64-query EnterpriseRAG-Bench slice over 5,189 documents, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.

### M.S. Thesis - Workplace Implicit Intent
**Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation**

- Built a role- and context-grounded retrieval framework for listener-side workplace intent from 51,414 posts and 20,455 extracted utterances.
- On 401 held-out utterances, Dual-KG Top1 scored 0.6890 automated semantic F1 versus 0.6250 without retrieved evidence.

## Skills

- **AI:** RAG, Information Retrieval, LLM Evaluation, LangGraph
- **Programming / Backend:** Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js
- **Data / Infra:** MySQL, SQLite, Linux, Git, GitHub Actions, pytest
- **Languages:** Chinese (Native), English (Fluent), Malay (Intermediate)

## Education

### National Tsing Hua University | M.S., Information Systems & Applications
**Sep 2024 - Jun 2026**

GPA 4.09/4.3 | Taiwan

### Chung Hua University | B.S., Computer Science & Information Engineering
**Sep 2022 - Jun 2024**

GPA 3.9/4.0 | Taiwan
