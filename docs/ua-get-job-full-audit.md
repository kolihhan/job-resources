# Understand Anything × get-job — Full Interview Audit Record

Last run: 2026-10-18 (MYT)

Primary use: Ant International Malaysia — Applied AI Engineer (Fresh Graduate) technical interview preparation.

This file records what was actually executed. Detailed project knowledge remains in `docs/interview-resume-knowledge-map.md`.

## 1. Execution truth table

| Repository | Understand Anything execution | Source snapshot | get-job resume mapping |
|---|---|---|---|
| `semantic-text2sql-agent` | **FULL local pipeline completed** | `2be1b2a09454788eca8b6b1a6233ee69a16a465d` | Complete |
| `local-rag-search` | **FULL local pipeline completed** | `02fedfff44249e21fe3089a6aad35ff8267b3c39` | Complete |
| `hermes-video-tutor` | **FULL local pipeline completed** | `22a9b3044695cef421feec2dd36938149d2038cc` | Complete |
| `master-thesis` | **Connector-based source/eval audit; NOT literal local `/understand --full`** | `f134750441dee036269ffe9e378fb9116ac7bdf9` | Complete for submitted resume claims |

`master-thesis` is private. The authenticated GitHub connector can read it, but the runtime safety boundary did not permit exporting that private repository into the local execution environment. Therefore this record does not mislabel the thesis audit as a literal local UA run.

## 2. Understand Anything version and phases executed

Pinned skill: `egonex-ai/understand-anything:understand`

Pinned upstream commit: `790b157028637b626c8666fa7fa28248944b900c`

For each of the three public repos, execution included:

1. source snapshot / pre-flight
2. official `scan-project.mjs`
3. official `extract-import-map.mjs`
4. official `compute-batches.mjs`
5. official `extract-structure.mjs` for every batch
6. file-analyzer semantic node/edge pass using those deterministic structures
7. official `merge-batch-graphs.py`
8. assembled whole-graph completeness review
9. architecture layer assignment
10. guided tour construction
11. official UA inline deterministic final-validation contract
12. official `build-fingerprints.mjs`
13. final `knowledge-graph.json`, `fingerprints.json`, `meta.json`
14. fresh post-save consistency check

### Text-to-SQL

- 85 scanned files: 43 code / 6 infra / 9 docs / 24 config / 1 data / 2 script
- 12 batches
- 271 nodes / 551 edges
- 25 internal import edges
- merge import recovery: **0**
- validator issues: **0**
- fingerprints: **85 / 85**
- dangling edges after save: **0**
- 5 architecture layers / 8 tour steps

Layers: Core Text-to-SQL Runtime; Evaluation & Experiments; Tests; Documentation; Project Support & Automation.

### Hybrid RAG

- 59 scanned files: 23 code / 1 infra / 22 docs / 9 config / 4 script
- 11 batches
- 160 nodes / 296 edges
- 19 internal import edges
- merge import recovery: **0**
- validator issues: **0**
- fingerprints: **59 / 59**
- dangling edges after save: **0**
- 5 architecture layers / 8 tour steps

Layers: Retrieval Runtime; Evaluation & Benchmarks; Tests; Documentation; Project Support & Automation.

### Video QA

- 68 scanned files: 37 code / 1 infra / 8 docs / 19 config / 3 script
- 12 batches
- 198 nodes / 353 edges
- 23 internal import edges
- merge import recovery: **0**
- validator issues: **0**
- fingerprints: **68 / 68**
- dangling edges after save: **0**
- 6 architecture layers / 8 tour steps

Layers: Video QA Runtime; Hermes Integration; Evaluation & Frozen Runs; Tests; Documentation; Project Support & Automation.

The final validator produced orphan-node warnings for some standalone docs/frozen artifacts, but no duplicate-ID, dangling-reference, layer-coverage, or tour-reference issues.

## 3. Thesis evidence status

The private thesis source and final report support the submitted headline result:

- baseline target-only F1: `0.643971`
- Role KG target-only F1: `0.679274`
- DualKG Top1 target-only F1: `0.681947`

So resume rounding `0.6440 → 0.6793 → 0.6819` is supported.

Final DualKG identity is:

```text
regenerated Task35 graph-policy Role backbone
+ Context KG rank-1 evidence per side
+ append only if unique
+ max 10 states per side
```

It is not RRF/P2Q and is not a simple Role Top1 + Context Top1 merge.

