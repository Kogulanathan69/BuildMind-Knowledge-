# Member 3 room dimensions: consolidation and provenance audit

Prepared 26 October 2026 by Claude (AI assistant) at the project owner's request. **This is an internal-consistency and provenance audit. It is not a legal, architectural or engineering review, and it does not verify any number against the Gazette PDF or establish current applicability.**

Policy applied: Sri Lankan statutory sources only (DECISION-033); no value invented; no foreign code used to fill a gap; "text verified" is never converted to "currently applicable" (all rows carry `applicability_status = PENDING`).

## 1. Scope, method and limits

- **Input:** the 14 files in `datasets/03_room_dimensions/recovered_versions/` (13 workbooks and 1 CSV). They were opened read-only; their SHA-256 hashes were recorded before work and re-checked after (section 3).
- **Consolidated:** every rule-bearing sheet (12 sheets in 9 files). Each sheet row, or each metric cell where a row carries several metrics, became one consolidated row with its origin workbook, sheet, row and cell.
- **Not consolidated:** 51 other sheets (484 data rows): READMEs, source registers, gap lists, test examples, backlogs, concept/prototype sizes, research-paper data and plan-image observations. Every one is listed with its reason in section 4.
- **Version order:** the files carry stage numbers (Starter, Extract/Stage2, Stage4, Stage5, Stage6, Stage9); `Gazette_Verified_Dataset` has none. All 14 files have the same file-system creation time (2026-10-25 19:03:28, the recovery copy), so **no chronology is inferred from file dates**.
- **Normalisation:** `subject_norm`, `parameter_norm`, units and clause references were mapped with an explicit dictionary. The builder stops on any unmapped term, so nothing was guessed. Raw origin text is preserved in `origin_*` columns.
- **Limits:** the primary Gazette PDF (2235/54, 8 July 2021) was not available to this audit, and uda.gov.lk is not reachable from the audit environment. No amendment, local-authority or development-plan check was possible. No reviewer is recorded in any origin file.

## 2. Files created

All in `datasets/03_room_dimensions/consolidated/`:

| File | Purpose |
|---|---|
| `member3_consolidated_rules.csv` | 262 rows, one per rule value, 54 columns, full provenance |
| `member3_cross_version_comparison.csv` | 61 rows, one per comparison key, values and citations across versions |
| `member3_audit_report.md` | this report |
| `validate_member3.py` | re-runnable integrity checks (read-only) |

Also updated (as requested): `CURRENT-STATUS.md` and `NEXT-STEPS.md` in the repository root. Nothing else was changed. The nested copies under `BuildMind-Data/BuildMind-Data/project_knowledge/` were left untouched and are now older than the root files.

## 3. Hash verification of the originals

**Result: IDENTICAL.** All 14 originals have an identical SHA-256 before and after the work (full list in Appendix A). `validate_member3.py` embeds the manifest and re-checks it on every run.

## 4. Inventory and row-count reconciliation

Every sheet of every original is classified. "Rows" are non-empty data rows (header excluded).

