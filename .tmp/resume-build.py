from weasyprint import HTML
from pathlib import Path

OUT=Path("resumes")

header='''<div class="header"><div class="name">{name}</div><div class="tagline">{tag}</div><div class="contact">+60 17-424 6282 &nbsp; | &nbsp; <a href="mailto:lihhanko526@gmail.com">lihhanko526@gmail.com</a> &nbsp; | &nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div><div class="rule"></div></div>'''

def section(t,c): return f'<div class="section"><div class="section-title">{t}</div>{c}</div>'
def li(xs): return '<ul>'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'
def row_entry(title, role, date, bullets):
    return f'<div class="item"><div class="row"><div class="left"><span class="item-title">{title}</span> &nbsp;|&nbsp; <span class="role">{role}</span></div><div class="date">{date}</div></div>{li(bullets)}</div>'
def proj(title,url,tech,bullets):
    return f'<div class="item"><div><a class="item-title" href="{url}">{title}</a> &nbsp;|&nbsp; <span class="tech">{tech}</span></div>{li(bullets)}</div>'
def plain_proj(title,tech,bullets):
    return f'<div class="item"><div><span class="item-title">{title}</span> &nbsp;|&nbsp; <span class="tech">{tech}</span></div>{li(bullets)}</div>'
def edu(title,role,date,meta):
    return f'<div class="item"><div class="row"><div class="left"><span class="item-title">{title}</span> &nbsp;|&nbsp; <span class="role">{role}</span></div><div class="date">{date}</div></div><div class="edu-meta">{meta}</div></div>'

EN_CSS=r'''
@page{size:A4;margin:10.5mm 12.5mm 10.5mm 12.5mm}*{box-sizing:border-box}body{font-family:"Liberation Sans",Arial,sans-serif;color:#171717;font-size:10.45pt;line-height:1.36;margin:0}a{color:inherit;text-decoration:none}.header{text-align:center;margin-bottom:3.1mm}.name{font-size:21.2pt;font-weight:800;margin:0 0 1.6mm}.tagline{font-size:11.15pt;font-weight:700;color:#17365d;margin-bottom:.9mm}.contact{font-size:8.85pt;color:#5a6470}.rule{border-top:1.1pt solid #17365d;margin-top:1.55mm}.section{margin-top:2.65mm}.section-title{color:#17365d;font-size:10.95pt;font-weight:800;letter-spacing:.14pt;text-transform:uppercase;padding-bottom:.45mm;border-bottom:.6pt solid #9ca9b7;margin-bottom:1.75mm}.item{margin:0 0 1.95mm;break-inside:avoid}.row{display:flex;justify-content:space-between;align-items:baseline;gap:8mm}.left{min-width:0}.item-title{font-weight:800;font-size:9.9pt}.role{font-style:italic;color:#66717f}.date{white-space:nowrap;color:#66717f;font-size:8.7pt}.tech{font-style:italic;color:#66717f;font-size:8.6pt}ul{margin:.5mm 0 0 4.3mm;padding:0}li{margin:0 0 .78mm 0;padding-left:.25mm}.skills{margin-top:.05mm}.skill-line{margin:0 0 .55mm}.skill-label{font-weight:800}.edu-meta{color:#66717f;margin-top:.25mm;font-size:8.75pt}
'''
CN_CSS=r'''
@page{size:A4;margin:10.5mm 12.5mm 10.5mm 12.5mm}*{box-sizing:border-box}body{font-family:"Noto Sans CJK SC","Noto Sans CJK TC","Noto Sans CJK",sans-serif;color:#171717;font-size:10.85pt;line-height:1.44;margin:0}a{color:inherit;text-decoration:none}.header{text-align:center;margin-bottom:3.0mm}.name{font-size:21pt;font-weight:800;margin:0 0 2.2mm}.tagline{font-size:11.2pt;font-weight:700;color:#17365d;margin-bottom:.9mm}.contact{font-family:"Liberation Sans","Noto Sans CJK SC",sans-serif;font-size:8.9pt;color:#5a6470}.rule{border-top:1.1pt solid #17365d;margin-top:1.55mm}.section{margin-top:2.95mm}.section-title{color:#17365d;font-size:11.2pt;font-weight:800;padding-bottom:.45mm;border-bottom:.6pt solid #9ca9b7;margin-bottom:2.0mm}.item{margin:0 0 2.25mm;break-inside:avoid}.row{display:flex;justify-content:space-between;align-items:baseline;gap:7mm}.left{min-width:0}.item-title{font-weight:800;font-size:10.45pt}.role{color:#66717f}.date{white-space:nowrap;color:#66717f;font-size:9.35pt}.tech{font-family:"Liberation Sans","Noto Sans CJK SC",sans-serif;font-style:italic;color:#66717f;font-size:8.9pt}ul{margin:.55mm 0 0 4.35mm;padding:0}li{margin:0 0 1.0mm 0;padding-left:.25mm}.skills{margin-top:.05mm}.skill-line{margin:0 0 .55mm}.skill-label{font-weight:800}.edu-meta{color:#66717f;margin-top:.25mm;font-size:9.35pt}
'''

