#!/usr/bin/env python3
"""Day 14: Sat 2 Jan 2027. Carousel. Know the Process.

Two weeks to go. Your election checklist.
Spine: hook -> five things to sort this week -> the two dates -> CTA.
VERIFY any INEC procedure mentioned before posting.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 14
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Two weeks\nto go. *Your\nelection\nchecklist.*",
        size=126,
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
    ("list", dict(
        kicker="Sort these this week",
        title="Your\n*checklist*",
        size=96,
        items=[("PVC in your hand", "Not \u201csomewhere at home\u201d. Find it today"),
               ("Know your polling unit", "It's on your PVC. Confirm it with INEC"),
               ("Plan your route", "Walk it or drive past once. Movement will be limited on the day"),
               ("Plan the day", "Go early. Water, umbrella, patience"),
               ("Bring three people", "Agree now who you're going with")],
        photo="ai-01-polling-queue.png",
    )),
    ("dates", dict(
        kicker="Mark both",
        title="Two\n*Saturdays*",
        size=96,
        rows=[("16 Jan", "Saturday", "President, Senate, House of Reps", "Three ballots"),
              ("6 Feb", "Saturday", "Governor and State House of Assembly", "Governor in 28 states, Assembly in all 36")],
        photo="ai-06-walk-to-vote.png",
        source="INEC",
    )),
    ("cta", dict(
        lead="Tick all five, then send this to the\nthree people you're going with.",
        punch="Ready in\ntwo weeks.",
        body="Save this checklist.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
