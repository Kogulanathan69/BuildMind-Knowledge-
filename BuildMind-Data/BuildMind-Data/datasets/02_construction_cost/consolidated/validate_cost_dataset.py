#!/usr/bin/env python3

"""
BuildMind Construction Cost Dataset Validator

Validates:
1. Required files exist
2. CSV headers are correct
3. Required IDs are unique
4. Work-item references exist
5. Material/Labour/Equipment references exist
6. Resource coefficient values are valid
7. Verification/applicability statuses are valid
8. Adjustment rules are valid
9. Basic row counts are reasonable
10. Pending rates are handled safely

Run:
    python validate_cost_dataset.py

Exit code:
    0 = all checks passed
    1 = one or more checks failed
"""

from pathlib import Path
import csv
import sys
from collections import Counter


# ============================================================
# PATHS
# ============================================================

BASE = Path(__file__).resolve().parent

FILES = {
    "work_items": BASE / "work_items.csv",
    "labour_rates": BASE / "labour_rates.csv",
    "material_prices": BASE / "material_prices.csv",
    "equipment_rates": BASE / "equipment_rates.csv",
    "resource_coefficients": BASE / "resource_coefficients.csv",
    "adjustment_rules": BASE / "adjustment_rules.csv",
}


# ============================================================
# EXPECTED HEADERS
# ============================================================

EXPECTED_HEADERS = {
    "work_items": [
        "work_item_id",
        "category",
        "work_item_name",
        "description",
        "unit",
        "source_document",
        "source_page",
        "year",
        "region",
        "unit_rate_lkr",
        "verification_status",
        "notes",
    ],

    "labour_rates": [
        "labour_id",
        "category",
        "unit",
        "hours_per_day",
        "region",
        "year",
        "basic_rate_lkr",
        "source_document",
        "source_page",
        "verification_status",
        "notes",
    ],

    "material_prices": [
        "material_id",
        "material_name",
        "specification",
        "unit",
        "region",
        "year",
        "unit_price_lkr",
        "source_document",
        "source_page",
        "verification_status",
        "notes",
    ],

    "equipment_rates": [
        "equipment_id",
        "equipment_name",
        "specification",
        "unit",
        "region",
        "year",
        "rate_lkr",
        "source_document",
        "source_page",
        "verification_status",
        "notes",
    ],

    "resource_coefficients": [
        "coefficient_id",
        "work_item_id",
        "resource_type",
        "resource_id",
        "resource_name",
        "quantity_per_work_unit",
        "resource_unit",
        "work_unit",
        "source_document",
        "source_page",
        "verification_status",
        "applicability_status",
        "notes",
    ],

    "adjustment_rules": [
        "rule_id",
        "rule_name",
        "rule_type",
        "value",
        "unit",
        "applies_to",
        "region",
        "year",
        "source_document",
        "source_page",
        "verification_status",
        "notes",
    ],
}


# ============================================================
# ALLOWED VALUES
# ============================================================

RESOURCE_TYPES = {
    "Material",
    "Labour",
    "Equipment",
}

VERIFICATION_STATUSES = {
    "SOURCE_VERIFIED",
    "RATE_PENDING",
    "PENDING",
    "UNVERIFIED",
}

APPLICABILITY_STATUSES = {
    "APPLICABILITY_PENDING",
    "APPLICABLE",
    "NOT_APPLICABLE",
}

ADJUSTMENT_RULE_TYPES = {
    "percentage",
    "separate_tax",
    "included_in_rate",
}


# ============================================================
# RESULT HANDLING
# ============================================================

checks = 0
failed = 0


def check(name, condition, detail=""):
    global checks, failed

    checks += 1

    if condition:
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")

    if detail:
        print(f"      {detail}")


def info(message):
    print(f"      (info) {message}")


# ============================================================
# CSV HELPERS
# ============================================================

def load_csv(path):
    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as f:
        return list(csv.DictReader(f))


def get_headers(path):
    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as f:
        reader = csv.reader(f)

        try:
            return next(reader)
        except StopIteration:
            return []


def duplicate_values(rows, key):
    values = [
        row.get(key, "").strip()
        for row in rows
        if row.get(key, "").strip()
    ]

    counts = Counter(values)

    return sorted(
        value
        for value, count in counts.items()
        if count > 1
    )


def is_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def positive_number(value):
    if not is_number(value):
        return False

    return float(value) > 0


# ============================================================
# START
# ============================================================

print()
print("=" * 68)
print("BuildMind Construction Cost Dataset Validation")
print("=" * 68)
print(f"Dataset folder: {BASE}")
print()


