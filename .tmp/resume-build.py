from pathlib import Path
from weasyprint import HTML

OUT = Path("resumes")
OUT.mkdir(exist_ok=True)
TMP = Path("/tmp")

base_css = r"""
@page { size: A4; margin: 10.5mm 12mm 9.5mm 12mm; }
* { box-sizing: border-box; }
body { font-family: "Liberation Sans", Arial, sans-serif; color:#171717; font-size:9.25pt; line-height:1.25; margin:0; }
a { color:inherit; text-decoration:none; }
.header { text-align:center; margin-bottom:3.2mm; }
.name { font-size:20.2pt; font-weight:800; letter-spacing:.25pt; margin:0 0 1.2mm; }
.tagline { font-size:10.8pt; font-weight:700; color:#17365d; margin-bottom:1mm; }
.contact { font-size:8.5pt; color:#5a6470; }
.rule { border-top:1.2pt solid #17365d; margin-top:1.8mm; }
.summary { margin:2.3mm 0 2.1mm; font-size:9.15pt; line-height:1.28; }
.section { margin-top:1.65mm; }
.section-title { color:#17365d; font-size:10.5pt; font-weight:800; letter-spacing:.18pt; text-transform:uppercase; padding-bottom:.55mm; border-bottom:.65pt solid #9ca9b7; margin-bottom:1.35mm; }
.item { margin:0 0 1.25mm; break-inside:avoid; }
.row { display:flex; justify-content:space-between; align-items:baseline; gap:8mm; }
.left { min-width:0; }
.item-title { font-weight:800; font-size:9.45pt; }
.role { font-style:italic; color:#66717f; font-weight:500; }
.date { white-space:nowrap; color:#66717f; font-size:8.35pt; }
.tech { font-style:italic; color:#66717f; font-size:8.25pt; font-weight:500; }
ul { margin:.45mm 0 0 4.3mm; padding:0; }
li { margin:0 0 .48mm 0; padding-left:.25mm; }
.skills { margin-top:.1mm; }
.skill-line { margin:0 0 .55mm; }
.skill-label { font-weight:800; }
.edu-meta { color:#66717f; margin-top:.35mm; font-size:8.45pt; }
"""
cn_css = base_css + r"""
body { font-family:"Noto Sans CJK SC","Noto Sans CJK TC","Noto Sans CJK",sans-serif; font-size:9pt; line-height:1.28; }
.name { font-family:"Noto Sans CJK SC","Noto Sans CJK",sans-serif; font-size:20.5pt; }
.tagline { font-size:10.9pt; }
.summary { font-size:9.1pt; line-height:1.32; }
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
body += '<div class="summary">Software engineer with production backend/full-stack experience and hands-on work building and evaluating LLM systems across Text-to-SQL, hybrid retrieval, and tool-using multimodal agents.</div>'
body += section("Experience",
    exp("Kahap Inc","Software Developer (Part-time)","Aug 2022 - Aug 2026",[
        "Primary developer for a production feedback platform, owning submission workflows, automated notifications, and administrative features from implementation through production support.",
        "Maintained and extended Laravel/Vue.js production applications, shipping business features and debugging application and database issues.",
        "Handled deployments and server operations, including upgrades, Laravel queues/workers, SSL maintenance, and database troubleshooting.",
    ]) +
    exp("Pac Com Solution","Full-Stack Developer Intern","Jun 2021 - Jan 2022",[
        "Developed and maintained full-stack features for production POS applications using Laravel and Vue.js.",
    ])
)
body += section("Projects",
    project("Semantic Text-to-SQL Agent","https://github.com/kolihhan/semantic-text2sql-agent","Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite",[
        "Built a local Text-to-SQL service with deterministic SQL verification, read-only execution, bounded repair, and one-pass clause-guided semantic review.",
        "On a frozen 100-query BIRD DEV run, guarded repair recovered 19 failed executions (63% → 82% execution success); official BIRD EX rose from 31% to 34%.",
    ]) +
    project("Local RAG Search","https://github.com/kolihhan/local-rag-search","Python · BM25 · Qwen Embeddings · RRF · FastAPI",[
        "Built a local hybrid retriever with BM25, Qwen dense retrieval, RRF fusion, and per-result rank provenance.",
        "On 64 Confluence-compatible queries over 5,189 documents, hybrid RRF reached 0.7630 Recall@10, 0.7418 MRR@20, and 0.8438 Hit@10.",
    ]) +
    project("Hermes Video Tutor","https://github.com/kolihhan/hermes-video-tutor","Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal",[
        "Built a local video-QA agent that uses transcript evidence first and inspects frames/clips only when needed, with visible tool traces and abstention.",
        "On a frozen 12-question self-authored paired fixture, multimodal tools raised visual-required full pass from 0% to 66.7%, with no unnecessary visual calls on transcript-answerable cases.",
    ])
)
body += section("Skills", '<div class="skills"><div class="skill-line"><span class="skill-label">AI / LLM:</span> LLM Agents, RAG, Tool Calling, Retrieval &amp; LLM Evaluation, Embeddings, LangGraph</div><div class="skill-line"><span class="skill-label">Programming / Backend:</span> Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js, React</div><div class="skill-line"><span class="skill-label">Cloud / Data:</span> AWS, MySQL, Redis, SQLite, Linux</div><div class="skill-line"><span class="skill-label">Other:</span> Java, C/C++, Git, pytest &nbsp;|&nbsp; Chinese (Native), English (Fluent), Malay (Intermediate)</div></div>')
body += section("Education",
    edu("National Tsing Hua University","M.S., Information Systems &amp; Applications","2024 - 2026",'GPA 4.09/4.3 &nbsp; | &nbsp; Taiwan &nbsp; | &nbsp; Thesis: <i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i>') +
    edu("Chung Hua University","B.S., Computer Science &amp; Information Engineering","2022 - 2024","GPA 3.9/4.0 &nbsp; | &nbsp; Taiwan")
)
write_pdf("resume-en-current.pdf", base_css, body, "en")

# Chinese
body = header("高立恒", "软件工程师｜AI 应用 / 后端开发")
body += '<div class="summary">国立清华大学资讯系统与应用研究所理学硕士，具备生产环境后端/全栈开发经验，并完成 Text-to-SQL、混合检索与多模态工具调用等可评测 AI 系统。</div>'
body += section("工作经历",
    exp("Kahap Inc","软件开发工程师（兼职）","2022.08 - 2026.08",[
        "作为主要开发者负责生产环境反馈平台，覆盖反馈提交、自动通知与后台管理，并持续参与上线后的维护与问题排查。",
        "维护并扩展 Laravel / Vue.js 生产应用，持续交付业务功能，并排查应用层与数据库问题。",
        "负责部署与服务器运维，包括服务器升级、Laravel Queue / Worker、SSL 维护及数据库故障排查。",
    ]) +
    exp("Pac Com Solution","全栈开发实习生","2021.06 - 2022.01",[
        "使用 Laravel / Vue.js 开发并维护生产环境 POS 应用的全栈功能。",
    ])
)
body += section("项目经历",
    project("Semantic Text-to-SQL Agent","https://github.com/kolihhan/semantic-text2sql-agent","Python · LangGraph · Qwen3.5 4B · FastAPI · SQLite",[
        "构建本地 Text-to-SQL 服务，包含确定性 SQL 校验、只读执行、有上限修复，以及一次性 Clause-Guided 语义复核。",
        "在冻结的 100 条 BIRD DEV 查询上，受控修复恢复 19 条原本执行失败的查询（执行成功率 63% → 82%）；官方 BIRD EX 从 31% 提升至 34%。",
    ]) +
    project("Local RAG Search","https://github.com/kolihhan/local-rag-search","Python · BM25 · Qwen Embeddings · RRF · FastAPI",[
        "构建本地混合检索系统，组合 BM25、Qwen 稠密检索与 RRF，并保留逐结果排名来源。",
        "在 64 条 Confluence-compatible 查询、5,189 份文档上，混合 RRF 达到 0.7630 Recall@10、0.7418 MRR@20、0.8438 Hit@10。",
    ]) +
    project("Hermes Video Tutor","https://github.com/kolihhan/hermes-video-tutor","Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal",[
        "构建本地视频 QA Agent：优先使用字幕证据，仅在需要时检查帧/视频片段，并保留工具轨迹与证据不足时的拒答。",
        "在冻结的 12 题自建配对测试中，多模态工具将视觉问题完整通过率从 0% 提升至 66.7%，文本可回答问题未产生不必要的视觉调用。",
    ])
)
body += section("专业技能", '<div class="skills"><div class="skill-line"><span class="skill-label">AI / LLM：</span>LLM Agents、RAG、Tool Calling、Retrieval / LLM Evaluation、Embeddings、LangGraph</div><div class="skill-line"><span class="skill-label">编程 / 后端：</span>Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js、React</div><div class="skill-line"><span class="skill-label">云与数据：</span>AWS、MySQL、Redis、SQLite、Linux</div><div class="skill-line"><span class="skill-label">其他：</span>Java、C/C++、Git、pytest &nbsp;|&nbsp; 中文（母语）、英语（流利）、马来语（中等）</div></div>')
body += section("教育背景",
    edu("国立清华大学（台湾）","资讯系统与应用研究所 理学硕士","2024.09 - 2026.06",'GPA：4.09/4.3 &nbsp; | &nbsp; 硕士论文：<i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i>') +
    edu("中华大学（台湾）","资讯工程学系 学士","2022.09 - 2024.06","GPA：3.9/4.0")
)
write_pdf("resume-cn-current.pdf", cn_css, body, "zh-CN")
