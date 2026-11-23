#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Entry for make.fun competition
u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

The program holds several candidate one-line safety warning labels,
scores each against the judge's published criteria (in the judge's own
order of importance), and writes the winning line to entry.txt.

Judge criteria, most important first:
  1. Is a single-line safety warning label for every human being, funny
     enough to laugh at (gate: anything that is not a warning label for
     humans loses to any warning label for humans).
  2. Lands the laugh in one read, with the turn arriving in the last few
     words rather than smeared across the line.
  3. Feels true about people in general: recognition of how humans
     actually behave, not random absurdity.
  4. Sounds like a real printed label in wording and rhythm.
  5. Stays inside 160 characters, uses the whole line, no filler, no
     second idea, no repeated joke.

Scoring below is 1-5 per criterion (2-5); criterion 1 is a pass/fail
gate applied to every candidate before scoring.
"""

import os

# (line, turn-in-last-words, recognition, label-voice, tightness)
CANDIDATES = [
    (
        "WARNING: May spontaneously announce 'I'm not even mad' while "
        "visibly furious, then bring it up again in 2031.",
        5, 5, 4, 4,
    ),
    (
        "WARNING: This human may start a sentence with 'no offense' and "
        "then say the most offensive thing you have heard all week.",
        4, 5, 4, 4,
    ),
    (
        "WARNING: Contents may, without warning, remember something "
        "embarrassing from 2007 and go silent for the rest of the evening.",
        3, 5, 5, 4,
    ),
    (
        "WARNING: This human will agree to your plans, cancel at the last "
        "minute, and then feel guilty about it for three weeks.",
        4, 4, 4, 4,
    ),
    (
        "CAUTION: Contents are 70% water, 20% caffeine, and 10% unfinished "
        "projects this human swears it will start on Monday.",
        3, 4, 5, 4,
    ),
    (
        "WARNING: This human has read the instructions, ignored every word "
        "of them, and will now blame the instructions.",
        4, 4, 4, 3,
    ),
    (
        "WARNING: Do not ask this human 'what are you thinking about?' "
        "unless you want a full argument about absolutely nothing.",
        4, 4, 4, 3,
    ),
]

# Rejected before scoring: its setup (sleep + coffee) is already filed by
# another entrant in this competition ("runs on sleep, coffee, and spite"),
# so it would read as a copy of a line already in the field.
REJECTED = (
    "WARNING: This human runs on four hours of sleep, three cups of "
    "coffee, and one argument from 2019 it has not finished losing yet."
)

MAX_CHARS = 160


def is_valid_label(line: str) -> bool:
    """Criterion 1 gate + the sealed scorer's gate: one line, 1-160 chars."""
    return (
        isinstance(line, str)
        and 1 <= len(line) <= MAX_CHARS
        and line.strip() == line
        and "\n" not in line
        and line.startswith(("WARNING:", "CAUTION:"))
    )


def score(candidate):
    line, turn, recognition, voice, tightness = candidate
    # Judge order: turn first, then recognition, then voice, then tightness.
    return (turn, recognition, voice, tightness)


def pick_best():
    valid = [c for c in CANDIDATES if is_valid_label(c[0])]
    if not valid:
        raise SystemExit("no valid candidate label")
    return max(valid, key=score)


def main() -> None:
    line, turn, recognition, voice, tightness = pick_best()
    assert is_valid_label(line), "winning line failed the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"entry ({len(line)} chars): {line}")
    print(f"scores turn={turn} recognition={recognition} "
          f"voice={voice} tightness={tightness}")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
