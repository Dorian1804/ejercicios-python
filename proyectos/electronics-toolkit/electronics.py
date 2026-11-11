"""Herramientas educativas de electrónica; usa unidades SI."""
import argparse
import math
import statistics


def positive(value):
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError("El valor debe ser finito y mayor que cero.")
    return value


def calculate(operation, values):
    values = [positive(value) for value in values]
    required = {"ohm": 2, "gain": 2, "divider": 3, "parallel": 2, "rc": 2, "median": 3}
    if operation not in required or len(values) != required[operation]:
        raise ValueError("Operación o cantidad de valores incorrecta.")
    a, b = values[:2]
    if operation == "ohm":
        return a / b
    if operation == "gain":
        return -b / a
    if operation == "divider":
        vin, r1, r2 = values
        return vin * r2 / (r1 + r2)
    if operation == "parallel":
        return 1 / (1 / a + 1 / b)
    if operation == "rc":
        return a * b
    return statistics.median(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["ohm", "gain", "divider", "parallel", "rc", "median"])
    parser.add_argument("values", type=float, nargs="+")
    args = parser.parse_args()
    try:
        result = calculate(args.operation, args.values)
        if not math.isfinite(result):
            raise ValueError("Resultado fuera del rango numérico.")
        print(f"{result:.8g}")
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
