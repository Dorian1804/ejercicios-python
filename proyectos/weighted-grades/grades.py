"""Compute a weighted mean from grade:weight pairs."""
import argparse
import math


def weighted_mean(pairs):
    if not pairs:
        raise ValueError("Provide at least one grade.")
    for grade, weight in pairs:
        if not math.isfinite(grade) or not math.isfinite(weight) or not 0 <= grade <= 100 or not 0 < weight <= 100:
            raise ValueError("Grades must be 0–100 and weights greater than 0 and at most 100.")
    total = sum(weight for _, weight in pairs)
    if not math.isclose(total, 100, abs_tol=.000001):
        raise ValueError("Weights must add up to 100 percent.")
    return sum(grade * weight for grade, weight in pairs) / total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pairs", nargs="+", metavar="GRADE:WEIGHT")
    args = parser.parse_args()
    try:
        pairs = []
        for value in args.pairs:
            grade, weight = value.split(":")
            pairs.append((float(grade), float(weight)))
        print(f"Weighted grade: {weighted_mean(pairs):.2f}")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
