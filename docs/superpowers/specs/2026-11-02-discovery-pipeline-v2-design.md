# Discovery Pipeline v2 Architecture Design

## Goal

Move bulk discovery, normalization, cross-source dedupe and conservative machine filtering out of the hourly ChatGPT scouts so the scouts spend their reasoning budget on only plausible, previously unseen candidates that require JD/eligibility/liveness/work-auth/Gmail verification.

The target flow is:

`source adapters -> normalized observations -> cross-source role identity -> conservative machine filter -> lossless candidate feed -> private known-role dedupe -> hourly reasoning scout -> APPLY/CHECK Issue`

GitHub Issues remain the only live human opportunity state.

## Why the current path is inefficient

Current FreeHire ingestion is healthy as a public firehose, but the downstream path has four structural costs:

1. `freehirefetch.job_identity()` prefers FreeHire `public_slug`, so identity is source-specific rather than a canonical cross-source role identity.
2. `feed/candidates.json` is intentionally capped to 10 candidates per market, so it is a fast snapshot rather than a lossless reasoning queue.
3. Hourly scouts recover raw FreeHire sequence events themselves, including large volumes of irrelevant/duplicate records.
4. Contiguous raw-sequence recovery can stall behind one unresolved relevant event even when thousands of later events are independently processable.

There is also one recall risk: the current candidate snapshot drops explicit non-permanent employment before downstream review, while `job-resources` deliberately permits fixed-term research through `RESEARCH_EXCEPTION`. The public machine layer must not erase that path.

## Architectural boundary

### Layer A — public collection and global dedupe (`kolihhan/freehirefetch`)

Owns:

- FreeHire API ingestion;
- later ATS/source adapters;
- source-specific pagination/cursors;
- normalization into one observation schema;
- canonical cross-source identity extraction;
- exact global dedupe across observations;
- content-change detection;
- conservative generic technical filtering/flagging;
- an uncapped, paged, append-only candidate event feed;
- ingestion/filter metrics.

Does not own:

- the user's GitHub Issue history;
- Gmail/application history;
- candidate profile/private resume facts;
- APPLY/CHECK/SKIP decisions;
- employer contact/application actions.

`freehirefetch` stays public and non-personal.

### Layer B — private known-role index (`kolihhan/job-resources`)

Owns a derived machine index generated from all GitHub Issues, open and closed. It exists only to make exact historical dedupe cheap before expensive reasoning.

It may contain:

- Issue number;
- strong canonical role keys;
- source listing aliases/IDs;
- weak suspected-duplicate fingerprints;
- generation metadata.

It must not become a second live opportunity tracker. Issue state remains canonical.

Do not copy this private index into the public `freehirefetch` repository. If `freehirefetch` is ever made private, this boundary may be revisited, but the default design keeps personal search history out of the collector.

### Layer C — hourly reasoning scouts

Each SG/CN/MY scout consumes only new candidate events after its candidate cursor, checks them against the private known-role index, and spends expensive work only on plausible unseen survivors.

The scout owns:

- exact final Issue-history read before any Issue creation;
- candidate-specific content fit under `PROFILE.md`/`RULES.md`;
- full employer-authored JD/liveness verification;
- cohort/degree/YOE/stack/employment checks;
- SG sponsorship / CN foreign-hire verification where required;
- targeted Gmail dedupe;
- exact application-route verification;
- creation/readback of a new APPLY/CHECK Issue;
- bounded retry receipts for transient verification failures;
- scout metrics.

A transient blocker is moved to bounded retry state; it must not block later independent candidate events.

## Canonical data model

### Observation

One source's representation of a job.

Required normalized fields:

- `source`
- `source_record_id`
- `source_url`
- `market`
- `employer_name_raw`
- `employer_key`
- `title_raw`
- `title_key`
- `location_raw`
- `posted_at`
- `description_text`
- `employment_type_raw`
- `employer_requisition_id` when proven employer/ATS-issued
- `canonical_role_url` when employer-controlled
- `ats_type` / `ats_tenant` when known
- `source_payload_fingerprint`

Source/board IDs are provenance. They are not automatically global role IDs.

### Role identity

Strong identity, in order:

