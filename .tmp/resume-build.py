from pathlib import Path
from weasyprint import HTML

OUT = Path("resumes")
OUT.mkdir(exist_ok=True)
TMP = Path("/tmp")

base_css = r"""
@page { size: A4; margin: 10.5mm 12mm 9.5mm 12mm; }
* { box-sizing: border-box; }
body { font-family: "Liberation Sans", Arial, sans-serif; color:#171717; font-size:9.65pt; line-height:1.29; margin:0; }
a { color:inherit; text-decoration:none; }
.header { text-align:center; margin-bottom:3.3mm; }
.name { font-size:20.2pt; font-weight:800; letter-spacing:.25pt; margin:0 0 1.2mm; }
.tagline { font-size:10.8pt; font-weight:700; color:#17365d; margin-bottom:1mm; }
.contact { font-size:8.5pt; color:#5a6470; }
.rule { border-top:1.2pt solid #17365d; margin-top:1.8mm; }
.summary { margin:2.5mm 0 2.3mm; font-size:9.65pt; line-height:1.31; }
.section { margin-top:1.85mm; }
.section-title { color:#17365d; font-size:10.5pt; font-weight:800; letter-spacing:.18pt; text-transform:uppercase; padding-bottom:.55mm; border-bottom:.65pt solid #9ca9b7; margin-bottom:1.45mm; }
.item { margin:0 0 1.4mm; break-inside:avoid; }
.row { display:flex; justify-content:space-between; align-items:baseline; gap:8mm; }
.left { min-width:0; }
.item-title { font-weight:800; font-size:9.45pt; }
.role { font-style:italic; color:#66717f; font-weight:500; }
.date { white-space:nowrap; color:#66717f; font-size:8.55pt; }
.tech { font-style:italic; color:#66717f; font-size:8.35pt; font-weight:500; }
ul { margin:.5mm 0 0 4.3mm; padding:0; }
li { margin:0 0 .58mm 0; padding-left:.25mm; }
.skills { margin-top:.1mm; }
.skill-line { margin:0 0 .55mm; }
.skill-label { font-weight:800; }
.edu-meta { color:#66717f; margin-top:.35mm; font-size:8.45pt; }
"""
cn_css = base_css + r"""
body { font-family:"Noto Sans CJK SC","Noto Sans CJK TC","Noto Sans CJK",sans-serif; font-size:9.55pt; line-height:1.31; }
.name { font-family:"Noto Sans CJK SC","Noto Sans CJK",sans-serif; font-size:20.5pt; }
.tagline { font-size:10.9pt; }
.summary { font-size:9.35pt; line-height:1.33; }
.section-title { font-size:10.6pt; }
.item-title { font-size:9.35pt; }
.tech { font-family:"Liberation Sans","Noto Sans CJK SC",sans-serif; }
"""

def page(css, body, lang):
    return f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'

def header(name, tagline):
    return f'<div class="header"><div class="name">{name}</div><div class="tagline">{tagline}</div><div class="contact">+60 17-424 6282 &nbsp; | &nbsp; <a href="mailto:lihhanko526@gmail.com">lihhanko526@gmail.com</a> &nbsp; | &nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div><div class="rule"></div></div>'

def section(title, content):
    return f'<div class="section"><div class="section-title">{title}</div>{content}</div>'

