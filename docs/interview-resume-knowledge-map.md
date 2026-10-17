# Resume Interview Knowledge Map — Applied AI / Backend

Last audited: 2026-10-18

Primary immediate use: Ant International Malaysia — Applied AI Engineer (Fresh Graduate) technical interview preparation.

This is the interview source of truth for what the current resume claims, what the repositories actually support, what must be understood, and what must not be overstated.

---

## 1. Audit scope

Current resume source:

- `resumes/resume-en-current.md`

Repository snapshots audited:

- `kolihhan/semantic-text2sql-agent` — main `2be1b2a09454788eca8b6b1a6233ee69a16a465d`
- `kolihhan/local-rag-search` — main `02fedfff44249e21fe3089a6aad35ff8267b3c39`
- `kolihhan/hermes-video-tutor` — main `22a9b3044695cef421feec2dd36938149d2038cc`
- `kolihhan/master-thesis` — main `f134750441dee036269ffe9e378fb9116ac7bdf9`

Coverage standard:

- Full repository trees inventoried for all four repositories.
- Interview-relevant runtime/source modules, canonical evaluation artifacts, architecture/pipeline docs and representative high-risk tests deep-read.
- Historical experiments, notebooks, fixtures, workflows and binary/model/data artifacts are inventoried where visible, but not every historical notebook cell or binary artifact is treated as semantically reviewed source code.
- `Understand Anything` methodology is used for component → dependency → data-flow explanation. Its generated knowledge-graph workflow was not literally available because these repositories do not contain a current `.ua/knowledge-graph.json` / `.understand-anything/knowledge-graph.json`.
- `get-job.skill` evidence discipline is used: **resume claim → likely drill → required knowledge → evidence → safe claim / red line**.

Evidence labels:

- **CODE** — directly supported by current implementation.
- **EVAL** — supported by checked-in evaluation/report artifacts.
- **RESUME** — present on the submitted resume.
- **USER** — depends on personal recollection, mainly company-internal work.

---

## 2. Interview priority

### P0 — must be solid

1. Text-to-SQL: architecture, validation, repair, safety, metrics, failure modes.
2. Kahap production work: personal ownership, debugging, DB issues, queues/workers/schedulers, migration/deployment.
3. AI-native engineering: context/constraints → AI assistance → inspect → test → edge cases → verify.
4. Backend/DB fundamentals: APIs, SQL, timeouts, retry, idempotency, transactions, indexes.

### P1 — strong working knowledge

5. Hybrid retrieval: BM25, dense embeddings, RRF, Recall/MRR/Hit@K, trade-offs.
6. Video QA agent: tool calling, ownership boundary, evidence/citations, routing, abstention.
7. M.S. thesis: full pipeline, Role KG, Context KG, DualKG Top1, semantic F1 and limitations.
8. Python engineering fundamentals.

### P2

9. General concurrency/locking/distributed-systems fundamentals.
10. Java-specific internals only if interviewer explicitly moves there.

---

## 3. Resume claim coverage

| Resume area | Evidence | Main drill |
|---|---|---|
| Kahap feedback platform end-to-end | RESUME + USER | What exactly did you own? Architecture? Production failure? |
| Kahap app/DB troubleshooting | RESUME + USER | Show one real incident and diagnosis sequence |
| Queue/worker/scheduler/migration/SSL | RESUME + USER | Why async? retries? duplicate jobs? cutover/rollback? |
| Pac Com POS | RESUME + USER | One real feature and full request/data flow |
| Text-to-SQL validation + repair | CODE | Exact flow, verifier, safety, repair budget |
| Text-to-SQL 75→90 executable; +6 correct | EVAL | Execution success vs semantic correctness |
| Hybrid BM25 + Dense + RRF | CODE | Why hybrid? Why RRF instead of averaging scores? |
| RAG Recall@10/MRR@20 result | EVAL | Metric definitions, benchmark scope, trade-offs |
| Video transcript/frame/clip tools | CODE | Who owns agent loop? Evidence flow? |
| Video 4/6 visual-required result | EVAL | Evaluation contract and limitations |
| Thesis Role KG / Context KG / DualKG | CODE + EVAL | Exact retrieval/fusion logic and result interpretation |

