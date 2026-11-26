#!/usr/bin/env python3
"""Day 21: Sat 26 Dec 2026. Carousel. Vote Wisely.

Vote buying: what it costs you and what the law says.
Spine: hook -> the maths (N5,000 over 1,461 days) -> the law: buying and
selling votes are offences -> what it looks like -> what to do -> CTA.
VERIFY: confirm the vote-buying provisions in the Electoral Act in force for
2027 before posting. No penalty figures on the slides.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 21
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Vote buying.\n*What it costs you.\nWhat the law says.*",
        size=118,
        photo="ai-11-market-trader.png",
    )),
    ("stat", dict(
        kicker="Do the maths",
        lead="N5,000 for your vote, spread over\na four-year term of 1,461 days:",
        number="N3",
        size=320,
        label="a day. *For four years.*",
        photo="ai-15-bus-stop-phone.png",
    )),
    ("statement", dict(
        lead="It isn't just wrong. It's illegal.",
        punch="Buying a vote\nis a crime.\n*So is selling one.*",
        size=112,
        body="Under the Electoral Act, the person who offers and the person who takes both commit an offence.",
        photo="ai-22-official-explains.png",
        source="Electoral Act",
    )),
    ("list", dict(
        kicker="What it looks like",
        title="Know it when\n*you see it*",
        size=96,
        items=[("Cash near the polling unit", "Or a transfer \u201cafter you vote\u201d"),
               ("Food, rice, recharge cards", "Handed out in exchange for your vote"),
               ("\u201cShow me your ballot\u201d", "Anyone asking for proof of who you voted for"),
               ("\u201cSnap your ballot\u201d", "Phones aren't allowed in the voting cubicle")],
        photo="ai-07-ballot-box.png",
    )),
    ("statement", dict(
        lead="If someone offers you money:",
        punch="Say no.\nKeep it secret.\nReport it.",
        size=118,
        body="Tell the presiding officer or the police at the polling unit. Your ballot stays secret either way.",
        photo="ai-27-wheelchair-voter.png",
    )),
    ("cta", dict(
        lead="Four years of roads, hospitals and\nschools are not worth N3 a day.",
        punch="Don't sell it.\nShow up.",
        body="Send this to someone who thinks it's harmless.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
