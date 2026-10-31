# Ko Lih Han

Malaysia | [+60 17-424 6282](tel:+60174246282) | [lihhanko526@gmail.com](mailto:lihhanko526@gmail.com) | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## Software Engineering Experience

**Software Developer**, **Kahap Inc** | Part-time | Aug 2022 - Aug 2026

- Built and shipped a feedback platform covering submissions, discussions, admin review, and notifications.
- Kept the Laravel/Vue.js system running in production, handling queues, scheduled jobs, migrations, and Linux server operations.
- Added GPT-SoVITS, pronunciation checks, and text validation to backend speech workflows.

**Full-Stack Developer Intern**, **Pac Com Solution** | Jun 2021 - Jan 2022

- Implemented features and fixes for a production Laravel/Vue.js POS system.

## Research Experience

**Interpreting Implicit Intent through Workplace Hierarchies and Context**  
*M.S. Thesis, National Tsing Hua University | NLP · Graph Learning · Role/Context KGs · Llama 3.1-8B*

- Examined workplace utterances whose intent shifts with conversational context and speaker-listener roles, instead of interpreting each utterance on its own.
- Encoded LLM-extracted speaker/listener states with GCN/GAT, then used Role KG and Context KG retrieval to provide evidence for Llama 3.1-8B.
- On 400 target-only cases, DualKG reached semantic F1 0.682 versus 0.644 for the text-only baseline, outperforming Prior KG, Role KG, and Context KG.

## Projects

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Python · Qwen3.5-9B · QLoRA / PEFT · Transformers · llama.cpp*

- Built a tool-using Qwen agent with search, file inspection, Python execution, timeouts, duplicate blocking, and trace logs.
- QLoRA on corrective failure examples raised success from 34.5% to 62.0% on a 200-task evaluation.
- GAIA100 accuracy rose from 9% to 18%; trace review showed over-search was still the main failure mode.

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*Python · BM25 · Qwen embeddings · RRF · FastAPI*

- Combined BM25 and Qwen dense retrieval with RRF, while keeping rank provenance inspectable.
- Across 64 queries and 5,189 documents, Recall@10 rose from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742.

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Python · FastAPI · LangGraph · SQLite · Qwen3.5-9B · pytest*

- Built an NL-to-SQL pipeline with schema grounding, validation, bounded repair, and read-only execution.
- Kept FastAPI, CLI, Streamlit, and evaluation on one service layer to avoid behavior drift between interfaces.
- On 100 BIRD DEV queries, correct-query accuracy rose from 33% to 39%, fixing 6 cases without regressions.

## Education

**National Tsing Hua University** | M.S., Information Systems & Applications | GPA 4.09/4.3 | Jun 2026  
**Chung Hua University** | B.S., Computer Science & Information Engineering | GPA 3.9/4.0 | Jun 2024

## Skills

**AI / LLM:** Agents & tool use, RAG / hybrid retrieval, evaluation, PEFT / QLoRA, Transformers, LangGraph, llama.cpp  
**Backend:** Python, FastAPI, PHP, Laravel, REST APIs, SQL, MySQL, SQLite  
**Web & Tools:** JavaScript, Vue.js, Linux, Git, pytest  
**Languages:** Chinese (Native), English (Fluent), Malay (Intermediate)
