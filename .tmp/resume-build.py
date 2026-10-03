from weasyprint import HTML
from pathlib import Path

OUT = Path("resumes")
OUT.mkdir(exist_ok=True)

COMMON_CSS = r'''
@page { size: A4; margin: 6.8mm 11.5mm 12.5mm 11.5mm; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { color: #161616; }
a { color: inherit; text-decoration: none; }
.header { text-align: center; margin: 0 0 6.2pt 0; }
.name { margin: 0; font-weight: 700; color: #111; line-height: 1.08; }
.headline { margin-top: 5.6pt; font-weight: 700; color: #15385f; line-height: 1.1; }
.contact { margin-top: 5.0pt; color: #5b6b7e; line-height: 1.1; }
.rule { border-top: 1.8pt solid #15385f; margin: 7.0pt 0 7.1pt 0; }
.section { margin-top: 7.0pt; }
.section:first-of-type { margin-top: 0; }
.section-title { color: #15385f; font-weight: 700; margin: 0 0 7.0pt 0; padding: 0 0 3.7pt 0; border-bottom: 0.7pt solid #a7b4c2; line-height: 1.0; }
.entry { margin: 0 0 8.2pt 0; break-inside: avoid; }
.entry:last-child { margin-bottom: 0; }
.row { display: flex; justify-content: space-between; align-items: baseline; gap: 8pt; }
.left { min-width: 0; flex: 1; }
.right { flex: 0 0 auto; white-space: nowrap; color: #5b6b7e; }
.entry-title { font-weight: 700; }
.entry-sub { color: #5b6b7e; }
.tech { font-style: italic; color: #66778d; }
ul { margin: 4.2pt 0 0 0; padding-left: 13.8pt; }
li { margin: 0 0 3.0pt 0; padding-left: 0.6pt; }
li:last-child { margin-bottom: 0; }
.skill-row { margin: 0 0 3.0pt 0; }
.skill-row:last-child { margin-bottom: 0; }
.gpa { margin-top: 3.0pt; color: #5b6b7e; }
'''

EN_CSS = COMMON_CSS + r'''
.entry { margin-bottom: 9.2pt; }
.section { margin-top: 8.0pt; }
.section:first-of-type { margin-top: 0; }
.section-title { margin-bottom: 7.8pt; }
li { margin-bottom: 3.3pt; }
body { font-family: "Liberation Sans", Arial, sans-serif; font-size: 10.7pt; line-height: 1.43; }
.name { font-size: 21.8pt; }
.headline { font-size: 12.4pt; }
.contact { font-size: 9.0pt; }
.section-title { font-size: 11.55pt; }
.right, .gpa { font-size: 8.95pt; }
.tech { font-size: 8.75pt; }
'''

CN_CSS = COMMON_CSS + r'''
.entry { margin-bottom: 13.5pt; }
.section { margin-top: 11.6pt; }
.section:first-of-type { margin-top: 0; }
.section-title { margin-bottom: 9.2pt; }
li { margin-bottom: 4.0pt; }
.skill-row { margin-bottom: 4.4pt; }
body { font-family: "Noto Sans CJK SC", "Noto Sans CJK", sans-serif; font-size: 10.9pt; line-height: 1.49; }
.name { font-size: 22.2pt; }
.headline { font-size: 12.45pt; }
.contact { font-family: "Noto Sans CJK SC", "Noto Sans CJK", sans-serif; font-size: 9.0pt; }
.section-title { font-size: 11.8pt; }
.right, .gpa { font-size: 8.95pt; }
.tech { font-family: "Liberation Sans", Arial, sans-serif; font-size: 8.75pt; }
ul { padding-left: 15.0pt; }
'''

