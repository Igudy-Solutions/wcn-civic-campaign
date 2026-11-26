#!/usr/bin/env python3
"""Day 42: Sat 5 Dec 2026. Carousel. Demand Accountability.

Who checks the people in charge? You do.
Spine: hook -> elections are the big check, not the only one -> five ways
to hold leaders to account between elections -> then use your vote.
Non-partisan: applies to every office holder.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 42
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Who checks\nthe people\nin charge?\n*You do.*",
        size=128,
        photo="ai-14-town-hall.png",
        pos="50% 18%",
    )),
    ("statement", dict(
        lead="Voting is the biggest check you have.",
        punch="It's not\nthe only one.",
        size=124,
        body="Leaders answer to the people who watch them. Here's how to watch.",
        photo="ai-04-friends-debate.png",
    )),
    ("list", dict(
        kicker="Between elections",
        title="Five ways to\n*hold them to account*",
        size=88,
        items=[("Know who represents you", "Your Senator, Rep, State Assembly member and LG chair"),
               ("Show up to town halls", "Constituency meetings are open. Ask your question"),
               ("Follow the money", "Budgets are public documents. Ask what was spent where"),
               ("Track the promises", "Roads, schools, clinics in your area. Done or not?"),
               ("Speak up, peacefully", "Letters, petitions, community groups, the media")],
        photo="ai-26-results-wall.png",
    )),
    ("statement", dict(
        lead="Then, on election day,\nbring what you saw.",
        punch="Your vote is\nyour verdict.",
        size=124,
        photo="ai-02-inked-thumb.png",
    )),
    ("cta", dict(
        lead="Save this. Pick one thing to do\nthis month.",
        punch="Watch them.\nThen vote.",
        body="Non-partisan. It applies to whoever wins.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
