# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

Malaysia | +60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan | LinkedIn

Software engineer with **4 years of part-time production experience** owning backend systems from build to deployment. Combines production engineering with hands-on LLM post-training, agent runtimes, retrieval, and evaluation.

## Experience

### Software Developer (Part-time)
**Kahap Inc**  
Aug 2022 - Aug 2026

- Owned the **0-to-1 build and production rollout** of a feedback platform, centralizing submissions, discussion, notifications, and admin workflows into one operational system.
- Kept a Laravel/Vue.js career platform running across queue workers, scheduled jobs, SSL renewals, database/server migrations, and Linux hosting.
- Integrated GPT-SoVITS and automated pronunciation/text checks into production features, connecting external AI services to existing backend workflows.

### Full-Stack Developer Intern
**Pac Com Solution**  
Jun 2021 - Jan 2022

- Shipped and debugged Laravel/Vue.js features in a production POS codebase across backend and frontend paths.

## Projects

### Small-Agent QLoRA
**github.com/kolihhan/small-agent-qlora**  
Python, Qwen3.5-9B, QLoRA / PEFT, Transformers, llama.cpp

- Post-trained a Qwen3.5-9B tool agent with QLoRA, lifting exact task success from **34.5% to 62.0%** on a frozen 200-task closed-loop evaluation.
- Built the agent runtime around bounded tool execution, duplicate-call blocking, timeouts, and persisted traces so failures could be reproduced and analyzed.
- Validated beyond the controlled benchmark on GAIA100, **doubling accuracy from 9% to 18%** and tracing the main remaining failure to over-search rather than tool errors.

### Semantic Text-to-SQL
**github.com/kolihhan/semantic-text2sql-agent**  
Python, FastAPI, LangGraph, SQLite, Qwen3.5-9B

- Designed and built a local NL-to-SQL service with schema grounding, deterministic validation, bounded repair, and read-only execution to reject invalid or destructive queries before they reach the database.
- Improved execution success from **75% to 90%** and execution-match accuracy from **33% to 39%** on 100 frozen BIRD DEV queries, recovering 6 wrong answers with 0 regressions.
- Unified FastAPI, CLI, and Streamlit behind one service layer so generation, verification, execution, and evaluation reused the same backend logic.

## Research

### Context-Aware Workplace Language Understanding
**M.S. Thesis, National Tsing Hua University**  
NLP, retrieval, role/context graphs

- Curated and labeled **20,455 workplace utterances across 7 boards**, capturing speaker/listener state, emotion, and communicative purpose for implicit-meaning analysis.
- Designed role- and context-aware graph retrieval/fusion, improving target-only macro-F1 from **0.625 to 0.689** on 401 test utterances.

## Skills

- **AI / LLM:** Hugging Face Transformers, PEFT / QLoRA, LangGraph, llama.cpp, RAG, tool calling, LLM evaluation
- **Backend:** Python, FastAPI, PHP, Laravel, SQL, REST APIs
- **Data / Infrastructure:** MySQL, SQLite, Linux, Git, GitHub Actions, pytest
- **Frontend:** JavaScript, Vue.js, React
- **Languages:** Chinese (Native/Bilingual), English (Fluent), Malay (Intermediate)

## Education

### National Tsing Hua University
Master of Science, Information Systems & Applications | GPA: 4.09/4.3 | Jun 2026

### Chung Hua University
Bachelor of Science, Computer Science & Information Engineering | GPA: 3.9/4.0 | Jun 2024
