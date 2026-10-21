# Ant International — Project Deep-Dive Coverage Map

Updated: 2026-10-21 (MYT)

Purpose: **coverage, not a question bank to memorize.**

Use this file to make sure every project on the current resume can survive a realistic deep dive. Questions are derived from the current resume, audited repository evidence, and the AI Engineering Field Guide's project-deep-dive pattern: ownership, architecture, design decisions, debugging, evaluation, trade-offs, and reflection.

Priority:

- **P0** — answer cold if this project is selected.
- **P1** — likely second-layer follow-up; understand, do not script word-for-word.
- **P2** — deeper repo/production follow-up; know the reasoning and boundaries.

Do not treat these as exact Ant predictions.

---

# 1. Text-to-SQL with Verification & Repair

## Core claim

Natural-language question → schema-grounded SQL generation → deterministic verification → bounded repair → read-only execution.

Main lesson: **executable SQL is not necessarily correct SQL.**

## P0 — must answer cold

1. What problem were you trying to solve?
2. Walk me through the system end-to-end.
3. What part did you personally build?
4. Why did you add deterministic verification instead of only improving the prompt?
5. What does the verifier actually check?
6. Why do you need a repair loop, and how does it work?
7. Why is the repair budget capped at two attempts?
8. How do you prevent generated SQL from modifying the database?
9. Your resume says execution improved from 75% to 90%. Does that mean 90% accuracy?
10. What is the difference between execution success and correctness in this project?
11. What does the 33% → 39% result measure?
12. What did the six wrong→correct cases tell you?
13. Give me one example where SQL executed successfully but was still wrong.
14. What is the biggest limitation of deterministic verification?

## P1 — natural deep dive

15. What schema information do you give the model?
16. Why use live schema introspection instead of a fixed schema prompt?
17. What happens when the generated SQL references a table or column that does not exist?
18. What happens when the user's natural-language question itself is ambiguous?
19. What would you do if the database had 1,000 tables?
20. What if the generated SQL is semantically correct but extremely slow?
21. Why use a bounded workflow instead of an open-ended autonomous agent?
22. Why LangGraph here? What state or branching does it manage?
23. What are the trade-offs of adding more repair attempts?
24. How would you debug a case where the verifier passes but the answer is wrong?
25. How would you evaluate semantic correctness beyond basic execution success?
26. Why did the later semantic-revision layer go from 39% to 38%?
27. What did you learn from choosing not to promote that semantic-revision experiment?

## P2 — repo-specific / production follow-up

28. How is read-only access enforced beyond just telling the model to generate SELECT?
29. Why is a prompt not a security boundary?
30. How would this design change for PostgreSQL/MySQL instead of SQLite?
31. How would you handle timeouts or expensive queries in production?
32. How would you protect sensitive data even if the SQL itself is read-only?
33. Your resume mentions schema and values. Which path actually uses value grounding, and is it part of the headline Qwen benchmark?
34. What was the DGSL/value-grounding experiment, and why was it kept separate from the default path?
35. The checked-in 9B summary exists, but the referenced workflow did not finish as a clean end-to-end success. What does that mean for how strongly you should state the result?

## Traps / red lines

- 90% = execution success, **not** 90% Text-to-SQL accuracy.
- 39% is the correctness-oriented EX-compatible result for the guarded Qwen 9B frozen-100 run.
- Default main path is schema-grounded; value grounding exists as a separate experiment.
- Verification rejects unsafe/invalid SQL but cannot prove user-intent correctness.
- SQLite is the current implementation boundary.

---

# 2. Hybrid Retrieval for RAG

## Core claim

Run BM25 lexical retrieval and Qwen dense retrieval in parallel, then combine their rankings with RRF while exposing ranking provenance.

Main lesson: **lexical and semantic retrieval fail differently; fusion can help, but retrieval quality is not final answer quality.**

## P0 — must answer cold

1. What problem were you solving?
2. Walk me through the retrieval flow.
3. What is BM25 good at?
4. What is dense retrieval good at?
5. Why combine them instead of choosing only one?
6. Why use RRF instead of averaging BM25 and embedding scores?
7. Explain RRF in simple terms.
8. What is Recall@10?
9. What is MRR@20?
10. What is Hit@10?
11. What were the benchmark size and headline results?
12. Why does higher retrieval Recall@10 not prove the final RAG answer is better?
13. What did hybrid recover that BM25 missed?
14. Would you always choose hybrid retrieval over BM25?

## P1 — natural deep dive