| Original file | Sheet | Rows | Disposition | Consolidated values |
|---|---|---:|---|---:|
| M3_Final_4_Paper_Research_Dataset | Source_Register | 4 | excluded: research_literature_non_statutory | 0 |
| M3_Final_4_Paper_Research_Dataset | Room_Dimensions | 4 | excluded: research_literature_non_statutory | 0 |
| M3_Final_4_Paper_Research_Dataset | Zone_Configurations | 21 | excluded: research_literature_non_statutory | 0 |
| M3_Final_4_Paper_Research_Dataset | Design_Findings | 14 | excluded: research_literature_non_statutory | 0 |
| M3_Final_4_Paper_Research_Dataset | Legal_Separation | 4 | excluded: research_literature_non_statutory | 0 |
| M3_Final_4_Paper_Research_Dataset | Research_Gaps | 6 | excluded: research_literature_non_statutory | 0 |
| M3_Final_4_Paper_Research_Dataset | README | 10 | excluded: research_literature_non_statutory | 0 |
| M3_Gazette_Verified_Dataset | Verified_2021_Rules | 57 | **consolidated** (row) | 57 |
| M3_Gazette_Verified_Dataset | AI_Validation_Examples | 3 | excluded: illustrative_test_cases | 0 |
| M3_Gazette_Verified_Dataset | Read_Me | 8 | excluded: readme_metadata | 0 |
| M3_Research_Starter | UDA_Minimums | 8 | **consolidated** (unpivot) | 15 |
| M3_Research_Starter | Research_Backlog | 18 | excluded: backlog_template | 0 |
| M3_Research_Starter | Sources | 3 | excluded: source_register | 0 |
| M3_Research_Starter | README | 8 | excluded: readme_metadata | 0 |
| M3_Sri_Lanka_Room_Standards_Extract | SL_Verified_Extract | 38 | **consolidated** (row) | 38 |
| M3_Sri_Lanka_Room_Standards_Extract | README | 11 | excluded: readme_metadata | 0 |
| M3_Sri_Lanka_Room_Standards_Extract | Research_Gaps | 7 | excluded: research_gaps | 0 |
| M3_Sri_Lanka_Room_Standards_Stage2 | SL_Verified_Extract | 38 | **consolidated** (row) | 38 |
| M3_Sri_Lanka_Room_Standards_Stage2 | README | 11 | excluded: readme_metadata | 0 |
| M3_Sri_Lanka_Room_Standards_Stage2 | Research_Gaps | 7 | excluded: research_gaps | 0 |
| M3_Sri_Lanka_Room_Standards_Stage2 | Lighting_Ventilation | 33 | **consolidated** (row) | 33 |
| M3_Sri_Lanka_Room_Standards_Stage2 | AI_Validation_Examples | 3 | excluded: illustrative_test_cases | 0 |
| M3_Stage3_Concept_Layout_Validation | Concept_Room_Sizes | 8 | excluded: prototype_assumption_concept | 0 |
| M3_Stage3_Concept_Layout_Validation | Furniture_Placeholders | 6 | excluded: prototype_assumption_concept | 0 |
| M3_Stage3_Concept_Layout_Validation | AI_Validation_Rules | 7 | excluded: validation_logic_not_data | 0 |
| M3_Stage3_Concept_Layout_Validation | Concept_Calculator | 3 | excluded: prototype_assumption_concept | 0 |
| M3_Stage3_Concept_Layout_Validation | README | 7 | excluded: readme_metadata | 0 |
| M3_Stage4_Verified_Research | Verified_Reference_Rules | 21 | **consolidated** (row) | 21 |
| M3_Stage4_Verified_Research | Design_Research_Backlog | 8 | excluded: research_backlog | 0 |
| M3_Stage4_Verified_Research | AI_Validation_Test_Cases | 6 | excluded: illustrative_test_cases | 0 |
| M3_Stage4_Verified_Research | README_Sources | 9 | excluded: readme_metadata | 0 |
| M3_Stage5_Sri_Lanka_Compliance_Research | Source_Register | 4 | excluded: source_register | 0 |
| M3_Stage5_Sri_Lanka_Compliance_Research | Rule_Verification | 10 | **consolidated** (row) | 10 |
| M3_Stage5_Sri_Lanka_Compliance_Research | Jurisdiction_Check | 7 | excluded: process_checklist | 0 |
| M3_Stage5_Sri_Lanka_Compliance_Research | AI_Rule_Schema | 13 | excluded: schema_definition | 0 |
| M3_Stage5_Sri_Lanka_Compliance_Research | Validation_Examples | 3 | excluded: illustrative_test_cases | 0 |
| M3_Stage5_Sri_Lanka_Compliance_Research | Open_Research_Tasks | 8 | excluded: process_checklist | 0 |
| M3_Stage5_Sri_Lanka_Compliance_Research | README | 5 | excluded: readme_metadata | 0 |
| M3_Stage6_Gazette_Verification_Audit | Rule_Audit | 10 | **consolidated** (row) | 10 |
| M3_Stage6_Gazette_Verification_Audit | Source_Evidence | 5 | excluded: source_register | 0 |
| M3_Stage6_Gazette_Verification_Audit | Legal_Gates | 6 | excluded: process_checklist | 0 |
| M3_Stage6_Gazette_Verification_Audit | Engine_Decisions | 3 | excluded: illustrative_test_cases | 0 |
| M3_Stage6_Gazette_Verification_Audit | Next_Actions | 5 | excluded: process_checklist | 0 |
| M3_Stage6_Gazette_Verification_Audit | README | 6 | excluded: readme_metadata | 0 |
| M3_Stage9_Gazette_Text_Verified | Room_Legal_Source | 7 | **consolidated** (unpivot) | 14 |
| M3_Stage9_Gazette_Text_Verified | Stairs_Legal_Source | 2 | **consolidated** (unpivot) | 8 |
| M3_Stage9_Gazette_Text_Verified | Room_Heights | 2 | **consolidated** (unpivot) | 3 |
| M3_Stage9_Gazette_Text_Verified | Research_Gaps | 5 | excluded: research_gaps | 0 |
| M3_Stage9_Gazette_Text_Verified | Source_Register | 1 | excluded: source_register | 0 |
| M3_Stage9_Gazette_Text_Verified | README | 5 | excluded: readme_metadata | 0 |
| M3_room_standards (csv) | (csv) | 8 | **consolidated** (unpivot) | 15 |
| NBRO_Reference_Plan_Extraction_v1 | Drawing_Register | 14 | excluded: plan_observations_examples | 0 |
| NBRO_Reference_Plan_Extraction_v1 | Room_Extraction | 60 | excluded: plan_observations_examples | 0 |
| NBRO_Reference_Plan_Extraction_v1 | Opening_Samples | 14 | excluded: plan_observations_examples | 0 |
| NBRO_Reference_Plan_Extraction_v1 | Data_Rules | 9 | excluded: readme_metadata | 0 |
| Stage8_2_Updated_Room_Dimensions | Plan_Register | 9 | excluded: plan_observations_examples | 0 |
| Stage8_2_Updated_Room_Dimensions | Room_Extracts | 33 | excluded: plan_observations_examples | 0 |
| Stage8_2_Updated_Room_Dimensions | Review_Queue | 9 | excluded: plan_observations_examples | 0 |
| Stage8_2_Updated_Room_Dimensions | Data_Rules | 12 | excluded: readme_metadata | 0 |
| Stage8_Sri_Lankan_Floor_Plans_Initial_Extraction | Plan_Register | 9 | excluded: plan_observations_examples | 0 |
| Stage8_Sri_Lankan_Floor_Plans_Initial_Extraction | Room_Extracts | 24 | excluded: plan_observations_examples | 0 |
| Stage8_Sri_Lankan_Floor_Plans_Initial_Extraction | Review_Queue | 9 | excluded: plan_observations_examples | 0 |
| Stage8_Sri_Lankan_Floor_Plans_Initial_Extraction | Data_Rules | 10 | excluded: readme_metadata | 0 |

