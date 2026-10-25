# Architecture and AI responsibilities

## RAG is an evidence service

The user asked whether to start RAG, how to train the collected data, how an agent would respond and whether plans could be generated directly. The agreed distinction is: source documents feed retrieval and reviewed rule extraction; geometry and layout generation require deterministic code and solving. Do not train a foundation model merely because PDFs have been collected. A useful pilot RAG can start with a small eligible corpus while further extraction continues, but its answers must abstain outside that coverage.

An agent response should state the understood requirements, ask for essential missing facts, cite applicable evidence, call the solver and validators, explain candidate results and propose reviewable edits. It must not produce invented room minima, rates or engineering quantities. An LLM cannot certify that a building can be constructed merely from land dimensions.

## Twelve engines

| Engine | Responsibility |
| --- | --- |
| Geometry | Exact coordinates, dimensions, polygons, shared walls, units and tolerances |
| Constraint | Plot envelope, applicable room bounds, hard constraints and soft preferences |
| Layout generator and solver | Search arrangements, preserve the brief and return truthful search status |
| Scoring | Rank eligible candidates using disclosed weighted soft criteria |
| Circulation validator | Entrance reachability, connected rooms, access paths and clearance |
| Opening validator | Wall hosting, offsets, door swings, window positions and source-linked conditions |
| Orientation | North and road context, reviewed light/ventilation/climate recommendations |
| BOQ | Reviewed measurement formulas, units, deductions and supported work items |
| Cost | Dated local rates, inclusions, exclusions and unpriced quantities |
| 2D renderer | Dimensioned CAD-style plan and edit controls |
| 3D renderer | Linked parametric model and supported edits |
| Validation report | Revision-specific results, evidence, pending checks and assumptions |

The original list had ten engines. Layout generation and scoring were added because validators alone do not create plans. Assign implementation owners explicitly rather than assuming seven dataset owners cover all twelve engines.

## Feasibility and scoring semantics

Keep candidate found, proven infeasible within the implemented constraint model, incomplete search/timeout, invalid model and insufficient information separate. A timeout does not prove impossibility. Even a feasible candidate does not establish soil suitability, utilities, structural safety or local approval. Missing statutory coverage remains pending.

Compare only candidates that meet implemented hard constraints. Record scoring criteria, weights, rule releases and score breakdown. Do not label an attractive rendering or arbitrary percentage as regulatory accuracy. Optional Vastu/cultural criteria are soft preferences by default.

## Shared model and edits

Stable IDs for Project, Brief, Plot, Storey, Room, Wall, Opening, ComponentInstance, Rule, Evidence, ClimateContext, QuantityItem, RateItem, ValidationResult and Revision. Canonical units are integer millimetres in the proposed backend; render units are independent. OR Tools CP SAT requires an integer formulation; choose solver discretisation deliberately and validate resulting geometry.

A validated edit transaction changes the canonical model, rehosts openings, updates views and invalidates dependent validation/quantity/cost results. Preserve shared-wall relationships; dragging independent room rectangles is insufficient. Include owner checks, base revision, conflict handling, undo and safe recovery. An LLM emits allowlisted structured operations, not executable scripts. Source text cannot invoke tools or override system instructions.

## Proposed implementation stack

| Layer | Proposed baseline | Status |
| --- | --- | --- |
| Frontend | Angular and TypeScript, CSS | Product direction; current prototype is plain JavaScript |
| 2D | SVG/Canvas with geometry interaction; Konva considered | Final library not pinned |
| 3D | Three.js and OrbitControls | Current prototype uses Three.js |
| API | FastAPI with Pydantic | Proposed backend |
| Geometry | Shapely | Proposed |
| Solver | OR Tools CP SAT | Proposed |
| Database and retrieval | PostgreSQL with pgvector | Submission BRD baseline |
| AI | One interchangeable LLM and embedding provider adapter | Provider and model unconfirmed |
| Documents | PDF extraction, optional OCR, evidence/page mapping | Pipeline not fully integrated |
| Files/jobs | File/object store and bounded background jobs | Proposed |
| QA | pytest and browser interaction tests, Git and CI | Acceptance work pending |

An alternative uploaded BRD proposed PostgreSQL/PostGIS plus Chroma. Do not run both vector stores by accident. pgvector is the present submitted recommendation; PostGIS needs demonstrated spatial requirements before inclusion. Versions, production hosting and provider choices need confirmation. Blender/MCP is optional for assets/offline rendering; it is not necessary for every browser edit. n8n is an earlier orchestration experiment.

## Integrations and API concepts

Candidate interfaces discussed: `/api/projects`, `/api/generate-plan`, `/api/chat`, `/api/estimate-budget`, `/api/projects/{id}`. These are design proposals, not evidence of deployed endpoints. Generation should receive project/revision IDs, confirmed brief and rule release, and return status, candidates, conflicts and evidence. Editing must use IDs, allowed operations and an expected base revision.

Weather integration supplies coordinates, period, timezone, temperature, rainfall, humidity and wind where available. Distinguish current weather, forecast and long-term climate. Provider failures preserve the plan and mark climate pending. Construction-rate ingestion is a curated import and review process, not an assumed live government API.

## Capacity and spending

The user asked about 100 users/month and API limits. There is no fixed supported user count until model choice, tokens, calls per design, retries, concurrency, hosting and budget are measured. Use per-project budgets, caching and cancellation. No live OpenAI key configuration or provider entitlement is established by this knowledge record; do not commit keys.
