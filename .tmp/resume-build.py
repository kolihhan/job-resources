from pathlib import Path
from html import escape
from weasyprint import HTML

OUT = Path("resumes")

BASE_CSS = r"""
@page { size: A4; margin: 8.5mm 11.5mm 11mm 11.5mm; }
* { box-sizing: border-box; }
body { margin: 0; color:#171717; font-family: "Liberation Sans", Arial, sans-serif; font-size:10.45pt; line-height:1.34; }
a { color: inherit; text-decoration: none; }
.header { text-align:center; margin-bottom:7.5pt; }
.name { font-size:21.5pt; font-weight:700; letter-spacing:.2pt; line-height:1.0; margin:0 0 8pt; }
.headline { font-size:12.25pt; font-weight:700; color:#17365d; line-height:1.1; margin-bottom:5.5pt; }
.contact { font-size:8.9pt; color:#5f6b7a; line-height:1.1; }
.rule { border-top:1.4pt solid #17365d; margin-top:7pt; }
.section { margin-top:8.1pt; }
.section-title { color:#17365d; font-weight:700; font-size:11.4pt; text-transform:uppercase; line-height:1.0; padding-bottom:3.5pt; border-bottom:.65pt solid #aeb7c3; margin-bottom:6.3pt; }
.entry { margin-bottom:7pt; break-inside:avoid; }
.entry:last-child { margin-bottom:0; }
.row { display:flex; justify-content:space-between; align-items:baseline; gap:8pt; margin-bottom:2.3pt; }
.left { min-width:0; }
.right { flex:0 0 auto; color:#5f6b7a; font-size:8.9pt; }
.org, .proj { font-weight:700; }
.role { color:#5f6b7a; font-style:italic; }
.tech { color:#6d7888; font-style:italic; font-size:8.65pt; }
ul { margin:2.4pt 0 0 13.5pt; padding:0; }
li { margin:0 0 2.6pt 0; padding-left:.7pt; }
li:last-child { margin-bottom:0; }
.skills { line-height:1.38; }
.skills div { margin-bottom:1.5pt; }
.skills div:last-child { margin-bottom:0; }
.edu .row { margin-bottom:1.2pt; }
.edu-meta { color:#5f6b7a; font-size:8.9pt; }
"""

CN_CSS = r"""
body { font-family: "Noto Sans CJK SC", "Liberation Sans", sans-serif; font-size:10.5pt; line-height:1.46; }
.section-title { text-transform:none; font-size:11.7pt; }
.section { margin-top:9pt; }
.entry { margin-bottom:7.6pt; }
li { margin-bottom:3pt; }
.headline { font-size:12.3pt; }
.name { font-size:22pt; }
.role { font-style:normal; }
.tech { font-family:"Liberation Sans", "Noto Sans CJK SC", sans-serif; }
.skills { line-height:1.5; }
"""

