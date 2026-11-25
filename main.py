#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who has just been
liquidated to <output dir>/entry.txt. Gate: 1-160 characters, at most
20 words, exactly one line, no trailing newline. Standard library only.

The fortune: the classic cookie trope (your lucky numbers) with the
punchline that they are all zero -- drawn by the exchange that just
liquidated the reader. Oracular opening, explicit loss, and the
exchange (not the trader) is the villain, so it stays rueful and warm.
"""

import os

FORTUNE = (
    "Your lucky numbers are 0, 0, and 0, drawn by the exchange that "
    "just liquidated you."
)


def main() -> None:
    text = FORTUNE.strip()
    # Gate: 1-160 characters, at most 20 words, exactly one line.
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert len(text.split()) <= 20, f"entry is {len(text.split())} words, max 20"
    assert "\n" not in text and text.strip(), "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)  # No trailing newline, per this bounty's brief.


if __name__ == "__main__":
    main()
