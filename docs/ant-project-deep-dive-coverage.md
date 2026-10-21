# Ant International — Resume & Project Deep-Dive Coverage Map

Updated: 2026-10-21 (MYT)

Purpose: **coverage, not a question bank to memorize.**

This file is the adversarial coverage map for the current resume. It is grounded in:

- `resumes/resume-en-current.md`
- `docs/interview-resume-knowledge-map.md`
- `docs/interview-resume-job-experience.md`
- audited project repositories and frozen evaluation artifacts
- Ant-specific prep evidence in `docs/ant-interview-prep.md`
- the AI Engineering Field Guide project-deep-dive pattern

Use it to answer one question: **if an interviewer attacks any visible resume claim, do I understand enough to answer without inventing?**

Evidence labels:

- **VERIFIED / CODE / EVAL** — directly supported by source, checked-in evaluation, config, Git history, or an explicitly checked artifact.
- **USER** — supported by Ko's recollection but not fully provable from public/source evidence alone.
- **INFERENCE** — engineering reasoning from evidence, not a claim that this happened in production.
- **UNKNOWN** — not established; do not improvise.

Priority:

- **P0** — answer cold.
- **P1** — understand and reason through naturally.
- **P2** — deeper follow-up; know the boundary, not a memorized script.

---

# 0. Grill findings first

The earlier project-only map was useful but **too narrow** if treated as the whole interview map.

Confirmed gaps that must be covered:

1. **Work experience is directly attackable from three resume bullets.** The feedback platform, existing Laravel/Vue platform, production DB/queue/worker/scheduler/migration/SSL claims need their own drill surface.
2. **The skills section is interview surface.** Python, SQL, REST APIs, FastAPI, Laravel, Vue, MySQL, SQLite, Linux, GitHub Actions and pytest can all become fundamentals questions.
3. **Some resume wording is broader than the strongest repo evidence.**
   - Text-to-SQL says schema **and values**; the headline guarded Qwen path is schema-grounded, with value grounding in a separate experiment.
   - Thesis says **10,645 workplace dialogue turns**; the current audit has not pinned the exact provenance of this number in the clean final pipeline. Do not invent a derivation if asked.
4. **Project metrics contain easy traps.**
   - Text-to-SQL 90% is execution success, not accuracy.
   - RAG retrieval metrics do not prove final answer quality.
   - Video QA post-hoc 12/12 is not a fresh rerun and is not the headline claim.
   - Thesis 0.6819 is semantic response-matching F1, not accuracy or macro-F1; Role→Dual gain is small.
5. **Ownership boundaries matter as much as architecture.**
   - SuggestionBox source proves behavior, but source alone does not prove who authored every line.
   - Career has much stronger Git-confirmed contribution evidence.
   - Hermes owns the core agent loop; the Video QA repo owns domain tools/evidence/evaluation/integration.
6. **Production incident stories are still the weakest area.** Static source can prove architecture/configuration; it cannot prove a specific incident happened. Do not fabricate a migration/worker/DB outage story.
7. **Ant's AI Coding Assessment is not on the resume but is high-prep-value.** It deserves a separate Ant-specific section because the recruiter explicitly required it before the interview.

This map therefore covers the **entire visible resume plus the direct Ant assessment surface**, then ends with an ELI5 mastery view.

---

# 1. Experience — Production feedback platform

Resume claim:

> Led end-to-end development of a production feedback platform, from system design and implementation through deployment, including submission workflows, automated notifications, and admin operations.

Evidence boundary:

- Source confirms a Laravel 9.36.4 + Livewire 2.10.7 application, not a Vue app.
- Student identity is integrated with the Career platform through a third-party login flow.
- Proposal submission, voting/messages, threshold/status transitions, admin processing and synchronous notification calls are visible in source.
- Production deployment/HTTPS ownership is partly USER-confirmed.
- Do not claim every line was written alone.