---

# 4. Project 1 — Text-to-SQL with Verification & Repair

## Mental model

> Generate SQL from database schema context, deterministically reject unsafe/invalid SQL, provide bounded repair feedback, then execute through a read-only SQLite boundary.

## Supported main path — CODE

```text
question
→ DatabaseCatalog reads tables / columns / foreign keys
→ LLM generates SQL
→ deterministic verifier
   → pass: read-only execute
   → fail: bounded repair → verify again
→ refuse if verification still fails
```

Important boundaries:

- `SemanticSQLService` is the application boundary.
- `catalog.py` reads SQLite schema metadata.
- LangGraph owns routing and bounded repair.
- deterministic verifier checks validity/safety.
- execution layer enforces read-only access.

Default repair budget: **2**.

## Safety / verifier

Know:

- one statement only
- `SELECT` / CTE boundary
- reject write/non-read-only SQL
- catch compilation/reference errors using SQLite preflight / `EXPLAIN QUERY PLAN`
- read-only defense includes `mode=ro`, `PRAGMA query_only`, and SQLite authorizer controls

Key concept:

> A prompt is not a security boundary.

The verifier does **not** prove that a valid query answers the user's intended question.

## Canonical result — EVAL

100 frozen BIRD DEV queries, Qwen3.5 9B:

- Direct EX-compatible correctness: **33%**
- Guarded + repair: **39%**
- Direct execution success: **75%**
- Guarded conservative execution success: **90%**
- wrong → correct: **6**
- correct → wrong: **0**

**90% is execution success, not Text-to-SQL accuracy.**

## Negative ablation

Optional semantic revision:

- 39% → 38% EX
- 0 wrong→correct
- 1 correct→wrong

Correct story: it did not earn its complexity, so it was not promoted.

## Resume/code mismatch — RED FLAG

Current resume says:

> “uses database schema and values to generate SQL”

The current supported `SemanticSQLService` passes `catalog.schema_text()` into the guarded path. The repo also contains a separate value/schema grounding experiment, but that is not the default supported main path.

For an already-submitted resume, safest interview explanation:

> “The main guarded path uses live schema introspection. I also implemented/experimented with value-aware grounding separately, but I keep that distinct from the headline guarded benchmark.”

Do not claim the 33→39 benchmark depends on DGSL/value grounding unless you can point to the exact experimental arm.

---

# 5. Project 2 — Hybrid Retrieval for RAG

## Mental model

> BM25 catches exact lexical signals, dense retrieval catches semantic paraphrases, and RRF fuses ranks without comparing incompatible raw score scales.

## CODE

```text
query
├─ BM25
└─ Qwen3-Embedding-0.6B dense retrieval
        ↓
     RRF (k=60)
        ↓
 ranked documents + rank provenance
```

BM25 implementation uses `k1=1.5`, `b=0.75`.

Dense path:

- Qwen3-Embedding-0.6B
- 1024 dimensions
- local L2 normalization
- dot product; for normalized vectors this equals cosine similarity

RRF:

```text
score(doc) = Σ 1/(k + rank_i(doc))
```

Why RRF rather than raw-score average: BM25 scores and embedding similarities have different scales and meanings.

## Canonical EVAL

EnterpriseRAG-Bench v1.0.0, 64 compatible Confluence-only queries, 5,189 docs:

| Arm | Recall@10 | MRR@20 | Hit@10 |
|---|---:|---:|---:|
| BM25 | 0.7341 | 0.6792 | 0.7969 |
| Dense | 0.6797 | 0.6919 | 0.7656 |
| Hybrid RRF | **0.7630** | **0.7418** | **0.8438** |

Hybrid helped on this frozen slice; it is not universally superior.

RED LINE:

- canonical benchmark does not use HyDE, generation, agent or neural reranker
- demo reranker is lightweight token overlap, not a cross-encoder
- retrieval improvement does not automatically prove better final generated answers

---

# 6. Project 3 — Multimodal Video QA Agent

## Mental model

> Search transcript when text evidence is enough; inspect actual frames/clips only when visual evidence is required.

## Ownership boundary — critical

Hermes owns:

