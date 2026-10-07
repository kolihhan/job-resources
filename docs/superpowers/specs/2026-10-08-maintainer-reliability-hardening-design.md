# Maintainer Reliability Hardening Design

Date: 2026-10-08
Status: Proposed — awaiting user review

## Goal

Improve the existing job-search maintainer without redesigning it. The objective is to reduce repeated discovery work, make discovery effort auditable, prevent requirement over-filtering, and make ambiguous GitHub writes safer while preserving the current high-precision freshness and dedupe gates.

The existing architecture stays intact:

- GitHub Issues remain the only live operational opportunity state.
- Gmail remains recruiting evidence and targeted dedupe evidence.
- `RULES.md` remains the only detailed execution-policy source.
- `DISCOVERY_STATE.md` remains a small rolling discovery receipt / next-rotation record, not a tracker.
- Scheduler prompts remain thin wrappers that read the repo contract.

## Non-goals

This change must not introduce:

- a second tracker, database, dashboard, scoring system, scraper framework, knowledge graph, or agent framework;
- a new scheduler cadence;
- a quota requiring a fixed number of survivors or applications per run;
- weaker freshness, sponsorship, cohort, seniority, route, or dedupe gates;
- bulk cleanup of historical `WAIT` Issues unless separate evidence requires it;
- automatic applications or external outreach.

`Understand Anything` is not added to this repository because the system is mostly policy + Issues + Gmail + discovery state rather than a complex code dependency graph. Matt Pocock-style agent-document principles are useful here only insofar as they preserve `RULES.md` as the canonical policy source. Ponytail/YAGNI remains the design constraint.

## Current failure modes

### 1. Discovery effort is hard to audit

`DISCOVERY_STATE.md` currently records source families and qualitative lanes, but a plausible-looking receipt can still hide a shallow search. A run may say it covered official careers, LinkedIn, JobStreet, Indeed, or multiple CN sources without showing how many distinct candidates or employers were actually screened.

This is a recall-observability problem, not a survivor-count problem.

### 2. Soft requirements can be misread as hard blockers

The independent control probe found a concrete example: Qore3's current Junior Blockchain Engineer wording is fresh-graduate compatible and allows blockchain familiarity from coursework, self-study, or personal projects. An earlier scheduler receipt summarized the role as requiring blockchain experience and filtered it.

The cheap screen therefore needs a clearer hard-vs-soft requirement rule.

### 3. Discovery can repeat inside the same scheduled window

Scheduled discovery runs during MYT hours `00/04/08/12/16/20`. A complete interactive or scheduled discovery can finish shortly before the hourly maintainer runs again in the same four-hour window. Without an idempotency rule, the next maintainer run may repeat discovery that is already complete.

### 4. Ambiguous GitHub writes can create duplicates

A `create_issue` call can time out even though GitHub later materializes the Issue. Retrying immediately can create a duplicate, as happened with Chainlabs (`#156` / `#157`). Read-back after a successful response is insufficient for ambiguous timeout / 5xx outcomes.

## Design

### A. Add compact discovery coverage counters

Keep `DISCOVERY_STATE.md` small, but require the discovery receipt to include bounded coverage evidence for each main market actually searched:

- number of raw employer-role candidates cheap-screened;
- number of distinct employers represented in those candidates;
- number of materially distinct source families used;
- number of candidates that reached deep verification;
- optional Web3 values when that lane is used.

Example:

```text
SG coverage: 14 candidates / 10 employers / 3 source families / 2 deep-verified
CN coverage: 18 candidates / 12 employers / 4 source families / 3 deep-verified
Web3 coverage: 6 candidates / 5 employers / 2 source families / 1 deep-verified
```

These counters are evidence of search effort only. They do not become quotas, scores, history tables, or success targets.

A run with `18 screened -> 0 survivors` can be healthy. A run with very low screening coverage is not automatically wrong, but it becomes visible and auditable.

`DISCOVERY_STATE.md` still must not contain long raw-candidate logs.

### B. Make the cheap hard filter explicitly requirement-aware

At broad-discovery / cheap-screen stage, reject only when the JD establishes a genuine hard blocker.

Treat wording such as these as non-hard by default unless the surrounding JD clearly makes them mandatory:

- preferred;
- plus / bonus / nice to have;
- familiarity with;
- exposure to;
- coursework;
- self-study;
- personal projects;
- willingness to learn.

Such items should be recorded later as fit gaps, not used for cheap rejection.

Professional-experience language remains a hard blocker when the JD clearly requires it, for example `5+ years required`, `must have production experience in X`, or an equivalent unambiguous mandatory condition.

This rule does not mean every fresh-graduate-compatible Web3 role is good. It only prevents a soft domain gap from being converted into fake professional-experience requirements.

### C. Make scheduled discovery idempotent by four-hour window

