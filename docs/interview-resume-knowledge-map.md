# Resume Interview Knowledge Map — Applied AI / Backend

Last audited: 2026-10-17

Primary immediate use: Ant International Malaysia — Applied AI Engineer (Fresh Graduate) technical interview preparation.

This file is the interview source-of-truth for **what is on the current resume, what the repositories actually prove, what must be understood, what may be asked, and what must not be overstated**.

---

## 1. Audit scope and evidence standard

Current resume source:

- `resumes/resume-en-current.md`

Repository snapshots audited:

- `kolihhan/semantic-text2sql-agent` — main `2be1b2a09454788eca8b6b1a6233ee69a16a465d`
- `kolihhan/local-rag-search` — main `02fedfff44249e21fe3089a6aad35ff8267b3c39`
- `kolihhan/hermes-video-tutor` — main `22a9b3044695cef421feec2dd36938149d2038cc`

Coverage:

- **Full repository trees inventoried** for all three public project repos.
- **All interview-relevant runtime source modules deep-read**.
- Architecture/design docs, canonical evaluation artifacts, and representative/high-risk tests deep-read.
- Tests, workflows, historical experiments, fixtures, and assets were inventoried; only interview-relevant ones were deep-read.
- Binary/static artifacts such as `.mp4`, `.db`, and images are recorded as repo contents but are not treated as semantically reviewed source code.
- `Understand Anything` was used as a methodology for component/data-flow/dependency explanation. Its own knowledge-graph workflow could not literally run because these repos do not contain `.ua/knowledge-graph.json` / `.understand-anything/knowledge-graph.json`.
- `get-job.skill` evidence discipline is applied here: **resume bullet → likely drill → required knowledge → evidence → safe claim / red line**.

Evidence levels used below:

- **CODE** — directly supported by current repository implementation.
- **EVAL** — supported by checked-in canonical evaluation/report artifact.
- **RESUME** — present in current resume but not independently proven by these public repos.
- **USER** — requires personal recollection/explanation from actual work or thesis.

---

## 2. Interview priority map

### P0 — must be solid

1. **Text-to-SQL project** — architecture, verification, repair, safety, evaluation, failure modes.
2. **Kahap production experience** — what you personally built, production debugging, DB issues, queue/worker/scheduler, deployment/migration.
3. **AI-native engineering** — how you use AI tools while retaining engineering judgment: context, constraints, review, tests, edge cases, verification.
4. **Backend fundamentals** — API, DB, SQL, retries/timeouts, idempotency, debugging.

### P1 — strong working knowledge

5. **Hybrid Retrieval for RAG** — BM25, dense embeddings, cosine/dot product, RRF, Recall/MRR/Hit@K, trade-offs.
6. **Multimodal Video QA Agent** — tool calling, ownership boundary, evidence/citations, routing, abstention, evaluation.
7. **Python engineering** — core collections, complexity, exceptions, typing/dataclasses/protocols, clean service boundaries.

### P2 — know enough to defend resume

8. **M.S. thesis** — problem, graph/retrieval idea, metrics, why hierarchy/context helps, limitations.
9. **General CS/reliability** — concurrency basics, locks, queue semantics, transactions, indexing.
10. **Java-specific internals** — lower priority unless interviewer explicitly moves there.

---

## 3. Current resume coverage matrix

