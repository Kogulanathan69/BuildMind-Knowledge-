\# BuildMind Knowledge Repository



BuildMind is an AI-powered residential house design and construction planning system.



This repository stores the project's knowledge, research, decisions, datasets, source documents, architecture notes, prompts, current progress, and future handoff information.



\## Main Goals



BuildMind aims to help users:



\- Enter land dimensions and house requirements

\- Generate residential floor plan alternatives

\- Apply room dimension and adjacency rules

\- Consider orientation, climate, lighting, ventilation, and user preferences

\- Generate 2D floor plans

\- Convert plans to 3D visualization

\- Estimate construction cost

\- Compare multiple design options

\- Interact with an AI assistant

\- Export project results and reports



\## Main System Roles



\### User

The user provides:

\- Land dimensions

\- Location

\- Number of rooms

\- Budget

\- Preferences

\- Orientation

\- Parking requirements

\- Design style



The user can:

\- Generate plans

\- Compare options

\- Edit or request changes

\- View cost estimates

\- View 2D and 3D outputs

\- Save and export projects



\### Admin

The admin manages:

\- Users

\- Projects

\- Room standards

\- Building rules

\- Construction prices

\- Labour rates

\- Dataset versions

\- Architecture templates

\- Cost estimation data

\- AI configuration

\- System monitoring



\### AI

The AI is responsible for:

\- Understanding user requirements

\- Converting natural language into structured data

\- Detecting missing information

\- Generating plan alternatives

\- Applying planning rules

\- Explaining design choices

\- Calling deterministic calculation modules

\- Assisting with cost estimation



The AI must not guess engineering quantities or claim professional certification.



\## Team Dataset Areas



1\. Weather / Climate Dataset

2\. Construction Cost Dataset

3\. Room Dimensions / Space Standards

4\. Room Adjacency

5\. Building Rules / Regulations

6\. Door, Window and Furniture Dimensions

7\. Architecture Styles / Plan Templates



\## Current Technology Direction



\- Frontend: Angular

\- 2D Plan: Konva.js / SVG / Canvas

\- 3D Visualization: Three.js

\- Backend: Python FastAPI

\- Database: PostgreSQL

\- AI: LLM + structured rule engine

\- Optimization: Constraint-based layout generation

\- Optional later tools: Blender / MCP



\## Cost Estimation Architecture



House Geometry

→ Measurement Engine

→ Work Item / BOQ Engine

→ Rate Analysis Dataset

→ Material + Labour + Equipment Quantities

→ Current Price Database

→ Location / Wastage / Transport Adjustments

→ Overhead + Profit + VAT

→ Final LKR Estimate



\## Important Sri Lankan Sources



The project uses and researches sources such as:



\- Northern Province Schedule of Rates

\- Department of Buildings BSR

\- CIDA / ICTAD specifications

\- Department of Census and Statistics price bulletins

\- Provincial labour and material rate schedules

\- Civil engineering calculation references



\## Repository Purpose



This repository is the central handoff point for BuildMind.



Any future developer, team member, or ChatGPT session should first read:



1\. START-HERE.md

2\. PROJECT-HANDOFF.md

3\. CURRENT-STATUS.md

4\. PROJECT-DECISIONS.md

5\. NEXT-STEPS.md



Do not redesign finalized project decisions without reviewing PROJECT-DECISIONS.md.

