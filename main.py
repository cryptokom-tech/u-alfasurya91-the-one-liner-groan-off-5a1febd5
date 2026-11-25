#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original dad joke to the output file. The joke plays on two
meanings of "date": every square on a calendar is a date, and showing up
for one is what a hopeful dad does. "Days are numbered" sets the turn up
and the last word lands it.

The program checks its own line before writing: UTF-8 text, a single
line, 1 to 140 characters, not only white space. It uses only the
standard library, touches no network, and writes identical bytes on
every run.
"""

import os
import sys

JOKE = "My calendar's days are numbered, but it still shows up for every date."
MAX_CHARS = 140


def check(text):
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"joke is {len(text)} characters; limit is {MAX_CHARS}")
    if not text.strip():
        raise SystemExit("joke is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    check(JOKE)
    folder = os.path.dirname(out_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)
    with open(out_path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != JOKE:
        raise SystemExit("written text does not match the joke")
    print(f"wrote {len(back)} characters to {out_path}")


if __name__ == "__main__":
    main(sys.argv)
