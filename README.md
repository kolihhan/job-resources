# Job Search Inbox

Private operating inbox for the current search:

- **Singapore + Mainland China + Hong Kong** = active target markets;
- **Malaysia** = parallel **TOP-only** lane;
- Web3 / crypto = opportunistic secondary lane.

Goal: get interviews and offers for a strong engineering role without turning the search itself into another software project.

`discover → cheap screen → verify serious survivors → user go → apply → follow up`

## Use these views

Do **not** work from the unfiltered Issues list.

- [NOW — ACTION + APPLY + CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20-label%3A%22status%3Await%22) — everything that may need attention.
- [SG NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Asg%22%20-label%3A%22status%3Await%22) — Singapore.
- [CN NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Acn%22%20-label%3A%22status%3Await%22) — Mainland China.
- [HK NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Ahk%22%20-label%3A%22status%3Await%22) — Hong Kong.
- [MY NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Amy%22%20-label%3A%22status%3Await%22) — Malaysia TOP-only lane.
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

`[APPLY]` by itself is never submission permission.

## Source of truth

- GitHub Issues = live operational opportunity state.
- Gmail = receipts, recruiter/OA/interview/rejection evidence and targeted dedupe.
- [`PROFILE.md`](PROFILE.md) = stable candidate facts and current market scope.
- [`RULES.md`](RULES.md) = the only detailed execution policy.
- [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md) = latest discovery receipt/cursor + next rotation only; never a second tracker.
- Old spreadsheet = legacy/read-only.

## Search model

Maintenance comes before discovery. Search broadly and cheaply, but only serious survivors become Issues.

- **SG:** FreeHire broad radar; normal runs focus on direct-employer/ATS and other coverage gaps.
- **CN:** native-source-first — BOSS, official/campus, 牛客, 51job, 智联, 猎聘.
- **HK:** official/ATS, LinkedIn/JobsDB and strong fintech/product/AI/research employers; GEP sponsorship willingness may remain unknown until engagement.
- **MY:** only strong role-level opportunities. A famous logo alone is not enough; optimize for engineering quality, compensation/WLB/growth, fit and career portability.

All markets use the same survivor gates: exact current liveness, early-career/cohort fit, dedupe, acceptable employment type, work-authorization classification, and a usable exact application route.

Unknown SG/CN/HK sponsorship willingness is allowed at APPLY. Explicit no-sponsorship/right-to-work/citizenship blockers are not. Singapore MCF-only routes are blocked.

## What I should do

1. Handle `ACTION` first.
2. Review `APPLY` and give `go` only for exact roles I want.
3. Resolve useful `CHECK` blockers.
4. Leave `WAIT` alone unless new evidence arrives.

## Automation

Scheduled maintenance keeps Issues synchronized with recruiting evidence. Discovery rotates markets, source families and role lanes rather than restarting the whole market every run. SG/CN remain high-frequency lanes; HK and MY TOP are active rotating lanes and must not be treated as out-of-scope.

The latest scheduled run leaves one compact receipt in [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md). If strategy changes, update `PROFILE.md` / `RULES.md` once rather than copying policy into prompts or another tracker.

See [`PROFILE.md`](PROFILE.md), [`RULES.md`](RULES.md), and [dated market evidence](docs/market-facts-2026-10-01.md). Older `docs/superpowers/` material is historical context.
