#!/usr/bin/env python3
"""Day 30: Thu 17 Dec 2026. Carousel. Know the Candidates.

Meet the candidates, part 6 of 6: tickets 17 to 19 (SDP, YPP, ZLP).
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

DAY = 30
OUT = folder_for(DAY)

TICKETS = ['SDP', 'YPP', 'ZLP']

SLIDES = [
    ("cover", dict(
        title="Meet the\ncandidates.\n*Part 6 of 6.*",
        size=132,
        photo="ai-03-public-count.png",
    )),
    ("statement", dict(
        lead="All 18 presidential candidates,\nin INEC's ballot order. Tickets 17 to 19.",
        punch="Same layout.\nSame facts.\nNo favourites.",
        size=104,
        body="Age, running mate and qualifications as INEC lists them. We don't rank, endorse or comment.",
        photo="ai-07-ballot-box.png",
        source="INEC final list",
    )),
] + [candidate_slide(t) for t in TICKETS] + [
    ("cta", dict(
        lead="That's all 18 presidential candidates.\nTicket 1 has no candidate listed, by court order.",
        punch="Now you know\nevery name.",
        body="Information, not endorsement. Your vote, your choice.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
