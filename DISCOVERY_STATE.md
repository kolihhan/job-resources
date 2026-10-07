# Discovery State

## Current receipt

- completed run time: `2026-10-07 23:00 MYT (freshness regression maintenance)`
- SG sources tried: `no new broad sweep; audited the latest SG survivor against source freshness metadata and the new Issue-creation liveness gate`
- SG focus: `verify whether exact-role retrieval was genuinely current rather than merely an older cached/crawled page`
- CN sources tried: `no new broad sweep; audited recent CN CHECK survivors and the user-confirmed closed #149 against source freshness evidence`
- CN focus: `separate explicit current listing-window evidence from cached exact-page retrieval`
- serious survivors created/updated: `none created; #149 手回集团 closed as user-confirmed closed position; #148 同花顺 and #150 Garena removed from active inbox because current liveness could not be independently proven; #146 Kuaishou remains CHECK because its exact listing recorded an explicit validity window covering the current date`
- blockers/errors: `root cause confirmed: the previous rules said to verify “current live status” but did not define acceptable freshness proof, so an exact URL retrieved from an old crawl could be mistaken for a live posting. #149 reproduced the failure: it was promoted from a Zhaopin exact page whose available retrieval metadata was about two months old, then the user opened it and reported “closed position”. RULES.md now hard-gates freshness before Issue creation; cached/indexed exact pages and stale Apply buttons are discovery evidence only.`
- next rotation: `SG/CN: keep the prior employer/keyword rotation, but promote nothing to CHECK/APPLY unless role-level liveness first passes the freshness gate. Prefer explicit listing/closing windows covering today or a freshly rendered exact application/ATS flow. If only cached/indexed content is available and no independent current signal exists, leave the candidate out of GitHub rather than asking the user to discover that it is closed.`
