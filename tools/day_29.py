#!/usr/bin/env python3
"""Day 29: Fri 18 Dec 2026. Carousel. Know the Candidates.

Second in line. Meet the running mates: all 18 vice presidential candidates
from INEC's final list, in ballot order, three list slides of six.
Facts: INEC final list; VP succession, 1999 Constitution s.146.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 29
OUT = folder_for(DAY)

VPS = [('Shehu Hussaini', 'AA · Ticket 2', '2'), ('Haruna Garba Magashi', 'AAC · Ticket 3', '3'), ('Chibuike Rotimi Amaechi', 'ADC · Ticket 4', '4'), ('Chinazam Ike', 'ADP · Ticket 5', '5'), ('Kashim Shettima', 'APC · Ticket 6', '6'), ('Musa Lawal Daura', 'APM · Ticket 7', '7'), ('Peace Egobia Ofordile', 'APP · Ticket 8', '8'), ('Usman Turaki Mustapha', 'BP · Ticket 9', '9'), ('Nafisat Usaku Abubakar', 'DLA · Ticket 10', '10'), ('Hajja Bintu Konto', 'LP · Ticket 11', '11'), ('Rabiu Musa Kwankwaso', 'NDC · Ticket 12', '12'), ('Uchenna Anthony Chukwuemeka', 'NDP · Ticket 13', '13'), ('Nasir Muhammed Sulaiman', 'NRM · Ticket 14', '14'), ('Babangida Umaru', 'PDP · Ticket 15', '15'), ('Sule Mohammed', 'PRP · Ticket 16', '16'), ('Usman Muhammed Bugaje', 'SDP · Ticket 17', '17'), ('Patience Ndidi Key', 'YPP · Ticket 18', '18'), ('Khalid Hassan', 'ZLP · Ticket 19', '19')]

SLIDES = [
    ("cover", dict(
        title="Second\nin line.\n*Meet the\nrunning mates.*",
        size=124,
        photo="ai-22-official-explains.png",
    )),
    ("statement", dict(
        lead="If anything happens to a president,\nthe vice president takes over.",
        punch="You're voting\nfor two people.",
        size=124,
        body="All 18 vice presidential candidates, in INEC's ballot order. Numbers are ballot tickets.",
        photo="ai-07-ballot-box.png",
        source="1999 Constitution, s.146",
    )),
] + [
    ("list", dict(kicker=f"Running mates · {i} of 3", title="Tickets\n*" + VPS[i * 6 - 6][2] + " to " + VPS[i * 6 - 1][2] + "*",
                  size=84, items=VPS[i * 6 - 6:i * 6], photo=p))
    for i, p in ((1, "ai-01-polling-queue.png"), (2, "ai-03-public-count.png"), (3, "ai-06-walk-to-vote.png"))
] + [
    ("cta", dict(
        lead="Ticket 1 has no candidates listed,\nby court order.",
        punch="Check the\nwhole ticket.",
        body="Information, not endorsement. Your vote, your choice.",
        photo="ai-23-inked-group.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
