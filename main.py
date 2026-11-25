#!/usr/bin/env python3
"""Write one funny tech-support line to /output/entry.txt.

Entry for make.fun competition
u-motasimfuad-have-you-tried-turning-it-off-154a938b.
Python 3.13 standard library only; no network at run time.
"""

import os

LINE = "Ma'am, your computer isn't frozen \u2014 it's meditating, and honestly it's coping better than I am."


def main():
    # Gate assertions: exactly one line, 1-199 characters, non-empty.
    assert LINE.strip(), "entry must not be empty or only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 199, "entry must be 1-199 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read and re-check what was actually written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written output differs from the entry line"


if __name__ == "__main__":
    main()
