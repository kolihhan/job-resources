# Operating Rules

## Goal

Get interviews and offers for a suitable full-time, on-site or hybrid engineering job.

Priority order:

1. advance active employer responses, OA, interviews and recruiter conversations;
2. create more strong **Singapore + Mainland China** opportunities;
3. use Malaysia as a practical backup without displacing SG/CN search.

Use the current resume and project evidence. Change them only for a concrete application need or repeated relevant employer feedback. Do not restart portfolio work, strategy research, application-count experiments, or another tracking system.

For unusually strong verified roles, selective recruiter/alumni/team contact research is allowed when it could help. Do not require networking for every role. Any external contact or application still requires explicit user authorization.

## Source of truth

- GitHub Issues = current operational state.
- Gmail = evidence for receipts, recruiter messages, OA/interviews, deadlines, rejections, and targeted dedupe.
- The old Library spreadsheet = legacy/read-only reference.

Do not create a second live tracker, dashboard, database, spreadsheet mirror, or agent framework.

## Every maintenance run

1. Read `PROFILE.md`, this file, and current open Issues.
2. Check both Gmail accounts for **recent recruiting evidence** since the last successful check, with a small overlap.
3. Update existing Issues before creating new ones.
4. Official application receipt → `WAIT`.
5. OA / interview / recruiter reply / time-sensitive deadline → `ACTION`.
6. Confirmed rejection / expired / duplicate / user `skip` → close the Issue.
7. Keep title, status label, body and next action synchronized.
8. Respect newer evidence over older evidence. An old receipt must not downgrade a newer interview/OA/action to `WAIT`.
9. Silence is not a rejection.
10. A user `applied` comment is sufficient to mark `WAIT`, noting that it is user-confirmed if no employer receipt exists.

Gmail should be searched narrowly. Use bounded recent windows for maintenance and exact company/role/req lookups for dedupe or unresolved evidence. Do not broad-audit the entire mailbox every run.

Verify material GitHub writes by reading them back. If Gmail/GitHub access or a required write fails, report the concrete incomplete step rather than claiming successful maintenance.

## Chat decision sync

A clear user decision to skip, drop, ignore or withdraw an exact tracked role must be mirrored to GitHub when write access exists.

A skip/drop decision is authoritative until the user explicitly reverses it. Older Gmail invitations, reminders or application receipts must not reopen a skipped role.

## Discovery schedule

During MYT hours `00/04/08/12/16/20`, run incremental discovery after maintenance. Explicit interactive searches can run at any time.

**SG + CN are the main discovery markets.** Malaysia is backup, not a mandatory equal third-market sweep.

Do not restart the whole market every run. Rotate high-value sources, employers and keywords, and avoid rechecking stale results repeatedly.

## Two-stage discovery

### Stage 1 — broad, cheap discovery

The purpose is to create a wide candidate pool before spending expensive verification effort.

Search SG and CN first across many employers and role families:

- Software Engineer / SDE
- Backend / Full-stack
- Platform / Infrastructure / Systems
- ML Systems / AI Platform / Inference / Evaluation
- Search / Retrieval
- Applied AI / AI Software Engineer / LLM / RAG / Agent engineering

Cheap-screen only obvious hard mismatches:

- wrong country or not full-time;
- Senior / Staff / Lead / Manager or hard 5+ YOE without a graduate exception;
- explicit incompatible graduation/cohort window;
- explicit citizenship / no-sponsorship blocker where relevant;
- substantial hard stack/domain mismatch;
- clearly stale/closed listing.

At this stage **do not** stop to research:

- salary or WLB unless immediately visible and decision-critical;
- unknown SG sponsorship or CN work-permit willingness;
- exact final ATS routing;
- both Gmail accounts for every raw candidate;
- detailed company history;
- networking contacts.

Do not create GitHub Issues for raw discovery candidates.

If few candidates survive, change employers, role keywords or source mix in the same run before concluding the market is sparse.

### Stage 2 — verify serious survivors

For roles that survive the cheap screen and are genuinely worth considering, verify:

1. exact/full JD and current live status;
2. graduation/cohort, seniority and hard requirements;
3. GitHub dedupe;
4. targeted Gmail dedupe by company/role/req ID;
5. exact usable application route;
6. any material work-authorization or fit blocker that changes the decision to apply.

Only serious survivors reach GitHub Issues.

## Singapore — primary

Primary discovery:

1. official company careers / ATS;
2. LinkedIn;
3. JobStreet;
4. Indeed.

Support/research when useful:

