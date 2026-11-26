#!/usr/bin/env python3
"""Special: Collect your PVC. Urgent insert, 26 Nov 2026 (Arkcore: PVCs are
out, start the collection push). Carousel, Know the Process.

Spine: your card is ready -> registered is not enough -> where to go -> what
to take -> how it works (in person, free, check it) -> collect this week and
bring a friend. No day count, so it can go out on any day.
Facts: INEC; collection points and deadline to VERIFY with INEC's notices.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402

OUT = os.path.join("Specials", "Collect Your PVC")

SLIDES = [
    ("cover", dict(
        badge=False,
        kicker="PVCs are ready for collection",
        title="Your PVC is ready.\n*Is it still sitting\nat INEC?*",
        size=118,
        photo="ai-08-pvc-collection.png",
    )),
    ("statement", dict(
        lead="Registering was step one.\nWithout the card in your hand,\nyour name on the register can't vote.",
        punch="No PVC.\nNo vote.",
        size=150,
        body="Not a photo of it. Not the slip. The card.",
        photo="ai-16-pvc-proud-card.png",
        pos="50% 20%",
    )),
    ("list", dict(
        kicker="How to collect it",
        title="Four things\n*to know*",
        items=[
            ("Go to your INEC office", "In your local government area, or the collection point INEC announces for your ward"),
            ("Take your details", "Your registration slip if you have it, or your name, date of birth and phone number"),
            ("Go in person", "Nobody can collect it for you. Not family, not an agent"),
            ("It's free", "No one should charge you for your own card"),
        ],
        photo="ai-22-official-explains.png",
    )),
    ("statement", dict(
        lead="Before you leave the office:",
        punch="Check your\nname and photo.",
        size=112,
        body="Your polling unit is printed on the card too. That's where you'll vote on 16 January and 6 February.",
        photo="ai-05-bvas-accreditation.png",
    )),
    ("cta", dict(
        lead="Collection doesn't stay open forever.\nThe queues get longer as January gets closer.",
        punch="Collect it\nthis week.\nBring a friend.",
        size=112,
        body="Tag the person whose PVC is still at INEC. You know who they are.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT)