## P0

1. What problem did the platform solve and who used it?
2. What did “end-to-end” mean in your case?
3. What exactly did you personally own versus inherit or collaborate on?
4. Walk through one student flow from login to proposal/vote to school-side follow-up.
5. Why Laravel/Livewire? What did Livewire handle versus controller/Blade flows?
6. How did the voting / support threshold work?
7. What happened when a proposal reached the threshold?
8. How were school/admin operations handled?
9. How were notifications triggered?
10. What did deployment and production maintenance involve?
11. What would you redesign today?

## P1

12. Why is a synchronous cross-system notification call fragile?
13. What happens if the DB update succeeds but the external notification fails?
14. Would you make notification retryable/idempotent? How?
15. Where would you use a transaction, and what can a DB transaction not roll back?
16. How would you prevent duplicate submissions/votes at the DB/application level?
17. How would you debug a production 500 in this application?
18. What logs/evidence would you inspect first?
19. How would you design permissions for student versus admin flows?
20. What would change if usage increased significantly?

## P2 / red lines

- Threshold is **100 total Message records including agree + disagree**, not “100 upvotes.”
- SuggestionBox does not have evidence of a custom Jobs directory/worker architecture like Career; do not merge the two systems in memory.
- Historical design motivation that is not remembered must not be reconstructed as fact from today's preferences.

---

# 2. Experience — Existing Laravel/Vue production career platform

Resume claim:

> Shipped new features and resolved application and database issues on an existing Laravel/Vue.js production platform.

Evidence boundary:

- Stack: Laravel 5.8.38 + Vue 2.7.16 + Vuex + Router + Axios/JWT.
- Full Git history supports substantial long-term contribution: user-confirmed identities total 516 / 1,176 commits from 2022-08-04 to 2026-08-31.
- Concrete commits support API, form, admin/front-end, bug-fix and maintenance work.
- Source can prove flows and changes; it does not prove every claimed production incident unless backed by recollection/logs.

## P0

1. What kind of system was this and what did you work on most often?
2. Was this greenfield or inherited? What changed because of your work?
3. Walk through one real Laravel/Vue request end-to-end.
4. How did Vue/Vuex/Axios interact with Laravel APIs?
5. How was authentication handled at a high level?
6. Give one concrete feature you added.
7. Give one concrete bug you fixed.
8. What kinds of DB/application problems did you handle?
9. How did you verify a fix before/after deployment?
10. What is one thing you learned from maintaining an old production system for years?

## P1

11. Explain the lecture-registration flow from Vue component to DB pivot/notification.
12. What can go wrong if a notification is dispatched before a transaction fully commits?
13. How do you approach a duplicate-registration or consistency problem?
14. How would you investigate a slow endpoint/query?
15. What is the difference between app bug, DB bug, data issue and infrastructure issue?
16. How do you safely change an older Laravel application without broad refactoring?
17. Why can a framework-level transaction still fail to protect file/email/external side effects?
18. What would you test around a form/API change?

## P2 / red lines

- Do not say you built the entire Career platform from scratch.
- Do not borrow Career commits or architecture to strengthen Pac Com.
- If asked for a specific production incident, use only a real remembered incident; static code is not incident evidence.

---

# 3. Experience — Queue / worker / scheduler / migration / SSL / DB operations

Resume claim:

> Managed server migrations and upgrades, Laravel queues/workers/schedulers, SSL renewal, and production database troubleshooting.

Evidence boundary:

- Career archived production configuration uses database queue + Redis cache.
- A Supervisor config shows `queue:work`, 3 processes, `sleep=3`, `tries=3`, autorestart.
- Career includes a `ShouldQueue` notification.
- SuggestionBox archived config is sync queue.
- Scheduler commands exist in both apps; actual historical runtime success is not automatically proven by config.
- Certbot/Let's Encrypt and Ubuntu production use are USER-confirmed; Career README contains Certbot/Nginx operational notes.

