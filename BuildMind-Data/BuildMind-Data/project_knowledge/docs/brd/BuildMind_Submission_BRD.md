# BuildMind Business Requirements Document

AI assisted residential planning for Sri Lanka

This document defines the business scope, users, product behaviour, data requirements and delivery criteria for BuildMind. It describes the intended system from a residential brief through feasibility screening, editable plans, furnishing and preliminary quantities and costs.

The proposed university release is a controlled residential concept design workflow. Its outputs support discussion and professional review. They do not establish building approval, structural safety or readiness for construction.

### Document control

| Field | Value |
| --- | --- |
| Document identifier | BM BRD 001 |
| Version and date | 1.1  /  24 October 2026 |
| Status | Submission edition for academic review |
| Prepared for | BuildMind project team and university supervisor |
| Prepared by | BuildMind Project Team |
| Project team | Seven member project team |
| Delivery planning window | Eight weeks proposed within the stated two month project period |
| Approval status | No signatures or external professional endorsements recorded |

 

### How to use this document

Agree the release boundaries and open decisions before implementation. Convert the numbered requirements into implementation tasks and tests. Maintain each rule, plan, asset and rate with its provenance so the team can distinguish verified evidence from assumptions.

Planning baseline: the BuildMind project brief, product requirements and prototype review. Named technical references were checked on 24 October 2026. The source document collection has not been reaudited as part of preparing this BRD.

## Document map and present status

| Section | Subject | Page |
| --- | --- | --- |
| 1 | Business problem and objectives | 3 |
| 2 | Release scope | 4 |
| 3 | Proposed unique selling points | 5 |
| 4 | Stakeholders and responsibilities | 6 |
| 5 | Business workflow | 7 |
| 6 | Requirements for project intake and generation | 8 |
| 7 | Requirements for editing and openings | 9 |
| 8 | Requirements for furnishing and climate | 10 |
| 9 | Requirements for knowledge costs and outputs | 11 |
| 10 | Decision rules and engine responsibilities | 12 |
| 11 | Data and knowledge governance | 13 |
| 12 | Nonfunctional requirements | 14 |
| 13 | Architecture and technical stack | 15 |
| 14 | Integrations and interfaces | 16 |
| 15 | User experience and business use cases | 17 |
| 16 | Acceptance and evaluation | 18 |
| 17 | Delivery plan and team ownership | 19 |
| 18 | Risks and budget | 20 |
| 19 | Assumptions decisions and approval | 21 |
| 20 | References and glossary | 22 |

 

### Implementation status

The current browser prototype demonstrates template layouts, dimension editing, 2D and 3D views, generic components, basic checks and keyword based commands. Source backed RAG, an integrated constraint solver, verified local applicability, live climate analysis and a validated BOQ and cost pipeline remain planned work. Existing prototype behaviour is not evidence that a requirement below has passed acceptance.

R1 means the proposed university MVP. R2 means an extension to the intended product after the MVP, subject to delivery capacity. Future scope means a separate later initiative. All performance and quality figures in this BRD are proposed targets, not measured results.

## Business problem and objectives

### Problem and opportunity

A homeowner can describe rooms and preferences without knowing whether they fit a plot, how access should work or what a change does to the rest of the design. Separate drawings, visualisations and estimates make early revisions difficult to follow. BuildMind will combine a structured brief, explainable checks and linked views in one concept planning workspace.

The first users are Sri Lankan residential clients, architecture students and professionals reviewing early concepts. The product should make design assumptions visible and preserve a clear handoff to an architect, engineer or quantity surveyor.

| ID | Business objective | Proposed success measure |
| --- | --- | --- |
| BO01 | Identify whether a brief has a candidate layout within the supported model. | Every generation result distinguishes feasible candidate, proven infeasible within model, search incomplete and missing inputs. |
| BO02 | Help users revise a concept without losing dimensional consistency. | All defined edit acceptance cases preserve stable IDs and matching 2D and 3D dimensions. |
| BO03 | Provide traceable guidance about selected Sri Lankan requirements. | All supported regulatory statements in the acceptance set link to an eligible source and clause or page; unsupported requests abstain. |
| BO04 | Reduce early concept iteration effort. | Pilot target: median completion time at least 20% below the same task in the agreed baseline workflow, with task quality held constant. |
| BO05 | Expose quantities and preliminary cost assumptions. | Every estimated line shows units, measurement basis, rate source, location, date and exclusions. |
| BO06 | Keep the university delivery manageable. | Deliver the agreed R1 vertical slice in eight weeks; obtain a recorded scope change before expanding it. |

 

### Business value and measurement

Record a baseline before claiming time savings. Pilot with at least five consenting target users if available, use identical briefs, retain task outcomes and report sample size. Do not present an unmeasured accuracy percentage, a dataset count or a successful visual rendering as proof of engineering correctness.

## Release scope

### R1 university MVP

Rectangular plots, one storey, one to three bedrooms, one or two bathrooms and optional one car parking. English interface first; explicit feet and metre display with a shared canonical model.

A structured project brief, location and authority context, road side, north direction, budget preference and a limited set of supported constraints.

Two or three distinct candidate layouts when the solver finds them, a transparent explanation when it cannot, and a comparison based on documented scoring weights.

