# Job Search Inbox

Private operating inbox for the current search.

## North star

Maximize the probability of getting a **permanent full-time AI-related offer I would genuinely accept**.

Do not optimize for raw application count, raw callback count, Issue count, or interview count in isolation. Those are funnel signals only.

Current contract:

- **Singapore + Mainland China + Malaysia** = active markets;
- **Hong Kong = paused** as of 2026-10-23;
- main search = **permanent full-time only**;
- current execution mode = **divide-and-conquer AI career search** across six battlefields, not one undifferentiated queue.

## Six battlefields

| Battlefield | Purpose |
|---|---|
| `SG-ENG` | High-quality AI engineering roles where the work and employer justify Singapore work-pass friction. |
| `SG-RES` | MSc-compatible research engineering / applied research roles with realistic degree/publication requirements. |
| `CN-ENG` | Higher-throughput AI engineering search using native/direct routes, with fast filtering for foreign-hire and cohort blockers. |
| `CN-RES` | Research engineering / applied research roles with realistic MSc-level requirements and foreign-hire feasibility. |
| `MY-ENG` | **TOP / destination-quality only**: strong employer/team, meaningful AI ownership, compensation/WLB/growth upside. Not a generic fallback lane. |
| `MY-RES` | **TOP / destination-quality only** research or research-engineering roles with strong technical environment and career upside. |

Engineering and research are both valid career outcomes. Weekly strategy review reallocates effort across the six battlefields based on real funnel evidence rather than a fixed market split.

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

Company quality determines priority in SG/CN. In Malaysia, the bar is intentionally higher: ordinary low-upside roles are not queue-worthy just because they are AI-related.

Cheap hard skips remain: clearly closed/expired or duplicate roles; explicit non-permanent employment; explicit citizenship/right-to-work/no-sponsorship blockers where relevant; incompatible cohort; hard 4+/5+ mature professional-YOE floors; clearly mature ownership; hard PhD/research requirements not met; and substantial mandatory technical/domain mismatch.

Operating loop:

`scout by battlefield → cheap hard screen → read actual JD → confirm AI relevance → dedupe → verify serious survivors → user review/go → apply → observe funnel → weekly rebalance`

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

Do not encode strategy priority using ad-hoc title markers such as `[TOP]`. Priority comes from battlefield fit, current evidence and the weekly strategy review.

## Simple commands

On an exact role:

- `go` — authorize that exact application/action.
- `applied` — I manually submitted it.
- `skip` — close it as intentionally skipped.

`go all ACTION applications` authorizes all current application-type ACTION items, but not interview/OA ACTION items. `[APPLY]` by itself is never submission permission.

## Source of truth

- GitHub Issues = live operational opportunity state.
- Gmail = receipts, recruiter/OA/interview/rejection evidence and targeted dedupe.
- [`PROFILE.md`](PROFILE.md) = stable candidate facts + battlefield/market strategy.
- [`RULES.md`](RULES.md) = the only detailed execution policy.
- [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md) = latest verified discovery/maintenance receipt + FreeHire cursor only.
- Old spreadsheet = legacy/read-only.

## Search model

Raw discovery candidates never become Issues automatically.

- **SG:** quality-first. Search both engineering and research lanes. FreeHire can remain broad raw radar because AI jobs may use generic titles, but promotion requires actual JD/team/product AI relevance and a role worth the work-pass friction. Fill gaps with direct employer/ATS + LinkedIn/JobStreet/Indeed.
- **CN:** higher-throughput and native-source-first — BOSS, official/campus, 牛客, 51job, 智联, 猎聘 — plus supplementary feeds. Search both engineering and research lanes, then cheaply eliminate cohort/foreign-hire/hard-fit blockers.
- **MY:** TOP/destination-quality only. Search strong MNCs, serious AI product/R&D teams, strong banks/digital banks and high-upside AI companies. Ordinary low-upside roles do not enter the queue merely because they contain AI keywords.
- **HK:** paused.

All active markets still use the same hard gates: material AI/ML relevance, current liveness, permanent full-time employment, realistic early-career/cohort fit, truthful hard-requirement fit, dedupe, work-authorization classification where relevant, and a usable exact application route.

Unknown SG/CN sponsorship willingness is allowed at APPLY. Explicit no-sponsorship/right-to-work/citizenship blockers are not. Singapore MCF-only routes are blocked.

## What I should do

1. Handle `ACTION` first.
2. Review `APPLY` and give `go` only for exact roles I want.
3. Resolve useful `CHECK` blockers.
4. Leave `WAIT` alone unless new evidence arrives.

## Automation

Automation is reconnaissance and feedback, not autonomous application execution.

- SG AI Scout: hourly, read-only.
- CN AI Scout: hourly, read-only.
- MY TOP AI Scout: hourly, read-only.
- Recruiting Signal Watch: hourly condition watch over both Gmail accounts; ordinary receipts do not count as meaningful progression.
- AI Job Strategy Review: weekly; evaluates `SG-ENG`, `SG-RES`, `CN-ENG`, `CN-RES`, `MY-ENG`, `MY-RES` and recommends next-week effort allocation from real funnel evidence.

Scouts may search, verify, dedupe, classify and recommend. They do **not** submit applications, contact employers, or mutate GitHub/Gmail state. Scheduler prompts must read the current repo contract rather than maintain private copies of policy.

See [`PROFILE.md`](PROFILE.md), [`RULES.md`](RULES.md), and [dated market evidence](docs/market-facts-2026-10-01.md).