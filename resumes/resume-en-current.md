# Ko Lih Han

**Software Engineer | Applied AI & LLM Systems**

Malaysia | +60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan | linkedin.com/in/ko-lih-han-748993241

## Experience

### Software Developer (Part-time)
**Kahap Inc | Aug 2022 - Aug 2026**

- Owned the 0-to-1 build and production rollout of a feedback platform, centralizing submissions, discussions, admin review, and notifications into one operational system.
- Operated a Laravel/Vue.js career platform across queue workers, scheduled jobs, SSL renewals, database/server migrations, and Linux hosting.
- Integrated GPT-SoVITS plus automated pronunciation and text checks into existing backend workflows for AI-assisted content features.

### Full-Stack Developer Intern
**Pac Com Solution | Jun 2021 - Jan 2022**

- Shipped and debugged Laravel/Vue.js features across backend and frontend paths in a production POS codebase.

## Projects

### [Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora) | 2026
**Python · Qwen3.5-9B · QLoRA / PEFT · Transformers · llama.cpp**

- Built a single-model tool agent for search, file inspection, and Python execution, with bounded tool errors, duplicate-call blocking, timeouts, source-size limits, and persisted traces.
- Diagnosed policy failures from traces and turned them into state-aware corrective QLoRA supervision, raising exact closed-loop success from 34.5% to 62.0% on 200 frozen tasks.
- Rejected full-trajectory SFT after held-out regression; on GAIA100, an intermediate tuned checkpoint doubled base accuracy from 9% to 18%, while the final continuation held 18% but exposed over-search / failure-to-finalize.

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent) | 2026
**Python · FastAPI · LangGraph · SQLite · Qwen3.5-9B**

- Designed a local NL-to-SQL service around a key reliability gap: executable SQL can still be wrong; combined schema grounding, deterministic preflight, bounded repair, read-only execution, and explicit traces.
- On 100 frozen BIRD DEV queries, guarded verification/repair raised conservative execution success from 75% to 90% and EX-compatible match from 33% to 39%, recovering 6 wrong answers with 0 regressions.
- Kept the simpler guarded path after semantic-review and grounding ablations failed to improve net correctness; reused one backend layer across FastAPI, CLI, and Streamlit.

## Research

### Context-Aware Implicit Workplace Meaning
**M.S. Thesis | National Tsing Hua University**  
*NLP · retrieval · role/context knowledge graphs · Llama 3.1-8B*

- Built a listener-side NLP pipeline for implicit workplace meaning, curating 20,455 utterances across 7 boards and labeling speaker/listener state, emotion, and communicative purpose.
- Built separate Role KG and Context KG retrieval paths and fused top-1 evidence into local Llama 3.1-8B generation to model who said what, to whom, and under what dialogue context.
- Designed a controlled evaluation on the same 400 aligned targets with fixed prompts across target-only and preceding-context arms, isolating context/evidence changes from prompt drift.
- Dual-KG improved target-only semantic F1 from 0.644 to 0.682 and preceding-context F1 from 0.680 to 0.691; the baseline context gain (+0.036) showed dialogue history remained a major signal alongside graph evidence.

## Skills

- **AI / LLM:** Agents & tool use, RAG / retrieval, model evaluation, PEFT / QLoRA, Hugging Face Transformers, LangGraph, llama.cpp
- **Backend:** Python, FastAPI, PHP, Laravel, SQL, REST APIs, JavaScript
- **Data / Infrastructure:** MySQL, SQLite, Linux, Git, GitHub Actions, pytest
- **Frontend:** Vue.js, React
- **Languages:** Chinese (Native/Bilingual), English (Fluent), Malay (Intermediate)

## Education

### National Tsing Hua University
**Master of Science, Information Systems & Applications | GPA: 4.09/4.3 | Jun 2026**

### Chung Hua University
**Bachelor of Science, Computer Science & Information Engineering | GPA: 3.9/4.0 | Jun 2024**