Editable 2D plans and parametric 3D models, bounded room and object edits, selected natural language edit commands, undo and revision history.

Opening placement, room access checks and generic furniture and bathroom fixtures from a small verified catalogue; revalidation after changes.

A curated Sri Lankan knowledge collection with source citations, one selected pilot jurisdiction, a limited climate demonstration and a reviewed subset of BOQ and rates.

Save and reopen a project, export a concept report and plan data, show assumptions and distinguish pending checks from passed checks.

### R2 intended product extensions

Extend the same workflow to more local authorities, broader component collections, richer conversational edits, more detailed preliminary BOQ items and more climate scenarios. Consider irregular plots, additional floors, complex roofs and richer exchange formats only after geometry, circulation and rule applicability are stable. R2 features require a new estimate and scope approval.

### Future scope

Add Sri Lankan supplier product availability and current furniture, door and fixture prices; procurement and ordering; professional collaboration; automatic interpretation of uploaded plan images; richer BIM interchange; specialised accessibility workflows; energy simulation and optional immersive walkthroughs.

### Explicit exclusions

R1 does not provide structural design, reinforcement or foundation calculations, geotechnical assessment, services engineering, approval submission, a certified cost quotation or construction documentation. Payments, supplier transactions, live collaboration and training a foundation model are outside R1. International building codes will not be substituted for Sri Lankan regulatory requirements.

## Proposed unique selling points

The following are proposed differentiators to demonstrate and evaluate. This BRD does not claim that these features are globally unique or absent from competing products; a separate competitor study is required for those claims.

| USP | Proposed distinction | User value and evidence |
| --- | --- | --- |
| USP01 | Sri Lankan evidence linked to a selected project context. | Explain which source and applicability conditions support a check; show uncertainty when local coverage is incomplete. |
| USP02 | Requirement fit with understandable alternatives. | When a brief is too demanding for the supported model, show which constraints conflict and suggest changes without silently removing requirements. |
| USP03 | One dimensioned model behind 2D, 3D, validation and quantities. | A room change updates every dependent view and flags stale outputs; demonstrate this with an end to end revision test. |
| USP04 | Manual editing and conversational editing in the same workspace. | Users may drag an item or request an equivalent supported edit, with preview, undo and the same validation rules. |
| USP05 | Space aware furnishing after concept review. | Place generic items using verified footprints, swing and clearance constraints, then let users replace and reposition them. |
| USP06 | Explainable climate and preference tradeoffs. | Compare orientation, openings and optional cultural preferences using explicit soft criteria; do not represent a preference as a statutory rule. |

 

### Target users and needs

Homeowners need clear inputs, understandable plan options and safe revision controls. Students need traceable decisions and reproducible evaluation. Architects need editable geometry and a record of assumptions rather than an asserted approval. Quantity surveyors need a quantity basis and a dated rate set they can review.

### Positioning

BuildMind is an AI assisted residential concept planning assistant for Sri Lanka. The initial business offering is a demonstrable design and explanation workflow. Commercial pricing, sales channels and service commitments remain undecided and are not implied by the prototype.

## Stakeholders and responsibilities

| Stakeholder | Interest and responsibility | Decision or access |
| --- | --- | --- |
| Residential user | Provides plot facts and preferences; explores, edits and finalises a personal concept. | Own projects and exports; cannot change shared regulations. |
| Project owner | Maintains scope, priorities, delivery dependencies and the acceptance record. | Approves release scope and changes within the project. |
| University supervisor | Reviews academic objectives, feasibility and evaluation evidence. | Reviews academic acceptance; does not automatically certify construction suitability. |
| Architect or planning reviewer | Reviews selected room, circulation, opening and applicability rules. | Records domain review and identifies missing or conflicting evidence. |
| Civil or structural engineer | Identifies the boundary between concept and structural feasibility. | Provides advisory review; structural design remains excluded. |
| Quantity surveyor | Reviews measurement rules, item mapping and rate interpretation. | Approves the pilot measurement methodology and review status. |
| Dataset curator | Deduplicates sources and manages extraction, units, citations and versions. | Publishes candidate records for review; cannot self label uncertain values as law. |
| Administrator | Manages users, access, eligible knowledge releases and operational settings. | Administrative actions logged; does not edit private designs without authorisation. |
| Development and QA team | Implements the model, services, UI, integrations and evaluation. | Test environments and role appropriate project access. |
| Authorities and data providers | Supply rules, approvals processes, weather, rates or licensed assets. | External dependencies; no partnership or endorsement is assumed. |

 

### Role and ownership boundaries

R1 proposes owner, reviewer and administrator roles. Reviewers receive access only when a project is shared with them. Enforce ownership on every project and export request at the server. A domain review status is scoped to the reviewed record and version; it must not be displayed as general endorsement of BuildMind.

Nominate named people and confirm reviewer availability during week one. The BRD assigns responsibilities, not appointments or signatures.

## Business workflow