**Reconciliation:** the validator recounts origin values independently. 262 origin values in 12 rule sheets equal 262 consolidated rows, sheet by sheet. Sheets with several metrics per row (Stage 9 and Starter/CSV) expand: Starter/CSV 8 rows → 15 values (the stair row has no area); Stage 9 Room_Legal_Source 7 rows → 14; Stairs 2 → 8; Room_Heights 2 → 3 (the second row has only a lowest-point value). Excluded sheets are never counted as rules.

Exclusion notes: `Final_4_Paper` `Room_Dimensions` holds RESEARCH_ONLY / NOT_LEGAL_MINIMUM simulation inputs citing a non-Sri-Lankan reference (Neufert). They are excluded and **must not be used to fill Sri Lankan rule gaps**. `Research_Backlog` (Starter) has empty value cells. `Stage3` values are DESIGN_HEURISTIC, flagged by the origin as not legal minima. NBRO and Stage 8 data are plan observations (examples), not rules.

## 5. Rule counts

**262 consolidated rule values** in **61 unique comparison keys** (a key = parameter + subject + context, e.g. kitchen minimum floor area, airwell area for height band 7-15 m).

| Origin version | Sheet | Values |
|---|---|---:|
| M3_Research_Starter | UDA_Minimums | 15 |
| M3_room_standards (csv) | (csv) | 15 |
| M3_Sri_Lanka_Room_Standards_Extract | SL_Verified_Extract | 38 |
| M3_Sri_Lanka_Room_Standards_Stage2 | Lighting_Ventilation | 33 |
| M3_Sri_Lanka_Room_Standards_Stage2 | SL_Verified_Extract | 38 |
| M3_Stage4_Verified_Research | Verified_Reference_Rules | 21 |
| M3_Stage5_Sri_Lanka_Compliance_Research | Rule_Verification | 10 |
| M3_Stage6_Gazette_Verification_Audit | Rule_Audit | 10 |
| M3_Stage9_Gazette_Text_Verified | Room_Heights | 3 |
| M3_Stage9_Gazette_Text_Verified | Room_Legal_Source | 14 |
| M3_Stage9_Gazette_Text_Verified | Stairs_Legal_Source | 8 |
| M3_Gazette_Verified_Dataset | Verified_2021_Rules | 57 |

