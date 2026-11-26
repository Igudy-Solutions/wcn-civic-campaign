#!/usr/bin/env python3
"""Day 8: Fri 8 Jan 2027. Carousel. Know Your Power.

Almost 40 percent of the 2023 register was 18 to 34.
Spine: hook -> 37m young registered voters in 2023 -> that's enough to swing
any race -> 2027 register over 103m -> show up and bring friends.
Facts: INEC 2023 register by age (18-34: 37.06m of 93.47m = 39.6%).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 8
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Almost 40%\nof the 2023\nregister was\n*18 to 34.*",
        size=124,
        photo="ai-23-inked-group.png",
    )),
    ("stat", dict(
        kicker="2023 voter register",
        lead="Registered voters aged 18 to 34:",
        number="37m",
        label="young Nigerians. *Out of 93.4m.*",
        photo="ai-04-friends-debate.png",
        source="INEC",
    )),
    ("statement", dict(
        lead="The 2023 presidential race was decided\nby about 1.8 million votes.",
        punch="Young voters\ncan decide\nany race.",
        size=124,
        body="If they show up.",
        photo="ai-15-bus-stop-phone.png",
    )),
    ("statement", dict(
        lead="The 2027 register: over 103 million.",
        punch="The youth\nvote is the\nbiggest bloc.",
        size=124,
        body="It only counts on the day it turns up.",
        photo="ai-01-polling-queue.png",
        source="INEC",
    )),
    ("cta", dict(
        lead="Show up, and bring your friends.\nThat's how a bloc becomes a result.",
        punch="Show up.\nBring three.",
        body="Tag the friends you're going with.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
