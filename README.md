# Job Search Inbox

Private operating inbox for the current search.

Current contract:

- **Singapore + Mainland China + Malaysia** = active markets;
- **Hong Kong = paused** as of 2026-10-23: do not discover or promote new HK roles until the user explicitly reactivates HK;
- main search = **permanent full-time only**;
- current execution mode = **high-throughput application generation**: find and verify any realistically applicable early-career engineering opportunity, with stronger companies/teams and Applied-AI roles prioritized first rather than used as eligibility gates.

Active role scope:

- Applied AI / AI Application / LLM / RAG / Agent / AI backend remain the preferred lane;
- general backend / full-stack / software engineer roles are active;
- test-development / SDET / QA automation roles are active when the stack is realistically learnable;
- Python / Java / PHP application engineering and adjacent early-career software roles are active;
- data/search/retrieval/platform roles may survive when the mandatory stack and ownership level are realistically compatible.

Do **not** reject a role merely because it is not Applied AI, because the company is ordinary, or because part of the stack is learnable rather than already on the resume. Company/team quality determines **priority**, not baseline eligibility.

Cheap hard skips remain: clearly closed/expired or duplicate roles; explicit non-permanent employment; explicit citizenship/right-to-work/no-sponsorship blockers where relevant; clearly incompatible cohort; hard 4+/5+ mature professional-YOE floors; Staff/Lead/Manager or clearly mature ownership; and substantial mandatory technical/domain mismatch.

Goal: maximize realistic interviews and offers without turning the search itself into another software project.

`discover broadly → cheap hard screen → read actual JD → dedupe → verify serious survivors → user go → apply → follow up`

## Use these views

Do **not** work from the unfiltered Issues list.

- [NOW — ACTION + APPLY + CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20-label%3A%22status%3Await%22) — everything that may need attention.
- [SG NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Asg%22%20-label%3A%22status%3Await%22) — Singapore.
- [CN NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Acn%22%20-label%3A%22status%3Await%22) — Mainland China.
- [MY NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Amy%22%20-label%3A%22status%3Await%22) — Malaysia.
- [HK WAIT / history](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Ahk%22) — historical submitted HK applications only; HK discovery is paused.
- [ACTION](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aaction%22) — OA, interview, recruiter reply, useful deadline/action.
- [APPLY](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aapply%22) — verified roles ready for review.
- [CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Acheck%22) — exactly one material blocker or user decision remains.
- [WAIT / history](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Await%22) — already applied/contacted; normally ignore until new evidence arrives.

`[TG]` only marks a Telegram / DeJob discovery source. It never means the role is verified.

## Four open states

- `[ACTION]` — something useful needs attention now or soon.
- `[APPLY]` — verified and realistically applicable; still needs my exact `go`.
- `[CHECK]` — liveness is proven and exactly one blocker/decision remains.
- `[WAIT]` — already submitted/contacted and waiting.

Rejected, expired, duplicate, blocked, withdrawn or intentionally skipped roles are closed.

## Simple commands

On an exact role:

- `go` — authorize that exact application/action.
- `applied` — I manually submitted it.
- `skip` — close it as intentionally skipped.

`go all ACTION applications` authorizes all current application-type ACTION items, but not interview/OA ACTION items.

`[APPLY]` by itself is never submission permission.

## Source of truth

- GitHub Issues = live operational opportunity state.
- Gmail = receipts, recruiter/OA/interview/rejection evidence and targeted dedupe.
- [`PROFILE.md`](PROFILE.md) = stable candidate facts and current market/role scope.
- [`RULES.md`](RULES.md) = the only detailed execution policy.
- [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md) = latest discovery receipt/cursor + next rotation only; never a second tracker.
- Old spreadsheet = legacy/read-only.

## Search model

Maintenance comes before discovery. Search broadly and cheaply, then spend verification effort only on plausible survivors. Raw discovery candidates never become Issues automatically.

- **SG:** FreeHire broad radar + direct employer/ATS + LinkedIn/JobStreet/Indeed gaps. Search Applied AI plus general SWE/backend/full-stack/test automation and adjacent early-career engineering.
- **CN:** native-source-first — BOSS, official/campus, 牛客, 51job, 智联, 猎聘 — plus FreeHire/other feeds as supplementary radar. Search 2026-compatible AI and general software/backend/test-development roles.
- **MY:** broad early-career engineering lane with no sponsorship friction. Prefer TOP companies/teams and Applied AI, but ordinary credible SWE/backend/full-stack/test/AI roles may enter the queue when realistically applicable.
- **HK:** paused. Do not discover new HK roles. Existing WAIT items remain only so employer replies are not lost.

All active markets use the same hard gates: current liveness, permanent full-time employment, realistic early-career/cohort fit, truthful hard-requirement fit, dedupe, work-authorization classification where relevant, and a usable exact application route.

Unknown SG/CN sponsorship willingness is allowed at APPLY. Explicit no-sponsorship/right-to-work/citizenship blockers are not. Singapore MCF-only routes are blocked.

## What I should do

1. Handle `ACTION` first.
2. Review `APPLY` and give `go` only for exact roles I want.
3. Resolve useful `CHECK` blockers.
4. Leave `WAIT` alone unless new evidence arrives.

## Automation

Scheduled maintenance keeps Issues synchronized with recruiting evidence. Discovery rotates SG/CN/MY source families and broad role lanes. HK stays paused until explicitly reactivated.

The latest scheduled run leaves one compact receipt in [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md). If strategy changes, update `PROFILE.md` / `RULES.md` once rather than copying policy into prompts or another tracker.

See [`PROFILE.md`](PROFILE.md), [`RULES.md`](RULES.md), and [dated market evidence](docs/market-facts-2026-10-01.md). Older `docs/superpowers/` material is historical context.
