# FreeHire helper

`freehire_fetch.py` is a small discovery helper, not a second tracker.

It reads FreeHire's public unauthenticated `/api/v1/jobs/search` endpoint for SG/CN engineering categories. By default it uses the API maximum deep-page window: `limit=100`, offsets `0..9900`, so up to **10,000 rows per market**. It stops early when `meta.total` is exhausted.

```bash
python scripts/freehire_fetch.py
```

Outputs go to `.freehire/`:

- `freehire-<market>-raw.jsonl` — raw FreeHire rows in the fetched slice
- `freehire-<market>-screened.jsonl` — survivors after conservative cheap screening
- `freehire-<market>-rejected.jsonl` — obvious rejects with `cheap_reject_reason`
- `freehire-<market>-summary.json` — counts

For an incremental run, narrow by when FreeHire first saw the posting:

```bash
python scripts/freehire_fetch.py --open-within-days 2
```

Important: FreeHire is discovery evidence only. A screened row still needs the existing GitHub/Gmail dedupe and official exact-role liveness/application-route verification before an Issue is created.