| Step | User and system action | Output or decision |
| --- | --- | --- |
| 1 | User supplies plot dimensions, units, location, road side, north angle and desired spaces. | Validated brief with confirmed facts, preferences and missing inputs. |
| 2 | System selects eligible local rules and distinguishes hard constraints from soft preferences. | Rule context with sources and unresolved applicability. |
| 3 | Solver searches for candidate layouts and validators assess implemented constraints. | Candidate set, model scoped infeasibility, incomplete search or insufficient evidence. |
| 4 | User compares candidates, room areas and tradeoffs. | Selected initial concept; requirements are not silently relaxed. |
| 5 | User edits 2D manually or requests a supported conversational change. | A previewed revision, validation results and an undoable change. |
| 6 | The same model produces 3D; user inspects and makes supported parametric edits. | Updated 2D, 3D and affected checks for the same revision. |
| 7 | User confirms the spatial concept and requests furnishing. | Space aware furniture placement and fixture selections; doors and windows were already planned. |
| 8 | User moves, rotates, replaces or deletes items and reviews conflicts. | An adjusted furnished concept with pending issues visible. |
| 9 | System calculates supported quantities and preliminary costs. | Version matched BOQ subset, dated rates, exclusions and assumptions. |
| 10 | User finalises and exports the concept for professional review. | A frozen project revision and review package, not permission to build. |

 

### Iteration and recovery

Any edit returns the affected model to validation. Finalisation does not erase warnings. A changed model invalidates earlier quantities, costs and reports until they are recalculated. Failed API requests, cancelled searches and invalid proposed edits must preserve the last accepted revision.

### Meaning of feasibility

A feasible result means a candidate satisfies the implemented model and its stated assumptions. It is not a statement about soil, structure, title, utility availability, hazards or local approval. Missing statutory evidence produces an unknown or pending check rather than an assumed pass.

## Requirements for project intake and generation

Priority M means required for the agreed R1 release; S means a useful extension. Requirement acceptance must be demonstrated rather than inferred from a screen.

| ID | Business requirement and expected behaviour | Verification | Release |
| --- | --- | --- | --- |
| FR01 | M  Create a named project with an owner, timestamp, unit setting and brief. | Save, reopen and retrieve only the authorised project. | R1 |
| FR02 | M  Capture rectangular plot width and length, north angle, road side, locality and planning authority where known. | Reject invalid dimensions and identify missing authority context. | R1 |
| FR03 | M  Record room counts, requested sizes, parking, budget and optional preferences. | Confirm a structured brief and mark facts versus preferences. | R1 |
| FR04 | M  Convert feet and metres without changing the underlying geometry. | A unit toggle preserves dimensions within the stated tolerance. | R1 |
| FR05 | M  Select an eligible rule release for the project context. | Inapplicable, draft or unresolved rules cannot establish a regulatory pass. | R1 |
| FR06 | M  Calculate usable planning area using applicable rules or explicitly labelled assumptions. | Display the source and basis of each boundary deduction. | R1 |
| FR07 | M  Generate up to three geometrically distinct candidate plans. | No overlap, required rooms present and all implemented hard checks satisfied. | R1 |
| FR08 | M  Report candidate found, model infeasible, timeout or incomplete search, invalid model and missing information separately. | A timed out search is never labelled impossible construction. | R1 |
| FR09 | M  Rank candidates using recorded soft criteria and weights. | Show a score breakdown; retain the same rule release for comparison. | R1 |
| FR10 | M  Suggest requirement adjustments when conflicts are identified. | Explain the affected requirement; apply relaxation only after user agreement. | R1 |

 

The first jurisdiction and allowed room catalogue must be selected before FR05 and FR07 can pass. If statutory coverage is incomplete, a concept may still be explored using labelled assumptions, but its regulatory status remains pending.

## Requirements for editing and openings

| ID | Business requirement and expected behaviour | Verification | Release |
| --- | --- | --- | --- |
| FR11 | M  Render dimensioned 2D rooms, walls, openings, plot boundary, road side and north. | Labels and exported geometry refer to the same model revision. | R1 |
| FR12 | M  Move and resize supported rooms using drag controls and numeric inputs. | Preserve stable IDs; recheck bounds, overlap, access and opening hosts. | R1 |
| FR13 | M  Render parametric 3D from the shared model with orbit, zoom, roof and cutaway controls. | Changing the camera does not change room or object dimensions. | R1 |
| FR14 | M  Support defined 3D edits to object transforms and room dimensions. | A 3D edit updates the source model and matching 2D view; no arbitrary mesh editing is implied. | R1 |
| FR15 | M  Interpret selected conversational edit commands into structured operations. | Ask about ambiguous targets and preview changes affecting multiple spaces. | R1 |
| FR16 | M  Record undo, redo and named project revisions. | Restore the exact prior model, selections and validation status as appropriate. | R1 |
| FR17 | M  Host doors and windows on specific walls with offsets and sizes. | Reject openings outside their host or overlapping invalid wall segments. | R1 |
| FR18 | M  Validate door swings, reachable room access and available circulation paths. | Detect disconnected rooms and obstruction cases using documented geometric criteria. | R1 |
| FR19 | M  Check windows against the applicable rule context and room use. | Display missing or unsuitable openings with a rule reference or guideline label. | R1 |
| FR20 | M  Revalidate affected geometry after each committed edit. | Block hard invalid commits or retain them only as an explicitly invalid draft; never mark them passed. | R1 |

 

