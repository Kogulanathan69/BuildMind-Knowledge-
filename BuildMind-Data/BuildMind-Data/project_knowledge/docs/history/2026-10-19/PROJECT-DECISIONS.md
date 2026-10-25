\# BuildMind - Project Decisions



Last Updated: 2026-10-19



This file records important finalized BuildMind project decisions.



Future developers, team members, or AI assistants should review this file before changing architecture, scope, datasets, or workflows.



\---



\## DECISION-001 - Project Name



Date:

2026-10-07



Decision:

The project name is finalized as:



BuildMind



Status:

Final



Reason:

The name represents an AI-assisted construction design and planning system.



\---



\## DECISION-002 - Main Project Type



Decision:

BuildMind is an:



AI-Powered Residential House Design and Construction Planning System



Status:

Final



\---



\## DECISION-003 - Primary Project Scope



Decision:

The system should support:



\- Residential house requirement collection

\- Automatic floor-plan generation

\- 2D visualization

\- 3D visualization

\- Cost estimation

\- AI chat assistance

\- Plan refinement

\- Dataset-driven validation

\- Admin-managed construction data



Status:

Final



\---



\## DECISION-004 - Main System Roles



Decision:

BuildMind has three major responsibility groups:



1\. User

2\. Admin

3\. AI



Status:

Final



\---



\## DECISION-005 - AI Responsibility Boundary



Decision:

The AI should understand user requests, explain outputs, and orchestrate system modules.



The AI must not independently invent:



\- Structural engineering values

\- Construction quantities

\- Construction prices

\- Legal rules

\- Safety certification

\- Government approval status



Engineering and cost calculations must use deterministic formulas and validated data.



Status:

Final



\---



\## DECISION-006 - Frontend Technology



Decision:

Angular will be used for the main web frontend.



Status:

Final



\---



\## DECISION-007 - Backend Direction



Decision:

Python FastAPI is the preferred backend direction.



Status:

Current Final Direction



Reason:

It fits AI, optimization, geometry, and data-processing workflows well.



\---



\## DECISION-008 - Database



Decision:

PostgreSQL is the preferred main database.



Status:

Current Final Direction



\---



\## DECISION-009 - 3D Technology



Decision:

Three.js is the preferred browser-based 3D visualization technology.



Blender may be used for:



\- prototyping

\- rendering

\- testing

\- asset creation



Status:

Final for MVP direction



\---



\## DECISION-010 - Floor Plan Generation



Decision:

Floor-plan generation should not depend only on an LLM.



The layout flow should use:



\- structured user requirements

\- room standards

\- adjacency rules

\- orientation rules

\- climate rules

\- constraint solving

\- deterministic geometry

\- validation

\- scoring



The AI should support orchestration and explanation.



Status:

Final



\---



\## DECISION-011 - Multiple Plan Alternatives



Decision:

The system should generate more than one valid floor-plan alternative when possible.



The user should be able to compare alternatives.



Status:

Final



\---



\## DECISION-012 - Construction Cost Estimation



Decision:

The AI must not guess the final construction cost.



Cost estimation should follow:



House Geometry



→ Measurement Engine



→ Work Item / BOQ Engine



→ Rate Analysis Dataset



→ Material Quantities



→ Labour Quantities



→ Equipment Quantities



→ Current Price Database



→ Location / District Adjustment



→ Wastage



→ Transport



→ Overhead



→ Profit



→ VAT / Tax



→ Final LKR Estimate



Status:

Final



\---



\## DECISION-013 - Dynamic Construction Prices



Decision:

Construction prices must not be permanently hard-coded.



The Admin Panel should allow authorized users to:



\- Add prices

\- Edit prices

\- Set effective dates

\- Update district-specific prices

\- Activate prices

\- Deactivate old prices

\- Maintain price history

\- Store source information



Status:

Final



Reason:

Construction material and labour prices change over time and by location.



\---



\## DECISION-014 - Price History



Decision:

Old price records should not simply be overwritten.



Historical prices should be retained.



Status:

Final



\---



\## DECISION-015 - District-Based Pricing



Decision:

The cost system should support location-specific pricing.



Priority regions for the MVP include Northern Province districts such as:



\- Jaffna

\- Kilinochchi

\- Mullaitivu

\- Mannar

\- Vavuniya



Status:

Final



\---



\## DECISION-016 - Current Price Selection



Decision:

The cost engine should use the latest validated active price for the selected district or region.



Status:

Final



\---



\## DECISION-017 - Cost Source Priority



Decision:

For Sri Lankan cost estimation, source priority should be:



1\. Northern Province Schedule of Rates

2\. Department of Buildings BSR

3\. CIDA / ICTAD references

4\. Department of Census and Statistics

5\. Provincial official schedules

6\. Verified supplier quotations

7\. Verified contractor quotations

8\. Civil-engineering reference books for calculation logic



Status:

Final



\---



\## DECISION-018 - Dataset Traceability



Decision:

Every important dataset row should eventually contain source metadata.



Recommended metadata:



\- source\_name

\- source\_document

\- source\_url

