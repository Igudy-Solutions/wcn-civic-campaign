#!/usr/bin/env python3
"""Day 51: Thu 26 Nov 2026. Single. Peaceful Participation.

Your future is worth fighting for. Fight with your vote.
Rewritten 26 Nov (Arkcore): lead with what is at stake and why it is worth
the fight, instead of only "no candidate is worth your life". The fight is
the vote: showing up, staying, watching the count. Never violence.
Photo: ai-23-inked-group (young voters holding up inked thumbs).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 51
OUT = folder_for(DAY)

SLIDES = [
    ("statement", dict(
        lead="Your hospital. Your school. Your job.\nThe next four years are on this ballot.",
        punch="Your future\nis worth\nfighting for.",
        size=128,
        body="Fight with your PVC, not your fists. Show up, stay to watch the count, and walk away from trouble. Violence only wins when good people stay home.",
        photo="ai-23-inked-group.png",
        pos="50% 20%",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
