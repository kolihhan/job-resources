# Job Search Inbox

Private operating inbox for the current search.

## North star

Prioritize **knowledge-enhanced NLP/LLM and agentic systems**: retrieval/RAG/knowledge/memory, language understanding, reasoning/tool use, and LLM/agent evaluation. `PROFILE.md` is the canonical North-Star definition; `RULES.md` governs comparative execution.

Do not optimize raw application count, callback count, Issue count, interview count, or discovery volume in isolation.

Active markets: **Singapore + Mainland China + Malaysia**. Hong Kong is paused.

Main search: **permanent full-time**, with only the narrow research exception in `RULES.md` section 5.

## Six battlefields

| Battlefield | Purpose |
|---|---|
| `SG-ENG` | High-quality AI engineering roles worth Singapore work-pass friction. |
| `SG-RES` | MSc-compatible research engineering / applied research. |
| `CN-ENG` | Higher-throughput native/direct AI engineering search. |
| `CN-RES` | MSc-compatible research engineering / applied research with foreign-hire feasibility. |
| `MY-ENG` | **TOP / destination-quality only** AI engineering. |
| `MY-RES` | **TOP / destination-quality only** research / research engineering. |

Engineering and research are both valid outcomes. Daily strategy review reallocates effort using real funnel evidence rather than a fixed market split.

Target families include Applied AI, GenAI, LLM/RAG/Agent, Coding Agent/Harness, AI backend/software/product, ML/NLP/search/retrieval/ranking, AI evaluation/quality/testing, and realistic Research Engineer / AI Researcher / Applied Scientist / Research Scientist roles.

SG/CN generic SWE/backend/full-stack/QA titles survive only when actual team/product/JD work is materially AI-related. Strong signals preserve a generic title until the JD is read. MY retains broader destination-quality SWE eligibility under `docs/my-swe-scope.md` as a secondary option; it must not crowd out realistic North-Star work.

## Four open states

- `[ACTION]` — concrete recruiting action now/soon.
- `[APPLY]` — verified opportunity ready for my review; still needs my exact `go`.
- `[CHECK]` — live role with exactly one material blocker/decision remaining.
- `[WAIT]` — already submitted/contacted and waiting.

Rejected, expired, duplicate, blocked, withdrawn, paused-market, direction-mismatch, or intentionally skipped roles are closed.

Do not encode strategy priority with `[TOP]`. Priority comes from battlefield fit and current evidence.

## Source of truth

- GitHub Issues = live operational opportunity state.
- Gmail = recruiting lifecycle evidence + targeted dedupe.
- `PROFILE.md` = stable candidate facts + market/battlefield strategy + bounded adaptive learning memory.
- `RULES.md` = **the only detailed execution policy**.
- `DISCOVERY_STATE.md` = compact machine efficiency state only: cursors/watermarks/recent-seen receipt.
- Old spreadsheet = legacy/read-only.

No parallel candidate inbox, dashboard, spreadsheet mirror, score file, or second tracker.

## Lossless discovery model

The operating loop is:

`first-party/source delta or fresh head → derive candidate key → exact GitHub Issue-history dedupe → seen gate → cheap hard screen → ONLY THEN read full JD → verify survivor → targeted Gmail dedupe → exact route → durable APPLY/CHECK Issue or terminal reject → advance source watermark`

Two invariants:

> **duplicate/reject must die early**

> **a GOLD survivor must never disappear**

Raw candidates do not become Issues automatically. A **verified serious survivor** may be created automatically as a new APPLY/CHECK Issue by the hourly scout after all promotion gates pass. That is queue maintenance only; it does **not** authorize an application.

A survivor is not considered handled until its Issue create succeeds and the Issue is read back. If persistence fails or is ambiguous, the scout must not mark it seen and must not advance the source watermark past it.

For campus/graduate/year-coded roles, campaign/program eligibility is part of verification. If the exact JD omits the graduation window, the official campaign/program window must be checked before promotion.

### Exact-ID dedupe

When a source exposes an exact job/requisition ID, the scout searches **all GitHub Issues, including closed history**, for that ID before opening the full JD. Issue search is the gate; repository code search is not a substitute.