By topic (first word of `parameter_norm`): min 159, airwell 47, stair 34, window 8, handrail 2, dwelling 2, kitchen 2, room 2, balcony 2, toilet 2, terrace 2. "min" covers room areas/widths and heights; "airwell" Schedule 9; "stair" Schedule 8; "window" Regulation 70(3).

Duplicates are intentional: the same rule appears once per version that records it, so provenance is kept per version. `Extract` and `Stage2 SL_Verified_Extract` are identical on all 38 rows (values, clause, page, status).

## 6. Verified versus pending counts

"Verified" below means only that **the originating workbook states** it transcribed or verified the 2021 Gazette text. This audit did not repeat that check (`independent_pdf_check_by_this_audit = NOT_PERFORMED` on all rows).

| Status (all 262 rows) | Rows |
|---|---:|
| text: TEXT_VERIFIED_PER_ORIGIN | 115 |
| text: SOURCE_EXTRACTED | 97 |
| text: PENDING_TEXT_RECHECK | 10 |
| text: NOT_VERIFIED | 10 |
| text: NOT_STATED | 30 |
| **applicability: PENDING** | **262** |
| applicability: confirmed / currently applicable | **0** |
| reviewer: NOT_RECORDED | 262 |
| independent PDF check by this audit: NOT_PERFORMED | 262 |
| severity (hard/soft): NOT_ASSIGNED | 262 |

By origin version:

| Version | text verified per origin | source-extracted | pending recheck | not verified | not stated |
|---|---:|---:|---:|---:|---:|
| Starter | 0 | 0 | 0 | 0 | 15 |
| CSV | 0 | 0 | 0 | 0 | 15 |
| Extract | 0 | 38 | 0 | 0 | 0 |
| Stage2 | 33 | 38 | 0 | 0 | 0 |
| Stage4 | 0 | 21 | 0 | 0 | 0 |
| Stage5 | 0 | 0 | 10 | 0 | 0 |
| Stage6 | 0 | 0 | 0 | 10 | 0 |
| Stage9 | 25 | 0 | 0 | 0 | 0 |
| GazetteVerified | 57 | 0 | 0 | 0 | 0 |

By comparison key: **58 of 61** keys have at least one version whose origin states text verification. **3 keys have none**: minimum water closets (Regulation 75(1)), non-public building handrail height (68(2)(a)) and kitchen sink required (75(4)); all three appear only in `Stage2` as "source-extracted".

Rule IDs are `regulation` candidates only. `rule_type` is `regulation` for all rows because every row transcribes a Gazette or UDA-regulation provision; `severity` (hard/soft) is **not** assigned by any origin file and is left `NOT_ASSIGNED` rather than guessed.