## P0

1. Explain queue vs job vs worker vs scheduler in simple terms.
2. Why use a queue instead of doing everything inside the HTTP request?
3. What happens if a worker dies?
4. How would you notice a stuck queue?
5. What is a failed job?
6. Why can retrying a job create duplicate side effects?
7. What is idempotency?
8. What does a scheduler do that a worker does not?
9. What does SSL renewal involve at a practical level?
10. Walk through how you would plan a server migration safely.
11. What would you back up and verify before cutover?
12. What is your rollback plan?
13. How do you troubleshoot a DB issue without immediately blaming the database?

## P1

14. Why don't 3 workers imply exactly-once processing?
15. What happens if the HTTP request times out after the server completed the side effect?
16. How would you make a notification/payment-like operation safe to retry?
17. How would you monitor queue length, error rate and worker health?
18. What is the difference between cron and Laravel scheduler?
19. What could go wrong during a DB/schema migration?
20. How do you minimize downtime during server migration?
21. What would you inspect when HTTPS suddenly fails after renewal?

## Boundary

These engineering answers can be reasoned through, but **do not convert them into “I personally had this exact incident” unless it is a real remembered event.**

---

# 4. Experience — Pac Com POS

Resume claim:

> Developed and maintained Laravel/Vue.js features for a production POS system.

Evidence boundary:

- Current support is USER memory only; no recovered source/Git history has been matched to Pac Com.
- Safe story: earlier internship, simpler maintenance, bug/UI/layout/existing-feature work, first real Laravel experience.

## P0

1. What did you actually do at Pac Com?
2. What kind of Laravel/Vue flow did you learn there?
3. How was it different from your later Kahap work?
4. What did you learn from working on a real codebase for the first time?

## Red line

Do not invent a complex production incident or reuse Career evidence here.

---

# 5. Project — Text-to-SQL with Verification & Repair

Core claim:

> Natural-language question → schema-grounded SQL generation → deterministic verification → bounded repair → read-only execution.

Main lesson: **executable SQL is not necessarily correct SQL.**

## P0 — must answer cold

1. What problem were you trying to solve?
2. Walk me through the system end-to-end.
3. What part did you personally build?
4. Why deterministic verification instead of only improving the prompt?
5. What does the verifier check?
6. Why a repair loop?
7. Why cap repair at two attempts?
8. How do you enforce read-only execution?
9. Does 90% mean 90% Text-to-SQL accuracy?
10. What is execution success versus correctness?
11. What does 33% → 39% measure?
12. What did the six wrong→correct cases tell you?
13. Give a case where SQL executes but is still wrong.
14. What can deterministic verification never prove?

## P1

15. What schema information is provided to the model?
16. Why live schema introspection?
17. What happens for nonexistent table/column references?
18. What if the natural-language question is ambiguous?
19. What if there are 1,000 tables?
20. What if SQL is correct but too expensive/slow?
21. Why a bounded workflow instead of an open-ended agent?
22. What does LangGraph manage here?
23. How would you debug verifier-pass / semantically-wrong cases?
24. Why did semantic revision go 39% → 38%?
25. Why was that experiment not promoted?

## P2 / repo-specific

26. What are the read-only defenses beyond prompting for SELECT?
27. Why is a prompt not a security boundary?
28. How would this change for PostgreSQL/MySQL?
29. How would you handle timeouts and sensitive data?
30. Resume says “schema and values”: which path uses values?
31. Is value grounding part of the headline Qwen benchmark?
32. What was the DGSL experiment and why is it separate?
33. The checked-in 9B summary exists, but its referenced workflow did not end as a clean canonical success. How should that affect claim strength?

## Red lines

- 90% = conservative execution success, not accuracy.
- Correctness-oriented frozen-100 result: 33% → 39% EX-compatible match.
- Default main path is schema-grounded; value grounding is separate.
- SQLite is the current implementation boundary.

