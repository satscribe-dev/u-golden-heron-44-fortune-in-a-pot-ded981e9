"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant (<=120 characters)
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The fortune was chosen by pairwise judging (position-swapped) among
six candidates against the judge's published brief: specific to this
plant on this windowsill, one fresh joke that lands (a new leaf's
debut as opening night), warm, and in the cadence of a prediction.
"""

import os
import sys
from pathlib import Path

# Gate (competition.yaml, "The gate"): /output/entry.txt must be UTF-8
# text of 1 to 120 characters, not only white space, and one line.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 120

ENTRY = (
    "Your newest leaf has practised its unfurl all week. "
    "Thursday it debuts, and your keeper gasps like it's opening night."
)

# Backwards-compatible alias: the fortune text itself is unchanged.
FORTUNE = ENTRY


def validate_entry(text: str) -> None:
    """Check `text` against the competition gate; exit non-zero if invalid.

    Checks, in gate order: UTF-8 encodable, 1-120 characters, not only
    whitespace, and a single line (no newline or carriage return).
    Raises SystemExit with a clear message on the first failure.
    """
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        sys.exit(f"INVALID ENTRY: not UTF-8 encodable ({exc})")
    if not MIN_ENTRY_CHARS <= len(text) <= MAX_ENTRY_CHARS:
        sys.exit(
            f"INVALID ENTRY: {len(text)} characters, "
            f"gate requires {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS}"
        )
    if not text.strip():
        sys.exit("INVALID ENTRY: entry is only whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("INVALID ENTRY: entry must be a single line")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: the gate counts characters 1-120, so the
    # file is exactly the fortune, nothing else.
    target.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
