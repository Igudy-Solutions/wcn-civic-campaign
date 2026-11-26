#!/usr/bin/env python3
"""Day 20: Sun 27 Dec 2026. Carousel. Know the Process.

"The courts will decide anyway?" Not quite.
Spine: hook -> courts don't vote, voters do -> tribunals work from the votes
and the records of the count -> a big, watched vote is harder to dispute ->
CTA. General description of the petition process; no case named.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 20
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="\u201cThe courts will\ndecide anyway.\u201d\n*Not quite.*",
        size=120,
        photo="ai-14-town-hall.png",
    )),
    ("statement", dict(
        lead="Judges don't vote.",
        punch="Courts don't\npick winners.\n*Voters do.*",
        size=120,
        photo="ai-02-inked-thumb.png",
    )),
    ("statement", dict(
        lead="If a result is challenged, an election\ntribunal looks at how it was run.",
        punch="It starts\nfrom your\nvote.",
        size=128,
        body="Tribunals examine the votes cast and the records of the count, like result sheets from polling units.",
        photo="ai-26-results-wall.png",
    )),
    ("statement", dict(
        lead="Every voter who shows up, and every\nperson who watches the count, adds proof.",
        punch="A big, watched\nvote is hard\nto argue with.",
        size=112,
        photo="ai-03-public-count.png",
    )),
    ("cta", dict(
        lead="Courts settle disputes about the vote.\nThey can't replace it.",
        punch="Vote.\nThen watch\nthe count.",
        body="Send this to the friend who says it's all decided in court.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
