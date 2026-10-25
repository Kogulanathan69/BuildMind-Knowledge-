\# BuildMind - Next Steps



Last Updated: 2026-10-19



This file records the immediate and upcoming tasks required to continue BuildMind from the current project state.



\---



\## 1. Current Main Priority



Current primary focus:



Construction Cost Estimation Dataset and Cost Engine Foundation.



The goal is to convert official Sri Lankan construction-rate documents into structured datasets that the BuildMind backend can query safely and consistently.



\---



\## 2. Immediate Next Step



Start with:



Northern Province Schedule of Rates 2026 - Building Works



Primary extraction targets:



\- Work item code

\- Work item description

\- Unit

\- District-wise rates

\- Labour-related values

\- Material-related values

\- Rate-analysis notes

\- Measurement notes

\- Source page

\- Effective date

\- Region

\- Amendments



\---



\## 3. Cost Dataset Files to Create



Create the following files under:



datasets/02-construction-cost/



Recommended files:



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



\## 4. First Dataset to Build



Start with:



work\_items.csv



Recommended columns:



\- work\_item\_id

\- source\_item\_code

\- category

\- work\_item\_name

\- description

\- unit

\- region

\- district

\- rate\_lkr

\- effective\_date

\- source\_document

\- source\_year

\- source\_page

\- source\_url

\- verification\_status

\- notes



\---



\## 5. Second Dataset to Build



Create:



labour\_rates.csv



Recommended columns:



\- labour\_id

\- labour\_category

\- skill\_level

\- trade

\- unit

\- hours\_per\_day

\- district

\- rate\_lkr

\- effective\_date

\- source\_document

\- source\_page

\- verification\_status

\- notes



Priority labour categories:



\- Skilled Grade I

\- Skilled Grade II

\- Semi-skilled

\- Unskilled

\- Mason

\- Carpenter

\- Electrician

\- Plumber

\- Welder

\- Tiler

\- Painter

\- Bar bender

\- Helper



\---



\## 6. Third Dataset to Build



Create:



material\_prices.csv



Recommended columns:



\- material\_id

\- category

\- material\_name

\- brand

\- specification

\- unit

\- district

\- price\_lkr

\- supplier\_or\_source

\- transport\_included

\- vat\_included

\- effective\_date

\- source\_document

\- source\_page

\- verification\_status

\- notes



Priority materials:



\- Cement

\- Sand

\- Aggregate

\- Rubble

\- Bricks

\- Cement blocks

\- Reinforcement steel

\- Binding wire

\- Roofing materials

\- Tiles

\- Paint

\- Timber

\- Aluminium

\- Glass

\- PVC

\- Plumbing materials

\- Electrical materials



\---



\## 7. Rate Analysis Dataset



Create:



resource\_coefficients.csv



Purpose:



Define how much material, labour, and equipment is required for one unit of construction work.



Recommended columns:



\- coefficient\_id

\- work\_item\_id

\- resource\_type

\- resource\_name

\- quantity\_per\_work\_unit

\- resource\_unit

\- wastage\_percentage

\- source\_document

\- source\_page

\- verification\_status

\- notes



Examples of work items:



\- 1 m³ PCC

\- 1 m³ RCC

\- 1 m² brick wall

\- 1 m² block wall

\- 1 m² plaster

\- 1 m² floor tile

\- 1 m² wall tile

\- 1 m² painting

\- 1 m² roof covering

\- 1 m² formwork



\---



\## 8. Measurement Rules Dataset



Create:



measurement\_rules.csv



Purpose:



Convert generated house geometry into BOQ quantities.



Examples:



Concrete volume:



length × width × thickness



Wall area:



wall\_length × wall\_height



Net plaster area:



wall\_area - door\_area - window\_area



Floor area:



room\_length × room\_width



Formwork area:



element face areas requiring shuttering



Recommended columns:



\- rule\_id

\- work\_category

\- rule\_name

\- formula

\- output\_unit

\- required\_inputs

\- source\_reference

\- verification\_status

\- notes



\---



\## 9. Reinforcement Dataset



Create:



reinforcement\_data.csv



Recommended fields:



\- bar\_diameter\_mm

\- weight\_kg\_per\_m

\- length\_per\_tonne

\- spacing\_mm

\- weight\_kg\_per\_m2

\- source\_document

\- source\_page

\- notes



Use official Northern Province / BSR tables where applicable.



\---



\## 10. Labour Productivity Dataset



Create:



labour\_productivity.csv



Purpose:



Estimate labour quantity from work quantity.



Examples:



\- masonry m² / labour-day

\- plastering m² / labour-day

\- tiling m² / labour-day

\- painting m² / labour-day

\- reinforcement kg / labour-day

\- formwork m² / labour-day

\- excavation m³ / labour-day



Recommended columns:



\- productivity\_id

\- work\_item

\- labour\_type

\- output\_quantity

\- output\_unit

\- time\_unit

\- productivity\_rate

\- source\_document

\- source\_page

\- verification\_status

\- notes



\---



\## 11. Adjustment Rules Dataset



Create:



adjustment\_rules.csv



Include:



\- Overhead

\- Profit

\- VAT

\- Transport

\- Loading

\- Unloading

\- Wastage

\- Sea transport

\- District adjustment

\- Contingency

\- Effective date



Recommended columns:



\- rule\_id

\- rule\_type

\- value

\- value\_type

\- applies\_to

\- region

\- effective\_date

\- source\_document

\- source\_page

\- notes



\---



\## 12. Core Residential Work Items for MVP



The first BuildMind cost engine should support:



1\. Site clearing

2\. Excavation

3\. Earth filling

4\. PCC

5\. RCC footing

6\. RCC column

7\. RCC beam

8\. RCC slab

9\. Reinforcement

10\. Formwork

11\. Brick / block masonry

12\. Plastering

13\. Floor screed

14\. Floor tiling

15\. Wall tiling

16\. Roofing

17\. Ceiling

18\. Doors

19\. Windows

20\. Painting

21\. Plumbing

22\. Sanitary fixtures

23\. Electrical

24\. Drainage

25\. External works



\---



\## 13. Admin Cost Management Module



After the datasets are structured, design the Admin module.



Admin should be able to:



\- Add work item

\- Edit work item

\- Add material price

\- Update material price

\- Add labour rate

\- Update district rate

\- Add effective date

\- Deactivate old rate

\- View price history

\- Import CSV

\- Export CSV

\- View data source

\- Verify source

\- Approve data

\- Reject data



\---



\## 14. Proposed Cost Database Tables



Future backend tables may include:



\- cost\_work\_items

\- cost\_materials

\- cost\_material\_prices

\- cost\_labour\_types

\- cost\_labour\_rates

\- cost\_resource\_coefficients

\- cost\_measurement\_rules

\- cost\_productivity

\- cost\_adjustment\_rules

\- cost\_source\_metadata

\- cost\_price\_history



\---



\## 15. Cost Calculation API



After database design, create an API concept such as:



POST /api/cost-estimate



Input example:



```json

{

&#x20; "projectId": "project-001",

&#x20; "district": "Jaffna",

&#x20; "geometry": {

&#x20;   "floorArea": 120,

&#x20;   "wallLength": 85,

&#x20;   "wallHeight": 3

&#x20; }

}

