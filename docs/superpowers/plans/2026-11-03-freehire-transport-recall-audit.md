# FreeHire Transport + Recall Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make hourly FreeHire consumption connector-safe without shrinking recall, then measure cheap-screen false negatives instead of assuming the filter is correct.

**Architecture:** Keep the full cold-start snapshot unchanged for machine filtering and rebuilds. Compress only the private hourly batch transport to metadata needed for cheap screening; deep-read authoritative JDs only for survivors and a small reject-audit sample. Active docs point to one canonical FreeHire contract.

**Tech Stack:** Python 3.13, unittest, GitHub Actions, Markdown contracts.

**Spec:** `docs/superpowers/specs/2026-11-02-discovery-pipeline-v2-design.md`

## Global Constraints

- GitHub Issues remain the only live opportunity queue.
- Strong identity may suppress; weak company/title identity may not.
- Keep the full cold-start candidate set and upstream high-recall filtering unchanged.
- Do not tune shard item count to one observed market payload; remove large JD text from hourly transport instead.
- Public repo: use GitHub Actions for regression and derived-state validation.

## Review Focus

- Long JD text must not leak back into hourly shards.
- Required cheap-screen identity/signal fields must remain present.
- 100-candidate throughput and stable candidate_seq semantics must remain unchanged.
- Reject audit must not turn sampled rejects into automatic survivors; it only checks whether the cheap rule was wrong.
- Old raw-sequence/30-candidate wording must not remain active in canonical docs.

---

### Task 1: Compact hourly batch transport

**Files:** `tests/test_freehire_review_throughput.py`, `scripts/build_freehire_review_queue.py`

- [ ] Add failing tests proving hourly candidates omit `description_excerpt`/large payload text while preserving IDs, company/title/location, source URL, known status, AI signals/score, flags, employment type, dates, role_key and candidate_seq.
- [ ] Add a serialized-size regression test using deliberately huge descriptions.
- [ ] Implement one compact-candidate projection before batch/shard generation.
- [ ] Run the derived-state test suite in GitHub Actions and verify generated SG/MY shards are readable without truncation.

### Task 2: Canonicalize active contracts

**Files:** `README.md`, `docs/freehire-triage-consumption.md`, `docs/fresh-discovery-rotation.md`

- [ ] Replace stale 30-candidate/raw-250 wording with references to the active 100 cheap-screen / 15 deep-read / 10 retry contract.
- [ ] State that shards are metadata transport, not cached full JDs.

### Task 3: Add false-negative audit

**Files:** `docs/freehire-triage-consumption.md`, `docs/scout-run-metrics.md`, existing SG/CN/MY automation prompts.

- [ ] Require up to 5 stratified cheap-reject audits per run, using authoritative/best available JD evidence.
- [ ] Track `reject_audit_sampled` and `reject_audit_false_negatives` separately from normal deep reads.
- [ ] If an audited reject proves to be a real survivor, route it through the normal final gates and count it as a false negative; do not silently retune rules from one case.
- [ ] Use SG/MY as holdout validation for transport because CN already succeeded under the old payload shape.

### Task 4: Verify deployed behavior

- [ ] Trigger/observe the public GitHub Action refresh.
- [ ] Read back generated manifest/shards and confirm compact payloads.
- [ ] Run one SG and one MY scout cycle; confirm no shard-truncation blocker and metrics include reject-audit fields.
- [ ] Record any remaining blocker as evidence for the next mechanism change rather than tuning another arbitrary shard count.