## 7. Cross-version findings

### 7.1 Numeric values: 0 conflicts

Across all 61 keys, 54 are CONSISTENT (same value in every version that records them, compared in SI units), 7 are SINGLE_ORIGIN (recorded in one version only) and **0 conflict**. The Schedule 7 minima, Regulation 67 heights, Regulation 70(3) ratios and the Schedule 8/9 values agree wherever more than one version records them.

### 7.2 Units

24 rows are stated in millimetres (stair width, riser, tread) and are compared in metres. The Starter/CSV state the stair width as 0.75 m while the other versions state 750 mm; equal after conversion. Ratio units use several labels ("floor area fraction", "fraction of room floor area", "floor area ratio"); all map to `ratio` with a stated basis.

### 7.3 Citations (information, not value conflicts)

- **Printed-page notation differs:** `Extract`/`Stage2` cite page **123** for Schedules 7 and 8 and **19** for Regulation 67, while `Stage9` cites **123A** and **19A**. 25 keys carry this variant. Without the PDF it cannot be said whether these are the same page. `Stage2`'s own README says the field holds the printed number "e.g. 123A", yet its rows contain 123; that is an internal inconsistency to resolve against the PDF.
- **Clause granularity differs:** some versions cite only "Schedule 7", others "Schedule 7; Regulations 65 and 75" (41 keys). Not a conflict; the narrower citation is less complete.
- **No page is given at all** in `GazetteVerified` (57 rows), `Stage4` (21), `Stage5` (10), `Stage6` (10), `Starter` (15) and `CSV` (15).

### 7.4 Rule-ID reuse (do not join versions on Rule_ID)

The same ID means different rules in different versions. `SL-R02` to `SL-R07` identify per-metric rows in `Stage5`/`Stage6` (for example `SL-R04` = first habitable room, minimum width 2.5 m) but per-room rows in `Stage9` (`SL-R04` = Kitchen, 5.5 m² and 1.8 m). 24 rows are flagged `ID_REUSED_FOR_DIFFERENT_RULE_IN_OTHER_VERSION`. Cross-version joins in this audit use the normalised comparison key instead. `SL-R01` is only a granularity difference. Other ID families (`SL-S7-*`, `UDA-ROOM-*`, `KITCHEN-AREA`, `SL-UDA-*`) are unique to one version.

### 7.5 Terminology drift

28 rows (`Starter`, `CSV`, `Stage5`, `Stage6`) label Schedule 7 categories as "single / first / additional **habitable** room". The Gazette wording recorded in `Stage9` is "Where there is only one room in a dwelling unit", "First Room (more than 1 room in dwelling unit)" and "Additional Room (...)". Several origin files warn not to equate these with bedrooms or a master bedroom. The audit maps all variants to `dwelling_single_room`, `dwelling_first_room`, `dwelling_additional_room` for comparison only, and flags `TERM_VARIANT_HABITABLE_NOT_GAZETTE_WORDING`. Likewise Regulation 70(3) is labelled "habitable rooms" in `Stage5`/`Stage6` and "Room with natural light/ventilation" elsewhere.

### 7.6 Parameter-label variant (Regulation 67(1)(b))

`Extract`, `Stage2`, `Stage4` and `GazetteVerified` record the 2.2 m height for bathrooms, lavatories, water closets, verandas, balconies, terraces and garages as "minimum height". `Stage9` records the same 2.2 m under "Min height at lowest point m". The value agrees; the label differs, and which label matches the Gazette text cannot be decided without the PDF.

### 7.7 Status disagreement between versions

10 keys (the Schedule 7 room minima for single/first/additional room and kitchen, and the Regulation 70(3) ratios) are "NOT_VERIFIED" (`Stage6`: exact clause not verified, engine BLOCKED) or "PENDING_TEXT_RECHECK" (`Stage5`) in earlier versions but "text verified" in `Stage9` and `GazetteVerified`. Taken by stage number this reads as progress, but file dates cannot confirm the order, and `Stage6` and `Stage5` still show the blocking statuses. The audit keeps every version's status and does not resolve the disagreement.

