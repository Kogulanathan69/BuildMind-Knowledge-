&#x20;# BuildMind - Start Here



Welcome to the BuildMind project knowledge repository.



This file is the first document that any new developer, team member, AI assistant, or future ChatGPT session should read before continuing the project.



\---



\## 1. Project Name



BuildMind



\---



\## 2. Project Type



AI-Powered Residential House Design and Construction Planning System



\---



\## 3. Main Project Goal



BuildMind helps a user provide land information, room requirements, budget, orientation, preferences, and other residential design requirements.



The system then assists with:



\- Requirement understanding

\- Automatic residential floor-plan generation

\- 2D plan visualization

\- Room dimension validation

\- Room adjacency validation

\- Climate-aware planning

\- Orientation-aware planning

\- Cost estimation

\- Multiple plan alternatives

\- 3D visualization

\- AI-assisted design modification

\- Project saving and export



\---



\## 4. Main System Roles



BuildMind currently has three main responsibility groups:



\### User



The user provides:



\- Land width and length

\- Location

\- Road direction

\- North direction

\- Number of floors

\- Number of bedrooms

\- Number of bathrooms

\- Parking requirements

\- Kitchen preferences

\- Living and dining requirements

\- Budget

\- Design style

\- Natural-light preferences

\- Ventilation preferences

\- Privacy preferences

\- Other house requirements



The user can:



\- Create a new project

\- Chat with the AI assistant

\- Generate floor-plan options

\- Compare plans

\- View 2D plans

\- View cost estimates

\- Request plan changes

\- View 3D visualization

\- Save projects

\- Export final outputs



\### Admin



The admin manages:



\- Users

\- Projects

\- Room dimension standards

\- Room adjacency rules

\- Building rules

\- Construction prices

\- Labour rates

\- Cost-estimation datasets

\- Architecture styles

\- Dataset versions

\- AI configuration

\- System errors

\- Generated plans

\- Source verification



\### AI



The AI assists with:



\- Understanding natural-language user requirements

\- Converting requirements to structured JSON

\- Detecting missing information

\- Asking follow-up questions

\- Suggesting layout options

\- Explaining design decisions

\- Calling deterministic geometry and calculation engines

\- Using validated datasets

\- Supporting cost estimation

\- Supporting plan refinement



Important:



The AI must not invent structural engineering values, construction quantities, or legal approval claims.



Engineering quantities should come from validated formulas, rules, standards, and datasets.



\---



\## 5. Current User Journey



Register / Login



→ Dashboard



→ Create New Project



→ Enter Land and Location Details



→ Enter Room Requirements



→ Enter Budget and Preferences



→ AI Requirement Processing



→ Missing Information Check



→ Rule and Constraint Validation



→ Generate Multiple Floor-Plan Alternatives



→ Plan Scoring and Comparison



→ 2D Plan View



→ Cost Estimate



→ User / AI Changes



→ Revalidation



→ Final Plan Selection



→ 3D Visualization



→ Save / Export



\---



\## 6. Current Admin Journey



Admin Login



→ Dashboard



→ User Management



→ Project Management



→ Room Standards Management



→ Building Rules Management



→ Construction Cost Management



→ Labour Rate Management



→ Dataset Management



→ Architecture Style Management



→ AI Configuration



→ Error Monitoring



→ Reports and Dataset Version Management



\---



\## 7. Team Dataset Responsibilities



The BuildMind team has seven dataset research areas.



\### Member 1 - Weather / Climate Dataset



Research:



\- Temperature

\- Humidity

\- Rainfall

\- Wind direction

\- Sunlight

\- Climate region

\- Ventilation-related data

\- Natural-light-related data



\### Member 2 - Construction Cost Dataset



Research:



\- Material prices

\- Labour rates

\- Work-item rates

\- Rate analysis

\- Resource consumption

\- Labour productivity

\- Reinforcement data

\- Formwork data

\- Transport

\- Wastage

\- Overhead

\- Profit

\- VAT / tax handling

\- District-wise rates



\### Member 3 - Room Dimensions / Space Standards



Research:



\- Bedroom dimensions

\- Master bedroom

\- Bathroom

\- Kitchen

\- Living room

\- Dining

\- Corridor

\- Parking

\- Staircase

\- Store

\- Laundry

\- Minimum / preferred sizes



\### Member 4 - Room Adjacency



Research:



\- Kitchen ↔ Dining

\- Living ↔ Entrance

\- Bedroom grouping

\- Master Bedroom ↔ Attached Bathroom

\- Parking ↔ Entrance

\- Privacy relationships

\- Avoid relationships

\- Noise relationships



\### Member 5 - Building Rules / Regulations



Research:



\- Setbacks

\- Plot coverage

\- Building height

\- Road boundaries

\- Ventilation rules

\- Window requirements

\- Parking rules

\- Drainage

\- Local authority rules

\- UDA / Municipal / Urban / Pradeshiya Sabha rules



\### Member 6 - Door, Window and Furniture Dataset



Research:



\- Door sizes

\- Window sizes

\- Door swing

\- Bed sizes

\- Sofa sizes

\- Dining tables

\- Wardrobes

\- Kitchen counters

\- Toilet fixtures

\- Clearance requirements



\### Member 7 - Architecture Styles / Plan Templates



Research:



\- Modern

\- Minimalist

\- Tropical

\- Traditional Sri Lankan

\- Contemporary

\- Luxury

\- Courtyard

\- Roof styles

\- Facade styles

\- Material preferences

\- Typical room arrangements

\- Sample plan references



\---



\## 8. Current Technology Direction



Frontend:



\- Angular



2D Plan:



\- Konva.js

