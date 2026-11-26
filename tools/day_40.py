#!/usr/bin/env python3
"""Day 40: Mon 7 Dec 2026. Single. Demand Accountability.

Public office is not a prize. It is a job. You are the employer.
Photo: ai-22-official-explains (polling official helping an elderly voter).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 40
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        lead="Public money pays them.\nThe public is the boss.",
        punch="Public office\nis not a prize.\n*It's a job.*",
        size=126,
        body="You're not crowning a winner. You're hiring someone to serve you for four years. Hire carefully.",
        photo="ai-22-official-explains.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
