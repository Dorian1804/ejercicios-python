"""Summarize a local expense CSV using exact decimal arithmetic."""
import argparse
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation


def summarize(path):
    totals = defaultdict(Decimal)
    with open(path, newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not {"category", "amount"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV requires category and amount columns.")
        for row in reader:
            category = (row.get("category") or "").strip()
            amount = Decimal(row["amount"])
            if not category or not amount.is_finite() or amount < 0:
                raise ValueError("Use nonempty categories and finite, nonnegative amounts.")
            if amount != amount.quantize(Decimal("0.01")):
                raise ValueError("Amounts may have at most two decimal places.")
            totals[category] += amount
    return dict(sorted(totals.items()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    args = parser.parse_args()
    try:
        totals = summarize(args.file)
        for category, amount in totals.items():
            print(f"{category}: {amount:.2f}")
        print(f"Total: {sum(totals.values(), Decimal(0)):.2f}")
    except (OSError, ValueError, InvalidOperation, TypeError, csv.Error) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