EN_BODY = r'''
<div class="header">
  <div class="name">KO LIH HAN</div>
  <div class="headline">Software Engineer | Applied AI &amp; LLM Systems</div>
  <div class="contact">+60 17-424 6282 &nbsp; | &nbsp; <a href="mailto:lihhanko526@gmail.com">lihhanko526@gmail.com</a> &nbsp; | &nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div>
</div>
<div class="rule"></div>

<section class="section">
  <h2 class="section-title">EXPERIENCE</h2>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">Kahap Inc</span><span class="entry-sub"><i> | Software Developer (Part-time)</i></span></div><div class="right">Aug 2022 - Aug 2026</div></div>
    <ul>
      <li>Primary developer for a production feedback platform, centralizing submissions, automated notifications, and admin workflows.</li>
      <li>Maintained and shipped features for a separate Laravel/Vue.js career platform, debugging production application and database issues.</li>
      <li>Handled deployments and production operations, including server migrations/upgrades, Laravel queues/workers, SSL renewal, and database troubleshooting.</li>
    </ul>
  </div>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">Pac Com Solution</span><span class="entry-sub"><i> | Full-Stack Developer Intern</i></span></div><div class="right">Jun 2021 - Jan 2022</div></div>
    <ul><li>Developed and maintained Laravel/Vue.js features for a production POS application.</li></ul>
  </div>
</section>

<section class="section">
  <h2 class="section-title">PROJECTS</h2>
  <div class="entry">
    <div><a class="entry-title" href="https://github.com/kolihhan/semantic-text2sql-agent">Semantic Text-to-SQL</a><span class="tech"> | Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite</span></div>
    <ul>
      <li>Built a local Text-to-SQL pipeline with XiYanSQL 7B, schema/value grounding, SQL validation, read-only execution, and bounded repair.</li>
      <li>Measured 58/100 execution-result matches on a frozen 100-question BIRD set and documented grounding and repair failure modes.</li>
    </ul>
  </div>
  <div class="entry">
    <div><a class="entry-title" href="https://github.com/kolihhan/local-rag-search">Local RAG Search</a><span class="tech"> | Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI</span></div>
    <ul>
      <li>Built a FastAPI hybrid retriever combining BM25, Qwen3 embeddings, and RRF, exposing lexical, dense, and fused ranks per result.</li>
      <li>On a frozen 64-query EnterpriseRAG-Bench slice over 5,189 documents, RRF improved Recall@10 from 0.734 to 0.763 and MRR@20 from 0.679 to 0.742 versus BM25.</li>
    </ul>
  </div>
  <div class="entry">
    <div><span class="entry-title">M.S. Thesis - Workplace Implicit Intent</span><span class="tech"> | Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation</span></div>
    <ul>
      <li>Built a role- and context-grounded retrieval framework for listener-side workplace intent from 51,414 posts and 20,455 extracted utterances.</li>
      <li>On 401 held-out utterances, Role-Context Top1 scored 0.6890 automated semantic F1 versus 0.6250 without retrieved evidence.</li>
    </ul>
  </div>
</section>

<section class="section">
  <h2 class="section-title">SKILLS</h2>
  <div class="skill-row"><b>AI:</b> RAG, Information Retrieval, LLM Evaluation, LangGraph</div>
  <div class="skill-row"><b>Programming / Backend:</b> Python, SQL, JavaScript, PHP, FastAPI, REST APIs, Laravel, Vue.js</div>
  <div class="skill-row"><b>Data / Infra:</b> MySQL, SQLite, Linux, Git, pytest</div>
  <div class="skill-row"><b>Languages:</b> Chinese (Native), English (Fluent), Malay (Intermediate)</div>
</section>

<section class="section">
  <h2 class="section-title">EDUCATION</h2>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">National Tsing Hua University</span><span class="entry-sub"><i> | M.S., Information Systems &amp; Applications</i></span></div><div class="right">Sep 2024 - Jun 2026</div></div>
    <div class="gpa">GPA 4.09/4.3 &nbsp; | &nbsp; Taiwan</div>
  </div>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">Chung Hua University</span><span class="entry-sub"><i> | B.S., Computer Science &amp; Information Engineering</i></span></div><div class="right">Sep 2022 - Jun 2024</div></div>
    <div class="gpa">GPA 3.9/4.0 &nbsp; | &nbsp; Taiwan</div>
  </div>
</section>
'''