### 7.8 Coverage differences

`GazetteVerified` (57 values) and `Stage2` (71 values) overlap on Schedule 7, Regulation 67, Regulation 70(3), Regulation 71(5), Schedule 8 (one stair category) and Schedule 9. 14 keys are in `Stage2` but not `GazetteVerified`: the public/condominium stair category (4 keys, also in `Stage9`), handrail height, minimum water closets, kitchen sink, Regulation 70(6)/(7) distances, terrace-house vent rules and the air-well projection limit. No key is in `GazetteVerified` only. `GazetteVerified` Read_Me states that the 75 m+ all-room air-well **area** is formula-based and deliberately not encoded as a fixed threshold; no version records it as a number.

### 7.9 Source identity

`Starter` and `CSV` cite a different PDF address (`Planning and Development Regulations.pdf`) with no edition or date, and call it "Schedule 7/8". Their numbers match the 2235/54 values, but **nothing in those files shows they come from Gazette 2235/54**, so `source_year` is left blank and flagged `SOURCE_EDITION_NOT_STATED` (30 rows). The `CSV` duplicates the `Starter` `UDA_Minimums` sheet (15 values each).

## 8. Missing fields and data

### 8.1 Missing fields in the consolidated rows

| Field | Rows missing | Where |
|---|---:|---|
| printed page | 128 | GazetteVerified 57, Stage4 21, Starter 15, CSV 15, Stage5 10, Stage6 10 |
| clause / provision | 10 | Stage6 (all 10 rows) |
| source year | 30 | Starter 15, CSV 15 (edition not stated) |
| operator stated in origin | 181 implied from the metric name, 3 not applicable | operator filled as `>=` / `<=` only where the metric says minimum/maximum (`operator_basis` says which) |
| source URL stated in row | 166 | URL appears in 61 rows; 35 more are taken from the workbook's own source register (Stage6, Stage9) and marked as such |
| severity hard/soft | 262 | not assigned by any origin file |
| reviewer | 262 | no reviewer recorded in any origin file |

### 8.2 Data the origin files themselves record as missing or unresolved

Quoted from the origin sheets (not verified by this audit):

- **Preferred room sizes:** NOT_FOUND (Stage9 Research_Gaps). "Master bedroom recommended sizes: Not in extracted clauses" (Stage2 Research_Gaps).
- **Living and dining room sizes:** UNRESOLVED; needs qualified architect review (Stage9).
- **Circulation clearances:** NOT_VERIFIED (Stage9). Furniture clearance is separate Member 6 research (Stage2).
- **Room length / aspect ratio:** not in Schedule 7; area and width do not prescribe length (Stage2).
- **Current legal applicability:** amendments, jurisdiction, development plan: PENDING / unverified (Stage9, Stage2, Stage6 Legal_Gates G03 to G06).
- **Additional room types** (parking, utility, veranda, prayer, store, stair) as measured Sri Lankan evidence: PENDING (Final_4_Paper Research_Gaps).
- **Nine floor plans:** high-resolution measurement verification PARTIAL (Stage9).
- **Climate and orientation:** separate Member 1 work.

Per the project rule, none of these gaps was filled. No international code, simulation input or placeholder value was used.

## 9. External verification still pending

1. Compare every value, clause and printed page with the primary Gazette 2235/54 (8 July 2021) PDF; resolve the 123/123A, 19/19A and Regulation 67(1)(b) label questions.
2. Check later gazettes and amendments. `Stage6` records, as an origin note not verified here: Gazette 2306/46 (2022) is "not a room-size amendment", a UDA review of the 2021 regulations is underway ("review, not enactment"), and "My Zone UDA" covers gazetted plans in Colombo and Gampaha only ("do not assume Jaffna or island-wide coverage").
3. Confirm UDA-declared jurisdiction and the applicable development plan for the pilot locality (Stage6 gates G04, G05).
4. Obtain qualified architect interpretation of the Schedule 7 categories ("first" / "additional" room) before mapping them to named rooms.
5. Record a reviewer. Until then `reviewer_status = NOT_RECORDED` and `applicability_status = PENDING` on every row.

