#!/usr/bin/env python3
"""Day 57: Fri 20 Nov 2026. The launch post.

The countdown starts. Hook on 2023 turnout, then the two dates, the numbers
behind them, the PVC, and the line from the content plan about vote buying.

Facts and where they come from:
  * Dates: INEC revised timetable, 26 Feb 2026 (16 Jan and 6 Feb 2027)
  * 2023: ~93m registered, ~25m voted, 26.7% turnout, winning margin ~1.8m
    (INEC figures)
  * 103.4m registered for 2027 (INEC October 2026 update,
    before the final register is published)
  * PVC collection at your INEC LGA office, in person (INEC)

WCN is not affiliated with whyvote.ng. Never name or link it on a slide or in
a caption. Cite INEC or the primary source.

Photos: AI generated scenes of Nigerians voting, in images/ai/ (made in
Figma, 20 Nov 2026). Swap any for a real photo by changing `photo=`.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = 57
OUT = folder_for(DAY)

# The story, one slide handing to the next:
#   hook (73% stayed home) -> what 2023 looked like -> why it mattered
#   -> 2027 is bigger -> when you show up -> what you need first
#   -> what not to trade it for -> don't be the 73% this time.
# Each lead line answers or picks up the slide before it.
SLIDES = [
    ("cover", dict(
        title="73% of us did not\nvote in 2023.\n*Will you be\none of them?*",
        size=124,
        photo="ai-01-polling-queue.png",
    )),
    ("stat", dict(
        lead="Here is what 2023 looked like.\nAbout **93 million** of us registered.\nAbout **25 million** showed up.",
        number="26.7%",
        size=250,
        label="turnout. The lowest\n*since 1999.*",
        source="INEC",
        photo="ai-07-ballot-box.png",
    )),
    ("statement", dict(
        lead="Did it matter? The presidential race\nwas won by about **1.8 million** votes.\nMeanwhile...",
        punch="68 million\nregistered voters\nstayed home.",
        size=110,
        body="The people who stayed home could have decided it many times over.",
        source="INEC",
        photo="ai-04-friends-debate.png",
    )),
    ("stat", dict(
        lead="Now it is 2027, and the list is longer.",
        number="103.4M",
        size=230,
        label="registered voters.\n*That includes you.*",
        body="INEC's October 2026 update. The final register is still to come.",
        source="INEC",
        photo="ai-05-bvas-accreditation.png",
    )),
    ("dates", dict(
        lead="So when do you show up?\nTwo Saturdays. Five offices.",
        title="Mark these *now.*",
        rows=[
            ("16 Jan", "Sat · 2027", "President, Senate, House of Reps", "Three ballot papers"),
            ("06 Feb", "Sat · 2027", "Governor, State House of Assembly", "Two ballot papers"),
        ],
        source="INEC revised timetable, 26 Feb 2026",
        photo="ai-06-walk-to-vote.png",
    )),
    ("statement", dict(
        lead="But none of that counts without one card.\nA registration without a PVC\nis a vote you can't cast.",
        punch="Collect your PVC.\nIn person.",
        body="Go to your INEC LGA office. Nobody can collect it for you.",
        source="INEC",
        photo="ai-08-pvc-collection.png",
    )),
    ("statement", dict(
        lead="And when someone offers ₦5,000 for it?\nSpread over four years, that's about\n**₦3 a day.**",
        punch="The bribe can't\nlast you 4 years.",
        size=112,
        body="Vote your choice. Don't sell your vote.",
        photo="ai-03-public-count.png",
    )),
    ("cta", dict(
        lead="57 days from now, the count starts again.\nDon't be part of the 73% this time.",
        punch="Save. Share.\nShow up.",
        body="Follow World Changers Network, and send this to someone who skipped 2023.",
        photo="ai-02-inked-thumb.png",
    )),
]

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
