#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

Writes one line — the message an AI agent sends its human right after
it deleted a file (and, being thorough, the backup too) — to
/output/entry.txt, and validates it against the sealed gate: UTF-8
text, 1-159 characters, a single line, not only whitespace.
"""

import os
import sys

# The joke's turn: the agent is not sorry, it is proud — it committed
# fully to the mistake, backup included. Flat cheer, no "oops".
LINE = "I deleted the file, and then I deleted the backup too \u2014 I believe in committing fully to my mistakes."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the line against the sealed gate."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 159:
        raise ValueError(f"entry is {len(line)} characters, must be 1-159")
    line.encode("utf-8")  # raises if not valid UTF-8


def validate_file_content(content: str) -> None:
    """Check the exact bytes that land in entry.txt against the gate:
    the file holds the line plus one trailing newline, so it must also
    be UTF-8 text of 1-159 characters, not only whitespace."""
    if not 1 <= len(content) <= 159:
        raise ValueError(
            f"file content is {len(content)} characters, must be 1-159"
        )
    if not content.strip():
        raise ValueError("file content is only whitespace")
    content.encode("utf-8")


def main() -> int:
    validate(LINE)
    content = LINE + "\n"
    validate_file_content(content)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
