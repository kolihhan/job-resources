# Discovery State

This file is **machine efficiency state only**. It is not opportunity/application state. GitHub Issues remain the only live job queue.

## FreeHire intake

- historical private-intake cursor: `513` (preserved; do not guess forward)
- public index: `kolihhan/freehirefetch/feed/index.json`
- sequence pages: `kolihhan/freehirefetch/feed/pages/*.jsonl`
- fast candidate surface: `kolihhan/freehirefetch/feed/candidates.json`
- latest public worker state checked during the 2026-10-26 migration: `last_seq=15757`, `last_success=2026-10-26T00:20:54.447314Z`
- `candidates.json` is a capped fast path, **not** a lossless queue; gap recovery uses sequence pages.

## Hourly scout incremental state

Candidate-key priority:

1. `source + exact job/requisition ID`
2. canonical exact-role URL
3. normalized `company|title|location`

Cache semantics version 2:

- exact job/requisition ID must be searched against **all GitHub Issues, open + closed**, before expensive JD research;
- cache only terminal dispositions (hard reject/duplicate/stable low-quality reject) or a survivor whose APPLY/CHECK Issue was created and read back successfully;
- do **not** cache transient failures, unresolved ambiguities, or survivors whose durable Issue handoff failed;
- a source watermark advances only after every relevant candidate through that boundary is terminally handled or durably persisted;
- `recent_seen_keys` is fallback-only, FIFO, max 500 keys per market;
- when a source exposes a trustworthy cursor/updated/posted watermark, persist it instead of relying on the fallback cache;
- `last_state_change_at` means the state object changed. It is **not** scheduler health and is not a heartbeat.

### Migration note — 2026-10-26

The v1 recent-seen caches were intentionally cleared because they mixed terminal rejects with unpersisted survivors. Keeping them would risk suppressing a good role that had never reached the GitHub queue.

All three markets are reset to the last known shared FreeHire sequence baseline `15589` so the next scout can recover the bounded `(15589, current last_seq]` gap before moving forward. This may cause one cheap re-dedupe pass; exact Issue-history search must stop known jobs before JD research.

<!-- hourly-scout-state:start -->
```json
{
  "version": 2,
  "cache_semantics": "terminal-or-durable-only",
  "migrated_on": "2026-10-26",
  "SG": {
    "last_state_change_at": "2026-10-26T05:57:31+08:00",
    "source_watermarks": {
      "freehire_event_seq": 15589
    },
    "recent_seen_keys": []
  },
  "CN": {
    "last_state_change_at": "2026-10-26T03:08:51+08:00",
    "source_watermarks": {
      "freehire_event_seq": 15589
    },
    "recent_seen_keys": []
  },
  "MY": {
    "last_state_change_at": "2026-10-26T11:18:43+08:00",
    "source_watermarks": {
      "freehire_event_seq": 15589
    },
    "recent_seen_keys": []
  }
}
```
<!-- hourly-scout-state:end -->

## Current migration receipt

### Verified fixes applied

- dedupe is a pre-JD hard gate;
- exact requisition/job IDs must use GitHub **Issue history**, not repository code search;
- verified serious survivors require durable GitHub APPLY/CHECK handoff before they can be marked handled;
- survivor Issue create must be read back; ambiguous/failed persistence cannot advance the source watermark;
- FreeHire `candidates.json` is fast-path only; watermark gaps and snapshot overflow recover from sequence pages;
- cache semantics no longer mix unpersisted survivors with terminal rejects;
- `last_success_at` was replaced by `last_state_change_at`; automation runtime is the source for scheduler health;
- cache bound increased from 200 to 500 only as a fallback for sources without reliable delta cursors.

### Prior queue receipt (not re-counted in this migration)

The previous reconciliation recorded:

- `ACTION 0 / APPLY 31 / CHECK 7`
- APPLY: `SG-ENG 5 / SG-RES 1 / CN-ENG 17 / CN-RES 2 / MY-ENG 6 / MY-RES 0`
- CHECK: `CN-ENG 3 / MY-ENG 3 / MY-RES 1`

Treat these as the prior receipt, not a fresh count. Current Issues are authoritative.

### Safety

- no application submission or employer contact is authorized by scout Issue creation;
- scouts may create only **new verified APPLY/CHECK Issues** and update their compact state object;
- scouts may not automatically modify/close/reopen existing opportunity Issues;
- no parallel candidate tracker is created.
