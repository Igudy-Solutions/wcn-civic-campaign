#!/usr/bin/env python3
"""Day 23: Thu 24 Dec 2026. Carousel. Know the Process.

Travelling for Christmas? You can only vote where you registered.
Spine: hook -> the rule -> transfer window has closed -> plan your return ->
CTA. VERIFY: confirm with INEC that registration transfer is closed for the
2027 general election before posting.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 23
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Travelling for\nChristmas?\n*Plan your\nreturn to vote.*",
        size=120,
        photo="ai-18-bus-park.png",
        pos="50% 25%",
    )),
    ("statement", dict(
        lead="This is the rule most people find out too late.",
        punch="You can only\nvote where you\nregistered.",
        size=118,
        body="Your polling unit is printed on your PVC. That's the only place your vote can be cast.",
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
    ("statement", dict(
        lead="Moving your registration to another\nstate or polling unit?",
        punch="The transfer\nwindow has\nclosed.",
        size=118,
        body="For 16 January and 6 February, you vote at the unit on your card.",
        photo="ai-22-official-explains.png",
        source="INEC",
    )),
    ("list", dict(
        kicker="If you're travelling",
        title="Plan your\n*return*",
        size=96,
        items=[("Book your trip back early", "Roads and parks get busy in January"),
               ("Be home before the 16th", "Aim for the week before, not the night before"),
               ("Keep your PVC with you", "Or safe in the place you'll vote"),
               ("Plan for 6 February too", "Governor and State Assembly, same unit"),
               ("Expect limited movement", "Vehicle movement is usually restricted on election day")],
        photo="ai-19-airport.png",
    )),
    ("cta", dict(
        lead="Enjoy Christmas. Then come home and vote.",
        punch="Home by\nthe 16th.",
        body="Send this to the friend travelling for the holidays.",
        photo="ai-18-bus-park.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
