# Four-band Resistor Decoder

Decode nominal resistance and tolerance from four English color names.

## Origin

New learning implementation created in November 2026 to revisit topics from earlier coursework. It is not presented as an exact recovery of a deleted source file.

## Requirements

Python 3.10+; standard library only. Run commands from this project folder.

## Run

```powershell
python resistor.py brown black red gold
python resistor.py --help
```

Expected output: 1000 ohms ±5%. Supports standard digit colors, gold/silver multipliers and supported tolerance bands. It models four-band resistors only.

## Files

- [resistor.py](resistor.py): implementation and CLI.

## Verification

Behavior and invalid input are covered in [the collection tests](../../tests/test_tools.py). Run python -m unittest discover -s tests -v from the repository root.
