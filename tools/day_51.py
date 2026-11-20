#!/usr/bin/env python3
"""Day 51: Thu 26 Nov 2026. Single. Peaceful Participation.

No candidate is worth your life. Disagreement is not a reason for violence.
Photo: ai-12-handshake (two young men shaking hands outside a polling unit).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 51
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        lead="Disagree. Argue. Debate.\nThen shake hands.",
        punch="No candidate\nis worth\nyour life.",
        size=132,
        body="If trouble starts at your polling unit, walk away and tell the police or INEC officials. Politicians move on. Neighbours stay.",
        photo="ai-12-handshake.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
