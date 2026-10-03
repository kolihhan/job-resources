# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> 当前经事实审计的中文简历文本镜像；2026-10-03 与 `resume-cn-current.pdf` 同步。

具备生产环境后端/全栈开发经验，能够构建并评测 Text-to-SQL、混合检索与多模态工具调用等 AI 系统。

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 作为主要开发者负责生产环境反馈平台，覆盖提交流程、自动通知与后台管理，从功能实现持续参与上线维护与问题排查。
- 维护并扩展 Laravel / Vue.js 生产应用，持续交付业务功能，并处理应用层与数据库问题。
- 负责部署与服务器运维，包括服务器升级、Laravel Queue / Worker、SSL 维护及数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护生产环境 POS 应用的全栈功能。

## 项目经历

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- 构建本地 Text-to-SQL 系统，包含 schema grounding、确定性 SQL 校验、只读执行与有上限修复。
- 在冻结的 100 条 BIRD 样本上，对 XiYanSQL 7B 的 lexical 与 DGSL grounding 进行对照；两者在项目内执行集匹配评分下均为 58/100（7 条修正 / 7 条回退）。

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- 构建本地混合检索系统，组合 BM25、Qwen 稠密检索与 RRF，并保留逐结果排名来源。
- 在 EnterpriseRAG-Bench v1.0.0 的 64 条官方 Confluence-compatible 查询、5,189 份文档上，RRF 相比 BM25 将 Recall@10 从 0.7341 提升至 0.7630，MRR@20 从 0.6792 提升至 0.7418。

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- 构建本地视频 QA Agent：优先使用字幕证据，仅在需要时检查帧/视频片段，并保留可见证据与证据不足时的拒答。
- 在冻结的 12 题自建配对测试中，多模态模式将整体完整通过率从 16.7% 提升至 50.0%，视觉问题达到 66.7%，且文本可回答问题未产生不必要的视觉调用。

## 专业技能

- **AI / LLM：** LLM Agents、RAG、Tool Calling、Retrieval / Evaluation、LangGraph
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
