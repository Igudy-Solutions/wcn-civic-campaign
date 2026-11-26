#!/usr/bin/env python3
"""Day 7: Sat 9 Jan 2027. Video (Reel). Know the Process.

Know your route to your polling unit.
Spine: do you know where -> it's on your PVC, check with INEC -> visit before -> movement restricted -> go early.
Facts: PU on PVC and INEC voter verification; vehicle movement is normally restricted on election day (VERIFY for 2027).
No day count on screen or in the voice. INEC is voiced "Eye-neck".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 7
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = ["Do you know exactly where you're voting?", "Your polling unit is printed on your voter's card. You can also check it with Eye-neck.", 'Go and see it before election day. Find the gate, the building, the way in.', 'Movement is usually restricted on election day, so plan to walk or go nearby.', 'Go early. Take your card. Take water.', 'Know your route.']


def spec():
    return [
        V.scene(0, "ai-06-walk-to-vote.png", "Do you know exactly where you're voting?", lambda a, b: f'''
          {t("Where exactly", "w", 92, 80, 760, -3, a + 0.3, b)}
          {t("are you voting?", "l", 77, 110, 910, 2, a + V.LEAD + 1.0, b)}'''),
        V.scene(1, "ai-08-pvc-collection.png", "Your polling unit is printed on your voter's card. You can also check it with Eye-neck.", lambda a, b: f'''
          {t("It's on", "w", 110, 80, 640, -2, a + V.LEAD + 1.0, b)}
          {t("your PVC.", "l", 120, 110, 790, 2, a + V.LEAD + 1.4, b)}
          {t("Or check with INEC.", "w", 63, 80, 990, -2, a + V.LEAD + 3.2, b)}'''),
        V.scene(2, "ai-01-polling-queue.png", 'Go and see it before election day. Find the gate, the building, the way in.', lambda a, b: f'''
          {t("Visit it", "w", 120, 80, 700, -2, a + 0.3, b)}
          {t("before the day.", "l", 77, 110, 860, 2, a + 0.9, b)}
          {V.mark("arrow", 800, 1060, 160, a + V.LEAD + 2.0)}'''),
        V.scene(3, "ai-24-peace-walk.png", 'Movement is usually restricted on election day, so plan to walk or go nearby.', lambda a, b: f'''
          <div class="a stamp" data-fx="stamp" data-r="-5" data-in="{a + V.LEAD + 2.4}" data-out="{b}" style="left:90px;top:560px;font-size:91px">PLAN TO WALK</div>
          {t("Roads may close.", "w", 74, 90, 800, 2, a + V.LEAD + 1.2, b)}'''),
        V.scene(4, "ai-16-pvc-proud.png", 'Go early. Take your card. Take water.', lambda a, b: f'''
          {t("Go early.", "w", 120, 80, 700, -2, a + V.LEAD + .1, b)}
          {t("Card. Water.", "l", 97, 110, 860, 2, a + V.LEAD + 1.0, b)}'''),
        V.end_card(5, "ai-23-inked-group.png", 'Know your route.', line='Know your route.'),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
