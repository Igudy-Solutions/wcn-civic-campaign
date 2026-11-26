#!/usr/bin/env python3
"""Day 22: Fri 25 Dec 2026. Single. Peaceful Participation.

Merry Christmas. Peace at home, peace at the polls. 25 Dec.
Photo: ai-24-peace-walk (pastor and imam walking together with neighbours).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 22
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        kicker="25 December",
        lead="From all of us at World Changers Network:",
        punch="Merry\nChristmas.",
        size=150,
        body="Peace at home. Peace at the polls. We go into January as neighbours, whoever we vote for.",
        photo="ai-24-peace-walk.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
