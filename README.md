# Job Search Inbox

Private operating inbox for my Singapore + Mainland China job search.

## Open Issues are the UI

Only four open states are used:

- `[ACTION]` — I need to do something now or soon: OA, interview, recruiter reply, deadline.
- `[APPLY]` — research is complete and the exact role is worth applying to.
- `[CHECK]` — one material blocker remains unresolved.
- `[WAIT]` — already applied; waiting for employer activity.

Rejected, expired, duplicate, withdrawn, or intentionally skipped roles are closed.

## Issue title

`[STATUS][MARKET] Company — Role — Req ID`

Examples:

- `[ACTION][CN] Company — Assessment — due 2026-10-01`
- `[APPLY][SG] Company — Software Engineer — 12345`
- `[WAIT][CN] Company — Backend Engineer — 67890`

## Simple commands

Comments on an exact role:

- `go` — authorize proceeding with that exact application/action.
- `applied` — I manually submitted it and no official receipt has arrived yet.
- `skip` — close it as intentionally skipped.

`[APPLY]` by itself is never permission to submit.

A clear skip/drop decision made in ChatGPT should be mirrored to the matching GitHub Issue immediately so the inbox does not drift from the real decision.

## Application-link rule

`[APPLY]` means the exact role-level application route has been verified, not merely that a listing exists.

- Generic careers/location/search pages are not enough.
- For Singapore, the final Apply destination must be checked.
- MyCareersFuture-only roles are blocked for this candidate unless a separate verified non-MCF route exists.
- If one route blocker remains, use `[CHECK]` instead of `[APPLY]`.

## What I should do each morning

1. Handle `[ACTION]` first.
2. Review `[APPLY]` roles and comment `go` on the ones I want to pursue.
3. Resolve `[CHECK]` only when the blocker matters.
4. Leave `[WAIT]` alone unless new evidence arrives.

## Source of truth

- GitHub Issues = current operational state.
- Gmail = evidence for receipts, OA/interviews, recruiter messages, deadlines, rejections, and status changes.
- The old Library spreadsheet is legacy/read-only reference only.

Do not create a second live tracker, dashboard, database, or spreadsheet mirror.

## Automation behavior

Maintenance runs hourly. It checks both Gmail accounts and updates existing Issues before doing anything else.

Full SG + CN discovery happens only around MYT `00/04/08/12/16/20`. Other hourly runs are maintenance-only.

Normal new `[APPLY]` roles can wait here quietly. Notify me only for genuinely time-sensitive actions such as OA/interview deadlines or recruiter messages requiring a reply.

See `PROFILE.md` for stable candidate facts and `RULES.md` for the operating contract.