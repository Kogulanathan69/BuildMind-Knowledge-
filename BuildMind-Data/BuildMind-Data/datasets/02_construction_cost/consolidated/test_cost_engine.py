#!/usr/bin/env python3

from pathlib import Path
import csv

BASE = Path(__file__).resolve().parent

WORK_ITEMS_FILE = BASE / "work_items.csv"
ADJUSTMENT_RULES_FILE = BASE / "adjustment_rules.csv"


def load_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_work_items():
    rows = load_csv(WORK_ITEMS_FILE)

    return {
        row["work_item_id"].strip(): row
        for row in rows
    }


def load_adjustments():
    rows = load_csv(ADJUSTMENT_RULES_FILE)

    return {
        row["rule_id"].strip(): row
        for row in rows
    }


def calculate_item(work_item, quantity):
    rate = float(work_item["unit_rate_lkr"])
    base_cost = quantity * rate

    return {
        "work_item_id": work_item["work_item_id"],
        "name": work_item["work_item_name"],
        "unit": work_item["unit"],
        "quantity": quantity,
        "unit_rate": rate,
        "base_cost": base_cost,
    }


def money(value):
    return f"{value:,.2f}"


def main():
    work_items = load_work_items()
    adjustments = load_adjustments()

    # ---------------------------------------------------------
    # SAMPLE HOUSE / SAMPLE QUANTITIES
    # Later these quantities will come automatically from
    # BuildMind 2D / 3D geometry.
    # ---------------------------------------------------------

    sample_quantities = {
        "WI-001": 10.00,   # Soft soil excavation m3
        "WI-007": 5.00,    # Concrete 1:2:4 m3
        "WI-011": 450.00,  # Reinforcement kg
        "WI-012": 3.00,    # Brickwork foundation m3
        "WI-013": 40.00,   # 9" brick wall m2
        "WI-014": 90.00,   # Plastering m2
        "WI-016": 50.00,   # Floor tiles m2
        "WI-019": 70.00,   # Roofing m2
        "WI-021": 120.00,  # Wall painting m2
        "WI-022": 5.00,    # Door work m2
        "WI-023": 6.00,    # Window work m2
    }

    results = []

    for work_item_id, quantity in sample_quantities.items():

        if work_item_id not in work_items:
            print(f"ERROR: Missing work item: {work_item_id}")
            return

        result = calculate_item(
            work_items[work_item_id],
            quantity
        )

        results.append(result)

    subtotal = sum(
        item["base_cost"]
        for item in results
    )

    profit_percent = float(
        adjustments["ADJ-001"]["value"]
    )

    overhead_percent = float(
        adjustments["ADJ-002"]["value"]
    )

    combined_percent = float(
        adjustments["ADJ-003"]["value"]
    )

    profit_amount = subtotal * profit_percent / 100
    overhead_amount = subtotal * overhead_percent / 100
    ohp_amount = subtotal * combined_percent / 100

    total_before_vat = subtotal + ohp_amount

    # VAT intentionally NOT calculated.
    # The current dataset stores VAT as separate and the
    # percentage has not yet been independently verified.

    print()
    print("=" * 100)
    print("BuildMind Cost Engine - SAMPLE TEST")
    print("=" * 100)
    print()

    print(
        f"{'ID':<8}"
        f"{'Work Item':<38}"
        f"{'Qty':>10}"
        f"{'Unit':>8}"
        f"{'Rate LKR':>15}"
        f"{'Cost LKR':>18}"
    )

    print("-" * 100)

    for item in results:

        print(
            f"{item['work_item_id']:<8}"
            f"{item['name'][:36]:<38}"
            f"{item['quantity']:>10.2f}"
            f"{item['unit']:>8}"
            f"{money(item['unit_rate']):>15}"
            f"{money(item['base_cost']):>18}"
        )

    print("-" * 100)

    print(
        f"{'BASE SUBTOTAL':<79}"
        f"{money(subtotal):>21}"
    )

    print(
        f"{'Profit (' + str(profit_percent) + '%)':<79}"
        f"{money(profit_amount):>21}"
    )

    print(
        f"{'General Overhead (' + str(overhead_percent) + '%)':<79}"
        f"{money(overhead_amount):>21}"
    )

    print(
        f"{'Combined OH & Profit (' + str(combined_percent) + '%)':<79}"
        f"{money(ohp_amount):>21}"
    )

    print("=" * 100)

    print(
        f"{'TOTAL BEFORE VAT':<79}"
        f"{money(total_before_vat):>21}"
    )

    print("=" * 100)

    print()
    print("VAT: NOT CALCULATED")
    print(
        "Reason: VAT is stored as a separate tax and "
        "the percentage is not yet independently verified."
    )

    print()
    print(
        "NOTE: This is a SAMPLE calculation using manually "
        "entered quantities."
    )

    print(
        "Future BuildMind flow: 2D/3D geometry -> quantities "
        "-> work item mapping -> unit rates -> final cost."
    )

    print()


if __name__ == "__main__":
    main()