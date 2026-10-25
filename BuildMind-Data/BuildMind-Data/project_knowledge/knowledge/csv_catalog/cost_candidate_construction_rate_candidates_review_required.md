# construction_rate_candidates_REVIEW_REQUIRED.csv

**Dataset status:** `unverified_candidates` (not production verified)  
**Records:** 5,304  
**Columns:** 12  
**SHA-256:** `1f0d5c767c6d486601b60d92adcfbb9936567000d11b7ba3854dda0d8d9ca521`  
**Actual CSV public on GitHub:** No  

## Field-level data dictionary (inferred, not confirmed definitions)

| Column | Inferred type | Blank cells | Safe category examples |
|---|---|---:|---|
| dataset | text/mixed | 0 | — |
| item_code | text/mixed | 0 | — |
| description | text/mixed | 0 | — |
| unit | text/mixed | 0 | M3, M2, No, Lm, Kg |
| district | text/mixed | 0 | Jaffna, Kilinochchi, Mullaitivu, Mannar, Vavuniya |
| rate_lkr | numeric-like | 0 | — |
| rate_year | numeric-like | 0 | — |
| rate_period | text/mixed | 0 | — |
| source_document | text/mixed | 0 | BSR.pdf, Const_BSR_2020_final-compressed.pdf, SoR_2026 _Road.pdf |
| source_pdf_page | numeric-like | 0 | — |
| verification_status | text/mixed | 0 | PENDING_MANUAL_REVIEW |
| review_reason | text/mixed | 0 | — |

## Interpretation and safety

- Column meanings, units and provenance must be verified against source PDFs and dataset READMEs.
- Do not interpret candidate rates as verified market prices or current construction quotations.
- Never convert `Not Applicable` into zero; preserve missing/non-applicable values.
- Never merge BSR 2020, Northern Province BSR 2026, and Road SoR 2026 without year/type/region metadata.
- Weather timestamps have an Oct 7–30, 2021 coverage gap and timezone remains unconfirmed.
- The original records are **not** contained in this document. For full analysis, authorized access to CSV files is required.
