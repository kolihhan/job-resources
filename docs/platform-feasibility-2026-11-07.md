# Public hiring-platform feasibility — 2026-11-07

## Verdict

**GitHub Actions is NOT a universal native scraper for SG/MY/CN hiring platforms.** A strict read-only GitHub-hosted, two-page HTML benchmark evaluated 12 market/platform entry points. No source passed the final gate for query-relevant, meaningfully distinct page-2 job identities. A successful HTTP status is not job coverage.

Evidence:
- Initial test: https://github.com/kolihhan/job-resources/actions/runs/42349864977
- Tightened independent rerun: https://github.com/kolihhan/job-resources/actions/runs/42350155908
- Code: `scripts/probe_platform_feasibility.py`; regression tests: `tests/test_platform_feasibility.py`
- Source: downloadable `platform-feasibility` artifact from the rerun, containing the exact HTTP/page titles, source-local job-detail paths, uniqueness and challenge state.

| Market | Platform | Observed runner behavior | Coverage route for now |
| --- | --- | --- | --- |
| SG | LinkedIn | HTTP 200, challenge HTML; 0 proven job IDs | indexed exact-role discovery -> official JD/route |
| SG | JobStreet | 403 | indexed exact-role discovery -> official JD/route |
| SG | Indeed | 403 | indexed exact-role discovery -> official JD/route |
| SG | MyCareersFuture | HTTP 200 JS/search shell; 0 proven IDs | indexed MCF exact-role JDs for discovery; employer application route for foreign applicant |
| MY | LinkedIn | HTTP 200 challenge HTML; 0 proven IDs | indexed exact-role discovery -> official JD/route |
| MY | JobStreet | 403 | indexed exact-role discovery -> official JD/route |
| MY | Indeed | 403 | indexed exact-role discovery -> official JD/route |
| MY | Hiredly | HTML search page loaded; 0 provable job-detail IDs | indexed Hiredly exact-role pages; probe full JD and official company alternative |
| CN | BOSS直聘 | HTTP 200, 0 proven job-detail IDs in returned search HTML | indexed exact-role/official owner -> preserve recruiter route signal |
| CN | 牛客 | HTTP 200 challenge HTML, 0 proven IDs | indexed exact-role job pages with IDs; verify eligibility and chat/application route |
| CN | 智联 | HTTP 200, 20 source-local job-detail links but query title was generic and next page repeated the same 20 IDs in the independent rerun | **NOT verified**; do not credit page-two coverage or `大模型` search to this page |
| CN | 51job | No proven role IDs; response can vary by run | indexed detail discovery and official source checks |

### Method and limits

- Each native URL got a bounded first/second page probe when accessible, with exact anchored job URL paths extracted from returned HTML. No login, cookie storage, proxy, CAPTCHA bypass, or write actions.
- An HTML 200 plus an advertisement of thousands of jobs is **not** evidence of job identities.
- Job IDs from two pages count as real search depth only if the returned page titles support the query topic and the second page adds meaningful new IDs (>=25% page-two novelty or a distinct complete small page).
- JobStreet and Indeed currently block this specific GitHub-hosted runner. This does **not** establish universal platform unavailability: a separate indexed web search can still surface concrete JD pages.
- CN Liepin is covered by a **different** public API adapter and has demonstrated 2 pages / 162 exact IDs in one source run; many further pages remain unconsumed, and access can fail by city/query/volume. See `docs/source-feasibility-pilot-2026-11-07.md`.
- Results are a momentary source-access benchmark, not proof of permanent blocking, target-role recall, sponsorship eligibility, or end-to-end search completeness.

## Routing architecture (concrete tasks)

1. **PROGRAMMATIC_NATIVE:** Only assign recurring native platform collection to a host/endpoint after source-specific page/query/role-ID proof. Current benchmark validates **none of these 12 HTML search endpoints** for unattended native collection. Use the separately verified Liepin API and official ATS adapters where their specific feeds work. Never generalize an API result to all platforms.
2. **INDEX_DISCOVERY:** For inaccessible native search, use bounded exact-domain queries through an actually available search index (search engine/connector). Record `market`, `platform`, `query_family`, `retrieved_at`, exact job URL or ID, index source and retrieval state. A snippet alone is only a candidate signal, not a verified JD. **GitHub Actions has no authenticated search-index API provisioned here**; do not pretend an Actions job automatically performs this stage.
3. **EXACT_ROLE_VERIFY:** For each plausible indexed candidate, read platform exact-JD page if possible, resolve the canonical company ATS/PI recruiting source, confirm posting recency/live route, apply North-Star/MY TOP/YOE and foreign-hire gates, dedupe all GitHub Issues and application evidence before creating APPLY/CHECK. Preserve platform-exclusive recruiter/chat routes as additional evidence when legitimate.
4. **DURABLE CONSUMPTION:** Store machine-only source query/page/source-ID checkpoint and pending cases under existing discovery-state ownership; do not create a second human opportunity tracker. A new query completed without page or exact-job identity evidence is `PARTIAL_COVERAGE`; blocked/native-inaccessible states are not `DONE`. AI Scout should be a bounded reviewer of saved exact-role observations, not the authority on whether a broad market page was scanned.

## Critical missing implementation

The native feasibility test and CN source-producer handoff now exist. **The automated search-index-to-durable-candidate consumer is not built**. Current ChatGPT/web indexed searches can reveal JobStreet, Indeed, Hiredly, BOSS/Nowcoder exact job pages, but an unattended public search/index adapter or supported browser connector is needed before claiming platform-scale automated discovery. A paid/commercial search API, compliant indexing provider, or permissioned browser environment may be needed; this requires separate feasibility and constraints review.

**Acceptance test for next iteration:** one previously blocked SG/MY platform must produce a batch of *newly discovered exact job identities*, deduped against the entire GitHub Issues history, with verified JD/route evidence and persisted per-candidate outcomes. Number of HTTP 200 responses, search-result headlines or platform-advertised total jobs is not acceptable as a surrogate.