| Resume area | Evidence | Likely interviewer drill | Required mastery |
|---|---|---|---|
| Kahap feedback platform end-to-end | RESUME + USER | What did you personally own? Architecture? Hardest production issue? | Laravel/Vue request flow, DB, deployment, production debugging |
| Kahap app/DB issues | RESUME + USER | Example incident, diagnosis sequence, root cause, prevention | logs, SQL, migrations, transactions/index basics |
| Queue/worker/scheduler/server migration/SSL | RESUME + USER | Why queue? worker failure? scheduler vs queue? migration risk? | async jobs, retries, idempotency, process supervision, deployment basics |
| Pac Com POS | RESUME + USER | What feature? data flow? production constraint? | Laravel/Vue/DB fundamentals |
| Text-to-SQL generation + verification + repair | CODE | Walk through exact flow; why each stage? | schema grounding, LangGraph routing, verifier, repair budget, read-only execution |
| Text-to-SQL 75→90 executable; +6 correct | EVAL | What exactly do these metrics mean? | execution success vs semantic correctness; paired evaluation |
| Hybrid BM25 + Dense + RRF | CODE | Why hybrid? Why RRF? Why not average scores? | BM25, embeddings, L2 normalization, dot/cosine, rank fusion |
| RAG Recall@10 / MRR@20 gains | EVAL | Define metrics; dataset scope; trade-off | retrieval metrics and limitations |
| Video QA transcript/frame/clip routing | CODE | Who decides which tool? Did you build the agent loop? | Hermes ownership boundary, tool surface, evidence pipeline |
| Video QA 4/6 visual-required | EVAL | How measured? Why only 12? | strict evaluation contract, limitations, modality/evidence timing |
| Thesis graph-aware retrieval | RESUME + USER | Why graphs? How constructed? What changed over baseline? | retrieval design, role/context evidence, F1, limitations |

---

# 4. Project 1 — Text-to-SQL with Verification & Repair

## 4.1 One-line mental model

> Generate SQL from the real schema, **deterministically reject unsafe/invalid SQL**, give bounded repair feedback when needed, then execute through a read-only SQLite boundary.

## 4.2 Actual current flow — CODE

```text
Question
  ↓
DatabaseCatalog introspects SQLite
  ↓
Schema context: tables + columns + foreign keys
  ↓
LLM generates one SQL candidate
  ↓
Deterministic preflight verification
  ├─ pass → execute read-only
  └─ fail → repair with verifier errors → verify again
                  ↓
           repair budget exhausted
                  ↓
                refuse
```

Important implementation ownership:

- `agent.py` — `SemanticSQLService`, application boundary.
- `catalog.py` — reads `sqlite_master`, `PRAGMA table_info`, `PRAGMA foreign_key_list`.
- `direct.py` — initial model generation prompt.
- `inference.py` — LangGraph state/routing and bounded repair loop.
- `verifier.py` — deterministic preflight.
- `execution.py` — read-only enforcement and bounded result fetch.
- `providers.py` — model-provider abstraction; Ollama vs deterministic offline demo provider.

Default repair budget: **2**.

## 4.3 What verifier actually checks — CODE

Know this without hand-waving:

- empty SQL
- multiple statements
- prose/comments mixed with SQL
- only one `SELECT` or `WITH` query allowed
- explicit write/non-read-only operations rejected
- SQLite compilation/schema-reference problems caught using `EXPLAIN QUERY PLAN`

The verifier **does not prove semantic correctness**.

Example:

```text
Question: list members who attended October Meeting
Generated SQL: valid, safe, executes, returns rows
But: it can still answer the wrong relation/filter
```

That distinction is central to the project.

## 4.4 Read-only defense in depth — CODE

Execution does not merely trust the prompt.

Three important layers:

1. SQLite URI `mode=ro`
2. `PRAGMA query_only = ON`
3. SQLite authorizer denies write actions

Plus the application only permits a single `SELECT` / CTE.

Interview concept: **defense in depth** — a model instruction is not a security boundary.

## 4.5 Canonical result — EVAL

Frozen 100 BIRD DEV queries using Qwen3.5 9B:

- Direct BIRD EX-compatible correctness: **33%**
- Guarded + repair: **39%**
- Direct execution success: **75%**
- Guarded conservative execution success: **90%**
- Wrong → correct: **6**
- Correct → wrong: **0**

Resume wording emphasizes 75→90 executable and +6 correct recoveries.

### Must distinguish

**90% is NOT Text-to-SQL accuracy.**

- execution success = SQL can run successfully
- EX-compatible match = result matches expected execution result under evaluator contract

A syntactically valid query can still be semantically wrong.

## 4.6 Why deterministic verification instead of another LLM?

Good answer structure:

- Syntax/read-only/compiler failures are objectively checkable.
- Deterministic checks are cheaper and inspectable.
- They give concrete failure feedback to repair.
- An LLM judge adds another uncertain model decision.
- Semantic correctness remains harder and requires proper evaluation.

## 4.7 Why bounded repair?

Know the engineering reason:

- Prevent unbounded agent loops.
- Cap latency/cost.
- Make failure behavior predictable.
- If deterministic failures remain after the budget, refuse rather than execute unsafe/broken SQL.