1. `req:<employer_key>:<employer_requisition_id>` when the ID is proven employer/ATS-issued and stable;
2. `url:<normalized employer-controlled exact-role URL>`;
3. otherwise a source-local identity only until stronger evidence appears.

Weak fingerprint:

`normalized employer | normalized title | normalized location`

The weak fingerprint is **suspected duplicate only**. It must never silently merge/suppress a role by itself.

When a later official observation supplies a stronger key, existing source aliases may be attached to the canonical role key.

### Candidate event

A candidate event is emitted only after global dedupe and generic machine filtering.

Required fields:

- monotonic `candidate_seq`;
- `role_key`;
- `event_kind` = `NEW | CHANGED`;
- `market`;
- compact merged source observations/provenance;
- company/title/location;
- best canonical/source URL;
- technical signal list;
- machine flags;
- extracted hints (YOE/degree/cohort/employment/visa) with confidence/source;
- short JD excerpt;
- material content fingerprint.

Candidate events are transport, not opportunity state.

## Dedupe rules

### Global collector dedupe

Safe automatic collapse:

- same strong requisition key;
- same normalized employer-controlled exact-role URL;
- known source aliases already attached to the same strong role key.

Never auto-collapse solely from:

- same title/company/location;
- semantic title similarity;
- corporate-group ownership;
- board listing ID from different sources.

Company aliases must be explicit/verified. Do not automatically merge related legal employers (for example parent/subsidiary brands) merely because they share a group.

### Private historical dedupe

`job-resources` builds a `known-role-index` from all Issues.

Index entries may have several aliases:

- employer requisition keys;
- normalized canonical employer URLs;
- platform IDs (LinkedIn/MCF/BOSS/etc.) as source-local aliases;
- weak fingerprint for suspicion only.

The candidate may be cheaply suppressed only on a strong key/alias match. A weak match must remain inspectable or be confirmed by one cheap exact-role comparison.

Before creating a new Issue, the scout still performs the existing exact GitHub Issue-history search/readback gate. The derived index accelerates work; it never replaces the canonical final gate.

## Filtering philosophy

The machine layer optimizes for **high-recall conservative rejection**, not final fit classification.

Rule:

> Hard-drop only high-confidence negatives. Everything uncertain becomes a flag for the reasoning scout.

### Generic public hard drops

Safe examples:

- explicit Staff / Principal / Director / Manager / Head / Lead title;
- internship / trainee title;
- clearly non-engineering/non-research role outside the collector's configured technical scope;
- malformed/closed source record when the source itself proves closure.

Do not hard-drop from FreeHire enrichment alone. Enrichment fields remain hints.

### Preserve / flag instead of drop

- `Senior` title;
- 3+ or 4+ YOE hints;
- generic Software/Backend title with material LLM/Agent/RAG/retrieval/NLP/evaluation JD signals;
- research roles with fixed-term/contract wording;
- degree/cohort hints that require campaign-page verification;
- sponsorship/work-auth hints without exact employer evidence.

### Research exception safety

Explicit fixed-term/contract ordinary engineering may be low priority, but research/research-engineering/RA/RO/RE observations must survive the public filter when their technical content is plausible. The downstream private scout applies `RULES.md` section 5.

### Technical signal coverage

The signal extractor should cover at least:

- LLM / GenAI;
- Agent / tool use / planning / memory / MCP / coding agent;
- RAG / retrieval / reranking / semantic search / embeddings;
- NLP / language models / dialogue / text understanding;
- knowledge graph / knowledge-enhanced methods;
- evaluation / benchmarking / reliability;
- fine-tuning / SFT / LoRA / post-training;
- search/ranking/recommendation;
- AI/ML platform/inference/model serving;
- PyTorch/Transformers/model training when material.

Scores are ordering/diagnostic hints only. No single score decides APPLY/CHECK.

## Lossless candidate feed

Replace the capped `feed/candidates.json` as the downstream contract with paged candidate events, for example:

- `feed/triage/index.json`
- `feed/triage/pages/000001-000100.jsonl`

`feed/candidates.json` may remain as a human/debug snapshot but is not authoritative.

Requirements:

