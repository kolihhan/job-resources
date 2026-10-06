# 高立恒

**软件工程师｜AI 应用 / 后端开发**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 从初始开发到上线持续负责一套生产反馈平台，统一反馈提交、自动通知与后台管理流程。
- 为现有应用接入 GPT-SoVITS 语音生成 API，并增加文本缺失与发音结果检查。
- 维护 Laravel / Vue.js 职业发展平台，并负责服务器迁移与升级、队列 / Worker / 定时任务、SSL 续期及数据库故障排查等线上运维。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护已上线 POS 系统功能。

## 项目经历

### [Text-to-SQL 校验与修复系统](https://github.com/kolihhan/semantic-text2sql-agent)
**Python · Qwen3.5 9B · LangGraph · FastAPI · SQLite**

- 搭建包含 Schema / Value Grounding、确定性 SQL 校验、只读执行与限次修复的本地 Text-to-SQL 流程。
- 在固定 100 题 BIRD DEV 切片上，Guarded 校验 + 修复将 official EX 从 33% 提升至 39%，保守执行成功率从 75% 提升至 90%，EX 转移为 6 个 wrong-to-correct、0 个 correct-to-wrong。

### [面向 RAG 的混合检索](https://github.com/kolihhan/local-rag-search)
**Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI**

- 构建可追踪 BM25、Dense 与 RRF 排名来源的混合检索器；在 64 条查询、5,189 份文档的固定切片上，RRF 将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

### [多模态视频问答 Agent](https://github.com/kolihhan/hermes-video-tutor)
**Python · Hermes Agent · Multimodal Tools · Streamlit**

- 构建可在转录检索与帧 / 短片段检查间自主选择的视频问答 Agent，并展示工具调用与证据，证据不足时允许拒答。
- 在 12 题小型固定测试集上，多模态模式在视觉必需问题上的 full pass 为 66.7%，对比仅转录模式为 0%，且对可由转录回答的问题没有多余视觉调用。

### 硕士论文：上下文感知的职场隐含意图理解
**Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation**

- 基于 51,414 篇帖子和 20,455 条语句构建角色与上下文证据检索，区分稳定的职场角色证据与局部上下文证据。
- 在 401 条留出语句上，Dual-KG Top1 的语义 F1 为 0.6890，对比无检索证据 baseline 的 0.6250。

## 专业技能

- **AI / 检索：** RAG、信息检索、LLM 评测、Agent、Tool Calling、LangGraph
- **编程 / 后端：** Python、SQL、JavaScript、PHP、FastAPI、REST API、Laravel、Vue.js
- **数据 / 基础设施：** MySQL、SQLite、Linux、Git、GitHub Actions、pytest
- **语言：** 中文（母语）、英语（流利）、马来语（中等）

## 教育背景

### 国立清华大学（台湾） | 资讯系统与应用研究所 理学硕士
**2024.09 - 2026.06**

GPA：4.09/4.3

### 中华大学（台湾） | 资讯工程学系 学士
**2022.09 - 2024.06**

GPA：3.9/4.0
