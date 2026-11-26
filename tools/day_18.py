#!/usr/bin/env python3
"""Day 18: Tue 29 Dec 2026. Carousel. Know the Process.

What happens at your polling unit, step by step.
Spine: hook -> six steps, one per slide (queue, accreditation, ballot, mark
in secret, fold and drop, the public count) -> CTA.
VERIFY each step against INEC's 2027 Regulations and Guidelines and the
election manual before posting.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 18
OUT = folder_for(DAY)

STEPS = [
    ("Join the queue.", "Bring your PVC. Arrive early. Voting is in the open, at your own unit.", "ai-01-polling-queue.png"),
    ("Get accredited.", "An official checks your PVC on the BVAS device, which confirms you by fingerprint or face.", "ai-05-bvas-accreditation.png"),
    ("Collect your ballot.", "Make sure each ballot paper is stamped and signed by the official.", "ai-22-official-explains.png"),
    ("Mark it in secret.", "In the cubicle, ink your thumb and press it once, inside one box. No phones in the cubicle.", "ai-07-ballot-box.png"),
    ("Fold and drop it.", "Fold the way the official shows you and drop it in the right box, in full view.", "ai-02-inked-thumb.png"),
    ("Watch the count.", "Votes are counted in public. Results are written on the EC8A sheet, posted and uploaded to IReV.", "ai-03-public-count.png"),
]

SLIDES = [
    ("cover", dict(
        title="What happens\nat your polling\nunit. *Step\nby step.*",
        size=118,
        photo="ai-22-official-explains.png",
    )),
] + [
    ("statement", dict(kicker=f"Step {i} of 6", punch=h, size=124, body=b, photo=p))
    for i, (h, b, p) in enumerate(STEPS, 1)
] + [
    ("cta", dict(
        lead="Six steps. Most people are done\nin well under an hour.",
        punch="Save it.\nShow up.",
        body="Send this to a first-time voter.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
