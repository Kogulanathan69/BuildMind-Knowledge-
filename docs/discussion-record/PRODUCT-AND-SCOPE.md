# Product scope and user journey

## Identity and purpose

BuildMind is an AI assisted residential concept planning system for Sri Lanka. The product must generate a plan automatically, not just display a fixed dummy plan. The user wants dimensional consistency and realistic outputs; the requested “99% engineer accuracy” is an aspiration, not a measured or supportable claim. The system supports concept review, not automatic building permission or structural certification.

## Intended complete workflow

1. Capture land width and length, units, locality and authority, north direction, road side, room requirements, parking, budget and preferences.
2. Confirm the structured brief, missing information, source applicability and assumptions.
3. Compute the usable envelope and use a constraint solver to search for candidate arrangements.
4. Explain candidate feasibility within the implemented model. If requirements conflict, identify the conflict and suggest changes for user approval rather than silently removing rooms.
5. Show distinct plan alternatives and explain their scores and tradeoffs.
6. Display a dimensioned 2D plan. Support manual dragging, numeric dimensions and supported natural language comments to change it.
7. Generate a parametric 3D view from the same model. Allow supported 3D edits because the user may discover new ideas while inspecting it.
8. After spatial concept review, place furniture, doors and bathroom fixture models intelligently; let the user move, replace, resize where appropriate and delete them.
9. Revalidate dependent geometry, access, openings and clearances. Recompute supported quantities and costs or mark them stale.
10. Save revisions, undo changes, finalise a concept and export a review report. Finalisation freezes a revision; subsequent edits create a new one.

Door openings, windows and bathroom fixture positions must be considered during planning. Waiting until furnishing to create essential access would invalidate earlier checks. Final furnishing selects models and appearance and refines placement.

## Important user decisions

- Sri Lankan rules and regulations only for statutory research and validation. Do not substitute ICC IRC or another international code for Sri Lankan law.
- Global furniture, door and bathroom fixture dimensional sources are allowed. This exception concerns components, not regulatory requirements.
- Sri Lankan furniture stock, supplier availability and current product pricing are future scope. Sri Lankan construction BOQ/rates remain in scope as a bounded preliminary estimate.
- Consider road direction, north, daylight, ventilation and optional cultural preferences. “Pooja room should not be next to bathroom” is a user preference unless a separate applicable source proves a different classification.
- Keep this project record focused on BuildMind. Other projects discussed by the user are outside this repository.

## Proposed first release and later expansion

The submission BRD proposes rectangular plots, one storey, one to three bedrooms, one or two bathrooms and optional one car parking. English first; Tamil may follow user testing. Include bounded 2D/3D edits, selected chat commands, a small verified generic component catalogue, one pilot jurisdiction, limited climate demonstration and a reviewed subset of BOQ and rates.

Irregular plots, additional floors, advanced roofs, broad authority coverage, unrestricted conversational editing, richer BIM exchange, uploaded survey interpretation and specialist simulation need later scope and estimates. Detailed structure, foundations, MEP design, geotechnical checks, procurement, payments and approval submission are not first release deliverables.

## Stakeholders and roles

Homeowners provide facts and preferences; students and designers explore concepts; architects and planning reviewers review applicability and design guidance; civil/structural engineers advise within their discipline; QS reviewers validate measurement and rate interpretation. The project owner controls scope; the supervisor reviews academic acceptance. Data curators maintain evidence; admins manage authorised configuration and releases; developers and QA implement and test. A generic admin account is not a professional reviewer.

## Proposed differentiators

Sri Lankan source-linked guidance; explainable fit and alternatives; one shared 2D/3D/quantity model; manual plus conversational editing; space-aware furnishing; explicit climate and preference tradeoffs. These are proposed USPs to demonstrate. Global novelty and competitor superiority have not been established. Maket, Homestyler and Drafted were mentioned for comparison; use the same benchmark briefs and report actual observations before claiming an advantage. Local design-service examples discussed include Structa and housedesign.lk, not validated feature baselines.
