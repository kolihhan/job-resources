# Ko Lih Han

**Software Engineer | Applied AI & Backend**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Built and maintained a production feedback platform from initial implementation through deployment, centralizing submissions, automated notifications, and admin workflows.
- Integrated a GPT-SoVITS speech-generation API into an existing application and added checks for dropped text and pronunciation output.
- Maintained a Laravel/Vue.js career platform and handled production operations including server migrations/upgrades, queues/workers/schedulers, SSL renewal, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained Laravel/Vue.js features for a production POS system.

## Projects

### [Text-to-SQL with Verification & Repair](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · Qwen3.5 9B · LangGraph · FastAPI · SQLite**

- Built a local Text-to-SQL pipeline with schema/value grounding, deterministic SQL verification, read-only execution, and bounded repair.
- On a frozen 100-query BIRD DEV slice, guarded verification + repair improved official EX from 33% to 39% and conservative execution success from 75% to 90%, with 6 wrong-to-correct and 0 correct-to-wrong EX transitions.

### [Hybrid Retrieval for RAG](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- Built a hybrid retriever with per-result lexical, dense, and fused rank provenance; on a frozen 64-query / 5,189-document slice, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.

### [Multimodal Video QA Agent](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes Agent · Multimodal Tools · Streamlit**

- Built a local video QA agent that routes between transcript search and frame/clip inspection, exposing tool activity and evidence while allowing abstention when evidence is insufficient.
- On a small frozen 12-question fixture, multimodal mode reached 66.7% full pass on visual-required questions versus 0% transcript-only, with no unnecessary visual-tool calls on transcript-answerable cases.

### M.S. Thesis: Context-Aware Workplace Intent
**Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation**

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
