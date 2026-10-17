# Resume Interview Drill — Kahap Job Experience

Last updated: 2026-10-18

Primary use: technical interview preparation for the **Kahap Inc — Software Developer (Part-time)** section of the resume.

This file is a memory-recovery and interview-drill source of truth for the two main NTUST projects. The goal is to make the real work easy to explain without inventing implementation details that are no longer remembered.

---

## 0. Evidence rules

Use these labels strictly:

- **USER** — explicitly recalled by Lih Han.
- **RESUME** — currently stated in `resumes/resume-en-current.md`.
- **CODE** — directly verified from the original project source code.
- **CODE-PENDING** — source archive exists, but the claim has not yet been verified from code.
- **GENERAL** — technical knowledge that should be understood for interview follow-up; **not automatically a claim about the project**.

### Original code archives supplied

- `ntust-forum-20260608.tar(1).gz`
- `laravel-project(2).zip`

These archives still need a successful source-code audit before facts are promoted to **CODE**.

### Critical rule

> If a detail is only GENERAL knowledge, never turn it into “I did this in production” unless USER memory or CODE proves it.

Examples of things that must **not** be guessed:

- Redis vs database queue driver
- Supervisor vs systemd vs another worker manager
- Nginx vs Apache
- exact MySQL version
- exact Laravel version
- exact notification channel
- whether a specific feature used a queue
- whether `scheduler`, `worker`, or `queue` belonged to SuggestionBox, Career, or both
- exact migration commands / deployment sequence

---

# 1. Big picture — what the Kahap experience actually is

Current resume wording (**RESUME**):

- Led end-to-end development of a production feedback platform, from system design and implementation through deployment, including submission workflows, automated notifications, and admin operations.
- Shipped new features and resolved application and database issues on an existing Laravel/Vue.js production platform.
- Managed server migrations and upgrades, Laravel queues/workers/schedulers, SSL renewal, and production database troubleshooting.

The real experience should be mentally split into **two projects**, not blended into one vague “Laravel project”.

## Project A — NTUST SuggestionBox

**USER-confirmed:**

- Participated in / owned the project from **0 → 1**.
- System/design work was done by Lih Han.
- Main implementation stack: **Laravel + Livewire**.
- Deployment/server work was also handled by Lih Han.
- HTTPS was configured using **Certbot**.

This is the strongest project for questions about:

- ownership
- system design
- full-stack implementation
- taking a system from idea to production
- deployment
- HTTPS / production operations

## Project B — NTUST Career

**USER-confirmed:**

- Took over an **existing** system rather than building it from zero.
- Maintained it and added several functions/features.
- Migrated / changed the production server.
- Handled SSL / HTTPS work on the new server.

**RESUME context:** the existing production platform is described as **Laravel + Vue.js**.

This is the strongest project for questions about:

- understanding an unfamiliar existing codebase
- maintenance and incremental feature development
- production debugging
- server migration
- minimizing risk while changing a live system

## Queue / worker / scheduler ownership

**RESUME:** these are real items on the current resume.

**UNRESOLVED:** which exact NTUST project(s) used them, what driver/process manager was used, and what jobs were asynchronous.

Until the code audit or memory confirms this, do **not** attach them to a specific project in an interview answer.

---

# 2. Safe 60-second Kahap overview

Use this as the current baseline, then personalize it as memory returns:

> At Kahap I worked part-time on two main NTUST web systems. One was SuggestionBox, where I was involved from the beginning and handled the system design, Laravel/Livewire implementation, and production deployment, including HTTPS setup with Certbot. The other was an existing Career platform that I took over later. I added and maintained features there and also handled production work such as moving the application to a new server and restoring the SSL setup. So the experience was not only writing application code — I also had to understand existing systems, debug production issues, and keep the applications running after deployment changes.

### Do not over-expand this answer immediately

Stop after the high-level map and let the interviewer choose the drill direction.

Likely branches:

1. “Tell me more about SuggestionBox.”
2. “What did you design yourself?”
3. “How does Livewire work?”
4. “Walk me through deployment.”
5. “What did server migration involve?”
6. “Tell me about a production bug.”
7. “What did you use queue / worker / scheduler for?”

---

# 3. Project A — NTUST SuggestionBox

## 3.1 Facts currently safe to claim

