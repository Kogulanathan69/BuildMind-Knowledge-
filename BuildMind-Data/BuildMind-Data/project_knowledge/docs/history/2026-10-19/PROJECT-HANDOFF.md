\# BuildMind - Project Handoff



\## 1. Project Identity



Project Name: BuildMind



Project Type:

AI-Powered Residential House Design and Construction Planning System



Primary Goal:

Help users generate, understand, visualize, refine, and estimate residential house designs using structured construction knowledge, deterministic planning rules, cost data, and AI assistance.



\---



\## 2. Project Scope



BuildMind is designed to support a residential-house design workflow from user requirements to preliminary planning output.



The main project scope includes:



\- User requirement collection

\- Land dimension input

\- Orientation input

\- Road direction input

\- Room count and room-type input

\- Budget input

\- User design preferences

\- Room dimension validation

\- Room adjacency validation

\- Climate-aware planning

\- Natural-light considerations

\- Ventilation considerations

\- Automatic 2D floor-plan generation

\- Multiple design alternatives

\- 3D visualization

\- Construction cost estimation

\- AI chat assistance

\- Admin-managed datasets

\- Project export



\---



\## 3. Current MVP Focus



The MVP should focus on a practical residential prototype.



Priority MVP scope:



\- Single residential house project

\- Mostly rectangular land

\- Basic room layout generation

\- Room dimension constraints

\- Room adjacency constraints

\- Orientation support

\- 2D floor-plan output

\- Basic 3D conversion

\- Basic cost estimation

\- AI-assisted user interaction

\- Admin-managed dynamic datasets



The MVP does not need:



\- Full structural engineering automation

\- Government permit automation

\- Professional certification

\- High-end photorealistic rendering

\- Full BIM replacement

\- Complex multi-building planning



\---



\## 4. Main System Roles



BuildMind currently has three major responsibility groups.



\### 4.1 User



The user can:



\- Register

\- Login

\- Create a project

\- Enter land width

\- Enter land length

\- Select project location

\- Select road side / road direction

\- Select north direction

\- Select number of floors

\- Select number of bedrooms

\- Select number of bathrooms

\- Select parking requirements

\- Enter kitchen preferences

\- Enter living-room preferences

\- Enter dining requirements

\- Enter budget

\- Select design style

\- Enter natural-light preferences

\- Enter ventilation preferences

\- Enter privacy preferences

\- Add custom requirements

\- Chat with the AI

\- Generate floor-plan alternatives

\- Compare alternatives

\- View 2D plans

\- View cost estimates

\- Request modifications

\- View 3D models

\- Save projects

\- Export results



\### 4.2 Admin



The admin is responsible for:



\- User management

\- Project monitoring

\- Room-standard management

\- Adjacency-rule management

\- Building-rule management

\- Construction-cost management

\- Labour-rate management

\- Material-price management

\- Dataset-version management

\- Architecture-style management

\- AI configuration

\- Source verification

\- Error monitoring

\- System-content management

\- Activating and deactivating outdated rates

\- Maintaining price history



\### 4.3 AI



The AI is responsible for:



\- Understanding natural-language user requests

\- Converting user requirements into structured data

\- Detecting missing information

\- Asking follow-up questions

\- Suggesting alternatives

\- Explaining why a layout was selected

\- Calling deterministic geometry engines

\- Calling calculation engines

\- Using validated datasets

\- Supporting plan refinement

\- Explaining cost-estimate results



The AI must not:



\- Invent structural engineering values

\- Invent construction prices

\- Invent legal requirements

\- Claim architectural approval

\- Claim structural safety

\- Replace deterministic quantity calculations



\---



\## 5. Proposed Technology Stack



Frontend:



\- Angular



2D Plan:



\- Konva.js

\- SVG

\- HTML Canvas



3D Visualization:



\- Three.js



Backend:



\- Python

\- FastAPI



Database:



\- PostgreSQL



AI Layer:



\- LLM for natural-language understanding

\- Structured rule engine

\- Constraint engine

\- Deterministic calculation services



Optional future tools:



\- Blender

\- MCP integrations

\- Optimization libraries

\- Advanced rendering tools



\---



\## 6. Floor-Plan Generation Flow



User Input



→ Requirement Extraction



→ Structured Project JSON



→ Missing-Data Validation



→ Room Standards



→ Adjacency Rules



→ Orientation Rules



→ Climate Rules



→ Space Planning



→ Constraint Solving



→ Layout Generation



→ Validation



→ Plan Scoring



→ Alternative Generation



→ 2D Rendering



→ Optional 3D Conversion



\---



\## 7. Current 2D Plan Data Concept



Example project input:



```json

{

&#x20; "landWidth": 40,

&#x20; "landLength": 60,

&#x20; "bedrooms": 3,

&#x20; "bathrooms": 2,

&#x20; "parking": 1,

&#x20; "preferences": \[

&#x20;   "north light",

&#x20;   "open kitchen"

&#x20; ]

}

