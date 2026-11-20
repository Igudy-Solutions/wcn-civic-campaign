#!/usr/bin/env python3
"""Day 52: Wed 25 Nov 2026. Video (Reel). Vote Wisely.

Your vote for 5,000 naira? Here is the maths.
Spine: the offer -> do the maths -> 4 years is 1,461 days -> about N3 a day
-> N3 won't buy a sachet of water -> they will spend trillions on your roads,
hospitals and schools -> vote selling is a crime -> don't sell it, show up.

No day count on screen (videos must work any day); the days left go in the
caption. Facts: Electoral Act 2022, s.121 (giving or taking money for a vote
is an offence); federal budget runs to tens of trillions of naira a year.
Render: python3 tools/day_52.py  (or --stills to check one frame per scene)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 52
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

# What the voice says, one line per scene. Written for the ear.
LINES = [
    "Someone offers you five thousand naira for your vote.",
    "It sounds like money. Now do the maths.",
    "Four years is one thousand, four hundred and sixty one days.",
    "Five thousand naira over four years is about three naira a day.",
    "Three naira won't even buy a sachet of water.",
    "But the people you elect will spend trillions of naira. On your roads, your hospitals, your schools.",
    "And selling your vote is a crime under the Electoral Act.",
    "Don't sell your vote. Show up and choose.",
]


def count(to, suffix, size, left, top, r, at, b, cls="l", prefix="", dec=0, dur=1.4):
    return (f'<div class="a tag {cls}" data-fx="count" data-r="{r}" data-in="{at}" data-out="{b}" data-from="0" '
            f'data-to="{to}" data-dec="{dec}" data-prefix="{prefix}" data-suffix="{suffix}" data-dur="{dur}" '
            f'style="left:{left}px;top:{top}px;font-size:{size}px">{prefix}0{suffix}</div>')


def spec():
    return [
        V.scene(0, "ai-11-market-trader.png", "Someone offers you ₦5,000 for your vote.", lambda a, b: f'''
          {t("Your vote", "w", 110, 80, 330, -3, a + .3, b)}
          {count(5000, "", 190, 80, 500, 2, a + .6, b, prefix="₦")}
          {t("for sale?", "k", 110, 200, 830, -2, a + 1.4, b)}''', pos="50% 15%"),
        V.scene(1, "ai-15-bus-stop-phone.png", "It sounds like money. Now do the maths.", lambda a, b: f'''
          {t("Sounds like money.", "w", 84, 70, 360, -2, a + .3, b)}
          {t("Do the maths.", "l", 100, 80, 520, 2, a + 1.4, b)}
          {V.mark("arrow", 800, 760, 170, a + 1.9)}''', pos="50% 15%"),
        V.scene(2, "ai-06-walk-to-vote.png", "Four years is 1,461 days.", lambda a, b: f'''
          {t("4 years =", "w", 110, 80, 360, -3, a + .3, b)}
          {count(1461, "", 260, 80, 530, 2, a + .7, b, dur=1.8)}
          {t("days.", "k", 120, 520, 880, -2, a + 1.6, b)}'''),
        V.scene(3, "ai-11-market-trader.png", "₦5,000 over four years is about ₦3 a day.", lambda a, b: f'''
          <div class="a box" data-fx="slideup" data-r="-2" data-in="{a + .3}" data-out="{b}" style="left:90px;top:330px;width:900px">
            <div class="hdr"><span>The maths</span><span class="chip">÷</span></div>
            <div style="padding:34px 44px 40px;font-weight:700;font-size:56px;line-height:1.35;color:{V.FOREST}">
              ₦5,000 ÷ 1,461 days<br/><span style="font-size:240px;font-weight:800;letter-spacing:-.05em;line-height:1.05">= ₦3</span>
              <span style="font-size:60px">a day</span></div></div>
          {V.mark("tick", 860, 1060, 120, a + 2.4)}''', pos="50% 15%"),
        V.scene(4, "ai-04-friends-debate.png", "₦3 won't even buy a sachet of water.", lambda a, b: f'''
          {t("₦3 won't buy", "w", 110, 80, 380, -3, a + .3, b)}
          {t("a sachet", "l", 120, 140, 560, 2, a + .8, b)}
          {t("of water.", "l", 120, 200, 730, -2, a + 1.0, b)}'''),
        V.scene(5, "ai-09-hospital.png", "But the people you elect will spend trillions of naira. On your roads, your hospitals, your schools.", lambda a, b: f'''
          {t("They will spend", "w", 90, 70, 330, -2, a + .3, b)}
          {t("trillions.", "l", 136, 80, 480, 2, a + .9, b)}
          {t("Your roads.", "k", 70, 110, 760, -2, a + V.LEAD + 3.4, b)}
          {t("Your hospitals.", "k", 70, 150, 880, 2, a + V.LEAD + 4.0, b)}
          {t("Your schools.", "k", 70, 190, 1000, -2, a + V.LEAD + 4.8, b)}''', pos="50% 20%"),
        V.scene(6, "ai-07-ballot-box.png", "And selling your vote is a crime under the Electoral Act.", lambda a, b: f'''
          {t("Selling your vote?", "w", 76, 70, 380, -2, a + .3, b)}
          <div class="a stamp" data-fx="stamp" data-r="-7" data-in="{a + V.LEAD + 1.6}" data-out="{b}" style="left:120px;top:600px;font-size:110px">IT'S A CRIME</div>
          {t("Electoral Act 2022", "k", 56, 260, 900, 2, a + V.LEAD + 2.6, b)}'''),
        V.end_card(7, "ai-02-inked-thumb.png", "Don't sell your vote. Show up and choose.", line="Don't sell it. Show up."),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
