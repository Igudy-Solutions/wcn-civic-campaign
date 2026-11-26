#!/usr/bin/env python3
"""Day 6: Sun 10 Jan 2027. Carousel. Peaceful Participation.

The peace pledge. Five promises for election week.
Spine: hook -> five promises in one list -> take the pledge.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 6
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="The peace\npledge. *Five\npromises for\nelection week.*",
        size=120,
        photo="ai-24-peace-walk.png",
        pos="50% 20%",
    )),
    ("list", dict(
        kicker="I promise",
        title="My\n*pledge*",
        size=96,
        items=[("I won't sell my vote", "Not for money, food or favours"),
               ("I won't spread unverified results", "I'll wait for INEC"),
               ("I won't join or start violence", "If trouble starts, I walk away"),
               ("I'll respect people who vote differently", "Neighbours before politics"),
               ("I'll use the law for disputes", "Not my fists, not the street")],
        photo="ai-12-handshake.png",
    )),
    ("cta", dict(
        lead="Comment \u201cI pledge\u201d and tag three\npeople to take it with you.",
        punch="I pledge.",
        size=170,
        body="Peaceful participation is a choice we make together.",
        photo="ai-24-peace-walk.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
