#!/usr/bin/env python3
"""Day 47: Mon 30 Nov 2026. Carousel. Vote Wisely.

Popular is not the same as prepared. Five checks before you choose.
Spine: hook -> loud is not ready -> five checks, one per slide -> run all
five on everyone you're considering. Applies to every candidate equally.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 47
OUT = folder_for(DAY)

CHECKS = [
    ("What have they\nactually done?", "Look at the record in past jobs or offices, not the promises.", "ai-06-walk-to-vote.png"),
    ("A plan, or only\na slogan?", "Ask how, with what money and by when.", "ai-14-town-hall.png"),
    ("Who is on\nthe team?", "Running mates and appointees do much of the work. Know them too.", "ai-04-friends-debate.png"),
    ("Do they face\nhard questions?", "Watch debates and interviews. How they answer matters as much as what.", "ai-15-bus-stop-phone.png"),
    ("Do the numbers\nadd up?", "Big promises need real money. Ask where it comes from.", "ai-11-market-trader.png"),
]

SLIDES = [
    ("cover", dict(
        title="Popular is not\nthe same as\n*prepared.*",
        size=128,
        photo="ai-03-public-count.png",
    )),
    ("statement", dict(
        lead="Crowds, jingles and trending hashtags\ntell you who is loud.",
        punch="Not who\nis ready.",
        body="Five checks for any candidate, for any office. Swipe.",
        photo="ai-14-town-hall.png",
    )),
] + [
    ("statement", dict(kicker=f"Check {i} of 5", punch=q, size=112, body=b, photo=p))
    for i, (q, b, p) in enumerate(CHECKS, 1)
] + [
    ("cta", dict(
        lead="Run all five checks on every candidate\nyou're considering.",
        punch="Then choose\nfor yourself.",
        body="Save this for later. Share it with someone deciding.",
        photo="ai-02-inked-thumb.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
