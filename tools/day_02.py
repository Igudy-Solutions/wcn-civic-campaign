#!/usr/bin/env python3
"""Day 2: Thu 14 Jan 2027. Single. Know the Process.

Campaigns end today (14 Jan): campaigning stops 24 hours before election
day. No candidate content from here. Photo: ai-01-polling-queue.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 2
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        kicker="Thursday 14 January",
        lead="By law, campaigning stops 24 hours\nbefore election day.",
        punch="Campaigns\nend today.",
        size=140,
        body="The jingles stop. The choice is yours now. PVC ready, polling unit confirmed, Saturday planned.",
        photo="ai-01-polling-queue.png",
        pos="50% 18%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
