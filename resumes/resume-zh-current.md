# 高立恒

马来西亚籍 | [+60 17-424 6282](tel:+60174246282) | [lihhanko526@gmail.com](mailto:lihhanko526@gmail.com) | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## 教育背景

**国立清华大学（NTHU）**  
信息系统与应用硕士 | GPA 4.09/4.3 | 2026.06

**中华大学**  
计算机科学与信息工程学士 | GPA 3.9/4.0 | 2024.06

## 工作经历

**Kahap Inc** | 软件开发工程师 · 兼职 | 2022.08–2026.08

- 开发并上线基于 Laravel/Vue.js 的反馈平台核心模块，覆盖意见提交、讨论、后台审核、通知及定时任务。
- 承担线上部署与运维，处理队列 Worker、定时任务、数据库迁移、SSL 更新及 Linux 服务器故障。
- 将 GPT-SoVITS 接入后端语音流程，并在合成前增加发音与文本校验。

**Pac Com Solution** | 全栈开发实习生 | 2021.06–2022.01

- 参与 Laravel/Vue.js POS 系统功能开发与缺陷修复，涉及后端逻辑及前端页面。

## 科研经历

**基于上下文与角色关系的职场对话隐含意图理解**  
*硕士论文，国立清华大学 | NLP · 图学习 · 知识图谱 · LLM*

- 面向职场对话隐含意图识别，建模上下文及说话者-听者角色关系。
- 将说话者/听者状态编码为对话图，并分别检索角色与上下文知识，作为 Llama 3.1-8B 的辅助信息。
- 在 400 条仅提供目标话语的样本上进行评测；结合角色与上下文知识后，语义 F1 由 0.644 提升至 0.682。

## 项目经历

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Qwen3.5-9B · QLoRA · 工具调用 · Agent 评测*

- 基于 Qwen3.5-9B 构建工具调用 Agent，支持搜索、文件读取与 Python 执行。
- 基于失败轨迹构造纠错样本进行 QLoRA 微调，200 个评测任务成功率由 34.5% 提升至 62.0%。
- GAIA100 准确率由 9% 提升至 18%；错误分析显示，过度搜索仍是主要失败原因。

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*BM25 · 向量检索 · RRF · 检索评测*

- 对比 BM25、向量检索及 RRF 混合检索方案，在 5,189 篇文档上评测检索效果。
- 融合 BM25 与向量检索后，在 64 条查询上 Recall@10 由 0.734 提升至 0.763，MRR@20 由 0.679 提升至 0.742。

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Qwen3.5-9B · Schema Grounding · SQL 校验 · 自动修复*

- 基于数据库 Schema 生成 SQL，并加入确定性校验与自动修复机制。
- 在 100 条 BIRD DEV 查询上，正确率由 33% 提升至 39%，修复 6 条原本错误的查询，未引入回退。

## 专业技能

**LLM / NLP：** RAG、混合检索、知识图谱、工具调用 Agent、PEFT / QLoRA、LLM 评测  
**机器学习：** Transformers、图神经网络、Embedding 模型  
**后端：** Python、FastAPI、PHP、Laravel、REST API、SQL、MySQL、SQLite  
**工具：** Linux、Git、pytest、llama.cpp、LangGraph  
**语言：** 中文（母语）、英语（流利）、马来语（中级）