## 4.8 Experimental semantic revision — RED LINE

An optional semantic reviewer was tested for projection, aggregation/grain, join, filter/value, and order/top-k mistakes.

Result:

- guarded baseline EX: **39%**
- + semantic revision: **38%**
- wrong → correct: **0**
- correct → wrong: **1**

Therefore it was **not promoted**.

Good engineering lesson:

> More model calls do not automatically improve a system. Run an ablation; keep the simpler path when evidence says the extra layer does not earn its complexity.

## 4.9 Experimental DGSL grounding — RED LINE

The repo contains a separate schema/value-grounding experiment with decomposition, value matching, column/table scoring and FK bridges.

It is **not the default `SemanticSQLService` path**.

Do not say the default production/demo flow uses DGSL or value grounding unless explicitly discussing that experiment.

## 4.10 Likely drill tree

Be able to answer progressively:

1. What problem does the system solve?
2. Walk me through the architecture.
3. How do you give schema context to the model?
4. Why can SQL execute but still be wrong?
5. What exactly does verification check?
6. Why `EXPLAIN QUERY PLAN`?
7. How do you prevent generated SQL from modifying the database?
8. Why max two repairs?
9. What is BIRD EX?
10. Why did execution improve more than correctness?
11. What failed in semantic revision?
12. What would you improve next?

### Red-line claims

Do **not** say:

- “90% Text-to-SQL accuracy.”
- “Semantic revision improved the model.”
- “DGSL improved final correctness.”
- “The offline demo provider produced benchmark results.”
- “The current 9B result has a verified clean end-to-end successful canonical GitHub Actions run.”

---

# 5. Project 2 — Hybrid Retrieval for RAG

## 5.1 One-line mental model

> BM25 catches exact lexical signals, dense embeddings catch semantic paraphrases, and RRF combines their **ranks** without pretending their raw score scales are comparable.

## 5.2 Actual flow — CODE

```text
Query
  ├─ BM25 lexical retrieval
  └─ Qwen dense retrieval
          ↓
       RRF fusion
          ↓
     ranked results
          ↓
rank provenance: BM25 rank / dense rank / RRF rank
```

The service also supports typed lexical/vector/HyDE signals and an optional bounded reranker, but those are **not part of the canonical benchmark claim**.

## 5.3 BM25 — must understand

ELI5:

- words appearing in the query and document add score
- rare words matter more than common words
- repeated terms help but with diminishing returns
- document length is normalized

Current implementation uses typical parameters:

- `k1 = 1.5`
- `b = 0.75`

Useful example:

- `ORA-12516` → lexical retrieval is often excellent because exact identifiers matter.

## 5.4 Dense retrieval — must understand

Canonical serious path uses:

- `Qwen/Qwen3-Embedding-0.6B`
- 1024-dimensional vectors
- query instruction for retrieval
- local L2 normalization
- dot product for similarity

If two vectors are L2-normalized, their dot product is equivalent to cosine similarity.

Useful example:

```text
Query: buyers could not finish purchase
Document: payment authorization requests were rejected
```

Few exact words may overlap, but semantic embeddings may place them near each other.

## 5.5 Why RRF instead of averaging scores?

This is a likely interview question.

BM25 score and embedding similarity are on different scales. Raw `12.7` from BM25 and `0.82` from dense retrieval do not mean comparable quantities.

RRF ignores raw magnitude and combines rank positions:

```text
RRF(doc) = Σ 1 / (k + rank_i(doc))
```

Canonical experiment uses `k = 60`.

A document ranking highly in both lists accumulates more RRF score.

## 5.6 Canonical result — EVAL

EnterpriseRAG-Bench v1.0.0, **64 official compatible Confluence-only queries**, 5,189 documents:

| Arm | Recall@10 | MRR@20 | Hit@10 |
|---|---:|---:|---:|
| BM25 | 0.7341 | 0.6792 | 0.7969 |
| Qwen Dense | 0.6797 | 0.6919 | 0.7656 |
| Hybrid RRF | **0.7630** | **0.7418** | **0.8438** |

Hybrid recovered 5 BM25 top-10 misses but also lost 2 BM25 top-10 hits.

