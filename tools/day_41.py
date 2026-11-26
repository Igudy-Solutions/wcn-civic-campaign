#!/usr/bin/env python3
"""Day 41: Sun 6 Dec 2026. Carousel. Know the Candidates.

Meet the candidates, part 3 of 6: tickets 8 to 10 (APP, BP, DLA).
Same layout for everyone, INEC facts only (age, running mate, qualifications
as printed), party colours from tools/parties.py, INEC ballot order.

Photos: real photos only, never AI. Save a cut-out PNG as
images/candidates/<party>-president.png and re-run; until then a party
monogram stands in.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402
from preview_candidate import candidate_slide  # noqa: E402

DAY = 41
OUT = folder_for(DAY)

TICKETS = ['APP', 'BP', 'DLA']

SLIDES = [
    ("cover", dict(
        title="Meet the\ncandidates.\n*Part 3 of 6.*",
        size=132,
        photo="ai-01-polling-queue.png",
    )),
    ("statement", dict(
        lead="All 18 presidential candidates,\nin INEC's ballot order. Tickets 8 to 10.",
        punch="Same layout.\nSame facts.\nNo favourites.",
        size=104,
        body="Age, running mate and qualifications as INEC lists them. We don't rank, endorse or comment.",
        photo="ai-07-ballot-box.png",
        source="INEC final list",
    )),
] + [candidate_slide(t) for t in TICKETS] + [
    ("cta", dict(
        lead="Next in the series: tickets 11 to 13.",
        punch="Know every\nname.",
        body="Information, not endorsement. Your vote, your choice.",
        photo="ai-22-official-explains.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
