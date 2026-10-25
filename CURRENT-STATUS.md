# BuildMind current status

Updated 26 October 2026 (previous update 25 October 2026). This supersedes the October 19 cost-only priority summary; its original is preserved in docs/history.

|Area|Recorded state|
|-|-|
|Name and product intent|BuildMind; automatic residential concept generation and iterative editing|
|Rules policy|Sri Lankan regulations only; global dimensional components permitted|
|Team|Seven research areas; user selected Member 3|
|Prototype|Visual 2D/3D browser demonstration, template alternatives, generic components and limited checks|
|Production architecture|Proposed Angular, FastAPI, PostgreSQL/pgvector, Shapely, OR Tools, Three.js|
|Integrated RAG|Pending evidence-filtered pipeline, citations and abstention acceptance|
|Automatic layout solver/scoring|Required; not integrated in the visual prototype|
|Regulatory dataset|Sources collected; exact locality/version/applicability review incomplete|
|Climate|Existing four-month one-station dataset; reviewed guidance/API integration incomplete|
|Component catalogue|Illustrative assets exist; source-linked dimension/clearance verification needed|
|BOQ and cost|Extensive source research; measurement mapping and integrated reviewed computation incomplete|
|BRD|22-page version 1.1 delivered 24 October; proposed requirements, approvals pending|
|Room dimensions (Member 3)|Consolidation and provenance audit done 26 October 2026: 262 rule values from 12 sheets in 9 workbooks, 61 comparison keys, 0 numeric conflicts between versions. Origin files state text verification for 115 values; applicability is PENDING on all 262; no reviewer is recorded; no comparison against the Gazette PDF has been made. See [audit report](BuildMind-Data/BuildMind-Data/datasets/03_room_dimensions/consolidated/member3_audit_report.md)|
|Public/private repository split|User decision 26 October 2026: BuildMind-Data-Private must be private (done); the public repository should hold handoff documents, summaries, schemas, metadata and publishable derived data only. Private backups of the flagged third-party/unverified-rights sources are recorded in `knowledge/handoff/SOURCE_REGISTER.csv` (29 rows, `rights_status` UNVERIFIED). The owner has pushed a public cleanup commit that stops tracking those sources. Git history has not been rewritten, so the files remain in history, forks and existing clones; a rewrite needs a separate decision. `BuildMind_AI_Dataset_v1 (1).zip` is on hold (no private backup)|
|Overall completion percentage|Not established by an audited denominator|

See [discussion topics](docs/discussion-record/README.md), [dataset evidence](docs/discussion-record/DATASETS-AND-EVIDENCE.md), [prototype limitations](docs/discussion-record/PROTOTYPE-AND-EXPERIMENTS.md), and [evaluation backlog](docs/discussion-record/OPEN-WORK-AND-EVALUATION.md).

## Do not overstate

"Text verified per origin" means a Member 3 workbook says it transcribed the 2021 Gazette; it is not independent verification and not current applicability. Consolidated rows are candidate regulation records with `applicability_status = PENDING` until the Gazette PDF, later amendments, UDA-declared jurisdiction, the local development plan and a qualified reviewer are checked.


Source files are not cleaned datasets; clean rows are not locally applicable regulations; a renderer is not a solver; mirrored plans are not independently optimised alternatives; a preliminary estimate is not a professional quotation. Missing attachments and original dataset bytes are not asserted archived by this update.

