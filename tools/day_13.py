#!/usr/bin/env python3
"""Day 13: Sun 3 Jan 2027. Carousel. Know Your Power.

Your rights as a voter on election day.
Spine: hook -> six rights over two list slides -> if something goes wrong ->
CTA. VERIFY with INEC's 2027 Regulations and Guidelines and the Electoral
Act before posting.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 13
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Your rights\nas a voter on\n*election day.*",
        size=126,
        photo="ai-27-wheelchair-voter.png",
    )),
    ("list", dict(
        kicker="Rights 1 to 3",
        title="Know\n*your rights*",
        size=96,
        items=[("A secret ballot", "Nobody can watch you vote or make you show it"),
               ("To vote if you're in the queue", "If you're in line when voting closes, you still vote"),
               ("Help if you need it", "Elderly voters, people with disabilities and pregnant women get priority and can bring someone to assist")],
        photo="ai-27-wheelchair-voter.png",
    )),
    ("list", dict(
        kicker="Rights 4 to 6",
        title="Know\n*your rights*",
        size=96,
        start=4,
        items=[("To vote free from pressure", "No one can force, threaten or pay you"),
               ("To watch the count", "Counting is public. You can stay and observe, peacefully"),
               ("To see the result", "The EC8A result sheet is posted at your unit")],
        photo="ai-03-public-count.png",
    )),
    ("statement", dict(
        lead="If something goes wrong at your unit:",
        punch="Speak to the\npresiding\nofficer.",
        size=118,
        body="Stay calm, explain clearly, and if it isn't resolved, report it to INEC or the police.",
        photo="ai-22-official-explains.png",
    )),
    ("cta", dict(
        lead="Know your rights. Use them calmly.",
        punch="Save it for\nthe day.",
        body="Send this to someone voting for the first time.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
