# extraction_flags.csv

**Dataset status:** `unverified_candidates` (not production verified)  
**Records:** 96  
**Columns:** 5  
**SHA-256:** `6d92bda9ebc7ec226f8318767461edaee30184a7d36e086b7aba92a9c5e889a6`  
**Actual CSV public on GitHub:** No  

## Field-level data dictionary (inferred, not confirmed definitions)

| Column | Inferred type | Blank cells | Safe category examples |
|---|---|---:|---|
| document | text/mixed | 0 | BSR.pdf, Const_BSR_2020_final-compressed.pdf, SoR_2026 _Road.pdf |
| pdf_page | numeric-like | 0 | — |
| item_code | text/mixed | 0 | — |
| issue | text/mixed | 0 | AMBIGUOUS_OR_MISSING_RATE, UNEXPECTED_COLUMN_COUNT |
| detail | text/mixed | 0 | — |

## Interpretation and safety

- Column meanings, units and provenance must be verified against source PDFs and dataset READMEs.
- Do not interpret candidate rates as verified market prices or current construction quotations.
- Never convert `Not Applicable` into zero; preserve missing/non-applicable values.
- Never merge BSR 2020, Northern Province BSR 2026, and Road SoR 2026 without year/type/region metadata.
- Weather timestamps have an Oct 7–30, 2021 coverage gap and timezone remains unconfirmed.
- The original records are **not** contained in this document. For full analysis, authorized access to CSV files is required.
