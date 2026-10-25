# BuildMind next steps

Updated 26 October 2026.

The detailed backlog and acceptance cases are in [open work and evaluation](docs/discussion-record/OPEN-WORK-AND-EVALUATION.md).

1. Confirm named owners, pilot locality, reviewers, MVP boundaries and budget assumptions.
2. Audit source inventory, licences and duplicates. Extract source-linked Sri Lankan room/planning rules. *Member 3 consolidation and internal audit completed 26 October 2026 (see below); external verification is still open.*
3. Prepare typed adjacency, reviewed climate rules and a small verified generic component catalogue.
4. Freeze canonical model, shared walls, opening hosts, units and revision contracts.
5. Implement layout solver, truthful search statuses and disclosed scoring.
6. Integrate source-backed RAG and validated conversational operations.
7. Integrate editable 2D/3D, undo, dependent revalidation and smart furnishing.
8. Fix remaining cutaway and furnishing-panel UX issues.
9. Review measurement standard with QS; implement a bounded BOQ/rate pipeline.
10. Run the BRD acceptance suite, pilot evaluation and document measured limitations.

Cost research remains important and the older work-item/resource dataset design is preserved. It is one workstream within the integrated product, not the only current priority. Sri Lankan furniture stock and current local product prices remain future scope.

## Member 3 follow-ups (from the 26 October consolidation)

Outputs are in [`datasets/03_room_dimensions/consolidated/`](BuildMind-Data/BuildMind-Data/datasets/03_room_dimensions/consolidated/): rules CSV, cross-version comparison CSV, audit report and `validate_member3.py`.

a. Compare all 262 values and their clause/page citations with the primary Gazette 2235/54 (8 July 2021) PDF. Resolve printed-page notation (123 versus 123A, 19 versus 19A), the Regulation 67(1)(b) "minimum height" versus "lowest point" label, and the missing page numbers (128 rows).
b. Check later gazettes and amendments, UDA-declared jurisdiction and the applicable development plan for the pilot locality. Keep `applicability_status = PENDING` until then.
c. Obtain qualified architect interpretation of the Schedule 7 "first room" and "additional room" categories before mapping them to named rooms. Do not use the "habitable room" wording from the Starter, CSV, Stage 5 and Stage 6 files as if it were Gazette wording.
d. Record a named reviewer and decide hard/soft severity for each rule (no origin file assigns it).
e. Do not join versions on `Rule_ID`: `SL-R02` to `SL-R07` mean different rules in Stage 5/6 and Stage 9.
f. Preferred room sizes, living/dining interpretation and circulation clearances remain not found; source them from Sri Lankan documents only.
g. Repository hygiene: `BuildMind-Data-Private` is private and the public cleanup commit has been pushed. Still open: (1) decide whether to rewrite Git history (the flagged files remain in history, forks and clones); (2) hash-verify the weather, Member 6 and ResPlan backups with `verify_private_backup.py` and record the result; (3) back up `BuildMind_AI_Dataset_v1 (1).zip` privately or keep it public; (4) keep `rights_status = UNVERIFIED` until rights are confirmed. Re-run `validate_member3.py` after any change to the originals.
