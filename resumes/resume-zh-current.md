# 高立恒

**KO LIH HAN | 软件工程师 | Applied AI / LLM Systems**

马来西亚籍 | +60 17-424 6282 | lihhanko526@gmail.com | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## 教育背景

**国立清华大学（NTHU）** | 信息系统与应用硕士 | GPA 4.09/4.3 | 2026.06  
**中华大学** | 计算机科学与信息工程学士 | GPA 3.9/4.0 | 2024.06

## 工作经历

**Kahap Inc** | 软件开发工程师 · 兼职 | 2022.08–2026.08

- 从零开发并上线反馈平台，整合意见提交、讨论、后台审核和通知流程。
- 负责 Laravel/Vue.js 线上系统维护，包括队列与定时任务、数据库/服务器迁移和 Linux 故障排查。
- 接入 GPT-SoVITS，并在后端加入发音与文本检查，服务语音生成流程。

**Pac Com Solution** | 全栈开发实习生 | 2021.06–2022.01

- 参与 Laravel/Vue.js POS 系统功能开发和缺陷修复，覆盖后端与部分前端工作。

## 项目经历

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Python · Qwen3.5-9B · QLoRA / PEFT · Transformers · llama.cpp*

- 用 Qwen3.5-9B 开发工具调用 Agent，支持搜索、文件读取和 Python 执行，并加入超时、重复调用拦截和运行追踪。
- 针对运行失败整理纠错样本并做 QLoRA 微调，200 个固定任务成功率从 **34.5%** 提升到 **62.0%**。
- 在 GAIA100 的 100 个任务上，准确率从 **9%** 提升到 **18%**；主要问题仍是过度搜索。

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Python · FastAPI · LangGraph · SQLite · Qwen3.5-9B · pytest*

- 开发本地 NL-to-SQL 服务，包含 Schema Grounding、确定性校验、最多两次修复和只读执行。
- FastAPI、CLI、Streamlit 和评测共用同一服务层，避免应用路径与评测路径不一致。
- 在 100 条 BIRD DEV 查询上，正确率从 **33%** 提升到 **39%**，修复 6 条错误查询，未引入回退。

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*Python · BM25 · Qwen Embeddings · RRF · FastAPI*

- 实现 BM25、Qwen 向量检索与 RRF 融合的本地混合检索，并保留结果的排名来源便于分析。
- 在 5,189 篇文档和 64 条 EnterpriseRAG-Bench 查询上，Recall@10 从 **0.734** 提升到 **0.763**，MRR@20 从 **0.679** 提升到 **0.742**。

## 研究经历

**基於職場階層與情境脈絡之聽者隱含意圖解析** | 硕士论文 · 国立清华大学

- 整理并标注来自 7 个论坛的 20,455 条职场话语，标签包括说话者/听者状态、情绪和沟通目的。
- 设计 Role KG 与 Context KG 检索并结合 Llama 3.1-8B；在 400 条固定样本上，语义 F1 从 **0.644** 提升到 **0.682**。

## 专业技能

**AI / LLM：** Agent 与工具调用；RAG / 混合检索；模型评测；PEFT / QLoRA；Hugging Face Transformers；LangGraph；llama.cpp  
**后端：** Python；FastAPI；PHP；Laravel；REST API；SQL；MySQL；SQLite  
**Web / 工具：** JavaScript；Vue.js；Linux；Git；pytest  
**语言：** 中文（母语水平）；英语（流利）；马来语（中级）
