#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes one line (a single deadpan terms-of-service clause that quietly
turns absurd) to /output/entry.txt.
"""

import os

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "By using this service, you agree to mail the Company one (1) live duck, "
    "postage prepaid, within thirty (30) days of first reading this clause."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_ENTRY_CHARS, (
        f"entry is {len(ENTRY)} chars, must be 1-{MAX_ENTRY_CHARS}"
    )
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
