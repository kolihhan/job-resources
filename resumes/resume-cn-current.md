# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> 当前经事实审计的中文简历文本镜像；2026-10-03 与 `resume-cn-current.pdf` 同步。

具备 Laravel / Vue.js 生产系统开发经验，并使用 Python 构建 Text-to-SQL、混合检索与工具调用等 AI 应用。

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 开发并维护生产环境反馈平台的核心流程，包括反馈提交、自动通知与后台管理功能。
- 持续交付 Laravel / Vue.js 业务功能，并处理生产环境中的应用层与数据库问题。
- 支持部署与服务器运维，包括服务器升级、Laravel Queue / Worker、SSL 续期及数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护生产环境 POS 应用功能。

## 项目经历

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- 构建本地 NL-to-SQL 服务，使用 XiYanSQL 7B，并加入 schema grounding、SQL 校验、只读执行与有上限修复。
- 在冻结的 100 条 BIRD 样本上，XiYanSQL 7B 按仓库固定的 execution-set scorer 达到 58/100，并通过错误分析继续测试 schema-linking 方案。

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- 构建本地混合检索服务，组合 BM25、Qwen3 Embedding 与 RRF，并通过 FastAPI 返回结果及排名来源。
- 在 64 条 EnterpriseRAG-Bench 查询、5,189 份文档上，RRF 相比 BM25 将 Recall@10 从 0.7341 提升至 0.7630，MRR@20 从 0.6792 提升至 0.7418。

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- 构建本地视频 QA Agent：先检索字幕，仅在问题需要视觉信息时检查画面或视频片段。
- 在冻结的 12 题配对测试中，多模态模式将整体完整通过率从 16.7% 提升至 50.0%，视觉问题达到 66.7%。

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
