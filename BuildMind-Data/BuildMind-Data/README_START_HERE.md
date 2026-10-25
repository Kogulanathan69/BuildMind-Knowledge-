# BuildMind new PC recovery

Prepared 25 October 2026. Extract both ZIP packages into the SAME destination. Both create one BuildMind-Data folder. The first contains documents, recovered Excel/CSV versions, cost PDFs, weather observations, component/template packs and earlier code experiments. The second contains original source archives, including ResPlan and NBRO/BSR collections.

## What to open first

1. project_knowledge/START-HERE.md
2. documents/brd/BuildMind_Submission_BRD.pdf
3. datasets/03_room_dimensions/recovered_versions/
4. datasets/04_room_adjacency/recovered_versions/BuildMind_Room_Adjacency_DETAILED_FIXED.xlsx
5. MISSING_AND_PENDING.md

Original recovered workbooks are preserved byte-for-byte. Earlier versions are not all current or source-verified. WORKBOOK_STRUCTURE_AUDIT.json checks readable containers and sheet structure only. RECOVERY_SOURCE_REGISTER.json records recovered-file hashes and exact duplicates.

## Weather

Four monthly raw files and one concatenated raw CSV are available. There are 14,112 observations with 113 source columns. Missing October observations have not been fabricated. See datasets/01_weather/RECOVERY_QA.json.

## Git preparation

Your existing repository is separate from this recovery folder. Do not initialise Git here, overwrite the repository, remove its ignore file, or add all original archives to the public repo. Use Prepare-Git-Preview.ps1 to list candidates without copying, committing or pushing. Rights and large-file handling must be resolved before selecting what to publish. Public documentation already exists at https://github.com/Kogulanathan69/BuildMind-Knowledge- .

## Verification

Run Verify-Recovery.ps1 from PowerShell after extraction to compare file hashes. The source archive package is optional for verifying part 1; files from part 2 are reported missing until extracted. The checksum confirms transport integrity, not factual accuracy, licence or legal applicability.