- observe/act loop
- model/tool dispatch
- deciding which exposed tool to call

This repo owns:

- `search_transcript`
- `expand_context`
- `inspect_frame`
- `inspect_clip`
- transcript BM25 retrieval
- FFmpeg frame sampling
- evidence IDs/store
- activity trace
- strict answer/citation contract
- fail-closed abstention
- evaluation harness and integration

Do not say you implemented Hermes core from scratch.

## Canonical EVAL

Frozen self-authored 12-case product evaluation:

- 6 transcript-answerable
- 6 visual-required
- multimodal strict full pass: **50%**
- visual-required strict pass: **4/6 = 66.7%**
- visual-tool use on visual-required: **100%**
- unnecessary visual tool calls on transcript-answerable: **0% in that frozen run**

This is a narrow product/system experiment, not a broad video-QA benchmark.

---

# 7. Work Experience — Kahap / Pac Com

These remain **RESUME + USER** because public GitHub does not prove internal company implementation.

## Kahap feedback platform

Be able to explain:

- business problem and users
- architecture/request flow
- submission workflow
- notifications
- admin operations
- what you personally designed vs inherited
- deployment environment
- one production issue
- one DB issue
- one thing you would redesign now

Five-whys pattern:

```text
“Led end-to-end development”
→ what did end-to-end mean?
→ architecture?
→ why Laravel/Vue?
→ what failed?
→ how did you diagnose it?
→ how did you verify the fix?
```

## Queue / worker / scheduler

- Queue = stores asynchronous work.
- Worker = consumes queued jobs.
- Scheduler = triggers jobs/tasks by time/interval.
- Failure modes: worker crash, duplicate/retried jobs, stuck queue, poison job.
- Retry can duplicate side effects; idempotency matters.

## Migration / DB troubleshooting

Have one real story for each:

```text
migration: before → plan → risk → backup → cutover → verify → rollback
DB issue: symptom → logs/reproduce → app vs DB → query/data/schema → root cause → fix → verify → prevention
```

---

# 8. M.S. Thesis — CODE + EVAL audited

Repo: `kolihhan/master-thesis`.

Resume title:

> Interpreting Implicit Intent through Workplace Hierarchies and Context

Resume result:

> role-based retrieval `0.6440 → 0.6793`; role+context evidence `0.6819` on 400 held-out examples.

These numbers are directly supported by the checked-in final report after rounding:

- baseline target-only: **0.643971**
- Role KG target-only: **0.679274**
- DualKG Top1 target-only: **0.681947**

## 8.1 Clean pipeline — CODE

The current clean pipeline spec is:

```text
1. State Extraction
2. GCN Embedding
3. HeCo / ARD preparation
4. Cluster
5. Knowledge Graph
6. Role KG
7. Context KG
8. DualKG Top1 fusion
9. Evaluation with utterance-aligned preceding context
10. Evaluation target-only
11. Final comparison
```

Main generation model in the clean spec:

- `llama3.1:8b-instruct-q8_0`
- seed 42
- temperature 0
- three responses

## 8.2 State extraction / representation

High-level flow:

- clean raw posts/dialogues
- extract interpersonal relations
- aggregate relation labels and topic tags
- generate speaker/listener state descriptions with LLaMA
- transform states to graph-training format
- train/export graph-based state representations

Current Role/Context pipelines expect frozen add-listener GCN embeddings with dimension **600**.

Interview explanation:

> “Instead of treating an utterance as isolated text, I built representations of speaker/listener states and retrieved evidence from structurally similar workplace interactions.”

## 8.3 Role KG — current clean implementation

The clean Role pipeline uses:

- evidence rows grouped/clustering by normalized workplace relation
- frozen GCN state embeddings
- MiniLM dialogue embeddings using `paraphrase-multilingual-MiniLM-L12-v2`
- same-source-post exclusion to reduce leakage

Dialogue candidate score:

```text
0.6 * dialogue cosine similarity + 0.4 * role-pair match
```

Role match is strongest for same speaker/listener role pairing, lower for reversed/partial overlap.

Then:

1. take top dialogue candidates
2. collect their selected relation clusters
3. rank candidate states using GCN embedding similarity
4. prefer the target speaker/listener role
5. produce bounded speaker/listener clue lists

