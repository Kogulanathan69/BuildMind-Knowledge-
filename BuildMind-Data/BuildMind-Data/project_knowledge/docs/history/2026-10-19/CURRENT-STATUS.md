\# BuildMind - Current Status



Last Updated: 2026-10-19



\## Current Project Phase



BuildMind is currently in the research, dataset preparation, architecture definition, and prototype-planning phase.



The current main focus is:



Construction Cost Estimation Dataset and Cost Engine Design.



\---



\## Completed



\- Project name finalized as BuildMind.

\- Main project scope defined.

\- User, Admin, and AI responsibilities defined.

\- Seven-member dataset research split defined.

\- Initial user journey defined.

\- Initial admin journey defined.

\- AI responsibility boundaries defined.

\- Angular selected for frontend.

\- Python FastAPI selected for backend direction.

\- PostgreSQL selected for database direction.

\- Three.js selected for browser-based 3D visualization.

\- 2D-to-3D prototype direction defined.

\- Cost estimation architecture defined.

\- Dynamic pricing approach finalized.

\- Admin-managed price updates decided.

\- Price-history requirement identified.

\- District-wise pricing requirement identified.

\- AI must not guess engineering quantities or prices.

\- Knowledge repository created and pushed to GitHub.



\---



\## Construction Cost Research Completed



Collected / identified sources include:



\- Northern Province Schedule of Rates 2026

\- Northern Province Building Works Schedule

\- Northern Province Road Works Schedule

\- Northern Province Irrigation Works Schedule

\- Northern Province Material Testing Schedule

\- Northern Province labour-rate amendments

\- Northern Province second-half rate updates

\- Department of Buildings BSR 2020

\- Department of Buildings BSR 2021

\- Department of Buildings BSR 2023

\- Department of Buildings BSR 2024

\- Central Province Schedule of Rates

\- Department of Census and Statistics retail and producer price bulletin

\- Civil Engineering Handbooks

\- Civil Engineering Formula references

\- Reinforcement-weight tables

\- Labour and productivity-related norms

\- CIDA / ICTAD specification references



\---



\## Useful Cost Data Already Identified



Current sources provide useful data for:



\- Material prices

\- Labour rates

\- District-wise labour variation

\- Work-item rates

\- Reinforcement weights

\- Reinforcement spacing data

\- Overhead

\- Profit

\- VAT treatment

\- Transport treatment

\- Wastage treatment

\- Building work categories

\- Electrical work rates

\- Plumbing work rates

\- Irrigation productivity norms

\- Material-testing rates



\---



\## Cost Estimation Architecture



House Geometry



→ Measurement Engine



→ Work Item / BOQ Engine



→ Rate Analysis Dataset



→ Material Quantities



→ Labour Quantities



→ Equipment Quantities



→ Current Price Database



→ District / Location Adjustment



→ Wastage



→ Transport



→ Overhead



→ Profit



→ VAT / Tax



→ Final LKR Estimate



\---



\## Cost Datasets Planned



\- work\_items.csv

\- measurement\_rules.csv

\- resource\_coefficients.csv

\- material\_prices.csv

\- labour\_rates.csv

\- labour\_productivity.csv

\- reinforcement\_data.csv

\- formwork\_data.csv

\- masonry\_data.csv

\- finishing\_data.csv

\- plumbing\_data.csv

\- electrical\_data.csv

\- equipment\_rates.csv

\- transport\_rates.csv

\- adjustment\_rules.csv

\- source\_metadata.csv



\---



\## Current Missing / Incomplete Cost Data



Still needs extraction or research:



\- Detailed rate-analysis coefficients

\- 1 m³ concrete resource breakdowns

\- Concrete mix / grade mapping

\- RCC resource breakdown

\- Formwork coefficients

\- Masonry resource consumption

\- Plaster resource consumption

\- Flooring and tiling consumption rules

\- Roofing resource breakdown

\- Door / window cost structure

\- Plumbing detailed resource breakdown

\- Electrical detailed resource breakdown

\- Labour productivity for building work

\- Equipment productivity and rates

\- BOQ generation rules

\- Measurement formulas linked to work items



\---



\## Current Dataset Team Structure



\### Member 1

Weather / Climate Dataset



\### Member 2

Construction Cost Dataset



\### Member 3

Room Dimensions / Space Standards



\### Member 4

Room Adjacency



\### Member 5

Building Rules / Regulations



\### Member 6

Door / Window / Furniture Dimensions



\### Member 7

Architecture Styles / Plan Templates



\---



\## Current Prototype Direction



Input examples:



\- land width

\- land length

\- bedrooms

\- bathrooms

\- parking

\- budget

\- orientation

\- road direction

\- design preferences



Output direction:



\- structured JSON

\- 2D floor plan

\- doors

\- windows

\- dimensions

\- north arrow

\- multiple alternatives

\- basic cost estimate

\- 3D visualization



\---



\## Current Priority



Priority 1:

Extract structured data from Northern Province Building Schedule of Rates 2026.



Priority 2:

Create the first Construction Cost Dataset tables.



Priority 3:

Create resource coefficients for core residential work items.



Priority 4:

Design the Admin Cost Management database structure.



Priority 5:

Design the deterministic Cost Calculation API.



\---



\## Immediate Next Work Items



1\. Extract work items from Building SOR / BSR.

2\. Extract labour rates.

3\. Extract material prices.

4\. Extract reinforcement data.

5\. Extract productivity norms.

6\. Define rate-analysis table structure.

7\. Create initial CSV / Excel datasets.

8\. Link each row to source document, year, region, and page.

9\. Define admin update workflow.

10\. Define cost calculation formula flow.



\---



\## Important Current Rule



Do not move directly into AI model training.



First create:



\- clean structured datasets

\- deterministic formulas

\- validated source mapping

\- calculation logic



Then connect the AI as the explanation and orchestration layer.



\---



\## Current Repository Status



Knowledge repository:



BuildMind-Knowledge-



Main knowledge files:



\- README.md

\- START-HERE.md

\- PROJECT-HANDOFF.md

\- CURRENT-STATUS.md

\- PROJECT-DECISIONS.md

\- NEXT-STEPS.md



The repository is intended to support continuity across different ChatGPT sessions, computers, and team members.

