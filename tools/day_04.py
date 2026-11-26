#!/usr/bin/env python3
"""Day 4: Tue 12 Jan 2027. Carousel. Know Your Power.

The myths that keep people home, answered. Recap of the objections covered
during the campaign. Facts: 2023 margin (INEC); next presidential election 2031.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 4
OUT = folder_for(DAY)

MYTHS = [
    ("\u201cMy vote doesn't count.\u201d", "2023 was decided by about 1.8 million votes. About 68 million registered voters stayed home.", "ai-03-public-count.png"),
    ("\u201cThey're all the same.\u201d", "Compare the plan, the record, the team and the money. They're not the same.", "ai-14-town-hall.png"),
    ("\u201cThe courts will decide.\u201d", "Courts settle disputes about the vote. They start from your vote.", "ai-26-results-wall.png"),
    ("\u201cNothing ever changes.\u201d", "Nothing changes faster when the people who want change stay home.", "ai-10-classroom.png"),
    ("\u201cI'll vote next time.\u201d", "The next presidential election is in 2031. That's four more years.", "ai-06-walk-to-vote.png"),
]

SLIDES = [
    ("cover", dict(
        title="The myths that\nkeep people\nhome. *Answered.*",
        size=122,
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
] + [
    ("statement", dict(kicker=f"Myth {i} of 5", punch=m, size=104, body=a, photo=p))
    for i, (m, a, p) in enumerate(MYTHS, 1)
] + [
    ("cta", dict(
        lead="Send this to the one friend who has\na reason not to vote.",
        punch="No more\nexcuses.",
        body="Saturday 16 January. Saturday 6 February.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