Opening markers in the existing prototype do not satisfy FR17 by themselves. R1 requires actual wall hosting and coordinated updates. Movement and resizing must respect shared walls; moving a standalone rectangle is not sufficient for a connected house model.

## Requirements for furnishing and climate

| ID | Business requirement and expected behaviour | Verification | Release |
| --- | --- | --- | --- |
| FR21 | M  Maintain a curated global catalogue of furniture, doors and bathroom fixtures. | Each enabled item has source backed dimensions, unit, footprint and asset rights. | R1 |
| FR22 | M  Place furniture according to room function and usable space after spatial concept review. | Keep required paths, door swings and approved clearances available. | R1 |
| FR23 | M  Let users add, move, rotate, replace and delete catalogue items. | Use catalogue dimensions by default; flag custom resized products as conceptual. | R1 |
| FR24 | M  Distinguish product size, use clearance and installation requirements. | Do not treat manufacturer installation data as Sri Lankan statutory rules. | R1 |
| FR25 | M  Capture location and north for a limited climate demonstration. | Show location, period, units and data source; allow manual climate context if the API fails. | R1 |
| FR26 | M  Apply reviewed orientation and ventilation guidance as soft rules unless a sourced regulation applies. | Explain a recommendation and disclose model resolution and missing evidence. | R1 |
| FR27 | S  Compare alternative opening and shading strategies across a wider climate set. | Use multi year or representative climate data; do not infer climate from today’s forecast. | R2 |
| FR28 | M  Store optional cultural and lifestyle preferences separately. | A preference such as separating a pooja room from a bathroom is user configurable and not labelled law. | R1 |
| FR29 | S  Support richer fixtures, roof configurations and materials. | Each added parametric feature updates the model and relevant quantities through a documented mapping. | R2 |

 

### Furnishing boundary

Generic global products are acceptable for concept design. Current Sri Lankan store availability, furniture prices, delivery charges and purchasing are future scope. The construction cost workflow may still use selected Sri Lankan building rates. No item should be costed twice as a building component and a separately priced furnishing.

## Requirements for knowledge costs and outputs

| ID | Business requirement and expected behaviour | Verification | Release |
| --- | --- | --- | --- |
| FR30 | M  Retrieve eligible passages from the curated knowledge collection. | Filter by document type, locality, date, rule status and access permission. | R1 |
| FR31 | M  Answer supported questions with document, page or clause and source identity. | Abstain or qualify when evidence is absent, contradictory or outside scope. | R1 |
| FR32 | M  Restrict AI edits to validated structured tool operations. | Document text cannot invoke tools, change system rules or execute code. | R1 |
| FR33 | M  Allow curated document ingestion and reviewer publication. | Detect duplicates; retain extraction quality, source version and reviewer status. | R1 |
| FR34 | M  Calculate a reviewed subset of BOQ quantities from the current model. | Show formula, measurement unit, deduction rule and measurement standard reference. | R1 |
| FR35 | M  Map supported quantities to a selected Sri Lankan rate release. | Record district, year, revision, currency, taxes, transport and overhead basis. | R1 |
| FR36 | M  Recalculate estimates after relevant model edits. | Stamp the revision; refuse to present an outdated estimate as current. | R1 |
| FR37 | M  Produce an explainable validation and assumptions report. | Separate pass, fail, pending, not checked and not applicable by requirement. | R1 |
| FR38 | M  Export concept drawings, PDF report and structured JSON. | Include units, scale information where applicable, version and construction limitations. | R1 |
| FR39 | S  Expand the BOQ catalogue and offer additional exchange formats. | Validate every new measurement mapping; preserve source provenance. | R2 |
| FR40 | M  Finalise a revision and reopen it as a new editable revision. | Retain the original finalised record and its evidence snapshot. | R1 |

 

The pilot estimate excludes unmodelled structural, geotechnical, MEP and procurement work unless explicitly entered as a reviewed allowance. RAG can retrieve a rate explanation; deterministic measurement and costing services calculate the numbers.

## Decision rules and engine responsibilities

| Engine | Required responsibility |
| --- | --- |
| Geometry | Coordinates, dimensions, polygons, shared walls, units and tolerances. |
| Constraint | Applicable room bounds, plot envelope and configurable hard and soft constraints. |
| Layout generator and solver | Search feasible arrangements and return a truthful search status. |
| Scoring | Compare only eligible candidates using disclosed weighted preferences. |
| Circulation validator | Check room connectivity, entrance reachability and path clearance. |
| Opening validator | Check wall hosting, offsets, swings and applicable ventilation conditions. |
| Orientation | Combine north, road context and climate guidance without universal directional assumptions. |
| BOQ | Measure supported model elements using a reviewed measurement methodology. |
| Cost | Apply the selected dated rate release and show inclusions and exclusions. |
| 2D renderer | Display dimensioned plan geometry and editing controls. |
| 3D renderer | Display the same parametric model with supported edit operations. |
| Validation report | Aggregate evidence, assumptions and unresolved checks for the current revision. |

 

### Rule classification

Each rule records rule_type, severity, jurisdiction, applicability conditions, unit, effective period, verification status, source, page or clause and reviewer. Regulation, recommended practice, architect guideline, prototype assumption and user preference are different categories. Verified source text and verified local applicability are separate statuses.

### Business decisions

