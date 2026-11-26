#!/usr/bin/env python3
"""Day 34: Sun 13 Dec 2026. Carousel. Peaceful Participation.

No politician is worth your friendship. Five ways to argue without fighting.
Spine: hook -> it's okay to disagree -> five habits, one per slide -> CTA.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 34
OUT = folder_for(DAY)

WAYS = [
    ("Ask before\nyou argue.", "\u201cWhy do you like them?\u201d gets you further than \u201cYou're wrong.\u201d", "ai-04-friends-debate.png"),
    ("Talk issues,\nnot insults.", "Debate the plan. Leave tribe, religion and family out of it.", "ai-13-family-table.png"),
    ("Agree on\nthe facts first.", "If you can't agree what's true, check a trusted source together.", "ai-15-bus-stop-phone.png"),
    ("Know when\nto stop.", "When voices rise, change the subject. You can pick it up another day.", "ai-11-market-trader.png"),
    ("Their vote\nis theirs.", "You don't have to convince anyone. Respect the choice, keep the friend.", "ai-12-handshake.png"),
]

SLIDES = [
    ("cover", dict(
        title="No politician\nis worth your\n*friendship.*",
        size=128,
        photo="ai-12-handshake.png",
        pos="50% 15%",
    )),
    ("statement", dict(
        lead="Disagreeing is normal. It's democracy.",
        punch="Fighting\nis optional.",
        size=132,
        body="Five ways to talk politics and still be friends tomorrow.",
        photo="ai-04-friends-debate.png",
    )),
] + [
    ("statement", dict(kicker=f"Way {i} of 5", punch=h, size=126, body=b, photo=p))
    for i, (h, b, p) in enumerate(WAYS, 1)
] + [
    ("cta", dict(
        lead="Politicians move on after elections.\nYour friends and neighbours stay.",
        punch="Disagree.\nStay friends.",
        body="Send this to the group chat that gets heated.",
        photo="ai-24-peace-walk.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