| Claim | Evidence | Status |
|---|---|---|
| Built the system from the beginning / 0→1 | USER | Safe |
| Personally handled system/design work | USER | Safe |
| Laravel was used | USER | Safe |
| Livewire was used | USER | Safe |
| Personally handled production deployment | USER | Safe |
| HTTPS was configured with Certbot | USER | Safe |
| Submission workflow existed | RESUME | Safe at high level; recover exact flow |
| Automated notifications existed | RESUME | Safe at high level; recover exact implementation |
| Admin operations existed | RESUME | Safe at high level; recover exact functions |
| Exact DB schema/entities | CODE-PENDING | Do not invent |
| Exact Laravel/Livewire version | CODE-PENDING | Do not invent |
| Exact web server/runtime setup | CODE-PENDING | Do not invent |
| Exact queue use | CODE-PENDING | Do not invent |

---

## 3.2 The first question to master

**Interviewer:**

> You said you built the feedback platform from scratch. Walk me through what you did from the beginning until it went into production.

Your answer must eventually contain five layers:

```text
Problem / requirement
    ↓
System + data design
    ↓
Main user/admin workflow
    ↓
Laravel + Livewire implementation
    ↓
Production deployment + HTTPS
```

### Memory blanks to recover

Do not answer these from imagination. Recover them from memory/code:

- Who gave the original requirements?
- Who were the user roles?
- What could a normal user submit?
- Was submission anonymous or authenticated?
- What fields were stored?
- What statuses did one suggestion/submission move through?
- What could administrators do?
- What event triggered a notification?
- Who received notifications?
- Email, in-app, or another channel?
- What was the hardest business rule?
- Did the system handle attachments?
- Did it have search/filter/export?
- What authentication/authorization rules existed?
- What did “production ready” require before launch?

---

## 3.3 Laravel + Livewire — concepts you must be able to explain

These are **GENERAL** until the code audit maps them to the actual implementation.

### Laravel mental model

A normal Laravel request can involve:

```text
HTTP request
   ↓
Route
   ↓
Middleware / auth
   ↓
Controller or Livewire component
   ↓
Validation + business logic
   ↓
Eloquent model / database
   ↓
Blade / JSON / Livewire update
```

Know what each layer is responsible for.

### What Livewire is — ELI5

Livewire lets the UI behave interactively while much of the application logic remains in PHP.

Instead of writing a separate Vue/React frontend for every interaction:

1. the browser displays a Blade/Livewire component;
2. a user clicks/types/submits;
3. Livewire sends a request to the Laravel backend;
4. the PHP component updates state / queries the DB;
5. Livewire sends back the UI changes.

### Interview follow-up

> Why Livewire instead of Vue?

Do not invent the historical decision if you do not remember it.

Safe technical comparison:

- Livewire keeps frontend interaction close to Laravel/PHP.
- It can reduce the amount of separate frontend/API state management for server-driven forms/admin workflows.
- Vue gives more explicit client-side control and is better suited when the frontend behaves like a richer SPA.

Then say why **this project actually chose it** only after memory/code confirms the reason.

---

## 3.4 System design grill

You should eventually answer each of these without hand-waving:

1. What was the main business problem?
2. Who were the users?
3. What were the core entities/tables?
4. What was the lifecycle of one submission?
5. How did you separate user actions from admin actions?
6. How did authorization work?
7. Where did validation happen?
8. How were notifications triggered?
9. What happened when notification delivery failed?
10. What was synchronous vs asynchronous?
11. What was the most difficult edge case?
12. What did you do to prevent bad/duplicate/invalid submissions?
13. How did you test the workflow before production?
14. What did you log?
15. What would you redesign today?

### Strong interview standard

Do not just name Laravel classes.

The interviewer should be able to see the **data flow**:

```text
user action → validation → permission check → DB change → side effect → UI/admin visibility
```

---

# 4. SuggestionBox deployment + HTTPS

## 4.1 What is confirmed

**USER:** you handled deployment and used **Certbot** for HTTPS.

## 4.2 Deployment concepts to know

The exact historical sequence is **CODE-PENDING / MEMORY-PENDING**, but a Laravel production deployment normally forces you to think about:

- server OS/runtime
- PHP + required extensions
- Composer dependencies
- database connection
- `.env` / production secrets
- application key
- file/storage permissions
- web server / PHP-FPM configuration
- domain / DNS
- migrations
- cache/config optimization
- queue workers, if used
- scheduler/cron, if used
- persistent uploads/storage
- logs
- HTTPS certificate

These are a **checklist for recovering what you actually did**, not permission to claim every item.

---

## 4.3 Certbot / HTTPS — know the mechanism

**GENERAL:**

Certbot is commonly used to obtain and renew TLS certificates from **Let's Encrypt**.

Mental model:

```text
Domain DNS points to server
        ↓
Server proves control of domain
        ↓
Let's Encrypt issues certificate
        ↓
Web server serves HTTPS on 443
        ↓
Certificate renews before expiry
```

