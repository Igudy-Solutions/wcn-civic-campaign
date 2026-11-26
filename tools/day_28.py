#!/usr/bin/env python3
"""Day 28: Sat 19 Dec 2026. Single. Know the Candidates.

35 to 79: the age range of the presidential candidates. Facts only, no names.
Youngest 35, oldest 79; running mates 35 to 74 (INEC final list).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 28
OUT = folder_for(DAY)

SLIDES = [
    ("stat", dict(
        kicker="The 2027 presidential ballot",
        lead="The youngest candidate is 35. The oldest is 79.",
        number="35\u201379",
        size=250,
        label="The age range of the people\n*asking for your vote.*",
        body="Their running mates range from 35 to 74. Age alone tells you nothing. The plan and the record tell you more.",
        photo="ai-06-walk-to-vote.png",
        pos="50% 15%",
        source="INEC final list",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
