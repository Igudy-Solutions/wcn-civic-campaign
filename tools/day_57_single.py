#!/usr/bin/env python3
"""Day 57, the single image. Fri 20 Nov 2026.

The countdown on its own, for a feed post or an X post that stands alone.
Lands in `Day 57 - .../single/01-post.png`.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 57
OUT = folder_for(DAY) + "/single"

SLIDES = [
    ("countdown", dict(
        days=57,
        kicker="Saturday 16 January 2027",
        title="days to\n*election day.*",
        size=150,
        body="Collect your PVC. Know your polling unit. Show up.",
        photo="ai-06-walk-to-vote.png",
        pos="50% 20%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