# ============================================================
# 1. REQUIRED FILES
# ============================================================

missing_files = [
    name
    for name, path in FILES.items()
    if not path.exists()
]

check(
    "1 required CSV files exist",
    len(missing_files) == 0,
    (
        f"Missing: {missing_files}"
        if missing_files
        else "6/6 files present"
    ),
)

if missing_files:
    print()
    print("Validation stopped because required files are missing.")
    sys.exit(1)


# ============================================================
# LOAD DATA
# ============================================================

data = {
    name: load_csv(path)
    for name, path in FILES.items()
}


# ============================================================
# 2. HEADER VALIDATION
# ============================================================

header_errors = []

for name, path in FILES.items():

    actual = get_headers(path)
    expected = EXPECTED_HEADERS[name]

    if actual != expected:
        header_errors.append(name)


check(
    "2 CSV headers match expected schemas",
    not header_errors,
    (
        f"Header mismatch: {header_errors}"
        if header_errors
        else "All headers correct"
    ),
)


# ============================================================
# 3. ROW COUNTS
# ============================================================

info(
    f"work_items.csv rows = {len(data['work_items'])}"
)

info(
    f"labour_rates.csv rows = {len(data['labour_rates'])}"
)

info(
    f"material_prices.csv rows = {len(data['material_prices'])}"
)

info(
    f"equipment_rates.csv rows = {len(data['equipment_rates'])}"
)

info(
    f"resource_coefficients.csv rows = "
    f"{len(data['resource_coefficients'])}"
)

info(
    f"adjustment_rules.csv rows = "
    f"{len(data['adjustment_rules'])}"
)


check(
    "3 core dataset contains expected minimum rows",
    (
        len(data["work_items"]) >= 23
        and len(data["labour_rates"]) >= 4
        and len(data["material_prices"]) >= 7
        and len(data["equipment_rates"]) >= 2
        and len(data["resource_coefficients"]) >= 24
        and len(data["adjustment_rules"]) >= 5
    ),
)


# ============================================================
# 4. UNIQUE IDS
# ============================================================

id_fields = {
    "work_items": "work_item_id",
    "labour_rates": "labour_id",
    "material_prices": "material_id",
    "equipment_rates": "equipment_id",
    "resource_coefficients": "coefficient_id",
    "adjustment_rules": "rule_id",
}


duplicate_report = {}

for name, key in id_fields.items():

    duplicates = duplicate_values(
        data[name],
        key,
    )

    if duplicates:
        duplicate_report[name] = duplicates


check(
    "4 all master IDs are unique",
    not duplicate_report,
    (
        str(duplicate_report)
        if duplicate_report
        else "No duplicate IDs"
    ),
)


# ============================================================
# 5. BLANK IDS
# ============================================================

blank_ids = []

for name, key in id_fields.items():

    for index, row in enumerate(
        data[name],
        start=2,
    ):

        if not row.get(key, "").strip():
            blank_ids.append(
                f"{name} row {index}"
            )


check(
    "5 no blank primary IDs",
    not blank_ids,
    (
        str(blank_ids[:10])
        if blank_ids
        else "All rows have IDs"
    ),
)


# ============================================================
# 6. WORK ITEM BASIC VALIDATION
# ============================================================

bad_work_items = []

for row in data["work_items"]:

    required = [
        "work_item_id",
        "category",
        "work_item_name",
        "unit",
        "source_document",
        "source_page",
        "year",
        "region",
        "unit_rate_lkr",
        "verification_status",
    ]

    if any(
        not row.get(field, "").strip()
        for field in required
    ):
        bad_work_items.append(
            row["work_item_id"]
        )

        continue

    if not positive_number(
        row["unit_rate_lkr"]
    ):
        bad_work_items.append(
            row["work_item_id"]
        )


check(
    "6 work-item rows contain valid rates and provenance",
    not bad_work_items,
    (
        f"Problem rows: {bad_work_items}"
        if bad_work_items
        else f"{len(data['work_items'])} work items valid"
    ),
)


# ============================================================
# 7. LABOUR RATES
# ============================================================

bad_labour = []

for row in data["labour_rates"]:

    if (
        not row["labour_id"].strip()
        or not row["category"].strip()
        or not positive_number(
            row["hours_per_day"]
        )
        or not positive_number(
            row["basic_rate_lkr"]
        )
        or not row["source_document"].strip()
        or not row["source_page"].strip()
    ):
        bad_labour.append(
            row["labour_id"]
        )


check(
    "7 labour-rate rows valid",
    not bad_labour,
    (
        f"Problem rows: {bad_labour}"
        if bad_labour
        else f"{len(data['labour_rates'])} labour rows valid"
    ),
)


