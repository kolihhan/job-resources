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
    "last_state_change_at": "2026-10-26T13:57:40+08:00",
    "source_watermarks": {
      "freehire_event_seq": 15757
    },
    "recent_seen_keys": [
      "manatal:redalpha:QYW8W8V5", "whatjobs-sg:data engineer:94051195", "whatjobs-sg:data engineer:94037833", "whatjobs-sg:data engineer:94045725", "whatjobs-sg:data engineer:94046741", "whatjobs-sg:data engineer:94047967", "whatjobs-sg:data engineer:94050391", "whatjobs-sg:python developer:94046569", "manatal:redalpha:8X59W7WV", "manatal:redalpha:4R6WW957", "manatal:redalpha:L43436W7", "manatal:redalpha:L34Y94XW", "whatjobs-sg:data engineer:94037151", "naukri:5:291024009927", "naukri:5:141022013150", "manatal:talentweb3:W38W75YW", "mycareersfuture:eac399f067e138b998be391459373ac4", "mycareersfuture:d3cecccb9e595192f61230ee25f7df37", "manatal:wesource:W3X49449", "manatal:wesource:5WV9788R", "manatal:wesource:5WV97985", "whatjobs-sg:backend developer:94032928", "naukri:3:070521003493", "mycareersfuture:d7f6b4c6758ad0d036d7cb4119a4f143", "jobstreet:6290:95455412", "jobstreet:6290:95455304", "whatjobs-sg:data engineer:94033937", "mycareersfuture:8a7ed895383851b22f0a3f4ee31997ab", "zohorecruit:siscojobs.zohorecruit.com:696108000048625159", "manatal:work-with-us:5W958595", "manatal:work-with-us:5WR349V5", "keka:hrtech:5553", "keka:hrtech:5466", "naukri:8:151024015326", "naukri:3:080521001025", "mycareersfuture:4e0dbb07f43170894b8fb2b5772b9273", "mycareersfuture:d41681fec354b152ef718134547d1b64", "mycareersfuture:a833199031b47e71ed835a547f8db818", "mycareersfuture:12791d18dc256ff7566890fafac14b4d", "jobvite:veson:o3j0AfwG", "astar:3212", "micron:JR96479"
    ]
  },
  "CN": {
    "last_state_change_at": "2026-10-26T19:06:56+08:00",
    "source_watermarks": {
      "freehire_event_seq": 15878
    },
    "recent_seen_keys": [
      "manatal:hyred-apac:93V98694", "nowcoder:415407", "nowcoder:458229", "nowcoder:437310", "nowcoder:466220", "nowcoder:412983", "nowcoder:460621", "nowcoder:434106", "nowcoder:460589", "nowcoder:415292", "nowcoder:466398", "nowcoder:469603", "nowcoder:439289", "nowcoder:467251", "nowcoder:464026", "nowcoder:411836", "nowcoder:402337", "nowcoder:458196", "nowcoder:459703", "nowcoder:417625", "nowcoder:437982", "nowcoder:442114", "nowcoder:459127", "nowcoder:463573", "nowcoder:467328", "nowcoder:440311"
    ]
  },
  "MY": {
    "last_state_change_at": "2026-10-26T14:20:23+08:00",
    "source_watermarks": {
      "freehire_event_seq": 15878
    },
    "recent_seen_keys": [
      "whatjobs-my:data engineer:26965994", "whatjobs-my:full stack developer:26963001", "whatjobs-my:full stack developer:26962331", "whatjobs-my:full stack developer:26962221", "whatjobs-my:full stack developer:26965852", "jobstreet:compasia|ai engineer – gen ai, agentic ai & integration|petaling jaya", "jobstreet:6290:95468129"
    ]
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