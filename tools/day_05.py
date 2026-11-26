#!/usr/bin/env python3
"""Day 5: Mon 11 Jan 2027. Single. Peaceful Participation.

If trouble starts, walk away. Your life first.
No hotline numbers on the slide (VERIFY any reporting channel first).
Photo: ai-06-walk-to-vote.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 5
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        lead="Shouting, pushing, snatching boxes?\nDon't film it up close. Don't join in.",
        punch="If trouble\nstarts, *walk\naway.*",
        size=130,
        body="Leave calmly, keep your people close, and tell the police or INEC officials when you're safe. Your life first.",
        photo="ai-06-walk-to-vote.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
