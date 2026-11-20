#!/usr/bin/env python3
"""Day 55: Sun 22 Nov 2026. Carousel. Know Your Power.

Five names on your ballot, most people can only name one.
Spine: hook -> you vote for five offices on two days -> each office, one per
slide, what the job does -> close: know all five before you go.
Facts (Constitution of Nigeria, 1999 as amended; INEC timetable):
  * 16 Jan 2027: President, Senate, House of Reps (three ballots)
  * 6 Feb 2027: Governor, State House of Assembly (two ballots)
  * 109 senators (3 per state + 1 FCT); 360 House of Reps members
  * Senate confirms ministers and other key appointments
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 55
OUT = folder_for(DAY)

SLIDES = [
    ("cover", dict(
        title="Five names on\nyour ballot.\n*Most people can\nonly name one.*",
        size=112,
        photo="ai-07-ballot-box.png",
    )),
    ("statement", dict(
        lead="You don't vote once. You vote **five times**,\nfor five different jobs, on two Saturdays.",
        punch="Five offices.\nFive choices.",
        body="Each one does a different job. Swipe through them.",
        photo="ai-05-bvas-accreditation.png",
        source="INEC timetable",
    )),
    ("statement", dict(
        kicker="16 January · Ballot 1 of 5",
        punch="President",
        size=150,
        body="Runs the federal government, proposes the national budget and commands the armed forces. A four-year term.",
        photo="ai-06-walk-to-vote.png",
        source="Constitution",
    )),
    ("statement", dict(
        kicker="16 January · Ballot 2 of 5",
        punch="Senator",
        size=150,
        body="One of 109. Makes federal laws, passes the budget and confirms ministers. Three per state, one for the FCT.",
        photo="ai-14-town-hall.png",
        source="Constitution",
    )),
    ("statement", dict(
        kicker="16 January · Ballot 3 of 5",
        punch="House of\nReps member",
        size=124,
        body="One of 360. Makes federal laws and passes the budget with the Senate, for your federal constituency.",
        photo="ai-04-friends-debate.png",
        source="Constitution",
    )),
    ("statement", dict(
        kicker="6 February · Ballot 4 of 5",
        punch="Governor",
        size=150,
        body="Runs your state: state roads, state hospitals, state schools and the state budget.",
        photo="ai-10-classroom.png",
        source="Constitution",
    )),
    ("statement", dict(
        kicker="6 February · Ballot 5 of 5",
        punch="State Assembly\nmember",
        size=120,
        body="Makes your state's laws, approves the state budget and checks the governor.",
        photo="ai-09-hospital.png",
        source="Constitution",
    )),
    ("cta", dict(
        lead="Five jobs. Five decisions.\nMost people only think about one.",
        punch="Know all five\nbefore you go.",
        body="Find out who is running for each seat where you vote, then choose for yourself.",
        photo="ai-02-inked-thumb.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