Correct conclusion:

> Hybrid helped on this frozen evaluation; it is not universally superior.

## 5.7 Metrics — must explain simply

### Recall@10

Of all relevant documents, how many appear in the top 10?

### Hit@10

Did at least one relevant document appear in the top 10?

### MRR@20

How early does the **first relevant document** appear, capped at top 20?

Rank 1 is much better than rank 10.

## 5.8 Embedding cache — useful engineering depth

The dense index cache records:

- cache schema version
- provider/model identity
- corpus identity
- document IDs
- vector count/dimension

The implementation validates compatibility and writes cache files atomically.

Why it matters:

- embeddings are expensive to recompute
- stale vectors are dangerous
- model/corpus identity must match the cache

## 5.9 Reranker — RED LINE

Current default reranker is a deterministic **token-overlap** implementation for the offline/demo surface.

It is not a neural cross-encoder.

The canonical 64-query benchmark does **not** use reranking, HyDE, generation, or an agent.

### Red-line claims

Do **not** say:

- “This is the full EnterpriseRAG-Bench leaderboard result.”
- “Hybrid is always better.”
- “The benchmark used a reranker.”
- “The benchmark used HyDE / generation / agents.”
- “Better retrieval proves the generated RAG answer is better.”
- “The current reranker is a neural reranker.”

---

# 6. Project 3 — Multimodal Video QA Agent

## 6.1 One-line mental model

> Let the agent use transcript evidence when that is enough, and only inspect frames/clips when the question actually needs visual evidence.

## 6.2 Ownership boundary — critical

**Hermes owns:**

- observe/act loop
- model/tool dispatch
- deciding which exposed tool to call

**This project owns:**

- domain tool definitions
- transcript retrieval
- frame/clip extraction
- evidence storage and IDs
- activity tracing
- strict answer/citation contract
- fail-closed validation/abstention
- evaluation harness
- CLI/UI integration

Do not claim you implemented the Hermes core agent loop from scratch.

## 6.3 Four domain tools — CODE

1. `search_transcript(query, top_k)`
2. `expand_context(segment_id)`
3. `inspect_frame(timestamp_s)`
4. `inspect_clip(start_s, end_s, frame_count)`

`transcript_only` mode exposes only the first two. `multimodal` mode also exposes visual tools.

There is no hard-coded `search → frame → clip` workflow.

## 6.4 Transcript retrieval

Transcript segments are searched with BM25.

`expand_context` retrieves neighboring transcript segments by time window.

## 6.5 Visual inspection

FFmpeg extracts:

- one requested frame, or
- a bounded set of sampled frames from a short clip

Important: this is **sampled-frame inspection**, not native long-video ingestion.

Budgets include max clip duration and max frame count.

## 6.6 Evidence contract and abstention

Every tool result becomes evidence such as `E1`, `E2` with:

- modality (`transcript`, `frame`, `clip`)
- start/end timestamp
- text/metadata
- media paths where relevant

The final runtime format is constrained to roughly:

```text
FINAL: <short answer> [E#]
```

If the answer format is invalid, citations refer to unknown evidence, or the model explicitly reports insufficient evidence, `TutorService` fails closed to an abstention response.

## 6.7 Canonical evaluation — EVAL

Frozen 12-question self-authored product-oriented fixture:

- 6 transcript-answerable
- 6 visual-required

Canonical v2 multimodal result:

- strict full pass overall: **50%**
- visual-required strict full pass: **66.7% = 4/6**
- visual tool use on visual-required: **100%**
- unnecessary visual-tool calls on transcript-answerable: **0% in this frozen run**

The evaluator separates:

- answer correctness
- citation validity
- required modality
- evidence-time-window correctness

## 6.8 Post-hoc evaluator fix — RED LINE

A later corrected evaluator re-scored preserved outputs and produced a stronger diagnostic result.

That is **not a fresh end-to-end run** and is not promoted over the original canonical v2 headline.

Keep resume claim at **4/6 visual-required**.

### Red-line claims

Do **not** say:

- “I implemented Hermes’ whole agent loop.”
- “The model consumes arbitrary long video natively.”
- “The 12-question fixture is a broad video-QA benchmark.”
- “The canonical result is 6/6 visual questions.”
- “The agent never makes unnecessary visual calls in general.”

