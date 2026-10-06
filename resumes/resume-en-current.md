# Ko Lih Han

**Software Engineer | Applied AI & Backend**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Led end-to-end development of a production feedback platform, from system design and implementation through deployment, including submission workflows, automated notifications, and admin operations.
- Shipped new features and resolved application and database issues on an existing Laravel/Vue.js production platform.
- Handled server migrations, upgrades, Laravel queues/workers/schedulers, SSL renewal, and production database troubleshooting for the same platform.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained Laravel/Vue.js features for a production POS system.

## Projects

### [Text-to-SQL with Verification & Repair](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · FastAPI · LangGraph · SQLite · Qwen3.5 9B**

- Built a local Text-to-SQL pipeline with schema/value grounding, deterministic SQL verification, read-only execution, and bounded repair.
- On 100 BIRD DEV queries, verification + bounded repair raised execution accuracy from 33% to 39% and executable queries from 75 to 90, correcting 6 cases with no accuracy regressions.

### [Hybrid Retrieval for RAG](https://github.com/kolihhan/local-rag-search)
**Python · FastAPI · BM25 · Qwen3-Embedding-0.6B · RRF**

- Built a FastAPI hybrid retriever combining BM25, Qwen embeddings, and RRF, exposing lexical, dense, and fused ranks for each result.
- On 64 EnterpriseRAG-Bench queries over 5,189 documents, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.

### [Multimodal Video QA Agent](https://github.com/kolihhan/hermes-video-tutor)
**Python · Streamlit · Qwen3.5 4B · FFmpeg**

- Built a local video QA agent that chooses between transcript search and frame/clip inspection, shows the evidence used, and declines to answer when evidence is insufficient.
- In a 12-question evaluation, multimodal mode answered 4/6 visual-required cases correctly while avoiding unnecessary visual-tool calls on transcript-answerable cases.

### M.S. Thesis: Interpreting Implicit Intent through Workplace Hierarchies and Context

- Built a graph-aware retrieval framework over 10,645 workplace dialogue turns, using MiniLM and graph attention to learn speaker/listener state representations and retrieve evidence by workplace role and interaction context.
- On 400 held-out targets, role-based retrieval raised semantic F1 from 0.6440 to 0.6793; combining role and context evidence reached 0.6819.

## Skills

- **AI / Retrieval:** RAG, Information Retrieval, LLM Evaluation, Agents, Tool Calling, LangGraph
- **Programming / Backend:** Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js
- **Databases / Dev Tools:** MySQL, SQLite, Linux, Git, GitHub Actions, pytest
- **Languages:** Chinese (Native), English (Fluent), Malay (Intermediate)

## Education

### National Tsing Hua University | M.S., Information Systems & Applications
**Sep 2024 - Jun 2026**

GPA 4.09/4.3 | Taiwan

### Chung Hua University | B.S., Computer Science & Information Engineering
**Sep 2022 - Jun 2024**

GPA 3.9/4.0 | Taiwan