# ============================================================
# 8. MATERIAL PRICE HANDLING
# ============================================================

bad_materials = []
pending_materials = []
verified_materials = []

for row in data["material_prices"]:

    status = row[
        "verification_status"
    ].strip()

    rate = row[
        "unit_price_lkr"
    ].strip()

    if status == "SOURCE_VERIFIED":

        if not positive_number(rate):
            bad_materials.append(
                row["material_id"]
            )

        else:
            verified_materials.append(
                row["material_id"]
            )

    elif status == "RATE_PENDING":

        if rate != "":
            bad_materials.append(
                row["material_id"]
            )

        else:
            pending_materials.append(
                row["material_id"]
            )

    else:

        if status not in VERIFICATION_STATUSES:
            bad_materials.append(
                row["material_id"]
            )


check(
    "8 material prices correctly distinguish verified and pending rates",
    not bad_materials,
    (
        f"Problem rows: {bad_materials}"
        if bad_materials
        else (
            f"{len(verified_materials)} verified, "
            f"{len(pending_materials)} pending"
        )
    ),
)


# ============================================================
# 9. EQUIPMENT RATE HANDLING
# ============================================================

bad_equipment = []
pending_equipment = []
verified_equipment = []

for row in data["equipment_rates"]:

    status = row[
        "verification_status"
    ].strip()

    rate = row[
        "rate_lkr"
    ].strip()

    if status == "SOURCE_VERIFIED":

        if not positive_number(rate):
            bad_equipment.append(
                row["equipment_id"]
            )

        else:
            verified_equipment.append(
                row["equipment_id"]
            )

    elif status == "RATE_PENDING":

        if rate != "":
            bad_equipment.append(
                row["equipment_id"]
            )

        else:
            pending_equipment.append(
                row["equipment_id"]
            )

    else:

        if status not in VERIFICATION_STATUSES:
            bad_equipment.append(
                row["equipment_id"]
            )


check(
    "9 equipment rates correctly distinguish verified and pending rates",
    not bad_equipment,
    (
        f"Problem rows: {bad_equipment}"
        if bad_equipment
        else (
            f"{len(verified_equipment)} verified, "
            f"{len(pending_equipment)} pending"
        )
    ),
)


# ============================================================
# 10. MASTER ID SETS
# ============================================================

work_ids = {
    row["work_item_id"].strip()
    for row in data["work_items"]
}

material_ids = {
    row["material_id"].strip()
    for row in data["material_prices"]
}

labour_ids = {
    row["labour_id"].strip()
    for row in data["labour_rates"]
}

equipment_ids = {
    row["equipment_id"].strip()
    for row in data["equipment_rates"]
}


# ============================================================
# 11. COEFFICIENT -> WORK ITEM REFERENCES
# ============================================================

missing_work_refs = []

for row in data["resource_coefficients"]:

    if row[
        "work_item_id"
    ].strip() not in work_ids:

        missing_work_refs.append(
            (
                row["coefficient_id"],
                row["work_item_id"],
            )
        )


check(
    "10 every resource coefficient references an existing work item",
    not missing_work_refs,
    (
        str(missing_work_refs[:10])
        if missing_work_refs
        else "All work_item_id references valid"
    ),
)


# ============================================================
# 12. RESOURCE MASTER REFERENCES
# ============================================================

missing_resource_refs = []

for row in data["resource_coefficients"]:

    rtype = row[
        "resource_type"
    ].strip()

    rid = row[
        "resource_id"
    ].strip()

    exists = False

    if rtype == "Material":
        exists = rid in material_ids

    elif rtype == "Labour":
        exists = rid in labour_ids

    elif rtype == "Equipment":
        exists = rid in equipment_ids

    if not exists:
        missing_resource_refs.append(
            (
                row["coefficient_id"],
                rtype,
                rid,
            )
        )


check(
    "11 every resource_id exists in its master table",
    not missing_resource_refs,
    (
        str(missing_resource_refs[:10])
        if missing_resource_refs
        else "All material/labour/equipment links valid"
    ),
)


# ============================================================
# 13. RESOURCE TYPES
# ============================================================

bad_resource_types = [
    (
        row["coefficient_id"],
        row["resource_type"],
    )
    for row in data["resource_coefficients"]
    if row[
        "resource_type"
    ].strip() not in RESOURCE_TYPES
]


check(
    "12 resource_type values are valid",
    not bad_resource_types,
    (
        str(bad_resource_types)
        if bad_resource_types
        else "Material/Labour/Equipment only"
    ),
)


