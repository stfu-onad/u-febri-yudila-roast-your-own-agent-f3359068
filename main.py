#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt."""

ENTRY = "My agent apologized for the bug, fixed a different bug, then apologized for apologizing \u2014 and billed it as 'iterative progress.'"


def main():
    import os
    # Gate: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
