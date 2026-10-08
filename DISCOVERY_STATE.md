# Discovery State

## FreeHire intake cursor

- cursor: `0`
- public feed: `kolihhan/freehirefetch/feed/events.jsonl`
- public health verified: `2026-10-09 00:58 MYT` — `first_seq=1`, `last_seq=877`; live delta fetched `SG 391 / CN 8`, with `new=0 / changed=0`

## Current receipt

- completed run time: `2026-10-08 20:36 MYT`
- SG lanes tried: `official employer/careers pages, LinkedIn, JobStreet, Indeed, Lever and Ashby across junior backend/full-stack, applied AI, Agent infrastructure, enterprise workflow, fintech, retail technology, healthtech and industrial/product engineering`
- SG coverage: `23 candidates / 18 employers / 6 source families / 9 deep-verified`
- CN lanes tried: `official employer and university campus pages, 牛客, 智联招聘, 猎聘, BOSS直聘, 51job and LinkedIn across explicit 2026/往届 backend, AI application, Agent, full-stack, financial-technology and industrial software`
- CN coverage: `15 candidates / 11 employers / 7 source families / 4 deep-verified`
- Web3 lane tried: `Binance appeared in the SG sweep, but the exact Junior Software Engineer (AI&LLM) requisition was already tracked as WAIT; no genuinely new Web3 survivor remained after dedupe`
- Web3 coverage: `1 candidate / 1 employer / 2 source families / 1 deep-verified`
- serious-survivor Issues created/updated: `#161 金证科技 — 大模型应用开发工程师 was created as CHECK during discovery, then the user reported that the route was not usable and closed it in the same 20 MYT window. It is now BLOCKED and no live serious survivor remains from this receipt.`
- concrete filters / regressions exercised: `SG: AgentForger was rejected because the JD explicitly says no visa sponsorship; A1 listings were closed; Pave Bank was suppressed by a prior same-role rejection; Binance was an exact prior application; Simular was suppressed by recent same-employer/near-role-family application history; Maxify/Sunnystep was suppressed after both-Gmail dedupe recovered the prior application, prototype test and follow-up; FairPrice was senior/executive-leaning; Rakuten required 5+ years; Activate's current official careers page no longer listed A26300. CN: 智识神工 showed 已结束; 上海人工智能实验室 was suppressed by closed/blocked same-employer history; 中城交 was suppressed by a prior near-identical Agent application to the same employer; 携程/Shopee/PDD results were 2027-only or incompatible; Pudu's application window had expired; intermediary or unclear-company listings did not survive company-quality and route checks. #161 was the only genuinely new serious survivor.`
- concrete access/write issues: `One targeted Gmail query was transiently rate-limited; a narrower retry succeeded. The university/platform Apply action for #161 could not render the final exact-role candidate form, and the user later confirmed the route was not usable; #161 was normalized to BLOCKED. GitHub Issue and receipt writes were read back. No application or outreach action was taken.`
- next rotation: `SG: rotate to new direct product, healthtech, industrial and B2B SaaS employers with junior-friendly roles and employer-controlled forms; avoid rechecking Pave, Simular, Maxify/Sunnystep, Binance, AgentForger, A1, FairPrice, Activate and Rakuten unless new lifecycle evidence arrives. CN: rotate to new Shanghai/Shenzhen product employers with explicit 2026/往届 eligibility and official/platform-native routes; avoid 上海人工智能实验室, 中城交, 智识神工, 金证科技 and 2027-only campus families. Never submit without explicit authorization.`
