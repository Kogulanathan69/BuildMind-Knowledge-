# Datasets and evidence

## Seven owners and eight collections

| Member | Research area | Output |
| --- | --- | --- |
| 1 | Weather and climate | Source weather plus reviewed climate rules |
| 2 | Construction cost | BOQ measurement, work items, resources and dated rates |
| 3 | Room dimensions and space standards | Sri Lankan sourced dimensional rules and reviewed examples |
| 4 | Room adjacency | Typed adjacency and access relationships |
| 5 | Building regulations | Applicable Sri Lankan planning requirements |
| 6 | Doors, windows, furniture and bathroom fixtures | Dimensions, clearances, swings, catalogues and rights |
| 7 | Architecture styles and templates | Structured plans, style metadata and evaluation examples |

The user selected Member 3, research and dataset preparation, not ownership of automatic AI plan generation. Two days were available for that initial research task. Adjacency sources were also requested. Eight collections are planning rules, room standards, layout rules, climate rules, components, templates, BOQ/rates and test plans. Ten or twelve engines do not imply ten or twelve independent datasets; geometry, rendering and reporting are mostly code.

## Common schema and governance

Record `record_id`, `rule_type`, `severity`, `verification_status`, `verified_by`, `effective_date`, `unit`, source document/URL, publisher, page/clause, jurisdiction, applicability conditions, collected date, version and notes. Keep evidence verification separate from local applicability. Types: regulation, recommended practice, architect guideline, prototype assumption, user preference. Severities: hard/soft. Draft values cannot silently become mandatory law.

| Collection | Additional proposed fields |
| --- | --- |
| Room standards | room_type, parameter, min/max/recommended value, conditional basis |
| Layout rules | rule_id, room_a, room_b, relation, weight, rationale, reviewer |
| Climate rules | climate_zone, parameter, condition, recommended_value, basis, period |
| Components | component, type, width_mm, height_mm, depth_mm, thickness_mm, swing, clearance_mm, catalogue |
| Templates | template_id, plot range, bedrooms, storeys, plan_json, style, reviewer |
| Test plans | case_id, plot_w, plot_l, unit, brief_json, plan_json, expected_result, known_errors, reviewer, date |
| BOQ/rates | work_item_id, unit, formula, deductions, resource coefficients, rate, location, date, currency, inclusions |

Keep furniture in a separately understandable sheet where useful. Validate numeric ranges, units, required cells, IDs and references with pandas/Pydantic. A proposed starter completion gate was at least 20 source-verified sample rows, reviewer record, machine validation and Git versioning. This is not proof of sufficient coverage for a complete system. Never invent a source to fill a required cell.

## Sri Lankan room and planning research

The user repeatedly excluded foreign codes including ICC IRC. UDA documents must be opened and checked for exact room provisions before a number is labelled a Sri Lankan legal minimum. If no applicable legal minimum is found, record that uncertainty; use a named architect-reviewed guideline where available. Example plan dimensions are examples, not statutory rules.

NHDA PDFs and some Plans.lk/Kedella Homes links were reported unavailable to download. University of Moratuwa housing research and Sri Lankan plan publications were requested as alternatives. A Scribd plan named `09-03 FIRST FLOOR-1` was questioned for Sri Lankan origin; origin and reuse rights must be checked, not inferred from its title. Four user-supplied PDFs needed separate extraction; an initial two-file count was disputed. This archive does not certify that those four PDFs are all physically present here.

Nine Sri Lankan floor-plan images were discussed. The user manually confirmed Plan 5 and Plan 8 are different. Treat all nine as distinct candidate plans unless evidence later shows duplication. Image-derived dimensions need scale and annotation verification. An NBRO pack previously discussed had 14 sheets, not necessarily 14 distinct houses, with separate long manuals/foundation references. Do not equate sheets, PDFs and unique layouts.

Existing deliverable references: `BuildMind_NBRO_Reference_Plan_Extraction_v1.xlsx`, `BuildMind_AI_Room_Adjacency_Knowledgebase.xlsx`, `BuildMind_Room_Adjacency_DETAILED_FIXED.xlsx`. The initial adjacency workbook was challenged as insufficiently populated, and a detailed corrected version was supplied. These filenames identify earlier deliverables; their workbook bytes and cells have not been newly audited by this update.

## Weather

Existing repository report: Siyambalanduwa September–December 2021; 14,112 available ten-minute readings against 17,568 expected; 3,456 readings missing October 7–30. Timestamp coverage 80.3% is station-period coverage, not BuildMind completion. See `knowledge/datasets/01_weather/DATA_QUALITY_REPORT.md`. Solar, calibration, units, timezone and licensing need confirmation. One station and four months do not describe annual climate across Sri Lanka.

