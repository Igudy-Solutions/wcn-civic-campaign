#!/usr/bin/env python3
"""Day 24: Wed 23 Dec 2026. Video (Reel). Know Your Power.

Japa plans? Vote before you go.
Spine: travelling soon -> no diaspora, postal or embassy voting -> in person at your unit -> book after 16 Jan -> 6 Feb too.
Facts: Nigerian law has no diaspora or absentee voting (VERIFY before posting).
No day count on screen or in the voice. INEC is voiced "Eye-neck".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 24
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = ['Planning to travel out of Nigeria soon?', 'Nigeria has no voting from abroad. No postal votes. No embassy voting.', 'You can only vote in person, at your own polling unit.', 'If you can, book your trip after Saturday the sixteenth of January.', "And if you'll still be here on the sixth of February, vote again.", 'Vote before you go.']


def spec():
    return [
        V.scene(0, "ai-19-airport.png", 'Planning to travel out of Nigeria soon?', lambda a, b: f'''
          {t("Travelling", "w", 120, 80, 760, -3, a + 0.3, b)}
          {t("soon?", "l", 120, 110, 920, 2, a + 0.9, b)}''', pos="50% 20%"),
        V.scene(1, "ai-18-bus-park.png", 'Nigeria has no voting from abroad. No postal votes. No embassy voting.', lambda a, b: f'''
          <div class="a stamp" data-fx="stamp" data-r="-5" data-in="{a + V.LEAD + .4}" data-out="{b}" style="left:70px;top:520px;font-size:53px">NO VOTING FROM ABROAD</div>
          {t("No postal votes.", "w", 74, 90, 760, 2, a + V.LEAD + 2.0, b)}
          {t("No embassy voting.", "w", 64, 110, 900, -2, a + V.LEAD + 2.9, b)}'''),
        V.scene(2, "ai-01-polling-queue.png", 'You can only vote in person, at your own polling unit.', lambda a, b: f'''
          {t("In person.", "w", 120, 80, 700, -2, a + V.LEAD + 1.0, b)}
          {t("At your polling unit.", "l", 56, 100, 860, 2, a + V.LEAD + 1.6, b)}
          {V.mark("tick", 820, 1060, 140, a + V.LEAD + 2.0)}'''),
        V.scene(3, "ai-15-bus-stop-phone.png", 'If you can, book your trip after Saturday the sixteenth of January.', lambda a, b: f'''
          <div class="a cal" data-fx="slideup" data-r="-3" data-in="{a + V.LEAD + 1.4}" data-out="{b}" style="left:120px;top:420px"><div class="m">JANUARY 2027</div><div class="n">16</div><div class="d">SATURDAY</div><div class="o">Book your trip after this</div></div>''', pos="50% 15%"),
        V.scene(4, "ai-06-walk-to-vote.png", "And if you'll still be here on the sixth of February, vote again.", lambda a, b: f'''
          <div class="a cal" data-fx="slideup" data-r="3" data-in="{a + V.LEAD + 1.4}" data-out="{b}" style="left:120px;top:420px"><div class="m">FEBRUARY 2027</div><div class="n">6</div><div class="d">SATURDAY</div><div class="o">Governor and State Assembly</div></div>'''),
        V.end_card(5, "ai-16-pvc-proud.png", 'Vote before you go.', line='Vote before you go.'),
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