Be ready for:

- Why HTTPS is needed.
- Difference between HTTP and HTTPS.
- What a TLS certificate proves.
- Why DNS/domain configuration matters.
- What happens when a certificate expires.
- How automatic renewal is checked.
- Why you should verify the site after renewal/server migration.

### Safe answer today

> I handled the production deployment, including HTTPS. For the certificate I used Certbot with Let's Encrypt. I had to make sure the domain was pointing to the correct server, configure the web server for the application, obtain the certificate, and then verify that HTTPS and renewal were working.

Do not add the exact Certbot plugin/command (`--nginx`, `--apache`, standalone, webroot, etc.) until verified.

---

# 5. Project B — NTUST Career

## 5.1 Facts currently safe to claim

| Claim | Evidence | Status |
|---|---|---|
| Took over an existing system | USER | Safe |
| Maintained it | USER | Safe |
| Added several functions/features | USER | Safe; recover exact examples |
| Existing platform was Laravel/Vue.js | RESUME | Safe at resume level; code audit still useful |
| Migrated the application to another server | USER | Safe |
| Re-established / handled SSL on the server | USER | Safe |
| Exact features added | MEMORY-PENDING | Must recover |
| Exact server stack | CODE-PENDING | Do not invent |
| Exact migration process | MEMORY/CODE-PENDING | Recover before claiming details |

---

## 5.2 Core interview story

This project is useful because the engineering problem is different from SuggestionBox.

SuggestionBox demonstrates:

> “I can build and ship something from zero.”

Career demonstrates:

> “I can enter an existing production codebase, understand it, change it safely, and operate it.”

That distinction is valuable. Keep it.

---

## 5.3 Taking over an unfamiliar production system

Likely interviewer question:

> If you did not build the Career platform, how did you understand it well enough to change it?

Good reasoning sequence to recover from your real experience:

```text
Run / access existing system
      ↓
Understand user-facing workflow
      ↓
Trace route / backend entry point
      ↓
Trace database + frontend flow
      ↓
Make a small bounded change
      ↓
Test existing behavior + new behavior
      ↓
Deploy carefully
```

### Things you should remember

- How did you set it up locally?
- Was documentation available?
- Did another developer hand it over to you?
- Which part did you read first?
- How did Vue communicate with Laravel?
- Was it Blade + Vue components, or more SPA-like?
- What was one concrete feature you added?
- What was one old bug you fixed?
- What DB issue did you encounter?
- How did you know a change did not break old behavior?

---

# 6. Server migration — this WILL be drilled

## 6.1 What is confirmed

**USER:** you migrated / changed the server for the Career platform and handled SSL afterward.

## 6.2 Interviewer question

> Walk me through the server migration. What did you actually move and how did you reduce risk?

Do not answer only:

> “I copied the project to another server.”

A web application has more state than source code.

### Migration inventory — GENERAL recovery checklist

Ask yourself which of these you actually moved/recreated:

```text
Application code
Production .env / secrets
Database
User-uploaded files / storage
PHP/runtime dependencies
Web server config
Domain / DNS
SSL certificate setup
Cron / Laravel scheduler
Queue workers
Process manager
Permissions
Logs / monitoring
```

### Safe conceptual sequence

A controlled server migration usually looks like:

```text
1. Inventory old environment
2. Back up DB / persistent files
3. Prepare compatible new server
4. Deploy application + dependencies
5. Restore/configure DB and storage
6. Restore production environment configuration
7. Test app on new server
8. Switch traffic / DNS
9. Configure and verify HTTPS
10. Verify background processes
11. Watch logs / errors
12. Keep rollback path until stable
```

Again: this is the **knowledge model**. During an interview, replace it with the steps you genuinely remember performing.

---

## 6.3 Migration failure modes to know

An interviewer may ask “what can go wrong?”

Be able to reason about:

- incompatible PHP/Laravel/Composer versions
- missing PHP extensions
- wrong environment variables
- wrong database credentials
- migration/schema mismatch
- missing user-uploaded files
- `storage` / cache permission issues
- forgotten queue worker
- forgotten scheduler/cron
- DNS still pointing at old IP
- SSL issued/configured for the wrong server/domain
- application caches containing stale config
- old server still processing background jobs

Do **not** say you personally hit these unless true.

---

# 7. Queue / worker / scheduler — resume defense

Current resume explicitly contains:

> Laravel queues/workers/schedulers

So this is interviewable even before we know which project used what.

## 7.1 Queue — ELI5

A queue stores work that should be processed separately instead of blocking the current user request.

Example concept:

