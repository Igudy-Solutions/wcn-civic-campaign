#!/usr/bin/env python3
"""Day 49: Sat 28 Nov 2026. Carousel. Know the Candidates. Series 1 of 6.

Tickets 2 to 4 on INEC's ballot (AA, AAC, ADC). Ticket 1 (A) is blank by
court order. Same layout for everyone, INEC facts only (age, running mate,
qualifications as printed), party colours from tools/parties.py.

Photos: none yet. Real photos only, never AI. Save a cut-out PNG as
images/candidates/<party>-president.png (e.g. aa-president.png) and re-run;
until then a party monogram stands in.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402
from preview_candidate import candidate_slide  # noqa: E402

DAY = 49
OUT = folder_for(DAY)
TICKETS = ["AA", "AAC", "ADC"]

SLIDES = [
    ("cover", dict(
        title="Meet the\ncandidates.\n*Part 1 of 6.*",
        size=132,
        photo="ai-14-town-hall.png",
    )),
    ("statement", dict(
        lead="Over six posts, all 18 presidential\ncandidates, in INEC's ballot order.",
        punch="Same layout.\nSame facts.\nNo favourites.",
        size=104,
        body="Age, running mate and qualifications as INEC lists them. We don't rank, endorse or comment.",
        photo="ai-07-ballot-box.png",
        source="INEC final list",
    )),
] + [candidate_slide(t) for t in TICKETS] + [
    ("cta", dict(
        lead="Ticket 1 on the ballot has no candidate\nlisted, by court order. Next: tickets 5 to 7.",
        punch="Know every\nname.",
        body="Information, not endorsement. Your vote, your choice.",
        photo="ai-05-bvas-accreditation.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
