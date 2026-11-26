#!/usr/bin/env python3
"""Day 43: Fri 4 Dec 2026. Video (Reel). Know the Process.

Before you forward that election broadcast, check it.
Spine: a broadcast lands -> stop -> three questions -> INEC is the source -> unsure, don't share.
Facts: INEC publishes election dates and notices on its website and verified pages.
No day count on screen or in the voice. INEC is voiced "Eye-neck".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 43
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = ['A message lands in your family group. It says the election has been moved.', 'Before you forward it, stop.', 'Who sent it first? Is there a date? Is there a name you can check?', 'Election news comes from Eye-neck. Check its website and its verified pages.', "If you can't confirm it, don't share it.", 'Check before you share.']


def spec():
    return [
        V.scene(0, "ai-15-bus-stop-phone.png", 'A message lands in your family group. It says the election has been moved.', lambda a, b: f'''
          {t("Forwarded", "w", 120, 80, 760, -3, a + 0.3, b)}
          {t("many times.", "l", 90, 110, 920, 2, a + 0.9, b)}''', pos="50% 15%"),
        V.scene(1, "ai-04-friends-debate.png", 'Before you forward it, stop.', lambda a, b: f'''
          <div class="a stamp" data-fx="stamp" data-r="-6" data-in="{a + 0.5}" data-out="{b}" style="left:120px;top:520px;font-size:180px">STOP</div>
          {t("before you forward.", "w", 62, 100, 840, 2, a + V.LEAD + .6, b)}'''),
        V.scene(2, "ai-13-family-table.png", 'Who sent it first? Is there a date? Is there a name you can check?', lambda a, b: f'''
          {t("Who sent it?", "w", 96, 80, 420, -2, a + 0.3, b)}
          {t("Is it dated?", "w", 96, 110, 580, 2, a + V.LEAD + 1.3, b)}
          {t("Can you check it?", "l", 71, 80, 740, -2, a + V.LEAD + 2.4, b)}''', pos="50% 20%"),
        V.scene(3, "ai-22-official-explains.png", 'Election news comes from Eye-neck. Check its website and its verified pages.', lambda a, b: f'''
          {t("Election news", "w", 92, 80, 760, -2, a + 0.3, b)}
          {t("comes from INEC.", "l", 72, 110, 910, 2, a + V.LEAD + 1.0, b)}
          {V.mark("tick", 820, 1080, 140, a + V.LEAD + 1.6)}'''),
        V.scene(4, "ai-14-town-hall.png", "If you can't confirm it, don't share it.", lambda a, b: f'''
          {t("Can't confirm it?", "w", 71, 80, 700, -2, a + 0.3, b)}
          {t("Don't share it.", "l", 77, 110, 860, 2, a + V.LEAD + 1.0, b)}'''),
        V.end_card(5, "ai-12-handshake.png", 'Check before you share.', line='Check before you share.'),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
