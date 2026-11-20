#!/usr/bin/env python3
"""Day 54: Mon 23 Nov 2026. Single. Vote Wisely.

A slogan is not a plan. Three questions to put to any promise.
No candidate, party or slogan is named or quoted.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 54
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        lead="Catchy. Loud. Everywhere.\nBefore you repeat it, ask three things.",
        punch="A slogan is\nnot a plan.",
        size=140,
        body="**How** will it be done? With **what money**? By **when**? No answer, no plan.",
        photo="ai-14-town-hall.png",
        pos="50% 20%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
