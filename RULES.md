# Operating Rules

## Every hourly run

1. Read `PROFILE.md`, this file, and current open Issues.
2. Check both Gmail accounts for new job-search evidence.
3. Update existing Issues before creating anything new.
4. Official application receipt → `WAIT`.
5. OA / interview / recruiter reply / time-sensitive deadline → `ACTION`.
6. Confirmed rejection / expired / duplicate / user `skip` → close the Issue.
7. Avoid duplicate Issues.
8. Outside MYT `00/04/08/12/16/20`, stop after maintenance unless a time-sensitive action must be surfaced.

## Chat decision sync

GitHub Issues are the live operational state. Do not leave a clear user decision only in chat.

When the user explicitly says to skip, drop, ignore, withdraw, or otherwise stop pursuing an exact tracked role in an interactive session with GitHub write access, mirror that decision to the matching Issue immediately. Close intentionally skipped roles instead of leaving stale `ACTION`/`APPLY` state behind.

A user skip/drop decision is authoritative until the user explicitly reverses it. Older Gmail invitations, reminders, deadlines, or application evidence must **not** reopen or recreate an intentionally skipped role. A later employer message may be noted only if it materially changes the opportunity; do not restore it to the active queue without a new user decision.

Scheduled runs cannot infer private chat-only decisions unless those decisions have been reflected in GitHub or Gmail evidence.

## Discovery hours

On MYT `00/04/08/12/16/20`, run incremental Singapore + Mainland China discovery after maintenance.

Do not restart the market from scratch each time. Prefer established engineering/product employers and search across:

- Software Engineer / SDE
- Backend
- Platform / Infrastructure / Systems
- ML Systems / AI Platform
- Applied AI / LLM / RAG / Agent engineering

Do not let `AI Engineer` become the dominant search axis.

## When to create an Issue

Create one only when a role is serious enough to deserve attention:

- appears live;
- 2026 graduate timing is not obviously disqualifying;
- seniority is plausible for early career;
- no obvious hard stack mismatch;
- company/role quality is credible;
- an exact role-level application route is verified, or exactly one important route/eligibility/fit blocker remains;
- no exact application is already established.

Bad/stale/obvious-mismatch search results create nothing.

## Application-route hard gate

A listing being live is not enough. `APPLY` requires a usable **exact-role** route.

- Open or resolve the actual Apply action far enough to identify the final application destination.
- A generic company careers page, city/location page, search-results page, or aggregator listing is not an exact application route.
- If only a generic page is available and the exact requisition cannot be recovered, use `CHECK` at most, with the blocker `exact application route not verified`.
- For Singapore, MyCareersFuture is not a usable application channel for this candidate. If the final route is MCF-only, do not create/keep an `APPLY` Issue; close/block it unless a separate verified non-MCF exact route exists.
- Indeed, JobStreet, LinkedIn, Glints, or another platform can be used when the exact role has a real application path there, but an unresolved `Apply on company site` redirect is not proof of a usable route.
- Prefer employer-controlled ATS/direct application pages when available.

## Dedupe

Primary key:

`market + company + requisition/job ID`

Fallback when no ID exists:

`company + role + location`

Before a new Issue, check:

1. existing GitHub Issues;
2. Gmail A: `lihhanko526@gmail.com`;
3. Gmail B: `lihhanko3@gmail.com`;
4. ATS/candidate history when materially available.

If a receipt/application already exists, do not create a new `APPLY` Issue.

## Issue states

Only four open states:

- `ACTION`
- `APPLY`
- `CHECK`
- `WAIT`

`CHECK` means one material blocker, and the Issue must name the blocker and exactly one next action.

## APPLY / CHECK research

Store enough to decide without repeating the research:

- exact official/direct apply link, or the one unresolved route blocker for `CHECK`;
- final application destination/domain when routing is indirect;
- req/job ID and checked date;
- useful company background and current material developments;
- plain-language actual work;
- hard requirements and graduate/YOE fit;
- specific candidate strengths and gaps;
- SG sponsorship or CN foreign-work-permit evidence;
- supported salary/WLB evidence when available;
- both-Gmail + GitHub dedupe result;
- exactly one next action;
- source links.

Do not add generic company-history filler or unsupported claims.

## Authorization

`APPLY` means "recommended for review", not "submit now".

Only an explicit `go` from the user on that exact role authorizes an application action. Never mass apply.

## Privacy

The repository is private, but still store only operational facts.

Never copy full email bodies, auth/activation links, tokens, passwords, secrets, or unnecessary personal identifiers into Issues.

## Source of truth

GitHub Issues are the only live operational tracker. Gmail is evidence. `/Job Applications/JOB_TRACKER.xlsx` is legacy/read-only reference and must not be kept in sync as a second live tracker.

## Keep it small

Do not add GitHub Projects, a database, dashboard, web frontend, spreadsheet mirror, agent framework, or application code unless a real repeated failure proves GitHub Issues are insufficient.

Scheduled-task model routing may not guarantee GPT-5.6 Sol High. Do not claim otherwise; optimize the workflow for reliable evidence-first execution instead.