## 10. Validation results

Output of `python validate_member3.py` run after the files were written:

```text
Member 3 validation  (originals: /home/claude/know/BuildMind-Data/BuildMind-Data/datasets/03_room_dimensions/recovered_versions)

PASS  1 original files present (14 expected)
PASS  1 no unexpected files beside originals (outside consolidated/)
PASS  1 SHA-256 of every original equals the pre-consolidation manifest  -> 14/14 identical
PASS  2 every sheet of every original is classified (63 sheets)
PASS  3 per-sheet reconciliation: origin value count == consolidated rows (12 rule sheets)
PASS  3 total reconciliation: 262 expected == 262 consolidated
PASS  3 no consolidated row originates from an excluded/unknown sheet
      (info) 51 sheets / 484 data rows are excluded as non-rule data; see audit report
PASS  4 required fields non-empty on all rows
PASS  4 consolidated_id unique and sequential
PASS  4 applicability_status is PENDING on every row (text verified != currently applicable)
PASS  4 text_verification_status within allowed set
PASS  4 reviewer_status NOT_RECORDED on every row (no origin file records a reviewer)
PASS  4 severity NOT_ASSIGNED on every row (origin does not assign hard/soft)
PASS  4 independent PDF check is NOT_PERFORMED on every row
PASS  4 missing clause/page are explicitly flagged (no silent blanks)
PASS  4 operator blank only where origin gives none and metric is a flag/threshold
PASS  5 units belong to the allowed set
PASS  5 parameter/unit compatibility (area=m2, lengths=m, ratios=ratio, ...)
PASS  5 value_si recomputed from value and unit (mm -> m x0.001)
      (info) 24 rows were stated in mm and are compared in metres
PASS  5 maximum-type parameters use operator <= (no min/max inversion)
PASS  6 source traceability: every row re-matches its origin cell (id, value, subject, unit, metric)  -> 262/262 rows verified against originals
PASS  7 comparison CSV has one row per comparison key, no duplicates
PASS  7 comparison CSV statuses/counts equal an independent recomputation
PASS  7 comparison rows cover all consolidated rows
      (finding) value conflicts across versions: 0 []
      (finding) comparison keys: 54 consistent, 7 single-origin, 0 conflict
PASS  8 no foreign-code/standard reference in source fields
      (info) foreign-reference words in origin note fields on 0 rows []

SUMMARY: 25 checks, 25 passed, 0 failed
```

Negative testing: eight deliberate faults were injected into throwaway copies (altered value, applicability set to "currently applicable", modified original, deleted row, wrong unit, foreign-code source, blanked clause, stray file). The validator failed on all of them; a no-change control passed. Those copies were deleted.

## 11. Reproducibility

The CSVs were produced by a one-off builder script that is **not** committed (the request limited outputs to four files). `validate_member3.py` does not depend on it: it re-reads the originals and re-derives counts, hashes, traceability and cross-version status. If you want the builder committed for reproducibility, say so and it can be added as a fifth file.

## Appendix A. SHA-256 of the originals (before = after)