Open-Meteo was considered for API connection. Recorded reference https://open-meteo.com/en/pricing and documentation https://open-meteo.com/en/docs require current terms/period checks at integration. The prior review described free noncommercial evaluation/prototyping and paid commercial use. Do not promise a provider entitlement without checking it. Raw weather must become reviewed context-dependent guidance for opening direction, shading/overhang, ventilation pairing and any window-area recommendation. No universal numerical ratio or north-facing rule has been approved here.

## Components

Global dimensional catalogues are allowed; verify each item's dimensions and use/installation clearances. Catalogue dimensions alone do not prove comfort, legal accessibility, safe swing or access. An earlier Member 6 pack reportedly held 1,200 metadata entries with unverified dimensions and no per-row source URLs; 24 separate references were not matched to all entries. That count is not a verified catalogue. Sri Lankan product stock/prices stay future scope.

## Plan datasets

### ResPlan

Reference https://github.com/m-agour/ResPlan . A user upload `ResPlan(1).zip` previously passed ZIP integrity checks and contained `ResPlan.pkl` (258,453,658 uncompressed bytes; archive approximately 100 MB). This is prior discussion evidence, not a new record-by-record audit. The pickle was not unpickled. Never deserialize an untrusted pickle without an isolated review process.

Author-reported partition counts discussed: train 13,053; validation 1,632; test 1,632; augmented 683; total 17,000. Keep augmented/related plans together for evaluation and check near duplicates. Layout data are examples, not Sri Lankan permits. Plan graph conversion may be needed; no furniture/3D catalogue is implied. Prior review described data CC BY 4.0 and code MIT; retain the exact upstream terms and original attribution, and verify rights before redistribution.

The user's Windows clone failed with `No space left on device` and `invalid index-pack output`. Free storage and distinguish cloning code from acquiring dataset files; do not assert that a failed clone has installed the dataset.

### CubiCasa5K

Reference https://github.com/CubiCasa/CubiCasa5k . Discussed as 5,000 plan images with 80+ object categories; actual dataset download was separate (around 5.5 GB in the prior review). Cloning the repository is not downloading its data. Prior review identified CC BY NC 4.0 restrictions; check terms and commercial suitability before adoption. It supports plan understanding, not local compliance or a ready furnishing model library. An earlier `data.zip` reportedly held code/model weights rather than the expected dataset.

## Construction BOQ and rates

Existing cost notes remain in `knowledge/datasets/02_construction_cost` and the October 19 history. Sources discussed include Northern Province 2026 schedules and amendments, Department of Buildings BSR releases, provincial schedules, CIDA/ICTAD references, Census and Statistics bulletins and calculation references. Some collected documents are irrelevant, outdated or duplicates; a source archive inventory is not an approved rate catalogue.

Keep work items, measurement rules, resource coefficients, material prices, labour rates/productivity, equipment, transport, wastage and adjustment rules distinct. Preserve price history and district/effective-date selection. Separate RCC concrete, reinforcement, binding wire and formwork when the measurement basis requires it. Do not apply transport, tax, overhead or profit twice if included in a composite rate.

BSR/SoR are cost sources, not evidence for room minima or setbacks. Irrigation productivity is not automatically residential productivity. A prior schedule mentioned SLS 573:1999; a later review identified an SLS 573:2025 reference as a candidate update. The actual applicable measurement text/version remains unverified. Obtain the relevant document and QS review rather than claiming either edition has been adopted.

Unpriced quantities remain visibly unpriced; absence is not zero cost. Every estimate records revision, measurement basis, source release, date, region, currency, inclusions, exclusions and pending review. Preliminary quantities cannot imply structural design has been performed.

## Source collection and completion

The user supplied a Google Drive folder and asked about uploading/downloading/sharing ZIPs, file counts, inaccessible links and remaining documents. The link is a collection location, not proof of access, completeness or rights. Missing screenshot paths were repeatedly reported by the client; their contents cannot be reconstructed. The full private Drive link and personal email are intentionally not copied into this public-facing knowledge record.

Earlier approximate “70–80% source documents” and “25–35% cleaned” statements were not audited project metrics. Do not repeat them as current completion. Report separately: source acquired, extracted, source-verified, applicability-reviewed, schema-valid, integrated and acceptance-tested. Existing `SOURCE_INVENTORY.csv`, duplicate report and CSV catalogue are preserved; inspect their contents before counting.

## Recorded source entry points

- UDA: https://www.uda.gov.lk/development-plans.html
- ResPlan: https://github.com/m-agour/ResPlan
- CubiCasa5K: https://github.com/CubiCasa/CubiCasa5k
- Open-Meteo: https://open-meteo.com/en/docs
- OR Tools: https://developers.google.com/optimization/cp/cp_solver
- pgvector: https://github.com/pgvector/pgvector

These are entry points, not direct download guarantees. Local rules require exact document, clause/page, applicable locality, date and reviewer.