\- SVG / Canvas



3D Visualization:



\- Three.js



Backend:



\- Python FastAPI



Database:



\- PostgreSQL



AI:



\- Large Language Model

\- Structured rules

\- Constraint engine

\- Deterministic calculation services



Optional / Later:



\- Blender

\- MCP

\- Optimization tools

\- Advanced rendering



\---



\## 9. Floor Plan Generation Architecture



User Requirements



→ Requirement Extraction



→ Structured JSON



→ Rule Engine



→ Constraint Engine



→ Space Planning



→ Layout Generation



→ Validation



→ Plan Scoring



→ Best Plan Alternatives



→ 2D Visualization



→ 3D Visualization



\---



\## 10. Cost Estimation Architecture



The cost-estimation system must not depend on an AI model guessing prices or quantities.



Required flow:



House Geometry



→ Measurement Engine



→ Work Item / BOQ Engine



→ Rate Analysis Dataset



→ Material Quantities



→ Labour Quantities



→ Equipment Quantities



→ Current Price Database



→ Location Adjustment



→ Wastage



→ Transport



→ Overhead



→ Profit



→ VAT / Taxes



→ Final LKR Estimate



The AI should explain the result, but deterministic calculation modules should perform the actual calculations.



\---



\## 11. Construction Cost Dataset Structure



Important datasets currently planned:



1\. Work Item Dataset

2\. Measurement Rules Dataset

3\. Concrete / Mix Dataset

4\. Resource Consumption Dataset

5\. Material Price Dataset

6\. Labour Rate Dataset

7\. Labour Productivity Dataset

8\. Reinforcement Dataset

9\. Formwork Dataset

10\. Masonry Dataset

11\. Plaster / Mortar Dataset

12\. Flooring / Tiling Dataset

13\. Roofing Dataset

14\. Door / Window Dataset

15\. Plumbing Dataset

16\. Electrical Dataset

17\. Equipment Dataset

18\. Transport Dataset

19\. Wastage Dataset

20\. District / Location Dataset

21\. Overhead / Profit Dataset

22\. VAT / Tax Dataset

23\. Price History Dataset

24\. Source / Version Metadata



\---



\## 12. Important Construction Cost Sources Collected



Current research includes:



\- Northern Province Schedule of Rates 2026

\- Northern Province Building Schedule of Rates

\- Northern Province Road / Irrigation schedules

\- Northern Province labour-rate amendments

\- Department of Buildings BSR 2020

\- Department of Buildings BSR 2021

\- Department of Buildings BSR 2023

\- Department of Buildings BSR 2024

\- Central Province Schedule of Rates

\- Department of Census and Statistics price bulletins

\- Civil Engineering Handbooks

\- Civil Engineering Formula references

\- Reinforcement tables

\- Labour and productivity norms

\- CIDA / ICTAD specification references



\---



\## 13. Important Cost Estimation Decision



Dynamic construction prices must not be hard-coded permanently.



The Admin Panel should allow authorized users to:



\- Add cost items

\- Update prices

\- Update district-specific prices

\- Set effective dates

\- Activate / deactivate prices

\- Maintain price history

\- Record supplier/source details

\- Record VAT status

\- Record transport inclusion

\- Record notes



BuildMind should use the latest validated active price for the selected region.



\---



\## 14. Current BuildMind MVP Scope



The first practical MVP should focus on:



\- Single residential projects

\- Mostly rectangular land / room geometry

\- Automatic plan generation

\- Basic planning rules

\- Room dimensions

\- Room adjacency

\- Basic orientation

\- 2D plan

\- Simple 3D conversion

\- Cost estimation

\- AI chat support

\- Admin-managed datasets



Advanced structural engineering and permit automation are not MVP requirements.



\---



\## 15. Important Project Rules



Do not:



\- Let the AI invent structural values

\- Let the AI invent construction prices

\- Treat old price data as current without versioning

\- Claim government approval

\- Claim professional architectural certification

\- Claim structural safety without professional validation

\- Replace finalized project decisions without documenting the change



\---



\## 16. Repository Reading Order



Before continuing BuildMind, read these files in this order:



1\. START-HERE.md

2\. PROJECT-HANDOFF.md

3\. CURRENT-STATUS.md

4\. PROJECT-DECISIONS.md

5\. NEXT-STEPS.md

6\. README.md



Then inspect the relevant dataset, document, source, or prompt folders.



\---



\## 17. Future ChatGPT / AI Handoff Instruction



When this repository is given to another AI assistant, use this instruction:



"Read START-HERE.md, PROJECT-HANDOFF.md, CURRENT-STATUS.md, PROJECT-DECISIONS.md, and NEXT-STEPS.md first. Understand the current BuildMind architecture, finalized decisions, dataset responsibilities, current research state, and pending work. Continue from the documented current state. Do not redesign finalized decisions unless explicitly requested."



\---



\## 18. Current Main Research Focus



Current focus:



Construction Cost Estimation Dataset



Priority tasks:



\- Extract building work items

\- Extract labour rates

\- Extract material rates

\- Extract district-wise rates

\- Extract rate-analysis data

\- Extract productivity norms

\- Extract reinforcement data

\- Extract cost adjustment rules

\- Convert official documents into structured datasets

\- Prepare admin-manageable dynamic pricing



\---



\## 19. Project Continuity Rule



Every major BuildMind update should also update:



\- CURRENT-STATUS.md

\- NEXT-STEPS.md



If a new decision is made:



\- PROJECT-DECISIONS.md



If the overall architecture or scope changes:



\- PROJECT-HANDOFF.md

\- START-HERE.md



Then commit and push the changes to Git.