- MyCareersFuture for evidence only;
- employee-review sources for decision-relevant company/WLB questions;
- Wellfound selectively for startups.

MCF is not a usable application channel for this candidate. If the only verified route is MCF, block/close the role unless a separate non-MCF exact route exists.

Unknown sponsorship is **not** a discovery-stage rejection. Explicit no-sponsorship is.

Preferred flow:

`broad SG discovery → cheap hard filter → serious survivor → exact JD / eligibility / targeted dedupe / final apply route → APPLY or CHECK`

## Mainland China — primary

Primary discovery:

1. BOSS直聘;
2. official company careers / campus portals / useful recruiting WeChat pages;
3. 牛客;
4. 51job / 前程无忧;
5. 智联招聘 / 智联校园.

Secondary:

- LinkedIn;
- 猎聘.

Research only when decision-relevant:

- 牛客面经/题库;
- 脉脉;
- 小红书;
- 知乎;
- employee-review sources.

The candidate graduated in **2026**. Prioritize:

- `2026届`
- `往届可投`
- `毕业两年内`
- `应届/往届`
- `0-1年` / `0-3年`
- `初级`
- `海外留学生`
- recent graduate / recently completed

Clearly 2027-only roles are normally filtered unless official wording explicitly includes a 2026 graduate.

Do not equate legal foreign-work-permit possibility with employer willingness to hire a foreign fresh graduate. Employer willingness may remain unknown until engagement.

Preferred flow:

`broad CN discovery → cheap cohort/seniority filter → serious survivor → exact JD / targeted dedupe / usable apply/contact route → APPLY or CHECK`

## Malaysia — backup

Do not let Malaysia consume the main SG/CN search budget.

Search Malaysia when:

- SG/CN discovery remains sparse after changing employers, keywords or sources; or
- an unusually strong Malaysian role surfaces naturally.

For Malaysia, lean more toward:

- AI Engineer;
- Applied AI / AI Software Engineer;
- LLM / RAG / Agent engineering;
- AI backend / AI platform / ML systems.

Strong normal SWE/backend roles remain valid when they offer better production ownership, engineering peers, deployment/reliability depth and transferable career capital than a weak AI-titled role.

Do not apply SG/CN foreign-work-authorization blockers to Malaysia. Regional/China/SG-connected employers are interesting, but do not assume future internal transfer without evidence.

## Company / role quality

Prefer established engineering/product employers and credible product startups with clear engineering work.

De-prioritize staffing/bodyshop/outsourcing unless there is unusually strong evidence that the role itself offers direct, high-quality engineering work.

Do not reject a strong role because of missing nice-to-haves. Distinguish hard requirements from preferences.

Never convert part-time work, internships, projects or master's study into fictitious full-time professional YOE.

## When to create an Issue

Create an Issue only for a serious survivor that deserves user attention.

A new Issue should have:

- plausible early-career fit;
- no obvious cohort/seniority hard block;
- credible role/company quality;
- current exact/full role evidence;
- no established duplicate application;
- either a verified exact application route or exactly one material blocker remaining.

Bad/stale/obvious-mismatch raw search results create nothing.

## Application-route hard gate

`APPLY` requires a **fresh, usable, end-to-end exact-role application route**.

- Search results, cached/indexed copies, mirrors and generic careers/search/location pages are discovery evidence only. They do **not** prove that a role is currently actionable.
- The exact role page must currently match the intended employer/title/requisition and expose a real application/contact action.
- For any intermediary platform or button that redirects (including LinkedIn, JobStreet, Glints, Indeed and similar surfaces), follow the application flow far enough to identify the **final destination**. The intermediary page or visible Apply button alone is not proof of a usable route.
- A role-specific-looking URL such as `/apply` is **still intermediary evidence** unless the actual candidate application form renders there. Do not infer finality from the URL path, button label, or page title.
- Final-route proof requires at least one of:
  1. the actual candidate application form for the exact role renders and is usable;
  2. an employer-controlled ATS page for the exact requisition exposes a real start/submit application action with no unresolved external redirect; or
  3. a platform-native exact-role application/contact flow is directly usable and no external redirect remains.