| File | SHA-256 |
|---|---|
| `recovered_versions/BuildMind_Member3_Final_4_Paper_Research_Dataset.xlsx` | `4ad3b5789b72c7bf229517cecaf34347466dd0fa302b1e455c71d27f84a176de` |
| `recovered_versions/BuildMind_Member3_Gazette_Verified_Dataset.xlsx` | `6b55339e6a94168d85985229e0cba7e07d32baa5196a056193289920ee19e436` |
| `recovered_versions/BuildMind_Member3_Research_Starter.xlsx` | `39f25a7803404b44a333515e3cfe931d8b7e2933c61b3c9f7f39067fbfa158f0` |
| `recovered_versions/BuildMind_Member3_Sri_Lanka_Room_Standards_Extract.xlsx` | `7e7a6a54690e39093607b6f965081f16a3978245d33423ea0c172a463dc771f2` |
| `recovered_versions/BuildMind_Member3_Sri_Lanka_Room_Standards_Stage2.xlsx` | `e061e77e7512fef4e343291b51e416a9eea0c4c017acf5886071a5c3d975173c` |
| `recovered_versions/BuildMind_Member3_Stage3_Concept_Layout_Validation.xlsx` | `7096e30c635e240b38de260fd391f4ca31ecb918d1e4cb60d71bc33fbfa95de8` |
| `recovered_versions/BuildMind_Member3_Stage4_Verified_Research.xlsx` | `68c6be601a04929975e5e3d76dfbd2d7725173e07b31cd0ec2c7b9afa30e0808` |
| `recovered_versions/BuildMind_Member3_Stage5_Sri_Lanka_Compliance_Research.xlsx` | `da1d25fae9835854bada6b4c4b8739e3779f05009f2169a972fa2b9ca6726a7c` |
| `recovered_versions/BuildMind_Member3_Stage6_Gazette_Verification_Audit.xlsx` | `0b98ebc4fc3a73803619d133a0acb1d29c732e325f4fee6c89d322eee1b37a86` |
| `recovered_versions/BuildMind_Member3_Stage9_Gazette_Text_Verified.xlsx` | `c2d3a078f179272bcacf61196f89b862d47c24c8225277670bfb279401ed0523` |
| `recovered_versions/BuildMind_Member3_room_standards.csv` | `d70cb99d735bd76e8af86d7a06e6633538479a3e243272b353444fa6a92eef3d` |
| `recovered_versions/BuildMind_NBRO_Reference_Plan_Extraction_v1.xlsx` | `8b80bc58a9113e7a5354e5dd12a20077ca4da68cdc51c22370799d62eff17f57` |
| `recovered_versions/BuildMind_Stage8_2_Updated_Room_Dimensions.xlsx` | `d99a0f9e7a379c3e9442bdd3b30d99256e6344f8ae810542b0b390e943084d2c` |
| `recovered_versions/BuildMind_Stage8_Sri_Lankan_Floor_Plans_Initial_Extraction.xlsx` | `1b54bb644da7197105b84d9c227ac509635798d43538b0b046d920a1cf4d66cb` |

## Appendix B. Column guide for `member3_consolidated_rules.csv`

- **Provenance:** `origin_stage`, `origin_workbook`, `origin_sheet`, `origin_row`, `origin_rule_id`, `origin_rule_id_cell`, `origin_value_cell`, and the raw origin text (`origin_value_raw`, `origin_unit_raw`, `origin_subject_raw`, `origin_metric_raw`, `origin_operator_raw`, `origin_clause_raw`, `origin_page_raw`, `origin_status_raw`, `origin_applicability_raw`, `origin_condition_raw`, `origin_notes_raw`).
- **Normalised:** `subject_norm`, `subject_group`, `parameter_norm`, `context_norm` (building-height band for Schedule 9), `operator`, `operator_basis`, `value`, `unit_norm`, `value_si`, `unit_si`, `ratio_basis`, `cmp_key`.
- **Source:** `source_document`, `source_gazette_no`, `source_date`, `source_year`, `source_year_basis`, `source_url`, `source_url_basis`, `source_file_name`, `source_file_basis`, `region`, `region_note`, `clause_norm`, `printed_page`.
- **Status:** `rule_type`, `severity`, `text_verification_status`, `text_verification_basis`, `applicability_status` (always `PENDING`), `applicability_note`, `reviewer_status`, `independent_pdf_check_by_this_audit`, `engine_status_raw` (Stage6), `flags`.

Flags: `MISSING_PAGE`, `MISSING_CLAUSE`, `OPERATOR_IMPLIED`, `UNIT_MM_TO_M_FOR_COMPARISON`, `TERM_VARIANT_HABITABLE_NOT_GAZETTE_WORDING`, `SOURCE_EDITION_NOT_STATED`, `ID_REUSED_FOR_DIFFERENT_RULE_IN_OTHER_VERSION`.
