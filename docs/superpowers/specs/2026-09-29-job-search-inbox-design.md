# Job Search Inbox — Design

Date: 2026-09-29
Status: proposed for implementation after user review
Repository: `kolihhan/job-resources` (private)

## Goal

Create a low-maintenance job-search operating system that lets the user open GitHub Issues and immediately see what needs attention.

The system must do three things well:

1. keep application state current from two Gmail accounts and GitHub Issues;
2. find and research high-quality Singapore + Mainland China roles without repeating old work;
3. surface only actionable items: `ACTION`, `APPLY`, `CHECK`, or `WAIT`.

The design intentionally avoids a custom dashboard, database, duplicate spreadsheet state, and large agent framework.

## Source of truth

- **GitHub Issues**: operational source of truth for active roles and actions.
- **Gmail A** `lihhanko526@gmail.com`: evidence for China/direct-email applications and any other messages received there.
- **Gmail B** `lihhanko3@gmail.com`: evidence for Singapore/international/ATS applications and any other messages received there.
- Existing `/Job Applications/JOB_TRACKER.xlsx`: legacy/read-only reference after migration; it is not maintained as a second operational state store.

Original email bodies are not copied into GitHub. Issues retain only the minimum evidence needed to act, such as message type, date, employer, requisition, and deadline.

## GitHub UI model

One serious role = one GitHub Issue.

Issue title format:

`[STATUS][MARKET] Company — Role — Req ID`

Examples:

- `[ACTION][CN] 中景芯创 — Online Assessment — due 2026-10-01`
- `[APPLY][CN] Tencent Music — AI全栈工程师 — 15037`
- `[WAIT][SG] Agilent — AI & Data Scientist — 4039990`

Only four open states exist:

- `ACTION`: user must do something now or soon, such as OA, interview, recruiter reply, or deadline.
- `APPLY`: research is complete and the role is worth applying to.
- `CHECK`: exactly one material blocker remains unresolved.
- `WAIT`: already applied; wait for employer activity.

Rejected, expired, duplicate, withdrawn, or intentionally skipped roles are closed rather than given more live-state categories.

## What qualifies for an Issue

Do not create an Issue for every search result.

A role becomes an Issue only after a cheap screen shows that it is plausibly useful:

- role appears live;
- 2026 graduation timing is not obviously disqualifying;
- seniority is compatible with new-grad / early-career target, with selective stretch only;
- no obvious hard technical mismatch;
- company/role quality is credible enough to justify attention;
- a usable application route exists or one clearly defined route blocker remains;
- exact application history is not already established.

Obvious mismatches, stale results, generic alerts, weak staffing/bodyshop roles, senior/lead/staff/manager roles, hard 5+ YOE roles, and duplicate applications create no new Issue.

## Role research stored in an APPLY/CHECK Issue

A serious role should contain enough information to make an application decision without reopening the whole research process:

### Apply
- official/direct application link;
- requisition/job ID when available;
- checked date.

### Company
- what the company actually does;
- relevant size/stability/engineering context;
- recent material background only when it affects the role: major funding, layoffs, acquisition/restructuring, hiring trend, AI investment, or business risk;
- avoid generic company-history filler.

### Role
- plain-language description of the actual engineering work;
- important hard requirements;
- experience/graduate eligibility;
- relevant stack and production ownership.

### Fit
- specific strengths from the candidate profile;
- concrete gaps;
- never convert master's study, projects, internships, or part-time work into fictitious full-time professional YOE.

### Work authorization
- Singapore: employer-supported EP/S Pass required; distinguish explicit no-sponsor evidence from unknown sponsorship.
- Mainland China: employer-supported foreign work permit required; distinguish legal plausibility from employer willingness.

### Compensation / WLB
- include only supported evidence;
- do not invent salary, benefits, or WLB.

### Dedupe
- Gmail A exact/near-exact evidence;
- Gmail B exact/near-exact evidence;
- existing GitHub Issue check;
- ATS/candidate-portal history when materially available.

### Next action
Exactly one next action.

## Dedupe key

Primary fingerprint:

`market + company + requisition/job ID`

Fallback only when no requisition/job ID exists:

