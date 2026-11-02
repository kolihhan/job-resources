# FreeHire Gap Recovery Design

## Intent

Restore lossless FreeHire radar coverage for the SG, CN, and MY hourly scouts without weakening the existing first-party/native-platform discovery floors.

## Current failure

`DISCOVERY_STATE.md` records FreeHire watermarks around 15.8k while `kolihhan/freehirefetch/feed/index.json` is above 36k. Current scout prompts require market broad/native discovery floors but do not require a bounded FreeHire recovery slice on every lagging run. Recent scout output explicitly reports the backlog without advancing it, so the gap can persist indefinitely.

## Approaches

1. **Jump watermarks to current head** — rejected because it permanently drops unseen events and violates the lossless contract.
2. **Recover the entire backlog in one run** — rejected because a 20k+ sequence backlog can make an hourly scout unbounded and fragile.
3. **Bounded sequential recovery** — chosen. When a market watermark lags upstream, process the next contiguous block of at most 500 sequence events. Events for other markets are cheap skips; matching-market events follow normal dedupe/hard-screen/promotion rules. Advance only through a fully handled boundary.

## Constraints

- FreeHire remains Tier-3 radar and never replaces the SG/MY broad-platform floor or CN native-platform floor.
- Never skip sequence ranges or guess a watermark forward.
- A relevant survivor must be durably persisted as APPLY/CHECK and read back before the watermark can pass it.
- A transient fetch/verification/write failure blocks advancement past the affected sequence.
- Existing opportunity Issues must not be mutated by scouts.
- Chunk size is at most 500 global sequence events per market scout run while backlog exists.

## Success

Each lagging hourly run either advances that market's `freehire_event_seq` by a fully handled contiguous chunk (up to 500 seq) or reports the exact blocking sequence/reason. Once caught up, normal fresh-head behavior resumes.
