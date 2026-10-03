# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> 当前中文简历文本镜像。

具备 Laravel / Vue.js 生产系统开发经验，并使用 Python 开发过 Text-to-SQL、混合检索与多模态 Agent 项目。

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 开发并维护生产环境反馈平台，负责反馈提交、自动通知和后台管理等核心功能。
- 持续开发 Laravel / Vue.js 业务功能，并排查生产环境中的应用与数据库问题。
- 负责部署和服务器维护，包括服务器升级、Laravel Queue / Worker、SSL 续期与数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护生产环境 POS 应用功能。

## 项目经历

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- 构建本地 Text-to-SQL 服务，使用 XiYanSQL 7B，并加入 schema grounding、SQL 校验、只读执行和有限次数修复。
- 在 100 条 BIRD 测试题中，XiYanSQL 7B 有 58 条执行结果与参考结果一致，并结合错误分析比较不同的 Schema Linking 方案。

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- 构建本地混合检索服务，将 BM25、Qwen3 Embedding 与 RRF 组合，并通过 FastAPI 提供查询接口。
- 在 64 条 EnterpriseRAG-Bench 查询、5,189 份文档上，RRF 的 Recall@10 为 0.763（BM25 0.734），MRR@20 为 0.742（BM25 0.679）。

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- 构建视频问答 Agent：能用字幕回答时直接回答，只有在需要视觉信息时才检查画面或视频片段。
- 在 12 题测试中，加入视觉工具后整体通过率从 16.7% 提升到 50.0%，视觉题通过率为 66.7%。

## 专业技能

- **AI / LLM：** LLM Agents、RAG、Tool Calling、Retrieval、Evaluation、LangGraph
- **编程 / 后端：** Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js、React
- **数据 / 基础设施：** AWS、MySQL、Redis、SQLite、Linux、Git、pytest
- **其他：** Java、C/C++｜中文（母语）、英语（流利）、马来语（中等）

## 教育背景

### 国立清华大学（台湾） | 资讯系统与应用研究所 理学硕士
**2024.09 - 2026.06**

GPA：4.09/4.3｜硕士论文：*Interpreting Implicit Intent through Workplace Hierarchies and Context*

### 中华大学（台湾） | 资讯工程学系 学士
**2022.09 - 2024.06**

GPA：3.9/4.0