body=header.format(name='KO LIH HAN',tag='Software Engineer | Applied AI &amp; LLM Systems')
body+=section('EXPERIENCE',
    row_entry('Kahap Inc','Software Developer (Part-time)','Aug 2022 - Aug 2026',[
        'Primary developer for a production feedback platform that centralized submissions, automated notifications, and admin workflows.',
        'Maintained a separate Laravel/Vue.js career platform, shipping features and resolving production application and database issues.',
        'Managed deployments and server operations, including migrations/upgrades, Laravel queues/workers, SSL renewal, and database troubleshooting.'
    ])+
    row_entry('Pac Com Solution','Full-Stack Developer Intern','Jun 2021 - Jan 2022',[
        'Developed and maintained Laravel/Vue.js features for production POS applications.'
    ])
)
body+=section('PROJECTS',
    proj('Semantic Text-to-SQL','https://github.com/kolihhan/semantic-text2sql-agent','Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite',[
        'Built a local Text-to-SQL pipeline using XiYanSQL 7B with schema/value grounding, SQL validation, read-only execution, and bounded repair.',
        'Reached 58/100 execution-result matches on a 100-question BIRD evaluation and used failure analysis to refine grounding and repair.'
    ])+
    proj('Local RAG Search','https://github.com/kolihhan/local-rag-search','Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI',[
        'Built a hybrid retrieval API combining BM25, Qwen3 embeddings, and RRF, with per-result retrieval details for debugging.',
        'On 64 EnterpriseRAG-Bench queries over 5,189 documents, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.'
    ])+
    plain_proj('M.S. Thesis - Workplace Implicit Intent','Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation',[
        'Built a role- and context-grounded evidence framework for listener-side workplace intent using 51,414 posts and 20,455 extracted utterances.',
        'On 401 held-out utterances, Role-Context Top1 raised automated semantic F1 from 0.6250 to 0.6890 over the no-retrieved-evidence baseline.'
    ])
)
body+=section('SKILLS','''<div class="skills">
<div class="skill-line"><span class="skill-label">AI:</span> RAG, Information Retrieval, LLM Evaluation, LangGraph</div>
<div class="skill-line"><span class="skill-label">Programming / Backend:</span> Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js</div>
<div class="skill-line"><span class="skill-label">Data / Infra:</span> MySQL, Redis, SQLite, AWS, Linux, Git, pytest</div>
<div class="skill-line"><span class="skill-label">Languages:</span> Chinese (Native), English (Fluent), Malay (Intermediate)</div></div>''')
body+=section('EDUCATION',
    edu('National Tsing Hua University','M.S., Information Systems &amp; Applications','Sep 2024 - Jun 2026','GPA 4.09/4.3 &nbsp; | &nbsp; Taiwan')+
    edu('Chung Hua University','B.S., Computer Science &amp; Information Engineering','Sep 2022 - Jun 2024','GPA 3.9/4.0 &nbsp; | &nbsp; Taiwan')
)
HTML(string=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{EN_CSS}</style></head><body>{body}</body></html>').write_pdf(OUT/'resume-en-current.pdf')

body=header.format(name='高立恒',tag='软件工程师｜AI 应用 / 后端开发')
body+=section('教育背景',
    edu('国立清华大学（台湾）','资讯系统与应用研究所 理学硕士','2024.09 - 2026.06','GPA：4.09/4.3')+
    edu('中华大学（台湾）','资讯工程学系 学士','2022.09 - 2024.06','GPA：3.9/4.0')
)
body+=section('工作经历',
    row_entry('Kahap Inc','软件开发工程师（兼职）','2022.08 - 2026.08',[
        '作为主要开发者负责一套已上线的反馈平台，将反馈提交、自动通知和后台管理流程集中到同一系统。',
        '维护另一套 Laravel / Vue.js 职业平台，持续交付业务功能并排查线上应用与数据库问题。',
        '负责部署与服务器维护，包括服务器迁移/升级、Laravel Queue / Worker、SSL 续期和数据库故障排查。'
    ])+
    row_entry('Pac Com Solution','全栈开发实习生','2021.06 - 2022.01',[
        '使用 Laravel / Vue.js 开发并维护生产环境 POS 应用功能。'
    ])
)
body+=section('项目经历',
    proj('Semantic Text-to-SQL','https://github.com/kolihhan/semantic-text2sql-agent','Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite',[
        '使用 XiYanSQL 7B 搭建本地 Text-to-SQL 流程，加入 Schema / Value Grounding、SQL 校验、只读执行和有限次数修复。',
        '在 100 条 BIRD 测试题中，58 条查询的执行结果与参考结果一致，并结合错误分析调整 Grounding 与修复策略。'
    ])+
    proj('Local RAG Search','https://github.com/kolihhan/local-rag-search','Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI',[
        '搭建 BM25 + Qwen3 Embedding + RRF 的混合检索 API，并保留每条结果的检索信息用于调试。',
        '在 64 条 EnterpriseRAG-Bench 查询、5,189 份文档上，RRF 将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。'
    ])+
    plain_proj('硕士论文 - 职场隐含意图理解','Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation',[
        '构建角色与语境证据框架，用于生成职场对话中听者可能感受到的隐含意图；数据来自 51,414 篇帖子、20,455 条抽取语句。',
        '在 401 条留出测试语句上，Role-Context Top1 的自动语义 F1 从 baseline 0.6250 提升至 0.6890。'
    ])
)
body+=section('专业技能','''<div class="skills">
<div class="skill-line"><span class="skill-label">AI：</span> RAG、Information Retrieval、LLM Evaluation、LangGraph</div>
<div class="skill-line"><span class="skill-label">编程 / 后端：</span> Python、SQL、JavaScript、PHP、FastAPI、REST APIs、Laravel、Vue.js</div>
<div class="skill-line"><span class="skill-label">数据 / 基础设施：</span> MySQL、Redis、SQLite、AWS、Linux、Git、pytest</div>
<div class="skill-line"><span class="skill-label">语言：</span> 中文（母语）、英语（流利）、马来语（中等）</div></div>''')
HTML(string=f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>{CN_CSS}</style></head><body>{body}</body></html>').write_pdf(OUT/'resume-cn-current.pdf')