Define scheduled discovery windows in MYT:

- `00:00-03:59` -> `00` window
- `04:00-07:59` -> `04`
- `08:00-11:59` -> `08`
- `12:00-15:59` -> `12`
- `16:00-19:59` -> `16`
- `20:00-23:59` -> `20`

Before scheduled discovery, inspect the latest `DISCOVERY_STATE.md` receipt.

If the current window already contains a completed SG + CN discovery that satisfies the current contract and has a successful read-back receipt, the maintainer performs maintenance only and skips duplicate discovery for that window.

An explicit interactive search requested by the user can still run at any time. If that interactive run intentionally satisfies the full scheduled SG + CN contract and records a valid receipt, it counts as the discovery for that current window.

If the prior run was incomplete, one market was skipped, a required write failed, or the receipt was not verified, the window is not considered complete.

No external lock, database, or workflow state is introduced.

### D. Make ambiguous Issue creation retry-safe

For `create_issue` or equivalent GitHub create operations:

1. perform normal exact-req and employer-role-family dedupe before the write;
2. attempt the create once;
3. if the response is successful, read back and verify as today;
4. if the response is ambiguous (`timeout`, connection error, transient 5xx, or similar uncertain outcome), do **not** immediately retry;
5. search recent Issues using the intended exact requisition / employer + role fingerprint and inspect recent creations;
6. if the intended Issue exists, use it and stop;
7. if it still does not exist after verification, retry once;
8. read back again;
9. if the second outcome is still ambiguous, stop and report the incomplete write rather than looping.

This applies to create semantics where duplicate side effects are possible. It does not require a generalized transaction framework.

## Optional small maintenance rule

Unmapped recruiting email delivery failures may be surfaced once to the user when they represent a failed job-search outreach but do not map cleanly to an existing Issue. Do not create a synthetic CRM-style Issue solely for the bounce.

This is optional polish and is not required for the core reliability patch.

## Files / surfaces affected in implementation

Expected minimal implementation surface:

1. `RULES.md`
   - add compact coverage receipt requirements;
   - add hard-vs-soft cheap-screen wording;
   - add same-window scheduled-discovery idempotency;
   - add ambiguous-write retry behavior.
2. `DISCOVERY_STATE.md`
   - next completed discovery receipt adopts compact coverage counters.
3. `Job Inbox Maintainer` automation
   - keep the prompt thin; only adjust if needed so it obeys the repo's current-window completion rule rather than duplicating policy text.
4. `Job System Health Watch` automation
   - optionally add a health invariant that flags repeated discovery in the same completed window or malformed coverage receipts. It should point back to `RULES.md`, not restate the rules.

`README.md` and `NEXT_CHAT_PROMPT.md` should not need substantive policy changes unless implementation reveals a stale pointer.

## Verification / regression cases

Implementation is not complete until the following cases are checked:

### Coverage receipt

- A discovery run records compact SG + CN coverage counts.
- Counts are plausible against the actual candidates inspected in that run.
- No raw-candidate dump or second tracker is created.

### Hard-vs-soft parsing

- A JD saying `5+ years required` can still be cheap-rejected.
- A JD saying `blockchain familiarity from coursework/self-study/personal projects` is not rejected as if it required professional blockchain experience.
- A preference such as `Kubernetes preferred` remains a gap, not a hard blocker.

### Same-window idempotency

- Full compliant discovery at `00:18 MYT` followed by the hourly maintainer at roughly `00:30` results in maintenance only, not another broad discovery.
- An incomplete `00`-window run still allows a later maintainer in that window to finish discovery.
- A user explicitly requesting a fresh interactive search can still override the ordinary skip behavior.

### Ambiguous GitHub create

- Simulated/observed timeout after issue creation triggers search/read-back before retry.
- Existing delayed Issue is adopted rather than duplicated.
- If no Issue exists, only one retry occurs.
- Persistent ambiguity stops safely and is reported.

### Existing gates remain intact

- Stale aggregator result whose official role is expired remains filtered.
- Same-employer same-role-family duplicate remains suppressed.
- Unknown sponsorship is not converted into an automatic discovery rejection.
- Explicit no-sponsorship/citizenship/cohort hard blockers still filter correctly.

## Success criteria

The patch succeeds when:

- discovery effort is auditable without becoming another tracker;
- a soft requirement cannot silently become a fabricated hard-experience blocker;
- one valid discovery per scheduled four-hour window is sufficient;
- ambiguous GitHub creates no longer cause immediate duplicate retries;
- freshness and dedupe precision do not regress;
- no new infrastructure or parallel policy source is introduced.

No numeric claim is made that these changes will increase callbacks or survivor count. The expected benefit is narrower: less wasted work, better recall diagnostics, and fewer avoidable false negatives / duplicate side effects.