---

# 6. Project — Hybrid Retrieval for RAG

Core claim:

> BM25 lexical retrieval + Qwen dense retrieval → RRF fusion → ranked results with provenance.

Main lesson: **lexical and semantic retrieval fail differently; retrieval quality is not final answer quality.**

## P0

1. What problem were you solving?
2. Walk through the retrieval flow.
3. What is BM25 good at?
4. What is dense retrieval good at?
5. Why combine them?
6. Why RRF instead of averaging raw BM25/vector scores?
7. Explain RRF simply.
8. What is Recall@10?
9. What is MRR@20?
10. What is Hit@10?
11. What were the benchmark size/results?
12. Why does higher Recall not prove better generated answers?
13. What did hybrid recover and what did it lose?
14. Would you always use hybrid?

## P1

15. Why can dense have lower Recall but higher MRR on the same set?
16. Why expose BM25/dense/RRF rank provenance?
17. How would you debug one bad ranking?
18. How do you separate retrieval failure from generation failure?
19. Why Qwen3-Embedding-0.6B?
20. Why normalize vectors?
21. What is the embedding cache for?
22. What is the quality/latency trade-off?
23. How would you decide if hybrid is worth it in production?
24. What does Confluence-only mean for generalization?
25. Why keep eval queries/gold labels out of runtime inputs?

## P2

26. What does RRF `k=60` do conceptually?
27. When might calibrated score fusion be reasonable?
28. Which typed signals are actually part of the canonical benchmark?
29. Is the demo reranker a neural cross-encoder?
30. Why does demo infrastructure differ from benchmark infrastructure?
31. What changes at 10M documents?
32. How would you handle incremental updates?
33. What if evidence spans multiple chunks/documents?
34. What downstream answer evaluation would you add?

## Red lines

- Canonical benchmark: 64 compatible Confluence queries / 5,189 docs.
- BM25 Recall@10 0.7341 → Hybrid 0.7630; MRR@20 0.6792 → 0.7418.
- Canonical benchmark does not prove generated-answer quality.
- HyDE/agent/generation/neural reranking are not part of the headline benchmark.

---

# 7. Project — Multimodal Video QA Agent

Core claim:

> Search transcript when text evidence is enough; inspect frames/clips only when visual evidence is needed; answer with evidence IDs.

Main lesson: **use an agent when dynamic tool/evidence choice buys something; otherwise a fixed workflow is simpler.**

## P0

1. What problem were you solving?
2. Why is transcript-only insufficient?
3. Why not use vision for every question?
4. Walk through the system.
5. Why an agent instead of a fixed pipeline?
6. What are the four domain tools?
7. What did you implement versus what Hermes provides?
8. How is the answer tied to evidence?
9. Frame versus clip: when should each be used?
10. What happens when evidence is insufficient?
11. How was the system evaluated?
12. What does 4/6 visual-required mean?
13. Why is 12 cases not a broad benchmark?
14. What would you improve first?

## P1

15. How does transcript retrieval work?
16. Why `expand_context`?
17. How do you stop repeated tool calls / loops?
18. What if a tool fails or returns weak evidence?
19. How are timestamps/tool arguments validated?
20. Why allow abstention?
21. What are evidence IDs?
22. How do you know visual tools were not called unnecessarily?
23. How would you analyze the failed visual cases?
24. How do you separate routing/tool failure, evidence failure and generation failure?
25. Why expose Agent Activity?
26. How would you monitor tool-using agents in production without exposing chain-of-thought?

## P2

27. Why does original strict eval show 6/12 overall while post-hoc re-score can show 12/12?
28. Why is the post-hoc 12/12 not promoted as the headline?
29. What was wrong with the old evaluator contract?
30. What does strict full pass require?
31. How is evidence-window correctness checked?
32. Why sampled frames for clips?
33. How would this scale to long videos / a large library?
34. What are transcript/frame/clip latency-cost trade-offs?
35. How would you guard tool calls against unsafe/malformed actions?

