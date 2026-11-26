#!/usr/bin/env python3
"""Day 11: Tue 5 Jan 2027. Carousel. Know Your Power.

Five offices. Two Saturdays. The recap.
Spine: hook -> the two dates and what is on each ballot -> same PVC, same
polling unit -> CTA. Facts: INEC timetable.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 11
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Five offices.\nTwo Saturdays.\n*The recap.*",
        size=124,
        photo="ai-07-ballot-box.png",
    )),
    ("dates", dict(
        kicker="Saturday 16 January",
        title="Three\n*ballots*",
        size=96,
        rows=[("1", "Ballot", "President", "And vice president, on one ticket"),
              ("2", "Ballot", "Senate", "Your senatorial district"),
              ("3", "Ballot", "House of Reps", "Your federal constituency")],
        photo="ai-01-polling-queue.png",
        source="INEC",
    )),
    ("dates", dict(
        kicker="Saturday 6 February",
        title="Two\n*ballots*",
        size=96,
        rows=[("4", "Ballot", "Governor", "And deputy. In 28 states"),
              ("5", "Ballot", "State House of Assembly", "Your state constituency. All 36 states")],
        photo="ai-06-walk-to-vote.png",
        source="INEC",
    )),
    ("statement", dict(
        lead="Same PVC. Same polling unit. Both days.",
        punch="Don't stop\nat the first\nSaturday.",
        size=118,
        photo="ai-02-inked-thumb.png",
    )),
    ("cta", dict(
        lead="Five offices. Five choices. All yours.",
        punch="Vote both\nSaturdays.",
        body="Save this and share it with your family group.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
