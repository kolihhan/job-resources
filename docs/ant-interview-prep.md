# Ant International — Applied AI Engineer Interview Prep

Updated: 2026-10-21 (MYT)

This is the compact execution page for the Ant International Malaysia Applied AI Engineer (Fresh Graduate) interview. It does **not** replace the detailed evidence docs. It freezes the preparation scope so the remaining work is learning and practice, not inventing more frameworks.

## 1. Source of truth

Use these in this order:

1. `resumes/resume-en-current.md` — what the interviewer can directly attack.
2. `docs/ant-project-deep-dive-coverage.md` — adversarial resume-wide coverage map, including work experience, all four projects, skills/fundamentals, and the Ant coding assessment.
3. `docs/interview-resume-knowledge-map.md` — project architecture, metrics, red lines, safe claims.
4. `docs/interview-resume-job-experience.md` — Kahap / production feedback platform / Career / Pac Com evidence.
5. `docs/ant-interview-answer-framework.md` — reusable answer shapes and Field Guide-derived reasoning patterns.
6. `docs/ua-get-job-full-audit.md` — what Understand Anything / repo audit was actually completed.
7. `kolihhan/job-project/docs/*` — recovered Career / feedback-platform source archaeology and UA graph artifacts.
8. Current Ant International JD + recent Malaysia interview evidence — role-specific weighting only.

Repository evidence wins over ChatGPT memory. Official Ant JD wins over anonymous interview reports for role expectations. Anonymous reports are pattern evidence, not guarantees of the exact Oct 23 interview format.

---

## 2. Evidence status

### Resume projects

| Resume project | Evidence status |
|---|---|
| Text-to-SQL | FULL local Understand Anything pipeline completed; final knowledge graph available |
| Hybrid RAG | FULL local Understand Anything pipeline completed; final knowledge graph available |
| Video QA | FULL local Understand Anything pipeline completed; final knowledge graph available |
| M.S. thesis | Source/evaluation audit completed for resume claims; **not** a literal local `/understand --full` graph run |

All four are traceable enough for interview preparation, but the thesis evidence path is different from the other three.

### Work experience

| Experience | Evidence status |
|---|---|
| Kahap — production feedback platform | FULL recovered-source UA graph + code archaeology; production ownership partly USER-confirmed |
| Kahap — production career platform | FULL recovered-source UA graph + full Git history / confirmed author identities |
| Pac Com POS | No recovered source repo / Git evidence; USER-memory evidence only |

Do not use Career evidence to strengthen Pac Com claims.

### Ant format

Strong enough to prepare, not strong enough to claim an exact script. Current evidence supports emphasis on:

- project/resume deep dive
- backend services / APIs / databases
- practical coding / problem solving
- testing and debugging
- AI-native workflows and critical validation of AI output
- correctness, reliability, ownership and communication
- possible live coding / implementation and DB/fundamentals follow-ups

Recent China Ant “large-model application” first-round evidence is useful as **corroboration only**. It independently showed a mixed interview covering internship/business depth, architecture/selection/performance/high availability, AI project depth around memory/context/evaluation, backend fundamentals such as MySQL/MQ, Agent concepts such as MCP/Skill, and coding. This strengthens the working model that Ant application-AI interviews can mix **business/project depth + backend engineering + AI/Agent judgment + coding**.

Do **not** promote China-specific details into Malaysia predictions. In particular, this does not establish that MySQL redo/undo/binlog, MQ internals, MCP/Skill, Java Collections, or Hot100 will appear in the Oct 23 KL interview.

Unknown: exact first-round sequence, exact language, whether the coding assessment is reviewed, and whether live coding occurs in this specific round.

---

## 3. Frozen preparation categories

Do not create a new top-level category unless strong evidence proves an independent missing capability.

### 1. Resume / Project / Experience Deep Dive

- exact ownership
- architecture / request/data flow
- design decision and trade-off
- metric + denominator + meaning
- failure mode / debugging
- realistic improvement
- business purpose / production value when relevant

### 2. Engineering Fundamentals

- practical coding / problem solving
- Python/data structures
- API/backend request flow
- SQL/database fundamentals
- testing/debugging
- timeout/retry/idempotency
- transaction/index/locking/concurrency
- queue / asynchronous-work reliability at a practical level
- basic security/input validation
- light system reasoning

### 3. AI-native Engineering

- clarify requirements
- give AI agents sufficient context and constraints
- inspect generated implementation
- identify incorrect assumptions / unsafe output
- test happy path + edge cases + failure path
- evaluate AI systems with task-specific evidence
- memory/context-management trade-offs when relevant
- understand Agent/tool concepts such as tool selection, MCP and reusable skills at an application-engineering level
- retain human accountability for correctness/security/reliability

### 4. Communication / Behavioural

- concise English/Mandarin technical explanation
- ownership / failure / learning / collaboration stories
- why Ant / why this role
- communicate uncertainty without bluffing