---

# 7. Work experience — Kahap / Pac Com

Public GitHub cannot independently prove company-internal work, so these are **RESUME + USER evidence**. The goal is to make every bullet defensible from real memory, not invent details.

## 7.1 Kahap feedback platform

Must be able to explain:

- What problem the platform solved.
- Main user roles.
- Basic architecture and request/data flow.
- What you personally designed vs inherited.
- Submission workflow.
- Notification flow.
- Admin operations.
- Deployment environment.
- One difficult production bug or DB issue.
- One design choice you would change today.

### Likely five-whys

```text
You led end-to-end development.
→ What did “end-to-end” mean exactly?
→ What was the architecture?
→ Why Laravel/Vue?
→ What failed in production?
→ How did you debug it?
→ How did you know the fix worked?
```

## 7.2 Queues / workers / schedulers

Need to know:

- **Queue:** stores work to be processed asynchronously.
- **Worker:** process that consumes queued jobs.
- **Scheduler:** triggers jobs/tasks at specific times/intervals.
- Why use async work: slow email/API/task should not block user request.
- What can go wrong: worker crash, duplicate jobs, retries, stuck queues, poison jobs.
- Reliability concept: retries can produce duplicates, so important side effects may need idempotency.

## 7.3 Server migration / upgrades / SSL

Be ready with one concrete real migration story:

```text
before → migration plan → risk → backup → cutover → verification → rollback plan
```

Do not invent tooling that was not actually used.

## 7.4 Production DB troubleshooting

Know the generic debugging flow and attach it to a real incident:

```text
symptom
→ reproduce / inspect logs
→ narrow app vs DB
→ inspect query/data/schema
→ identify root cause
→ fix
→ verify
→ prevent recurrence
```

## 7.5 Pac Com POS

Prepare one real feature/change you worked on:

- user/business need
- frontend change
- backend/API change
- DB interaction
- testing/debugging
- outcome

---

# 8. Thesis — minimum defendable knowledge

Current resume claims are **RESUME + USER** until the thesis source is separately audited.

Must be able to explain:

1. What “implicit intent” means with a simple workplace example.
2. Why role/hierarchy could change interpretation.
3. Why conversation context could help.
4. What retrieval contributes before generation/classification.
5. What graph nodes/relations represent at a high level.
6. What the baseline is.
7. What semantic F1 means in this thesis evaluation.
8. Why `0.6440 → 0.6793 → 0.6819` matters.
9. What failure cases remain.
10. Why the result does not prove universal workplace-intent understanding.

Do not memorize the thesis abstract; be able to explain the causal idea in plain language.

---

# 9. Foundation knowledge checklist

These are the concepts underneath the resume. Learn them through the projects, not as disconnected trivia.

## Python

- [ ] list vs tuple vs set vs dict
- [ ] average lookup complexity for dict/set
- [ ] mutability and hashability
- [ ] exceptions and error boundaries
- [ ] dataclass
- [ ] type hints / `Protocol`
- [ ] iteration / comprehensions
- [ ] file/JSON handling
- [ ] basic subprocess behavior and timeout handling

## Backend / APIs

- [ ] request → validation → service → DB/external dependency → response
- [ ] GET vs POST
- [ ] common HTTP status classes: 2xx / 4xx / 5xx
- [ ] REST resource thinking
- [ ] input validation
- [ ] timeout vs failure
- [ ] retry strategy
- [ ] idempotency
- [ ] sync vs async/background jobs
- [ ] health endpoint purpose
- [ ] service-layer boundary

## Database / SQL

- [ ] primary key vs unique key
- [ ] foreign key
- [ ] index: why it helps and write/storage trade-off
- [ ] INNER JOIN / LEFT JOIN
- [ ] GROUP BY / aggregate functions
- [ ] transaction and ACID at a practical level
- [ ] locking/concurrency basics
- [ ] SQL injection concept
- [ ] read-only access / least privilege
- [ ] why syntactically valid SQL can be semantically wrong

## Reliability / distributed-system basics

- [ ] timeout does not necessarily mean operation failed
- [ ] retry can create duplicate side effects
- [ ] idempotency key / deduplication intuition
- [ ] queue and worker
- [ ] retry budget / backoff intuition
- [ ] at-least-once processing intuition
- [ ] graceful failure vs silent wrong result

