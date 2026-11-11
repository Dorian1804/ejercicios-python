# Expense CSV Summary

Group expense amounts by category using exact decimal arithmetic.

## Origin

New learning implementation created in November 2026 to revisit topics from earlier coursework. It is not presented as an exact recovery of a deleted source file.

## Requirements

Python 3.10+; standard library only. Run commands from this project folder.

## Run

```powershell
python expenses.py expenses.csv
python expenses.py --help
```

Use the header category,amount and rows such as food,12.50. Amounts must be nonnegative and have at most two decimal places. The result is a category summary and a total; no financial recommendations are provided.

## Files

- [expenses.py](expenses.py): implementation and CLI.

## Verification

Behavior and invalid input are covered in [the collection tests](../../tests/test_tools.py). Run python -m unittest discover -s tests -v from the repository root.
