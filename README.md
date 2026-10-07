# Job Search Inbox

Private operating inbox for my job search: **Singapore + Mainland China first**, Malaysia as backup.

Goal: get interviews and offers for a suitable full-time engineering role without turning the search into another project.

`discover → cheap screen → verify serious survivors → user go → apply → follow up`

## Use these views

Do **not** work from the unfiltered Issues list.

- [NOW — ACTION + APPLY + CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20-label%3A%22status%3Await%22) — everything that may need attention.
- [CN NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Acn%22%20-label%3A%22status%3Await%22) — Mainland China only.
- [SG NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22market%3Asg%22%20-label%3A%22status%3Await%22) — Singapore only.
- [TG NOW](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20TG%20-label%3A%22status%3Await%22) — leads first found through Telegram / DeJob.
- [ACTION](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aaction%22) — OA, interview, recruiter reply, deadline.
- [APPLY](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aapply%22) — verified roles ready for review.
- [CHECK](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Acheck%22) — exactly one blocker remains.
- [WAIT / history](https://github.com/kolihhan/job-resources/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Await%22) — already applied/contacted; normally ignore.

`[TG]` only marks the discovery source, for example `[CHECK][CN][TG] Company — Role`. It does not mean the role is verified or safe.

## Four open states

- `[ACTION]` — I need to do something now or soon.
- `[APPLY]` — verified and worth applying; still needs my `go`.
- `[CHECK]` — one material blocker or decision remains.
- `[WAIT]` — already submitted/contacted and waiting.

Rejected, expired, duplicate, blocked, withdrawn or intentionally skipped roles are closed.

## Simple commands

On an exact role:

- `go` — authorize that exact application/action.
- `applied` — I manually submitted it.
- `skip` — close it as intentionally skipped.

`[APPLY]` by itself is never submission permission.

## How the system runs

**Source of truth**

- GitHub Issues = live operational state.
- Gmail = recruiting evidence and targeted dedupe.
- [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md) = latest scheduled-discovery receipt + next rotation only; not a job tracker.
- Old spreadsheet = legacy/read-only.

**Discovery**

Search SG + CN broadly and cheaply first. Verify only serious survivors. Raw search results do not become Issues.

- SG: official careers/ATS, LinkedIn, JobStreet, Indeed; selective secondary sources such as DeJob/TG.
- CN: BOSS, official/campus portals, 牛客, 51job, 智联; secondary LinkedIn, 猎聘, DeJob/TG.
- MY: backup; lean toward Applied AI / AI Engineer / LLM / RAG / Agent / AI backend roles.

All sources use the same survivor checks: live exact JD, cohort/seniority fit, dedupe, work-authorization blockers when material, and a usable exact application route. Telegram/DeJob does **not** bypass verification.

Detailed execution rules live only in [`RULES.md`](RULES.md). Do not duplicate them into scheduler prompts, another tracker, or another framework.

## What I should do

1. Handle `ACTION` first.
2. Review `APPLY` and give `go` only for roles I want.
3. Resolve useful `CHECK` blockers.
4. Leave `WAIT` alone unless new evidence arrives.

## Automation

Maintenance checks recent recruiting evidence and keeps existing Issues synchronized. Incremental discovery rotates SG/CN sources; Malaysia remains backup.

The latest scheduled discovery should leave one small receipt in [`DISCOVERY_STATE.md`](DISCOVERY_STATE.md), including the SG/CN source mix tried, serious survivors (if any), concrete blockers, and the next rotation.

The automation reads the current repo rules. If strategy changes, update `RULES.md` once rather than maintaining multiple copies.

See `PROFILE.md`, [`RULES.md`](RULES.md), and [dated market evidence](docs/market-facts-2026-10-01.md). Older `docs/superpowers/` material is historical context.
