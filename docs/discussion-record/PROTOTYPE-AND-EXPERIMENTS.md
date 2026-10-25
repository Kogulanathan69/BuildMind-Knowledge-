# Prototype and experiments

## Current prototype versus intended product

Prototype URL recorded in the project discussion: https://buildmind-design-studio.parthyniru27.chatgpt.site . Access is owner-restricted according to the last deployment record; the knowledge-repository update does not publish or change the site.

The current browser prototype demonstrates templated rooms, dimension editing, linked 2D and 3D views, generic furniture, basic boundary/overlap checks, local project state and keyword commands. It does not have integrated source-backed RAG, a real layout constraint solver, authoritative regulatory coverage, live climate rules or a validated BOQ/cost pipeline. Attractive output is not proof of those integrations.

Last recorded deployed source commit: `b6e8627b921d9ef5fea0b6d29effe400ba936374` on 23 October. This is the separate prototype source repository, not a commit in the knowledge repository. The prototype source is not duplicated here by this documentation change.

## UI evolution and user feedback

1. Initial green dashboard rejected; user requested a colour change.
2. Blue treatment and subsequent navy CAD/dashboard approaches were rejected as childish or unsuitable.
3. Visual home editor direction selected.
4. User shared a Claude artifact reference and screenshots with a large plan/model area on the left and requirement/edit cards on the right.
5. Reference-oriented redesign implemented; user complained that sizes/proportions and rendering were inconsistent.
6. Three.js rendering and fit/zoom were improved. Later Windows screenshots showed working 3D but full-height walls obscured interior furniture and the furnishing panel required excessive scrolling.

Desired UI: professional, simple, accurate proportions, large readable canvas, clear units, predictable dimensions and compact same-screen furnishing controls. Do not revert to a green playful dashboard. A real cutaway view and a compact furnishing library were identified as remaining work, not silently completed. A reference screenshot's arbitrary 65/100 score was not adopted as meaningful feasibility.

## Browser implementation notes

The prototype uses plain JavaScript with `viewer.js`, locally vendored Three.js modules, OrbitControls and an official SVGRenderer fallback. WebGL was unavailable in the cloud QA browser; fallback rendering was inspected there. Later user screenshots showed actual Windows WebGL. Do not claim GPU testing in the cloud session.

Frontend state uses metres with feet display; proposed backend integer millimetres are a future model migration. Stable room/object/opening IDs and undo exist to a limited prototype extent. Local storage key was `buildmind-visual-v1`. Objects include beds, sofas, tables, chairs, plants, toilets, basins, doors and windows; they are illustrative, not a source-verified manufacturer catalogue.

Reference input: 40×60 ft, three bedrooms, two bathrooms, parking. Prototype assumed margin deductions produced a 34×35 ft footprint. These are demonstration assumptions, not Sri Lankan setbacks. Template zoning used bedrooms on the left, service rooms at the back and living/dining in the remaining area. Alternatives A/B/C were original and mirrored layouts, not independent solver-scored designs.

The revised renderer constructs hosted wall openings, sills/lintels and glass. Controls include room/object selection, move tools, roof visibility, wall-height slider and fit/reset. Numeric field precision was increased to avoid rounding untouched dimensions into apparent overlaps. Mirror floating-point overlap tolerance was corrected. Shared-model 2D/3D transforms are bounded; full adjacency, legal clearances and BOQ invalidation are still not implemented.

SVG fallback draw order was corrected so floor/base/ground do not obscure interiors. PNG/JSON export paths were demonstrated. Full-height walls can still hide furniture; reducing wall height is not a substitute for a proper cutaway mode. Furnishing below the viewport remains a UX issue.

## Earlier n8n and SVG experiment

Input fields: `landWidth`, `landLength`, `bedrooms`, `bathrooms`, `parking`, `preferences`. Earlier bounds included bedrooms 1–3, bathrooms 0–2, parking 0–1; the submitted proposed MVP now uses one or two bathrooms. Demonstration sizes included living 18×14 ft, kitchen 12×10, dining 10×10, master 12×12, other bedrooms 10×10, bathroom 6×8, parking 10×18 and corridor 4 ft. These were prototype assumptions, never verified Sri Lankan minima.

Rules tried: kitchen near dining, bedrooms grouped, master near living, north-light windows, open kitchen/dining merge. Output schema: `{land:{width,length}, rooms:[], doors:[], windows:[]}`; doors included coordinates, width, orientation and swing; windows included coordinates, width and orientation.

SVG experiment used a 900×760 canvas, auto scaling, land boundary, coloured rooms, labels, swing arcs, double-line windows, dimensions and north arrow, titled BuildMind AI Generated 2D Floor Plan with preliminary-concept wording. This was an experiment, not a tested CAD export engine.

## Blender and MCP experiment

Prior user environment: Blender 3.6 with MCP on port 9876. Recorded Stage 4 roof `Roof_Hip_22deg`: 22-degree hip roof, 0.6 m overhang, 0.10 m solidify, terracotta `Roof_Tile`, collection `07_Roof`. Camera `BuildMind_IsoCam`; EEVEE render 1920×1080, 64 samples, Filmic.

Stage 5 report described 64 objects: 3 land, 9 walls, 7 floors, 6 doors, 11 windows, 24 furniture, roof, camera, sun and original light. File name `BuildMind_House_Stage5.blend`; Stage 6 continuation was requested. That `.blend` file is not asserted present in this repository or freshly inspected. Do not turn a named scene snapshot into a validated construction model.

## Branding

The user requested circular logo variants, merged visual references, lighter colours, removal of inner text and BuildMind name placement near/below the mark. Tagline direction: clear AI-assisted residential house design. Final logo bytes and a definitively approved variant are not established by this documentation update; do not invent a final asset.
