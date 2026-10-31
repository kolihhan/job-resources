# Ko Lih Han

Malaysia | [+60 17-424 6282](tel:+60174246282) | [lihhanko526@gmail.com](mailto:lihhanko526@gmail.com) | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## Education

**National Tsing Hua University** | M.S., Information Systems & Applications | GPA 4.09/4.3 | Jun 2026  
**Chung Hua University** | B.S., Computer Science & Information Engineering | GPA 3.9/4.0 | Jun 2024

## Research Experience

**Interpreting Implicit Intent through Workplace Hierarchies and Context**  
*M.S. Thesis | National Tsing Hua University | NLP · Graph Learning · Role/Context KGs · Llama 3.1-8B*

- Studied how workplace implicit intent changes with conversational context and speaker–listener role/hierarchy, rather than treating each utterance in isolation.
- Built a pipeline from LLM-extracted speaker/listener states to GCN/GAT graph representations, then retrieved complementary evidence from a Role KG and Context KG for Llama 3.1-8B interpretation.
- Compared Baseline, Prior KG, Role KG, Context KG, and DualKG on 400 targets; in target-only evaluation, DualKG achieved the highest observed semantic F1 among the evaluated methods (0.682 vs 0.644 baseline).

## Selected AI Projects

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Python · Qwen3.5-9B · QLoRA / PEFT · Transformers · llama.cpp*

- Built a tool-using agent with search, file inspection, Python execution, timeouts, duplicate blocking, and trace logs.
- QLoRA on corrective failure examples raised 200-task success from 34.5% to 62.0%.
- Evaluated on GAIA100, raising accuracy from 9% to 18%; failure analysis showed over-search remained the main failure mode.

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*Python · BM25 · Qwen embeddings · RRF · FastAPI*

- Built a hybrid retriever combining BM25, Qwen dense retrieval, RRF, and inspectable rank provenance.
- Evaluated 64 queries over 5,189 documents; Recall@10 rose from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742.

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Python · FastAPI · LangGraph · SQLite · Qwen3.5-9B · pytest*

- Built an NL-to-SQL service with schema grounding, validation, bounded repair, and read-only execution.
- Shared one service layer across FastAPI, CLI, Streamlit, and evaluation to prevent path drift.
- Evaluated 100 BIRD DEV queries; correct-query accuracy rose from 33% to 39%, fixing 6 queries with no regressions.

## Software Engineering Experience

**Software Developer**, **Kahap Inc** | Part-time | Aug 2022 - Aug 2026

- Built and launched a feedback platform for submissions, discussions, admin review, and notifications.
- Maintained a Laravel/Vue.js production platform across queues, scheduled jobs, migrations, and Linux operations.
- Integrated GPT-SoVITS, pronunciation checks, and text checks into backend speech workflows.

**Full-Stack Developer Intern**, **Pac Com Solution** | Jun 2021 - Jan 2022

- Built features and fixed bugs in a production Laravel/Vue.js POS system.

## Skills

**AI / LLM:** Agents & tool use, RAG / hybrid retrieval, evaluation, PEFT / QLoRA, Transformers, LangGraph, llama.cpp  
**Backend:** Python, FastAPI, PHP, Laravel, REST APIs, SQL, MySQL, SQLite  
**Web & Tools:** JavaScript, Vue.js, Linux, Git, pytest  
**Languages:** Chinese (Native), English (Fluent), Malay (Intermediate)
