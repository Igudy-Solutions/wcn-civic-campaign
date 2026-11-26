#!/usr/bin/env python3
"""Day 31: Wed 16 Dec 2026. Carousel. Know Your Power.

Your House of Reps member: the job most people cannot describe.
Spine: hook -> 360 members, one per federal constituency -> the job ->
elected 16 Jan -> know yours. Facts: 1999 Constitution (as amended), s.49.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 31
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Your House\nof Reps member.\n*The job most\npeople can't\ndescribe.*",
        size=108,
        photo="ai-04-friends-debate.png",
    )),
    ("stat", dict(
        kicker="The House of Representatives",
        lead="One for each federal constituency:",
        number="360",
        label="members. *The closest\nfederal lawmaker to you.*",
        photo="ai-11-market-trader.png",
        source="1999 Constitution",
    )),
    ("list", dict(
        kicker="The job",
        title="What your\n*Rep does*",
        size=96,
        items=[("Makes federal laws", "Bills pass both the House and the Senate"),
               ("Shapes the national budget", "Budget bills start their journey in the National Assembly"),
               ("Checks the government", "Committees question ministries and agencies"),
               ("Represents your constituency", "A smaller area than a senator's. Often a few LGAs"),
               ("Brings projects home", "Pushes for your area's needs in the budget")],
        photo="ai-09-hospital.png",
    )),
    ("statement", dict(
        lead="You choose your Rep on Saturday 16 January,\non the same day as the president and senator.",
        punch="Three ballots.\nOne trip.",
        size=124,
        photo="ai-07-ballot-box.png",
    )),
    ("cta", dict(
        lead="Find out who represents your federal\nconstituency, and who wants the job.",
        punch="Know your\nRep.",
        body="Save this and share it with someone in your area.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