- no 10-per-market loss cap;
- monotonic `candidate_seq` independent from raw FreeHire event seq;
- market field on every event;
- paged/small-range retrieval compatible with connector limits;
- retained long enough that hourly scouts cannot silently fall behind;
- health metadata exposes first/last candidate sequence and per-market emitted counts.

## Retry semantics

Candidate sequence processing is independent. A transient failure must not stall the global cursor.

For a candidate that cannot be fully verified:

1. persist a bounded retry receipt containing `role_key`, `candidate_seq`, reason code, attempt count, and next eligible retry time/run;
2. advance the normal candidate cursor;
3. revisit retry receipts separately;
4. remove the receipt after terminal rejection, successful Issue handoff, exact-history duplicate, or retry expiry policy.

Retry receipts are machine-efficiency state, not a human opportunity tracker.

A candidate with enough proven liveness and exactly one material unresolved fact may instead become a normal CHECK Issue under existing rules.

## Source adapter strategy

Do not add every ATS at once. Stabilize identity/feed/scheduler semantics using FreeHire first, then add adapters behind the same `Observation` contract.

Recommended order:

1. Greenhouse
2. Lever
3. Ashby
4. SmartRecruiters
5. Workday CXS (tenant/site-specific and more complex)
6. selected public CN ATS surfaces such as Moka / Feishu Hire / Beisen only where a stable unauthenticated contract is verified

LinkedIn, JobStreet, Indeed, BOSS, 牛客 and similar job boards are not equivalent to ATS APIs. Do not make brittle authenticated scraping a core dependency. Keep them as scheduler/platform gap sources until a reliable permitted adapter exists.

## Cold start / migration

1. Build the private known-role index from all current + closed `job-resources` Issues.
2. Replay the existing FreeHire retained event history through identity-v2 + generic filtering to generate the new candidate feed.
3. During scout consumption, subtract strong matches using the private known-role index.
4. Process only unseen candidate events with the expensive rules pipeline.
5. Run old raw-sequence recovery and new candidate-feed consumption in shadow long enough to prove the new feed does not lose serious survivors.
6. After acceptance, retire `docs/freehire-gap-recovery.md` and per-market raw FreeHire sequence obligations from scout prompts.

The raw public event feed may remain for audit/rebuild purposes even after scouts stop consuming it directly.

## Metrics

### Collector metrics

Per run/source/market:

- fetched observations;
- normalized observations;
- exact cross-source merges;
- weak duplicate suspicions;
- hard drops by reason;
- flagged candidates by reason;
- candidate events emitted;
- source errors/latency;
- first/last candidate sequence.

### Scout metrics

Per market/hour:

- candidate events read;
- strong known-history duplicates skipped;
- weak duplicate suspicions checked;
- cheap policy rejects;
- full JD reads;
- liveness/eligibility verified;
- retry receipts created/resolved;
- APPLY/CHECK Issues created/read back.

This replaces raw FreeHire sequence advancement as the meaningful efficiency metric after cutover.

## Invariants

- GitHub Issues remain the only live opportunity state.
- No application/contact without explicit authorization.
- Public collector contains no personal history/profile/Gmail data.
- Strong exact identity may suppress; weak fingerprint may not.
- Unknown/ambiguous evidence is not converted into a hard negative merely for throughput.
- Fixed-term research is preserved for downstream `RESEARCH_EXCEPTION` review.
- A transient candidate failure cannot block later independent candidates.
- Scheduler final Issue creation always performs canonical Issue-history dedupe/readback.
- Source adapters are replaceable; downstream logic depends on the normalized observation/candidate contracts, not source-specific payloads.

## Success criteria

The redesign is accepted when all are true:

1. historical replay produces a lossless candidate feed with no 10-per-market cap;
2. a known job from `job-resources` is skipped through a strong private identity match without full-JD reasoning;
3. the same role observed through two sources collapses only when a strong identity proves equivalence;
4. a same-title/company/location pair without strong identity is not silently merged;
5. a fixed-term research candidate reaches the scout rather than being machine-dropped;
6. one deliberately broken/unreadable candidate is placed into retry while later candidate sequences continue;
7. the hourly scouts no longer need raw FreeHire event-gap recovery;
8. metrics show the funnel from observations -> global candidates -> historical dedupe -> JD verification -> APPLY/CHECK.
