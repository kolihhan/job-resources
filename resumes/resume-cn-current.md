# 高立恒

**大模型应用开发工程师 / AI 应用工程师 / 后端开发工程师**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> 当前已批准中文简历的文本镜像；2026-10-03 与 `resume-cn-current.pdf` 同步。

国立清华大学资讯系统与应用研究所理学硕士，具备生产系统后端/全栈开发经验，并完成 Text-to-SQL、混合检索和多模态工具调用等可评测 AI 应用系统。

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 作为主要开发者负责生产环境反馈平台，覆盖反馈提交、自动通知与后台管理，并持续参与上线后的维护与问题排查。
- 维护并扩展 Laravel / Vue.js 生产应用，持续交付业务功能，并排查应用层与数据库问题。
- 负责部署与服务器运维，包括服务器升级、Laravel Queue / Worker、SSL 维护及数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护生产环境 POS 应用的全栈功能。

## 项目经历

### [Semantic Text-to-SQL Agent](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite**

- 构建本地 Text-to-SQL 服务，包含确定性 SQL 校验、SQLite 只读执行、有上限修复，以及一次性 Clause-Guided Semantic Revision。
- 在冻结的 100 条 BIRD DEV 查询上，受控路径将执行成功率从 63% 提升至 82%，官方 BIRD EX 从 31% 提升至 34%；明确区分执行可靠性与语义正确性。

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen Embeddings · RRF · FastAPI**

- 在 64 条官方 Confluence-compatible 查询、5,189 份文档上评测 BM25、Qwen 稠密检索与 RRF；混合检索达到 0.7630 Recall@10、0.7418 MRR@20、0.8438 Hit@10，并保留逐结果排名来源。

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- 构建本地多模态视频 QA Agent：优先使用字幕证据，仅在需要时检查帧/视频片段；在冻结的 12 题自建配对测试中，视觉问题完整通过率为 66.7%，且文本可回答问题未产生不必要的视觉工具调用。

## 专业技能

- **AI / LLM：** LLM Agents、RAG、Tool Calling、Retrieval / LLM Evaluation、Embeddings、LangGraph
- **编程 / 后端：** Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js、React
- **云与数据：** AWS、MySQL、Redis、SQLite、Linux
- **其他：** Java、C/C++、Git、pytest｜中文（母语）、英语（流利）、马来语（中等）

## 教育背景

### 国立清华大学（台湾） | 资讯系统与应用研究所 理学硕士
**2024.09 - 2026.06**

GPA：4.09/4.3｜硕士论文：*Interpreting Implicit Intent through Workplace Hierarchies and Context*

### 中华大学（台湾） | 资讯工程学系 学士
**2022.09 - 2024.06**

GPA：3.9/4.0
