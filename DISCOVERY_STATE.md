# Discovery State

## Current receipt

- completed run time: `2026-10-08 00:15 MYT (consolidation smoke test)`
- SG lanes tried: `official/company careers plus current LinkedIn/JobStreet/Indeed-style discovery; graduate/junior SWE, backend, full-stack, platform and product-engineering lanes across product/fintech/enterprise employers`
- CN lanes tried: `牛客 exact roles plus current 智联/社会招聘-style discovery; 2026/0-3 year backend, AI application/full-stack, Agent and search/retrieval lanes across multiple product employers`
- Web3 lane tried: `current CryptoJobsList feed plus independent role/company verification for remote PT backend/full-stack/infrastructure-style work`
- serious survivors created/updated: `#156 Chainlabs — Fullstack Developer (Part-time) — Remote — CHECK; current liveness proven, final exact application route remains the one blocker`
- concrete filters / regressions exercised: `many CN exact pages were explicitly 已结束 and stayed raw; SG citizenship/current-work-right/seniority blockers were filtered; 北森 J14527 was suppressed by existing #117 before deep research; Pave Junior SWE was suppressed by #66 rejection history; Huawei AI-application-family and Autodesk same-family SWE history were treated as early dedupe, not fresh leads; a high-fit Zhaopin AI/full-stack candidate with insufficient current role-level liveness evidence stayed raw rather than becoming CHECK`
- concrete access/write issues: `dedicated Chainlabs-only GitHub search retries timed out; both Gmail targeted searches were clean. Chainlabs create_issue calls returned timeout responses, so no blind retry was trusted; recent-Issue readback confirmed exactly one resulting Issue, #156.`
- next rotation: `SG: continue beyond already-covered Autodesk/Pave/Palantir/Exa/ST Engineering with fresh product/backend/platform roles in new fintech, enterprise, cloud/data and B2B SaaS employers. CN: emphasize current social-hire / 0-3 year employer-controlled or platform listings beyond Huawei/Kuaishou/北森, especially Shanghai/Shenzhen/Beijing backend, AI-application and search/retrieval roles with provable current liveness. Web3: first resolve #156 final route; then rotate to a new backend/platform/data/AI×Web3 employer rather than repeating Chainlabs.`
