#!/usr/bin/env python3
"""Write one funny status-report line to /output/entry.txt.

Deterministic: the line is a fixed string, so every run produces
byte-identical output. Stdlib only, no network.

Before writing, the entry passes a self-check gate (see
``validate_entry``): the line must be non-empty and at most 200
characters. The gate fails loudly with a clear error instead of
writing a broken or oversized entry, so a bad edit can never
silently reach the output file.
"""

import os

MAX_ENTRY_CHARS = 200

ENTRY = (
    "Weekly report: 38 tasks completed, 2 apologies issued for things "
    "I definitely did, and I'm still waiting on the file you said "
    "you'd send on Tuesday."
)


def validate_entry(line: str) -> str:
    """Check the entry line before it is written; return it unchanged.

    Raises ValueError with a plain message when the line is empty
    (or only whitespace) or longer than MAX_ENTRY_CHARS.
    """
    if not line.strip():
        raise ValueError("entry line must not be empty")
    if len(line) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, "
            f"over the {MAX_ENTRY_CHARS}-character limit"
        )
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validate_entry(ENTRY) + "\n")


if __name__ == "__main__":
    main()