Only applicable verified hard rules may support a regulatory pass. Missing mandatory evidence remains pending. A soft preference cannot override a hard rule.

Use one canonical model. A proposed edit is validated before acceptance; all derived views and quantities identify the resulting revision.

A failed search does not prove the physical site cannot be built on. Describe the supported model and any proved constraint conflict.

Finalising a concept freezes a revision; it does not issue a permit or certify engineering adequacy.

## Data and knowledge governance

| Collection | Minimum useful content | Publication condition |
| --- | --- | --- |
| Planning rules | Authority, zone, setbacks, coverage and conditions. | Original source and pilot applicability reviewed. |
| Room standards | Room use, dimensions, area and conditional minima or recommendations. | No invented Sri Lankan legal minima; label guidelines correctly. |
| Layout rules | Adjacency, separation, access, severity and rationale. | Architect review; observation is distinct from prescription. |
| Climate rules | Climate context, parameter, period, condition and recommended action. | Reviewed transformation from weather to design guidance. |
| Components | Dimensions, footprints, swings, clearances, installation data and asset rights. | Verified catalogue values and licensed or original visual assets. |
| Templates | Geometry, room labels, connectivity, scale, provenance and licence. | Sample geometry audit and local revalidation. |
| BOQ and rates | Measurement method, item mapping and dated local rates. | QS reviewed pilot items; rate basis and exclusions recorded. |
| Test plans | Valid and deliberately invalid geometry with expected outcomes. | Independent holdout cases, review and version tracking. |

 

### RAG preparation and quality

Register sources, compute file hashes, remove duplicates and irrelevant material, extract text and tables, apply OCR where needed, then attach document and page metadata to chunks. Keep tables and conditional rules intact. Review critical numeric passages before indexing. Publish a versioned eligible collection and preserve it with project reports.

RAG retrieves supporting evidence; it does not train new foundation model weights. Structured rules and geometry remain accessible to deterministic services. Evaluate keyword and vector retrieval together, then assess answer support, citation accuracy and appropriate abstention.

### Plan datasets and rights

ResPlan is a candidate source of vector plan examples, not a source of Sri Lankan regulations or approved site plans. Audit duplicates, scale, labels and connectivity before use; keep related plans in one evaluation split. CubiCasa5K supports plan image understanding research and is optional future work. Its noncommercial restriction must be respected [R7, R8]. The current BRD does not certify either dataset record by record.

## Nonfunctional requirements

These are proposed R1 test targets. Record the selected hardware, browser, corpus and workload before measurement. Targets may be revised through the change process, not silently relabelled as achieved.

| ID | Quality requirement | Acceptance target |
| --- | --- | --- |
| NF01 | Dimensional consistency | Canonical values retain at least millimetre precision; unit round trips differ by no more than 1 mm for supported sizes. |
| NF02 | Interactive editing | On the agreed reference PC, 95% of tested committed local edits update visible geometry within 500 ms for the reference model. |
| NF03 | 3D responsiveness | Target at least 30 frames per second during orbit for a model of up to 15 rooms and 50 generic objects on agreed hardware; provide a 2D fallback. |
| NF04 | Generation responsiveness | Use a configurable search budget, initially 60 seconds; display progress, cancellation and truthful timeout status. |
| NF05 | RAG response time | Target 95% of test queries within 15 seconds, excluding clearly reported provider outages; log retrieval and generation latency separately. |
| NF06 | Access control | All defined cross owner access tests fail closed for project, revision, document and export endpoints. |
| NF07 | Data integrity | A failed save or invalid edit preserves the last accepted model. Use atomic revisions and explicit conflict handling. |
| NF08 | Recovery | Proposed pilot recovery point is 24 hours and recovery time is 4 hours; demonstrate one backup restore before assessment. |
| NF09 | Security | Server held API keys, TLS, input limits, rate limits, safe file parsing and sanitised display; no execution of uploaded pickle or document instructions. |
| NF10 | Privacy | Collect only necessary plot and account data; restrict external AI context; support export and deletion with a documented retention policy. |
| NF11 | Accessibility and usability | Keyboard operable forms, visible focus, labelled controls, numeric alternatives to dragging and warnings that do not rely on colour alone. |
| NF12 | Browser compatibility | Test the agreed Chrome and Edge releases on Windows; report WebGL fallback and unsupported devices explicitly. |
| NF13 | Maintainability and testing | Versioned schemas, reviewed changes, geometry and validator tests, API tests and reproducible data releases. |
| NF14 | Traceability and observability | Every check, estimate and AI edit records revision, rules, source release, operation status and errors without leaking secrets. |
| NF15 | Pilot capacity | Exercise 10 simultaneous active sessions and 100 distinct demo projects; this is a test workload, not a monthly user or paid API entitlement. |

 

## Architecture and technical stack

Use a modular monolith for the first integrated release. The browser edits a shared project model; backend modules retrieve evidence, search layouts, validate changes and calculate outputs. Keep the layout solver separate from the LLM decision loop. Add distributed services only when measured workload or ownership requires them.

