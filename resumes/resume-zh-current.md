# 高立恒

马来西亚籍 | [+60 17-424 6282](tel:+60174246282) | [lihhanko526@gmail.com](mailto:lihhanko526@gmail.com) | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## 教育背景

**国立清华大学（NTHU）** | 信息系统与应用硕士 | GPA 4.09/4.3 | 2026.06  
**中华大学** | 计算机科学与信息工程学士 | GPA 3.9/4.0 | 2024.06

## 工作经历

**Kahap Inc** | 软件开发工程师（兼职） | 2022.08–2026.08

- 开发并上线反馈平台的核心功能，包括意见提交、讨论、后台审核、通知与定时任务，主要使用 Laravel、Vue.js 和 MySQL。
- 维护线上系统与服务器环境，处理部署、队列 Worker、定时任务、数据库迁移、SSL 更新及 Linux 故障排查。
- 在语音生成流程中接入 GPT-SoVITS，并加入发音与文本校验。

**Pac Com Solution** | 全栈开发实习生 | 2021.06–2022.01

- 参与 Laravel/Vue.js POS 系统的功能开发与问题修复，包括后端逻辑和前端页面实现。

## 科研经历

**职场对话隐含意图理解：上下文与角色关系建模**  
*硕士论文，国立清华大学 | NLP · 图学习 · 知识图谱 · LLM*

- 研究上下文与说话者/听者角色如何影响职场话语的隐含意图判断。
- 将说话者和听者状态表示为对话图，并检索角色与上下文知识，为 Llama 3.1-8B 提供补充信息。
- 在 400 条仅给出目标话语的样本上，加入角色与上下文知识后，语义 F1 从 0.644 提升至 0.682。

## 项目经历

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Qwen3.5-9B · QLoRA · Tool Use · Agent Evaluation*

- 构建可调用搜索、文件读取和 Python 的 Qwen Agent，用于完成多步骤任务。
- 从失败轨迹中整理纠错样本进行 QLoRA 微调，在 200 个固定评测任务上将成功率从 34.5% 提升至 62.0%。
- GAIA100 准确率从 9% 提升至 18%；运行轨迹分析显示，过度搜索仍是主要失败原因。

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*BM25 · Dense Retrieval · RRF · Retrieval Evaluation*

- 对比 BM25、向量检索与 RRF 混合检索，在 5,189 篇文档、64 条查询上进行评测。
- 混合检索将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Qwen3.5-9B · Schema Grounding · SQL Validation · Repair*

- 构建 Text-to-SQL 系统，利用数据库 Schema 生成 SQL，并在执行前完成校验与有限次数修复。
- 在 100 条 BIRD DEV 查询上，正确率从 33% 提升至 39%，修复 6 条错误查询且没有新增错误案例。

## 专业技能

**LLM / NLP：** RAG、混合检索、知识图谱、Tool-using Agent、PEFT / QLoRA、LLM 评测  
**机器学习：** Transformers、图神经网络、Embedding / Dense Retrieval  
**工程开发：** Python、FastAPI、PHP、Laravel、Vue.js、REST API、SQL、MySQL、SQLite  
**工具：** Linux、Git、pytest、llama.cpp、LangGraph  
**语言：** 中文（母语）、英语（流利）、马来语（中级）