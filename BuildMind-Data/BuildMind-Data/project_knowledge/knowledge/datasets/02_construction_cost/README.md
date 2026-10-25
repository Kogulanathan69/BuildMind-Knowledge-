# BuildMind Construction Cost Dataset

## Sources
1. Northern Province BSR 2026, second half (83 PDF pages)
2. Department of Buildings BSR 2020 (105 PDF pages)
3. Northern Province Road SoR 2026 (81 PDF pages)

## Batch Extraction
- Total processed pages: 269
- Rate candidate records: 5,304
- Extraction review flags: 96

## Preliminary Review Classification
- NOT_APPLICABLE_REVIEW: 31
- MANUAL_REVIEW: 65

## Important Limitations
- Rate candidates have not been fully verified against their PDFs.
- Not Applicable must not become a zero price.
- Historical 2020 rates must not be treated as current prices.
- Road rates must remain separate from residential building rates.
- Applicable district, item unit, year and source page must be preserved.
- Source licensing and redistribution permissions require confirmation.

## Output Data
Raw PDFs and rate candidate CSV files are stored locally in:
Downloads/BuildMind_Cost_Extracted/
Downloads/BuildMind_Cost_Output/

## Next Tasks
1. Review the 65 manual-review flags.
2. Verify the 31 Not Applicable flags.
3. Audit numerical rates against source pages.
4. Validate item descriptions, units and district mapping.
5. Produce verified construction cost datasets.
6. Connect verified rates to the quotation calculation engine.

## Status
EXTRACTION COMPLETE - VERIFICATION PENDING.
NOT PRODUCTION READY.
