#!/usr/bin/env python3
"""Writes the six voiced video scripts (Days 43, 32, 24, 16, 7, 1) and their captions."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import write_captions, ROOT

HEAD = '''#!/usr/bin/env python3
"""Day {day}: {date}. Video (Reel). {pillar}.

{doc}
No day count on screen or in the voice. INEC is voiced "Eye-neck".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video_engine as V  # noqa: E402
from plan import folder_for  # noqa: E402

DAY = {day}
OUT = os.path.join(V.ROOT, folder_for(DAY))
t = V.tag

LINES = {lines!r}


def spec():
    return [
{scenes}
    ]


if __name__ == "__main__":
    V.make(OUT, "video.mp4", spec, lines=LINES)
'''


def sc(i, photo, sub, body, pos=None):
    p = f', pos="{pos}"' if pos else ""
    return f'        V.scene({i}, "{photo}", {sub!r}, lambda a, b: f\'\'\'{body}\'\'\'{p}),'


def end(i, photo, sub, line):
    return f'        V.end_card({i}, "{photo}", {sub!r}, line={line!r}),'


def write(day, date, pillar, doc, lines, subs, scenes):
    src = HEAD.format(day=day, date=date, pillar=pillar, doc=doc.strip(), lines=lines,
                      scenes="\n".join(scenes))
    path = os.path.join(ROOT, "tools", f"day_{day:02d}.py")
    open(path, "w").write(src)
    return path


def fit(txt, size, x, k=0.72, right=1010):
    """Shrink a size so the uppercase sticker clears the right edge."""
    n = len(txt.replace("&quot;", '"'))
    return min(size, int((right - x - 60) / (k * n)))


T = lambda txt, cls, size, x, y, r, d, b="b": _T(txt, cls, fit(txt, size, x), x, y, r, d, b)
_T = lambda txt, cls, size, x, y, r, d, b="b": f'\n          {{t("{txt}", "{cls}", {size}, {x}, {y}, {r}, a + {d}, {b})}}'
M = lambda kind, x, y, s, d: f'\n          {{V.mark("{kind}", {x}, {y}, {s}, a + {d})}}'
STAMP = lambda txt, x, y, size, r, d: _S(txt, x, y, fit(txt, size, x, 0.78), r, d)
_S = lambda txt, x, y, size, r, d: (f'\n          <div class="a stamp" data-fx="stamp" data-r="{r}" data-in="{{a + {d}}}" '
                                      f'data-out="{{b}}" style="left:{x}px;top:{y}px;font-size:{size}px">{txt}</div>')

# ---------------------------------------------------------------- Day 43
L43 = [
    "A message lands in your family group. It says the election has been moved.",
    "Before you forward it, stop.",
    "Who sent it first? Is there a date? Is there a name you can check?",
    "Election news comes from Eye-neck. Check its website and its verified pages.",
    "If you can't confirm it, don't share it.",
    "Check before you share.",
]
write(43, "Fri 4 Dec 2026", "Know the Process",
      "Before you forward that election broadcast, check it.\nSpine: a broadcast lands -> stop -> three questions -> INEC is the source -> unsure, don't share.\nFacts: INEC publishes election dates and notices on its website and verified pages.",
      L43, None, [
    sc(0, "ai-15-bus-stop-phone.png", L43[0], T("Forwarded", "w", 120, 80, 760, -3, .3) + T("many times.", "l", 90, 110, 920, 2, .9), "50% 15%"),
    sc(1, "ai-04-friends-debate.png", L43[1], STAMP("STOP", 120, 520, 180, -6, .5) + T("before you forward.", "w", 80, 100, 840, 2, "V.LEAD + .6")),
    sc(2, "ai-13-family-table.png", L43[2], T("Who sent it?", "w", 96, 80, 420, -2, .3) + T("Is it dated?", "w", 96, 110, 580, 2, "V.LEAD + 1.3") + T("Can you check it?", "l", 86, 80, 740, -2, "V.LEAD + 2.4"), "50% 20%"),
    sc(3, "ai-22-official-explains.png", L43[3], T("Election news", "w", 100, 80, 760, -2, .3) + T("comes from INEC.", "l", 96, 110, 910, 2, "V.LEAD + 1.0") + M("tick", 820, 1080, 140, "V.LEAD + 1.6")),
    sc(4, "ai-14-town-hall.png", L43[4], T("Can't confirm it?", "w", 96, 80, 700, -2, .3) + T("Don't share it.", "l", 110, 110, 860, 2, "V.LEAD + 1.0")),
    end(5, "ai-12-handshake.png", L43[5], "Check before you share."),
])
write_captions(43, "Video", "Know the Process",
    "Before you forward that election broadcast, check it. Three questions, one trusted source, and a simple rule: if you can't confirm it, don't share it.",
    [("ai-15-bus-stop-phone", "A broadcast lands: forwarded many times"),
     ("ai-04-friends-debate", "STOP stamp: before you forward"),
     ("ai-13-family-table", "Three questions: who sent it, is it dated, can you check it"),
     ("ai-22-official-explains", "Election news comes from INEC"),
     ("ai-14-town-hall", "Can't confirm it? Don't share it"),
     ("ai-12-handshake", "End card: Check before you share")],
    ["INEC publishes election dates, notices and results through its official website and verified social media pages",
     "Voiceover by Kokoro TTS (af_heart). Video carries no day count"],
    """Before you forward that election broadcast, stop. 🛑

Ask three things:
1️⃣ Who sent it first?
2️⃣ Is there a date on it?
3️⃣ Can you check it anywhere?

Election news comes from INEC: its website and its verified pages. If you can't confirm it, don't share it.

Send this to the family group that forwards everything. 😅

43 days to election day.""",
    ["Before you forward that election broadcast, stop.\n\nWho sent it first? Is it dated? Can you check it?\n\nElection news comes from INEC. If you can't confirm it, don't share it.\n\n43 days to go. #NigeriaDecides2027"])

# ---------------------------------------------------------------- Day 32
L32 = [
    "I voted in twenty twenty-three and nothing changed. We hear you.",
    "In twenty twenty-three, about ninety-three million people registered. About sixty-eight million of them did not vote.",
    "Elections are decided by the people who show up.",
    "And one vote is only the start. Know who you elected. Ask what they did.",
    "Change takes more than one Saturday. It starts with this one.",
    "Vote. Then follow up.",
]
write(32, "Tue 15 Dec 2026", "Know Your Power",
      "I voted in 2023 and nothing changed.\nSpine: we hear you -> 68 million stayed home -> elections go to who shows up -> vote, then follow up.\nFacts: INEC 2023: 93.4m registered, about 25m votes cast (26.7% turnout).",
      L32, None, [
    sc(0, "ai-11-market-trader.png", L32[0], T("&quot;Nothing changed.&quot;", "w", 100, 80, 760, -3, .3) + T("We hear you.", "l", 96, 110, 920, 2, "V.LEAD + 2.2")),
    sc(1, "ai-01-polling-queue.png", L32[1], T("93 million", "w", 120, 80, 520, -2, "V.LEAD + 1.4") + T("registered.", "w", 80, 100, 680, 2, "V.LEAD + 1.9") + T("68 million", "l", 120, 80, 840, -2, "V.LEAD + 3.6") + T("didn't vote.", "l", 80, 100, 1000, 2, "V.LEAD + 4.2")),
    sc(2, "ai-23-inked-group.png", L32[2], T("Elections go to", "w", 90, 80, 760, -2, .3) + T("who shows up.", "l", 110, 110, 900, 2, "V.LEAD + 1.4") + M("thumb", 820, 1080, 140, "V.LEAD + 1.8")),
    sc(3, "ai-14-town-hall.png", L32[3], T("Know who", "w", 100, 80, 640, -2, "V.LEAD + 1.6") + T("you elected.", "w", 100, 110, 790, 2, "V.LEAD + 2.2") + T("Ask what they did.", "l", 86, 80, 950, -2, "V.LEAD + 3.3")),
    sc(4, "ai-06-walk-to-vote.png", L32[4], T("It starts", "w", 110, 80, 760, -2, "V.LEAD + 2.0") + T("with this one.", "l", 110, 110, 910, 2, "V.LEAD + 2.6")),
    end(5, "ai-02-inked-thumb.png", L32[5], "Vote. Then follow up."),
])
write_captions(32, "Video", "Know Your Power",
    "Answers the common objection \"I voted in 2023 and nothing changed\" with respect and one fact: about 68 million registered voters stayed home. Then the second half of the job: follow up on who you elect.",
    [("ai-11-market-trader", "\"Nothing changed.\" We hear you"),
     ("ai-01-polling-queue", "93 million registered, 68 million didn't vote"),
     ("ai-23-inked-group", "Elections go to who shows up"),
     ("ai-14-town-hall", "Know who you elected. Ask what they did"),
     ("ai-06-walk-to-vote", "It starts with this one"),
     ("ai-02-inked-thumb", "End card: Vote. Then follow up.")],
    ["2023: 93.4 million registered, about 25 million votes cast (turnout 26.7%), so about 68 million did not vote: INEC",
     "Voiceover by Kokoro TTS (af_heart). Video carries no day count"],
    """\"I voted in 2023 and nothing changed.\" We hear you. 💬

In 2023, about 93 million Nigerians registered. About 68 million of them didn't vote. Elections go to the people who show up.

And voting is only half the job. Know who you elected. Ask what they did with your vote. Show up again.

Change takes more than one Saturday. It starts with this one. 🗳️

32 days to election day.""",
    ["\"I voted in 2023 and nothing changed.\"\n\nWe hear you. In 2023 about 68 million registered voters stayed home. Elections go to who shows up.\n\nThen follow up: know who you elected, ask what they did.\n\n32 days to go. #NigeriaDecides2027"])

# ---------------------------------------------------------------- Day 24
L24 = [
    "Planning to travel out of Nigeria soon?",
    "Nigeria has no voting from abroad. No postal votes. No embassy voting.",
    "You can only vote in person, at your own polling unit.",
    "If you can, book your trip after Saturday the sixteenth of January.",
    "And if you'll still be here on the sixth of February, vote again.",
    "Vote before you go.",
]
write(24, "Wed 23 Dec 2026", "Know Your Power",
      "Japa plans? Vote before you go.\nSpine: travelling soon -> no diaspora, postal or embassy voting -> in person at your unit -> book after 16 Jan -> 6 Feb too.\nFacts: Nigerian law has no diaspora or absentee voting (VERIFY before posting).",
      L24, None, [
    sc(0, "ai-19-airport.png", L24[0], T("Travelling", "w", 120, 80, 760, -3, .3) + T("soon?", "l", 120, 110, 920, 2, .9), "50% 20%"),
    sc(1, "ai-18-bus-park.png", L24[1], STAMP("NO VOTING FROM ABROAD", 70, 520, 66, -5, "V.LEAD + .4") + T("No postal votes.", "w", 80, 90, 760, 2, "V.LEAD + 2.0") + T("No embassy voting.", "w", 80, 110, 900, -2, "V.LEAD + 2.9")),
    sc(2, "ai-01-polling-queue.png", L24[2], T("In person.", "w", 120, 80, 700, -2, "V.LEAD + 1.0") + T("At your polling unit.", "l", 80, 100, 860, 2, "V.LEAD + 1.6") + M("tick", 820, 1060, 140, "V.LEAD + 2.0")),
    sc(3, "ai-15-bus-stop-phone.png", L24[3], f'''
          <div class="a cal" data-fx="slideup" data-r="-3" data-in="{{a + V.LEAD + 1.4}}" data-out="{{b}}" style="left:120px;top:420px"><div class="m">JANUARY 2027</div><div class="n">16</div><div class="d">SATURDAY</div><div class="o">Book your trip after this</div></div>''', "50% 15%"),
    sc(4, "ai-06-walk-to-vote.png", L24[4], f'''
          <div class="a cal" data-fx="slideup" data-r="3" data-in="{{a + V.LEAD + 1.4}}" data-out="{{b}}" style="left:120px;top:420px"><div class="m">FEBRUARY 2027</div><div class="n">6</div><div class="d">SATURDAY</div><div class="o">Governor and State Assembly</div></div>'''),
    end(5, "ai-16-pvc-proud.png", L24[5], "Vote before you go."),
])
write_captions(24, "Video", "Know Your Power",
    "For anyone planning to relocate or travel: Nigeria has no diaspora, postal or embassy voting, so the only way to vote is in person at your own polling unit. Book travel after 16 Jan, and after 6 Feb if you can.",
    [("ai-19-airport", "Travelling soon?"),
     ("ai-18-bus-park", "No voting from abroad. No postal votes. No embassy voting"),
     ("ai-01-polling-queue", "In person, at your polling unit"),
     ("ai-15-bus-stop-phone", "Calendar: Sat 16 Jan, book your trip after this"),
     ("ai-06-walk-to-vote", "Calendar: Sat 6 Feb, Governor and State Assembly"),
     ("ai-16-pvc-proud", "End card: Vote before you go.")],
    ["Nigeria has no diaspora, postal or absentee voting; voters vote in person at their registered polling unit: Electoral Act 2022 and INEC (VERIFY the current position before posting)",
     "Dates: Sat 16 Jan 2027 (President, National Assembly), Sat 6 Feb 2027 (Governor, State Assembly): INEC revised timetable",
     "Voiceover by Kokoro TTS (af_heart). Video carries no day count"],
    """Japa plans? ✈️ Vote before you go.

Nigeria has no voting from abroad. No postal votes. No embassy voting. The only way to vote is in person, at your own polling unit, with your PVC.

📅 Sat 16 Jan: President, Senate, House of Reps
📅 Sat 6 Feb: Governor and State House of Assembly

If you can, book the flight for after. Your vote doesn't travel with you.

Tag someone who's packing. 🧳

24 days to election day.""",
    ["Japa plans? Vote before you go. ✈️\n\nNigeria has no voting from abroad: no postal votes, no embassy voting. Only in person, at your own polling unit.\n\nSat 16 Jan and Sat 6 Feb. Book the flight for after.\n\n24 days to go. #NigeriaDecides2027"])

# ---------------------------------------------------------------- Day 16
L16 = [
    "On election night, results will fly around your phone.",
    "Some will be real. Many will not.",
    "Real results start at your polling unit. They're counted in public and pinned on the wall.",
    "Eye-neck uploads polling unit results to its results viewing portal, and only Eye-neck declares the winner.",
    "Don't share a result you can't trace.",
    "Wait for Eye-neck.",
]
write(16, "Thu 31 Dec 2026", "Know the Process",
      "Fake results travel faster than real ones. Wait for INEC.\nSpine: results flood phones -> some fake -> real results start at the unit -> IReV and INEC declare -> don't share what you can't trace.\nFacts: public count, EC8A posted at the unit, IReV upload, INEC returning officers declare (VERIFY wording).",
      L16, None, [
    sc(0, "ai-15-bus-stop-phone.png", L16[0], T("Results", "w", 120, 80, 760, -3, .3) + T("on your phone.", "l", 96, 110, 920, 2, "V.LEAD + 1.6"), "50% 15%"),
    sc(1, "ai-04-friends-debate.png", L16[1], T("Some real.", "w", 110, 80, 700, -2, "V.LEAD + .2") + T("Many not.", "l", 120, 110, 860, 2, "V.LEAD + 1.2")),
    sc(2, "ai-03-public-count.png", L16[2], T("Counted", "w", 110, 80, 680, -2, "V.LEAD + 2.2") + T("in public.", "l", 110, 110, 830, 2, "V.LEAD + 2.6") + M("tick", 820, 1060, 140, "V.LEAD + 3.0")),
    sc(3, "ai-26-results-wall.png", L16[3], T("Only INEC", "w", 120, 80, 700, -2, "V.LEAD + 3.6") + T("declares.", "l", 120, 110, 860, 2, "V.LEAD + 4.2")),
    sc(4, "ai-13-family-table.png", L16[4], STAMP("CAN'T TRACE IT?", 80, 520, 84, -5, .4) + T("Don't share it.", "w", 100, 100, 760, 2, "V.LEAD + 1.0"), "50% 20%"),
    end(5, "ai-22-official-explains.png", L16[5], "Wait for INEC."),
])
write_captions(16, "Video", "Know the Process",
    "Prepares followers for election night: fake results spread faster than real ones. Real results start at the polling unit, are uploaded by INEC, and only INEC declares winners.",
    [("ai-15-bus-stop-phone", "Results on your phone"),
     ("ai-04-friends-debate", "Some real. Many not"),
     ("ai-03-public-count", "Real results are counted in public at the unit"),
     ("ai-26-results-wall", "INEC uploads to IReV; only INEC declares"),
     ("ai-13-family-table", "Can't trace it? Don't share it"),
     ("ai-22-official-explains", "End card: Wait for INEC.")],
    ["Votes are counted in public at the polling unit and the result sheet (EC8A) is posted there: Electoral Act 2022, INEC guidelines (VERIFY)",
     "INEC uploads polling unit results to the IReV portal; only INEC returning officers declare results: INEC (VERIFY)",
     "Voiceover by Kokoro TTS (af_heart). Video carries no day count"],
    """Fake results travel faster than real ones. 📲

On election night your phone will fill up with numbers. Some real. Many not.

✅ Real results are counted in public at each polling unit and pinned on the wall
✅ INEC uploads polling unit results to its IReV portal
✅ Only INEC declares the winner

Can't trace it? Don't share it. Wait for INEC.

Happy New Year's Eve. Start 2027 with facts. 🎆

16 days to election day.""",
    ["Fake results travel faster than real ones.\n\nReal results are counted in public at your polling unit, uploaded to INEC's IReV portal, and only INEC declares.\n\nCan't trace it? Don't share it. Wait for INEC.\n\n16 days to go. #NigeriaDecides2027"])

# ---------------------------------------------------------------- Day 7
L7 = [
    "Do you know exactly where you're voting?",
    "Your polling unit is printed on your voter's card. You can also check it with Eye-neck.",
    "Go and see it before election day. Find the gate, the building, the way in.",
    "Movement is usually restricted on election day, so plan to walk or go nearby.",
    "Go early. Take your card. Take water.",
    "Know your route.",
]
write(7, "Sat 9 Jan 2027", "Know the Process",
      "Know your route to your polling unit.\nSpine: do you know where -> it's on your PVC, check with INEC -> visit before -> movement restricted -> go early.\nFacts: PU on PVC and INEC voter verification; vehicle movement is normally restricted on election day (VERIFY for 2027).",
      L7, None, [
    sc(0, "ai-06-walk-to-vote.png", L7[0], T("Where exactly", "w", 110, 80, 760, -3, .3) + T("are you voting?", "l", 96, 110, 910, 2, "V.LEAD + 1.0")),
    sc(1, "ai-08-pvc-collection.png", L7[1], T("It's on", "w", 110, 80, 640, -2, "V.LEAD + 1.0") + T("your PVC.", "l", 120, 110, 790, 2, "V.LEAD + 1.4") + T("Or check with INEC.", "w", 80, 80, 990, -2, "V.LEAD + 3.2")),
    sc(2, "ai-01-polling-queue.png", L7[2], T("Visit it", "w", 120, 80, 700, -2, .3) + T("before the day.", "l", 100, 110, 860, 2, .9) + M("arrow", 800, 1060, 160, "V.LEAD + 2.0")),
    sc(3, "ai-24-peace-walk.png", L7[3], STAMP("PLAN TO WALK", 90, 560, 92, -5, "V.LEAD + 2.4") + T("Roads may close.", "w", 80, 90, 800, 2, "V.LEAD + 1.2")),
    sc(4, "ai-16-pvc-proud.png", L7[4], T("Go early.", "w", 120, 80, 700, -2, "V.LEAD + .1") + T("Card. Water.", "l", 110, 110, 860, 2, "V.LEAD + 1.0")),
    end(5, "ai-23-inked-group.png", L7[5], "Know your route."),
])
write_captions(7, "Video", "Know the Process",
    "Know your route to your polling unit: find it on your PVC or check with INEC, visit it before election day, plan to walk because movement is usually restricted, and go early.",
    [("ai-06-walk-to-vote", "Where exactly are you voting?"),
     ("ai-08-pvc-collection", "It's on your PVC, or check with INEC"),
     ("ai-01-polling-queue", "Visit it before the day"),
     ("ai-24-peace-walk", "Plan to walk: roads may close"),
     ("ai-16-pvc-proud", "Go early. Card. Water."),
     ("ai-23-inked-group", "End card: Know your route.")],
    ["Polling unit is shown on the PVC and can be checked through INEC's voter verification service: INEC",
     "Vehicle movement is normally restricted on election day: police and INEC practice in past elections (VERIFY the 2027 order)",
     "Voiceover by Kokoro TTS (af_heart). Video carries no day count"],
    """One week to go. 📍 Do you know your route?

✅ Your polling unit is on your PVC. You can also check it with INEC.
✅ Visit it this week. Find the gate, the building, the way in.
✅ Movement is usually restricted on election day, so plan to walk.
✅ Go early. Take your PVC and some water.

Saturday 16 January. See you in the queue. 🗳️

7 days to election day.""",
    ["One week. Do you know your route? 📍\n\nYour polling unit is on your PVC. Visit it this week. Roads are usually closed on election day, so plan to walk.\n\nGo early. Take your PVC.\n\n7 days to go. #NigeriaDecides2027"])

# ---------------------------------------------------------------- Day 1
L1 = [
    "Saturday, the sixteenth of January. Nigeria decides.",
    "Three ballots. President, Senate, House of Representatives.",
    "Take your voter's card. Go early. Stay in the queue.",
    "Your ballot is secret. Nobody can buy it and nobody can see it.",
    "Whatever happens, stay peaceful. Wait for Eye-neck.",
    "Go early. Stay peaceful.",
]
write(1, "Fri 15 Jan 2027", "Know Your Power",
      "Nigeria decides. Go early. Stay peaceful.\nSpine: Saturday 16 Jan -> three ballots -> PVC, early, stay -> secret ballot -> peace, wait for INEC.\nFacts: INEC timetable; three federal ballots on 16 Jan.",
      L1, None, [
    sc(0, "ai-01-polling-queue.png", L1[0], f'''
          <div class="a cal" data-fx="slideup" data-r="-3" data-in="{{a + .3}}" data-out="{{b}}" style="left:120px;top:380px"><div class="m">JANUARY 2027</div><div class="n">16</div><div class="d">SATURDAY</div><div class="o">Nigeria decides</div></div>'''),
    sc(1, "ai-07-ballot-box.png", L1[1], T("President.", "w", 110, 80, 600, -2, "V.LEAD + 1.4") + T("Senate.", "w", 110, 110, 750, 2, "V.LEAD + 2.6") + T("House of Reps.", "l", 100, 80, 900, -2, "V.LEAD + 3.2")),
    sc(2, "ai-16-pvc-proud-card.png", L1[2], T("Your PVC.", "w", 110, 80, 700, -2, .3) + T("Go early.", "l", 110, 110, 850, 2, "V.LEAD + 1.4") + T("Stay.", "w", 110, 80, 1000, -2, "V.LEAD + 2.3")),
    sc(3, "ai-05-bvas-accreditation.png", L1[3], STAMP("SECRET BALLOT", 90, 520, 96, -6, .5) + T("Not for sale.", "w", 96, 100, 760, 2, "V.LEAD + 1.6")),
    sc(4, "ai-24-peace-walk.png", L1[4], T("Stay peaceful.", "w", 110, 80, 700, -2, "V.LEAD + .3") + T("Wait for INEC.", "l", 110, 110, 860, 2, "V.LEAD + 1.6")),
    end(5, "ai-23-inked-group.png", L1[5], "Go early. Stay peaceful."),
])
write_captions(1, "Video", "Know Your Power",
    "Election eve. Nigeria decides on Saturday 16 January: three ballots, take your PVC, go early, stay in the queue, your ballot is secret, stay peaceful and wait for INEC.",
    [("ai-01-polling-queue", "Calendar: Saturday 16 January, Nigeria decides"),
     ("ai-07-ballot-box", "President. Senate. House of Reps."),
     ("ai-16-pvc-proud-card", "Your PVC. Go early. Stay."),
     ("ai-05-bvas-accreditation", "Secret ballot. Not for sale."),
     ("ai-24-peace-walk", "Stay peaceful. Wait for INEC."),
     ("ai-23-inked-group", "End card: Go early. Stay peaceful.")],
    ["Sat 16 Jan 2027: Presidential, Senate and House of Representatives elections: INEC revised timetable, 26 Feb 2026",
     "Campaigns close 24 hours before polling: no candidate content on this post",
     "Voiceover by Kokoro TTS (af_heart). Video carries no day count"],
    """Tomorrow, Nigeria decides. 🇳🇬

🗳️ Three ballots: President, Senate, House of Representatives
🪪 Take your PVC
⏰ Go early and stay in the queue
🤫 Your ballot is secret. Nobody can buy it, nobody can see it
🕊️ Whatever happens, stay peaceful and wait for INEC

And on Saturday 6 February, do it again for Governor and State House of Assembly.

Go early. Stay peaceful. See you at the polling unit.""",
    ["Tomorrow, Nigeria decides. 🇳🇬\n\nThree ballots: President, Senate, House of Reps. Take your PVC. Go early. Stay in the queue.\n\nYour ballot is secret. Stay peaceful. Wait for INEC.\n\n#NigeriaDecides2027"])

print("videos written")
