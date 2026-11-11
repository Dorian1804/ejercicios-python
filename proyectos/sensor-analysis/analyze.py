"""Summarize one numeric column from a CSV sensor recording."""
import argparse
import csv
import math
import statistics


def summarize(path, column):
    with open(path, newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if column not in (reader.fieldnames or []):
            raise ValueError(f"Column not found: {column}")
        values = []
        for row in reader:
            value = float(row[column])
            if not math.isfinite(value):
                raise ValueError("Readings must be finite numbers.")
            values.append(value)
    if not values:
        raise ValueError("The CSV contains no readings.")
    return {"count": len(values), "min": min(values), "max": max(values), "mean": statistics.mean(values), "median": statistics.median(values), "stdev": statistics.stdev(values) if len(values) > 1 else 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--column", default="y_V")
    args = parser.parse_args()
    try:
        for key, value in summarize(args.file, args.column).items():
            print(f"{key}: {value:.6g}")
    except (OSError, ValueError, TypeError, csv.Error) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
