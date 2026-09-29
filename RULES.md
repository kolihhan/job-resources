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
- a usable application route exists, or exactly one important route/eligibility/fit blocker remains;
- no exact application is already established.

Bad/stale/obvious-mismatch search results create nothing.

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

- official/direct apply link;
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