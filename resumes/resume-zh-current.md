# 高立恒

马来西亚籍 | [+60 17-424 6282](tel:+60174246282) | [lihhanko526@gmail.com](mailto:lihhanko526@gmail.com) | [GitHub](https://github.com/kolihhan) | [LinkedIn](https://www.linkedin.com/in/ko-lih-han-748993241)

## 教育背景

**国立清华大学（NTHU）** | 信息系统与应用硕士 | **GPA 4.09/4.3** | 2026.06  
**中华大学** | 计算机科学与信息工程学士 | GPA 3.9/4.0 | 2024.06

## 工作经历

**Kahap Inc** | 软件开发工程师（兼职） | 2022.08–2026.08

- 使用 **Laravel、Vue.js 与 MySQL** 开发并上线反馈平台，覆盖意见提交、讨论、后台审核、通知与定时任务，并持续迭代生产功能。
- 负责应用发布与后台任务运行，处理部署、队列 Worker、定时任务、数据库迁移及线上异常排查。
- 维护 **Linux / Nginx** 运行环境，处理 SSL 续期、服务器迁移与数据库故障，并跟进队列和定时任务的运行状态。
- 在语音生成流程中接入 **GPT-SoVITS**，并加入发音与文本校验，减少异常输入进入合成流程。

**Pac Com Solution** | 全栈开发实习生 | 2021.06–2022.01

- 参与 Laravel/Vue.js POS 系统的功能开发与问题修复，在既有代码库中完成后端业务逻辑与前端页面实现。

## 科研经历

**职场对话隐含意图理解：上下文与角色关系建模**  
*硕士论文，国立清华大学 | NLP · 图学习 · 知识图谱 · LLM*

- 研究同一句话在不同上下文和职场角色关系下为何会表达不同意图，重点关注角色权力与对话状态对意图判断的影响。
- 构建有序对话状态图，使用 **GCN/GAT** 编码说话者与听者的状态、关系及上下文信息。
- 从 **Role KG 与 Context KG** 检索角色和情境证据，并将两类知识融合后提供给 Llama 3.1-8B 进行隐含意图判断。
- 对比纯文本 Baseline、Prior KG、Role KG、Context KG 与 DualKG；在 400 条仅给出目标话语的样本上，DualKG 语义 **F1 从 0.644 提升至 0.682**。

## 项目经历

**[Small-Agent QLoRA](https://github.com/kolihhan/small-agent-qlora)**  
*Qwen3.5-9B · QLoRA / SFT · Tool Use · Agent Evaluation*

- 构建 Qwen Agent，支持搜索、文件读取和 Python 执行，并加入超时、重复调用拦截与运行轨迹记录。
- 根据失败轨迹整理纠错样本进行 **QLoRA/SFT**，在 200 个固定评测任务上将成功率从 **34.5% 提升至 62.0%**。
- 在 GAIA100 外部评测中，准确率从 **9% 提升至 18%**；轨迹分析显示，过度搜索仍是主要失败原因。

**[Hybrid Retrieval Evaluation](https://github.com/kolihhan/local-rag-search)**  
*BM25 · Qwen Dense Retrieval · RRF · Retrieval Evaluation*

- 实现 **BM25、Qwen Dense Retrieval 与 RRF 融合**，保留各路排名与融合结果，便于分析不同检索器对单条结果的贡献。
- 在 5,189 篇文档、64 条查询上进行检索评测，**Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742**。

**[Semantic Text-to-SQL](https://github.com/kolihhan/semantic-text2sql-agent)**  
*Qwen3.5-9B · Schema Grounding · SQL Verification · Bounded Repair*

- 构建 Text-to-SQL 系统，以问题和数据库 Schema 生成 SQL，并串接确定性 verifier、有限次数修复与只读执行流程。
- verifier 检查单语句、SQL-only、只读约束及执行前编译验证；失败时最多修复 **2 次**，同时记录执行结果与 trace。
- 在 100 条 BIRD DEV 查询上，正确率从 **33% 提升至 39%**，执行成功率从 **75% 提升至 90%**；修复 6 条错误查询，且未出现原本正确的查询被改错。

## 专业技能

**LLM / NLP：** RAG、混合检索、知识图谱、Tool-using Agent、PEFT / QLoRA、LLM 评测  
**机器学习：** Transformers、图神经网络、Embedding / Dense Retrieval  
**工程开发：** Python、FastAPI、PHP、Laravel、Vue.js、REST API、SQL、MySQL、SQLite  
**工具：** Linux、Git、pytest、llama.cpp、LangGraph  
**语言：** 中文（母语）、英语（流利）、马来语（中级）