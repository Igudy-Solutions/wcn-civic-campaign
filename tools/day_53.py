#!/usr/bin/env python3
"""Day 53: Tue 24 Nov 2026. Carousel. Know the Candidates.

18 people want to be your president. Can you name five?
Spine: hook -> most of us know two -> the whole list, INEC ballot order, in
two slides -> a name is only the start; the series that follows -> test
yourself.
Facts: INEC final list of presidential candidates (data/), 19 tickets, ticket
1 (A) blank by court order, so 18 candidates. Same tile for everyone, INEC
order, no ranking. Party colours from tools/parties.py (to be confirmed).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_carousel as G  # noqa: E402
from parties import PARTIES  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 53
OUT = folder_for(DAY)

data = json.load(open(os.path.join(G.ROOT, "data", "presidential_candidates.json")))
tickets = []
for t in data["tickets"]:
    abbr = t["party"]
    cols, ink = (PARTIES[abbr][1], PARTIES[abbr][2]) if abbr in PARTIES else (["#3A3F3B"], "#fff")
    if t["president"]:
        tickets.append(dict(party=abbr, colour=cols[0], ink=ink, name=t["president"]["display"],
                            sub=f"Running mate: {t['vp']['display']}"))
    else:
        tickets.append(dict(party=abbr, colour=cols[0], ink=ink, blank="No candidate listed (court order)"))

SLIDES = [
    ("cover", dict(
        title="18 people want\nto be your\npresident.\n*Can you name five?*",
        size=118,
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
    ("statement", dict(
        lead="Most of us can name two. Maybe three.",
        punch="There are 18\non your ballot.",
        body="Here is every one, in INEC's ballot order. No ranking, no favourites.",
        photo="ai-07-ballot-box.png",
        source="INEC final list",
    )),
    ("ballot", dict(
        title="Ballot order, *1 to 10*",
        size=76,
        dim=0.5,
        tickets=tickets[:10],
        photo="ai-07-ballot-box.png",
        pos="50% 10%",
        source="INEC final list",
    )),
    ("ballot", dict(
        title="Ballot order, *11 to 19*",
        size=76,
        dim=0.5,
        tickets=tickets[10:],
        body="Names and running mates as INEC lists them. Information, not endorsement.",
        photo="ai-05-bvas-accreditation.png",
        pos="50% 10%",
        source="INEC final list",
    )),
    ("statement", dict(
        lead="A name is only the start.",
        punch="Look past\nthe poster.",
        body="Next, we show every candidate on the same layout: age, running mate and qualifications, as INEC lists them.",
        photo="ai-14-town-hall.png",
    )),
    ("cta", dict(
        lead="Cover the list. How many can you name now?",
        punch="Name five.\nThen learn\nthe rest.",
        size=124,
        body="Send this to the friend who only knows two names. Your vote, your choice.",
        photo="ai-16-pvc-proud.png",
        pos="50% 15%",
    )),
]

if __name__ == "__main__":
    G.render_post(SLIDES, OUT, day=DAY)
