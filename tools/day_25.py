#!/usr/bin/env python3
"""Day 25: Tue 22 Dec 2026. Single. Peaceful Participation.

This Christmas, talk politics without the fight. Holiday family conversations.
Photo: ai-13-family-table.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 25
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        lead="The whole family is home.\nSomeone will bring up the election.",
        punch="Talk politics.\n*Skip the fight.*",
        size=126,
        body="Ask, listen, keep it about issues, and know when to pass the rice. Family first, every year.",
        photo="ai-13-family-table.png",
        pos="50% 18%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
