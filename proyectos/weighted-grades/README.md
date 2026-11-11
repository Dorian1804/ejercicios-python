# Weighted Grade Calculator

Calculate a weighted grade from command-line grade:weight pairs.

## Origin

New learning implementation created in November 2026 to revisit topics from earlier coursework. It is not presented as an exact recovery of a deleted source file.

## Requirements

Python 3.10+; standard library only. Run commands from this project folder.

## Run

```powershell
python grades.py 80:40 100:60
python grades.py --help
```

Expected output: Weighted grade: 92.00. Grades use a 0–100 scale; weights must be positive and add up to 100 percent. Invalid and nonfinite values are rejected.

## Files

- [grades.py](grades.py): implementation and CLI.

## Verification

Behavior and invalid input are covered in [the collection tests](../../tests/test_tools.py). Run python -m unittest discover -s tests -v from the repository root.