Important: be able to explain **text similarity + structural role signal + graph/state similarity** as separate signals.

## 8.4 Context KG — current clean pipeline

Context groups are built from:

```text
normalized_relation | communicative_purpose
```

Communicative purposes include categories such as pressure, refusal, deflection, compliance, risk mitigation and neutral coordination.

The current clean script:

- builds context-key clusters using GCN state embeddings
- represents evidence/relation/purpose/context-key/cluster as typed nodes/edges
- excludes evidence from the same source post during retrieval
- ranks by a mixture of GCN-state semantic similarity and context/relation match
- prefers the relevant interlocutor role

### Historical-doc warning

`Context_Cond/README.md` and `context_cond_status.json` describe an older Task108/109 branch using `0.80 * dialogue cosine + 0.20 * role-pair match`. The later clean pipeline spec and clean script define the cleaned final pipeline used for the final report.

Do not mix the historical Task108/109 retrieval description with the cleaned final implementation when explaining the final thesis.

## 8.5 DualKG Top1 — very important

Current final fusion is **not RRF/P2Q** and not a simple Role Top1 + Context Top1 merge.

The checked-in builder states the identity explicitly:

```text
Task35 graph-policy Role backbone
+ Context KG rank-1 evidence per side
+ append only if unique
+ maximum 10 states per side
```

Therefore if asked “How did you combine role and context?” say:

> “The final DualKG kept the regenerated Task35 role graph-policy evidence as the backbone, then conditionally appended the top Context-KG clue for each side without exceeding the fixed evidence budget.”

## 8.6 Evaluation design — EVAL

Final primary evaluation has two arms using the same selected targets/model/scorer:

1. **Utterance-aligned preceding context** — target + only source-post text before the aligned target unit.
2. **Target-only** — target utterance with no post context.

Upstream graph construction uses 401 targets; primary evaluation is capped at **400**.

Preceding-context alignment audit:

- exact: 218
- fuzzy: 132
- ambiguous: 6
- unmatched: 44
- usable: 350/400

The automatic pseudo-reference comes from the complete post; this is an explicit limitation.

## 8.7 Final results — EVAL

### Target-only — this is the resume headline

| Method | F1 |
|---|---:|
| Baseline | **0.643971** |
| Context KG | 0.664568 |
| Old PRKG best | 0.677335 |
| Role KG | **0.679274** |
| DualKG Top1 | **0.681947** |

Thus resume rounding `0.6440 → 0.6793 → 0.6819` is supported.

### Utterance-aligned preceding context

| Method | F1 |
|---|---:|
| Baseline | 0.680288 |
| Context KG | 0.680139 |
| Old PRKG best | 0.684936 |
| Role KG | 0.687634 |
| DualKG Top1 | 0.691147 |
| Empty-clue protocol control | **0.704428** |

Important nuance:

> DualKG is best in the target-only method table, but the empty-clue protocol control scored higher in the preceding-context arm. Do not claim DualKG is globally the best condition across every evaluation arm.

## 8.8 Semantic F1 scorer

The thesis evaluator follows the existing semantic precision/recall/F1 protocol:

- parse generated answer items
- normalize/strip role labels
- compare generated items and pseudo-reference items using MiniLM sentence embeddings
- compute semantic precision, recall and F1

So when explaining `F1`, do not present it as exact-label classification macro-F1 unless discussing a different experiment. The checked-in final report is a semantic response-matching F1 evaluation.

## 8.9 Thesis likely drill tree

Be ready for:

1. What is “implicit intent” in one concrete workplace example?
2. Why does workplace role/hierarchy matter?
3. What are speaker/listener states?
4. Why use graph/state embeddings instead of only sentence similarity?
5. Explain Role KG retrieval step-by-step.
6. What changes in Context KG?
7. What exactly is a communicative purpose?
8. Why exclude the same source post from retrieval?
9. How exactly is DualKG Top1 fused?
10. Why target-only baseline 0.644 but preceding-context baseline 0.680?
11. Why is the empty-clue control strong in the preceding-context arm?
12. What does semantic F1 measure?
13. What are the limitations of using a pseudo-reference generated from the complete post?
14. What would you change if rebuilding the thesis today?

