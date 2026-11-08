# Fresh Discovery Rotation

Focused execution supplement to `README.md`, `RULES.md`, and `docs/source-routing.md`.

## Goal

Fresh discovery must cover the relevant platform set instead of repeatedly choosing the easiest source. **Substantive engineering and research both get top-priority fresh ATS/official source coverage**, rather than research-lab visits consuming the engineering search budget. Fresh discovery and FreeHire triage are independent phases so neither starves the other.

**Canonical FreeHire throughput/retry/transport rules live only in `docs/freehire-triage-consumption.md`. Do not restate or override those numbers here.**

## Authoritative fresh state

- SG: `discovery-state/fresh-sg.json`
- CN: `discovery-state/fresh-cn.json`
- MY: `discovery-state/fresh-my.json`

Opportunity/application state remains only in GitHub Issues.

## Per-run phases

### Phase A — fresh discovery

Every run prioritizes **completed, useful candidate decisions** over a wide but superficial source-attempt count:

1. **Start with the next current official employer/ATS owner bucket and one distinct query-family bucket**; get exact current role IDs, not just the company homepage. Explicitly include engineering career/ATS searches, not only academic RA/RE. Expand to two owners/three queries only after seriously promising identities receive disposition.
2. Resume at least **one unresolved high-value coverage debt** with a concrete next probe, prioritizing debts exposing NEW exact employer roles; do not revisit old failed URLs without a materially different path.
3. Attempt the next **two individual platforms** in rotation with real page/cursor depth; four platforms is a **ceiling** when time and verification budget allow, not a mandatory minimum. Process good fresh exact roles before the next platform.
4. SG also attempts **one current research/lab bucket**, expandable to two when useful; this complements rather than replaces the official engineering ATS probe.

Platform rules:

- start at `next_platform_index` and rotate by only the platforms actually attempted;
- do not repeat a platform until the sweep cycles through the others, apart from explicit coverage-debt recovery;
- process new exact job identities through the cheap gate and, for serious leads, actual JD verification **before** spending the rest of the run on more metadata searches;
- two platforms per hour cover the SG/MY five-source set in at most three *attempted* cycles and the CN seven-source set in at most four; none of these attempt counts proves adequate coverage;
- bounded failed/weak searches still count as attempts and must be recorded honestly, but never count as successful coverage;
- persist/read back fresh state after attempts;
- prefer fresh-head/delta semantics where supported.
- search each selected query family across the chosen platforms with bounded metadata-first discovery; do not multiply expensive full-JD reads by the platform × query cross-product.
- prioritize unique early-career **AI engineering OR research** exact job identities, not advertised search-result totals.


### Mandatory source-depth and unfinished-work contract

**One search page or a few indexed snippets is not a completed source scan.** A platform attempt is a checkpoint, never proof of coverage. Each selected source should first try a current result set and **at least the next page/cursor** when the source actually exposes pagination (continue while useful new identities appear, up to a bounded three-page probe). Log the first and next page separately, with actual exact-role identifiers or direct URLs and the source's end-of-results signal if available. A search-result headline, a platform-advertised total, or a homepage is **not** an identifiable job row.

When native pagination is inaccessible, explicitly log `native_pages_read: 0` and recover via at least **two independent source paths** where possible (employer careers/ATS API, alternative native job pages, indexed exact-role detail pages, PI/team direct notices). Distinguish original-platform verified rows, search-index fallback rows, and employer-direct rows. Never describe indexed snippets as "native pages scanned". If these probes cannot produce a credible cross-page sample or verified exhaustion, mark this source `UNDERCOVERED` rather than reporting it searched comprehensively.

The roughly 20 unique identifiable rows per platform is a **coverage diagnostic**, not a reason to fabricate hits or waste full-JD reads. Below-target scans require evidence of source exhaustion or a durable coverage debt, never an unsupported `DONE`. Do not increase the number of platforms at the expense of reading page 2 or following exact job details. Four attempted platform families are a trial ceiling; a substantial multi-page, evidence-backed pass is better than four token one-page attempts.

**Durable coverage debt:** `discovery-state/fresh-<market>.json` owns an additive `coverage_debt` array (not GitHub Issues, not a second job queue). Each debt records `platform`, `query_family`, `last_attempt_at`, `native_pages_read`, `native_unique_rows`, `fallback_unique_rows`, `reason`, and `next_probe` (exact next page/cursor, second source, or employer ATS path). Keep debts distinct by platform + query family. Each new run must attempt at least one previous high-value debt before declaring the current rotation handled, unless access/tooling is genuinely unavailable; in that case preserve the debt and report the blocker. Clear only when a real multi-page/exhaustion check or independent substitute establishes adequate coverage. Bound the array to current actionable gaps without silently erasing unresolved relevant gaps; coalesce redundant histories for the same platform/query.

Rotation counters may still move past an inaccessible source to avoid a permanent deadlock, but **the unresolved coverage debt must not disappear**. The run is `PARTIAL_COVERAGE` while material debts or unprocessed required phases remain. Do not use "done", "finished market scan", "no more jobs", or "scanned the market" for a partial run. Say exactly what was and was not inspected. If Phase B FreeHire is untouched, record `phase_b_completed: false`; even with a fresh-platform pass, the full scout cycle is unfinished.