- If JavaScript, login, cookies, bot protection, or tool limitations prevent following the route far enough to establish one of those proofs, the route is **unverified**: use `CHECK`, never `APPLY`.
- A route is usable only when the final destination is accessible for this candidate and still belongs to the intended exact role. If the final destination is removed, expired, ambiguous, login-blocked beyond verification, or otherwise cannot be confirmed, use `CHECK` at most.
- If any step in an SG application flow ultimately resolves to MyCareersFuture, immediately close/block the role with `status:blocked` + `blocked:mcf` unless a separate current non-MCF exact route is directly verified. Do not leave it as `APPLY` or `CHECK`.
- Platform-native application/contact actions such as LinkedIn Easy Apply, BOSS, 51job, 智联, 牛客 or 猎聘 may count when the actual role-level action itself is directly usable and does not redirect into a blocked channel.
- Prefer employer-controlled ATS/direct routes when available.
- If the exact final route cannot be verified, use `CHECK` with one named route blocker rather than `APPLY`.

### Freshness / recheck-at-action

A previous verification is not permanent proof of liveness.

- Before presenting an `APPLY` role to the user as ready, and again immediately before acting on a user `go`, fresh-check the exact application route.
- If the fresh check fails, downgrade to `CHECK` when the route is merely unverified, or close/block when current evidence confirms the route is stale, removed, expired, MCF-only, or otherwise unusable.
- Do not preserve `APPLY` merely because the role was live on an earlier run.
- Clearly old listings or listings with uncertain age must not survive on search-index presence alone; they need a current working exact application action.

This hard gate applies at the **verification / ready-to-apply stage**, not to every raw discovery candidate.

## Dedupe

Primary key:

`market + company + requisition/job ID`

Fallback:

`company + role + location`

For a serious survivor, check:

1. existing open/closed GitHub Issues;
2. targeted search in `lihhanko526@gmail.com`;
3. targeted search in `lihhanko3@gmail.com`;
4. ATS/candidate history only when materially available.

Do not run expensive mailbox-wide dedupe for raw discovery candidates.

## Issue states

Only four open states:

- `ACTION`
- `APPLY`
- `CHECK`
- `WAIT`

State meanings:

- `ACTION` = a concrete employer/recruiting action that should be handled now or soon, such as an OA, interview, recruiter reply, requested form/document, or real deadline. Do not use `ACTION` merely because a low-priority out-of-lane application could optionally be continued.
- `APPLY` = verified serious survivor ready for user review, with a usable exact application route. It is not authorization to submit.
- `CHECK` = exactly one material blocker or user decision remains, with exactly one next action.
- `WAIT` = already submitted/contacted and waiting for employer activity; do not duplicate.

No active Issue should use old experiment concepts such as `clean cohort`, `main sample`, or diagnostic application batches. Track the real opportunity and its next action instead.

## Labels and consistency

Every open Issue must have exactly:

1. one market label: `market:sg`, `market:cn`, or `market:my`;
2. one matching operational status label: `status:action`, `status:apply`, `status:check`, or `status:wait`.

Closed intentional outcomes may keep `status:skipped` or `status:blocked`; MCF-only SG roles may also use `blocked:mcf`.

Whenever state changes, update title, label, body and next action together. A closed/rejected Issue must not keep a misleading open-state title or label, and a role with a usable non-MCF route must not remain labeled MCF-only.

Treat these as maintenance invariants:
- no closed Issue may retain `status:action`, `status:apply`, `status:check`, or `status:wait`;
- no closed Issue title may remain `[ACTION]`, `[APPLY]`, `[CHECK]`, or `[WAIT]`;
- user feedback equivalent to `MCF` / `onclick is MCF` on an SG route → `[BLOCKED][SG][MCF]`, `status:blocked`, `blocked:mcf`;
- user feedback equivalent to `skip` / `no` / `no tq` / `I don't want` → terminal skipped state;
- user feedback equivalent to `not reachable` / `no find` / confirmed unusable route → terminal blocked state;
- after closing or relabeling an Issue, read it back and verify the terminal title, labels, body/outcome, and state agree.

## APPLY / CHECK content

Store enough to make the decision without repeating research:

- exact role link / apply route or the one CHECK blocker;
- req/job ID and verification date when available;
- plain-language work;
- hard requirements and early-career fit;
- specific strengths/gaps;
- material work-authorization evidence when known;
- targeted GitHub/Gmail dedupe result;
- exactly one next action;
- source links.

Salary, WLB, company background and networking research are optional and should be added only when they can change the decision. Do not make them mandatory verification work.

## Authorization

`APPLY` means recommended for user review, not permission to submit.

Only an explicit `go` for that exact role/action authorizes an application or external contact. Never mass apply or automatically send outreach.

## Privacy

Store only operational facts. Never copy full email bodies, auth links, tokens, passwords, secrets or unnecessary personal identifiers into Issues.

## Keep it small

Do not add Projects, another database/dashboard/frontend/spreadsheet, or a new application framework unless repeated real failures prove GitHub Issues are insufficient.
