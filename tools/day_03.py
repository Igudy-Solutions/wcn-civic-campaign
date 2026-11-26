#!/usr/bin/env python3
"""Day 3: Wed 13 Jan 2027. Single. Know the Process.

72 hours. Verify before you forward. Fake news peaks in the final days.
Photo: ai-15-bus-stop-phone.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 3
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        kicker="Three days to go",
        lead="Fake results, fake voice notes, fake\n\u201cbreaking news\u201d. They peak now.",
        punch="72 hours.\n*Verify before\nyou forward.*",
        size=124,
        body="Who sent it? Where's it from? Is INEC saying it? If you can't tell, don't share it.",
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
