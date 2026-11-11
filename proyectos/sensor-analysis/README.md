# Sensor CSV Analysis

Summarize a numeric CSV column: sample count, range, mean, median and sample standard deviation.

## Origin

New learning implementation created in November 2026 to revisit topics from earlier coursework. It is not presented as an exact recovery of a deleted source file.

## Requirements

Python 3.10+; standard library only. Run commands from this project folder.

## Run

```powershell
python analyze.py readings.csv --column y_V
python analyze.py --help
```

Create a CSV with a header named y_V and one finite numeric reading per row. Missing columns, empty files and nonfinite values are rejected. The script reads the CSV without changing it.

## Files

- [analyze.py](analyze.py): implementation and CLI.

## Verification

Behavior and invalid input are covered in [the collection tests](../../tests/test_tools.py). Run python -m unittest discover -s tests -v from the repository root.