CN_BODY = r'''
<div class="header">
  <div class="name">高立恒</div>
  <div class="headline">软件工程师｜AI 应用 / 后端开发</div>
  <div class="contact">+60 17-424 6282 &nbsp; | &nbsp; <a href="mailto:lihhanko526@gmail.com">lihhanko526@gmail.com</a> &nbsp; | &nbsp; <a href="https://github.com/kolihhan">github.com/kolihhan</a></div>
</div>
<div class="rule"></div>

<section class="section">
  <h2 class="section-title">教育背景</h2>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">国立清华大学（台湾）</span><span class="entry-sub"> | 资讯系统与应用研究所 理学硕士</span></div><div class="right">2024.09 - 2026.06</div></div>
    <div class="gpa">GPA：4.09/4.3</div>
  </div>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">中华大学（台湾）</span><span class="entry-sub"> | 资讯工程学系 学士</span></div><div class="right">2022.09 - 2024.06</div></div>
    <div class="gpa">GPA：3.9/4.0</div>
  </div>
</section>

<section class="section">
  <h2 class="section-title">工作经历</h2>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">Kahap Inc</span><span class="entry-sub"> | 软件开发工程师（兼职）</span></div><div class="right">2022.08 - 2026.08</div></div>
    <ul>
      <li>作为主要开发者负责一套已上线反馈平台的开发与维护，统一反馈提交、自动通知和后台管理流程。</li>
      <li>负责另一套 Laravel / Vue.js 职业发展平台的功能迭代，排查线上应用和数据库问题。</li>
      <li>负责部署和线上运维，包括服务器迁移/升级、Laravel 队列 / Worker、SSL 续期及数据库故障排查。</li>
    </ul>
  </div>
  <div class="entry">
    <div class="row"><div class="left"><span class="entry-title">Pac Com Solution</span><span class="entry-sub"> | 全栈开发实习生</span></div><div class="right">2021.06 - 2022.01</div></div>
    <ul><li>使用 Laravel / Vue.js 开发并维护已上线的 POS 系统功能。</li></ul>
  </div>
</section>

<section class="section">
  <h2 class="section-title">项目经历</h2>
  <div class="entry">
    <div><a class="entry-title" href="https://github.com/kolihhan/semantic-text2sql-agent">Semantic Text-to-SQL</a><span class="tech"> | Python · XiYanSQL 7B · LangGraph · FastAPI · SQLite</span></div>
    <ul>
      <li>基于 XiYanSQL 7B 搭建本地 Text-to-SQL 流程，包含 Schema / Value Grounding、SQL 校验、只读执行和限次修复。</li>
      <li>在 100 条固定 BIRD 测试题上，执行结果匹配为 58/100，并整理 Grounding 与修复阶段的失败模式。</li>
    </ul>
  </div>
  <div class="entry">
    <div><a class="entry-title" href="https://github.com/kolihhan/local-rag-search">Local RAG Search</a><span class="tech"> | Python · BM25 · Qwen3-Embedding-0.6B · RRF · FastAPI</span></div>
    <ul>
      <li>搭建基于 BM25、Qwen3 Embedding 和 RRF 的混合检索 API，返回每条结果的 BM25、Dense 与 RRF 排名，便于调试。</li>
      <li>在包含 64 条查询、5,189 份文档的 EnterpriseRAG-Bench 固定切片上，RRF 将 Recall@10 从 0.734 提升至 0.763，MRR@20 从 0.679 提升至 0.742。</li>
    </ul>
  </div>
  <div class="entry">
    <div><span class="entry-title">硕士论文 - 职场隐含意图理解</span><span class="tech"> | Llama 3.1 8B · Retrieval · Knowledge Graphs · Semantic Evaluation</span></div>
    <ul>
      <li>构建基于角色关系与上下文检索的职场隐含意图框架，数据覆盖 51,414 篇帖子和 20,455 条抽取语句。</li>
      <li>在 401 条留出评测语句上，Role-Context Top1 的自动语义 F1 为 0.6890，对比无检索证据 baseline 的 0.6250。</li>
    </ul>
  </div>
</section>

<section class="section">
  <h2 class="section-title">专业技能</h2>
  <div class="skill-row"><b>AI：</b> RAG、信息检索、LLM 评测、LangGraph</div>
  <div class="skill-row"><b>编程 / 后端：</b> Python、SQL、JavaScript、PHP、FastAPI、REST API、Laravel、Vue.js</div>
  <div class="skill-row"><b>数据 / 基础设施：</b> MySQL、SQLite、Linux、Git、pytest</div>
  <div class="skill-row"><b>语言：</b> 中文（母语）、英语（流利）、马来语（中等）</div>
</section>
'''

def render(title, css, body, out_name):
    html = f'''<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>{body}</body></html>'''
    HTML(string=html, base_url=str(OUT)).write_pdf(OUT / out_name)

render("Ko Lih Han Resume", EN_CSS, EN_BODY, "resume-en-current.pdf")
render("高立恒 简历", CN_CSS, CN_BODY, "resume-cn-current.pdf")