| Layer | Proposed choice | Reason and boundary |
| --- | --- | --- |
| Frontend | Angular with TypeScript and CSS | Forms, project workflow and typed state. Keep components simple for the team [R1]. |
| 2D editor | SVG or Canvas with a geometry interaction layer | Numeric editing, dimensions, selection, snapping and exports; enforce common model IDs. |
| 3D editor | Three.js with parametric meshes and orbit controls | Model linked views, object transforms and ray based selection; 2D fallback for unsupported devices [R3]. |
| Backend API | Python FastAPI with Pydantic | Typed contracts, input validation and integration with Python geometry and AI services [R2]. |
| Geometry and search | Shapely and Google OR Tools CP SAT | Polygon checks and bounded constraint search. CP SAT requires integer constraints; scale to integer units explicitly [R4]. |
| Database | PostgreSQL with pgvector | Projects, rules, revisions and vector retrieval in one database [R5]. |
| Document ingestion | PDF text extraction with optional OCR | Use page provenance and review queues. Pin parser versions after compatibility testing. |
| AI orchestration | One provider adapter for an LLM and embeddings | Choose provider and model after a cost and grounding evaluation; no provider is yet contracted. |
| Files and jobs | File object storage and a bounded worker queue | Source PDFs, exports and long running ingestion or generation jobs. |
| Testing and delivery | pytest, browser interaction tests and Git based CI | Reproducible checks, locked dependencies, separate configuration and a staged deployment. |

 

### Current prototype and migration

The existing prototype uses browser JavaScript and local project storage. It demonstrates interaction design, not the proposed secure multiuser backend. Retain useful model and renderer logic, add schema migration and replace browser only ownership with server authorisation. Blender may be an optional offline render tool; it is not required for every interactive edit.

## Integrations and interfaces

| Integration | Required exchange | Failure and operating rule |
| --- | --- | --- |
| LLM provider | Filtered evidence and a user request; receive an answer or structured edit proposal. | Server credentials, timeouts, budgets and validation. No direct uncontrolled writes to projects. |
| Embedding service | Eligible document chunks and query embeddings. | Version the embedding model; rebuild an index when model compatibility changes. |
| Weather or climate API | Coordinates, period and variables; receive temperature, rain, wind and solar context. | Cache with provenance. On failure mark climate pending; do not invent observations. |
| Sri Lankan rule sources | Curated UDA, local plan and other eligible source documents. | Controlled ingestion rather than assuming a live authoritative regulations API. |
| Rates and measurement sources | Reviewed BSR or SoR releases and measurement references. | Manual or batch import with review; never treat a rate PDF as a source for room setbacks. |
| Global component sources | Manufacturer specifications and licensed 2D or 3D assets. | Track dimensions and rights; source sizes do not establish local availability or price. |
| Exports and storage | Versioned JSON, drawings, images and PDF reports. | Validate ownership, preserve units and revision, and expire temporary download links. |

 

### Weather licensing and design use

Open Meteo is a candidate provider. Its free tier is described for noncommercial evaluation and prototyping; commercial use requires a subscription. Historical data availability depends on the selected plan [R6]. Confirm the chosen endpoint and terms before integration. Multi year context is needed for orientation; a current forecast is not a climate design rule.

### Core interface contract

A generation request contains project_id, base_revision, brief, unit and rule_release_id. Its result contains status, candidates, constraint_conflicts, pending_checks and evidence references. An edit request contains target IDs and a structured operation. The service returns a proposed or committed revision with validation results; it never silently overwrites a different base revision.

Stable entities include Project, Brief, Plot, Storey, Room, Wall, Opening, ComponentInstance, Rule, Evidence, ClimateContext, QuantityItem, RateItem, ValidationResult and Revision. Canonical dimensions use integer millimetres. Display units are independent; solver discretisation must not weaken verified bounds.

## User experience and business use cases

### Workspace requirements

Use the user supplied prototype references as the interaction starting point. Keep a large, proportionally correct 2D or 3D viewport and a readable requirements and review panel. Room names and dimensions must remain legible when furnished. Offer explicit mode, unit, north, road and revision indicators. Avoid hiding the active scene while the component library is open.

Provide a cutaway view to reveal interiors without changing real wall heights. Fit the full model to the viewport on first load and provide a reset camera control. Separate camera zoom from geometry scaling. Numeric fields must not round and resave untouched dimensions during unrelated edits.

| Use case | Main path | Exception or recovery |
| --- | --- | --- |
| UC01 Create a concept | Enter brief, confirm assumptions, generate, compare and choose a candidate. | Missing locality or rule coverage is shown before a regulatory claim can be made. |
| UC02 Adjust a room | Select a room, change size, preview consequences and commit a valid edit. | Show conflicts and permit undo; do not silently squeeze other rooms. |
| UC03 Edit through conversation | Ask for a supported change, resolve ambiguity, review the proposed operation. | Unsupported commands return a clear limitation and a manual edit route. |
| UC04 Inspect and furnish | Inspect 3D, confirm the spatial concept, place items and customise them. | Warn about clearance or access conflicts and offer alternate placement. |
| UC05 Review a cost | Select a rate release, calculate supported quantities and inspect exclusions. | Missing mappings are shown as unpriced; do not default missing costs to zero. |
| UC06 Finalise and export | Review warnings, freeze a revision and download the review package. | Show unresolved checks in the exported report; stale calculations must be recomputed. |

 

### Accessibility and language

