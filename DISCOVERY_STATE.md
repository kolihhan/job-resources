# Discovery State

This is a tiny rolling audit receipt for the **latest scheduled discovery run**. It is not a job tracker and must not contain raw candidate dumps.

The maintainer overwrites this file after each scheduled discovery window so the next run can rotate sources/keywords and the health check can tell the difference between a real zero-result run and a skipped/lazy run.

## Current receipt

- status: `bootstrap`
- schema_started_at: `2026-10-07 09:37 MYT`
- last_discovery_run: `not yet recorded under this schema`
- expected_next_window: `2026-10-07 12:xx MYT`
- SG sources tried: `pending`
- SG focus: `pending`
- CN sources tried: `pending`
- CN focus: `pending`
- serious survivors created/updated: `pending`
- blockers/errors: `none recorded`
- next rotation: `establish on first post-schema discovery run`

## Receipt contract

After each scheduled discovery run, replace **Current receipt** with only:

- completed run time in MYT;
- SG source families actually tried + short focus (employers/role keywords);
- CN source families actually tried + short focus;
- serious-survivor Issue numbers created/updated, or `none`;
- concrete search/access failures, if any;
- next source/keyword rotation to avoid repeating the same search.

A zero-survivor run is valid if both primary markets were actually searched/rotated. Do not store raw rejected candidates, long search logs, dashboards, scores, or duplicate policy here. Detailed rules remain in `RULES.md`.