## 8.10 Thesis red lines

Do **not** say:

- “DualKG uses RRF.”
- “DualKG is simply Role Top1 + Context Top1.”
- “0.6819 is accuracy.”
- “0.6819 proves universal understanding of workplace intent.”
- “Context always helps.”
- “DualKG was the best result in every arm.”
- “The final clean Context KG is exactly the old Task108/109 README path.”
- “The evaluation has a human gold label for every generated semantic state.”

---

# 9. Foundation knowledge checklist

## Python

- [ ] list / tuple / set / dict
- [ ] average dict/set lookup complexity
- [ ] mutability / hashability
- [ ] exceptions and failure boundaries
- [ ] dataclass / type hints / Protocol
- [ ] file/JSON processing
- [ ] subprocess timeout/error handling

## Backend/API

- [ ] request → validation → service → DB/dependency → response
- [ ] GET vs POST
- [ ] 2xx / 4xx / 5xx
- [ ] retries and timeouts
- [ ] idempotency
- [ ] sync vs queued/background work
- [ ] health checks

## Database

- [ ] primary vs unique key
- [ ] foreign key
- [ ] index trade-offs
- [ ] JOIN / GROUP BY / aggregates
- [ ] transactions / ACID intuition
- [ ] locks/concurrency basics
- [ ] SQL injection
- [ ] least privilege/read-only DB access

## Reliability

- [ ] timeout ≠ confirmed failure
- [ ] retries can duplicate side effects
- [ ] idempotency/deduplication
- [ ] queues/workers
- [ ] bounded retry/backoff
- [ ] fail closed vs silently wrong

## Retrieval/AI

- [ ] BM25
- [ ] embeddings / cosine similarity
- [ ] RRF
- [ ] Recall@K / Hit@K / MRR
- [ ] retrieval vs generation failure
- [ ] tool calling vs fixed workflow
- [ ] evidence grounding
- [ ] abstention
- [ ] evaluation design / ablations

---

# 10. Recommended drill order

1. **Text-to-SQL** — 60-second explanation → five-whys → safety → metrics → failure cases.
2. **Kahap production engineering** — architecture → incident → queues → DB → migration.
3. **Thesis** — explain full idea in plain English → Role KG → Context KG → DualKG → metrics/limitations.
4. **Hybrid RAG** — BM25 → dense → RRF → metrics/trade-offs.
5. **Video QA / agent** — ownership → tools → evidence → abstention → evaluation.
6. **Backend + DB scenario questions**.
7. **Full Ant-style mixed mock**.

---

# 11. Mastery gate

A resume bullet is interview-ready only if:

- [ ] I can explain it in 30–60 seconds.
- [ ] I can describe the architecture/data flow.
- [ ] I can explain why the design was chosen.
- [ ] I can name a failure mode.
- [ ] I can explain a trade-off.
- [ ] I can explain the metric without exaggeration.
- [ ] I can say exactly what I personally did.
- [ ] I can say what I would improve next.
- [ ] I can separate CODE/EVAL evidence from personal recollection.

---

# 12. Remaining evidence gaps / cleanup items

1. **Kahap / Pac Com internal work** still depends on real personal examples; do not invent details.
2. **Text-to-SQL resume wording “schema and values”** is broader than the current supported main-path implementation; prepare the distinction between main schema-grounded path and separate value-grounding experiment.
3. Thesis repo contains substantial historical Task/investigation material alongside the cleaned final pipeline. For interview answers, prioritize `Evaluate/CLEAN_THESIS_PIPELINE.md`, the current clean Role/Context/DualKG code, and `Evaluate/results/THESIS_PIPELINE_FINAL_REPORT.md`.
4. Not every historical notebook cell or LFS/binary/model artifact is semantically deep-read; those are not needed to defend the submitted resume claims.

Never fill a gap by guessing.

---

## Current study starting point

Start with **Text-to-SQL**, then thesis is now fully in scope for drilling.

First question:

> “Can you walk me through your Text-to-SQL project and explain why you added deterministic verification and bounded repair instead of just prompting the model to generate better SQL?”
