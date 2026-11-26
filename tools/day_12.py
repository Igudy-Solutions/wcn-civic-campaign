#!/usr/bin/env python3
"""Day 12: Mon 4 Jan 2027. Single. Know Your Power.

Who you vote for is nobody's business. Your ballot is secret.
Photo: ai-07-ballot-box.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 12
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        lead="Not your boss's. Not your family's.\nNot the man with the money.",
        punch="Who you vote\nfor is *nobody's\nbusiness.*",
        size=124,
        body="Your ballot is secret. Don't show it, don't photograph it, and nobody can make you tell.",
        photo="ai-07-ballot-box.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
