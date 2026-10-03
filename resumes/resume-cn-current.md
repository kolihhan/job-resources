# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> 当前中文简历文本镜像。

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 作为主要开发者负责生产环境反馈平台，完成反馈提交流程、自动通知和后台管理等功能。
- 维护另一套 Laravel / Vue.js 职业平台，持续交付业务功能，并处理生产环境中的应用与数据库问题。
- 参与生产部署与服务器维护，包括服务器迁移/升级、Linux / SSL、Laravel Queue / Worker 与数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护生产环境 POS 应用功能。

## 项目经历

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite**

- 以 XiYanSQL 7B 搭建本地 Text-to-SQL 流程，加入 schema / value grounding、SQL 校验、只读执行和有限次数修复。
- 在 100 条 BIRD 测试题上达到 58% execution-match；Schema Linking 调整修正了 7 条失败样本，同时造成 7 条回退，用于定位下一步优化方向。

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- 搭建 BM25 + Qwen3 Embedding + RRF 的混合检索流程，通过 FastAPI 提供查询接口，并保留检索与排序来源用于调试。
- 在 64 条 EnterpriseRAG-Bench 查询、5,189 份文档上，RRF 相比 BM25 将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

### [Hermes Video Tutor](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- 搭建工具调用式视频问答 Agent，根据问题在字幕、画面和视频片段之间选择证据，而不是所有问题都调用视觉工具。
- 在 12 题配对测试中，多模态路由将整体通过率从 16.7% 提升至 50.0%；视觉题通过率为 66.7%，文本可回答问题未产生额外视觉调用。

## 专业技能

- **AI / LLM：** LLM Systems、RAG、Tool Calling、Retrieval / Evaluation、LangGraph
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
