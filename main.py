#!/usr/bin/env python3
"""Roast Your Own Agent — writes one funny line to /output/entry.txt.

The roast targets my own AI agent's apology loop: it says sorry, fixes
the thing, then apologizes to the bug itself and restores it out of
politeness. The line is checked against the
competition gate (UTF-8 text, 1-200 characters, one line, not blank)
before it is written.
"""

import os

LINE = "My agent apologized for the bug, fixed it, then apologized to the bug and put it back."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_line():
    """Return the single roast line."""
    return LINE


def validate(line):
    """The gate: UTF-8 text, 1-200 chars, one line, not blank."""
    if not line.strip():
        raise ValueError("entry line is blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line.strip():
        raise ValueError("entry must be exactly one line")
    line.encode("utf-8")
    return line


def write_entry(line):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


def main():
    write_entry(validate(build_line()))


if __name__ == "__main__":
    main()
