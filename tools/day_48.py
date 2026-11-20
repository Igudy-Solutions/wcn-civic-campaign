#!/usr/bin/env python3
"""Day 48: Sun 29 Nov 2026. Video (Reel). Know Your Power.

Not your uncle's vote. Not your pastor's. Not your boss's. Yours.
Spine: everyone has an opinion (uncle, pastor or imam, boss) -> listen, then
decide -> the ballot is secret -> not their vote, yours.
Religion handled evenly: pastor and imam together. No day count on screen.
Facts: secret ballot (Electoral Act 2022).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 48
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = [
    "Your uncle has an opinion on who you should vote for.",
    "Your pastor or your imam might too.",
    "So might your boss.",
    "Listen to all of them. Then decide for yourself.",
    "Your ballot is secret. Nobody sees who you choose.",
    "Not their vote. Yours.",
]


def spec():
    return [
        V.scene(0, "ai-13-family-table.png", "Your uncle has an opinion on who you should vote for.", lambda a, b: f'''
          {t("Your uncle", "w", 130, 80, 820, -3, a + .3, b)}
          {t("has an opinion.", "l", 86, 110, 1010, 2, a + .8, b)}''', pos="50% 20%"),
        V.scene(1, "ai-14-town-hall.png", "Your pastor or your imam might too.", lambda a, b: f'''
          {t("Your pastor.", "w", 110, 80, 820, -2, a + .3, b)}
          {t("Your imam.", "w", 110, 200, 990, 2, a + .9, b)}'''),
        V.scene(2, "ai-15-bus-stop-phone.png", "So might your boss.", lambda a, b: f'''
          {t("Your boss.", "w", 130, 80, 860, -3, a + .3, b)}''', pos="50% 15%"),
        V.scene(3, "ai-04-friends-debate.png", "Listen to all of them. Then decide for yourself.", lambda a, b: f'''
          {t("Listen.", "w", 140, 80, 380, -3, a + .3, b)}
          {t("Then decide", "l", 100, 90, 600, 2, a + V.LEAD + 1.3, b)}
          {t("for yourself.", "l", 100, 130, 770, -2, a + V.LEAD + 1.6, b)}'''),
        V.scene(4, "ai-07-ballot-box.png", "Your ballot is secret. Nobody sees who you choose.", lambda a, b: f'''
          <div class="a stamp" data-fx="stamp" data-r="-6" data-in="{a + .5}" data-out="{b}" style="left:90px;top:420px;font-size:96px">SECRET BALLOT</div>
          {t("Nobody sees", "w", 96, 90, 720, 2, a + V.LEAD + 1.5, b)}
          {t("who you choose.", "w", 82, 120, 890, -2, a + V.LEAD + 1.8, b)}
          {V.mark("thumb", 820, 1060, 140, a + 2.2)}'''),
        V.end_card(5, "ai-16-pvc-proud.png", "Not their vote. Yours.", line="Not their vote. Yours."),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
