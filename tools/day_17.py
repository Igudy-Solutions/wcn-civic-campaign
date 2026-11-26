#!/usr/bin/env python3
"""Day 17: Wed 30 Dec 2026. Carousel. Know the Process.

BVAS, IReV, EC8A. Election words in plain English.
Spine: hook -> one word per slide -> two more you'll hear (PVC, PU) -> CTA.
VERIFY definitions with INEC before posting.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 17
OUT = folder_for(DAY)

WORDS = [
    ("BVAS", "Bimodal Voter Accreditation System", "The handheld device that checks you're the real owner of your PVC, by fingerprint or face. It also photographs the result sheet.", "ai-05-bvas-accreditation.png"),
    ("EC8A", "The polling unit result sheet", "After the public count, results are written on it, signed, and a copy is posted at the unit.", "ai-26-results-wall.png"),
    ("IReV", "INEC Result Viewing portal", "The website where photos of polling unit result sheets are published, so anyone can check them.", "ai-15-bus-stop-phone.png"),
]

SLIDES = [
    ("cover", dict(
        title="BVAS. IReV.\nEC8A. *Election\nwords in plain\nEnglish.*",
        size=118,
        photo="ai-05-bvas-accreditation.png",
    )),
] + [
    ("statement", dict(kicker=k, lead=None, punch=w, size=200, body=d, photo=p))
    for w, k, d, p in WORDS
] + [
    ("list", dict(
        kicker="Two more you'll hear",
        title="And these\n*two*",
        size=96,
        items=[("PVC", "Permanent Voter's Card. No PVC, no vote", "1"),
               ("PU", "Polling unit. Yours is printed on your PVC", "2")],
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
    ("cta", dict(
        lead="Now when someone says \u201ccheck IReV\u201d,\nyou'll know what they mean.",
        punch="Know the\nwords.",
        body="Save this and share it with someone voting for the first time.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