`company + role + location`

Do not create a more complex fingerprint system unless repeated real collisions prove this insufficient.

## Hourly maintenance behavior

The scheduled task runs at most once per hour.

Every run prioritizes maintenance over discovery:

1. read current open GitHub Issues;
2. check both Gmail accounts for new job-search evidence;
3. update existing Issues before creating anything new;
4. convert application receipts to `WAIT`;
5. convert OA/interview/recruiter/deadline items to `ACTION`;
6. close confirmed rejections/expired/duplicate items;
7. avoid creating duplicate Issues;
8. perform market discovery only when the discovery cooldown has elapsed.

### Discovery cooldown

Full market discovery should run approximately every four hours, not every hourly maintenance cycle.

The same hourly task may decide whether discovery is due. No second scheduler is necessary.

Discovery is incremental rather than a full restart.

## Discovery priorities

Markets: Singapore + Mainland China.

Primary role families:

- Software Engineer / SDE
- Backend Engineer
- Platform / Infrastructure / Systems
- ML Systems / AI Platform
- Applied AI / LLM / RAG / Agent engineering

The search should not use `AI Engineer` as the dominant discovery axis.

Prefer recognizable, established engineering/product employers first, then credible smaller companies with clear engineering quality and ownership.

The first-job objective is durable CS career capital: production code, code review, backend/API/data/cloud/distributed systems, deployment/reliability, strong peers/mentorship, and portable engineering reputation. Applied AI is a differentiator, not the only acceptable title family.

## Notifications

GitHub is the primary UI. The scheduled task should stay quiet when there is no meaningful change.

Notify the user only for items such as:

- OA / assessment deadline;
- interview invitation or schedule change;
- recruiter/HR message requiring a response;
- application deadline within roughly 24 hours;
- other genuinely time-sensitive user action.

Normal new `APPLY` Issues do not require an interruption; they can wait in GitHub for the user to review after waking.

## User interaction

The user should be able to work primarily from GitHub Issues.

Desired simple commands/comments:

- `go` — user wants to proceed with this exact role/application action;
- `applied` — user confirms manual submission when no receipt has arrived yet;
- `skip` — close as intentionally skipped.

Email evidence can supersede manual comments when an official receipt/outcome is available.

## Privacy

The repository is private.

Do not store:

- full email bodies;
- authentication links/tokens;
- passwords or secrets;
- unnecessary personal identifiers;
- private recruiter phone numbers unless the user explicitly needs them in the Issue.

Store only operational facts required to make or track the job-search decision.

## Repository contents

Keep the repository intentionally small:

- `README.md` — how to use the GitHub Issues inbox;
- `PROFILE.md` — stable candidate facts and role preferences;
- `RULES.md` — concise maintenance/discovery rules;
- `docs/superpowers/specs/` — this approved design history.

Do not add a database, custom dashboard, web frontend, spreadsheet mirror, framework, or application code unless a real limitation later proves GitHub Issues inadequate.

## Migration

Initial migration should include only current useful state, not every historical application.

Create Issues for:

- active `ACTION` items;
- credible active `WAIT` applications still worth tracking;
- current researched `APPLY` / `CHECK` candidates.

Do not import old rejected, expired, duplicate, stale, or low-quality roles merely for completeness. Historical evidence remains in Gmail and the legacy tracker.

## Success criteria

The design succeeds if:

1. the user can open GitHub Issues in the morning and know what to do without consulting another tracker;
2. new Gmail evidence updates existing role state instead of creating duplicate records;
3. serious new roles contain company background, JD interpretation, fit/gaps, work-authorization context, supported compensation/WLB evidence, direct apply route, and dedupe result;
4. routine hourly runs are quiet unless there is a meaningful change;
5. repeated searches do not create duplicate Issues;
6. the repo remains small enough that maintenance is simpler than the prior job-agent system.

## Explicit non-goals

- custom job-search dashboard;
- database-backed application tracker;
- automatic mass application;
- invented callback scores or rankings;
- mirroring every job alert;
- synchronizing GitHub and Excel as equal sources of truth;
- recreating the previous `job-agent` architecture.