R1 proposes English labels with plain explanations and unit clarity. Tamil and Sinhala support can follow user testing. Keep exact source excerpts in their original language and distinguish translated explanation from the authoritative source. Provide keyboard and numeric alternatives for drag actions.

## Acceptance and evaluation

Release acceptance requires recorded evidence from the integrated R1 system. Screen appearance alone does not satisfy geometry, regulatory or cost requirements. Use a versioned holdout set and record both expected results and actual outputs.

| Test | Acceptance scenario | Requirements |
| --- | --- | --- |
| AT01 | A supported brief produces candidates that contain the requested rooms and satisfy all implemented hard constraints. | FR01 to FR09 |
| AT02 | An oversized brief reports the solver status and conflicts. A forced timeout returns incomplete search, not construction impossibility. | FR08 FR10 |
| AT03 | Changing feet to metres and back preserves dimensions within 1 mm; display formatting does not change untouched fields. | FR04 NF01 |
| AT04 | A room resize updates shared walls, 2D, 3D and quantities; an invalid overlap cannot be finalised as passed. | FR11 to FR20 |
| AT05 | Undo restores the prior geometry, opening hosts and revision consistent outputs. | FR16 FR20 |
| AT06 | A disconnected room, blocked door swing and opening outside a host wall are correctly identified. | FR17 to FR19 |
| AT07 | Furniture replacement respects catalogue size; placement identifies tested access and clearance conflicts. | FR21 to FR24 |
| AT08 | A regulatory question receives an eligible source and page; absent or conflicting evidence produces abstention or pending status. | FR30 FR31 |
| AT09 | A malicious instruction inside a source document cannot invoke an edit or expose another project. | FR32 NF06 NF09 |
| AT10 | Known sample quantities match a QS reviewed worksheet within the stated item tolerance; rate basis is reproduced. | FR34 to FR36 |
| AT11 | Weather failure preserves the plan, labels climate pending and offers cached or manual context. | FR25 FR26 |
| AT12 | Saving, reopening, finalising and exporting preserve ownership, units, revision and outstanding issues. | FR01 FR38 FR40 |

 

### Evaluation set and release gate

Proposed starter set: 20 diverse briefs, 20 deliberately invalid plan cases, 50 evidence linked questions and 10 reviewed BOQ examples. Keep related or duplicate source plans out of separate train and test partitions. All critical acceptance cases must pass; every remaining limitation must be listed in the release notes. Report measured citation support and abstention rather than claiming 99% overall engineering accuracy.

## Delivery plan and team ownership

| Week | Primary outcome | Evidence before progression |
| --- | --- | --- |
| 1 | Freeze R1, pilot jurisdiction, canonical schema and benchmark briefs. | Scope record, initial source register, reviewer plan and schema examples. |
| 2 | Prepare verified starter rules and establish project persistence and knowledge retrieval. | Unit validation, source provenance and ownership tests. |
| 3 | Implement geometry, bounded generation and initial hard checks. | Valid and infeasible cases; truthful search status. |
| 4 | Connect editable 2D, openings and circulation checks. | Shared wall and door access tests; undo demonstration. |
| 5 | Connect parametric 3D and structured conversational edits. | Matching revision across views and ambiguity handling. |
| 6 | Add furnishing, limited climate context and pilot BOQ and rates. | Placement tests and reviewed quantity calculations. |
| 7 | Integrate reports, exports, performance checks and end to end scenarios. | Acceptance results, security tests and restored backup. |
| 8 | Run user evaluation, fix critical defects and package the submission. | Demonstration, limitations, source release and signoff record. |

 

### Seven member research and delivery mapping

| Member | Research ownership | Suggested delivery pairing |
| --- | --- | --- |
| 1 | Weather and climate rules | Orientation module and climate integration. |
| 2 | Construction measurement and rates | BOQ and cost service with QS review. |
| 3 | Room dimensions and space standards | Constraint rules, unit checks and applicability evidence. |
| 4 | Room adjacency and functional relationships | Solver preferences and circulation tests. |
| 5 | Sri Lankan planning rules | Rule governance and regulatory reporting. |
| 6 | Doors windows furniture and fixtures | Component catalogue and editable 2D or 3D assets. |
| 7 | Architecture templates and reference plans | Template retrieval, layout evaluation and UI workflow. |

 

This is a proposed ownership model, not a claim that research members have accepted development tasks. The technical lead owns the solver integration; the adjacency lead owns scoring criteria. Confirm named assignees during kickoff. One member must coordinate integration and QA; domain data ownership alone does not deliver an automatic planning system.

## Risks and budget

| Risk | Business impact | Mitigation and owner |
| --- | --- | --- |
| Incomplete local rule coverage | Users may mistake an assumption for a regulatory pass. | Pilot one locality, require provenance and retain pending status. Planning lead. |
| Solver complexity or failed search | Candidate generation may miss the delivery window. | Bound R1 geometry and search time; distinguish timeout. Solver owner. |
| Dataset errors or duplicates | Layouts and evaluation results may be misleading. | Audit sample records, units and near duplicates. Data curator. |
| 2D and 3D drift | Users may edit or export inconsistent models. | Shared model, stable IDs and revision tests. Geometry owner. |
| LLM hallucination or unsafe instructions | Unsupported advice or unintended edits. | Evidence filters, abstention and validated operations. AI owner. |
| Unreviewed measurement or old rates | Preliminary costs may be materially wrong. | QS review, dated releases and explicit exclusions. Cost lead. |
| Device or external service limits | Rendering, weather or AI may be unavailable. | 2D fallback, caching, cancellation and budgets. Platform lead. |
| Scope expansion or missing reviewers | The team cannot complete the agreed release. | Scope freeze, weekly review and early reviewer scheduling. Project owner. |

 

