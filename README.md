# Job Search Inbox

Private operating inbox for the current search.

Current contract:

- **Singapore + Mainland China** = active primary markets;
- **Malaysia** = active **TOP-only** parallel lane;
- **Hong Kong = paused** as of 2026-10-23: do not discover or promote new HK roles until the user explicitly reactivates HK;
- main search = **permanent full-time only**.

Primary role lane:

- Applied AI / AI Application / LLM / RAG / Agent;
- AI backend / AI-native product engineering;
- retrieval / search / evaluation when the work is closely connected to LLM or Agent systems;
- strong software/backend roles only when they clearly compound the same career direction.

Default deprioritize/skip: pure CV, traditional ML without LLM/application overlap, generic MLOps, model-serving/platform/infra, deep distributed systems, mature FDE/solution-architecture ownership, and generic SWE that would require a separate interview-prep track.

Goal: get interviews and offers for a strong engineering role without turning the search itself into another software project.

`discover → cheap screen → verify serious survivors → user go → apply → follow up`

## Use these views

Do **not** work from the unfiltered Issues list.

- [NOW — ACTION + APPLY + CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20-label%3A%22status%3Await%22) — everything that may need attention.
- [SG NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Asg%22%20-label%3A%22status%3Await%22) — Singapore.
- [CN NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Acn%22%20-label%3A%22status%3Await%22) — Mainland China.
- [MY NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Amy%22%20-label%3A%22status%3Await%22) — Malaysia TOP-only lane.
- [HK WAIT / history](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Ahk%22) — historical submitted HK applications only; HK discovery is paused.
- [ACTION](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aaction%22) — OA, interview, recruiter reply, useful deadline/action.
- [APPLY](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aapply%22) — verified roles ready for review.
- [CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Acheck%22) — exactly one material blocker or user decision remains.
- [WAIT / history](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Await%22) — already applied/contacted; normally ignore until new evidence arrives.

`[TG]` only marks a Telegram / DeJob discovery source. It never means the role is verified.

## Four open states

- `[ACTION]` — something useful needs attention now or soon.
- `[APPLY]` — verified and worth applying; still needs my exact `go`.
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

Maintenance comes before discovery. Search broadly enough to find good roles, but only serious survivors become Issues.

- **SG:** direct employer/ATS + targeted FreeHire/LinkedIn/JobStreet/Indeed gaps. Focus Agent/RAG/evaluation/AI backend and early-career AI-native product roles.
- **CN:** native-source-first — BOSS, official/campus, 牛客, 51job, 智联, 猎聘. Focus 2026-compatible Agent/RAG/evaluation/AI backend/search-retrieval roles.
- **MY:** TOP-only and AI-first. Strong Applied AI / Agent / RAG / AI software/backend roles at high-quality employers/teams; ordinary fallback jobs do not enter the queue.
- **HK:** paused. Do not discover new HK roles. Existing WAIT items remain only so employer replies are not lost.

All active markets use the same survivor gates: exact current liveness, permanent full-time employment, early-career/cohort fit, truthful YOE fit, dedupe, work-authorization classification, technical-direction fit and a usable exact application route.

Unknown SG/CN sponsorship willingness is allowed at APPLY. Explicit no-sponsorship/right-to-work/citizenship blockers are not. Singapore MCF-only routes are blocked.

## What I should do

1. Handle `ACTION` first.
2. Review `APPLY` and give `go` only for exact roles I want.
3. Resolve useful `CHECK` blockers.
4. Leave `WAIT` alone unless new evidence arrives.

## Automation

Scheduled maintenance keeps Issues synchronized with recruiting evidence. Discovery rotates SG/CN source families and role lanes; MY TOP is a smaller parallel rotation. HK stays paused until explicitly reactivated.

The latest scheduled run leaves one compact receipt in [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md). If strategy changes, update `PROFILE.md` / `RULES.md` once rather than copying policy into prompts or another tracker.

See [`PROFILE.md`](PROFILE.md), [`RULES.md`](RULES.md), and [dated market evidence](docs/market-facts-2026-10-01.md). Older `docs/superpowers/` material is historical context.
