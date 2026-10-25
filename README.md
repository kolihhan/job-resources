# Job Search Inbox

Private operating inbox for the current search.

Current contract:

- **Singapore + Mainland China + Malaysia** = active markets;
- **Hong Kong = paused** as of 2026-10-23;
- main search = **permanent full-time only**;
- current execution mode = **high-throughput AI-career search**: search broadly inside AI-related work, not across all generic tech jobs.

Active role scope:

- Applied AI / AI Application / Generative AI;
- LLM / RAG / Agent / Coding Agent / Agent Harness;
- AI Backend / AI Software Engineer / AI-native Product Engineer;
- ML Engineer / NLP / Search / Retrieval / Ranking when meaningfully AI/ML-related;
- Agent/LLM evaluation / AI quality / AI testing when AI systems are the actual object of the work;
- **Research Engineer / AI Researcher / Applied Scientist / Research Scientist** when the hard requirements are realistic for this candidate;
- data-science roles only when the work is materially ML/AI, not generic BI/analytics.

A generic title such as `Software Engineer` or `Backend Engineer` may still survive **only when the actual team/product/JD is materially AI-related**. Pure generic SWE, ordinary QA/SDET, ordinary backend/full-stack, DevOps/SRE, security/networking and unrelated data roles are not target lanes merely because the candidate could technically perform them.

Research is explicitly allowed. Do not reject a role merely because it is research-oriented; instead check the real degree/publication/research-experience requirements. A hard PhD/publication/mature-research requirement the candidate does not satisfy remains a blocker.

Company quality determines **priority**, not baseline eligibility. A credible smaller company with real AI work may be better than a famous company offering unrelated generic software work.

Cheap hard skips remain: clearly closed/expired or duplicate roles; explicit non-permanent employment; explicit citizenship/right-to-work/no-sponsorship blockers where relevant; incompatible cohort; hard 4+/5+ mature professional-YOE floors; clearly mature ownership; hard PhD/research requirements not met; and substantial mandatory technical/domain mismatch.

Goal: maximize realistic interviews and offers **within an AI/ML career direction** without turning the search itself into another software project.

`discover AI-related roles broadly → cheap hard screen → read actual JD → confirm AI relevance → dedupe → verify serious survivors → user go → apply → follow up`

## Use these views

Do **not** work from the unfiltered Issues list.

- [NOW — ACTION + APPLY + CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20-label%3A%22status%3Await%22)
- [SG NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Asg%22%20-label%3A%22status%3Await%22)
- [CN NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Acn%22%20-label%3A%22status%3Await%22)
- [MY NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Amy%22%20-label%3A%22status%3Await%22)
- [HK WAIT / history](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Ahk%22)
- [ACTION](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aaction%22)
- [APPLY](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aapply%22)
- [CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Acheck%22)
- [WAIT / history](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Await%22)

`[TG]` only marks a Telegram / DeJob discovery source. It never means the role is verified.

## Four open states

- `[ACTION]` — something useful needs attention now or soon.
- `[APPLY]` — verified AI-related opportunity ready for review; still needs my exact `go`.
- `[CHECK]` — liveness is proven and exactly one blocker/decision remains.
- `[WAIT]` — already submitted/contacted and waiting.

Rejected, expired, duplicate, blocked, AI-direction-mismatch, withdrawn or intentionally skipped roles are closed.

## Simple commands

On an exact role:

- `go` — authorize that exact application/action.
- `applied` — I manually submitted it.
- `skip` — close it as intentionally skipped.

`go all ACTION applications` authorizes all current application-type ACTION items, but not interview/OA ACTION items. `[APPLY]` by itself is never submission permission.

## Source of truth

- GitHub Issues = live operational opportunity state.
- Gmail = receipts, recruiter/OA/interview/rejection evidence and targeted dedupe.
- [`PROFILE.md`](PROFILE.md) = stable candidate facts and current market/role scope.
- [`RULES.md`](RULES.md) = the only detailed execution policy.
- [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md) = latest discovery receipt/cursor + next rotation only.
- Old spreadsheet = legacy/read-only.

## Search model

Maintenance comes before discovery. Raw discovery candidates never become Issues automatically.

- **SG:** FreeHire can remain a broad raw radar because AI jobs may use generic SWE/backend titles, but promotion requires reading the JD/team/product and confirming material AI/ML relevance. Add direct employer/ATS + LinkedIn/JobStreet/Indeed gaps.
- **CN:** native-source-first — BOSS, official/campus, 牛客, 51job, 智联, 猎聘 — plus FreeHire/other feeds. Search AI应用、大模型、Agent、RAG、算法/ML/NLP、AI后端、评测 and AI research/research-engineering lanes.
- **MY:** search AI/ML/GenAI/LLM/Agent/AI software and realistic AI research roles. Strong companies/teams are preferred but not required.
- **HK:** paused.

All active markets use the same hard gates: material AI/ML relevance, current liveness, permanent full-time employment, realistic early-career/cohort fit, truthful hard-requirement fit, dedupe, work-authorization classification where relevant, and a usable exact application route.

Unknown SG/CN sponsorship willingness is allowed at APPLY. Explicit no-sponsorship/right-to-work/citizenship blockers are not. Singapore MCF-only routes are blocked.

## What I should do

1. Handle `ACTION` first.
2. Review `APPLY` and give `go` only for exact roles I want.
3. Resolve useful `CHECK` blockers.
4. Leave `WAIT` alone unless new evidence arrives.

## Automation

Scheduled maintenance keeps Issues synchronized with recruiting evidence. Discovery rotates **AI-related** role/source lanes across SG/CN/MY. HK stays paused until explicitly reactivated.

The latest scheduled run leaves one compact receipt in [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md). If strategy changes, update `PROFILE.md` / `RULES.md` once rather than copying policy into prompts or another tracker.

See [`PROFILE.md`](PROFILE.md), [`RULES.md`](RULES.md), and [dated market evidence](docs/market-facts-2026-10-01.md).