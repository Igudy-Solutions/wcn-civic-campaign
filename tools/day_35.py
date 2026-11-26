#!/usr/bin/env python3
"""Day 35: Sat 12 Dec 2026. Carousel. Know Your Power.

What does your senator actually do?
Spine: hook -> 109 senators (3 per state, 1 for the FCT) -> what they do ->
you elect yours on 16 Jan with the president -> do you know their name?
Facts: 1999 Constitution (as amended), s.48 and Part II.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 35
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="What does\nyour senator\n*actually do?*",
        size=132,
        photo="ai-14-town-hall.png",
    )),
    ("stat", dict(
        kicker="The Senate",
        lead="Three for every state, one for the FCT:",
        number="109",
        label="senators. *One of them is yours.*",
        photo="ai-01-polling-queue.png",
        source="1999 Constitution",
    )),
    ("list", dict(
        kicker="The job",
        title="What your\n*senator does*",
        size=96,
        items=[("Makes federal laws", "Every Act of the National Assembly passes the Senate"),
               ("Approves the national budget", "No federal spending without it"),
               ("Confirms top appointments", "Ministers, ambassadors, service chiefs"),
               ("Checks the government", "Committees question ministries and agencies"),
               ("Speaks for your district", "Brings your area's needs to Abuja")],
        photo="ai-10-classroom.png",
    )),
    ("statement", dict(
        lead="You choose your senator on\nSaturday 16 January, the same day as the president.",
        punch="Can you name\nyours today?",
        size=124,
        photo="ai-15-bus-stop-phone.png",
    )),
    ("cta", dict(
        lead="Find out who represents your senatorial\ndistrict, and who wants to.",
        punch="Know them.\nThen vote.",
        body="Save this. Share it with someone who skips the Senate box.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