Important evaluation boundaries: 400 examples in primary eval; 401 upstream targets; target-only and preceding-context are distinct; pseudo-reference uses the complete post; semantic F1 is response-matching F1 rather than exact-label accuracy. The preceding-context empty-clue protocol control scores higher than DualKG, so do not say DualKG is globally best in every arm.

## 4. get-job Stage 3 coverage — all 12 submitted bullets

Every submitted experience/project/thesis bullet now has: a 30–60s story anchor, likely follow-ups, evidence boundary, required knowledge, and a safe fallback.

| ID | Resume bullet | Evidence | Primary drill / risk |
|---|---|---|---|
| E1 | Kahap feedback platform end-to-end | USER | exact personal ownership; architecture; production failure |
| E2 | Kahap features + app/DB issues | USER | one real incident; diagnosis; verification |
| E3 | migration / queues / workers / schedulers / SSL / DB | USER | async reliability, retries/idempotency, rollback |
| E4 | Pac Com POS Laravel/Vue | USER | one concrete feature end-to-end |
| T1 | Text-to-SQL schema/values + validation/repair | CODE + wording risk | main schema path vs separate value-grounding experiment |
| T2 | 75→90 executable +6 correct | EVAL | execution success vs semantic correctness |
| R1 | BM25 + dense + RRF | CODE | why hybrid; why RRF; cosine/BM25 intuition |
| R2 | Recall/MRR benchmark gains | EVAL | metric definitions and exact benchmark scope |
| V1 | transcript vs frame/clip routing + evidence | CODE | Hermes ownership boundary; tools/evidence/abstention |
| V2 | 4/6 visual-required, no unnecessary visual calls | EVAL | narrow frozen 12-case scope; do not generalize |
| TH1 | graph-aware workplace retrieval | CODE + connector audit | role/context/state representation; dataset definition |
| TH2 | 0.6440→0.6793→0.6819 | EVAL | semantic F1; DualKG identity; limitations |

### Highest-risk claim wording

1. **Text-to-SQL “schema and values”.** The supported headline `SemanticSQLService` main path directly uses live schema introspection. Value-aware grounding is a separate experiment. Safe wording: “The main guarded path uses live schema introspection; I also experimented with value-aware grounding separately.”
2. **Text-to-SQL 90%.** This is execution success, not accuracy. Headline semantic EX is 39% after guard/repair vs 33% direct.
3. **Video no-unnecessary-visual claim.** Say “in that frozen evaluation run”, not as a universal property.
4. **Thesis F1.** It is semantic response-matching F1 in the final report, not accuracy.
5. **Thesis 10,645 turns.** Rehearse the exact dataset-definition behind this resume count; do not substitute another intermediate pipeline count.
6. **Kahap/Pac Com.** Public GitHub cannot prove internal implementation. Use real personal incidents and never invent operational detail.

## 5. Knowledge to master, attached to the resume

- **Kahap + Text-to-SQL:** REST request flow, primary vs unique key, indexes, joins, transactions, timeout/retry/idempotency, queue/worker/scheduler, read-only DB boundaries.
- **RAG + thesis:** BM25, embeddings, cosine, RRF, Recall@K, Hit@K, MRR, retrieval-vs-generation failure, ablation/evaluation discipline.
- **Video QA + Text-to-SQL:** model vs workflow vs agent, tool schema, bounded action/retry budget, deterministic guards, evidence grounding, abstention.
- **Across repos:** Python collections/hashability, exceptions, dataclass, Protocol/type hints, JSON/file handling, subprocess timeout/error behavior.

## 6. Drill order

1. Text-to-SQL — overview → architecture → verifier/safety → metrics → failure modes.
2. Kahap — platform → production incident → queue/retry/idempotency → migration/DB.
3. Thesis — plain-language problem → Role KG → Context KG → DualKG → semantic F1/limitations.
4. Hybrid RAG — BM25 → dense → RRF → metrics/trade-offs.
5. Video QA — ownership → tools/evidence → abstention → evaluation.
6. Backend + DB scenarios.
7. Full Ant-style mixed technical mock.

A bullet is interview-ready only when it can be explained naturally in 30–60 seconds, its architecture and design choice can be defended, one failure mode and trade-off are known, the metric can be explained without exaggeration, personal ownership is precise, and a realistic improvement can be proposed.

## 7. Starting drill

> **Can you walk me through your Text-to-SQL project and explain why you added deterministic verification and bounded repair instead of just prompting the model to generate better SQL?**