def wrap(doc_title, body, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{escape(doc_title)}</title><style>{BASE_CSS}\n{css}</style></head><body>{body}</body></html>"""

def section(title, content):
    return f'<section class="section"><div class="section-title">{title}</div>{content}</section>'

def entry(title_html, date, bullets, cls=""):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f'<div class="entry {cls}"><div class="row"><div class="left">{title_html}</div><div class="right">{date}</div></div><ul>{lis}</ul></div>'

def proj(title, url, tech, bullets):
    if url:
        title_html = f'<span class="proj"><a href="{url}">{title}</a></span> <span class="role">|</span> <span class="tech">{tech}</span>'
    else:
        title_html = f'<span class="proj">{title}</span> <span class="role">|</span> <span class="tech">{tech}</span>'
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f'<div class="entry"><div class="row"><div class="left">{title_html}</div></div><ul>{lis}</ul></div>'

def edu(org, degree, date, meta):
    return f'<div class="entry edu"><div class="row"><div class="left"><span class="org">{org}</span> <span class="role">| {degree}</span></div><div class="right">{date}</div></div><div class="edu-meta">{meta}</div></div>'

def build_en():
    header = """<header class="header"><div class="name">KO LIH HAN</div><div class="headline">Software Engineer | Applied AI &amp; LLM Systems</div><div class="contact">+60 17-424 6282 &nbsp; | &nbsp; <a href="mailto:lihhanko526@gmail.com">lihhanko526@gmail.com</a> &nbsp; | &nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div><div class="rule"></div></header>"""
    exp = "".join([
        entry('<span class="org">Kahap Inc</span> <span class="role">| Software Developer (Part-time)</span>', 'Aug 2022 - Aug 2026', [
            'Primary developer for a production feedback platform, centralizing submissions, automated notifications, and admin workflows.',
            'Maintained and shipped features for a separate Laravel/Vue.js career platform, debugging production application and database issues.',
            'Handled deployments and production operations, including server migrations/upgrades, Laravel queues/workers, SSL renewal, and database troubleshooting.'
        ]),
        entry('<span class="org">Pac Com Solution</span> <span class="role">| Full-Stack Developer Intern</span>', 'Jun 2021 - Jan 2022', [
            'Developed and maintained Laravel/Vue.js features for a production POS application.'
        ])
    ])
    projects = "".join([
        proj('Semantic Text-to-SQL', 'https://github.com/kolihhan/semantic-text2sql-agent', 'Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite', [
            'Built a local Text-to-SQL pipeline with XiYanSQL 7B, schema/value grounding, SQL validation, read-only execution, and bounded repair.',
            'Measured 58/100 execution-result matches on a frozen 100-question BIRD set and documented grounding and repair failure modes.'
        ]),
        proj('Local RAG Search', 'https://github.com/kolihhan/local-rag-search', 'Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI', [
            'Built a FastAPI hybrid retriever combining BM25, Qwen3 embeddings, and RRF, exposing lexical, dense, and fused ranks per result.',
            'On a frozen 64-query EnterpriseRAG-Bench slice over 5,189 documents, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.'
        ]),
        proj('M.S. Thesis - Workplace Implicit Intent', None, 'Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation', [
            'Built a role- and context-grounded retrieval framework for listener-side workplace intent from 51,414 posts and 20,455 extracted utterances.',
            'On 401 held-out utterances, Role-Context Top1 scored 0.6890 automated semantic F1 versus 0.6250 without retrieved evidence.'
        ])
    ])
    skills = """<div class="skills"><div><b>AI:</b> RAG, Information Retrieval, LLM Evaluation, LangGraph</div><div><b>Programming / Backend:</b> Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js</div><div><b>Data / Infra:</b> MySQL, SQLite, Linux, Git, pytest</div><div><b>Languages:</b> Chinese (Native), English (Fluent), Malay (Intermediate)</div></div>"""
    education = "".join([
        edu('National Tsing Hua University', 'M.S., Information Systems &amp; Applications', 'Sep 2024 - Jun 2026', 'GPA 4.09/4.3 &nbsp; | &nbsp; Taiwan'),
        edu('Chung Hua University', 'B.S., Computer Science &amp; Information Engineering', 'Sep 2022 - Jun 2024', 'GPA 3.9/4.0 &nbsp; | &nbsp; Taiwan')
    ])
    html = wrap('Ko Lih Han Resume', header + section('EXPERIENCE', exp) + section('PROJECTS', projects) + section('SKILLS', skills) + section('EDUCATION', education))
    HTML(string=html, base_url=str(OUT)).write_pdf(OUT / 'resume-en-current.pdf')

def build_cn():
    header = """<header class="header"><div class="name">高立恒</div><div class="headline">软件工程师｜AI 应用 / 后端开发</div><div class="contact">+60 17-424 6282 &nbsp; | &nbsp; <a href="mailto:lihhanko526@gmail.com">lihhanko526@gmail.com</a> &nbsp; | &nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div><div class="rule"></div></header>"""
    education = "".join([
        edu('国立清华大学（台湾）', '资讯系统与应用研究所 理学硕士', '2024.09 - 2026.06', 'GPA：4.09/4.3'),
        edu('中华大学（台湾）', '资讯工程学系 学士', '2022.09 - 2024.06', 'GPA：3.9/4.0')
    ])
    exp = "".join([
        entry('<span class="org">Kahap Inc</span> <span class="role">| 软件开发工程师（兼职）</span>', '2022.08 - 2026.08', [
            '作为主要开发者负责一套已上线反馈平台的开发与维护，统一反馈提交、自动通知和后台管理流程。',
            '负责另一套 Laravel / Vue.js 职业发展平台的功能迭代，排查线上应用和数据库问题。',
            '负责部署和线上运维，包括服务器迁移/升级、Laravel 队列 / Worker、SSL 续期及数据库故障排查。'
        ]),
        entry('<span class="org">Pac Com Solution</span> <span class="role">| 全栈开发实习生</span>', '2021.06 - 2022.01', [
            '使用 Laravel / Vue.js 开发并维护已上线的 POS 系统功能。'
        ])
    ])
    projects = "".join([
        proj('Semantic Text-to-SQL', 'https://github.com/kolihhan/semantic-text2sql-agent', 'Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite', [
            '基于 XiYanSQL 7B 搭建本地 Text-to-SQL 流程，包含 Schema / Value Grounding、SQL 校验、只读执行和限次修复。',
            '在 100 条固定 BIRD 测试题上，执行结果匹配为 58/100，并整理 Grounding 与修复阶段的失败模式。'
        ]),
        proj('Local RAG Search', 'https://github.com/kolihhan/local-rag-search', 'Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI', [
            '搭建基于 BM25、Qwen3 Embedding 和 RRF 的混合检索 API，返回每条结果的 BM25、Dense 与 RRF 排名，便于调试。',
            '在包含 64 条查询、5,189 份文档的 EnterpriseRAG-Bench 固定切片上，RRF 将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。'
        ]),
        proj('硕士论文 - 职场隐含意图理解', None, 'Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation', [
            '构建基于角色关系与上下文检索的职场隐含意图框架，数据覆盖 51,414 篇帖子和 20,455 条抽取语句。',
            '在 401 条留出评测语句上，Role-Context Top1 的自动语义 F1 为 0.6890，对比无检索证据 baseline 的 0.6250。'
        ])
    ])
    skills = """<div class="skills"><div><b>AI：</b> RAG、信息检索、LLM 评测、LangGraph</div><div><b>编程 / 后端：</b> Python、SQL、JavaScript、PHP、FastAPI、REST API、Laravel、Vue.js</div><div><b>数据 / 基础设施：</b> MySQL、SQLite、Linux、Git、pytest</div><div><b>语言：</b> 中文（母语）、英语（流利）、马来语（中等）</div></div>"""
    html = wrap('高立恒 简历', header + section('教育背景', education) + section('工作经历', exp) + section('项目经历', projects) + section('专业技能', skills), CN_CSS)
    HTML(string=html, base_url=str(OUT)).write_pdf(OUT / 'resume-cn-current.pdf')

if __name__ == '__main__':
    build_en()
    build_cn()
