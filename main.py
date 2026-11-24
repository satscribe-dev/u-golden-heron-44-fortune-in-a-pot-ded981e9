"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant (<=120 characters)
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The fortune was chosen by pairwise judging (position-swapped) among
six candidates against the judge's published brief: specific to this
plant on this windowsill, one fresh joke that lands (a new leaf's
debut as opening night), warm, and in the cadence of a prediction.
"""

import os
from pathlib import Path

FORTUNE = (
    "Your newest leaf has practised its unfurl all week. "
    "Thursday it debuts, and your keeper gasps like it's opening night."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: the gate counts characters 1-120, so the
    # file is exactly the fortune, nothing else.
    target.write_text(FORTUNE, encoding="utf-8")
    print(f"wrote {len(FORTUNE)} characters to {target}")


if __name__ == "__main__":
    main()
