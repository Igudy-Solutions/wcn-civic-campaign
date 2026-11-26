#!/usr/bin/env python3
"""Day 38: Wed 9 Dec 2026. Carousel. Vote Wisely.

"They are all the same?" Here is how to actually compare them.
Spine: hook -> they're not the same, compare like an employer -> four things
to put side by side (plan, record, team, money) -> make your own scorecard.
Applies to every candidate equally.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 38
OUT = folder_for(DAY)

COMPARE = [
    ("The plan", "Is it specific? Does it say how, by when\nand with what money?", "ai-15-bus-stop-phone.png"),
    ("The record", "What did they actually do in their last\njob, office or business?", "ai-06-walk-to-vote.png"),
    ("The team", "Running mate, party, allies. Who would\nrun things with them?", "ai-04-friends-debate.png"),
    ("The money", "Can the promises be paid for?\nAsk where it comes from.", "ai-11-market-trader.png"),
]

SLIDES = [
    ("cover", dict(
        title="\u201cThey're all\nthe same.\u201d\n*Here's how to\ncompare them.*",
        size=116,
        photo="ai-14-town-hall.png",
    )),
    ("statement", dict(
        lead="They're not all the same.\nBut slogans make them sound it.",
        punch="Compare them\nlike you're\nhiring.",
        size=124,
        body="Put any two candidates side by side on these four things.",
        photo="ai-13-family-table.png",
    )),
] + [
    ("statement", dict(kicker=f"Compare {i} of 4", punch=h, size=132, lead=None, body=b.replace("\n", " "), photo=p))
    for i, (h, b, p) in enumerate(COMPARE, 1)
] + [
    ("cta", dict(
        lead="Score them yourself, one to five,\non each of the four.",
        punch="Your scorecard.\nYour choice.",
        body="Save this and use it before 16 January.",
        photo="ai-02-inked-thumb.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
