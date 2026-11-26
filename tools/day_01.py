#!/usr/bin/env python3
"""Day 1: Fri 15 Jan 2027. Video (Reel). Know Your Power.

Nigeria decides. Go early. Stay peaceful.
Spine: Saturday 16 Jan -> three ballots -> PVC, early, stay -> secret ballot -> peace, wait for INEC.
Facts: INEC timetable; three federal ballots on 16 Jan.
No day count on screen or in the voice. INEC is voiced "Eye-neck".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 1
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = ['Saturday, the sixteenth of January. Nigeria decides.', 'Three ballots. President, Senate, House of Representatives.', "Take your voter's card. Go early. Stay in the queue.", 'Your ballot is secret. Nobody can buy it and nobody can see it.', 'Whatever happens, stay peaceful. Wait for Eye-neck.', 'Go early. Stay peaceful.']


def spec():
    return [
        V.scene(0, "ai-01-polling-queue.png", 'Saturday, the sixteenth of January. Nigeria decides.', lambda a, b: f'''
          <div class="a cal" data-fx="slideup" data-r="-3" data-in="{a + .3}" data-out="{b}" style="left:120px;top:380px"><div class="m">JANUARY 2027</div><div class="n">16</div><div class="d">SATURDAY</div><div class="o">Nigeria decides</div></div>'''),
        V.scene(1, "ai-07-ballot-box.png", 'Three ballots. President, Senate, House of Representatives.', lambda a, b: f'''
          {t("President.", "w", 110, 80, 600, -2, a + V.LEAD + 1.4, b)}
          {t("Senate.", "w", 110, 110, 750, 2, a + V.LEAD + 2.6, b)}
          {t("House of Reps.", "l", 86, 80, 900, -2, a + V.LEAD + 3.2, b)}'''),
        V.scene(2, "ai-16-pvc-proud-card.png", "Take your voter's card. Go early. Stay in the queue.", lambda a, b: f'''
          {t("Your PVC.", "w", 110, 80, 700, -2, a + 0.3, b)}
          {t("Go early.", "l", 110, 110, 850, 2, a + V.LEAD + 1.4, b)}
          {t("Stay.", "w", 110, 80, 1000, -2, a + V.LEAD + 2.3, b)}'''),
        V.scene(3, "ai-05-bvas-accreditation.png", 'Your ballot is secret. Nobody can buy it and nobody can see it.', lambda a, b: f'''
          <div class="a stamp" data-fx="stamp" data-r="-6" data-in="{a + 0.5}" data-out="{b}" style="left:90px;top:520px;font-size:84px">SECRET BALLOT</div>
          {t("Not for sale.", "w", 90, 100, 760, 2, a + V.LEAD + 1.6, b)}'''),
        V.scene(4, "ai-24-peace-walk.png", 'Whatever happens, stay peaceful. Wait for Eye-neck.', lambda a, b: f'''
          {t("Stay peaceful.", "w", 86, 80, 700, -2, a + V.LEAD + .3, b)}
          {t("Wait for INEC.", "l", 83, 110, 860, 2, a + V.LEAD + 1.6, b)}'''),
        V.end_card(5, "ai-23-inked-group.png", 'Go early. Stay peaceful.', line='Go early. Stay peaceful.'),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
