from weasyprint import HTML

def li(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def exp(company, role, date, bullets):
    return f'<div class="item"><div class="row"><div class="left"><span class="item-title">{company}</span> &nbsp;|&nbsp; <span class="role">{role}</span></div><div class="date">{date}</div></div>{li(bullets)}</div>'

def project(name, url, tech, bullets):
    return f'<div class="item"><div><a class="item-title" href="{url}">{name}</a> &nbsp;|&nbsp; <span class="tech">{tech}</span></div>{li(bullets)}</div>'

def edu(name, degree, date, meta):
    return f'<div class="item"><div class="row"><div class="left"><span class="item-title">{name}</span> &nbsp;|&nbsp; <span class="role">{degree}</span></div><div class="date">{date}</div></div><div class="edu-meta">{meta}</div></div>'

def section(title, content):
    return f'<div class="section"><div class="section-title">{title}</div>{content}</div>'

def header(name, tagline):
    return f'<div class="header"><div class="name">{name}</div><div class="tagline">{tagline}</div><div class="contact">+60 17-424 6282 &nbsp; | &nbsp; <a href="mailto:lihhanko526@gmail.com">lihhanko526@gmail.com</a> &nbsp; | &nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div><div class="rule"></div></div>'

en_css = r'''
@page { size: A4; margin: 11.5mm 13mm 11.5mm 13mm; }
* { box-sizing: border-box; }
body { font-family: "Liberation Sans", Arial, sans-serif; color:#171717; font-size:10.4pt; line-height:1.36; margin:0; }
a { color:inherit; text-decoration:none; }
.header { text-align:center; margin-bottom:3.4mm; }
.name { font-size:21.2pt; font-weight:800; letter-spacing:.2pt; margin:0 0 1.8mm; }
.tagline { font-size:11.3pt; font-weight:700; color:#17365d; margin-bottom:1mm; }
.contact { font-size:9.0pt; color:#5a6470; }
.rule { border-top:1.15pt solid #17365d; margin-top:1.7mm; }
.summary { margin:2.6mm 0 2.5mm; font-size:10.0pt; line-height:1.36; }
.section { margin-top:2.3mm; }
.section-title { color:#17365d; font-size:11.1pt; font-weight:800; letter-spacing:.16pt; text-transform:uppercase; padding-bottom:.5mm; border-bottom:.65pt solid #9ca9b7; margin-bottom:1.7mm; }
.item { margin:0 0 1.8mm; break-inside:avoid; }
.row { display:flex; justify-content:space-between; align-items:baseline; gap:8mm; }
.left { min-width:0; }
.item-title { font-weight:800; font-size:10.0pt; }
.role { font-style:italic; color:#66717f; font-weight:500; }
.date { white-space:nowrap; color:#66717f; font-size:8.85pt; }
.tech { font-style:italic; color:#66717f; font-size:8.75pt; font-weight:500; }
ul { margin:.6mm 0 0 4.5mm; padding:0; }
li { margin:0 0 .78mm 0; padding-left:.25mm; }
.skills { margin-top:.05mm; }
.skill-line { margin:0 0 .72mm; }
.skill-label { font-weight:800; }
.edu-meta { color:#66717f; margin-top:.3mm; font-size:8.9pt; }
'''

cn_css = r'''
@page { size: A4; margin: 11.5mm 13mm 11.5mm 13mm; }
* { box-sizing: border-box; }
body { font-family:"Noto Sans CJK SC","Noto Sans CJK TC","Noto Sans CJK",sans-serif; color:#171717; font-size:10.8pt; line-height:1.42; margin:0; }
a { color:inherit; text-decoration:none; }
.header { text-align:center; margin-bottom:3.4mm; }
.name { font-family:"Noto Sans CJK SC","Noto Sans CJK",sans-serif; font-size:21.2pt; font-weight:800; letter-spacing:.2pt; margin:0 0 2.65mm; }
.tagline { font-size:11.3pt; font-weight:700; color:#17365d; margin-bottom:1mm; }
.contact { font-size:9.0pt; color:#5a6470; }
.rule { border-top:1.15pt solid #17365d; margin-top:1.7mm; }
.summary { margin:2.6mm 0 2.5mm; font-size:10.3pt; line-height:1.42; }
.section { margin-top:3.1mm; }
.section-title { color:#17365d; font-size:11.6pt; font-weight:800; letter-spacing:.16pt; padding-bottom:.5mm; border-bottom:.65pt solid #9ca9b7; margin-bottom:2.25mm; }
.item { margin:0 0 2.65mm; break-inside:avoid; }
.row { display:flex; justify-content:space-between; align-items:baseline; gap:8mm; }
.left { min-width:0; }
.item-title { font-weight:800; font-size:10.8pt; }
.role { color:#66717f; font-weight:500; }
.date { white-space:nowrap; color:#66717f; font-size:10.1pt; }
.tech { font-family:"Liberation Sans","Noto Sans CJK SC",sans-serif; font-style:italic; color:#66717f; font-size:9.35pt; font-weight:500; }
ul { margin:.6mm 0 0 4.5mm; padding:0; }
li { margin:0 0 1.15mm 0; padding-left:.25mm; }
.skills { margin-top:.05mm; }
.skill-line { margin:0 0 .72mm; }
.skill-label { font-weight:800; }
.edu-meta { color:#66717f; margin-top:.3mm; font-size:10.1pt; }
'''

en = header("KO LIH HAN", "Software Engineer | Applied AI &amp; LLM Systems")
en += '<div class="summary">Software engineer with production experience in Laravel/Vue.js and hands-on experience building LLM, retrieval, and multimodal AI systems in Python.</div>'
en += section("EXPERIENCE",
    exp("Kahap Inc","Software Developer (Part-time)","Aug 2022 - Aug 2026",[
        "Built and maintained a production feedback platform, including submission workflows, automated notifications, and admin tools.",
        "Developed Laravel/Vue.js features and debugged application and database issues in production.",
        "Handled deployments and server operations, including server upgrades, Laravel queues/workers, SSL renewal, and database troubleshooting.",
    ]) +
    exp("Pac Com Solution","Full-Stack Developer Intern","Jun 2021 - Jan 2022",[
        "Developed and maintained Laravel/Vue.js features for production POS applications.",
    ])
)
en += section("PROJECTS",
    project("Semantic Text-to-SQL","https://github.com/kolihhan/semantic-text2sql-agent","Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite",[
        "Built a local Text-to-SQL service with XiYanSQL 7B, schema grounding, SQL validation, read-only execution, and bounded repair.",
        "Evaluated XiYanSQL 7B on 100 BIRD questions, matching the expected execution result on 58, then used failure analysis to compare schema-linking approaches.",
    ]) +
    project("Local RAG Search","https://github.com/kolihhan/local-rag-search","Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI",[
        "Built a local hybrid search service combining BM25, Qwen3 embeddings, and RRF behind a FastAPI API.",
        "On 64 EnterpriseRAG-Bench queries over 5,189 documents, RRF outperformed BM25 on Recall@10 (0.763 vs 0.734) and MRR@20 (0.742 vs 0.679).",
    ]) +
    project("Hermes Video Tutor","https://github.com/kolihhan/hermes-video-tutor","Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal",[
        "Built a video-QA agent that answers from transcripts when possible and inspects frames or clips only when visual evidence is needed.",
        "Tested on 12 questions, adding visual tools improved overall pass rate from 16.7% to 50.0%, with 66.7% on visual questions.",
    ])
)
en += section("SKILLS", '<div class="skills"><div class="skill-line"><span class="skill-label">AI / LLM:</span> LLM Agents, RAG, Tool Calling, Retrieval, Evaluation, LangGraph</div><div class="skill-line"><span class="skill-label">Programming / Backend:</span> Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js, React</div><div class="skill-line"><span class="skill-label">Data / Infra:</span> AWS, MySQL, Redis, SQLite, Linux, Git, pytest</div><div class="skill-line"><span class="skill-label">Other:</span> Java, C/C++ &nbsp;|&nbsp; Chinese (Native), English (Fluent), Malay (Intermediate)</div></div>')
en += section("EDUCATION",
    edu("National Tsing Hua University","M.S., Information Systems &amp; Applications","Sep 2024 - Jun 2026",'GPA 4.09/4.3 &nbsp; | &nbsp; Taiwan &nbsp; | &nbsp; Thesis: <i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i>') +
    edu("Chung Hua University","B.S., Computer Science &amp; Information Engineering","Sep 2022 - Jun 2024","GPA 3.9/4.0 &nbsp; | &nbsp; Taiwan")
)

cn = header("高立恒", "软件工程师｜AI 应用 / 后端开发")
cn += '<div class="summary">具备 Laravel / Vue.js 生产系统开发经验，并使用 Python 开发过 Text-to-SQL、混合检索与多模态 Agent 项目。</div>'
cn += section("工作经历",
    exp("Kahap Inc","软件开发工程师（兼职）","2022.08 - 2026.08",[
        "开发并维护生产环境反馈平台，负责反馈提交、自动通知和后台管理等核心功能。",
        "持续开发 Laravel / Vue.js 业务功能，并排查生产环境中的应用与数据库问题。",
        "负责部署和服务器维护，包括服务器升级、Laravel Queue / Worker、SSL 续期与数据库故障排查。",
    ]) +
    exp("Pac Com Solution","全栈开发实习生","2021.06 - 2022.01",[
        "使用 Laravel / Vue.js 开发并维护生产环境 POS 应用功能。",
    ])
)
cn += section("项目经历",
    project("Semantic Text-to-SQL","https://github.com/kolihhan/semantic-text2sql-agent","Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite",[
        "构建本地 Text-to-SQL 服务，使用 XiYanSQL 7B，并加入 schema grounding、SQL 校验、只读执行和有限次数修复。",
        "在 100 条 BIRD 测试题中，XiYanSQL 7B 有 58 条执行结果与参考结果一致，并结合错误分析比较不同的 Schema Linking 方案。",
    ]) +
    project("Local RAG Search","https://github.com/kolihhan/local-rag-search","Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI",[
        "构建本地混合检索服务，将 BM25、Qwen3 Embedding 与 RRF 组合，并通过 FastAPI 提供查询接口。",
        "在 64 条 EnterpriseRAG-Bench 查询、5,189 份文档上，RRF 的 Recall@10 为 0.763（BM25 0.734），MRR@20 为 0.742（BM25 0.679）。",
    ]) +
    project("Hermes Video Tutor","https://github.com/kolihhan/hermes-video-tutor","Python · Hermes · Qwen3.5 4B · Tool Calling · Multimodal",[
        "构建视频问答 Agent：能用字幕回答时直接回答，只有在需要视觉信息时才检查画面或视频片段。",
        "在 12 题测试中，加入视觉工具后整体通过率从 16.7% 提升到 50.0%，视觉题通过率为 66.7%。",
    ])
)
cn += section("专业技能", '<div class="skills"><div class="skill-line"><span class="skill-label">AI / LLM：</span> LLM Agents、RAG、Tool Calling、Retrieval、Evaluation、LangGraph</div><div class="skill-line"><span class="skill-label">编程 / 后端：</span> Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js、React</div><div class="skill-line"><span class="skill-label">数据 / 基础设施：</span> AWS、MySQL、Redis、SQLite、Linux、Git、pytest</div><div class="skill-line"><span class="skill-label">其他：</span> Java、C/C++｜中文（母语）、英语（流利）、马来语（中等）</div></div>')
cn += section("教育背景",
    edu("国立清华大学（台湾）","资讯系统与应用研究所 理学硕士","2024.09 - 2026.06",'GPA：4.09/4.3 &nbsp; | &nbsp; 硕士论文：<i>Interpreting Implicit Intent through Workplace Hierarchies and Context</i>') +
    edu("中华大学（台湾）","资讯工程学系 学士","2022.09 - 2024.06","GPA：3.9/4.0")
)

def write(path, css, body, lang):
    html=f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
    HTML(string=html).write_pdf(path)

write("resumes/resume-en-current.pdf", en_css, en, "en")
write("resumes/resume-cn-current.pdf", cn_css, cn, "zh-CN")
