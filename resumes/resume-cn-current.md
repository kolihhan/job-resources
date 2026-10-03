# 高立恒

**大模型应用开发工程师 / AI 应用工程师 / 后端开发工程师**

+60 17-424 6282 | lihhanko526@gmail.com | github.com/kolihhan

> 当前已批准中文简历的文本镜像；2026-10-03 从 `resume-cn-current.pdf` 同步。

国立清华大学计算机科学硕士，具备生产系统软件开发经验，并完成 LLM Agent、RAG 检索评测、多模态工具调用与 Text-to-SQL 可靠性等可评测 AI 应用项目。

## 工作经历

### Kahap Inc | 软件开发工程师（兼职）
**2022.08 - 2026.08**

- 作为主要开发者负责生产环境反馈平台，覆盖反馈提交、自动通知与后台管理等功能，支撑实际业务流程线上运行。
- 维护并扩展 Laravel / Vue.js 生产应用，持续交付业务功能，并排查应用层与数据库问题。
- 负责生产环境部署与服务器运维，包括服务器升级、Laravel Queue / Worker、SSL 维护及数据库故障排查。

### Pac Com Solution | 全栈开发实习生
**2021.06 - 2022.01**

- 使用 Laravel / Vue.js 开发并维护生产环境 POS 应用的全栈功能。

## 项目经历

### Semantic Text-to-SQL Agent
**Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite**

- 构建本地 Text-to-SQL 服务，包含确定性 SQL 校验、SQLite 只读执行、有上限修复，以及一次性 Clause-Guided Semantic Revision 语义检查。
- 在冻结的 100 条 BIRD DEV 查询上，受控修复将执行成功率从 63% 提升至 82%，官方 EX 从 31% 提升至 34%（CGSR 前基线）。

### Local RAG Search
**Python · BM25 · Qwen Embeddings · RRF · FastAPI**

- 在 64 条查询、5,189 份文档上对 BM25、Qwen 稠密检索与 RRF 进行基准测试；混合检索达到 0.7630 Recall@10、0.7418 MRR@20，并保留逐 Query 排名来源。

### Hermes Video Tutor
**Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal**

- 构建自适应视频 QA Agent：优先使用字幕证据，必要时再检查帧 / 视频片段；在 12 组配对案例中，视觉问题通过率为 66.7%，视觉问题工具调用覆盖率为 100%。

### Small-Agent QLoRA
**Python · Qwen3.5 4B · QLoRA · GAIA · Tool Use**

- 构建本地工具调用 Agent，支持 search / read / inspect / python，并实现步数上限、重复调用拦截、可见轨迹、验证式轨迹收集与训练数据泄漏检查。
- 实现 QLoRA 训练入口与冻结 GAIA 分区上的 Base-vs-LoRA 配对评测；在有效配对实验完成前不宣称微调带来提升。

## 专业技能

- **AI / LLM：** LLM Agents、RAG、Tool Calling、Retrieval / LLM Evaluation、Embeddings、LangGraph、QLoRA / PEFT
- **编程 / 后端：** Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js、React
- **云与数据：** AWS Lambda、API Gateway、S3、RDS、MySQL、Redis、SQLite、Linux
- **其他：** Java、C/C++、Git、pytest｜中文（母语）、英语（流利）、马来语（中等）

## 教育背景

### 国立清华大学（台湾） | 计算机科学硕士
**2024.09 - 2026.06**

GPA：4.09/4.3｜硕士论文：*Interpreting Implicit Intent through Workplace Hierarchies and Context*

### 中华大学（台湾） | 计算机科学学士
**2022.09 - 2024.06**

GPA：3.9/4.0
