#!/usr/bin/env python3
"""Day 19: Mon 28 Dec 2026. Single. Know the Process.

Countdown single: 19 days. Tag one person who has not collected their PVC.
Photo: ai-08-pvc-collection.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 19
OUT = folder_for(DAY)

SLIDES = [
    ("countdown", dict(
        days=19,
        kicker="Saturday 16 January 2027",
        big=340,
        title="days. *Tag one person\nwithout a PVC.*",
        size=100,
        body="You know who they are. No PVC, no vote. INEC office in their LGA, in person.",
        photo="ai-08-pvc-collection.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
