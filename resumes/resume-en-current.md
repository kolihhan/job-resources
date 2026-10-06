# Ko Lih Han

**Software Engineer | Applied AI & Backend**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Built and maintained a production feedback platform from initial implementation through deployment, centralizing submissions, automated notifications, and admin workflows.
- Maintained and shipped features for a Laravel/Vue.js career platform, debugging production application and database issues.
- Handled production operations for the career platform, including server migrations/upgrades, Laravel queues/workers/schedulers, SSL renewal, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained Laravel/Vue.js features for a production POS system.

## Projects

### [Text-to-SQL with Verification & Repair](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · FastAPI · LangGraph · SQLite · Ollama**

- Built a local Text-to-SQL pipeline with schema/value grounding, deterministic SQL verification, read-only execution, and bounded repair.
- Using Qwen3.5 9B on a frozen 100-query BIRD DEV slice, guarded verification + repair raised official EX from 33% to 39% and conservative execution success from 75% to 90%, recovering 6 incorrect cases with no EX regressions.

### [Hybrid Retrieval for RAG](https://github.com/kolihhan/local-rag-search)
**Python · FastAPI · BM25 · Qwen Embeddings · RRF**

- Built a FastAPI hybrid retriever combining BM25, Qwen embeddings, and RRF, exposing lexical, dense, and fused ranks for each result.
- On a frozen 64-query slice over 5,189 documents, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.

### [Multimodal Video QA Agent](https://github.com/kolihhan/hermes-video-tutor)
**Python · Streamlit · Ollama · ffmpeg**

- Built a local video QA agent that routes between transcript search and frame/clip inspection, exposing tool activity and evidence while allowing abstention when evidence is insufficient.
- On a small frozen 12-question test, visual-required full-pass rate rose from 0% with transcript-only to 66.7% with multimodal tools, with no unnecessary visual calls on transcript-answerable cases.

### M.S. Thesis: Context-Aware Workplace Intent
**Llama 3.1 8B · Retrieval · Knowledge Graphs · NLP**

- Built role- and context-grounded retrieval over 51,414 posts and 20,455 utterances, separating workplace-role evidence from local context evidence.
- On 401 held-out utterances, Dual-KG Top1 reached 0.6890 semantic F1 versus 0.6250 without retrieved evidence.

## Skills

- **AI / Retrieval:** RAG, Information Retrieval, LLM Evaluation, Agents, Tool Calling, LangGraph
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