\- source\_year

\- source\_region

\- page\_number

\- collected\_date

\- verification\_status

\- notes



Status:

Final



\---



\## DECISION-019 - Seven-Member Dataset Split



Decision:

Research responsibilities are divided into seven areas.



Member 1:

Weather / Climate



Member 2:

Construction Cost



Member 3:

Room Dimensions / Space Standards



Member 4:

Room Adjacency



Member 5:

Building Rules / Regulations



Member 6:

Doors / Windows / Furniture Dimensions



Member 7:

Architecture Styles / Plan Templates



Status:

Final



\---



\## DECISION-020 - Cost Dataset Structure



Decision:

The Construction Cost module should eventually contain structured datasets for:



\- work items

\- measurement rules

\- resource coefficients

\- material prices

\- labour rates

\- labour productivity

\- reinforcement

\- formwork

\- masonry

\- finishing

\- plumbing

\- electrical

\- equipment

\- transport

\- adjustment rules

\- source metadata



Status:

Final



\---



\## DECISION-021 - Rate Analysis



Decision:

Material prices alone are not enough for cost estimation.



The system also needs resource-consumption data.



Example:



For 1 m³ of a specified concrete work item, the system may need:



\- cement

\- sand

\- aggregate

\- water

\- labour

\- equipment



The exact coefficient must come from a validated source or reviewed engineering rule.



Status:

Final



\---



\## DECISION-022 - RCC Cost Structure



Decision:

RCC cost should not be treated as concrete alone.



RCC may include separate components such as:



\- concrete

\- reinforcement steel

\- binding wire

\- formwork

\- concrete labour

\- steel-fixing labour

\- formwork labour



Status:

Final



\---



\## DECISION-023 - Measurement Units



Decision:

Work items should use appropriate engineering measurement units.



Examples:



\- Concrete → m³

\- Wall / Plaster / Tiles → m²

\- Steel → kg

\- Doors / Fixtures → No.

\- Pipes → m

\- Labour → day / hour where applicable



Status:

Final



\---



\## DECISION-024 - Admin Cost Module



Decision:

The Admin Panel should eventually include a Cost Management module.



Expected areas:



\- Material Prices

\- Labour Rates

\- Work Items

\- Rate Analysis

\- District Rates

\- Effective Dates

\- Price History

\- Data Sources

\- Activate / Deactivate

\- Import / Export



Status:

Final



\---



\## DECISION-025 - Cost Estimate Disclaimer



Decision:

BuildMind cost estimates should be presented as preliminary estimates.



They are not:



\- contractor quotations

\- professional QS certification

\- final structural quantities

\- guaranteed construction costs



Status:

Final



\---



\## DECISION-026 - Structural Validation



Decision:

Structural quantities and safety-critical engineering values must be validated by qualified professionals before real construction use.



Status:

Final



\---



\## DECISION-027 - Building Rule Validation



Decision:

BuildMind may assist with building-rule checks, but final legal approval must be verified with the relevant local authority or professional.



Status:

Final



\---



\## DECISION-028 - MVP Scope Control



Decision:

The MVP should remain achievable within the university project timeline.



MVP priority:



\- basic residential planning

\- automatic 2D plan generation

\- room standards

\- adjacency

\- orientation

\- basic 3D

\- cost estimation

\- AI interaction

\- admin-managed datasets



Advanced BIM and full structural automation are not required for the MVP.



Status:

Final



\---



\## DECISION-029 - Knowledge Repository



Decision:

BuildMind project knowledge should be maintained in a Git repository.



Repository:



BuildMind-Knowledge-



Purpose:



\- preserve project continuity

\- support future ChatGPT sessions

\- support team handoff

\- preserve decisions

\- preserve research

\- preserve dataset definitions

\- preserve next steps



Status:

Final



\---



\## DECISION-030 - Handoff File Strategy



Decision:

Future sessions should first read:



1\. START-HERE.md

2\. PROJECT-HANDOFF.md

3\. CURRENT-STATUS.md

4\. PROJECT-DECISIONS.md

5\. NEXT-STEPS.md

6\. README.md



Status:

Final



\---



\## DECISION-031 - Repository Update Rule



Decision:

After major BuildMind work:



Update:



\- CURRENT-STATUS.md

\- NEXT-STEPS.md



If a new decision is finalized:



\- PROJECT-DECISIONS.md



If architecture or scope changes:



\- PROJECT-HANDOFF.md

\- START-HERE.md



Then commit and push to Git.



Status:

Final



\---



\## DECISION-032 - Current Research Priority



Decision:

The current main research priority is:



Construction Cost Estimation Dataset



Immediate focus:



\- work items

\- labour rates

\- material prices

\- rate analysis

\- productivity norms

\- reinforcement data

\- adjustment rules

\- source traceability



Status:

Current Priority



\---



\## Change Control Rule



Do not silently change a finalized decision.



If a finalized decision must change:



1\. Add a new decision entry.

2\. Reference the old decision.

3\. Explain why it changed.

4\. Mark the old decision as superseded.

5\. Update relevant handoff documents.

