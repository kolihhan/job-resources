# Job Search Inbox

Private operating inbox for my job search: **Singapore + Mainland China first**, Malaysia as a practical backup.

The goal is interviews and offers for a suitable full-time, on-site or hybrid engineering job. Prioritize active employer responses, then create more strong SG/CN opportunities. Use the current resume and project evidence; change them only for a concrete application need or repeated relevant employer feedback.

Keep the workflow small:

`discover broadly → cheap screen → verify serious survivors → user go → apply → follow up`

Do not create an application quota, experiment framework, or another tracker.

## Open Issues are the UI

Only four open states are used:

- `[ACTION]` — I need to do something now or soon: OA, interview, recruiter reply, deadline.
- `[APPLY]` — verification is complete and the exact role is worth applying to.
- `[CHECK]` — one material blocker remains unresolved.
- `[WAIT]` — already applied; waiting for employer activity.

Rejected, expired, duplicate, withdrawn, or intentionally skipped roles are closed.

## Labels / quick filters

Every tracked Issue carries one market label and one status label.

Market:

- `market:sg`
- `market:cn`
- `market:my` — Malaysia backup

Open status:

- `status:action`
- `status:apply`
- `status:check`
- `status:wait`

Useful filters:

- Ready to review/apply: `is:issue is:open label:"status:apply"`
- Waiting applications: `is:issue is:open label:"status:wait"`
- Needs one blocker resolved: `is:issue is:open label:"status:check"`
- Singapore: `is:issue is:open label:"market:sg"`
- China: `is:issue is:open label:"market:cn"`

Closed intentional outcomes may use `status:skipped` or `status:blocked`; MCF-only Singapore roles also use `blocked:mcf`.

## Issue title

`[STATUS][MARKET] Company — Role — Req ID`

## Simple commands

Comments on an exact role:

- `go` — authorize proceeding with that exact application/action.
- `applied` — I manually submitted it and no official receipt has arrived yet.
- `skip` — close it as intentionally skipped.

`[APPLY]` by itself is never permission to submit.

A clear skip/drop decision made in ChatGPT should be mirrored to the matching GitHub Issue immediately.

## Discovery vs verification

Discovery and verification are deliberately separate.

### Stage 1 — broad discovery

Search **SG + CN first** across many employers and relevant role families. Discovery should be cheap and wide.

At this stage check only enough to reject obvious bad candidates:

- wrong country / not full-time;
- clearly senior or hard 5+ YOE;
- clearly incompatible graduation window;
- substantial hard stack/domain mismatch;
- clearly stale listing.

Do **not** stop discovery to deeply research salary, WLB, unknown sponsorship, exact final ATS routing, or both Gmail accounts for every raw candidate. Do not create Issues for raw candidates.

### Stage 2 — survivor verification

For serious survivors, verify:

- full/exact JD and current live status;
- cohort / seniority / hard requirements;
- GitHub + targeted Gmail dedupe;
- exact usable application route;
- any material work-authorization or fit blocker that affects whether to apply.

Only then create or update an Issue.

`[APPLY]` still requires a verified exact role-level application route. Generic careers/search pages are not enough. On intermediary sites such as JobStreet/LinkedIn/Indeed/Glints, an Apply button or role-specific `/apply` URL is not final proof: the real application form or employer ATS must be reached. For Singapore, any flow that ultimately resolves to MCF is blocked unless a separate verified non-MCF route exists.

## Market focus

### Singapore — primary

Primary discovery: official company careers/ATS, LinkedIn, JobStreet, Indeed.

Support: MCF for evidence only, employee-review sources when decision-relevant, Wellfound selectively.

Unknown sponsorship is not a discovery-stage rejection. Explicit no-sponsorship is.

### Mainland China — primary

Primary discovery: BOSS直聘, official company careers/campus portals, 牛客, 51job/前程无忧, 智联/智联校园.

Secondary: LinkedIn and 猎聘.

Prioritize 2026-compatible wording such as `2026届`, `往届可投`, `毕业两年内`, `0–3年`, `海外留学生`, recent graduate. Clearly 2027-only roles are normally filtered unless the official window includes a 2026 graduate.

Search normal SWE/backend/full-stack/platform roles and Applied-AI roles in parallel. `AI Engineer` is not the only useful title.

### Malaysia — backup, not an equal lane

Do not let Malaysia consume the main SG/CN search budget.

Search Malaysia when:

- SG/CN discovery in the current run is genuinely sparse after changing employers/keywords/sources; or
- an unusually strong Malaysian opportunity surfaces naturally.

For Malaysia, lean more toward **AI Engineer / Applied AI / AI Software Engineer / LLM / RAG / Agent / AI backend/platform** because local work authorization is not a blocker. Strong normal SWE/backend roles are still valid when they offer better engineering career capital.

Regional or China/SG-connected employers are interesting, but do not assume a future internal transfer without evidence.

## Human route

For an unusually strong verified role, optionally look for one relevant recruiter, alumnus, former colleague, or team contact when it could materially improve the application. Do not turn networking into a requirement for every role. Contacting anyone still requires explicit user authorization.

## What I should do each morning

1. Handle `[ACTION]` first.
2. Review `[APPLY]` and give `go` on roles I want to pursue.
3. Resolve `[CHECK]` only when the blocker matters.
4. Leave `[WAIT]` alone unless new evidence arrives.

## Source of truth

- GitHub Issues = current operational state.
- Gmail = targeted evidence for receipts, OA/interviews, recruiter messages, deadlines, rejections, and dedupe.
- The old Library spreadsheet = legacy/read-only reference.

Do not create a second live tracker, dashboard, database, or spreadsheet mirror.

## Automation behavior

Maintenance runs hourly and updates existing Issues first.

Incremental discovery runs during MYT hours `00/04/08/12/16/20`. **SG + CN are always the primary discovery markets.** Malaysia is backup as defined above, not a mandatory third-market sweep.

Gmail maintenance should use bounded recent recruiting evidence and exact-role/company lookups when needed; do not broad-audit the entire mailbox every run.

The weekly review focuses on real employer signals and the single most useful next action. Scheduled prompts read current GitHub rules rather than carrying a second copy of the strategy.

Normal `[APPLY]` roles can wait quietly. Notify me for time-sensitive actions or access/write failures that need intervention.

See [dated market evidence](docs/market-facts-2026-10-01.md), [the next-chat prompt](NEXT_CHAT_PROMPT.md), `PROFILE.md`, and `RULES.md`. Older documents under `docs/superpowers/` are historical context.
