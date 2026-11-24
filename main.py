#!/usr/bin/env python3
"""Write the one-word boss entry to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1-30 characters, not only
whitespace, a single word with no spaces.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        text = f.read()
    stripped = text.strip()
    if not stripped or len(stripped) > 30:
        print("entry must be 1-30 non-whitespace characters", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in stripped):
        print("entry must be a single word with no spaces", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 for ch in stripped):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    tmp = os.path.join(HERE, ".entry.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(stripped)
    shutil.copyfile(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)
    os.remove(tmp)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
