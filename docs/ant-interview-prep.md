# Ant International — Applied AI Engineer Interview Prep

Updated: 2026-10-19 (MYT)

This file is the compact execution page for the Ant International Malaysia Applied AI Engineer (Fresh Graduate) interview. It does **not** replace the detailed evidence docs. It freezes the preparation scope so we stop redesigning the map and spend the remaining time drilling.

## 1. Source of truth

Use these in this order:

1. `resumes/resume-en-current.md` — what the interviewer can attack.
2. `docs/interview-resume-knowledge-map.md` — project architecture, metrics, red lines, safe claims.
3. `docs/interview-resume-job-experience.md` — Kahap / Career / SuggestionBox / Pac Com evidence.
4. `docs/ua-get-job-full-audit.md` — what Understand Anything / repo audit was actually completed.
5. `kolihhan/job-project/docs/*` — recovered Career / SuggestionBox source archaeology and UA graph artifacts.
6. Current Ant International JD + recent Malaysia interview evidence — role-specific weighting only.

Repository evidence wins over ChatGPT memory. Official Ant JD wins over anonymous interview reports for role expectations. Anonymous reports are pattern evidence, not guarantees of the exact Oct 23 interview format.

---

## 2. Fact-check of current assumptions

### A. “All resume projects have a graph we can track.”

**Mostly true, but not literally all four.**

| Resume project | Status |
|---|---|
| Text-to-SQL | FULL local Understand Anything pipeline completed; final knowledge graph available |
| Hybrid RAG | FULL local Understand Anything pipeline completed; final knowledge graph available |
| Video QA | FULL local Understand Anything pipeline completed; final knowledge graph available |
| M.S. thesis | Connector-based source/eval audit completed for resume claims; **not** a literal local `/understand --full` graph run |

Therefore the practical claim is:

> All current resume projects are traceable enough for interview preparation; three public project repos have full UA graphs, while the private thesis has a source/evaluation audit rather than a literal local UA graph.

### B. “Work experience also has graphs/evidence now.”

**Partly true.**

| Experience | Status |
|---|---|
| Kahap — NTUST SuggestionBox | FULL recovered-source UA graph + code archaeology |
| Kahap — NTUST Career | FULL recovered-source UA graph + full Git history / confirmed author identities |
| Pac Com POS | No recovered source repo / Git evidence; remains USER-memory evidence only |

Do not use Career evidence to strengthen Pac Com claims.

### C. “We know the Ant interview pattern.”

**Strong enough to prepare, not strong enough to claim an exact script.**

Current official role evidence strongly emphasizes:

- requirement clarification through deployment
- backend services and APIs
- databases and core software engineering
- validation, debugging and production feedback
- AI-native workflows across implementation/testing/debugging/documentation
- giving AI agents context and constraints
- critically validating AI outputs
- code review, ownership, communication, correctness/security/reliability

Recent Kuala Lumpur Ant interview reports for adjacent engineering roles add evidence for:

- project/resume discussion
- backend implementation or live coding
- Java/CS fundamentals depending on interviewer/role
- database/indexing
- easy–medium DSA in some backend loops
- concurrency/locking in older backend loops
- practical reliability scenarios such as timeout/retry/duplicate side effects

This supports the preparation taxonomy below. It does **not** prove the exact first-round sequence for this Applied AI Fresh Grad interview.

---

## 3. Frozen Ant preparation map

Do not add a new top-level category unless new strong evidence proves a missing independent capability.

### 1. Resume / Project Deep Dive

- exact ownership
- architecture / data flow
- design decision and trade-off
- metric + denominator + meaning
- failure mode
- debugging story
- realistic improvement

### 2. Engineering Fundamentals

- practical coding / problem solving
- API / backend request flow
- SQL / database fundamentals
- testing and debugging
- timeout / retry / idempotency
- transaction / index / basic locking and concurrency
- basic security and input validation
- light system reasoning only

### 3. AI-native Engineering

- clarify requirement
- give the AI sufficient context and constraints
- inspect generated implementation
- identify incorrect assumptions / unsafe output
- test happy path + edge cases + failure path
- fix and verify
- retain human accountability for correctness/security/reliability

