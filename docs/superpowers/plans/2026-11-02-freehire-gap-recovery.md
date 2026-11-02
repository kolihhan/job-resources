# FreeHire Gap Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make every lagging SG/CN/MY hourly scout consume a bounded contiguous FreeHire backlog slice instead of leaving the watermark indefinitely stale.

**Architecture:** Keep existing discovery floors unchanged. Add one canonical repo supplement that defines a max-500 sequence recovery slice, then make each automation read and execute that supplement. Verification is behavioral: run each scout once and confirm either watermark progress or an explicit blocking sequence.

**Tech Stack:** GitHub repository policy/docs + ChatGPT Automations

**Spec:** `docs/superpowers/specs/2026-11-02-freehire-gap-recovery-design.md`

## Global Constraints

- Never jump or guess a watermark forward.
- FreeHire remains radar only.
- Max recovery slice is 500 global sequence events per market run.
- Existing opportunity Issues remain read-only to scouts.

## Review Focus

- Backlog exists but a run still reports success without attempting recovery.
- A relevant candidate is unresolved but the watermark advances past it.
- Broad/native market floors get accidentally replaced by FreeHire work.
- A scout tries to process the entire 20k+ backlog in one run.
- A survivor is marked handled before durable Issue create/readback.

---

### Task 1: Canonical recovery contract

**Files:**
- Create: `docs/freehire-gap-recovery.md`

- [ ] Define upstream-vs-market watermark comparison.
- [ ] Define contiguous max-500 recovery interval.
- [ ] Define cheap cross-market skipping and normal handling for matching-market events.
- [ ] Define advancement and blocker rules.

### Task 2: Wire all three scouts

**Files:**
- Automation: `SG AI Scout`
- Automation: `CN AI Scout`
- Automation: `MY TOP Tech Scout`

- [ ] Add `docs/freehire-gap-recovery.md` to required repo reads.
- [ ] Require the repo-defined recovery floor before reporting no new survivors.
- [ ] Keep existing market discovery floors unchanged.

### Task 3: Behavioral verification

- [ ] Run SG scout once.
- [ ] Run CN scout once.
- [ ] Run MY scout once.
- [ ] Confirm each run attempts the recovery floor when lag exists.
- [ ] Re-read `DISCOVERY_STATE.md`; verify cursor progress or capture exact blocker evidence.
