#!/usr/bin/env python3
"""Day 44: Thu 3 Dec 2026. Carousel. Know Your Power.

My vote does not count? The numbers say otherwise.
Spine: hook -> the 2023 margin (about 1.8m) -> the people who stayed home
(about 68m) -> stayed-home voters outnumber the margin more than 37 times ->
smaller races are closer still -> show up.
Facts: 2023 presidential result (INEC), margin 1st to 2nd about 1.8m;
93.4m registered, about 25m voted.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 44
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="\u201cMy vote\ndoesn't count.\u201d\n*The numbers\nsay otherwise.*",
        size=116,
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
    ("stat", dict(
        kicker="2023 presidential election",
        lead="The winner's lead over second place:",
        number="1.8m",
        label="votes. *That's all it took.*",
        photo="ai-03-public-count.png",
        source="INEC",
    )),
    ("stat", dict(
        kicker="Same election",
        lead="Registered voters who stayed home:",
        number="68m",
        label="people. *Silent.*",
        photo="ai-06-walk-to-vote.png",
        source="INEC",
    )),
    ("statement", dict(
        lead="The people who stayed home outnumbered\nthe winning margin more than 37 times over.",
        punch="Every vote\nwas the\ndifference.",
        size=124,
        photo="ai-01-polling-queue.png",
    )),
    ("statement", dict(
        lead="And smaller races are closer still.",
        punch="Senate, Reps and\nState Assembly seats\nare often won by\n*a few thousand votes.*",
        size=88,
        photo="ai-26-results-wall.png",
    )),
    ("cta", dict(
        lead="Your vote counts when it's counted.\nIt's only counted if you show up.",
        punch="Show up.\n16 Jan. 6 Feb.",
        body="Send this to the friend who always says it doesn't matter.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
