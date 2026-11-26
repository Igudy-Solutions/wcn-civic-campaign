import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import write_script, write_captions

# ---------------------------------------------------------------- Day 26
write_script(26, "Carousel", "Know Your Power", """
The election nobody talks about: your State House of Assembly.
Spine: hook -> every state elects one, on 6 Feb -> 24 to 40 members per
state -> what they do (incl. checking the governor) -> can you name yours.
Facts: 1999 Constitution (as amended), ss.90-93, 188; INEC timetable.""", '''
SLIDES = [
    ("cover", dict(
        title="The election\\nnobody talks\\nabout: *your State\\nHouse of Assembly.*",
        size=108,
        photo="ai-14-town-hall.png",
    )),
    ("statement", dict(
        lead="Saturday 6 February, the same day as governor.\\nIn all 36 states.",
        punch="Your state's\\nlawmakers.",
        size=124,
        body="Each state has between 24 and 40 members, one for each state constituency.",
        photo="ai-01-polling-queue.png",
        source="1999 Constitution",
    )),
    ("list", dict(
        kicker="What they do",
        title="The job\\n*nobody explains*",
        size=96,
        items=[("Make your state's laws", "From land and markets to local rules"),
               ("Approve the state budget", "The governor can't spend without it"),
               ("Check the governor", "Committees question ministries and contracts"),
               ("Can remove a governor", "Impeachment starts in the Assembly"),
               ("Represent your area", "Your member is a short drive away")],
        photo="ai-11-market-trader.png",
    )),
    ("statement", dict(
        lead="Most people vote for governor\\nand skip the Assembly box.",
        punch="Don't skip it.",
        size=132,
        body="A governor with no one checking them is a governor with no limits.",
        photo="ai-07-ballot-box.png",
    )),
    ("cta", dict(
        lead="Find out who represents your state\\nconstituency, and who wants to.",
        punch="6 Feb.\\nTwo ballots.",
        body="Governor and State Assembly. Same PVC, same polling unit.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(26, "Carousel", "Know Your Power",
    "Who does what: the State House of Assembly, elected on 6 Feb in all 36 states, and why it matters.",
    [("Town hall", "The election nobody talks about: your State House of Assembly"),
     ("Queue outside a polling unit", "6 Feb, all 36 states. 24 to 40 members per state"),
     ("Market woman", "State laws, the state budget, checking the governor, impeachment, your area"),
     ("Ballot box", "Don't skip the Assembly box"),
     ("Young voters with inked thumbs", "6 Feb. Two ballots")],
    ["State Houses of Assembly, size and functions, including the budget and removal of a governor: 1999 Constitution (as amended), ss.90-93, 120-121, 188",
     "State Assembly elections Sat 6 Feb 2027 in all 36 states: INEC revised timetable, 26 Feb 2026"],
    """The election nobody talks about: your State House of Assembly.

On Saturday 6 February every state elects its Assembly, the same day as the governorship vote. Each state has between 24 and 40 members.

What they do:
1. Make your state's laws
2. Approve the state budget
3. Check the governor
4. Can start the removal of a governor
5. Represent your area

Most people vote for governor and skip the Assembly box. Don't. 6 February: two ballots, same PVC, same polling unit.""",
    ["""The election nobody talks about: your State House of Assembly.

6 Feb, all 36 states. They make state laws, approve the state budget and check the governor.

Don't skip the Assembly box. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 25
write_script(25, "Single", "Peaceful Participation", """
This Christmas, talk politics without the fight. Holiday family conversations.
Photo: ai-13-family-table.""", '''
SLIDES = [
    ("statement", dict(
        lead="The whole family is home.\\nSomeone will bring up the election.",
        punch="Talk politics.\\n*Skip the fight.*",
        size=126,
        body="Ask, listen, keep it about issues, and know when to pass the rice. Family first, every year.",
        photo="ai-13-family-table.png",
        pos="50% 18%",
    )),
]''')
write_captions(25, "Single", "Peaceful Participation",
    "Holiday conversations: talk about the election with family without falling out.",
    [("Family around the dinner table", "Talk politics, skip the fight. Ask, listen, issues not insults, know when to stop")],
    [],
    """The whole family is home this Christmas. Someone will bring up the election.

Talk about it. Just skip the fight:
Ask before you argue.
Listen to the answer.
Keep it about issues, not tribe or religion.
Know when to change the subject and pass the rice.

Elections come every four years. Family is every year.""",
    ["""The whole family is home this Christmas. Someone will bring up the election.

Talk politics. Skip the fight. Ask, listen, keep it about issues, and know when to pass the rice.

Family first. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 23
write_script(23, "Carousel", "Know the Process", """
Travelling for Christmas? You can only vote where you registered.
Spine: hook -> the rule -> transfer window has closed -> plan your return ->
CTA. VERIFY: confirm with INEC that registration transfer is closed for the
2027 general election before posting.""", '''
SLIDES = [
    ("cover", dict(
        title="Travelling for\\nChristmas?\\n*Plan your\\nreturn to vote.*",
        size=120,
        photo="ai-18-bus-park.png",
        pos="50% 25%",
    )),
    ("statement", dict(
        lead="This is the rule most people find out too late.",
        punch="You can only\\nvote where you\\nregistered.",
        size=118,
        body="Your polling unit is printed on your PVC. That's the only place your vote can be cast.",
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
    ("statement", dict(
        lead="Moving your registration to another\\nstate or polling unit?",
        punch="The transfer\\nwindow has\\nclosed.",
        size=118,
        body="For 16 January and 6 February, you vote at the unit on your card.",
        photo="ai-22-official-explains.png",
        source="INEC",
    )),
    ("list", dict(
        kicker="If you're travelling",
        title="Plan your\\n*return*",
        size=96,
        items=[("Book your trip back early", "Roads and parks get busy in January"),
               ("Be home before the 16th", "Aim for the week before, not the night before"),
               ("Keep your PVC with you", "Or safe in the place you'll vote"),
               ("Plan for 6 February too", "Governor and State Assembly, same unit"),
               ("Expect limited movement", "Vehicle movement is usually restricted on election day")],
        photo="ai-19-airport.png",
    )),
    ("cta", dict(
        lead="Enjoy Christmas. Then come home and vote.",
        punch="Home by\\nthe 16th.",
        body="Send this to the friend travelling for the holidays.",
        photo="ai-18-bus-park.png",
    )),
]''')
write_captions(23, "Carousel", "Know the Process",
    "Christmas travel: you can only vote at the polling unit where you registered, so plan your return.",
    [("Travellers boarding a bus at a motor park", "Travelling for Christmas? Plan your return to vote"),
     ("Young woman holding her voter card", "You can only vote where you registered"),
     ("Official at a polling unit", "The transfer window has closed"),
     ("Young woman at the airport", "Plan your return: book early, home before the 16th, PVC, 6 Feb, movement limits"),
     ("Motor park", "Home by the 16th")],
    ["You can only vote at the polling unit where you registered: INEC",
     "VERIFY before posting: transfer of registration closed for the 2027 general election (plan notes 26 Jul 2026); confirm with INEC",
     "Vehicle movement restriction on election day: usual practice, confirm the 2027 order closer to the date"],
    """Travelling for Christmas? Plan your return to vote.

You can only vote at the polling unit where you registered. It's printed on your PVC. The window to transfer your registration has closed, so for 16 January and 6 February you vote at the unit on your card.

If you're travelling:
1. Book your trip back early
2. Be home before the 16th
3. Keep your PVC safe and with you
4. Plan for 6 February too
5. Expect movement to be restricted on election day

Enjoy Christmas. Then come home and vote.""",
    ["""Travelling for Christmas?

You can only vote at the polling unit where you registered, and the transfer window has closed.

Book your trip back early. Be home before 16 Jan. Plan for 6 Feb too. #NigeriaDecides2027""",
     """Keep your PVC safe and with you, and expect vehicle movement to be restricted on election day.

Enjoy Christmas. Then come home and vote."""])

# ---------------------------------------------------------------- Day 22
write_script(22, "Single", "Peaceful Participation", """
Merry Christmas. Peace at home, peace at the polls. 25 Dec.
Photo: ai-24-peace-walk (pastor and imam walking together with neighbours).""", '''
SLIDES = [
    ("statement", dict(
        kicker="25 December",
        lead="From all of us at World Changers Network:",
        punch="Merry\\nChristmas.",
        size=150,
        body="Peace at home. Peace at the polls. We go into January as neighbours, whoever we vote for.",
        photo="ai-24-peace-walk.png",
        pos="50% 15%",
    )),
]''')
write_captions(22, "Single", "Peaceful Participation",
    "Christmas greeting with the campaign's peace message.",
    [("Community peace walk, pastor and imam together", "Merry Christmas. Peace at home, peace at the polls")],
    [],
    """Merry Christmas from all of us at World Changers Network.

Peace at home. Peace at the polls.

Whatever your plans today, and whoever you'll vote for next month, we go into January as neighbours.""",
    ["""Merry Christmas from World Changers Network.

Peace at home. Peace at the polls. We go into January as neighbours, whoever we vote for. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 21
write_script(21, "Carousel", "Vote Wisely", """
Vote buying: what it costs you and what the law says.
Spine: hook -> the maths (N5,000 over 1,461 days) -> the law: buying and
selling votes are offences -> what it looks like -> what to do -> CTA.
VERIFY: confirm the vote-buying provisions in the Electoral Act in force for
2027 before posting. No penalty figures on the slides.""", '''
SLIDES = [
    ("cover", dict(
        title="Vote buying.\\n*What it costs you.\\nWhat the law says.*",
        size=118,
        photo="ai-11-market-trader.png",
    )),
    ("stat", dict(
        kicker="Do the maths",
        lead="N5,000 for your vote, spread over\\na four-year term of 1,461 days:",
        number="N3",
        size=320,
        label="a day. *For four years.*",
        photo="ai-15-bus-stop-phone.png",
    )),
    ("statement", dict(
        lead="It isn't just wrong. It's illegal.",
        punch="Buying a vote\\nis a crime.\\n*So is selling one.*",
        size=112,
        body="Under the Electoral Act, the person who offers and the person who takes both commit an offence.",
        photo="ai-22-official-explains.png",
        source="Electoral Act",
    )),
    ("list", dict(
        kicker="What it looks like",
        title="Know it when\\n*you see it*",
        size=96,
        items=[("Cash near the polling unit", "Or a transfer \\u201cafter you vote\\u201d"),
               ("Food, rice, recharge cards", "Handed out in exchange for your vote"),
               ("\\u201cShow me your ballot\\u201d", "Anyone asking for proof of who you voted for"),
               ("\\u201cSnap your ballot\\u201d", "Phones aren't allowed in the voting cubicle")],
        photo="ai-07-ballot-box.png",
    )),
    ("statement", dict(
        lead="If someone offers you money:",
        punch="Say no.\\nKeep it secret.\\nReport it.",
        size=118,
        body="Tell the presiding officer or the police at the polling unit. Your ballot stays secret either way.",
        photo="ai-27-wheelchair-voter.png",
    )),
    ("cta", dict(
        lead="Four years of roads, hospitals and\\nschools are not worth N3 a day.",
        punch="Don't sell it.\\nShow up.",
        body="Send this to someone who thinks it's harmless.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(21, "Carousel", "Vote Wisely",
    "Vote buying: the maths, the law (buying and selling are both offences), what it looks like and what to do.",
    [("Market woman counting notes", "Vote buying: what it costs you, what the law says"),
     ("Young man on his phone", "N5,000 over 1,461 days is about N3 a day"),
     ("Polling official", "Buying a vote is a crime. So is selling one"),
     ("Ballot box", "What it looks like: cash, food, 'show me your ballot', 'snap your ballot'"),
     ("Voter being assisted", "Say no. Keep it secret. Report it"),
     ("Young voters with inked thumbs", "Don't sell it. Show up")],
    ["N5,000 / 1,461 days = N3.42 a day: arithmetic, four-year term including one leap day",
     "VERIFY before posting: vote buying and vote selling as offences under the Electoral Act in force for 2027 (Electoral Act 2022, s.121, if unchanged)",
     "Phones and cameras not allowed in the voting cubicle: INEC regulations and guidelines (confirm the 2027 version)"],
    """Vote buying: what it costs you and what the law says.

N5,000 for your vote, over a four-year term of 1,461 days, is about N3 a day.

It isn't just a bad deal. It's illegal. Under the Electoral Act, the person who offers money for a vote and the person who takes it both commit an offence.

What it looks like: cash near the polling unit, food or recharge cards for your vote, anyone asking to see or photograph your ballot.

If someone offers you money: say no, keep your ballot secret, and tell the presiding officer or the police.

Four years of roads, hospitals and schools are not worth N3 a day.""",
    ["""Vote buying: N5,000 over a four-year term is about N3 a day.

And under the Electoral Act, buying a vote is an offence. So is selling one.

Say no. Keep your ballot secret. Report it at the polling unit. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 20
write_script(20, "Carousel", "Know the Process", """
"The courts will decide anyway?" Not quite.
Spine: hook -> courts don't vote, voters do -> tribunals work from the votes
and the records of the count -> a big, watched vote is harder to dispute ->
CTA. General description of the petition process; no case named.""", '''
SLIDES = [
    ("cover", dict(
        title="\\u201cThe courts will\\ndecide anyway.\\u201d\\n*Not quite.*",
        size=120,
        photo="ai-14-town-hall.png",
    )),
    ("statement", dict(
        lead="Judges don't vote.",
        punch="Courts don't\\npick winners.\\n*Voters do.*",
        size=120,
        photo="ai-02-inked-thumb.png",
    )),
    ("statement", dict(
        lead="If a result is challenged, an election\\ntribunal looks at how it was run.",
        punch="It starts\\nfrom your\\nvote.",
        size=128,
        body="Tribunals examine the votes cast and the records of the count, like result sheets from polling units.",
        photo="ai-26-results-wall.png",
    )),
    ("statement", dict(
        lead="Every voter who shows up, and every\\nperson who watches the count, adds proof.",
        punch="A big, watched\\nvote is hard\\nto argue with.",
        size=112,
        photo="ai-03-public-count.png",
    )),
    ("cta", dict(
        lead="Courts settle disputes about the vote.\\nThey can't replace it.",
        punch="Vote.\\nThen watch\\nthe count.",
        body="Send this to the friend who says it's all decided in court.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(20, "Carousel", "Know the Process",
    "Answers \"the courts will decide anyway\": tribunals settle disputes about the vote, starting from the votes and records of the count.",
    [("Town hall", "\"The courts will decide anyway.\" Not quite"),
     ("Inked thumb", "Courts don't pick winners. Voters do"),
     ("Residents photographing a results sheet", "A tribunal starts from your vote and the records of the count"),
     ("Public count", "A big, watched vote is hard to argue with"),
     ("Young voters with inked thumbs", "Vote. Then watch the count")],
    ["Election petitions are heard by election tribunals and decided on the votes cast and records of the count: Electoral Act and 1999 Constitution (as amended), s.285. General description, no case named"],
    """"The courts will decide anyway."

Not quite. Judges don't vote. Courts don't pick winners. Voters do.

If a result is challenged, an election tribunal looks at how the election was run, and it starts from the votes cast and the records of the count: the result sheets from polling units like yours.

Every voter who shows up, and every person who stays to watch the count, adds proof. A big, watched vote is hard to argue with.

Courts settle disputes about the vote. They can't replace it.""",
    ["""\"The courts will decide anyway.\" Not quite.

Courts don't pick winners. Voters do. A tribunal starts from the votes cast and the records of the count.

A big, watched vote is hard to argue with. Vote, then watch the count. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 19
write_script(19, "Single", "Know the Process", """
Countdown single: 19 days. Tag one person who has not collected their PVC.
Photo: ai-08-pvc-collection.""", '''
SLIDES = [
    ("countdown", dict(
        days=19,
        kicker="Saturday 16 January 2027",
        big=340,
        title="days. *Tag one person\\nwithout a PVC.*",
        size=100,
        body="You know who they are. No PVC, no vote. INEC office in their LGA, in person.",
        photo="ai-08-pvc-collection.png",
        pos="50% 15%",
    )),
]''')
write_captions(19, "Single", "Know the Process",
    "Countdown single that turns followers into messengers: tag someone who hasn't collected their PVC.",
    [("Young people collecting PVCs at an INEC office", "19 days. Tag one person without a PVC")],
    ["PVC collected in person at the INEC office in your local government area: INEC"],
    """19 days to Saturday 16 January 2027.

Tag one person who still hasn't collected their PVC. You know who they are.

No PVC, no vote. They need to go to the INEC office in their local government area, in person. Nobody can collect it for them.""",
    ["""19 days to election day.

Tag one person who still hasn't collected their PVC. You know who they are.

No PVC, no vote. INEC office in their LGA, in person. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 18
write_script(18, "Carousel", "Know the Process", """
What happens at your polling unit, step by step.
Spine: hook -> six steps, one per slide (queue, accreditation, ballot, mark
in secret, fold and drop, the public count) -> CTA.
VERIFY each step against INEC's 2027 Regulations and Guidelines and the
election manual before posting.""", '''
STEPS = [
    ("Join the queue.", "Bring your PVC. Arrive early. Voting is in the open, at your own unit.", "ai-01-polling-queue.png"),
    ("Get accredited.", "An official checks your PVC on the BVAS device, which confirms you by fingerprint or face.", "ai-05-bvas-accreditation.png"),
    ("Collect your ballot.", "Make sure each ballot paper is stamped and signed by the official.", "ai-22-official-explains.png"),
    ("Mark it in secret.", "In the cubicle, ink your thumb and press it once, inside one box. No phones in the cubicle.", "ai-07-ballot-box.png"),
    ("Fold and drop it.", "Fold the way the official shows you and drop it in the right box, in full view.", "ai-02-inked-thumb.png"),
    ("Watch the count.", "Votes are counted in public. Results are written on the EC8A sheet, posted and uploaded to IReV.", "ai-03-public-count.png"),
]

SLIDES = [
    ("cover", dict(
        title="What happens\\nat your polling\\nunit. *Step\\nby step.*",
        size=118,
        photo="ai-22-official-explains.png",
    )),
] + [
    ("statement", dict(kicker=f"Step {i} of 6", punch=h, size=124, body=b, photo=p))
    for i, (h, b, p) in enumerate(STEPS, 1)
] + [
    ("cta", dict(
        lead="Six steps. Most people are done\\nin well under an hour.",
        punch="Save it.\\nShow up.",
        body="Send this to a first-time voter.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(18, "Carousel", "Know the Process",
    "Six steps at the polling unit, from the queue to the public count. For first-time voters.",
    [("Official explaining the ballot", "What happens at your polling unit, step by step"),
     ("Queue", "1 Join the queue with your PVC"),
     ("Accreditation on a BVAS device", "2 Get accredited: PVC plus fingerprint or face"),
     ("Official explaining the ballot", "3 Collect your ballot, stamped and signed"),
     ("Ballot box", "4 Mark it in secret, one box. No phones in the cubicle"),
     ("Inked thumb", "5 Fold and drop it in full view"),
     ("Public count", "6 Watch the count. EC8A posted, uploaded to IReV"),
     ("Young voters with inked thumbs", "Save it. Show up")],
    ["VERIFY before posting: each step against INEC's Regulations and Guidelines for the Conduct of Elections and the election manual for 2027",
     "Accreditation with BVAS by fingerprint or facial recognition; results on Form EC8A, posted at the unit and uploaded to IReV: INEC (2023 procedure)",
     "\"Well under an hour\": general expectation, varies by unit; remove if the team prefers"],
    """What happens at your polling unit, step by step:

1. Join the queue at your own polling unit, with your PVC
2. Get accredited: the BVAS device confirms you by fingerprint or face
3. Collect your ballot papers, stamped and signed by the official
4. Mark them in secret, one box each. No phones in the cubicle
5. Fold and drop them in the right box, in full view
6. Stay and watch the public count. Results go on the EC8A sheet, are posted at the unit and uploaded to IReV

Save this. Send it to a first-time voter.""",
    ["""What happens at your polling unit, step by step:

1 Join the queue with your PVC
2 Get accredited on the BVAS
3 Collect your ballot, stamped and signed
4 Mark it in secret

#NigeriaDecides2027""",
     """5 Fold and drop it in full view
6 Watch the public count. Results go on the EC8A, posted at the unit and uploaded to IReV

Send this to a first-time voter."""])

# ---------------------------------------------------------------- Day 17
write_script(17, "Carousel", "Know the Process", """
BVAS, IReV, EC8A. Election words in plain English.
Spine: hook -> one word per slide -> two more you'll hear (PVC, PU) -> CTA.
VERIFY definitions with INEC before posting.""", '''
WORDS = [
    ("BVAS", "Bimodal Voter Accreditation System", "The handheld device that checks you're the real owner of your PVC, by fingerprint or face. It also photographs the result sheet.", "ai-05-bvas-accreditation.png"),
    ("EC8A", "The polling unit result sheet", "After the public count, results are written on it, signed, and a copy is posted at the unit.", "ai-26-results-wall.png"),
    ("IReV", "INEC Result Viewing portal", "The website where photos of polling unit result sheets are published, so anyone can check them.", "ai-15-bus-stop-phone.png"),
]

SLIDES = [
    ("cover", dict(
        title="BVAS. IReV.\\nEC8A. *Election\\nwords in plain\\nEnglish.*",
        size=118,
        photo="ai-05-bvas-accreditation.png",
    )),
] + [
    ("statement", dict(kicker=k, lead=None, punch=w, size=200, body=d, photo=p))
    for w, k, d, p in WORDS
] + [
    ("list", dict(
        kicker="Two more you'll hear",
        title="And these\\n*two*",
        size=96,
        items=[("PVC", "Permanent Voter's Card. No PVC, no vote", "1"),
               ("PU", "Polling unit. Yours is printed on your PVC", "2")],
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
    ("cta", dict(
        lead="Now when someone says \\u201ccheck IReV\\u201d,\\nyou'll know what they mean.",
        punch="Know the\\nwords.",
        body="Save this and share it with someone voting for the first time.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(17, "Carousel", "Know the Process",
    "Plain-English glossary: BVAS, EC8A, IReV, plus PVC and PU.",
    [("Accreditation on a BVAS device", "BVAS. IReV. EC8A. Election words in plain English"),
     ("Accreditation on a BVAS device", "BVAS: checks you by fingerprint or face, photographs the result sheet"),
     ("Residents photographing a results sheet", "EC8A: the polling unit result sheet"),
     ("Young man on his phone", "IReV: where photos of result sheets are published"),
     ("Young woman holding her voter card", "PVC and PU"),
     ("Young voters with inked thumbs", "Know the words")],
    ["VERIFY before posting: definitions of BVAS, IReV and Form EC8A against INEC's 2027 guidelines",
     "BVAS = Bimodal Voter Accreditation System; IReV = INEC Result Viewing portal; EC8A = polling unit result sheet: INEC"],
    """Election words in plain English:

BVAS: Bimodal Voter Accreditation System. The handheld device that checks you're the real owner of your PVC, by fingerprint or face. It also photographs the result sheet.

EC8A: the polling unit result sheet. Results are written on it after the public count, and a copy is posted at the unit.

IReV: the INEC Result Viewing portal. Photos of polling unit result sheets are published there so anyone can check.

PVC: Permanent Voter's Card. No PVC, no vote.
PU: polling unit. Yours is on your PVC.

Save this for election day.""",
    ["""Election words in plain English:

BVAS: the device that checks you by fingerprint or face
EC8A: the polling unit result sheet
IReV: INEC's portal where photos of result sheets are published

#NigeriaDecides2027""",
     """And two more: PVC, your Permanent Voter's Card (no PVC, no vote), and PU, your polling unit, printed on your PVC."""])
print("batch3 written")
