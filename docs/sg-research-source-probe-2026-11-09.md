# Singapore academic research official-source pilot — 2026-11-09

## Verified action

- Workflow: .github/workflows/sg-research-portal-probe.yml, daily 10:47 MYT, read-only.
- Source parser: scripts/probe_sg_research_portals.py; tests: tests/test_probe_sg_research_portals.py.
- Live first-party probe: https://github.com/kolihhan/job-resources/actions/runs/42599578398
- No new GitHub Issues, recruiter contact, application or canonical candidate queue records are created by this workflow. Its evidence is a short-lived GitHub Actions artifact.

## Actual GitHub-hosted source result

| First-party portal | Identifiable list job links | Employer req IDs and Apply control in actual detail | Assessment |
|---|---:|---:|---|
| SUTD Research | 9 | 9 | Bounded category list had explicit page 1 of 1; technically readable |
| NUS Research / SuccessFactors | 0 | 0 | UNDERCOVERED: official HTML listing was a JS shell, not evidence of no vacancies |
| A*STAR Agent search | 0 | 0 | UNDERCOVERED: no source job identities extracted |
| A*STAR LLM search | 0 | 0 | UNDERCOVERED: no source job identities extracted |

The source tool also guards against cross-host job links, hidden script "Apply" strings and mismatched/missing requisition details. Successfully reading job detail does not establish full-JD completeness, applicant eligibility, or candidate fit.

## Decision

**Keep the SUTD source probe and its real daily source receipt; do not auto-promote its nine mixed-discipline research jobs.** Each qualified exact role still needs substantive LLM/NLP/Agent fit, requirements, work pass, contract/term, current route and all-history dedupe under RULES.md.

**Do not claim NUS or A*STAR breadth.** Their exact official roles may still be available through individually indexed/verified employer pages, but the tested native HTML list did not provide a machine-readable discovery stream in this host. Next source research should seek the correct official listing/offset API or a permitted indexed query bridge, demonstrate page depth and exact IDs, and only then connect that source to the existing SG queue. Re-running the same blocked HTML with more scheduling is not a coverage improvement.

The test above is a bounded source-access check, not a market-recall test or a verified new APPLY count.