def exp(company, role, date, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f'<div class="item"><div class="row"><div class="left"><span class="item-title">{company}</span> &nbsp;|&nbsp; <span class="role">{role}</span></div><div class="date">{date}</div></div><ul>{lis}</ul></div>'

def project(name, url, tech, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f'<div class="item"><div><a class="item-title" href="{url}">{name}</a> &nbsp;|&nbsp; <span class="tech">{tech}</span></div><ul>{lis}</ul></div>'

def edu(name, degree, date, meta):
    return f'<div class="item"><div class="row"><div class="left"><span class="item-title">{name}</span> &nbsp;|&nbsp; <span class="role">{degree}</span></div><div class="date">{date}</div></div><div class="edu-meta">{meta}</div></div>'

def write_pdf(filename, css, body, lang):
    html = TMP / (filename + ".html")
    html.write_text(page(css, body, lang), encoding="utf-8")
    HTML(filename=str(html)).write_pdf(str(OUT / filename))

# English
body = header("KO LIH HAN", "Software Engineer | Applied AI &amp; LLM Systems")
body += '<div class="summary">Software engineer with production backend/full-stack experience and hands-on work building and evaluating AI systems across Text-to-SQL, hybrid retrieval, and multimodal tool use.</div>'
body += section("Experience",
    exp("Kahap Inc","Software Developer (Part-time)","Aug 2022 - Aug 2026",[
        "Primary developer for a production feedback platform, owning submission workflows, automated notifications, and administrative features from implementation through production support.",
        "Maintained and extended Laravel/Vue.js production applications, shipping business features and resolving application and database issues.",
        "Handled deployments and server operations, including server upgrades, Laravel queues/workers, SSL maintenance, and database troubleshooting.",
    ]) +
    exp("Pac Com Solution","Full-Stack Developer Intern","Jun 2021 - Jan 2022",[
        "Developed and maintained full-stack features for production POS applications using Laravel and Vue.js.",
    ])
)
body += section("Projects",
    project("Semantic Text-to-SQL","https://github.com/kolihhan/semantic-text2sql-agent","Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite",[
        "Built a local Text-to-SQL system with grounded schema context, deterministic SQL verification, read-only execution, and bounded repair.",
        "Evaluated lexical vs DGSL grounding with XiYanSQL 7B on a frozen 100-case BIRD slice; both reached 58/100 execution-set matches under the project-local scorer (7 gains / 7 regressions).",
    ]) +
    project("Local RAG Search","https://github.com/kolihhan/local-rag-search","Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI",[
        "Built a local hybrid retriever combining BM25 and Qwen dense retrieval with RRF fusion and per-result rank provenance.",
        "On 64 official Confluence-compatible EnterpriseRAG-Bench v1.0.0 queries over 5,189 documents, RRF improved Recall@10 from 0.7341 to 0.7630 and MRR@20 from 0.6792 to 0.7418 over BM25.",
    ]) +
    project("Hermes Video Tutor","https://github.com/kolihhan/hermes-video-tutor","Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal",[
        "Built a local video-QA agent that starts with transcript evidence and escalates to frame/clip inspection only when needed, with visible evidence and abstention.",
        "On a frozen 12-question self-authored paired fixture, multimodal mode improved overall full-pass from 16.7% to 50.0% and reached 66.7% on visual-required questions, with no unnecessary visual calls on transcript-answerable cases.",
    ])
)
body += section("Skills", '<div class="skills"><div class="skill-line"><span class="skill-label">AI / LLM:</span> LLM Agents, RAG, Tool Calling, Retrieval &amp; Evaluation, LangGraph</div><div class="skill-line"><span class="skill-label">Programming / Backend:</span> Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js, React</div><div class="skill-line"><span class="skill-label">Data / Infra:</span> AWS, MySQL, Redis, SQLite, Linux, Git, pytest</div><div class="skill-line"><span class="skill-label">Other:</span> Java, C/C++ &nbsp;|&nbsp; Chinese (Native), English (Fluent), Malay (Intermediate)</div></div>')
body += section("Education",
    edu("National Tsing Hua University","M.S., Information Systems &amp; Applications","Sep 2024 - Jun 2026",'GPA 4.09/4.3 &nbsp; | &nbsp; Taiwan &nbsp; | &nbsp; Thesis: <i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i>') +
    edu("Chung Hua University","B.S., Computer Science &amp; Information Engineering","Sep 2022 - Jun 2024","GPA 3.9/4.0 &nbsp; | &nbsp; Taiwan")
)
write_pdf("resume-en-current.pdf", base_css, body, "en")

# Chinese
body = header("高立恒", "软件工程师｜AI 应用 / 后端开发")
body += '<div class="summary">具备生产环境后端/全栈开发经验，能够构建并评测 Text-to-SQL、混合检索与多模态工具调用等 AI 系统。</div>'
body += section("工作经历",
    exp("Kahap Inc","软件开发工程师（兼职）","2022.08 - 2026.08",[
        "作为主要开发者负责生产环境反馈平台，覆盖提交流程、自动通知与后台管理，从功能实现持续参与上线维护与问题排查。",
        "维护并扩展 Laravel / Vue.js 生产应用，持续交付业务功能，并处理应用层与数据库问题。",
        "负责部署与服务器运维，包括服务器升级、Laravel Queue / Worker、SSL 维护及数据库故障排查。",
    ]) +
    exp("Pac Com Solution","全栈开发实习生","2021.06 - 2022.01",[
        "使用 Laravel / Vue.js 开发并维护生产环境 POS 应用的全栈功能。",
    ])
)
body += section("项目经历",
    project("Semantic Text-to-SQL","https://github.com/kolihhan/semantic-text2sql-agent","Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite",[
        "构建本地 Text-to-SQL 系统，包含 schema grounding、确定性 SQL 校验、只读执行与有上限修复。",
        "在冻结的 100 条 BIRD 样本上，对 XiYanSQL 7B 的 lexical 与 DGSL grounding 进行对照；两者在项目内执行集匹配评分下均为 58/100（7 条修正 / 7 条回退）。",
    ]) +
    project("Local RAG Search","https://github.com/kolihhan/local-rag-search","Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI",[
        "构建本地混合检索系统，组合 BM25、Qwen 稠密检索与 RRF，并保留逐结果排名来源。",
        "在 EnterpriseRAG-Bench v1.0.0 的 64 条官方 Confluence-compatible 查询、5,189 份文档上，RRF 相比 BM25 将 Recall@10 从 0.7341 提升至 0.7630，MRR@20 从 0.6792 提升至 0.7418。",
    ]) +
    project("Hermes Video Tutor","https://github.com/kolihhan/hermes-video-tutor","Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal",[
        "构建本地视频 QA Agent：优先使用字幕证据，仅在需要时检查帧/视频片段，并保留可见证据与证据不足时的拒答。",
        "在冻结的 12 题自建配对测试中，多模态模式将整体完整通过率从 16.7% 提升至 50.0%，视觉问题达到 66.7%，且文本可回答问题未产生不必要的视觉调用。",
    ])
)
body += section("专业技能", '<div class="skills"><div class="skill-line"><span class="skill-label">AI / LLM：</span>LLM Agents、RAG、Tool Calling、Retrieval / Evaluation、LangGraph</div><div class="skill-line"><span class="skill-label">编程 / 后端：</span>Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js、React</div><div class="skill-line"><span class="skill-label">数据 / 基础设施：</span>AWS、MySQL、Redis、SQLite、Linux、Git、pytest</div><div class="skill-line"><span class="skill-label">其他：</span>Java、C/C++ &nbsp;|&nbsp; 中文（母语）、英语（流利）、马来语（中等）</div></div>')
body += section("教育背景",
    edu("国立清华大学（台湾）","资讯系统与应用研究所 理学硕士","2024.09 - 2026.06",'GPA：4.09/4.3 &nbsp; | &nbsp; 硕士论文：<i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i>') +
    edu("中华大学（台湾）","资讯工程学系 学士","2022.09 - 2024.06","GPA：3.9/4.0")
)
write_pdf("resume-cn-current.pdf", cn_css, body, "zh-CN")
