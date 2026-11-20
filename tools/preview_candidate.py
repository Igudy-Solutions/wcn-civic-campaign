#!/usr/bin/env python3
"""Render one candidate slide from the INEC data, to check the template.

  python3 tools/preview_candidate.py APC [photo.png]

Output: templates/previews/candidate-<PARTY>.png
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_carousel as G  # noqa: E402
from parties import PARTIES  # noqa: E402


def candidate_slide(abbr, photo=None):
    data = json.load(open(os.path.join(G.ROOT, "data", "presidential_candidates.json")))
    t = next(x for x in data["tickets"] if x["party"] == abbr)
    full, cols, ink, _ = PARTIES[abbr]
    p, vp = t["president"], t["vp"]
    return ("candidate", dict(
        kicker=f"On the ballot · President · Ticket {t['sn']}",
        name=p["display"], party=f"{abbr} · {full}", colours=cols, party_ink=ink,
        photo=photo or f"{abbr.lower()}-president.png",
        facts=[("Age", str(p["age"])), ("Running mate", vp["display"]),
               ("Qualifications", p["qualifications"])],
        source="INEC final list of candidates",
    ))


if __name__ == "__main__":
    abbr = sys.argv[1] if len(sys.argv) > 1 else "APC"
    photo = sys.argv[2] if len(sys.argv) > 2 else None
    out = os.path.join(G.ROOT, "templates", "previews")
    os.makedirs(out, exist_ok=True)
    kind, cfg = candidate_slide(abbr, photo)
    G.render(G.build(kind, cfg, 0, 1, None, "portrait"), os.path.join(out, f"candidate-{abbr}.png"))
    print("rendered", abbr)
