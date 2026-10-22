# BuildMind — AI Continuation / Handoff
Updated: 2026-10-22. Context reconstructed from conversation and uploaded file inventory.

## User goal
BuildMind: Sri Lanka-focused AI-assisted residential house design and construction planning. Intended capabilities include 2D floor-plan drawing/generation, 3D house models, cost quotations, and regulatory/climate-aware design support. User wants continuity when switching between AI assistants.

## Technical direction discussed (verify against current repository code)
- Angular frontend; Konva.js for 2D; Three.js for 3D.
- Python FastAPI backend; PostgreSQL and RAG/knowledge retrieval under consideration.
- **Do not assume any implementation is complete**. Read the existing GitHub repository documents and source tree first.

## Seven dataset owners/topics
1. Weather / climate: temperature, humidity, wind, rainfall, solar radiation, district/time metadata.
2. Construction costs: BSR/SoR, suppliers, regional prices, material and labor rates, edition years.
3. Room dimensions: minimum/preferred sizes, circulation, heights, context.
4. Room adjacency: privacy zones, functional relations, plan-derived adjacency matrices.
5. Sri Lanka building rules: UDA, local plans, gazettes, setbacks, zoning, road access etc.
6. Doors, windows, furniture and object dimensions: dimensions/clearances/schedules.
7. Architecture styles and house plan templates: local examples, provenance and permitted usage.

## Source collection summary
- Numerous city development plans, UDA-related documents and gazettes in source ZIPs.
- BSR/SoR construction cost material in source ZIPs.
- `weather-data-siyambalanduwa.zip`: four monthly weather CSVs for Sep–Dec 2021, with gaps/quality checks required. Local station data cannot represent all Sri Lanka.
- `BuildMind_AI_Dataset_v1 (1).zip`: structured Excel seed data; rules must be legally validated.
- `Build Mind Data Set - Niru.zip`: 26 files including flood/landslide type plans, construction/foundation guidance, cost/design research and presentation material. Can derive room dimensions, adjacency examples and openings schedules; not a ready-made adjacency dataset.
- Some uploaded ZIPs contain food, unrelated procurements, awards and other materials; do not indiscriminately ingest.
- Exact per-file manifest and SHA-256 duplicate groups are in SOURCE_INVENTORY.csv and DUPLICATES.json.

## Important epistemic limits
- Earlier assistant estimated raw collection at ~63%, **not a measured completeness or RAG readiness figure**.
- Some earlier conversation claims of completeness/validation should be treated as provisional until checked against source content.
- A city plan applies to its actual jurisdiction and effective date; do not extrapolate to all 25 districts.
- Regulations, professional guidelines and research papers must be tagged separately.
- Never claim building code compliance or safe structural design from unverified retrieval; professional/local authority review needed.

## Next actions
1. Inspect current repo before changing existing files.
2. Commit these handoff files under `knowledge/handoff/` or merge with existing docs.
3. Decide which source PDFs/CSVs can legally be redistributed. Preserve provenance, publication dates and source URLs.
4. Deduplicate, discard corrupted downloads; perform malware and confidential-data review.
5. Parse PDFs/Excel/CSV, recording page/section, jurisdiction, rule type, validity/edition, language, extraction confidence.
6. Create normalized tables, chunk documents, embed, index in vector store, and design hybrid source-cited retrieval.
7. Evaluation: 7 topic coverage, source citation accuracy, conflicting regulations, local scope, outdated documents, missing answer abstention.
8. Add verified source gaps in missing-data tracker and expand data collection.

## Instruction for next AI
Start by reading this file, DATASET_STATUS.md, SOURCE_INVENTORY.csv and repository README / project decisions / current status. Summarize what is **verified** versus **assumed**; ask only for genuinely missing inputs. Continue with RAG ingestion and source validation rather than re-collecting already archived PDFs.
