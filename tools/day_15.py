#!/usr/bin/env python3
"""Day 15: Fri 1 Jan 2027. Single. Know Your Power.

Happy New Year. 2027 is the year you choose. 1 Jan.
Photo: ai-23-inked-group.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 15
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        kicker="1 January 2027",
        lead="Happy New Year from World Changers Network.",
        punch="2027 is the\nyear *you\nchoose.*",
        size=140,
        body="Two Saturdays: 16 January and 6 February. Make showing up your first resolution.",
        photo="ai-23-inked-group.png",
        pos="50% 12%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
