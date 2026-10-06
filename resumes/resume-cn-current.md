# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

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

- 从初始开发到上线持续负责一套生产反馈平台，统一反馈提交、自动通知和后台管理流程。
- 为现有应用接入 GPT-SoVITS 语音生成 API，并增加文本缺失与发音结果检查。
- 负责另一套 Laravel / Vue.js 职业发展平台的功能迭代，排查线上应用和数据库问题。
- 负责该平台的部署与线上运维，包括服务器迁移 / 升级、Laravel 队列 / Worker / 定时任务、SSL 续期及数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护已上线的 POS 系统功能。

## 项目经历

### [Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · Qwen3.5 9B · LangGraph · FastAPI · SQLite**

- 搭建本地 Text-to-SQL 流程，包含 Schema / Value Grounding、确定性 SQL 校验、只读执行和限次修复。
- 在固定 100 题 BIRD DEV 切片上，Guarded 校验 + 修复将 official EX 从 33% 提升至 39%，保守执行成功率从 75% 提升至 90%，且没有 correct-to-wrong EX 回退。

### [Local RAG Search](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- 搭建基于 BM25、Qwen3 Embedding 和 RRF 的混合检索 API，返回每条结果的 BM25、Dense 与 RRF 排名，便于调试。
- 在包含 64 条查询、5,189 份文档的 EnterpriseRAG-Bench 固定切片上，RRF 将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

### 硕士论文 - 职场隐含意图理解
**Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation**

- 构建基于角色关系与上下文检索的职场隐含意图框架，数据覆盖 51,414 篇帖子和 20,455 条抽取语句。
- 在 401 条留出评测语句上，Dual-KG Top1 的自动语义 F1 为 0.6890，对比无检索证据 baseline 的 0.6250。

## 专业技能

- **AI：** RAG、信息检索、LLM 评测、LangGraph
- **编程 / 后端：** Python、SQL、JavaScript、PHP、FastAPI、REST API、Laravel、Vue.js
- **数据 / 基础设施：** MySQL、SQLite、Linux、Git、GitHub Actions、pytest
- **语言：** 中文（母语）、英语（流利）、马来语（中等）