## Ownership boundary

Hermes owns:

- observe/act loop
- model/tool dispatch
- choosing among exposed tools

Your repository owns:

- transcript search / context expansion
- frame / clip inspection tools
- BM25 transcript retrieval
- FFmpeg sampling
- evidence IDs/store
- answer/citation contract
- abstention behavior
- evaluation harness
- UI/integration

---

# 8. Project — M.S. Thesis: Workplace implicit intent

Core claim:

> Literal text may not reveal workplace intent; speaker/listener role and conversational context provide structured evidence for interpretation.

## P0

1. Explain the problem in plain English.
2. Give a concrete implicit-intent example.
3. Why do hierarchy and speaker/listener roles matter?
4. What are speaker/listener states?
5. Walk through the high-level pipeline.
6. What is Role KG trying to retrieve?
7. What is Context KG trying to retrieve?
8. What is a communicative purpose?
9. How does final DualKG Top1 combine evidence?
10. Why exclude same-source-post evidence?
11. What does semantic F1 mean?
12. What are the 400-example target-only results?
13. Is 0.6819 accuracy?
14. Is 0.6793 → 0.6819 enough to claim meaningful superiority?
15. What is the biggest evaluation limitation?
16. What would you redesign now?

## P1

17. Why graph/state embeddings instead of only sentence embeddings?
18. What signals are combined in Role KG retrieval?
19. Why dialogue similarity + role-pair match?
20. How is Context KG different?
21. How are communicative-purpose categories used?
22. Give examples of pressure/refusal/deflection/compliance/risk mitigation/neutral coordination.
23. How exactly does final DualKG Top1 fuse evidence?
24. Why is it not Role Top1 + Context Top1?
25. Why do target-only and preceding-context baselines differ?
26. Why is the empty-clue control strong in the preceding-context arm?
27. Where does the pseudo-reference come from?
28. How can the pseudo-reference bias evaluation?
29. How would you design human evaluation?
30. Why MiniLM and Llama 3.1 8B?

## P2 / research integrity

31. What do GCN state embeddings represent?
32. Why same-source-post exclusion?
33. What is the Role KG candidate scoring intuition?
34. What is the evidence budget in DualKG Top1?
35. How is target/pre-context alignment handled?
36. Why 401 upstream targets but 400 primary examples?
37. What does the empty-clue result tell you about the protocol?
38. If the model already has preceding context, when can external graph evidence still help?
39. How would you test statistical significance?
40. Resume says **10,645 workplace dialogue turns**. The current clean audit has not pinned the exact provenance of that count. If asked, do not improvise a derivation; distinguish the resume dataset count from the 400-example evaluation and offer the verified evaluation scope.

## Red lines

- 0.6819 = semantic response-matching F1, not accuracy or classification macro-F1.
- DualKG does not use RRF.
- DualKG is not simply Role Top1 + Context Top1.
- DualKG is not best in every evaluation condition.
- Pseudo-reference from the complete post is a real limitation.
- Role→Dual gain is small and not established as statistically significant.

---

# 9. Resume skills — fundamentals attack surface

The interviewer does not need to stay inside project questions. Anything listed under Skills can become a probe.

## Python

P0:

- list vs tuple vs set vs dict
- average dict/set lookup
- mutability / hashability
- exceptions and failure boundaries
- file/JSON handling
- async basics because the Ant assessment uses `asyncio`

Likely bridge questions:

- Why use a dict/set here?
- What is a race condition?
- What does `asyncio` help with?
- Concurrency versus parallelism?
- What does a lock protect?

## SQL / databases

P0:

- primary key vs unique key
- foreign key
- index: faster reads, write/storage cost
- JOIN / GROUP BY / aggregates
- transaction intuition
- locks/concurrency basics
- SQL injection
- read-only / least privilege

