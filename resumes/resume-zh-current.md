# 高立恒

马来西亚籍 | +60 17-424 6282 | lihhanko526@gmail.com | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## 工作经历

**Kahap Inc** | 软件开发工程师 · 兼职 | 2022.08–2026.08

- 从零开发并上线反馈平台，覆盖意见提交、讨论、后台审核和通知等核心流程。
- 长期维护 Laravel/Vue.js 线上系统，处理队列、定时任务、数据库迁移和 Linux 服务器问题。
- 在后端接入 GPT-SoVITS，并加入发音与文本检查，完善语音生成流程。

**Pac Com Solution** | 全栈开发实习生 | 2021.06–2022.01

- 负责 Laravel/Vue.js POS 系统的功能开发和线上问题修复。

## 研究经历

**基于职场层级与情境脉络的隐含意图理解**  
*硕士论文，国立清华大学 | NLP · 图学习 · Role/Context KG · Llama 3.1-8B*

- 研究职场对话中会随上下文、说话者与听者角色变化的隐含意图，而不是只根据单句话判断。
- 将 LLM 提取的说话者/听者状态编码为 GCN/GAT 图表示，再通过 Role KG 与 Context KG 检索，为 Llama 3.1-8B 提供补充证据。
- 在 400 条 target-only 样本上，DualKG 的语义 F1 为 0.682，高于纯文本基线的 0.644，也高于 Prior KG、Role KG 和 Context KG。

## 项目经历

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Python · Qwen3.5-9B · QLoRA / PEFT · Transformers · llama.cpp*

- 开发可调用搜索、文件读取和 Python 的 Qwen Agent，并加入超时、重复调用拦截和运行追踪。
- 用失败案例整理纠错样本并做 QLoRA 微调，200 个固定任务的成功率从 34.5% 提升到 62.0%。
- GAIA100 准确率从 9% 提升到 18%；分析运行记录后，主要问题仍是过度搜索。

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*Python · BM25 · Qwen Embeddings · RRF · FastAPI*

- 将 BM25 与 Qwen 向量检索通过 RRF 融合，并保留每条结果的排名来源，方便检查检索行为。
- 在 5,189 篇文档和 64 条查询上，Recall@10 从 0.734 提升到 0.763，MRR@20 从 0.679 提升到 0.742。

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Python · FastAPI · LangGraph · SQLite · Qwen3.5-9B · pytest*

- 开发 NL-to-SQL 流程，包含 Schema Grounding、确定性校验、有限次数修复和只读执行。
- FastAPI、CLI、Streamlit 与评测共用同一服务层，避免不同入口出现行为偏差。
- 在 100 条 BIRD DEV 查询上，正确率从 33% 提升到 39%，修复 6 条原本错误的查询，没有引入回退。

## 教育背景

**国立清华大学（NTHU）** | 信息系统与应用硕士 | GPA 4.09/4.3 | 2026.06  
**中华大学** | 计算机科学与信息工程学士 | GPA 3.9/4.0 | 2024.06

## 专业技能

**AI / LLM：** Agent 与工具调用；RAG / 混合检索；模型评测；PEFT / QLoRA；Transformers；LangGraph；llama.cpp  
**后端：** Python；FastAPI；PHP；Laravel；REST API；SQL；MySQL；SQLite  
**Web / 工具：** JavaScript；Vue.js；Linux；Git；pytest  
**语言：** 中文（母语）；英语（流利）；马来语（中级）
