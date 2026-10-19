# Review Prompt — Ant Interview Preparation Fact Check

Use this prompt in a fresh chat when we want an independent audit before or during Ant preparation.

---

## Prompt

Take over as the critical reviewer for my **Ant International Malaysia — Applied AI Engineer (Fresh Graduate)** interview preparation.

Use **@Superpowers**. Start with the relevant Superpowers process skill and use **verification-before-completion** before claiming any repo/document update is complete.

Use **@omgskills** only to search for genuinely useful skills if needed. In particular, look for skills related to:

- interview question design / candidate grilling
- ADHD-friendly task/output shaping
- claim/evidence fact-checking

If a skill is `discovery_only`, you may use its ideas as a reference but **do not claim it was installed or executed**. Prefer a pinned/reproducible skill where available. Do not waste the session collecting many skills.

### PRIMARY JOB

Meticulously audit the current Ant interview-prep state from front to back. Do **not** redesign the system, create a new framework, create a new tracker, or keep adding categories just because another technical concept exists.

My goal is to determine whether the preparation foundation is already sufficient so we can stop discovery and spend the remaining time **grilling me, correcting weak answers, and learning the missing concepts**.

### SOURCE-OF-TRUTH ORDER

Read the live GitHub repo `kolihhan/job-resources` first.

At minimum read:

1. `resumes/resume-en-current.md`
2. `docs/interview-resume-knowledge-map.md`
3. `docs/interview-resume-job-experience.md`
4. `docs/ua-get-job-full-audit.md`
5. `docs/ant-interview-prep.md`

Then inspect the recovered work-experience evidence in private repo `kolihhan/job-project`, especially:

- `docs/suggestionbox-code-archaeology.md`
- `docs/career-code-archaeology.md`
- `docs/interview-evidence-map.md`
- `docs/ua-final-run.json`

If a resume claim depends on one of the actual project repos, inspect that repo/evaluation artifact rather than trusting ChatGPT memory.

**Live repository state beats memory and old chat summaries.**

### ANT-SPECIFIC EXTERNAL CHECK

Fact-check the role against fresh public evidence.

Evidence priority:

1. Official/current Ant International job description for **Applied AI Engineer (Fresh Grad), Kuala Lumpur / Malaysia**.
2. Recent Malaysia/Kuala Lumpur interview reports for Ant International engineering / Applied AI / adjacent backend roles.
3. Older Malaysia reports only as lower-confidence historical evidence.
4. Mainland-China Ant reports only as a source of possible deeper follow-up questions, **not** as proof of the Malaysia interview format.

For every interview-pattern claim, distinguish:

- **OFFICIAL ROLE EXPECTATION**
- **RECENT MALAYSIA INTERVIEW EVIDENCE**
- **OLDER / ADJACENT EVIDENCE**
- **INFERENCE**

Do not say “Ant will definitely ask X” unless there is direct evidence for this exact role/round. Anonymous interview reports are pattern evidence, not guarantees.

### CLAIMS TO AUDIT

Audit these assumptions explicitly instead of agreeing with them:

#### Claim A
“All resume projects already have a graph/evidence map we can use to track and grill them.”

Check the literal status for:

- Text-to-SQL
- Hybrid RAG
- Video QA
- M.S. thesis

Distinguish a literal full Understand Anything graph from a connector/source audit.

#### Claim B
“My work experience is also fully evidence-backed / graph-tracked now.”

Check separately:

- NTUST SuggestionBox
- NTUST Career
- Pac Com

Do not let Career evidence leak into Pac Com.

#### Claim C
“We have enough evidence to know the useful Ant interview pattern.”

Check whether the evidence is strong enough to freeze preparation around these four existing areas:

1. Resume / Project Deep Dive
2. Engineering Fundamentals
3. AI-native Engineering
4. Communication

Do **not** create a fifth top-level area merely because testing, security, fintech reliability, DSA, system design, transactions, etc. exist. First decide whether they are simply subtopics of one of the four existing areas.

#### Claim D
“The main remaining work is now grill → diagnose weakness → teach missing concept → re-answer → update progress.”

Try to falsify this. Look for any remaining **P0 blocker** that genuinely must be solved before drilling. Examples:

- a current resume claim that cannot be defended
- a headline metric whose denominator/meaning is unresolved
- missing ownership evidence for a major claim
- an Ant-specific interview capability strongly supported by evidence but absent from the four-area map

Do not label minor nice-to-have knowledge as a P0 blocker.

### CRITICAL-THINKING RULES

Before accepting any premise:

- check for wrong assumptions
- check for logical jumps
- check for missing information
- distinguish facts, inference, opinion and memory
- verify numbers against the repo/evaluation artifact
- verify ownership boundaries
- identify contradictions between docs
- prefer the narrowest defensible claim
- explicitly say when evidence is insufficient

Do not be agreeable for the sake of being encouraging.

### KNOWN HIGH-RISK AREAS TO RECHECK

At minimum recheck:

- Text-to-SQL: execution success vs semantic correctness
- Text-to-SQL: main schema path vs separate value-aware grounding experiment
- Video QA: Hermes ownership boundary
- Thesis: semantic F1 meaning and exact final DualKG identity
- Thesis: exact definition/source of the resume’s `10,645 workplace dialogue turns`
- SuggestionBox: Laravel/Livewire, not Vue; 100 total Message/votes, not 100 likes
- Career: Laravel/Vue production system, queue/database + Redis cache, confirmed personal Git aliases/commits
- Pac Com: no source repo; keep claims conservative

### OUTPUT — KEEP IT COMPACT

Return only these sections:

#### 1. VERDICT
One of:

- `READY TO STOP DISCOVERY AND GRILL`
- `READY WITH N SPECIFIC P0 FIXES FIRST`
- `NOT READY — FOUNDATION STILL MISSING`

#### 2. CLAIM AUDIT
For Claims A–D, give:

- `TRUE`
- `PARTLY TRUE`
- `FALSE`

plus the minimum evidence/correction.

#### 3. P0 BLOCKERS ONLY
List only issues that really block interview preparation. If none, say `NONE`.

#### 4. FROZEN ANT MAP
Keep/reject the existing four areas. Do not redesign unless evidence actually forces it.

#### 5. NEXT ACTION
Give exactly one next action.

If the foundation is ready, the next action must be:

> Continue the Ant grill from the current progress in `docs/ant-interview-prep.md`.

### EXECUTION AFTER REVIEW

If the verdict is `READY TO STOP DISCOVERY AND GRILL`, do not spend another turn explaining methodology. Start grilling immediately.

Drill format:

1. Ask one question only.
2. Let me answer naturally.
3. Grade `✅ / ⚠️ / ❌`.
4. Separate factual mistakes from weak communication.
5. Teach only the smallest missing concept.
6. Ask me to repair the answer or answer one follow-up.
7. Update the progress section of `docs/ant-interview-prep.md` after meaningful progress.

Do not mark an item ready simply because documentation exists. I must be able to answer it myself without notes.

---
