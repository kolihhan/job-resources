# Public ATS Feed — Verified Candidate Intake

Purpose: turn the browserless, first-party ATS feed into **new verified job opportunities**, not a separate application tracker. This is an execution supplement to `README.md`, `PROFILE.md`, `RULES.md` and `docs/source-routing.md`; those policies win on conflict.

## Source

- Public data producer: `kolihhan/freehirefetch` — `.github/workflows/ats-discovery.yml`, `ats_discovery.py`, `ats_boards.json`.
- **Current searchable snapshot:** `kolihhan/freehirefetch/feed/ats/current.json` (all public candidate identities currently retained). Do not process only `changes.json` — it is **one-run ephemeral** and can be overwritten between Scout executions.
- `feed/ats/health.json` identifies complete vs failed boards; ignore absence as proof of closure when a board fails. A board with `scope: targeted_keywords` is only keyword-coverage, not an exhaustive company scan.
- **Full JD evidence is sharded for reliable GitHub reading:** first read public `feed/ats/current.json` (compact candidate identities), then `feed/ats/jd/index.json` and the relevant `feed/ats/jd/<market>-<part>.json` when more than the short `description_excerpt` is needed. Match `key` exactly. Each part contains at most 10 public employer-authored JD records, not private applicant data. An `ats_discovery` key is ATS slug/type/job ID; compare employer requisition IDs across sources. `evidence: listing_only` has no full JD; `evidence: partial_jd` means long content was truncated and the exact source must be opened. Even `full_jd` from the public feed requires a fresh exact employer-role liveness and application-route check before an APPLY/CHECK Issue.
- The feed contains only **public employer listings**, without Gmail, application, user identity, CV, or private evaluation results. GitHub Issues remain the **only operational application queue**.

## Every SG, MY, CN Scout run — ATS-first intake

1. **Start** with the newest readable `current.json`, `health.json` and the sharded `jd/index.json` for full-JD lookups. Never parse a large monolithic JD field inside `current.json`; use per-market shard paths and exact candidate keys. Filter to market; prioritize verified employer boards covering direct AI Engineering **and** Research. Do not spend the first phase on FreeHire unless the existing bounded stalled-cursor checkpoint exception applies. Do not claim that a currently failed ATS board had no jobs.
2. Target **up to 20 distinct public exact job IDs per market per cycle for cheap screen**, prioritizing plausible 0–3-year roles, different employers/team families, genuinely AI-centric responsibilities, and first-seen/changed roles. **Ceiling, not success quota.** Explicit Senior/Staff/Lead/mature hard mismatches die cheaply. A company name or generic “AI Finance Agent” label in an otherwise unrelated mobile/frontend role is **not** AI ownership. Keep qualified MY destination-quality SWE secondary under `docs/my-swe-scope.md`.
3. Before opening the JD, exact-search **all open and closed** GitHub Issues by stable employer requisition ID, plus company/title where identity is ambiguous. Avoid deep-reading already-applied or unchanged SKIP/WAIT. Do not equate two distinct employer IDs because titles match.
4. For the most plausible **up to 6–10 substantive new roles per run** (subject to tools/time), open exact current employer JD, hard YOE/degree/cohort/employment, SG/CN visa feasibility if explicit, actual AI ownership, and **real usable application link**. Search BOTH Gmail accounts only for serious promotion candidates. Follow `RULES.md` for CHECK's **exactly one blocker**. Never create raw, unverified or stale Issues to meet a count.
5. Persist and read back **new verified APPLY/CHECK Issues**. Only then store durable handled keys in the established market-owned terminal/recent-seen state. For plausible unresolved roles use existing market retry receipts with decisive next evidence, do not silently drop. Do not mark unknown evidence terminal. For a confirmed hard reject/duplicate use existing bounded terminal cache. Cursor/cache changes need to be read back; no second personal candidate tracker.
6. Then continue one bounded native-platform/coverage-debt probe and independent FreeHire recovery as budget allows. Persist truthful `PARTIAL_COVERAGE` for unfinished work. 100+ metadata rows are **not** 100 apply-ready jobs.

## Outcome reporting

For each run: **new verified APPLY URLs/count, new verified CHECK URLs/count**, distinct employer ATS IDs cheaply screened, actual complete JDs, exact duplicates, hard rejects, unverified blockers/receipts, source coverage gaps, and evidence of durable handoff. Include a coverage-by-employer breakdown to detect one-employer domination (BJAK was 93 of the first 134 candidates). Do not invent application probabilities or claim a source is exhausted when Workday uses targeted keywords.

## Overnight PI target

Use the overnight Scout cycles to maximize the number of **real, deduplicated, verified opportunities awaiting the user's application decision**. The aspirational target of 100 belongs to **candidate auditing throughput**, not a mandate to falsely produce 100 APPLY issues. Keep no applications sent; exact user authorization is still required. On the morning report distinguish verified new APPLY, verified new CHECK, older outstanding APPLY, and raw ATS leads rather than combining them into a misleading number.