# ============================================================
# 14. COEFFICIENT VALUES
# ============================================================

bad_coeff_values = []

for row in data["resource_coefficients"]:

    if not positive_number(
        row[
            "quantity_per_work_unit"
        ]
    ):
        bad_coeff_values.append(
            row[
                "coefficient_id"
            ]
        )


check(
    "13 all resource coefficient quantities are positive numbers",
    not bad_coeff_values,
    (
        str(bad_coeff_values)
        if bad_coeff_values
        else f"{len(data['resource_coefficients'])} coefficients valid"
    ),
)


# ============================================================
# 15. COEFFICIENT PROVENANCE
# ============================================================

bad_coeff_provenance = []

for row in data["resource_coefficients"]:

    fields = [
        "source_document",
        "source_page",
        "verification_status",
        "applicability_status",
    ]

    if any(
        not row.get(
            field,
            "",
        ).strip()
        for field in fields
    ):
        bad_coeff_provenance.append(
            row[
                "coefficient_id"
            ]
        )


check(
    "14 every resource coefficient has source and status provenance",
    not bad_coeff_provenance,
    (
        str(bad_coeff_provenance)
        if bad_coeff_provenance
        else "All coefficient provenance present"
    ),
)


# ============================================================
# 16. COEFFICIENT VERIFICATION STATUS
# ============================================================

bad_coeff_verification = [
    (
        row["coefficient_id"],
        row["verification_status"],
    )
    for row in data["resource_coefficients"]
    if row[
        "verification_status"
    ].strip() not in VERIFICATION_STATUSES
]


check(
    "15 coefficient verification statuses valid",
    not bad_coeff_verification,
    (
        str(bad_coeff_verification)
        if bad_coeff_verification
        else "All verification statuses valid"
    ),
)


# ============================================================
# 17. APPLICABILITY STATUS
# ============================================================

bad_applicability = [
    (
        row["coefficient_id"],
        row["applicability_status"],
    )
    for row in data["resource_coefficients"]
    if row[
        "applicability_status"
    ].strip() not in APPLICABILITY_STATUSES
]


check(
    "16 coefficient applicability statuses valid",
    not bad_applicability,
    (
        str(bad_applicability)
        if bad_applicability
        else "All applicability statuses valid"
    ),
)


pending_applicability = [
    row[
        "coefficient_id"
    ]
    for row in data[
        "resource_coefficients"
    ]
    if row[
        "applicability_status"
    ].strip()
    ==
    "APPLICABILITY_PENDING"
]


info(
    f"APPLICABILITY_PENDING coefficients = "
    f"{len(pending_applicability)}"
)


# ============================================================
# 18. RESOURCE DISTRIBUTION
# ============================================================

resource_counts = Counter(
    row[
        "resource_type"
    ].strip()
    for row in data[
        "resource_coefficients"
    ]
)


check(
    "17 expected resource categories are represented",
    all(
        resource_counts.get(
            resource_type,
            0,
        ) > 0
        for resource_type
        in RESOURCE_TYPES
    ),
    (
        f"Distribution: {dict(resource_counts)}"
    ),
)


# ============================================================
# 19. CURRENT EXPECTED CONCRETE MAPPING
# ============================================================

expected_concrete_work_items = {
    "WI-006",
    "WI-007",
    "WI-008",
}


mapped_concrete_items = {
    row[
        "work_item_id"
    ].strip()
    for row in data[
        "resource_coefficients"
    ]
}


check(
    "18 initial concrete work items have resource coefficients",
    expected_concrete_work_items.issubset(
        mapped_concrete_items
    ),
    (
        f"Mapped: "
        f"{sorted(expected_concrete_work_items & mapped_concrete_items)}"
    ),
)


# ============================================================
# 20. EXPECTED 8 RESOURCES PER CONCRETE MIX
# ============================================================

bad_concrete_counts = []

for work_id in sorted(
    expected_concrete_work_items
):

    count = sum(
        1
        for row in data[
            "resource_coefficients"
        ]
        if row[
            "work_item_id"
        ].strip()
        ==
        work_id
    )

    if count != 8:
        bad_concrete_counts.append(
            (
                work_id,
                count,
            )
        )


check(
    "19 each initial concrete mix has 8 resource coefficients",
    not bad_concrete_counts,
    (
        str(bad_concrete_counts)
        if bad_concrete_counts
        else "WI-006/WI-007/WI-008 each have 8 resources"
    ),
)


# ============================================================
# 21. ADJUSTMENT RULE TYPES
# ============================================================