Classic example to master:

> Email API times out. If you blindly retry, the first request may actually have succeeded, causing two emails. Use an idempotent request key / deduplication strategy, persist operation state where appropriate, and distinguish timeout from confirmed failure.

## Retrieval / RAG

- [ ] lexical vs semantic retrieval
- [ ] BM25 intuition
- [ ] embedding intuition
- [ ] cosine similarity
- [ ] why normalized dot product = cosine
- [ ] RRF formula and motivation
- [ ] Recall@K
- [ ] Hit@K
- [ ] MRR
- [ ] reranking
- [ ] retrieval failure vs generation failure
- [ ] retrieval metric ≠ answer quality

## Agents / tool calling

- [ ] model vs agent vs workflow
- [ ] tool schema
- [ ] observe / choose action / tool result / continue or stop
- [ ] bounded action/tool budgets
- [ ] evidence grounding
- [ ] abstention
- [ ] why deterministic validation still matters around agents

## AI-native engineering

Be able to describe your actual working discipline:

```text
Understand requirement
→ give AI relevant context
→ specify constraints and interfaces
→ let AI propose/implement
→ inspect the diff/output
→ run tests / targeted checks
→ test edge cases
→ debug failures using evidence
→ keep/revert based on measured result
```

Important principle:

> AI can accelerate implementation; responsibility for requirements, architecture, validation and correctness remains with the engineer.

---

# 10. Recommended drill order

Do not study everything at once.

### Session 1 — Text-to-SQL

Goal: survive 5 layers of follow-up without bluffing.

- 60-second explanation
- architecture from memory
- verifier/safety
- metrics
- failure cases
- why semantic revision was rejected

### Session 2 — Kahap production engineering

- feedback platform architecture
- one production incident
- queues/workers/schedulers
- DB troubleshooting
- migration/deployment

### Session 3 — Hybrid RAG

- BM25
- dense embeddings
- RRF
- metrics
- benchmark scope
- latency/quality trade-off

### Session 4 — Video QA / Agents

- ownership boundary
- tool calling
- evidence flow
- transcript vs visual decision
- abstention
- evaluation contract

### Session 5 — Backend + DB fundamentals

Focus on scenario questions, not rote definitions.

### Session 6 — Thesis

Explain like to a software engineer who has not read the paper.

### Session 7 — Full Ant-style mock

Mix:

- resume deep dive
- project five-whys
- backend/DB fundamentals
- business-logic problem
- AI-assisted coding/validation reasoning

---

# 11. Mastery gate for each resume item

A bullet is interview-ready only when all are true:

- [ ] I can explain it in **30–60 seconds** without jargon dumping.
- [ ] I can draw/describe its **data flow / architecture**.
- [ ] I can explain **why** I chose the approach.
- [ ] I can name at least one **failure mode**.
- [ ] I can explain one **trade-off**.
- [ ] I can explain the **metric/result without exaggerating it**.
- [ ] I can answer “what did YOU personally do?” precisely.
- [ ] I can answer “what would you improve next?” realistically.
- [ ] I know which details are **code/eval evidence** vs personal recollection.

---

# 12. Open evidence gaps

These are intentionally not filled with guesses:

1. **Kahap / Pac Com internal implementation** — requires real personal examples; public repos cannot verify them.
2. **Thesis implementation details** — current resume claims recorded, but thesis/code source has not been audited in this file.
3. **Understand Anything graph** — no generated `.ua/knowledge-graph.json` was present, so repo understanding was built by full tree inventory + direct source/dependency/data-flow reading instead.
4. Historical experiment/workflow/static files were inventoried but are not all interview-relevant; the deep-read prioritizes current runtime, canonical evaluation, architecture and tests.

Never fill these gaps by inventing details. During practice, mark uncertain personal details and recover them from actual memory/source material.

---

## Current study starting point

Start with **Text-to-SQL**.

First drill question:

> “Can you walk me through your Text-to-SQL project and explain why you added verification and repair instead of just prompting the model to generate better SQL?”

Answer naturally first. Then drill the exact weak points instead of memorizing a polished script.
