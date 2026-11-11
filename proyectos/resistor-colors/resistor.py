"""Decode the nominal resistance of a four-band resistor."""
import argparse

DIGITS = {name: value for value, name in enumerate(["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white"])}
TOLERANCE = {"brown": 1, "red": 2, "green": .5, "blue": .25, "violet": .1, "gray": .05, "gold": 5, "silver": 10}


def decode(first, second, multiplier, tolerance):
    if first not in DIGITS or second not in DIGITS or first == "black":
        raise ValueError("First band must be brown–white; second band black–white.")
    if multiplier not in DIGITS and multiplier not in {"gold", "silver"}:
        raise ValueError("Invalid multiplier color.")
    if tolerance not in TOLERANCE:
        raise ValueError("Invalid tolerance color.")
    power = {"gold": -1, "silver": -2}.get(multiplier, DIGITS.get(multiplier))
    return (10 * DIGITS[first] + DIGITS[second]) * 10 ** power, TOLERANCE[tolerance]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("colors", nargs=4, metavar="COLOR", type=str.lower)
    args = parser.parse_args()
    try:
        resistance, tolerance = decode(*args.colors)
        print(f"{resistance:g} ohms ±{tolerance:g}%")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
