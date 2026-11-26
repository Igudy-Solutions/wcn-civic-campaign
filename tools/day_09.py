#!/usr/bin/env python3
"""Day 9: Thu 7 Jan 2027. Carousel. Know the Process.

Things that can get your vote cancelled.
Spine: hook -> what makes a ballot invalid (two slides) -> the cubicle rules
-> how to mark it right -> CTA. VERIFY against INEC's 2027 guidelines.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 9
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Things that\ncan get your\nvote *cancelled.*",
        size=126,
        photo="ai-07-ballot-box.png",
    )),
    ("list", dict(
        kicker="Your ballot can be rejected if",
        title="Don't\n*do this*",
        size=96,
        items=[("You mark more than one box", "One thumbprint, one box, per ballot"),
               ("Your ink touches two boxes", "A smudge across the line can void it"),
               ("You write or sign on it", "Any mark that identifies you")],
        photo="ai-02-inked-thumb.png",
    )),
    ("list", dict(
        kicker="And watch out for",
        title="These\n*too*",
        size=96,
        start=4,
        items=[("An unstamped ballot", "Check it's stamped and signed before you vote"),
               ("A torn or damaged ballot", "Ask the official for help before marking"),
               ("Phones in the cubicle", "Photographing your ballot is not allowed")],
        photo="ai-22-official-explains.png",
    )),
    ("statement", dict(
        lead="How to get it right:",
        punch="One thumb.\nOne box.\nFold it right.",
        size=118,
        body="Press firmly inside one box, let the ink settle, and fold the way the official shows you.",
        photo="ai-23-inked-group.png",
    )),
    ("cta", dict(
        lead="Don't queue for hours and lose\nyour vote to a smudge.",
        punch="Mark it\nright.",
        body="Save this. Send it to a first-time voter.",
        photo="ai-01-polling-queue.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
