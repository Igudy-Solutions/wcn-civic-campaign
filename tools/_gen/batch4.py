import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import write_script, write_captions

# ---------------------------------------------------------------- Day 15
write_script(15, "Single", "Know Your Power", """
Happy New Year. 2027 is the year you choose. 1 Jan.
Photo: ai-23-inked-group.""", '''
SLIDES = [
    ("statement", dict(
        kicker="1 January 2027",
        lead="Happy New Year from World Changers Network.",
        punch="2027 is the\\nyear *you\\nchoose.*",
        size=140,
        body="Two Saturdays: 16 January and 6 February. Make showing up your first resolution.",
        photo="ai-23-inked-group.png",
        pos="50% 12%",
    )),
]''')
write_captions(15, "Single", "Know Your Power",
    "New Year's Day post: the year you choose.",
    [("Young voters with inked thumbs", "Happy New Year. 2027 is the year you choose. 16 Jan and 6 Feb")],
    ["Election dates Sat 16 Jan and Sat 6 Feb 2027: INEC revised timetable, 26 Feb 2026"],
    """Happy New Year from all of us at World Changers Network.

2027 is the year you choose.

Two Saturdays: 16 January for President and the National Assembly, 6 February for Governor and State Assembly.

Make showing up your first resolution of the year.""",
    ["""Happy New Year from World Changers Network.

2027 is the year you choose. Sat 16 Jan and Sat 6 Feb.

Make showing up your first resolution. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 14
write_script(14, "Carousel", "Know the Process", """
Two weeks to go. Your election checklist.
Spine: hook -> five things to sort this week -> the two dates -> CTA.
VERIFY any INEC procedure mentioned before posting.""", '''
SLIDES = [
    ("cover", dict(
        title="Two weeks\\nto go. *Your\\nelection\\nchecklist.*",
        size=126,
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
    ("list", dict(
        kicker="Sort these this week",
        title="Your\\n*checklist*",
        size=96,
        items=[("PVC in your hand", "Not \\u201csomewhere at home\\u201d. Find it today"),
               ("Know your polling unit", "It's on your PVC. Confirm it with INEC"),
               ("Plan your route", "Walk it or drive past once. Movement will be limited on the day"),
               ("Plan the day", "Go early. Water, umbrella, patience"),
               ("Bring three people", "Agree now who you're going with")],
        photo="ai-01-polling-queue.png",
    )),
    ("dates", dict(
        kicker="Mark both",
        title="Two\\n*Saturdays*",
        size=96,
        rows=[("16 Jan", "Saturday", "President, Senate, House of Reps", "Three ballots"),
              ("6 Feb", "Saturday", "Governor and State House of Assembly", "Governor in 28 states, Assembly in all 36")],
        photo="ai-06-walk-to-vote.png",
        source="INEC",
    )),
    ("cta", dict(
        lead="Tick all five, then send this to the\\nthree people you're going with.",
        punch="Ready in\\ntwo weeks.",
        body="Save this checklist.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(14, "Carousel", "Know the Process",
    "Two-week checklist: PVC, polling unit, route, plan for the day, bring people.",
    [("Young woman holding her voter card", "Two weeks to go. Your election checklist"),
     ("Queue outside a polling unit", "PVC, polling unit, route, plan the day, bring three people"),
     ("Walking to vote", "16 Jan and 6 Feb, what's on each ballot"),
     ("Young voters with inked thumbs", "Ready in two weeks")],
    ["Election dates and offices: INEC revised timetable, 26 Feb 2026",
     "Governorship in 28 states (8 off-cycle), State Assembly in all 36: INEC"],
    """Two weeks to go. Your election checklist:

1. PVC in your hand. Not "somewhere at home"
2. Know your polling unit. It's on your PVC, confirm it with INEC
3. Plan your route. Movement will be limited on the day
4. Plan the day. Go early. Water, umbrella, patience
5. Bring three people. Agree now who you're going with

Saturday 16 January: President, Senate, House of Reps.
Saturday 6 February: Governor and State House of Assembly.

Tick all five, then send this to the people you're going with.""",
    ["""Two weeks to go. Your checklist:

1 PVC in your hand
2 Know your polling unit
3 Plan your route
4 Plan the day: go early
5 Bring three people

Sat 16 Jan, then Sat 6 Feb. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 13
write_script(13, "Carousel", "Know Your Power", """
Your rights as a voter on election day.
Spine: hook -> six rights over two list slides -> if something goes wrong ->
CTA. VERIFY with INEC's 2027 Regulations and Guidelines and the Electoral
Act before posting.""", '''
SLIDES = [
    ("cover", dict(
        title="Your rights\\nas a voter on\\n*election day.*",
        size=126,
        photo="ai-27-wheelchair-voter.png",
    )),
    ("list", dict(
        kicker="Rights 1 to 3",
        title="Know\\n*your rights*",
        size=96,
        items=[("A secret ballot", "Nobody can watch you vote or make you show it"),
               ("To vote if you're in the queue", "If you're in line when voting closes, you still vote"),
               ("Help if you need it", "Elderly voters, people with disabilities and pregnant women get priority and can bring someone to assist")],
        photo="ai-27-wheelchair-voter.png",
    )),
    ("list", dict(
        kicker="Rights 4 to 6",
        title="Know\\n*your rights*",
        size=96,
        start=4,
        items=[("To vote free from pressure", "No one can force, threaten or pay you"),
               ("To watch the count", "Counting is public. You can stay and observe, peacefully"),
               ("To see the result", "The EC8A result sheet is posted at your unit")],
        photo="ai-03-public-count.png",
    )),
    ("statement", dict(
        lead="If something goes wrong at your unit:",
        punch="Speak to the\\npresiding\\nofficer.",
        size=118,
        body="Stay calm, explain clearly, and if it isn't resolved, report it to INEC or the police.",
        photo="ai-22-official-explains.png",
    )),
    ("cta", dict(
        lead="Know your rights. Use them calmly.",
        punch="Save it for\\nthe day.",
        body="Send this to someone voting for the first time.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(13, "Carousel", "Know Your Power",
    "Voter rights on election day, and what to do if something goes wrong.",
    [("Voter in a wheelchair being assisted", "Your rights as a voter on election day"),
     ("Voter being assisted", "Secret ballot; in the queue at close, you vote; help and priority if you need it"),
     ("Public count", "Free from pressure; watch the count; see the result"),
     ("Official explaining the ballot", "If something goes wrong: speak to the presiding officer"),
     ("Young voters with inked thumbs", "Save it for the day")],
    ["VERIFY before posting: each right against the Electoral Act and INEC's Regulations and Guidelines for the 2027 elections",
     "Secret ballot; voters in the queue at the close of polls allowed to vote; priority and assistance for persons with disabilities, the elderly and pregnant women; public counting; result posted at the unit: INEC guidelines (2023 edition)"],
    """Your rights as a voter on election day:

1. A secret ballot. Nobody can watch you vote or make you show it
2. If you're in the queue when voting closes, you still vote
3. Help if you need it. Elderly voters, people with disabilities and pregnant women get priority and can bring someone to assist
4. To vote free from pressure, threats or payment
5. To watch the count, peacefully
6. To see the result posted at your polling unit

If something goes wrong, speak calmly to the presiding officer. If it isn't resolved, report it to INEC or the police.

Save this for the day.""",
    ["""Your rights on election day:

1 A secret ballot
2 In the queue at closing? You still vote
3 Priority and help if you need it
4 No pressure, threats or payment
5 Watch the count
6 See the result at your unit

#NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 12
write_script(12, "Single", "Know Your Power", """
Who you vote for is nobody's business. Your ballot is secret.
Photo: ai-07-ballot-box.""", '''
SLIDES = [
    ("statement", dict(
        lead="Not your boss's. Not your family's.\\nNot the man with the money.",
        punch="Who you vote\\nfor is *nobody's\\nbusiness.*",
        size=124,
        body="Your ballot is secret. Don't show it, don't photograph it, and nobody can make you tell.",
        photo="ai-07-ballot-box.png",
        pos="50% 15%",
    )),
]''')
write_captions(12, "Single", "Know Your Power",
    "The secret ballot: no one is entitled to know how you vote.",
    [("Voter folding a ballot behind a privacy screen", "Who you vote for is nobody's business. Your ballot is secret")],
    ["Secret ballot: Electoral Act; no phones in the voting cubicle: INEC guidelines"],
    """Who you vote for is nobody's business.

Not your boss's. Not your family's. Not the man offering money.

Your ballot is secret. Don't show it. Don't photograph it. Nobody can make you tell.

Vote with your conscience, fold it and drop it in the box.""",
    ["""Who you vote for is nobody's business.

Not your boss's. Not your family's. Not the man with the money.

Your ballot is secret. Don't show it, don't photograph it. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 11
write_script(11, "Carousel", "Know Your Power", """
Five offices. Two Saturdays. The recap.
Spine: hook -> the two dates and what is on each ballot -> same PVC, same
polling unit -> CTA. Facts: INEC timetable.""", '''
SLIDES = [
    ("cover", dict(
        title="Five offices.\\nTwo Saturdays.\\n*The recap.*",
        size=124,
        photo="ai-07-ballot-box.png",
    )),
    ("dates", dict(
        kicker="Saturday 16 January",
        title="Three\\n*ballots*",
        size=96,
        rows=[("1", "Ballot", "President", "And vice president, on one ticket"),
              ("2", "Ballot", "Senate", "Your senatorial district"),
              ("3", "Ballot", "House of Reps", "Your federal constituency")],
        photo="ai-01-polling-queue.png",
        source="INEC",
    )),
    ("dates", dict(
        kicker="Saturday 6 February",
        title="Two\\n*ballots*",
        size=96,
        rows=[("4", "Ballot", "Governor", "And deputy. In 28 states"),
              ("5", "Ballot", "State House of Assembly", "Your state constituency. All 36 states")],
        photo="ai-06-walk-to-vote.png",
        source="INEC",
    )),
    ("statement", dict(
        lead="Same PVC. Same polling unit. Both days.",
        punch="Don't stop\\nat the first\\nSaturday.",
        size=118,
        photo="ai-02-inked-thumb.png",
    )),
    ("cta", dict(
        lead="Five offices. Five choices. All yours.",
        punch="Vote both\\nSaturdays.",
        body="Save this and share it with your family group.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(11, "Carousel", "Know Your Power",
    "Recap of what's on each ballot: three on 16 Jan, two on 6 Feb.",
    [("Ballot box", "Five offices. Two Saturdays. The recap"),
     ("Queue", "16 Jan: President, Senate, House of Reps"),
     ("Walking to vote", "6 Feb: Governor (28 states), State Assembly (all 36)"),
     ("Inked thumb", "Same PVC, same unit. Don't stop at the first Saturday"),
     ("Young voters with inked thumbs", "Vote both Saturdays")],
    ["Election dates and offices: INEC revised timetable, 26 Feb 2026",
     "Governorship in 28 states (8 off-cycle), State Assembly in all 36: INEC"],
    """Five offices. Two Saturdays. The recap.

Saturday 16 January, three ballots:
1. President (with the vice president on one ticket)
2. Senate
3. House of Representatives

Saturday 6 February, two ballots:
4. Governor (in 28 states)
5. State House of Assembly (all 36 states)

Same PVC, same polling unit, both days. Don't stop at the first Saturday.""",
    ["""Five offices. Two Saturdays.

Sat 16 Jan: President, Senate, House of Reps.
Sat 6 Feb: Governor (28 states), State House of Assembly (all 36).

Same PVC, same unit, both days. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 10
write_script(10, "Single", "Know the Process", """
Countdown single: 10 days. Photo: ai-02-inked-thumb.""", '''
SLIDES = [
    ("countdown", dict(
        days=10,
        kicker="Saturday 16 January 2027",
        big=400,
        title="days. *Ready?*",
        size=120,
        body="PVC in hand. Polling unit confirmed. Route planned. Three friends coming with you.",
        photo="ai-02-inked-thumb.png",
        pos="50% 12%",
    )),
]''')
write_captions(10, "Single", "Know the Process",
    "Countdown single: 10 days, a quick readiness check.",
    [("Smiling young woman with an inked thumb", "10 days. Ready? PVC, polling unit, route, friends")],
    [],
    """10 days to Saturday 16 January 2027.

Ready?
PVC in your hand.
Polling unit confirmed.
Route planned.
Three friends coming with you.

If any of those isn't done, do it this weekend.""",
    ["""10 days to election day. Ready?

PVC in hand. Polling unit confirmed. Route planned. Three friends coming with you.

Not done? Do it this weekend. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 9
write_script(9, "Carousel", "Know the Process", """
Things that can get your vote cancelled.
Spine: hook -> what makes a ballot invalid (two slides) -> the cubicle rules
-> how to mark it right -> CTA. VERIFY against INEC's 2027 guidelines.""", '''
SLIDES = [
    ("cover", dict(
        title="Things that\\ncan get your\\nvote *cancelled.*",
        size=126,
        photo="ai-07-ballot-box.png",
    )),
    ("list", dict(
        kicker="Your ballot can be rejected if",
        title="Don't\\n*do this*",
        size=96,
        items=[("You mark more than one box", "One thumbprint, one box, per ballot"),
               ("Your ink touches two boxes", "A smudge across the line can void it"),
               ("You write or sign on it", "Any mark that identifies you")],
        photo="ai-02-inked-thumb.png",
    )),
    ("list", dict(
        kicker="And watch out for",
        title="These\\n*too*",
        size=96,
        start=4,
        items=[("An unstamped ballot", "Check it's stamped and signed before you vote"),
               ("A torn or damaged ballot", "Ask the official for help before marking"),
               ("Phones in the cubicle", "Photographing your ballot is not allowed")],
        photo="ai-22-official-explains.png",
    )),
    ("statement", dict(
        lead="How to get it right:",
        punch="One thumb.\\nOne box.\\nFold it right.",
        size=118,
        body="Press firmly inside one box, let the ink settle, and fold the way the official shows you.",
        photo="ai-23-inked-group.png",
    )),
    ("cta", dict(
        lead="Don't queue for hours and lose\\nyour vote to a smudge.",
        punch="Mark it\\nright.",
        body="Save this. Send it to a first-time voter.",
        photo="ai-01-polling-queue.png",
    )),
]''')
write_captions(9, "Carousel", "Know the Process",
    "How ballots get rejected, and how to mark yours correctly.",
    [("Ballot box", "Things that can get your vote cancelled"),
     ("Inked thumb", "More than one box, ink across two boxes, writing on it"),
     ("Official explaining the ballot", "Unstamped ballot, torn ballot, phones in the cubicle"),
     ("Young voters with inked thumbs", "One thumb. One box. Fold it right"),
     ("Queue", "Mark it right")],
    ["VERIFY before posting: grounds for rejecting a ballot paper and cubicle rules against INEC's Regulations and Guidelines for the 2027 elections",
     "Rejected ballots (more than one mark, unclear mark, identifying mark, no official stamp and signature) and the ban on phones in the cubicle: INEC guidelines (2023 edition)"],
    """Things that can get your vote cancelled:

1. Marking more than one box
2. Ink smudged across two boxes
3. Writing or signing on the ballot
4. A ballot without the official's stamp and signature. Check before you vote
5. A torn or damaged ballot. Ask the official for help
6. Phones in the cubicle. Photographing your ballot is not allowed

How to get it right: one thumb, one box, press firmly, let the ink settle, and fold the way the official shows you.

Don't queue for hours and lose your vote to a smudge.""",
    ["""Things that can get your vote cancelled:

1 Marking more than one box
2 Ink across two boxes
3 Writing on the ballot
4 No official stamp and signature

#NigeriaDecides2027""",
     """5 A torn ballot. Ask for help
6 Phones in the cubicle

One thumb. One box. Fold it the way the official shows you."""])

# ---------------------------------------------------------------- Day 8
write_script(8, "Carousel", "Know Your Power", """
Almost 40 percent of the 2023 register was 18 to 34.
Spine: hook -> 37m young registered voters in 2023 -> that's enough to swing
any race -> 2027 register over 103m -> show up and bring friends.
Facts: INEC 2023 register by age (18-34: 37.06m of 93.47m = 39.6%).""", '''
SLIDES = [
    ("cover", dict(
        title="Almost 40%\\nof the 2023\\nregister was\\n*18 to 34.*",
        size=124,
        photo="ai-23-inked-group.png",
    )),
    ("stat", dict(
        kicker="2023 voter register",
        lead="Registered voters aged 18 to 34:",
        number="37m",
        label="young Nigerians. *Out of 93.4m.*",
        photo="ai-04-friends-debate.png",
        source="INEC",
    )),
    ("statement", dict(
        lead="The 2023 presidential race was decided\\nby about 1.8 million votes.",
        punch="Young voters\\ncan decide\\nany race.",
        size=124,
        body="If they show up.",
        photo="ai-15-bus-stop-phone.png",
    )),
    ("statement", dict(
        lead="The 2027 register: over 103 million.",
        punch="The youth\\nvote is the\\nbiggest bloc.",
        size=124,
        body="It only counts on the day it turns up.",
        photo="ai-01-polling-queue.png",
        source="INEC",
    )),
    ("cta", dict(
        lead="Show up, and bring your friends.\\nThat's how a bloc becomes a result.",
        punch="Show up.\\nBring three.",
        body="Tag the friends you're going with.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(8, "Carousel", "Know Your Power",
    "Youth power: nearly 40% of the 2023 register was 18 to 34.",
    [("Young voters with inked thumbs", "Almost 40% of the 2023 register was 18 to 34"),
     ("Friends debating", "37 million registered voters aged 18 to 34, out of 93.4m"),
     ("Young man on his phone", "2023 was decided by about 1.8m votes. Young voters can decide any race"),
     ("Queue", "2027 register: over 103 million. Youth is the biggest bloc"),
     ("Young voters with inked thumbs", "Show up. Bring three")],
    ["2023 register by age: 18-34 about 37.06 million of 93.47 million (39.6%): INEC, 2023 register breakdown",
     "2023 presidential margin of about 1.8 million votes: INEC declaration",
     "2027 register of 103.4 million: INEC October 2026 update, not final"],
    """Almost 40% of the 2023 voter register was aged 18 to 34. That's about 37 million young Nigerians, out of 93.4 million.

The 2023 presidential race was decided by about 1.8 million votes.

Young voters can decide any race in this country. If they show up.

The 2027 register has over 103 million names. Show up, and bring your friends. Tag the three you're going with.""",
    ["""Almost 40% of the 2023 register was 18 to 34. That's about 37 million young Nigerians.

The 2023 race was decided by about 1.8 million votes.

Young voters can decide any race, if they show up. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 6
write_script(6, "Carousel", "Peaceful Participation", """
The peace pledge. Five promises for election week.
Spine: hook -> five promises in one list -> take the pledge.""", '''
SLIDES = [
    ("cover", dict(
        title="The peace\\npledge. *Five\\npromises for\\nelection week.*",
        size=120,
        photo="ai-24-peace-walk.png",
        pos="50% 20%",
    )),
    ("list", dict(
        kicker="I promise",
        title="My\\n*pledge*",
        size=96,
        items=[("I won't sell my vote", "Not for money, food or favours"),
               ("I won't spread unverified results", "I'll wait for INEC"),
               ("I won't join or start violence", "If trouble starts, I walk away"),
               ("I'll respect people who vote differently", "Neighbours before politics"),
               ("I'll use the law for disputes", "Not my fists, not the street")],
        photo="ai-12-handshake.png",
    )),
    ("cta", dict(
        lead="Comment \\u201cI pledge\\u201d and tag three\\npeople to take it with you.",
        punch="I pledge.",
        size=170,
        body="Peaceful participation is a choice we make together.",
        photo="ai-24-peace-walk.png",
    )),
]''')
write_captions(6, "Carousel", "Peaceful Participation",
    "A five-point peace pledge for election week, for people to take publicly.",
    [("Community peace walk", "The peace pledge. Five promises for election week"),
     ("Two young men shaking hands", "Won't sell my vote, spread fake results, or join violence; respect others; use the law"),
     ("Community peace walk", "Comment 'I pledge' and tag three people")],
    [],
    """The peace pledge. Five promises for election week:

1. I won't sell my vote
2. I won't spread unverified results. I'll wait for INEC
3. I won't join or start violence. If trouble starts, I walk away
4. I'll respect people who vote differently
5. I'll use the law for disputes, not my fists

Comment "I pledge" and tag three people to take it with you.""",
    ["""The peace pledge for election week:

1 I won't sell my vote
2 I won't spread unverified results
3 I won't join or start violence
4 I'll respect people who vote differently
5 I'll use the law for disputes

Reply \"I pledge\". #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 5
write_script(5, "Single", "Peaceful Participation", """
If trouble starts, walk away. Your life first.
No hotline numbers on the slide (VERIFY any reporting channel first).
Photo: ai-06-walk-to-vote.""", '''
SLIDES = [
    ("statement", dict(
        lead="Shouting, pushing, snatching boxes?\\nDon't film it up close. Don't join in.",
        punch="If trouble\\nstarts, *walk\\naway.*",
        size=130,
        body="Leave calmly, keep your people close, and tell the police or INEC officials when you're safe. Your life first.",
        photo="ai-06-walk-to-vote.png",
        pos="50% 15%",
    )),
]''')
write_captions(5, "Single", "Peaceful Participation",
    "Safety message for the final week: walk away from trouble, report when safe.",
    [("Elderly man and young woman walking", "If trouble starts, walk away. Report when safe. Your life first")],
    ["VERIFY before adding any reporting phone number or channel to the caption"],
    """If trouble starts at your polling unit, walk away.

Shouting, pushing, snatching ballot boxes: don't join in, and don't get close to film it.

Leave calmly. Keep your family and friends with you. When you're safe, tell the police or INEC officials what you saw.

No vote is worth your life. Your life first.""",
    ["""If trouble starts at your polling unit, walk away.

Don't join in. Don't get close to film it. Leave calmly, keep your people close, and report it when you're safe.

Your life first. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 4
write_script(4, "Carousel", "Know Your Power", """
The myths that keep people home, answered. Recap of the objections covered
during the campaign. Facts: 2023 margin (INEC); next presidential election 2031.""", '''
MYTHS = [
    ("\\u201cMy vote doesn't count.\\u201d", "2023 was decided by about 1.8 million votes. About 68 million registered voters stayed home.", "ai-03-public-count.png"),
    ("\\u201cThey're all the same.\\u201d", "Compare the plan, the record, the team and the money. They're not the same.", "ai-14-town-hall.png"),
    ("\\u201cThe courts will decide.\\u201d", "Courts settle disputes about the vote. They start from your vote.", "ai-26-results-wall.png"),
    ("\\u201cNothing ever changes.\\u201d", "Nothing changes faster when the people who want change stay home.", "ai-10-classroom.png"),
    ("\\u201cI'll vote next time.\\u201d", "The next presidential election is in 2031. That's four more years.", "ai-06-walk-to-vote.png"),
]

SLIDES = [
    ("cover", dict(
        title="The myths that\\nkeep people\\nhome. *Answered.*",
        size=122,
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
] + [
    ("statement", dict(kicker=f"Myth {i} of 5", punch=m, size=104, body=a, photo=p))
    for i, (m, a, p) in enumerate(MYTHS, 1)
] + [
    ("cta", dict(
        lead="Send this to the one friend who has\\na reason not to vote.",
        punch="No more\\nexcuses.",
        body="Saturday 16 January. Saturday 6 February.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(4, "Carousel", "Know Your Power",
    "Final-week recap of the myths that keep people home, with short answers.",
    [("Young man on his phone", "The myths that keep people home. Answered"),
     ("Public count", "\"My vote doesn't count\": 1.8m margin, 68m stayed home"),
     ("Town hall", "\"They're all the same\": compare plan, record, team, money"),
     ("Results sheet", "\"The courts will decide\": they start from your vote"),
     ("Classroom", "\"Nothing ever changes\""),
     ("Walking to vote", "\"I'll vote next time\": next presidential election is 2031"),
     ("Young voters with inked thumbs", "No more excuses")],
    ["2023 margin about 1.8 million, about 68 million registered did not vote: INEC",
     "Four-year presidential term, next election 2031: 1999 Constitution (as amended)"],
    """The myths that keep people home, answered:

"My vote doesn't count." 2023 was decided by about 1.8 million votes. About 68 million registered voters stayed home.

"They're all the same." Compare the plan, the record, the team and the money.

"The courts will decide." Courts settle disputes about the vote. They start from your vote.

"Nothing ever changes." Nothing changes faster when the people who want change stay home.

"I'll vote next time." The next presidential election is in 2031.

Send this to the one friend who has a reason not to vote.""",
    ["""The myths that keep people home, answered:

\"My vote doesn't count.\" 2023 was decided by about 1.8m votes.
\"They're all the same.\" Compare plan, record, team, money.

#NigeriaDecides2027""",
     """\"The courts will decide.\" They start from your vote.
\"Nothing changes.\" Not while the people who want change stay home.
\"I'll vote next time.\" Next time is 2031."""])

# ---------------------------------------------------------------- Day 3
write_script(3, "Single", "Know the Process", """
72 hours. Verify before you forward. Fake news peaks in the final days.
Photo: ai-15-bus-stop-phone.""", '''
SLIDES = [
    ("statement", dict(
        kicker="Three days to go",
        lead="Fake results, fake voice notes, fake\\n\\u201cbreaking news\\u201d. They peak now.",
        punch="72 hours.\\n*Verify before\\nyou forward.*",
        size=124,
        body="Who sent it? Where's it from? Is INEC saying it? If you can't tell, don't share it.",
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
]''')
write_captions(3, "Single", "Know the Process",
    "Final-days misinformation warning: three checks before forwarding.",
    [("Young man at a bus stop on his phone", "72 hours. Verify before you forward. Who sent it, where's it from, is INEC saying it?")],
    [],
    """72 hours to go.

Fake results, fake voice notes, fake "breaking news". They peak in these last days.

Before you forward anything, ask:
Who sent it?
Where did it come from?
Is INEC saying it?

If you can't tell, don't share it.""",
    ["""72 hours to go. Fake news peaks now.

Before you forward: who sent it? Where's it from? Is INEC saying it?

If you can't tell, don't share it. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 2
write_script(2, "Single", "Know the Process", """
Campaigns end today (14 Jan): campaigning stops 24 hours before election
day. No candidate content from here. Photo: ai-01-polling-queue.""", '''
SLIDES = [
    ("statement", dict(
        kicker="Thursday 14 January",
        lead="By law, campaigning stops 24 hours\\nbefore election day.",
        punch="Campaigns\\nend today.",
        size=140,
        body="The jingles stop. The choice is yours now. PVC ready, polling unit confirmed, Saturday planned.",
        photo="ai-01-polling-queue.png",
        pos="50% 18%",
    )),
]''')
write_captions(2, "Single", "Know the Process",
    "Campaigns end 24 hours before the vote. No candidate content from here.",
    [("Queue outside a polling unit", "Campaigns end today. The choice is yours now")],
    ["Campaigns end 24 hours before polling day: Electoral Act; INEC timetable for the 16 Jan 2027 elections"],
    """Campaigns end today.

By law, campaigning stops 24 hours before election day. The jingles stop. The rallies stop. The choice is yours now.

Tonight: PVC ready, polling unit confirmed, Saturday planned.""",
    ["""Campaigns end today. By law, campaigning stops 24 hours before election day.

The choice is yours now. PVC ready, polling unit confirmed, Saturday planned. #NigeriaDecides2027"""])
print("batch4 written")
