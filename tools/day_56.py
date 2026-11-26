#!/usr/bin/env python3
"""Day 56: Sat 21 Nov 2026. Single. Know the Process.

Countdown single that turns the number into a question: where is your PVC?
Facts: PVC collected in person at your INEC LGA office (INEC).
Photo: ai-16-pvc-proud-card (AI photo; tools/pvc_card.py draws a generic
voter-card face on the card). Number set to 320 so it clears the card.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 56
OUT = folder_for(DAY)

SLIDES = [
    ("countdown", dict(
        days=56,
        kicker="Saturday 16 January 2027",
        title="days. *Where is\nyour PVC right now?*",
        big=320,
        size=104,
        body="Not “somewhere at home”. In your hand. Not collected yet? Go to your INEC LGA office, in person.",
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
        source="INEC",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
