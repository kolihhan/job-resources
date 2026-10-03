from pathlib import Path

OUT = Path(".tmp/resume-build")
OUT.mkdir(parents=True, exist_ok=True)

BASE_CSS = r"""
@page { size: A4; margin: 10.5mm 13mm 9.5mm 13mm; }
* { box-sizing: border-box; }
body { margin: 0; color: #111827; font-family: "Noto Sans", Arial, sans-serif; font-size: 9.1pt; line-height: 1.30; }
body.cn { font-family: "Noto Sans CJK SC", "Noto Sans", Arial, sans-serif; }
a { color: inherit; text-decoration: none; }
.header { text-align: center; margin-bottom: 4.2px; }
.name { font-size: 21.5pt; letter-spacing: .65px; font-weight: 700; line-height: 1.0; margin: 0 0 3px; }
.headline { color: #173a63; font-weight: 700; font-size: 10.0pt; margin-bottom: 3.2px; }
.contact { font-size: 8.35pt; color: #374151; }
.summary { margin: 5px 0 5.8px; font-size: 8.85pt; line-height: 1.32; }
.section { margin-top: 4.6px; }
.section-title { color: #173a63; font-size: 10.1pt; font-weight: 800; letter-spacing: .35px; border-bottom: 1.25px solid #173a63; padding-bottom: 1.1px; margin-bottom: 3.4px; }
.entry { margin-bottom: 3.0px; page-break-inside: avoid; }
.entry-head { display: flex; justify-content: space-between; gap: 8px; align-items: baseline; }
.entry-title { font-weight: 700; font-size: 9.15pt; }
.entry-date { white-space: nowrap; font-size: 8.35pt; color: #374151; font-weight: 600; }
.tech { font-size: 8.05pt; color: #374151; margin-top: .5px; margin-bottom: .7px; }
ul { margin: 1.1px 0 0 14px; padding: 0; }
li { margin: 0 0 1.0px 0; padding-left: .2px; }
.skills { font-size: 8.65pt; line-height: 1.32; }
.skill-row { margin-bottom: 1.2px; }
.label { font-weight: 700; }
.edu-meta { font-size: 8.35pt; color: #374151; margin-top: .6px; }
.project-link { font-weight: 700; color: #111827; }
.project-link::after { content: " ↗"; font-size: 6.8pt; color: #173a63; }
"""

EN = f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="header">
  <div class="name">KO LIH HAN</div>
  <div class="headline">Software Engineer | Applied AI &amp; LLM Systems</div>
  <div class="contact">+60 17-424 6282 &nbsp;|&nbsp; lihhanko526@gmail.com &nbsp;|&nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div>
