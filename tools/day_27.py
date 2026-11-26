#!/usr/bin/env python3
"""Day 27: Sun 20 Dec 2026. Carousel. Know the Candidates.

Women on the 2027 presidential ballot: how many?
2 of 18 presidential candidates and 4 of 18 running mates are women
(INEC final list). Facts and names only, ballot order, no endorsement.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 27
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Women on the\n2027 presidential\nballot. *How many?*",
        size=118,
        photo="ai-23-inked-group.png",
    )),
    ("stat", dict(
        kicker="Presidential candidates",
        lead="Out of 18 people running for president:",
        number="2",
        size=340,
        label="are women.",
        photo="ai-02-inked-thumb.png",
        source="INEC final list",
    )),
    ("stat", dict(
        kicker="Running mates",
        lead="Out of 18 vice presidential candidates:",
        number="4",
        size=340,
        label="are women.",
        photo="ai-22-official-explains.png",
        source="INEC final list",
    )),
    ("list", dict(
        kicker="In INEC's ballot order",
        title="The six\n*women*",
        size=96,
        items=[("Peace Egobia Ofordile", "Running mate · APP · Ticket 8", "8"),
               ("Nafisat Usaku Abubakar", "Running mate · DLA · Ticket 10", "10"),
               ("Hajja Bintu Konto", "Running mate · LP · Ticket 11", "11"),
               ("Ada Elizabeth Fredrick Okwori", "President · NDP · Ticket 13", "13"),
               ("Nkem Esther Okereke", "President · NRM · Ticket 14", "14"),
               ("Patience Ndidi Key", "Running mate · YPP · Ticket 18", "18")],
        photo="ai-07-ballot-box.png",
        source="INEC final list",
    )),
    ("cta", dict(
        lead="6 of the 36 names on the presidential\ntickets are women.",
        punch="Now you\nknow.",
        body="Information, not endorsement. Your vote, your choice.",
        photo="ai-27-wheelchair-voter.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
