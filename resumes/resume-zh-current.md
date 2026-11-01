# 高立恒

马来西亚籍 | [+60 17-424 6282](tel:+60174246282) | [lihhanko526@gmail.com](mailto:lihhanko526@gmail.com) | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## 工作经历

**Kahap Inc** | 软件开发工程师 · 兼职 | 2022.08–2026.08

- 开发并上线 Laravel/Vue.js 反馈平台核心功能，涵盖意见提交、讨论、后台审核、通知和定时任务。
- 维护线上系统的部署与运行，处理队列 Worker、定时任务、数据库迁移、SSL 更新和 Linux 服务器故障。
- 将 GPT-SoVITS 接入后端语音流程，并在合成前加入发音与文本校验。

**Pac Com Solution** | 全栈开发实习生 | 2021.06–2022.01

- 开发并维护 Laravel/Vue.js POS 系统功能，覆盖后端逻辑和前端界面。

## 研究经历

**基于上下文与角色关系的职场对话隐含意图理解**  
*硕士论文，国立清华大学 | NLP · 图学习 · 知识图谱 · LLM*

- 建模职场对话中的上下文与说话者/听者角色关系，用于判断话语的隐含意图。
- 将说话者和听者状态表示为对话图，并检索与角色和上下文相关的知识，辅助 Llama 3.1-8B 判断意图。
- 在 400 条仅提供目标话语的样本上评测；结合角色与上下文知识后，语义 F1 从 0.644 提升至 0.682。

## 项目经历

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Qwen3.5-9B · QLoRA · 工具调用 · Agent 评测*

- 构建可搜索、读取文件并执行 Python 的 Qwen Agent，用于完成多步骤任务。
- 将 Agent 失败案例整理为训练样本并进行 QLoRA 微调，在 200 个评测任务上成功率从 34.5% 提升至 62.0%。
- GAIA100 准确率从 9% 提升至 18%；错误分析显示，过度搜索仍是主要失败原因。

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*BM25 · 向量检索 · RRF · 检索评测*

- 比较关键词检索、向量检索与混合检索在 5,189 篇文档中的检索效果。
- 融合 BM25 与向量检索后，在 64 条查询上 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Qwen3.5-9B · Schema Grounding · SQL 校验 · 自动修复*

- 构建 Text-to-SQL 系统，利用数据库 Schema 生成 SQL，并在执行前进行校验和自动修复。
- 在 100 条 BIRD DEV 查询上，正确率从 33% 提升至 39%，修复 6 条原本错误的查询，未引入回退。

## 教育背景

**国立清华大学（NTHU）**  
信息系统与应用硕士 | GPA 4.09/4.3 | 2026.06

**中华大学**  
计算机科学与信息工程学士 | GPA 3.9/4.0 | 2024.06

## 专业技能

**LLM / NLP：** RAG、混合检索、知识图谱、工具调用 Agent、PEFT / QLoRA、LLM 评测  
**机器学习：** Transformers、图神经网络、Embedding 模型  
**后端：** Python、FastAPI、PHP、Laravel、REST API、SQL、MySQL、SQLite  
**工具：** Linux、Git、pytest、llama.cpp、LangGraph  
**语言：** 中文（母语）、英语（流利）、马来语（中级）
