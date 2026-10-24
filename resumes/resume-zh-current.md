# Ko Lih Han

**软件工程师 | 应用 AI 与 LLM 系统**

马来西亚 | [+60 17-424 6282](tel:+60174246282) | [lihhanko526@gmail.com](mailto:lihhanko526@gmail.com) | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## 工作经历

**软件开发工程师**，Kahap Inc | 兼职 | 2022.08 – 2026.08

- 从 0 到 1 构建并上线反馈平台，统一处理意见提交、讨论、管理员审核与通知。
- 维护 Laravel/Vue.js 生产平台，负责队列任务、定时任务、数据库/服务器迁移及 Linux 故障排查。
- 将 GPT-SoVITS、发音检查与文本检查集成到后端语音生成流程。

**全栈开发实习生**，Pac Com Solution | 2021.06 – 2022.01

- 在生产环境 Laravel/Vue.js POS 系统中开发功能并修复缺陷。

## 项目经历

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Python · Qwen3.5-9B · QLoRA / PEFT · Transformers · llama.cpp*

- 构建可调用搜索、文件检查与 Python 执行工具的 Agent，并加入超时、重复调用拦截与执行追踪。
- 基于运行失败样本构造纠错数据并使用 QLoRA 微调，在固定的 200 个评测任务上将成功率从 34.5% 提升至 62.0%。
- 在 GAIA100 的 100 个任务上将准确率从 9% 提升至 18%；主要失败模式仍为过度搜索。

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Python · FastAPI · LangGraph · SQLite · Qwen3.5-9B · pytest*

- 搭建 NL-to-SQL 服务，通过 Schema Grounding、确定性校验、有限次修复与只读执行提升查询可靠性。
- 统一 FastAPI、CLI、Streamlit 与评测流程的服务层，确保交互与评测走同一执行路径。
- 在 100 条 BIRD DEV 查询上将正确查询率从 33% 提升至 39%，修复 6 个错误，0 个回退。

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*Python · BM25 · Qwen Embeddings · RRF · FastAPI*

- 构建本地混合检索系统，结合 BM25 与 Qwen 向量检索并使用 RRF 融合，同时保留可检查的排序来源。
- 在 5,189 篇文档、64 条 EnterpriseRAG-Bench 查询上，Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

## 研究经历

**基於職場階層與情境脈絡之聽者隱含意圖解析** | 硕士论文  
*国立清华大学（NTHU） · NLP · Retrieval · Role/Context KGs · Llama 3.1-8B*

- 整理并标注来自 7 个论坛的 20,455 条职场话语，标签覆盖说话者/听者状态、情绪与沟通目的。
- 基于 Llama 3.1-8B 构建 Role KG 与 Context KG 检索，在 400 条目标话语上将语义 F1 从 0.644 提升至 0.682。

## 技能

**AI / LLM：** Agent 与工具调用，RAG / 混合检索，模型评测，PEFT / QLoRA，Hugging Face Transformers，LangGraph，llama.cpp  
**后端：** Python，FastAPI，PHP，Laravel，REST APIs，SQL，MySQL，SQLite  
**Web 与工具：** JavaScript，Vue.js，Linux，Git，pytest  
**语言：** 中文（母语水平），英语（流利），马来语（中级）

## 教育背景

**国立清华大学（NTHU）** | 信息系统与应用 硕士 | GPA 4.09/4.3 | 2026.06  
**中华大学** | 计算机科学与信息工程 学士 | GPA 3.9/4.0 | 2024.06