Likely bridge questions:

- Why can an index make writes slower?
- When would a transaction be required?
- What if two requests update the same row?
- How do you investigate a slow query?

## Backend / REST / FastAPI / Laravel

P0:

- request → validation → business logic → DB/dependency → response
- GET vs POST
- 2xx / 4xx / 5xx
- validation
- authn vs authz
- timeout / retry
- idempotency
- sync request vs queued/background work
- health/logging basics

## Retrieval / AI

P0:

- BM25
- embeddings / cosine similarity
- RRF
- Recall@K / Hit@K / MRR
- retrieval vs generation failure
- grounding / evidence
- agent/tool calling vs fixed workflow
- abstention
- evaluation design / frozen sets / ablations

## PHP / JavaScript / Vue / MySQL / SQLite

Working depth:

- explain where each appeared in real work/projects
- do not pretend equal expertise in every listed technology
- be ready for practical framework/request-flow questions rather than language trivia

## Linux / Git / GitHub Actions / pytest

Working depth:

- basic process/log/file/port reasoning
- Git branch/commit/diff/merge basics
- CI purpose and failure interpretation
- pytest unit/integration test intuition, fixtures/assertions at a practical level

Important caution:

- Text-to-SQL's referenced workflow did not complete as a clean canonical end-to-end success; do not use that run to claim “my GitHub Actions pipeline is fully green/reproducible.”

---

# 10. Education / profile attack surface

Visible resume facts can still be used to enter technical discussion.

## P0

1. Tell me about yourself.
2. What did you focus on in your master's?
3. How did you move from production backend work toward applied AI?
4. Which project best represents what you want to do now?
5. What did your thesis teach you that your engineering projects did not?
6. Why Applied AI / backend + AI?
7. Why Ant International?

Do not force a “why Applied AI” conclusion into the self-introduction unless asked; the intro can simply expose the three anchors: NTHU NLP/LLM, production backend experience, applied-AI projects.

---

# 11. Ant-specific non-resume surface — AI Coding Assessment

This is not a resume item, but it is direct interview-context evidence and should be prepared.

Known implementation/story:

- terminal breakfast-shop system
- three terminal roles / shared real-time order state
- Python + `asyncio.start_server`
- raw TCP / telnet-compatible terminals
- shared in-memory `OrderStore`
- `asyncio.Lock`
- legal order-state transitions
- tests for multiple connections, transitions, disconnect/recovery and concurrent consistency
- initial SSH / `asyncssh` direction hit session/channel/connection lifecycle issues
- simplified to raw TCP/telnet-compatible path
- AI used as coding agent under explicit requirements/minimal-diff/verification constraints

## P0

1. Explain the task and your architecture.
2. Why `asyncio`?
3. Why a shared store?
4. Why a lock?
5. What race condition were you protecting against?
6. Concurrency versus parallelism?
7. What happens if the lock is too broad?
8. What if you run multiple processes/instances?
9. Why did the SSH direction fail?
10. Why was simplifying to raw TCP a good engineering decision under time pressure?
11. How did you use AI?
12. How did you make sure AI-generated code was actually correct?
13. What tests did you run?
14. What would you improve with more time?
15. What would you persist in a real production version?

Main lesson:

> AI accelerated implementation, but requirement interpretation, debugging direction, verification and acceptance remained the engineer's responsibility.

---

# 12. Universal interviewer pivots

Any resume item can pivot into these:

1. **Problem** — what real problem is this solving?
2. **Ownership** — what exactly did you do?
3. **Flow** — trace input/request → processing → state/DB/tool → output.
4. **Why** — why this design, not an obvious alternative?
5. **Evidence** — how do you know it works?
6. **Failure** — show a failure and how you reason about it.
7. **Trade-off** — what did you gain and pay?
8. **Changed condition** — what if scale/latency/data/requirements change?
9. **Production** — security, monitoring, retries, recovery, cost.
10. **Reflection** — what would you redo?

