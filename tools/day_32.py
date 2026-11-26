#!/usr/bin/env python3
"""Day 32: Tue 15 Dec 2026. Video (Reel). Know Your Power.

I voted in 2023 and nothing changed.
Spine: we hear you -> 68 million stayed home -> elections go to who shows up -> vote, then follow up.
Facts: INEC 2023: 93.4m registered, about 25m votes cast (26.7% turnout).
No day count on screen or in the voice. INEC is voiced "Eye-neck".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 32
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = ['I voted in twenty twenty-three and nothing changed. We hear you.', 'In twenty twenty-three, about ninety-three million people registered. About sixty-eight million of them did not vote.', 'Elections are decided by the people who show up.', 'And one vote is only the start. Know who you elected. Ask what they did.', 'Change takes more than one Saturday. It starts with this one.', 'Vote. Then follow up.']


def spec():
    return [
        V.scene(0, "ai-11-market-trader.png", 'I voted in twenty twenty-three and nothing changed. We hear you.', lambda a, b: f'''
          {t("&quot;Nothing changed.&quot;", "w", 67, 80, 760, -3, a + 0.3, b)}
          {t("We hear you.", "l", 96, 110, 920, 2, a + V.LEAD + 2.2, b)}'''),
        V.scene(1, "ai-01-polling-queue.png", 'In twenty twenty-three, about ninety-three million people registered. About sixty-eight million of them did not vote.', lambda a, b: f'''
          {t("93 million", "w", 120, 80, 520, -2, a + V.LEAD + 1.4, b)}
          {t("registered.", "w", 80, 100, 680, 2, a + V.LEAD + 1.9, b)}
          {t("68 million", "l", 120, 80, 840, -2, a + V.LEAD + 3.6, b)}
          {t("didn't vote.", "l", 80, 100, 1000, 2, a + V.LEAD + 4.2, b)}'''),
        V.scene(2, "ai-23-inked-group.png", 'Elections are decided by the people who show up.', lambda a, b: f'''
          {t("Elections go to", "w", 80, 80, 760, -2, a + 0.3, b)}
          {t("who shows up.", "l", 89, 110, 900, 2, a + V.LEAD + 1.4, b)}
          {V.mark("thumb", 820, 1080, 140, a + V.LEAD + 1.8)}'''),
        V.scene(3, "ai-14-town-hall.png", 'And one vote is only the start. Know who you elected. Ask what they did.', lambda a, b: f'''
          {t("Know who", "w", 100, 80, 640, -2, a + V.LEAD + 1.6, b)}
          {t("you elected.", "w", 97, 110, 790, 2, a + V.LEAD + 2.2, b)}
          {t("Ask what they did.", "l", 67, 80, 950, -2, a + V.LEAD + 3.3, b)}'''),
        V.scene(4, "ai-06-walk-to-vote.png", 'Change takes more than one Saturday. It starts with this one.', lambda a, b: f'''
          {t("It starts", "w", 110, 80, 760, -2, a + V.LEAD + 2.0, b)}
          {t("with this one.", "l", 83, 110, 910, 2, a + V.LEAD + 2.6, b)}'''),
        V.end_card(5, "ai-02-inked-thumb.png", 'Vote. Then follow up.', line='Vote. Then follow up.'),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
