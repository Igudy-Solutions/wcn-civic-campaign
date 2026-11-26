#!/usr/bin/env python3
"""Day 10: Wed 6 Jan 2027. Single. Know the Process.

Countdown single: 10 days. Photo: ai-02-inked-thumb.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 10
OUT = folder_for(DAY)

SLIDES = [
    ("countdown", dict(
        days=10,
        kicker="Saturday 16 January 2027",
        big=400,
        title="days. *Ready?*",
        size=120,
        body="PVC in hand. Polling unit confirmed. Route planned. Three friends coming with you.",
        photo="ai-02-inked-thumb.png",
        pos="50% 12%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