Everything maps back into these four areas.

---

## 4. Execution method — grill first, then mastery, then mock

The old approach of walking one project through a long sequential question tree was too narrow. Do **not** resume that pattern.

### Phase A — GRILL COVERAGE

Before drilling answers, use `docs/ant-project-deep-dive-coverage.md` to attack the whole visible resume.

For every visible claim ask:

```text
What can the interviewer challenge?
→ what evidence supports it?
→ what is CODE/EVAL/USER/INFERENCE/UNKNOWN?
→ what wording would overclaim?
→ what underlying concept can the claim pivot into?
```

The goal is to expose blind spots, not to memorize every question.

### Phase B — ELI5 MASTERY

For each anchor, reduce the verified evidence into a simple mental model. A resume item is mastered when Ko can explain without notes:

```text
Problem
→ Flow
→ My part
→ Why
→ Evidence
→ Failure / limitation
→ Redo / changed condition
```

Do not mechanically recite all seven. They are anchors used according to the interviewer question.

For theory/fundamentals use:

```text
plain definition
→ why/when useful
→ trade-off
→ example from real work/project
```

### Phase C — MIXED INTERVIEW PRACTICE

Only after coverage and ELI5 mastery, use realistic mixed questions. Do not keep drilling one project until every possible question is exhausted.

A realistic sequence may jump:

```text
self-intro
→ work/project ownership
→ architecture
→ DB/backend concept
→ changed condition/failure
→ another project
→ AI validation/eval
→ coding/reliability
→ motivation/behavioural
```

Per actual spoken answer:

1. Ask one realistic question.
2. Candidate answers naturally without reading a script.
3. Grade `✅ / ⚠️ / ❌`.
4. Separate factual/evidence error from communication weakness.
5. Fix only the biggest gap.
6. Retry or move to one natural follow-up.

Do not dump a new syllabus after every answer.

---

## 5. Resume mastery order

Coverage is resume-wide; learning depth is weighted by interview value.

1. **Self-intro / profile story** — NTHU NLP/LLM + production backend + applied-AI projects.
2. **Text-to-SQL** — deepest: validation, safety, repair, metrics, failure analysis.
3. **Kahap production engineering** — feedback platform + Career, request flows, DB, queues/workers/schedulers, deployment/migration/SSL.
4. **Ant AI Coding Assessment** — asyncio, shared state, lock/concurrency, debugging, AI-assisted implementation and verification.
5. **Hybrid RAG** — lexical/dense/RRF, evaluation, retrieval-vs-generation boundary, trade-offs.
6. **Video QA Agent** — dynamic tool/evidence choice, ownership boundary, evidence/abstention/evaluation.
7. **Thesis** — plain-language problem, Role/Context/DualKG, semantic F1, research/evaluation limitations.
8. **Backend/DB/Python/reliability + practical Agent fundamentals** — mixed through real project anchors: transaction/index/locking/concurrency, queues/retries/idempotency, context/evaluation/tool selection/MCP/Skill concepts. Do not turn this into a detached China-style 八股 syllabus.
9. **Pac Com** — conservative early-internship explanation only.
10. **Behavioural / why Ant** — small set of real stories; no fabricated production incident or team conflict.
11. **Full mixed mock**.

---

## 6. Interview-ready gate

A resume item is ready only when the candidate can, without notes:

- explain it in 30–60 seconds
- state personal ownership precisely
- trace the main request/data flow
- defend one design decision
- explain the headline metric without exaggeration
- name one real limitation/failure mode
- answer a deeper engineering follow-up
- handle one changed-condition question
- propose one reasonable improvement
- distinguish verified evidence from inference or memory

Do not mark ready because a document exists or because ChatGPT can answer it.

---

## 7. Current Grill findings / high-risk gaps

### Verified important risks

1. **Production incident story remains weak.** Source/config proves architecture and potential failure modes, but not a specific real outage. Do not fabricate symptom/root cause/fix history.
2. **Text-to-SQL resume wording:** “schema and values” is broader than the default headline guarded Qwen path. Main path is schema-grounded; value grounding is a separate experiment.
3. **Text-to-SQL metric trap:** 75→90 is execution success; 33→39 is correctness-oriented EX-compatible result.
4. **RAG metric trap:** retrieval improvement does not prove generated-answer improvement.
5. **Video QA integrity:** Hermes owns the core agent loop; the post-hoc 12/12 re-score is not a fresh run and is not the headline benchmark.
6. **Thesis metric trap:** 0.6819 is semantic response-matching F1, not accuracy or classification macro-F1; Role→Dual improvement is small.
7. **Thesis dataset-count provenance:** resume says 10,645 workplace dialogue turns; the current clean audit has not pinned the exact derivation. Do not improvise if challenged.
8. **Pac Com evidence is memory-only.** Keep it small and honest.
9. **Human disagreement/collaboration story is less well established than technical stories.** Do not convert annotation/evaluator disagreement into a teammate-conflict story.