```text
User submits request
      ↓
App saves DB state
      ↓
Job is placed on queue
      ↓
HTTP response can finish
      ↓
Worker processes job later
```

Typical reasons:

- email / notifications
- slow external API calls
- file processing
- batch jobs

Do **not** claim those were your exact queued tasks until confirmed.

## 7.2 Worker

A worker is the long-running process that pulls queued jobs and executes them.

Laravel concept to recognize:

`php artisan queue:work`

Interview follow-ups:

- What happens when a worker crashes?
- How are failed jobs handled?
- Why might workers need restarting after deployment?
- How do retries create duplicate side effects?
- What is idempotency?

## 7.3 Scheduler

Laravel Scheduler defines recurring application tasks in code.

Typical production mechanism:

```text
OS cron triggers Laravel schedule runner
                  ↓
Laravel decides which scheduled tasks are due
```

Concept to recognize:

`php artisan schedule:run`

Do not confuse:

- **scheduler** = decides *when* a recurring task should run
- **queue** = stores work waiting to be processed
- **worker** = executes queued work

## 7.4 Red lines

Until verified, do not say:

- “We used Redis.”
- “Supervisor managed the workers.”
- “SuggestionBox notifications were queued.”
- “Career used the database queue.”
- “The scheduler ran X every night.”

All of those may be true, but they require evidence.

---

# 8. Production bug debugging

This is more important than memorizing Laravel trivia.

## 8.1 Generic debugging sequence

When something breaks in production:

```text
1. Define the symptom precisely
2. Check scope: one user / one feature / whole system?
3. Check logs and error message
4. Reproduce if possible
5. Check recent changes
6. Trace request/data flow
7. Isolate app vs DB vs environment/server
8. Fix the smallest root cause
9. Verify affected + nearby flows
10. Monitor after deployment
```

### Laravel things you should know where to inspect

**GENERAL:**

- application logs
- validation exceptions
- stack traces
- route/middleware/auth behavior
- config/environment differences
- cache/config issues
- database errors
- queue failures
- server/web-server logs when the request never reaches Laravel correctly

---

## 8.2 Database problem drill

**Interviewer:**

> You wrote that you troubleshot production database issues. Give me an example.

We still need a **real incident** from your memory/code.

For every incident, recover this exact structure:

```text
Symptom:
What evidence did I check first?
What did I initially suspect?
What was the actual root cause?
What did I change?
How did I verify it?
What would prevent it next time?
```

### DB failure categories to distinguish

**GENERAL:**

- connection/configuration failure
- missing/wrong schema migration
- incorrect data
- application query bug
- constraint violation
- slow query/index problem
- transaction/concurrency issue

Do not jump to “indexing” just because an interviewer says DB problem. Diagnose from evidence.

---

# 9. High-value interview questions — grill list

## SuggestionBox — ownership

1. What was the original requirement?
2. Who were the users?
3. What did you personally design?
4. Draw the main workflow.
5. What were the core database entities?
6. Why Laravel?
7. Why Livewire?
8. How did one Livewire action reach the database?
9. What validation and authorization existed?
10. How did notifications work?
11. What was the hardest feature?
12. What production bug do you remember?
13. How did you deploy it?
14. How exactly did HTTPS/Certbot fit into the deployment?
15. What would you redesign now?

## Career — takeover + maintenance

1. What did the Career system do?
2. What stack/version did it use?
3. How did you understand a codebase you did not build?
4. Name two or three functions you added.
5. Name one application bug you fixed.
6. Name one DB issue you fixed.
7. What was risky about modifying a live existing system?
8. Why did the server need to move?
9. What did you copy vs reinstall vs reconfigure?
10. How did you move the DB/persistent files?
11. How did you switch the domain to the new server?
12. What did you do for SSL afterward?
13. How did you verify the migration succeeded?
14. Was there a rollback plan?
15. What background jobs/schedulers had to survive the move?

## Queue / worker / scheduler

1. What actual job did you queue?
2. Why not execute it synchronously?
3. Which queue driver did you use?
4. What starts the worker?
5. What happens after a worker crashes?
6. How did you inspect failed jobs?
7. How did you avoid duplicated side effects on retry?
8. What scheduled task did the system have?
9. How was the scheduler triggered in production?
10. What deployment step could accidentally leave old workers running old code?

If any answer is currently “I forgot”, that becomes a **memory/code-recovery target**, not something to improvise.

---

# 10. Strong answer format for any work-experience story

Use **Context → Ownership → Technical path → Problem → Evidence/Result**.

Example skeleton:

```text
Context
- What system / user problem?

Ownership
- What was specifically mine?

Technical path
- How did the request/data move through the system?

Problem
- What went wrong / what constraint mattered?

Evidence / Result
- How did I verify the feature/fix/deployment worked?
```

This is stronger than listing tools:

> Laravel, Vue, Livewire, MySQL, Linux, Certbot...

The interviewer wants to know whether you understand the system you operated.

---

# 11. Resume risk check

## Bullet 1

> Led end-to-end development of a production feedback platform, from system design and implementation through deployment, including submission workflows, automated notifications, and admin operations.

Main drills:

- “Led” / personal ownership
- exact workflow
- architecture
- notification implementation
- admin permissions
- deployment

Current evidence status:

- 0→1, design, Laravel/Livewire, deployment: **USER**
- submission/notification/admin detail: **RESUME**, needs exact recovery

## Bullet 2

> Shipped new features and resolved application and database issues on an existing Laravel/Vue.js production platform.

Main drills:

- which exact features?
- one application bug
- one DB bug
- how Vue and Laravel interacted

Current evidence status:

- existing-system takeover + feature work: **USER**
- Laravel/Vue.js: **RESUME**
- exact incidents: **MEMORY-PENDING**

## Bullet 3

> Managed server migrations and upgrades, Laravel queues/workers/schedulers, SSL renewal, and production database troubleshooting.

This is the **highest-risk bullet** if memory is weak because every noun can create a technical drill tree.

Must recover:

- migration: old → new environment and concrete steps
- queue: actual job + driver
- worker: how process stayed running / restarted
- scheduler: actual scheduled task + production trigger
- SSL: Certbot flow + renewal
- DB troubleshooting: at least one real incident

---

# 12. Code-audit checklist for the supplied archives

When the archive execution environment is available, inspect **all interview-relevant source**, not only README files.

## Phase A — identify which archive is which project

Check:

- `composer.json`
- `package.json`
- app name / README
- routes
- namespaces / views / UI text

## Phase B — architecture inventory

Inspect:

- `routes/web.php`
- `routes/api.php`
- `app/Http/Controllers/**`
- `app/Livewire/**` or `app/Http/Livewire/**`
- `app/Models/**`
- `database/migrations/**`
- `resources/views/**`
- `resources/js/**`
- auth/middleware/policies

Output:

```text
user flow → route/component → service/business logic → model/table → side effect
```

## Phase C — background work

Search:

- `ShouldQueue`
- `dispatch(`
- `Job`
- `Notification`
- `Mail`
- queue config
- scheduler definitions
- console kernel / scheduled commands
- process-manager config if included

Goal: resolve **queue / worker / scheduler** claims exactly.

## Phase D — production/deployment evidence

Search for:

- nginx / apache config
- Docker files
- deployment scripts
- `.env.example`
- storage links
- cron
- Supervisor/systemd configs
- SSL/certbot references
- server migration notes

Do not expose real secrets from `.env` files.

## Phase E — git/history evidence if included

If `.git` exists:

- identify Lih Han's commits
- map concrete features/fixes
- find server/deployment changes
- extract real bug stories from commits

## Phase F — update this document

Promote only proven facts:

```text
USER / RESUME / CODE-PENDING → CODE
```

Add exact file paths beside important claims so interview revision remains evidence-first.

---

# 13. Next grill order

Do this **one question at a time**, not as a giant quiz.

### Round 1 — SuggestionBox business flow

> What exactly happened from the moment a user opened SuggestionBox until an admin finished handling one submission?

### Round 2 — SuggestionBox architecture

> Which Laravel/Livewire pieces handled that flow, and what did the main database tables represent?

### Round 3 — deployment

> Start with a blank/new server. What do you remember doing until the production domain showed the application over HTTPS?

### Round 4 — Career takeover

> Name the first real feature you remember adding after taking over the Career system. Trace it from UI → backend → DB.

### Round 5 — server migration

> What triggered the server move, what state had to be preserved, and how did you know the new server was safe to cut over to?

### Round 6 — production incident

> Give one real application or database problem you saw in production. We will reconstruct the debugging path from evidence, not from the final answer.

### Round 7 — queue / worker / scheduler

> Which exact background task do you remember? If none yet, stop and recover it from code before practicing an interview answer.

---

## Final rule

The target is **not** to memorize a polished story.

The target is to recover enough real system understanding that follow-up questions remain consistent:

```text
what I built
→ how data flowed
→ why it was designed that way
→ how it failed
→ how I debugged it
→ how I deployed/operated it
```

If those six layers are solid, the Kahap experience becomes one of the strongest parts of the resume rather than a risky bullet to defend.
