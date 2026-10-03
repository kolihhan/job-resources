# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> Text mirror of the current approved English resume, synced 2026-10-03 from `resume-en-current.pdf`.

NTHU M.S. Computer Science graduate with production software engineering experience and evaluated Applied AI work across LLM agents, retrieval, multimodal tool use, and Text-to-SQL reliability.

## Experience

### Kahap Inc | Software Developer (Part-time)
**Aug 2022 - Aug 2026**

- Primary developer for a production feedback platform covering submission workflows, automated notifications, and administrative features.
- Maintained and extended Laravel/Vue.js production applications, shipping business features and resolving application and database issues.
- Managed deployments and server operations, including upgrades, Laravel queues/workers, SSL maintenance, and database troubleshooting.

### Pac Com Solution | Full-Stack Developer Intern
**Jun 2021 - Jan 2022**

- Developed and maintained full-stack features for production POS applications using Laravel and Vue.js.

## Projects

### Semantic Text-to-SQL Agent
**Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite**

- Built a local Text-to-SQL service with deterministic SQL verification, read-only execution, bounded repair, and one-pass clause-guided semantic revision for common semantic errors.
- On a frozen 100-query BIRD DEV slice, guarded repair raised execution success from 63% to 82%; official EX improved from 31% to 34% (pre-CGSR baseline).

### Local RAG Search
**Python · BM25 · Qwen Embeddings · RRF · FastAPI**

- Benchmarked BM25, Qwen dense retrieval, and RRF on 64 queries over 5,189 documents; hybrid reached 0.7630 Recall@10 and 0.7418 MRR@20 with per-query rank provenance.

### Hermes Video Tutor
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- Built an adaptive video QA agent that escalates from transcript search to frame/clip inspection; on a 12-case paired fixture, visual-required full pass reached 66.7% with visual-tool use on 100% of visual questions.

### Small-Agent QLoRA
**Python · Qwen3.5 4B · QLoRA · GAIA · Tool Use**

- Built a local tool agent with search/read/inspect/python, bounded steps, duplicate-call blocking, visible trajectories, verified trajectory collection, leakage guards, and a paired Base-vs-LoRA evaluator.
- Implemented the QLoRA training path and frozen GAIA evaluation partitions; no uplift claim is made until a valid paired run completes.

## Skills

- **AI / LLM:** LLM Agents, RAG, Tool Calling, Retrieval & LLM Evaluation, Embeddings, LangGraph, QLoRA / PEFT
- **Programming / Backend:** Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js, React
- **Cloud / Data:** AWS Lambda, API Gateway, S3, RDS, MySQL, Redis, SQLite, Linux
- **Other:** Java, C/C++, Git, pytest | Chinese (Native), English (Fluent), Malay (Intermediate)

## Education

### National Tsing Hua University | M.S., Computer Science
**2024 - 2026**

GPA 4.09/4.3 | Taiwan | Thesis: *Interpreting Implicit Intent through Workplace Hierarchies and Context*

### Chung Hua University | B.S., Computer Science
**2022 - 2024**

GPA 3.9/4.0 | Taiwan
