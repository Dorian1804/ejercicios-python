# File Integrity Manifest

Generate a JSON SHA-256 manifest for a directory without modifying its contents.

## Origin

New learning implementation created in November 2026 to revisit topics from earlier coursework. It is not presented as an exact recovery of a deleted source file.

## Requirements

Python 3.10+; standard library only. Run commands from this project folder.

## Run

```powershell
python checksums.py ./samples
python checksums.py --help
```

Paths in the output are relative to the selected folder. Symbolic links and paths resolving outside the root are skipped. Output goes to stdout; save it outside the scanned directory to avoid hashing an earlier manifest. A checksum detects changes but does not encrypt or authenticate files.

## Files

- [checksums.py](checksums.py): implementation and CLI.

## Verification

Behavior and invalid input are covered in [the collection tests](../../tests/test_tools.py). Run python -m unittest discover -s tests -v from the repository root.