### Coverage recovery and honest completion

The earlier 4-platform / 2-owner / 3-query / (SG) 2-lab sweep was a throughput trial that repeatedly ended before candidate verification. Prefer **two deeper platforms + one owner + one query + one SG lab**, expanding only after candidate decisions and durable state handoff. Do not spend verification budget just to inflate source-attempt counts. Use metadata-first search, all-Issue-history dedupe, and targeted first-party checks. If execution limits prevent all buckets, report PARTIAL_COVERAGE and persist only attempts actually made; never advance an unattempted bucket.

For any run report the attempted platform identities, rows inspected per platform, distinct net-new identities, unique duplicates, cheap rejects, authoritative full-JD reads, new durable APPLY/CHECK survivors, fallbacks and failure reasons. Count source-family overlaps only once in global unique counts. A high platform attempt count alone is not proof of recall.

The rotation counts **attempts**, not successful market coverage. Continue advancing the platform index after a bounded attempt (to avoid getting stuck on a blocked site), but never label a low-coverage run as a healthy complete search.

For each selected platform:

1. Count only distinct, identifiable job rows actually inspected. An unreachable page, blank results, or an index hit with no exact role identity counts **zero**.
2. When a platform yields **zero rows** or substantially misses its roughly 20-row target, perform **one bounded alternate-source gap pass in the same run**: indexed/site-specific exact-role queries, official ATS/company career search, or PI/lab postings appropriate to that platform and query bucket. Clearly distinguish alternate-source rows from native rows; do not double count across search queries or source families.
3. Re-anchor promising new signals to authoritative exact-role JD and usable application route. If the official page is JS-only, try another employer-published route or faithful full-JD reproduction once; record the unresolved blocker rather than claiming verification.
4. If coverage remains weak, set run_quality=PARTIAL_COVERAGE, add/update the same-platform/query `coverage_debt` with the actual next probe, and record coverage_gaps/fallback_sources in the run metrics. Zero new APPLY/CHECK then means **no verified survivors in the limited slice**, not no new roles on the market. The next run still rotates normally **and must work a previous debt before claiming completion**; do not reset the search to page one and repeat identical snippets.

**SG research recall:** Every SG run also performs a bounded current RA/RE/Research Officer lab/official-portal sweep in its research bucket **without replacing the current engineering employer-ATS probe**, including current NUS/NTU/A*STAR requisitions or PI-managed postings. Use role IDs and posted dates to find genuinely new opportunities, not just static lab homepages. Check all-Issue history before deep work; do not let unrelated university/research roles crowd out knowledge-enhanced LLM, Agent, NLP and evaluation research.

**CN access fallback:** BOSS/51job/脉脉 inaccessible does not mean no vacancies. Use bounded search-index/native alternatives (including 牛客, employer social recruiting and lab/PI direct postings), and preserve the unverified source as a coverage gap.

With two deep platform attempts per hourly run, SG/MY rotate through five platform families in at most three attempted cycles, CN through seven in at most four attempted cycles. Platform attempts are not proof that readable job rows were obtained; preserve coverage debt until supported by actual page/cursor/alternate-source evidence.

### Phase B — FreeHire triage

Execute **only** `docs/freehire-triage-consumption.md`. Normally run after Phase A. **Stall recovery exception:** when the canonical FreeHire doc identifies consecutive unpersisted SG/CN/MY candidate research, complete a validated first-shard checkpoint **before** broad Phase A discovery; only then work a bounded official-source/debt probe. If time is insufficient for the usual two-platform/owner/query rotation, preserve unattempted counters and report `PARTIAL_COVERAGE`, rather than repeating the same uncommitted candidate research next hour. Do not claim Phase A completed. A market with no unconsumed FreeHire prefix should instead favor fresh current roles and evidence-bearing due retries. The old raw-sequence recovery document is historical/audit only and is not an active hourly obligation.

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

- advance `next_platform_index` by the number of platforms actually attempted (default 2, ceiling 4), wrapping modulo platform count;
- increment `platform_cycle` on wrap;
- advance `next_owner_bucket` by official-owner buckets actually attempted (default 1, ceiling 2), modulo its count;
- advance `next_query_bucket` by query families actually attempted (default 1, ceiling 3), modulo its count;
- SG advances `next_research_bucket` by lab buckets actually attempted (default 1, ceiling 2), modulo 5;
- write `last_completed_at`, last attempted buckets/platforms, and increment `run_counter`. Preserve the existing fresh-state field types/validator contract (the legacy `last_*_bucket` fields may remain a single string). Capture all attempted buckets in the run metrics;
- read back the state before reporting success; verify any new/unresolved `coverage_debt` entries were preserved and that a claimed resolved debt has page/exhaustion/independent-source evidence.

## Health criterion

Healthy fresh discovery means:

- at least one existing coverage debt and the selected deep platform/owner/query/(SG) lab rotations are attempted, with truthful partial-coverage accounting and real role IDs/pages;
- owner/query/research buckets continue rotating;
- FreeHire runs independently under its canonical contract and any unprocessed Phase B is explicitly marked incomplete;
- verified survivors in **either engineering or research** reach APPLY/CHECK when found; measure actual new eligible unique Issues (APPLY and CHECK separately), not cursor/receipt counts.