A resume item is ready when these ten directions do not force you to invent facts.

---

# 13. ELI5 mastery map

This is the **memory version**, not the evidence source.

## Experience

### Feedback platform

> Students submit suggestions and vote; the school follows up. I worked across building, deploying and maintaining it. I need to understand the user flow, what I personally owned, notification/state consistency, and what I would redesign.

### Career platform

> I inherited a real Laravel/Vue production system and worked on it for years. I added/fixed APIs, forms and workflows and dealt with production maintenance. I need one full request flow and real examples of my contribution, without pretending I built the whole platform.

### Queue / worker / scheduler

> Queue = waiting work. Worker = person/process doing the work. Scheduler = clock deciding when work should start. Retry can accidentally do the same side effect twice, so idempotency matters.

### Pac Com

> Earlier Laravel/Vue POS internship: simpler maintenance and UI/application fixes. Keep it honest and small.

## Text-to-SQL

> A user asks in English → LLM writes SQL → deterministic checks reject unsafe/invalid SQL → limited repair → read-only execution. The key lesson is: **runs successfully does not mean answers correctly.**

Remember:

> 75→90 = execution reliability. 33→39 = correctness-oriented EX result.

## Hybrid RAG

> BM25 is good at matching words; dense search is good at matching meaning. RRF combines their rankings because their raw scores are not directly comparable.

Remember:

> Better retrieval ≠ automatically better final answer.

## Video QA Agent

> Some video questions can be answered from speech; some require looking at the screen. The agent chooses transcript/frame/clip tools and returns evidence.

Remember:

> Hermes owns the core agent loop; I built the domain tools, evidence/eval/integration around it.

## Thesis

> The same sentence can mean different things depending on who says it to whom and what happened around it. Role KG retrieves role-related evidence; Context KG retrieves context/purpose-related evidence; DualKG combines them under a fixed evidence budget.

Remember:

> 0.6819 = semantic F1, not accuracy. The gain over Role alone is small, and the evaluation has real limitations.

## Backend / DB

> API: request comes in → validate → do business logic → talk to DB/dependency → return response.

> Index: extra lookup structure; faster reads, more write/storage cost.

> Transaction: use it when partial DB state would be invalid.

> Retry: useful, but dangerous if the operation can happen twice.

> Idempotency: repeating the same operation should not create a second unintended effect.

## Concurrency

> Concurrency = several tasks making progress around the same time. Parallelism = literally running at the same time on different cores/workers.

> Lock = only one task can change a critical piece of shared state at once.

## AI engineering

> Don't ask “Did the model produce something?” Ask “What does good mean, how do I test it, what can fail, and what happens in production?”

## AI Coding Assessment

> Three terminals share order state. `asyncio` handles many I/O connections; a lock protects check-and-update of shared state. The first SSH approach was too troublesome for the task, so I simplified the protocol and verified the smaller design.

## One universal answer shape

When blank, think:

> **Problem → Flow → My part → Why → Evidence → Failure/limit → Redo**

Do not mechanically recite all seven. Use them as anchors for whatever the interviewer actually asks.

---

# 14. Highest-risk gaps to fix before interview

1. **Real production bug story — still not fully recovered.** Need one genuine symptom → evidence → root cause → fix → verification story from Kahap if memory allows.
2. **Thesis 10,645 count provenance — currently not pinned by the clean repo audit.** Do not make up the derivation.
3. **Text-to-SQL “schema and values” wording — know default schema path vs separate value-grounding experiment.**
4. **Pac Com — keep conservative because source evidence is unavailable.**
5. **Human disagreement/collaboration story — still weaker than technical stories; relevant mainly if the round turns behavioral.

Stop rule: do not create another framework. Use this map to identify one weak concept/story, learn it, then return to mixed interview practice.