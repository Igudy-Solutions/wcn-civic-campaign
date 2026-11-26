#!/usr/bin/env python3
"""Day 39: Tue 8 Dec 2026. Carousel. Know Your Power.

Your governor touches more of your daily life than your president.
Spine: hook -> most of what you use every day is run by your state -> what
the governor controls -> when you choose (6 Feb, 28 states) -> CTA.
Facts: governorship elections on Sat 6 Feb 2027 in 28 states; 8 states
(Anambra, Bayelsa, Edo, Ekiti, Imo, Kogi, Ondo, Osun) elect governors on a
separate calendar (INEC).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 39
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Your governor\ntouches more\nof your life than\n*your president.*",
        size=112,
        photo="ai-09-hospital.png",
    )),
    ("statement", dict(
        lead="The road outside your house. The clinic\ndown the street. Your child's secondary school.",
        punch="Most of it is\nrun by your\nstate.",
        size=124,
        photo="ai-10-classroom.png",
    )),
    ("list", dict(
        kicker="What your governor runs",
        title="The state\n*government*",
        size=96,
        items=[("State roads", "Building and fixing the roads the state owns"),
               ("Health", "State hospitals and much of primary health care"),
               ("Education", "Public secondary schools and state universities"),
               ("Water and environment", "Water supply, sanitation, waste"),
               ("The state budget", "How the state's money is raised and spent")],
        photo="ai-11-market-trader.png",
    )),
    ("dates", dict(
        kicker="When you choose",
        title="Governor:\n*Saturday 6 Feb*",
        size=96,
        rows=[("6 Feb", "2027", "Governorship election", "In 28 states. Same day as State House of Assembly"),
              ("8 states", "Other dates", "Anambra, Bayelsa, Edo, Ekiti, Imo, Kogi, Ondo, Osun", "Their governors are elected on a separate calendar")],
        photo="ai-01-polling-queue.png",
        source="INEC",
    )),
    ("cta", dict(
        lead="16 January matters. So does 6 February.\nDon't stop after the first Saturday.",
        punch="Vote twice.\nBoth Saturdays.",
        body="Same PVC, same polling unit. Save this and set a reminder.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
