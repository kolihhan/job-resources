# Fresh Discovery Rotation

This is a focused execution supplement to `README.md`, `RULES.md`, and `docs/source-routing.md`.

## Problem this contract prevents

A prompt that merely says `rotate sources` is not enough. Without durable rotation state, an hourly scout can repeatedly choose the same familiar source/query family and keep rediscovering the same already-seen jobs. Fresh discovery and FreeHire backlog recovery must also have separate bounded work floors so backlog work cannot starve new-role discovery, and fresh search cannot silently replace lossless recovery.

## Authoritative fresh-rotation state

Each market owns one small mutable state file:

- SG: `discovery-state/fresh-sg.json`
- CN: `discovery-state/fresh-cn.json`
- MY: `discovery-state/fresh-my.json`

Each scout may update only its own file. The file stores **next** indexes, not last indexes. A bounded attempted rotation unit advances its corresponding next index even if it yields zero survivors; this prevents a temporarily weak or inaccessible source from pinning the scout forever. Exact opportunity state remains only in GitHub Issues.

## Two independent work floors per hourly run

Every market run has two independent phases:

### Phase A — fresh discovery floor

Complete one persisted rotation unit **before** FreeHire backlog work:

1. one official/canonical owner bucket;
2. one required broad/native surface bucket;
3. one query-family bucket;
4. SG additionally advances one research/lab bucket when the SG-RES gap pass is due.

Use the indexes from the market's fresh-state file. Do not substitute a favorite source because it is easier. After the bounded attempt, persist the next indexes and record the selections used.

Fresh discovery must use current/fresh-head or owner-delta semantics where the source supports them. The purpose is **new unique recall**, not repeatedly proving that old roles still exist.

### Phase B — FreeHire backlog floor

After Phase A, execute FreeHire recovery from the market-owned FreeHire cursor under `docs/freehire-gap-recovery.md`.

- target up to **250 global sequence numbers per run** when backlog exists;
- persist any fully handled contiguous prefix even if fewer than 250 are completed;
- other-market events are cheap skips;
- FreeHire work never satisfies the fresh-discovery floor;
- fresh discovery never satisfies FreeHire recovery.

The 250 target is a bounded catch-up target, not a requirement to overrun the execution window or deep-read every event.

## SG rotation

### Official/canonical owner buckets

0. NUS / NTU / A*STAR / AI Singapore
1. Sea / SAIL / Shopee / Grab / Singtel
2. ByteDance / TikTok / Micron
3. Google / Microsoft / Apple / OpenAI
4. strong finance / fintech AI teams and other recurring canonical owners

### Broad surface buckets

0. LinkedIn Jobs
1. JobStreet Singapore
2. Indeed Singapore
3. MyCareersFuture
4. recruiter / team / PI direct posts

### Query buckets

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

## CN rotation

### Official owner buckets

0. Alibaba / Tencent
1. ByteDance / Baidu
2. Huawei / Meituan
3. JD / Xiaohongshu
4. DeepSeek / Moonshot
5. Zhipu AI / StepFun / other strong AI-native owners

### Native surface buckets

0. BOSS直聘 + 牛客招聘
1. 猎聘 + 智联招聘
2. 前程无忧/51job + 脉脉/team-direct signals

The two members of the selected native bucket are both attempted, preserving the existing two-source-family recall floor.

### Query buckets

0. Agent / 智能体 / planning / memory / tool use
1. RAG / 知识库 / 知识图谱 / NL2SQL / Data Agent
2. 大模型评测 / Agent评测 / AI质量 / reliability
3. NLP / 检索 / 搜索 / ranking
4. AI后端 / 大模型平台 / 推理 / AI systems
5. Coding Agent / AI Coding / MCP / Skills / Harness

## MY rotation

### Official/canonical owner buckets

0. Sea / Shopee / Grab
1. Gen Digital / MoneyLion
2. AEON Bank / GXBank
3. Keysight / AMD / Intel
4. Dell / YTL AI Labs
5. MIMOS / strong university-industry research labs / other recurring destination-quality owners

### Broad surface buckets

0. LinkedIn Jobs Malaysia
1. Indeed Malaysia
2. Hiredly
3. recruiter / team posts
4. JobStreet Malaysia

### Query buckets

0. Agent / LLM / RAG / GenAI
1. NLP / search / retrieval / evaluation / knowledge
2. AI backend / platform / ML engineering
3. destination-quality backend / data / cloud / SRE / SDET
4. destination-quality full-stack / product engineering with material AI signal

## Advancement and reporting

After the fresh phase, update only the market-owned fresh-state file:

- increment each attempted `next_*_index` modulo that market's bucket count;
- write `last_completed_at`;
- record `last_owner_bucket`, `last_surface_bucket`, `last_query_bucket`, and where applicable `last_research_bucket`;
- increment `run_counter`.

A run result must name the actual owner bucket, surface bucket, query bucket, and FreeHire cursor movement. If the selected source cannot be searched, report the bounded failure and still rotate to the next source for the next hourly run; do not silently fall back to the same favorite source every hour.

## Success criterion

The system is healthy when consecutive hourly runs visibly change source/query buckets while still advancing the FreeHire cursor. Raw APPLY count is not itself a health metric, but repeated identical source selections are a routing failure.