15. Why did dense retrieval have lower Recall@10 than BM25 but slightly higher MRR@20 on this slice?
16. What does it mean that hybrid recovered five BM25 top-10 misses but lost two BM25 hits?
17. Why expose BM25 rank, dense rank, and final RRF rank?
18. How would you debug a bad final ranking?
19. How do you separate a retrieval problem from a generation problem?
20. Why use Qwen3-Embedding-0.6B?
21. Why normalize vectors, and what does cosine similarity mean here?
22. What is the role of the embedding cache?
23. What is the quality-vs-latency trade-off of hybrid retrieval?
24. How would you evaluate whether hybrid is worth the extra latency in production?
25. How was the 64-query evaluation slice chosen, and what does Confluence-only mean for generalization?
26. Why keep evaluation queries / gold labels outside runtime retrieval inputs?

## P2 — repo-specific / production follow-up

27. What does the RRF constant `k=60` do conceptually?
28. When could raw-score normalization be reasonable instead of RRF?
29. The repo supports typed query signals such as `lex`, `vec`, `hyde`, and `intent`. Which of these are part of the canonical benchmark and which are not?
30. Is the demo reranker a neural cross-encoder?
31. Why does the browser demo use a lightweight embedding provider while the benchmark uses Qwen embeddings?
32. How would the architecture change at 10 million documents?
33. How would you handle incremental document updates without recomputing everything?
34. What if relevant evidence spans multiple chunks/documents?
35. What downstream evaluation would you add if turning this retriever into a full RAG product?

## Traps / red lines

- Canonical benchmark: 64 compatible Confluence queries, 5,189 documents.
- BM25 Recall@10 0.7341 → Hybrid 0.7630; MRR@20 0.6792 → 0.7418.
- Hybrid helped this frozen slice; it is not universally better.
- Canonical benchmark does **not** prove generated-answer quality.
- Canonical benchmark does not use HyDE, an agent, generation, or a neural reranker.

---

# 3. Multimodal Video QA Agent

## Core claim

Some questions can be answered from transcript evidence; others require visual evidence. The agent can choose among transcript search, context expansion, frame inspection, and clip inspection, then answer with evidence IDs.

Main lesson: **use an agent when dynamic evidence/tool choice buys something; otherwise a fixed pipeline is simpler.**

## P0 — must answer cold

1. What problem were you trying to solve?
2. Why is transcript-only QA insufficient?
3. Why not send every question to a vision model?
4. Walk me through the system end-to-end.
5. Why use an agent instead of a fixed pipeline?
6. What are the four domain tools?
7. What exactly did you implement, and what does Hermes itself provide?
8. How does the answer stay tied to evidence?
9. When should the agent use a frame versus a clip?
10. What happens when there is not enough evidence?
11. How did you evaluate the system?
12. What does 4/6 visual-required questions mean?
13. Why is the 12-question evaluation not a broad benchmark claim?
14. What would you improve first if you continued the project?

## P1 — natural deep dive

15. How does transcript retrieval work?
16. What does `expand_context` add after a transcript hit?
17. How do you prevent or stop repeated tool calls / loops?
18. What happens when a tool call fails or returns weak evidence?
19. How do you validate tool arguments such as timestamps?
20. Why allow abstention instead of forcing an answer?
21. What do the evidence IDs represent?
22. How do you know visual tools were used only when needed?
23. What are the failure modes behind the two failed visual-required cases?
24. How would you separate tool-selection failure from evidence-quality failure from answer-generation failure?
25. Why expose Agent Activity in the UI?
26. How would you monitor this kind of agent in production without exposing hidden chain-of-thought?

## P2 — repo-specific / production follow-up

27. The original strict evaluation says 6/12 overall and 4/6 visual-required. Why does a later post-hoc re-score say 12/12?
28. Why did you keep the original frozen score as the headline instead of promoting the post-hoc 12/12?
29. What was wrong with the original evaluator contract?
30. What does "strict full pass" actually require?
31. How is visual evidence-window correctness checked?
32. Why use sampled frames for clip inspection instead of native long-video input?
33. How would this scale to a two-hour video or a large video library?
34. What are the latency/cost trade-offs between transcript, frame, and clip inspection?
35. How would you protect an agent with tools from unsafe or malformed tool calls?

## Ownership boundary

Hermes owns:

- observe/act loop
- model/tool dispatch
- choosing among exposed tools

Your repository owns:

- transcript search/context tools
- frame/clip inspection tools
- BM25 transcript retrieval
- FFmpeg sampling
- evidence store/IDs
- answer/citation contract
- abstention behavior
- evaluation harness
- UI/integration

Do not claim you implemented Hermes core from scratch.

## Traps / red lines

