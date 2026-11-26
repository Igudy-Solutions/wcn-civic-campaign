#!/usr/bin/env python3
"""Day 16: Thu 31 Dec 2026. Video (Reel). Know the Process.

Fake results travel faster than real ones. Wait for INEC.
Spine: results flood phones -> some fake -> real results start at the unit -> IReV and INEC declare -> don't share what you can't trace.
Facts: public count, EC8A posted at the unit, IReV upload, INEC returning officers declare (VERIFY wording).
No day count on screen or in the voice. INEC is voiced "Eye-neck".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 16
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = ['On election night, results will fly around your phone.', 'Some will be real. Many will not.', "Real results start at your polling unit. They're counted in public and pinned on the wall.", 'Eye-neck uploads polling unit results to its results viewing portal, and only Eye-neck declares the winner.', "Don't share a result you can't trace.", 'Wait for Eye-neck.']


def spec():
    return [
        V.scene(0, "ai-15-bus-stop-phone.png", 'On election night, results will fly around your phone.', lambda a, b: f'''
          {t("Results", "w", 120, 80, 760, -3, a + 0.3, b)}
          {t("on your phone.", "l", 83, 110, 920, 2, a + V.LEAD + 1.6, b)}''', pos="50% 15%"),
        V.scene(1, "ai-04-friends-debate.png", 'Some will be real. Many will not.', lambda a, b: f'''
          {t("Some real.", "w", 110, 80, 700, -2, a + V.LEAD + .2, b)}
          {t("Many not.", "l", 120, 110, 860, 2, a + V.LEAD + 1.2, b)}'''),
        V.scene(2, "ai-03-public-count.png", "Real results start at your polling unit. They're counted in public and pinned on the wall.", lambda a, b: f'''
          {t("Counted", "w", 110, 80, 680, -2, a + V.LEAD + 2.2, b)}
          {t("in public.", "l", 110, 110, 830, 2, a + V.LEAD + 2.6, b)}
          {V.mark("tick", 820, 1060, 140, a + V.LEAD + 3.0)}'''),
        V.scene(3, "ai-26-results-wall.png", 'Eye-neck uploads polling unit results to its results viewing portal, and only Eye-neck declares the winner.', lambda a, b: f'''
          {t("Only INEC", "w", 120, 80, 700, -2, a + V.LEAD + 3.6, b)}
          {t("declares.", "l", 120, 110, 860, 2, a + V.LEAD + 4.2, b)}'''),
        V.scene(4, "ai-13-family-table.png", "Don't share a result you can't trace.", lambda a, b: f'''
          <div class="a stamp" data-fx="stamp" data-r="-5" data-in="{a + 0.4}" data-out="{b}" style="left:80px;top:520px;font-size:74px">CAN'T TRACE IT?</div>
          {t("Don't share it.", "w", 78, 100, 760, 2, a + V.LEAD + 1.0, b)}''', pos="50% 20%"),
        V.end_card(5, "ai-22-official-explains.png", 'Wait for Eye-neck.', line='Wait for INEC.'),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