### Source hierarchy

Discovery is **first-party first**:

1. **Tier 1 — official/direct:** employer careers/ATS, official campus/social portals, research/university portals, employer-controlled recruiting email/direct route.
2. **Tier 2 — native/direct platforms:** BOSS/牛客 in China; LinkedIn/JobStreet/Hiredly/Indeed exact-role flows in SG/MY.
3. **Tier 3 — radar:** FreeHire, WhatJobs, generic indexes, mirrors and search snippets.

Tier 3 helps discover gaps; it does not drive the queue. The market target-company lists in `RULES.md` are priority watch lists, **not whitelists**.

### FreeHire

FreeHire is a broad upstream radar, not the human job queue and no longer the primary source for any market.

`feed/candidates.json` is the fast path, not a lossless queue. Each market scout also tracks `freehire_event_seq`. If the scout watermark lags `feed/index.json:last_seq`, a run was missed/delayed, or the capped snapshot overflows (`matched_counts > counts`), the scout recovers only the missing sequence range from `feed/pages/*.jsonl` before advancing the watermark.

This prevents scheduler delay or snapshot caps from silently dropping jobs.

### Market sourcing

**Singapore:** first-party watch includes AI Singapore/NTU, A*STAR, OpenAI Singapore, Sea/SAIL/Shopee, Grab, ByteDance/TikTok, Micron, Apple, Google, Microsoft, Singtel and selected strong finance/fintech AI teams. LinkedIn/JobStreet/Indeed and FreeHire fill gaps.

**Mainland China:** official employer/social/campus recruiting comes first for Alibaba, Tencent, ByteDance, Huawei, Baidu, Meituan, JD, Xiaohongshu and strong AI-native companies such as DeepSeek, Kimi/Moonshot, Zhipu AI and StepFun. BOSS/牛客 remain high-value because recruiter reach matters; 51job/智联/猎聘 are secondary coverage; FreeHire/aggregators are radar only.

**Malaysia:** company-first and TOP-only. Core watch includes Sea/Shopee, Grab, Gen Digital/MoneyLion, AEON Bank/GXBank, Keysight, AMD, Intel, Dell, YTL AI Labs and similarly strong product/R&D teams. LinkedIn/JobStreet/Hiredly and recruiter routes fill exact-role gaps; FreeHire remains supplementary.

Target lists prioritize search effort, not eligibility. An excellent exact role from another credible employer can still enter the queue.

## Automation

- SG AI Scout — hourly, `SG-ENG` + `SG-RES`.
- CN AI Scout — hourly, `CN-ENG` + `CN-RES`.
- MY TOP AI Scout — hourly, `MY-ENG` + `MY-RES`.
- Recruiting Signal Watch — hourly over both Gmail accounts; substantive lifecycle signals update the canonical Issue and preserve `Furthest stage`.
- AI Job Strategy Review — **daily** across all six battlefields; controlled learning may update only the bounded adaptive-memory block in `PROFILE.md` when the evidence threshold is met.

Hourly scouts may search/verify/dedupe, create a **new verified APPLY/CHECK Issue**, and update only their compact discovery cursor/cache. They do not submit applications, contact employers, modify Gmail, or automatically modify/close/reopen existing opportunity Issues.

Scheduler runtime health comes from the automation system. `DISCOVERY_STATE.md` stores `last_state_change_at`, not a heartbeat; a successful no-change run should not create a commit.

## What I should do

1. Handle time-sensitive recruiting ACTIONs and application completion as operational tasks; their urgency does not establish career fit.
2. Derive a **top 3–5 APPLY NOW** from current eligible Issues using the North Star; keep NEXT/SELECTIVE secondary views and useful CHECK resolutions separate, without new labels/trackers.
3. Say `go` only for exact roles I want submitted.
4. Resolve useful CHECK blockers.
5. Leave WAIT alone unless new evidence arrives.

Simple commands on an exact role:

- `go` — authorize that exact application/action.
- `applied` — I manually submitted it.
- `skip` — close it as intentionally skipped.

See `PROFILE.md`, `RULES.md`, and `DISCOVERY_STATE.md` for the current contract and machine state.