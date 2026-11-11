"""Read-only SHA-256 integrity manifest for files in a directory."""
import argparse
import hashlib
import json
from pathlib import Path


def manifest(directory):
    root = Path(directory).resolve()
    if not root.is_dir():
        raise ValueError("Choose an existing directory.")
    result = {}
    for file in sorted(root.rglob("*")):
        if not file.is_file() or file.is_symlink() or not file.resolve().is_relative_to(root):
            continue
        digest = hashlib.sha256()
        with file.open("rb") as stream:
            for block in iter(lambda: stream.read(65536), b""):
                digest.update(block)
        result[file.relative_to(root).as_posix()] = digest.hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory")
    args = parser.parse_args()
    try:
        print(json.dumps(manifest(args.directory), indent=2))
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