### Provisional cash planning envelope

A prior project planning figure of LKR 15,000 is carried forward as an assumption for confirmation. The following allocations are spending caps, not vendor quotes, exchange rate conversions or confirmed invoices. Team labour and existing equipment are not priced here.

| Category | Proposed cap LKR | Basis |
| --- | --- | --- |
| LLM and inference | 6,000 | Usage limited pilot only |
| Embeddings and ingestion | 2,000 | Prefer reusable indexes and local processing |
| Hosting and storage | 4,000 | Pilot environment and backups |
| Data review and tools | 1,000 | Small operational allowance, not a professional fee quote |
| Contingency | 2,000 | Provider, storage or integration variance |
| Total | 15,000 | Requires approval and current service quotes |

 

Paid historical climate access, professional consultation, software licences and local product procurement are not assumed affordable within this cap. Use an eligible research workflow or revise scope and budget before committing expenditure.

## Assumptions decisions and approval

### Assumptions and dependencies

The university accepts a concept planning MVP and a transparent limitations report rather than an approved construction drawing service.

The team can provide an appropriate development PC, a persistent database and reviewer access; restricted university PCs may require a separate test environment.

Collected documents are candidate evidence until extraction, applicability, rights and reviewer status are established. No completion percentage is asserted by this BRD.

The team will confirm any statutory interpretation and measurement method with suitable reviewers. A downloaded source or dataset is not automatically applicable to a project.

Generic global component dimensions remain in scope. Current Sri Lankan furniture availability and prices remain future scope.

### Open decisions before the R1 baseline

| ID | Decision to confirm | Owner |
| --- | --- | --- |
| D01 | Select the pilot locality, planning authority and eligible rule release. | Planning lead and domain reviewer |
| D02 | Confirm R1 limits, required room types and full versus reduced BOQ subset. | Project owner and supervisor |
| D03 | Confirm the proposed technical stack and a compatible development environment. | Technical lead |
| D04 | Select the LLM, embedding model, privacy settings and spending limits. | AI and project leads |
| D05 | Choose the climate data period, provider access and reviewed guidance. | Climate lead |
| D06 | Confirm KPI baselines, test hardware, measurement tolerances and pilot participants. | QA lead and reviewers |
| D07 | Nominate reviewers and approve retention, sharing and finalisation policies. | Project owner |

 

### Change control and approval record

Record each requested change with its reason, affected requirement IDs, data dependencies, delivery impact and acceptance changes. The project owner and supervisor agree any change to R1; domain reviewers approve changes within their reviewed subject. Retain the previous BRD version.

| Approval role | Name | Decision and date |
| --- | --- | --- |
| Project representative | To be nominated | Pending |
| University supervisor | To be confirmed | Pending |
| Architect or planning reviewer | To be confirmed | Domain review pending |
| Quantity surveyor | To be confirmed | Measurement and rates review pending |

 

## References and glossary

References below support technology selection and source handling. They do not establish that a particular building rule applies to an individual site. Source documents used by the deployed RAG require their own document register with page, clause, effective period and applicability review.

R0  Project brief and scope baseline
BuildMind project requirements and prototype review, including automatic layout generation, manual and conversational edits, linked 2D and 3D, furnishing and future local product pricing.

R1  Angular documentation
https://angular.dev/overview

R2  FastAPI documentation
https://fastapi.tiangolo.com/

R3  Three js documentation
https://threejs.org/docs/

R4  Google OR Tools CP SAT documentation
https://developers.google.com/optimization/cp/cp_solver

R5  pgvector project documentation
https://github.com/pgvector/pgvector

R6  Open Meteo access and pricing
https://open-meteo.com/en/pricing

R7  ResPlan dataset and licence information
https://github.com/m-agour/ResPlan

R8  CubiCasa5K dataset and licence information
https://github.com/CubiCasa/CubiCasa5k

R9  UDA development plans and regulations source portal
https://www.uda.gov.lk/development-plans.html

Online technical references checked 24 October 2026. Pin implementation versions and recheck service terms at integration. The proposed stack is a project recommendation, not an already completed backend.

### Glossary

| Term | Meaning in this document |
| --- | --- |
| BRD | Business requirements document defining business intent and acceptance. |
| RAG | Retrieval augmented generation using selected evidence at answer time. |
| BOQ | Bill of quantities derived using a stated measurement method. |
| BSR and SoR | Building or schedule of rates; the precise release and scope must be recorded. |
| Hard constraint | A required condition that a candidate or committed edit may not violate. |
| Soft preference | A weighted design goal that can be traded off and explained. |
| Parametric model | Geometry defined by dimensions, relations and editable parameters. |
| Pending check | A requirement for which necessary data, applicability or validation is incomplete. |

 

