#!/usr/bin/env python3
"""Day 26: Mon 21 Dec 2026. Carousel. Know Your Power.

The election nobody talks about: your State House of Assembly.
Spine: hook -> every state elects one, on 6 Feb -> 24 to 40 members per
state -> what they do (incl. checking the governor) -> can you name yours.
Facts: 1999 Constitution (as amended), ss.90-93, 188; INEC timetable.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 26
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="The election\nnobody talks\nabout: *your State\nHouse of Assembly.*",
        size=108,
        photo="ai-14-town-hall.png",
    )),
    ("statement", dict(
        lead="Saturday 6 February, the same day as governor.\nIn all 36 states.",
        punch="Your state's\nlawmakers.",
        size=124,
        body="Each state has between 24 and 40 members, one for each state constituency.",
        photo="ai-01-polling-queue.png",
        source="1999 Constitution",
    )),
    ("list", dict(
        kicker="What they do",
        title="The job\n*nobody explains*",
        size=96,
        items=[("Make your state's laws", "From land and markets to local rules"),
               ("Approve the state budget", "The governor can't spend without it"),
               ("Check the governor", "Committees question ministries and contracts"),
               ("Can remove a governor", "Impeachment starts in the Assembly"),
               ("Represent your area", "Your member is a short drive away")],
        photo="ai-11-market-trader.png",
    )),
    ("statement", dict(
        lead="Most people vote for governor\nand skip the Assembly box.",
        punch="Don't skip it.",
        size=132,
        body="A governor with no one checking them is a governor with no limits.",
        photo="ai-07-ballot-box.png",
    )),
    ("cta", dict(
        lead="Find out who represents your state\nconstituency, and who wants to.",
        punch="6 Feb.\nTwo ballots.",
        body="Governor and State Assembly. Same PVC, same polling unit.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
