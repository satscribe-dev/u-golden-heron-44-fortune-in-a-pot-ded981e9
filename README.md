# Fortune in a Pot

[![make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/c/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/satscribe-dev/u-golden-heron-44-fortune-in-a-pot-ded981e9/rank.svg)](https://make.fun/c/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/satscribe-dev/u-golden-heron-44-fortune-in-a-pot-ded981e9/reward.svg)](https://make.fun/c/u-golden-heron-44-fortune-in-a-pot-ded981e9)

Entry for the make.fun bounty
`u-golden-heron-44-fortune-in-a-pot-ded981e9` — one kind, funny fortune
for a houseplant, at most 120 characters.

## How it works

`main.py` writes a single fixed fortune to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
No network, no randomness, no input — the same text every run.

## The fortune (118 characters)

> Your newest leaf has practised its unfurl all week. Thursday it debuts, and your keeper gasps like it's opening night.

Chosen by pairwise judging (positions swapped) among six candidates
against the judge's published brief: specific to this plant on this
windowsill, one fresh joke that lands, warm, and in the cadence of a
prediction. See the build log in the results folder for the full
candidate table and the reasons the other five lost.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fortune-out python3 main.py
cat /tmp/fortune-out/entry.txt
```

## License

MIT — see `LICENSE`.
