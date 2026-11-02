# FreeHire Raw Gap Recovery — Superseded

> **Status:** superseded for normal hourly scout execution on 2026-11-03.
>
> Active contract: [`docs/freehire-triage-consumption.md`](./freehire-triage-consumption.md).

The old hourly path read `freehirefetch/feed/pages/*.jsonl` from a per-market raw event watermark and could stop behind one unreadable or transiently unverifiable sequence. That path is no longer the normal reasoning contract.

## Active replacement

Hourly SG/CN/MY scouts now consume bounded private market batches produced from the current full-JD FreeHire cold-start scan:

`FreeHire full scan -> conservative machine candidate set -> private known-role strong dedupe -> stable candidate_seq -> 30-candidate market batch -> hourly scout`

The current market state is:

- `discovery-state/triage-sg.json`, `retry-sg.json`, `freehire-batch-sg.json`
- `discovery-state/triage-cn.json`, `retry-cn.json`, `freehire-batch-cn.json`
- `discovery-state/triage-my.json`, `retry-my.json`, `freehire-batch-my.json`

A transient candidate verification failure is moved into a durable retry receipt so later candidate sequences can continue. Weak company/title matches remain suspicion only and cannot suppress a role.

Raw FreeHire event pages and the legacy `discovery-state/freehire-*.json` watermarks are retained for audit/rebuild history only. Hourly scouts must not scan or advance them during normal operation.

## Historical algorithm

The superseded implementation used a contiguous global event watermark `W`, upstream head `H`, and a bounded target `B = min(W + 500, H)`. A market scout read every raw event in `(W, B]`, cheap-skipped other markets, and could advance only through a fully handled contiguous prefix.

That design provided lossless raw-event recovery but had two operational costs:

1. compact event records did not always contain enough substantive JD text for reliable relevance decisions;
2. one unresolved relevant event could stall all later events for that market.

The public raw event feed remains useful for audit and future deterministic rebuild work, but expensive hourly reasoning now follows the bounded triage contract instead.
