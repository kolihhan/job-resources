# Fresh Discovery Rotation

This is a focused execution supplement to `README.md`, `RULES.md`, and `docs/source-routing.md`.

## Goal

Fresh discovery must cover the whole relevant platform set instead of repeatedly choosing the easiest or most familiar source. A platform sweep is **exhaustive and persistent**: every listed platform is attempted once before any platform repeats.

Fresh discovery and FreeHire recovery remain separate bounded work floors so neither can starve the other.

## Authoritative state

Each market owns one mutable state file:

- SG: `discovery-state/fresh-sg.json`
- CN: `discovery-state/fresh-cn.json`
- MY: `discovery-state/fresh-my.json`

Each file stores the next platform index plus owner/query rotation state. Opportunity/application state remains only in GitHub Issues.

## Two independent phases per scout run

### Phase A — fresh discovery

Every run must complete all of the following before FreeHire work:

1. one official/canonical owner bucket;
2. the next **two individual platforms** in that market's platform sweep;
3. one query-family bucket;
4. SG additionally attempts the current research/lab bucket.

### Platform-sweep invariant

- Start at `next_platform_index`.
- Attempt two consecutive platforms in listed order, wrapping only after the final platform.
- A platform may not repeat until every other platform in the current sweep has been attempted.
- When the index wraps from the final platform to `0`, increment `platform_cycle`.
- A bounded attempted search counts as an attempt even when the platform is inaccessible, weak, or yields zero results. Record the failure; do not silently replace it with a favorite platform.
- Persist and read back fresh-state progress after the attempts.
- Fresh-head/delta semantics are preferred where supported. The goal is unique new recall, not repeatedly revalidating old roles.

With two platforms per hourly run, SG and MY finish their five-platform sweep within at most three runs; CN finishes its six-platform sweep within three runs.

### Phase B — FreeHire backlog

After Phase A, execute FreeHire recovery under `docs/freehire-gap-recovery.md` using the market-owned FreeHire cursor.

- target up to 250 global sequence numbers per run while backlog exists;
- persist every fully handled contiguous prefix;
- other-market events are cheap skips;
- FreeHire never satisfies fresh discovery, and fresh discovery never satisfies FreeHire recovery.

## SG platform sweep

In this exact order:

0. LinkedIn Jobs Singapore
1. JobStreet Singapore
2. Indeed Singapore
3. MyCareersFuture
4. recruiter / team / PI direct posts

### SG official/canonical owner buckets

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

In this exact order:

0. BOSS直聘
1. 牛客招聘
2. 猎聘
3. 智联招聘
4. 前程无忧 / 51job
5. 脉脉 / team-direct recruiting signals

The platform sweep replaces the old paired native-surface buckets. Two individual platforms are attempted each run, so every six-platform sweep completes within three runs.

### CN official owner buckets

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

In this exact order:

0. LinkedIn Jobs Malaysia
1. JobStreet Malaysia
2. Indeed Malaysia
3. Hiredly
4. recruiter / team / direct hiring posts

### MY official/canonical owner buckets

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

After Phase A, update only the market-owned fresh-state file:

- advance `next_platform_index` by the number of attempted platforms, wrapping modulo platform count;
- increment `platform_cycle` on each wrap;
- increment `next_owner_bucket` and `next_query_bucket` modulo their counts;
- SG also increments `next_research_bucket` modulo 5;
- write `last_completed_at`;
- record `last_platforms`, `last_owner_bucket`, `last_query_bucket`, and SG `last_research_bucket`;
- increment `run_counter`;
- read the state file back before reporting success.

A run result must name every platform actually attempted, not just a generic source family.

## Health criterion

The system is healthy when:

- no platform repeats before the current market sweep is complete;
- each market completes a full platform sweep within at most three successful hourly runs;
- owner/query buckets continue rotating;
- FreeHire recovery continues independently;
- new verified survivors are durably handed off to APPLY/CHECK when found.