### Direct Ant-specific prep risk

The AI Coding Assessment is high preparation value but **unknown interviewer probability**. Know it cold without claiming the first round will definitely review it.

The new CN large-model-application report increases confidence in the **mixed engineering + AI judgment** interview model, but it should not trigger a last-minute pivot into memorizing deep MySQL/MQ trivia or a large Hot100 set. The remaining highest-value work is still spoken project depth, backend/reliability reasoning, AI validation/evaluation, and changed-condition follow-ups.

---

## 8. Current speaking progress

### Self-introduction — `GOOD / keep natural`

Current content is sufficient:

> Hi, I’m Ko Lih Han. I recently completed my master’s degree at NTHU, where my work focused mainly on NLP and LLM-related topics. While studying, I also worked part-time as a software engineer, mostly on backend and production web systems. I also worked on several applied AI projects, including Text-to-SQL, retrieval, and agent-based systems.

Do not force “therefore I am interviewing for Applied AI Engineer” into the intro unless asked.

### Text-to-SQL problem framing — `PARTIAL / concept correct`

Candidate correctly understands:

> non-SQL user → natural-language question → generated SQL → database result

Still needs project-level mastery of verifier/safety, repair, metrics, failure distinction and ownership; do not continue as a narrow Q1→Q2→Q3 ladder. Use the resume-wide coverage map first.

---

## 9. Interviewer Chase Mode — default live practice

From now on, when Ko says `go`, `mock`, `interview me`, or continues an active interview session, default to **Interviewer Chase Mode** rather than teaching first.

### Interviewer behavior

- Act like the interviewer, not the tutor, until an answer exposes a real gap.
- Ask exactly **one question at a time**.
- Choose the next question from what Ko just said: ownership claim, architecture detail, metric, failure, trade-off, changed condition, production implication, business value, or a natural pivot to backend/DB/AI fundamentals.
- Do not reveal the planned follow-up tree in advance.
- Do not exhaust one project mechanically. Stay on it while the answer creates useful depth, then pivot naturally across the resume.
- Use `docs/ant-project-deep-dive-coverage.md` and the evidence docs as the hidden coverage map, not as a script.
- Prefer questions grounded in visible resume claims and verified repo evidence.
- A realistic interviewer may challenge an imprecise number or overclaim immediately.

### After each candidate answer

Keep feedback short:

1. `✅ / ⚠️ / ❌`
2. State the **single biggest issue** only.
3. If there is a factual/evidence mistake, correct it before communication polish.
4. If the answer is basically correct, do not rewrite it just to sound prettier.
5. Ask the next interviewer question immediately.

Only switch into ELI5 teaching when Ko is genuinely missing the concept or explicitly asks for explanation. After teaching the smallest missing concept, return to interviewer mode.

### Evaluation dimensions

Do not collapse everything into one vague score. Internally distinguish:

- factual / evidence correctness
- technical reasoning
- ownership boundary
- metric interpretation
- clarity / natural spoken English
- engineering judgment

But surface only the most important issue per turn unless Ko asks for a full review.

### Interview realism

The interviewer may:

- interrupt a vague answer with `What exactly do you mean by ...?`
- challenge a metric: `Does 90% mean accuracy?`
- change one condition: `What if there are 1,000 tables?`
- move from project to fundamentals: `Why would a transaction help here?`
- pivot from AI design to engineering: `How would you make this reliable in production?`
- challenge ownership: `What part did you personally implement?`
- challenge evidence: `How do you know that actually improved the system?`
- ask for business/production impact rather than accepting a purely technical explanation
- ask for one concrete failure instead of accepting abstractions.

Do not manufacture obscure trivia just to make the interview harder. Difficulty should come from depth, changed conditions, evidence, and reasoning.

### Current starting point

Self-introduction is already acceptable. Start the next mock from a natural follow-up into an AI project, preferably Text-to-SQL, then chase the candidate's actual answer rather than following a prewritten sequence.

---

## 10. Stop rules

- Do not create another interview framework/tracker/question-bank file.
- Do not turn the coverage map into a list to memorize word-for-word.
- Do not grind one project through every P0/P1/P2 question sequentially.
- Do not claim exact Ant interview format from anonymous reports.
- Do not replace project evidence with textbook answers.
- Do not overstate Pac Com, feedback platform/Career ownership, Hermes ownership, thesis metrics, or Text-to-SQL accuracy.
- Do not pivot into memorizing China-specific MySQL/MQ/Hot100 trivia solely because one Ant large-model-application report included it.
- When a gap is found, update the existing source of truth and learn the smallest missing concept/story.
- After coverage is stable, spend time on recall and mixed interview practice rather than more meta-analysis.
