# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> 当前中文简历文本镜像。

## 教育背景

### 国立清华大学（台湾） | 资讯系统与应用研究所 理学硕士
**2024.09 - 2026.06**

GPA：4.09/4.3

### 中华大学（台湾） | 资讯工程学系 学士
**2022.09 - 2024.06**

GPA：3.9/4.0

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 作为主要开发者负责一套已上线的反馈平台，将反馈提交、自动通知和后台管理流程集中到同一系统。
- 维护另一套 Laravel / Vue.js 职业平台，持续交付业务功能并排查线上应用与数据库问题。
- 负责部署与服务器维护，包括服务器迁移/升级、Laravel Queue / Worker、SSL 续期和数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护生产环境 POS 应用功能。

## 项目经历

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- 使用 XiYanSQL 7B 搭建本地 Text-to-SQL 流程，加入 Schema / Value Grounding、SQL 校验、只读执行和有限次数修复。
- 在 100 条 BIRD 测试题中，58 条查询的执行结果与参考结果一致，并结合错误分析调整 Grounding 与修复策略。

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- 搭建 BM25 + Qwen3 Embedding + RRF 的混合检索 API，并保留每条结果的检索信息用于调试。
- 在 64 条 EnterpriseRAG-Bench 查询、5,189 份文档上，RRF 将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

### 硕士论文 - 职场隐含意图理解
**Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation**

- 构建角色与语境证据框架，用于生成职场对话中听者可能感受到的隐含意图；数据来自 51,414 篇帖子、20,455 条抽取语句。
- 在 401 条留出测试语句上，Role-Context Top1 的自动语义 F1 从 baseline 0.6250 提升至 0.6890。

## 专业技能

- **AI：** RAG、Information Retrieval、LLM Evaluation、LangGraph
- **编程 / 后端：** Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js
- **数据 / 基础设施：** MySQL、Redis、SQLite、AWS、Linux、Git、pytest
- **语言：** 中文（母语）、英语（流利）、马来语（中等）