</div>
<div class="summary">Software engineer with production backend/full-stack experience and hands-on work building and evaluating LLM systems across Text-to-SQL, hybrid retrieval, and multimodal tool use.</div>
<div class="section"><div class="section-title">EXPERIENCE</div>
<div class="entry"><div class="entry-head"><div class="entry-title">Kahap Inc | Software Developer (Part-time)</div><div class="entry-date">Aug 2022 – Aug 2026</div></div><ul>
<li>Primary developer for a production feedback platform, owning submission workflows, automated notifications, and administrative features from implementation through production support.</li>
<li>Maintained and extended Laravel/Vue.js production applications, shipping business features and debugging application and database issues.</li>
<li>Handled deployments and server operations, including upgrades, Laravel queues/workers, SSL maintenance, and database troubleshooting.</li></ul></div>
<div class="entry"><div class="entry-head"><div class="entry-title">Pac Com Solution | Full-Stack Developer Intern</div><div class="entry-date">Jun 2021 – Jan 2022</div></div><ul><li>Developed and maintained full-stack features for production POS applications using Laravel and Vue.js.</li></ul></div>
</div>
<div class="section"><div class="section-title">PROJECTS</div>
<div class="entry"><div class="entry-title"><a class="project-link" href="https://github.com/kolihhan/semantic-text2sql-agent">Semantic Text-to-SQL Agent</a></div><div class="tech">Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite</div><ul>
<li>Built a local Text-to-SQL service with deterministic SQL verification, read-only execution, bounded repair, and one-pass clause-guided semantic revision.</li>
<li>On a frozen 100-query BIRD DEV run, guarded execution raised execution success from 63% to 82%; official BIRD EX moved from 31% to 34%, separating execution reliability from semantic correctness.</li></ul></div>
<div class="entry"><div class="entry-title"><a class="project-link" href="https://github.com/kolihhan/local-rag-search">Local RAG Search</a></div><div class="tech">Python · BM25 · Qwen Embeddings · RRF · FastAPI</div><ul><li>Benchmarked BM25, Qwen dense retrieval, and RRF on 64 official Confluence-compatible queries over 5,189 documents; hybrid reached 0.7630 Recall@10, 0.7418 MRR@20, and 0.8438 Hit@10 with per-result rank provenance.</li></ul></div>
<div class="entry"><div class="entry-title"><a class="project-link" href="https://github.com/kolihhan/hermes-video-tutor">Hermes Video Tutor</a></div><div class="tech">Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal</div><ul><li>Built a local multimodal video-QA agent that starts with transcript evidence and escalates to frame/clip inspection only when needed; on a frozen 12-question self-authored paired fixture, visual-required full pass reached 66.7% with no unnecessary visual-tool calls on transcript-answerable cases.</li></ul></div>
</div>
<div class="section"><div class="section-title">SKILLS</div><div class="skills">
<div class="skill-row"><span class="label">AI / LLM:</span> LLM Agents, RAG, Tool Calling, Retrieval &amp; LLM Evaluation, Embeddings, LangGraph</div>
<div class="skill-row"><span class="label">Programming / Backend:</span> Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js, React</div>
<div class="skill-row"><span class="label">Cloud / Data:</span> AWS, MySQL, Redis, SQLite, Linux</div>
<div class="skill-row"><span class="label">Other:</span> Java, C/C++, Git, pytest &nbsp;|&nbsp; Chinese (Native), English (Fluent), Malay (Intermediate)</div></div></div>
<div class="section"><div class="section-title">EDUCATION</div>
<div class="entry"><div class="entry-head"><div class="entry-title">National Tsing Hua University | M.S., Information Systems &amp; Applications</div><div class="entry-date">2024 – 2026</div></div><div class="edu-meta">GPA 4.09/4.3 | Taiwan | Thesis: <i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i></div></div>
<div class="entry"><div class="entry-head"><div class="entry-title">Chung Hua University | B.S., Computer Science &amp; Information Engineering</div><div class="entry-date">2022 – 2024</div></div><div class="edu-meta">GPA 3.9/4.0 | Taiwan</div></div>
</div></body></html>"""

CN = f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body class="cn">
<div class="header"><div class="name">高立恒</div><div class="headline">大模型应用开发工程师 / AI 应用工程师 / 后端开发工程师</div><div class="contact">+60 17-424 6282 &nbsp;|&nbsp; lihhanko526@gmail.com &nbsp;|&nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div></div>
<div class="summary">国立清华大学资讯系统与应用研究所理学硕士，具备生产系统后端/全栈开发经验，并完成 Text-to-SQL、混合检索和多模态工具调用等可评测 AI 应用系统。</div>
<div class="section"><div class="section-title">工作经历</div>
<div class="entry"><div class="entry-head"><div class="entry-title">Kahap Inc | 软件开发工程师（兼职）</div><div class="entry-date">2022.08 – 2026.08</div></div><ul>
<li>作为主要开发者负责生产环境反馈平台，覆盖反馈提交、自动通知与后台管理，并持续参与上线后的维护与问题排查。</li>
<li>维护并扩展 Laravel / Vue.js 生产应用，持续交付业务功能，并排查应用层与数据库问题。</li>
<li>负责部署与服务器运维，包括服务器升级、Laravel Queue / Worker、SSL 维护及数据库故障排查。</li></ul></div>
<div class="entry"><div class="entry-head"><div class="entry-title">Pac Com Solution | 全栈开发实习生</div><div class="entry-date">2021.06 – 2022.01</div></div><ul><li>使用 Laravel / Vue.js 开发并维护生产环境 POS 应用的全栈功能。</li></ul></div></div>
<div class="section"><div class="section-title">项目经历</div>
<div class="entry"><div class="entry-title"><a class="project-link" href="https://github.com/kolihhan/semantic-text2sql-agent">Semantic Text-to-SQL Agent</a></div><div class="tech">Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite</div><ul>
<li>构建本地 Text-to-SQL 服务，包含确定性 SQL 校验、SQLite 只读执行、有上限修复，以及一次性 Clause-Guided Semantic Revision。</li>
<li>在冻结的 100 条 BIRD DEV 查询上，受控路径将执行成功率从 63% 提升至 82%，官方 BIRD EX 从 31% 提升至 34%；明确区分执行可靠性与语义正确性。</li></ul></div>
<div class="entry"><div class="entry-title"><a class="project-link" href="https://github.com/kolihhan/local-rag-search">Local RAG Search</a></div><div class="tech">Python · BM25 · Qwen Embeddings · RRF · FastAPI</div><ul><li>在 64 条官方 Confluence-compatible 查询、5,189 份文档上评测 BM25、Qwen 稠密检索与 RRF；混合检索达到 0.7630 Recall@10、0.7418 MRR@20、0.8438 Hit@10，并保留逐结果排名来源。</li></ul></div>
<div class="entry"><div class="entry-title"><a class="project-link" href="https://github.com/kolihhan/hermes-video-tutor">Hermes Video Tutor</a></div><div class="tech">Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal</div><ul><li>构建本地多模态视频 QA Agent：优先使用字幕证据，仅在需要时检查帧/视频片段；在冻结的 12 题自建配对测试中，视觉问题完整通过率为 66.7%，且文本可回答问题未产生不必要的视觉工具调用。</li></ul></div></div>
<div class="section"><div class="section-title">专业技能</div><div class="skills">
<div class="skill-row"><span class="label">AI / LLM：</span> LLM Agents、RAG、Tool Calling、Retrieval / LLM Evaluation、Embeddings、LangGraph</div>
<div class="skill-row"><span class="label">编程 / 后端：</span> Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js、React</div>
<div class="skill-row"><span class="label">云与数据：</span> AWS、MySQL、Redis、SQLite、Linux</div>
<div class="skill-row"><span class="label">其他：</span> Java、C/C++、Git、pytest｜中文（母语）、英语（流利）、马来语（中等）</div></div></div>
<div class="section"><div class="section-title">教育背景</div>
<div class="entry"><div class="entry-head"><div class="entry-title">国立清华大学（台湾） | 资讯系统与应用研究所 理学硕士</div><div class="entry-date">2024.09 – 2026.06</div></div><div class="edu-meta">GPA：4.09/4.3｜硕士论文：<i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i></div></div>
<div class="entry"><div class="entry-head"><div class="entry-title">中华大学（台湾） | 资讯工程学系 学士</div><div class="entry-date">2022.09 – 2024.06</div></div><div class="edu-meta">GPA：3.9/4.0</div></div>
</div></body></html>"""

(OUT / "resume-en-current.html").write_text(EN, encoding="utf-8")
(OUT / "resume-cn-current.html").write_text(CN, encoding="utf-8")
