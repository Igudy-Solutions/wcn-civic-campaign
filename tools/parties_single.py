#!/usr/bin/env python3
"""Single image: every party on the 2027 presidential ballot.

Built from INEC's final list of presidential candidates (data/), in INEC's
ballot order. Every party gets the same tile; only the colour chip changes.
Party colours come from tools/parties.py and are still to be confirmed.

Output: Specials/Parties On The Ballot/01-post.png
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_carousel as G  # noqa: E402
from parties import PARTIES  # noqa: E402

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
    ("ballot", dict(
        title="19 parties. One ballot.\n*Know every name on it.*",
        size=84,
        dim=0.45,
        tickets=tickets,
        body="Presidential ballot, Saturday 16 January 2027. In INEC's ballot order. Information, not endorsement.",
        photo="ai-07-ballot-box.png",
        pos="50% 10%",
    )),
]

if __name__ == "__main__":
    G.render_post(SLIDES, "Specials/Parties On The Ballot", day=None)
