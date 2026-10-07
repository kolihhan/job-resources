# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 负责一套生产反馈平台的完整开发，从系统设计、实现到上线，覆盖反馈提交、自动通知和后台管理流程。
- 在已上线的 Laravel / Vue.js 平台上持续开发新功能，并排查线上应用与数据库问题。
- 负责服务器迁移与升级，以及 Laravel 队列 / Worker / 定时任务、SSL 和生产数据库的维护与故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发和维护已上线 POS 系统功能。

## 项目经历

### [Text-to-SQL 校验与修复系统](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · FastAPI · LangGraph · SQLite · Qwen3.5 9B**

- 构建本地 Text-to-SQL 系统，根据数据库 Schema 和实际数据生成 SQL，并在执行前自动校验，必要时进行修复。
- 在 100 条 BIRD DEV 查询上，校验与修复将可执行查询从 75 条提升至 90 条，并额外修正 6 条查询结果。

### [面向 RAG 的混合检索](https://github.com/kolihhan/local-rag-search)
**Python · FastAPI · BM25 · Qwen3-Embedding-0.6B · RRF**

- 构建面向 RAG 的混合检索服务，结合关键词检索和语义检索，并使用 RRF 融合结果。
- 在 5,189 份文档、64 条 EnterpriseRAG-Bench 查询上，Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

### [多模态视频问答 Agent](https://github.com/kolihhan/hermes-video-tutor)
**Python · Streamlit · Qwen3.5 4B · FFmpeg**

- 构建本地视频问答 Agent，根据问题自动选择转录检索或视频画面 / 短片段检查，并展示作答依据。
- 在 12 题评测中，Agent 答对了 6 个必须查看画面的问题中的 4 个，并在仅需转录文本的问题上避免了不必要的视觉工具调用。

### 硕士论文：基於職場階層與情境脈絡之聽者隱含意圖解析

- 基于 10,645 条职场对话构建图感知检索系统，利用职场角色关系和对话上下文检索证据，帮助判断对话中的隐含意图。
- 在 400 条留出样本上，角色检索将语义 F1 从 0.6440 提升至 0.6793；结合角色和上下文证据后达到 0.6819。

## 专业技能

- **AI / 检索：** RAG、信息检索、LLM 评测、Agent、Tool Calling、LangGraph
- **编程 / 后端：** Python、SQL、JavaScript、PHP、FastAPI、REST API、Laravel、Vue.js
- **数据库 / 工程工具：** MySQL、SQLite、Linux、Git、GitHub Actions、pytest
- **语言：** 中文（母语）、英语（流利）、马来语（中等）

## 教育背景

### 国立清华大学（台湾） | 资讯系统与应用研究所 理学硕士
**2024.09 - 2026.06**

GPA：4.09/4.3

### 中华大学（台湾） | 资讯工程学系 学士
**2022.09 - 2024.06**

GPA：3.9/4.0
