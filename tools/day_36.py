#!/usr/bin/env python3
"""Day 36: Fri 11 Dec 2026. Single. Know the Process.

Countdown single: 36 days. Your polling unit is printed on your PVC.
Polling units can move or be added, so check before January.
Photo: ai-16-pvc-proud-card (voter card face drawn in by tools/pvc_card.py).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 36
OUT = folder_for(DAY)

SLIDES = [
    ("countdown", dict(
        days=36,
        kicker="Saturday 16 January 2027",
        big=320,
        title="days. *Do you know\nyour polling unit?*",
        size=100,
        body="It's printed on your PVC. Units can move, so confirm yours with INEC before January.",
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