### 4. Communication

- explain reasoning clearly
- concise English and Mandarin technical explanation
- ownership / collaboration / failure-learning stories
- why Ant / why this role

Everything else maps back into these four areas. Fintech correctness belongs under Engineering Fundamentals. AI code review belongs under AI-native Engineering. Ownership belongs under Resume / Projects.

---

## 4. Drill method — the only execution loop

Do **not** study each concept as a separate course.

For each anchor project:

```text
Interviewer asks project overview
→ ownership
→ architecture / flow
→ why this design
→ failure / edge case
→ testing / debugging
→ metric interpretation
→ AI usage / validation if relevant
→ backend/DB scenario if relevant
→ improvement / trade-off
```

Per question:

1. Ask exactly one interview question.
2. Candidate answers naturally without reading a script.
3. Grade `✅ / ⚠️ / ❌`.
4. Separate factual error from communication weakness.
5. Teach only the smallest missing concept.
6. Ask candidate to repair the answer or answer one follow-up.
7. Record progress below.

Do not dump the entire syllabus after every answer.

---

## 5. Drill order

1. **Text-to-SQL** — Applied AI + validation + safety + metrics + failure analysis.
2. **Career** — production backend + API/DB + debugging + queue/worker/scheduler + migration.
3. **Hybrid RAG** — retrieval signals + RRF + evaluation + trade-offs.
4. **Video QA** — agent/tool ownership + evidence + abstention + evaluation.
5. **Thesis** — plain-language problem + Role/Context/DualKG + semantic F1 + limitations.
6. **SuggestionBox** — ownership + Laravel/Livewire + request/data flow + deployment.
7. **Pac Com** — conservative early-internship explanation only.
8. Mixed coding/backend/reliability scenarios.
9. Behavioural + why Ant.
10. Full mixed mock.

---

## 6. Interview-ready gate

A resume item is ready only when the candidate can, without notes:

- explain it in 30–60 seconds
- state personal ownership precisely
- trace the main request/data flow
- defend one design decision
- explain the headline metric without exaggeration
- name one real limitation/failure mode
- answer one deeper engineering follow-up
- propose one reasonable improvement

Do not mark ready because a document exists or because ChatGPT can answer it.

---

## 7. Progress log

### 2026-10-19 — Loop 1: Text-to-SQL

**Q1:** Walk through the Text-to-SQL project: problem, end-to-end flow, personal implementation.

**Candidate answer status:** `⚠️ PARTIAL`

What was already correct:

- goal: allow a non-SQL user to query a database in natural language
- natural-language input → LLM SQL generation
- validate before use
- failed query enters LLM repair with error context
- bounded repair budget of 2

Missing / needs repair:

- personal ownership was not stated
- validation was described mainly as executability; must also explain deterministic safety/read-only boundary
- benchmark description was too vague (“open-source DB”); current evaluated headline is 100 frozen BIRD DEV queries on SQLite databases
- must keep execution success separate from semantic correctness

**Next question:**

> Why did you add deterministic validation and bounded repair instead of simply prompting the LLM to generate better SQL directly?

### Current status

- Text-to-SQL overview: `⚠️`
- Text-to-SQL verifier/safety: `NOT YET DRILLED`
- Text-to-SQL metrics: `NOT YET DRILLED`
- Text-to-SQL failure modes: `NOT YET DRILLED`
- Career: `NOT STARTED`
- RAG: `NOT STARTED`
- Video QA: `NOT STARTED`
- Thesis: `NOT STARTED`
- SuggestionBox: `NOT STARTED`
- Pac Com: `NOT STARTED`
- mixed coding/backend: `NOT STARTED`
- behavioural/why Ant: `NOT STARTED`

---

## 8. Stop rules

- Do not create another interview framework or tracker.
- Do not turn every newly discovered concept into a new study category.
- Do not claim exact Ant interview format from anonymous reports.
- Do not replace project evidence with memorized textbook answers.
- Do not overstate Pac Com, SuggestionBox, Career, Hermes ownership, thesis metrics, or Text-to-SQL accuracy.
- When a gap is found, attach it to one of the four frozen Ant categories and continue drilling.