- Headline frozen result remains the original strict v2 result, not the post-hoc 12/12 diagnostic.
- 12 cases are self-authored and small.
- The project tests adaptive modality/evidence use, not generic video understanding leadership.

---

# 4. M.S. Thesis — Workplace Implicit Intent

## Core claim

The same workplace utterance can imply different intent depending on speaker/listener roles and conversational context. The system retrieves structured role/context evidence before interpretation.

Main lesson: **literal text alone can miss social meaning; structured evidence can help, but evaluation must be interpreted carefully.**

## P0 — must answer cold

1. Explain the thesis problem in plain English.
2. Give one concrete example of implicit workplace meaning.
3. Why do workplace hierarchy and speaker/listener roles matter?
4. What are speaker and listener states?
5. Walk me through the high-level pipeline.
6. What is Role KG trying to retrieve?
7. What is Context KG trying to retrieve?
8. What is a communicative purpose?
9. How does DualKG combine role and context evidence?
10. Why exclude evidence from the same source post?
11. What does semantic F1 mean in this thesis?
12. What were the 400-example target-only results?
13. Is 0.6819 accuracy?
14. Is the improvement from Role KG 0.6793 to DualKG 0.6819 large enough to claim DualKG is meaningfully better?
15. What is the biggest evaluation limitation?
16. What would you change if rebuilding the thesis now?

## P1 — natural deep dive

17. Why use graph/state embeddings instead of only sentence embeddings?
18. What signals are combined in Role KG retrieval?
19. Why combine dialogue similarity and role-pair match?
20. How is Context KG different from Role KG?
21. How are communicative-purpose categories used?
22. What are examples of pressure, refusal, deflection, compliance, risk mitigation, and neutral coordination?
23. How exactly does the final DualKG Top1 fusion work?
24. Why is the final DualKG not simply Role Top1 + Context Top1?
25. Why do target-only and preceding-context baselines differ so much?
26. Why is the empty-clue control strong in the preceding-context arm?
27. What does the pseudo-reference come from, and why can that bias evaluation?
28. How would you design a stronger human evaluation?
29. What failure cases would you inspect to decide whether role/context retrieval is actually helping?
30. Why use MiniLM for semantic matching/retrieval, and Llama 3.1 8B for generation?

## P2 — repo-specific / research follow-up

31. What are the GCN state embeddings representing?
32. Why are same-source-post examples excluded during retrieval?
33. How does the Role KG candidate score combine dialogue cosine similarity and role-pair match?
34. What is the evidence budget in DualKG Top1?
35. How are target utterances aligned with preceding context, and what happens to ambiguous/unmatched cases?
36. Why are there 401 upstream targets but 400 primary evaluation examples?
37. What does the empty-clue result tell you about the evaluation protocol itself?
38. If the model already sees preceding conversation context, when does external graph evidence still add value?
39. How would you test whether improvements are statistically meaningful rather than noise?
40. The current resume says 10,645 workplace dialogue turns. Be ready to explain exactly what that count represents from the final data pipeline; if you cannot trace it confidently, do not improvise.

## Traps / red lines

- 0.6819 is semantic response-matching F1, **not accuracy** and not classification macro-F1.
- DualKG is not RRF.
- Final DualKG is not simply Role Top1 + Context Top1.
- DualKG is not best in every evaluation arm; the preceding-context empty-clue control is higher.
- The pseudo-reference is generated from the complete post and is an explicit evaluation limitation.
- The Role → Dual gain is small; do not claim significance without evidence.

---

# 5. Universal project attack surfaces

If an interviewer selects any project, expect questions from these buckets:

1. **Problem** — What problem did you solve? Who needs it?
2. **Flow** — Walk me through input → processing → output.
3. **Ownership** — What exactly did you build yourself?
4. **Why** — Why this design instead of an obvious alternative?
5. **Evidence** — How do you know it worked? What does the metric really mean?
6. **Failure** — Show me a case where it failed. How did you diagnose it?
7. **Trade-off** — What did you gain and what did you pay?
8. **Changed condition** — What if scale/data/latency/requirements change?
9. **Production** — How would you monitor, secure, and operate it?
10. **Reflection** — What would you redo now?

The goal is not to memorize all questions. A project is ready when you can reason through all ten buckets without inventing facts.

---

# 6. Study priority for Ant first round

1. **Text-to-SQL — deepest**
2. **Hybrid RAG — strong working depth**
3. **Video QA Agent — strong working depth, ownership boundary must be exact**
4. **Thesis — strong conceptual/evaluation depth, avoid research overclaiming**

For each project, first master:

> Problem → Flow → Ownership → Why → Metric → Failure → Limitation → Redo

Then use the question list only to find missing knowledge.
