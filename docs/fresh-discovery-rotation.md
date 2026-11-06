# Fresh Discovery Rotation

Focused execution supplement to `README.md`, `RULES.md`, and `docs/source-routing.md`.

## Goal

Fresh discovery must cover the relevant platform set instead of repeatedly choosing the easiest source. Fresh discovery and FreeHire triage are independent phases so neither starves the other.

**Canonical FreeHire throughput/retry/transport rules live only in `docs/freehire-triage-consumption.md`. Do not restate or override those numbers here.**

## Authoritative fresh state

- SG: `discovery-state/fresh-sg.json`
- CN: `discovery-state/fresh-cn.json`
- MY: `discovery-state/fresh-my.json`

Opportunity/application state remains only in GitHub Issues.

## Per-run phases

### Phase A — fresh discovery

Every run attempts:

1. one official/canonical owner bucket;
2. the next **two individual platforms** in the market sweep;
3. one query-family bucket;
4. SG additionally one current research/lab bucket.

Platform rules:

- start at `next_platform_index`;
- attempt two consecutive platforms in listed order;
- do not repeat a platform until the sweep cycles through the others;
- bounded failed/weak searches still count as attempts and must be recorded honestly;
- persist/read back fresh state after attempts;
- prefer fresh-head/delta semantics where supported.


### Coverage recovery and honest completion

The rotation counts **attempts**, not successful market coverage. Continue advancing the platform index after a bounded attempt (to avoid getting stuck on a blocked site), but never label a low-coverage run as a healthy complete search.

For each selected platform:

1. Count only distinct, identifiable job rows actually inspected. An unreachable page, blank results, or an index hit with no exact role identity counts **zero**.
2. When a platform yields **zero rows** or substantially misses its roughly 20-row target, perform **one bounded alternate-source gap pass in the same run**: indexed/site-specific exact-role queries, official ATS/company career search, or PI/lab postings appropriate to that platform and query bucket. Clearly distinguish alternate-source rows from native rows; do not double count across search queries or source families.
3. Re-anchor promising new signals to authoritative exact-role JD and usable application route. If the official page is JS-only, try another employer-published route or faithful full-JD reproduction once; record the unresolved blocker rather than claiming verification.
4. If coverage remains weak, set run_quality=PARTIAL_COVERAGE and record coverage_gaps/fallback_sources in the run metrics. Zero new APPLY/CHECK then means **no verified survivors in the limited slice**, not no new roles on the market. The next run still rotates normally; revisit a failed source through its next rotation or high-value targeted gap pass.

**SG research recall:** Every SG run also performs a bounded current RA/RE/Research Officer lab/official-portal sweep in its research bucket, including current NUS/NTU/A*STAR requisitions or PI-managed postings. Use role IDs and posted dates to find genuinely new opportunities, not just static lab homepages. Check all-Issue history before deep work; do not let unrelated university/research roles crowd out knowledge-enhanced LLM, Agent, NLP and evaluation research.

**CN access fallback:** BOSS/51job/脉脉 inaccessible does not mean no vacancies. Use bounded search-index/native alternatives (including 牛客, employer social recruiting and lab/PI direct postings), and preserve the unverified source as a coverage gap.

With two platforms per hourly run, SG/MY complete five-platform sweeps within at most three successful runs; CN completes seven platforms within at most four.

### Phase B — FreeHire triage

Execute **only** `docs/freehire-triage-consumption.md` after Phase A. The old raw-sequence recovery document is historical/audit only and is not an active hourly obligation.

## SG platform sweep

0. LinkedIn Jobs Singapore
1. JobStreet Singapore
2. Indeed Singapore
3. MyCareersFuture
4. recruiter / team / PI direct posts

### SG owner buckets

0. NUS / NTU / A*STAR / AI Singapore
1. Sea / SAIL / Shopee / Grab / Singtel
2. ByteDance / TikTok / Micron
3. Google / Microsoft / Apple / OpenAI
4. strong finance / fintech AI teams and other recurring canonical owners

### SG query buckets

0. Agent / LLM / RAG / evaluation
1. NLP / search / retrieval / ranking / knowledge graph
2. AI backend / platform / inference / ML systems
3. RA / RE / Applied Scientist + LLM/NLP
4. coding agent / MCP / tool use / agent reliability

### SG research/lab buckets

0. NUS
1. NTU
2. A*STAR
3. SMU
4. SUTD

## CN platform sweep

0. BOSS直聘
1. 牛客招聘
2. 猎聘
3. 智联招聘
4. 前程无忧 / 51job
5. 脉脉 / team-direct recruiting signals
6. 高校 / 实验室 / 研究院 / PI / research-direct recruiting signals

The research-direct family is bounded: prioritize current RA/RE/Research Associate/Research Officer/research-engineering signals from strong labs, institutes, PI/team pages, GitHub recruiting notices, and joint research centres materially overlapping LLM, NLP, retrieval, knowledge, Agent, or AI systems. Do not crawl universities indiscriminately.

### CN owner buckets

0. Alibaba / Tencent
1. ByteDance / Baidu
2. Huawei / Meituan
3. JD / Xiaohongshu
4. DeepSeek / Moonshot
5. Zhipu AI / StepFun / other strong AI-native owners

### CN query buckets

0. Agent / 智能体 / planning / memory / tool use
1. RAG / 知识库 / 知识图谱 / NL2SQL / Data Agent
2. 大模型评测 / Agent评测 / AI质量 / reliability
3. NLP / 检索 / 搜索 / ranking
4. AI后端 / 大模型平台 / 推理 / AI systems
5. Coding Agent / AI Coding / MCP / Skills / Harness

## MY platform sweep

0. LinkedIn Jobs Malaysia
1. JobStreet Malaysia
2. Indeed Malaysia
3. Hiredly
4. recruiter / team / direct hiring posts

### MY owner buckets

0. Sea / Shopee / Grab
1. Gen Digital / MoneyLion
2. AEON Bank / GXBank
3. Keysight / AMD / Intel
4. Dell / YTL AI Labs
5. MIMOS / strong university-industry research labs / other recurring destination-quality owners

### MY query buckets

0. Agent / LLM / RAG / GenAI
1. NLP / search / retrieval / evaluation / knowledge
2. AI backend / platform / ML engineering
3. destination-quality backend / data / cloud / SRE / SDET
4. destination-quality full-stack / product engineering with material AI signal

## State advancement

After Phase A:

- advance `next_platform_index` by attempted platforms, wrapping modulo platform count;
- increment `platform_cycle` on wrap;
- increment owner/query buckets modulo their counts;
- SG increments research bucket modulo 5;
- write `last_completed_at`, last attempted buckets/platforms, and increment `run_counter`;
- read back the state before reporting success.

## Health criterion

Healthy fresh discovery means:

- platform rotations complete without favorite-source loops;
- owner/query/research buckets continue rotating;
- FreeHire runs independently under its canonical contract;
- verified survivors reach APPLY/CHECK when found.
