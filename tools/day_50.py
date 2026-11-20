#!/usr/bin/env python3
"""Day 50: Fri 27 Nov 2026. Carousel. Know Your Power.

They decide your hospital, your school and your job.
Spine: hook -> the hospital queue -> the classroom -> prices at the market
-> jobs -> who decides what (federal, state, local) -> close: you're hiring.
Facts: federal and state budgets are passed by the National Assembly and
State Houses of Assembly; public schools and hospitals are funded through
them; local government elections are separate, run by State Independent
Electoral Commissions (Constitution).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 50
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="They decide your\nhospital, your school\nand your job.\n*Do you know\nwho they are?*",
        size=96,
        photo="ai-09-hospital.png",
        pos="50% 10%",
    )),
    ("statement", dict(
        lead="That long queue at the general hospital?",
        punch="A budget\ndecided it.",
        body="How many nurses, beds and drugs there are is set in budgets passed by the people you elect.",
        photo="ai-09-hospital.png",
        pos="50% 25%",
    )),
    ("statement", dict(
        lead="That crowded classroom?",
        punch="Someone you\nelected funds it.",
        body="Teachers, desks and new classrooms come from state and federal budgets.",
        photo="ai-10-classroom.png",
    )),
    ("statement", dict(
        lead="The prices you buy and sell at?",
        punch="Policy moves\nprices.",
        body="Fuel, power, roads, ports and tax rules all reach the market stall. Elected people set them.",
        photo="ai-11-market-trader.png",
        pos="50% 15%",
    )),
    ("statement", dict(
        lead="The job you have, or the one you're waiting for?",
        punch="Jobs follow\nchoices.",
        body="Power supply, security and investment decide whether jobs come. Those are political decisions.",
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
    ("list", dict(
        title="So who decides *what?*",
        size=88,
        dim=0.35,
        items=[
            ("President and National Assembly", "Federal budget, federal roads, national security, federal hospitals and universities"),
            ("Governor and State Assembly", "State budget, state hospitals, state schools, state roads"),
            ("Local government chairman", "Primary health centres, local markets. Elected separately, by your state's electoral commission"),
        ],
        photo="ai-14-town-hall.png",
        source="Constitution",
    )),
    ("cta", dict(
        lead="Election day lasts one day.\nWhat they decide lasts four years.",
        punch="You're not\nvoting. You're\nhiring.",
        size=124,
        body="16 January and 6 February. Know who you're hiring.",
        photo="ai-06-walk-to-vote.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
