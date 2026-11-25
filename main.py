#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes one line (a single deadpan terms-of-service clause that quietly
turns absurd) to /output/entry.txt.
"""

import os

ENTRY = (
    "By using this service, you agree to mail the Company one (1) live duck, "
    "postage prepaid, within thirty (30) days of first reading this clause."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