bad_rule_types = [
    (
        row["rule_id"],
        row["rule_type"],
    )
    for row in data[
        "adjustment_rules"
    ]
    if row[
        "rule_type"
    ].strip()
    not in ADJUSTMENT_RULE_TYPES
]


check(
    "20 adjustment rule types valid",
    not bad_rule_types,
    (
        str(bad_rule_types)
        if bad_rule_types
        else "All adjustment rule types valid"
    ),
)


# ============================================================
# 22. ADJUSTMENT SOURCES
# ============================================================

bad_adjustment_sources = []

for row in data[
    "adjustment_rules"
]:

    if (
        not row[
            "source_document"
        ].strip()
        or not row[
            "source_page"
        ].strip()
        or not row[
            "verification_status"
        ].strip()
    ):
        bad_adjustment_sources.append(
            row[
                "rule_id"
            ]
        )


check(
    "21 adjustment rules have provenance",
    not bad_adjustment_sources,
    (
        str(bad_adjustment_sources)
        if bad_adjustment_sources
        else "All adjustment rules have source provenance"
    ),
)


# ============================================================
# 23. 10 + 6 = 16 CHECK
# ============================================================

rule_map = {
    row[
        "rule_id"
    ]: row
    for row in data[
        "adjustment_rules"
    ]
}


ohp_ok = False

try:

    profit = float(
        rule_map[
            "ADJ-001"
        ][
            "value"
        ]
    )

    overhead = float(
        rule_map[
            "ADJ-002"
        ][
            "value"
        ]
    )

    combined = float(
        rule_map[
            "ADJ-003"
        ][
            "value"
        ]
    )

    ohp_ok = abs(
        (
            profit
            + overhead
        )
        -
        combined
    ) < 1e-9

except Exception:
    ohp_ok = False


check(
    "22 Profit + General Overhead equals combined OH&P",
    ohp_ok,
    "Expected 10 + 6 = 16",
)


# ============================================================
# 24. VAT SAFETY CHECK
# ============================================================

vat_rows = [
    row
    for row in data[
        "adjustment_rules"
    ]
    if row[
        "rule_id"
    ]
    ==
    "ADJ-004"
]


vat_safe = (
    len(
        vat_rows
    )
    ==
    1
    and vat_rows[
        0
    ][
        "rule_type"
    ]
    ==
    "separate_tax"
    and vat_rows[
        0
    ][
        "value"
    ].strip()
    ==
    ""
)


check(
    "23 VAT percentage remains unset unless independently verified",
    vat_safe,
    (
        "VAT stored as separate tax with blank percentage"
        if vat_safe
        else "Check ADJ-004"
    ),
)


# ============================================================
# 25. TRANSPORT/WASTAGE DOUBLE-COUNT CHECK
# ============================================================

included_rows = [
    row
    for row in data[
        "adjustment_rules"
    ]
    if row[
        "rule_id"
    ]
    ==
    "ADJ-005"
]


transport_safe = (
    len(
        included_rows
    )
    ==
    1
    and included_rows[
        0
    ][
        "rule_type"
    ]
    ==
    "included_in_rate"
)


check(
    "24 transport/loading/unloading/wastage marked included to avoid double counting",
    transport_safe,
)


# ============================================================
# 26. FINAL COST-ENGINE READINESS
# ============================================================

pending_rate_resources = (
    len(
        pending_materials
    )
    +
    len(
        pending_equipment
    )
)


info(
    f"Resources still waiting for standalone rates = "
    f"{pending_rate_resources}"
)


cost_engine_ready = (
    failed == 0
    and pending_rate_resources == 0
    and len(
        pending_applicability
    )
    ==
    0
)


if cost_engine_ready:

    info(
        "Full resource-based cost calculation is READY"
    )

else:

    info(
        "Dataset structure is valid, but full resource-based "
        "cost calculation remains PARTIAL"
    )

    if pending_rate_resources:
        info(
            "Reason: some material/equipment rates are RATE_PENDING"
        )

    if pending_applicability:
        info(
            "Reason: some coefficients are APPLICABILITY_PENDING"
        )


# ============================================================
# SUMMARY
# ============================================================

print()
print("=" * 68)

print(
    f"SUMMARY: {checks} checks, "
    f"{checks - failed} passed, "
    f"{failed} failed"
)

print("=" * 68)


if failed == 0:

    print(
        "RESULT: DATASET VALID"
    )

    if not cost_engine_ready:
        print(
            "STATUS: STRUCTURE VALID / COST ENGINE PARTIAL"
        )

else:

    print(
        "RESULT: DATASET INVALID"
    )


print()


sys.exit(
    1
    if failed
    else 0
)