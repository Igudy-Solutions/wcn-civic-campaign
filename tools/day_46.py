#!/usr/bin/env python3
"""Day 46: Tue 1 Dec 2026. Single. Know Your Power.

Poll single: what matters most in a leader? Four options, people vote in the
comments (and on the Story poll). Non-partisan: qualities, not people.
Photo: ai-04-friends-debate.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 46
OUT = folder_for(DAY)

SLIDES = [
    ("list", dict(
        kicker="Quick poll",
        title="What matters\nmost in a *leader?*",
        size=104,
        items=[("Integrity", "Honest, keeps their word", "1"),
               ("Competence", "Can actually do the job", "2"),
               ("A clear plan", "Says how, with what, by when", "3"),
               ("Accountability", "Answers to the people", "4")],
        body="Pick one. Drop the number in the comments.",
        photo="ai-04-friends-debate.png",
        pos="50% 12%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
