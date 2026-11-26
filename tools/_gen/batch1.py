import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import write_script, write_captions

CAND_IMPORT = "from preview_candidate import candidate_slide  # noqa: E402\n"


def candidates(day, part, tickets, first, nxt, cover_photo, intro_photo, cta_photo):
    names = ", ".join(tickets)
    last = part == 6
    cta_lead = ("That's all 18 presidential candidates.\\nTicket 1 has no candidate listed, by court order."
                if last else f"Next in the series: {nxt}.")
    src = f'''TICKETS = {tickets!r}

SLIDES = [
    ("cover", dict(
        title="Meet the\\ncandidates.\\n*Part {part} of 6.*",
        size=132,
        photo="{cover_photo}",
    )),
    ("statement", dict(
        lead="All 18 presidential candidates,\\nin INEC's ballot order. Tickets {first}.",
        punch="Same layout.\\nSame facts.\\nNo favourites.",
        size=104,
        body="Age, running mate and qualifications as INEC lists them. We don't rank, endorse or comment.",
        photo="{intro_photo}",
        source="INEC final list",
    )),
] + [candidate_slide(t) for t in TICKETS] + [
    ("cta", dict(
        lead="{cta_lead}",
        punch="{"Now you know\\nevery name." if last else "Know every\\nname."}",
        body="Information, not endorsement. Your vote, your choice.",
        photo="{cta_photo}",
    )),
]'''
    doc = f"""Meet the candidates, part {part} of 6: tickets {first} ({names}).
Same layout for everyone, INEC facts only (age, running mate, qualifications
as printed), party colours from tools/parties.py, INEC ballot order.

Photos: real photos only, never AI. Save a cut-out PNG as
images/candidates/<party>-president.png and re-run; until then a party
monogram stands in."""
    write_script(day, "Carousel", "Know the Candidates", doc, src, CAND_IMPORT)
    return names


# ---------------------------------------------------------------- Day 46
write_script(46, "Single", "Know Your Power", """
Poll single: what matters most in a leader? Four options, people vote in the
comments (and on the Story poll). Non-partisan: qualities, not people.
Photo: ai-04-friends-debate.""", '''
SLIDES = [
    ("list", dict(
        kicker="Quick poll",
        title="What matters\\nmost in a *leader?*",
        size=104,
        items=[("Integrity", "Honest, keeps their word", "1"),
               ("Competence", "Can actually do the job", "2"),
               ("A clear plan", "Says how, with what, by when", "3"),
               ("Accountability", "Answers to the people", "4")],
        body="Pick one. Drop the number in the comments.",
        photo="ai-04-friends-debate.png",
        pos="50% 12%",
    )),
]''')
write_captions(46, "Single", "Know Your Power",
    "Poll: which quality matters most in a leader. Gets people thinking about what they are choosing, not who.",
    [("Young friends debating on a roadside bench", "Poll: 1 Integrity, 2 Competence, 3 A clear plan, 4 Accountability. Answer in the comments")],
    [],
    """Quick poll. What matters most to you in a leader?

1. Integrity: honest, keeps their word
2. Competence: can actually do the job
3. A clear plan: says how, with what money, by when
4. Accountability: answers to the people

Drop your number in the comments, and vote in our Story poll too. Then ask yourself which candidates on your ballot show the quality you picked.""",
    ["""Quick poll: what matters most in a leader?

1 Integrity
2 Competence
3 A clear plan
4 Accountability

Reply with your number. Then check which candidates on your ballot actually show it. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 45
n = candidates(45, 2, ["ADP", "APC", "APM"], "5 to 7", "tickets 8 to 10", "ai-23-inked-group.png", "ai-07-ballot-box.png", "ai-05-bvas-accreditation.png")
write_captions(45, "Carousel", "Know the Candidates",
    "Meet the candidates, part 2 of 6. Tickets 5 to 7 on INEC's ballot: ADP, APC, APM.",
    [("Young voters showing inked thumbs", "Meet the candidates. Part 2 of 6"),
     ("Woman casting her ballot", "Same layout, same facts, no favourites"),
     ("Photo or monogram (real photo only)", "Ticket 5, ADP: Aliyu Abbas-Bin, 44. Running mate Chinazam Ike"),
     ("Photo or monogram (real photo only)", "Ticket 6, APC: Bola Ahmed Tinubu, 74. Running mate Kashim Shettima"),
     ("Photo or monogram (real photo only)", "Ticket 7, APM: Oluseyi Abiodun Makinde, 58. Running mate Musa Lawal Daura"),
     ("Accreditation at a polling unit", "Next: tickets 8 to 10. Information, not endorsement")],
    ["Names, ages, running mates, qualifications and ballot order: INEC Final List of Candidates (Presidential), Jan 2027 elections, PDF of 30 Oct 2026",
     "Candidate photos: still to add, real photos only (images/candidates/adp-president.png, apc-president.png, apm-president.png)"],
    """Meet the candidates, part 2 of 6.

Tickets 5 to 7 on the presidential ballot, in INEC's order:

5. ADP: Aliyu Abbas-Bin, 44. Running mate: Chinazam Ike
6. APC: Bola Ahmed Tinubu, 74. Running mate: Kashim Shettima
7. APM: Oluseyi Abiodun Makinde, 58. Running mate: Musa Lawal Daura

Same layout and the same facts for every candidate, straight from INEC's final list. We don't rank, endorse or comment. Next: tickets 8 to 10.""",
    ["""Meet the candidates, part 2 of 6. Tickets 5 to 7, in INEC's ballot order:

5 ADP: Aliyu Abbas-Bin, 44
6 APC: Bola Ahmed Tinubu, 74
7 APM: Oluseyi Abiodun Makinde, 58

Facts from INEC's final list. Information, not endorsement. #NigeriaDecides2027""",
     """Running mates: Chinazam Ike (ADP), Kashim Shettima (APC), Musa Lawal Daura (APM).

Next in the series: tickets 8 to 10."""])

# ---------------------------------------------------------------- Day 44
write_script(44, "Carousel", "Know Your Power", """
My vote does not count? The numbers say otherwise.
Spine: hook -> the 2023 margin (about 1.8m) -> the people who stayed home
(about 68m) -> stayed-home voters outnumber the margin more than 37 times ->
smaller races are closer still -> show up.
Facts: 2023 presidential result (INEC), margin 1st to 2nd about 1.8m;
93.4m registered, about 25m voted.""", '''
SLIDES = [
    ("cover", dict(
        title="\\u201cMy vote\\ndoesn't count.\\u201d\\n*The numbers\\nsay otherwise.*",
        size=116,
        photo="ai-15-bus-stop-phone.png",
        pos="50% 15%",
    )),
    ("stat", dict(
        kicker="2023 presidential election",
        lead="The winner's lead over second place:",
        number="1.8m",
        label="votes. *That's all it took.*",
        photo="ai-03-public-count.png",
        source="INEC",
    )),
    ("stat", dict(
        kicker="Same election",
        lead="Registered voters who stayed home:",
        number="68m",
        label="people. *Silent.*",
        photo="ai-06-walk-to-vote.png",
        source="INEC",
    )),
    ("statement", dict(
        lead="The people who stayed home outnumbered\\nthe winning margin more than 37 times over.",
        punch="Every vote\\nwas the\\ndifference.",
        size=124,
        photo="ai-01-polling-queue.png",
    )),
    ("statement", dict(
        lead="And smaller races are closer still.",
        punch="Senate, Reps and\\nState Assembly seats\\nare often won by\\n*a few thousand votes.*",
        size=88,
        photo="ai-26-results-wall.png",
    )),
    ("cta", dict(
        lead="Your vote counts when it's counted.\\nIt's only counted if you show up.",
        punch="Show up.\\n16 Jan. 6 Feb.",
        body="Send this to the friend who always says it doesn't matter.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(44, "Carousel", "Know Your Power",
    "Answers the most common objection with the 2023 numbers: a 1.8m margin against 68m people who stayed home.",
    [("Young man at a bus stop on his phone", "\"My vote doesn't count.\" The numbers say otherwise"),
     ("Public count at a polling unit", "2023: the winner's lead was about 1.8 million votes"),
     ("Elderly man and young woman walking to vote", "About 68 million registered voters stayed home"),
     ("Queue outside a polling unit", "Stayed-home voters outnumbered the margin 37 times over"),
     ("Residents photographing a results sheet", "Smaller races are often won by a few thousand votes"),
     ("Young voters showing inked thumbs", "Your vote is only counted if you show up. 16 Jan, 6 Feb")],
    ["2023 presidential result, margin between first and second of about 1.8 million votes: INEC declaration, 1 Mar 2023",
     "93.4 million registered, about 25 million votes cast (turnout 26.7%), so about 68 million did not vote: INEC",
     "Close legislative races: general statement, no specific seat named"],
    """"My vote doesn't count."

In 2023 the presidential race was decided by about 1.8 million votes.
About 68 million registered voters stayed home.

The people who stayed home outnumbered the winning margin more than 37 times over. Senate, House of Reps and State Assembly seats are often won by a few thousand votes.

Your vote only counts if it's counted. It's only counted if you show up.

Saturday 16 January and Saturday 6 February. Send this to the friend who always says it doesn't matter.""",
    ["""\"My vote doesn't count.\"

2023: the presidential race was decided by about 1.8 million votes. About 68 million registered voters stayed home.

That's the margin 37 times over. #NigeriaDecides2027""",
     """Smaller races are closer still: Senate, Reps and State Assembly seats are often won by a few thousand votes.

Your vote counts when it's counted. Show up on 16 Jan and 6 Feb."""])

# ---------------------------------------------------------------- Day 42
write_script(42, "Carousel", "Demand Accountability", """
Who checks the people in charge? You do.
Spine: hook -> elections are the big check, not the only one -> five ways
to hold leaders to account between elections -> then use your vote.
Non-partisan: applies to every office holder.""", '''
SLIDES = [
    ("cover", dict(
        title="Who checks\\nthe people\\nin charge?\\n*You do.*",
        size=128,
        photo="ai-14-town-hall.png",
        pos="50% 18%",
    )),
    ("statement", dict(
        lead="Voting is the biggest check you have.",
        punch="It's not\\nthe only one.",
        size=124,
        body="Leaders answer to the people who watch them. Here's how to watch.",
        photo="ai-04-friends-debate.png",
    )),
    ("list", dict(
        kicker="Between elections",
        title="Five ways to\\n*hold them to account*",
        size=88,
        items=[("Know who represents you", "Your Senator, Rep, State Assembly member and LG chair"),
               ("Show up to town halls", "Constituency meetings are open. Ask your question"),
               ("Follow the money", "Budgets are public documents. Ask what was spent where"),
               ("Track the promises", "Roads, schools, clinics in your area. Done or not?"),
               ("Speak up, peacefully", "Letters, petitions, community groups, the media")],
        photo="ai-26-results-wall.png",
    )),
    ("statement", dict(
        lead="Then, on election day,\\nbring what you saw.",
        punch="Your vote is\\nyour verdict.",
        size=124,
        photo="ai-02-inked-thumb.png",
    )),
    ("cta", dict(
        lead="Save this. Pick one thing to do\\nthis month.",
        punch="Watch them.\\nThen vote.",
        body="Non-partisan. It applies to whoever wins.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(42, "Carousel", "Demand Accountability",
    "Accountability is a habit, not one day. Five practical ways to watch the people in charge, whoever they are.",
    [("Town hall, young woman asking a question", "Who checks the people in charge? You do"),
     ("Friends talking on a roadside bench", "Voting is the biggest check, not the only one"),
     ("Residents photographing a posted results sheet", "Five ways: know your reps, town halls, follow the money, track promises, speak up"),
     ("Inked thumb", "Your vote is your verdict"),
     ("Young voters with inked thumbs", "Watch them. Then vote")],
    ["No figures on this post"],
    """Who checks the people in charge? You do.

Voting is the biggest check you have. It isn't the only one. Between elections:

1. Know who represents you: Senator, Rep, State Assembly member, LG chair
2. Show up to town halls and constituency meetings
3. Follow the money. Budgets are public documents
4. Track the promises made for your area
5. Speak up, peacefully: letters, petitions, community groups, the media

Then on election day, bring what you saw. Your vote is your verdict.

Pick one thing to do this month.""",
    ["""Who checks the people in charge? You do.

1 Know who represents you
2 Show up to town halls
3 Follow the money. Budgets are public
4 Track the promises
5 Speak up, peacefully

Then vote. Your vote is your verdict. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 41
n = candidates(41, 3, ["APP", "BP", "DLA"], "8 to 10", "tickets 11 to 13", "ai-01-polling-queue.png", "ai-07-ballot-box.png", "ai-22-official-explains.png")
write_captions(41, "Carousel", "Know the Candidates",
    "Meet the candidates, part 3 of 6. Tickets 8 to 10 on INEC's ballot: APP, BP, DLA.",
    [("Queue outside a polling unit", "Meet the candidates. Part 3 of 6"),
     ("Woman casting her ballot", "Same layout, same facts, no favourites"),
     ("Photo or monogram (real photo only)", "Ticket 8, APP: Kabiru Yusuf, 54. Running mate Peace Egobia Ofordile"),
     ("Photo or monogram (real photo only)", "Ticket 9, BP: Sunday Adenuga, 52. Running mate Usman Turaki Mustapha"),
     ("Photo or monogram (real photo only)", "Ticket 10, DLA: Moses Olusoji Adebisi, 35. Running mate Nafisat Usaku Abubakar"),
     ("Official explaining the ballot", "Next: tickets 11 to 13. Information, not endorsement")],
    ["Names, ages, running mates, qualifications and ballot order: INEC Final List of Candidates (Presidential), Jan 2027 elections, PDF of 30 Oct 2026",
     "Candidate photos: still to add, real photos only (images/candidates/app-president.png, bp-president.png, dla-president.png)"],
    """Meet the candidates, part 3 of 6.

Tickets 8 to 10 on the presidential ballot, in INEC's order:

8. APP: Kabiru Yusuf, 54. Running mate: Peace Egobia Ofordile
9. BP: Sunday Adenuga, 52. Running mate: Usman Turaki Mustapha
10. DLA: Moses Olusoji Adebisi, 35. Running mate: Nafisat Usaku Abubakar

Same layout and the same facts for every candidate, straight from INEC's final list. We don't rank, endorse or comment. Next: tickets 11 to 13.""",
    ["""Meet the candidates, part 3 of 6. Tickets 8 to 10, in INEC's ballot order:

8 APP: Kabiru Yusuf, 54
9 BP: Sunday Adenuga, 52
10 DLA: Moses Olusoji Adebisi, 35

Facts from INEC's final list. Information, not endorsement. #NigeriaDecides2027""",
     """Running mates: Peace Egobia Ofordile (APP), Usman Turaki Mustapha (BP), Nafisat Usaku Abubakar (DLA).

Next in the series: tickets 11 to 13."""])

# ---------------------------------------------------------------- Day 40
write_script(40, "Single", "Demand Accountability", """
Public office is not a prize. It is a job. You are the employer.
Photo: ai-22-official-explains (polling official helping an elderly voter).""", '''
SLIDES = [
    ("statement", dict(
        lead="Public money pays them.\\nThe public is the boss.",
        punch="Public office\\nis not a prize.\\n*It's a job.*",
        size=126,
        body="You're not crowning a winner. You're hiring someone to serve you for four years. Hire carefully.",
        photo="ai-22-official-explains.png",
        pos="50% 15%",
    )),
]''')
write_captions(40, "Single", "Demand Accountability",
    "Reframes the election as hiring: public office is a job paid for by the public.",
    [("Polling official explaining the ballot to an elderly woman", "Public office is not a prize. It's a job. You're hiring for four years")],
    [],
    """Public office is not a prize. It's a job.

Public money pays every elected official. That makes the public the boss.

On 16 January and 6 February you're not crowning a winner. You're hiring someone to serve you for four years. Read the CV. Check the record. Ask how they'll do the work.

Hire carefully.""",
    ["""Public office is not a prize. It's a job.

Public money pays them. The public is the boss.

On 16 Jan and 6 Feb you're hiring someone for four years. Read the CV. Check the record. Hire carefully. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 39
write_script(39, "Carousel", "Know Your Power", """
Your governor touches more of your daily life than your president.
Spine: hook -> most of what you use every day is run by your state -> what
the governor controls -> when you choose (6 Feb, 28 states) -> CTA.
Facts: governorship elections on Sat 6 Feb 2027 in 28 states; 8 states
(Anambra, Bayelsa, Edo, Ekiti, Imo, Kogi, Ondo, Osun) elect governors on a
separate calendar (INEC).""", '''
SLIDES = [
    ("cover", dict(
        title="Your governor\\ntouches more\\nof your life than\\n*your president.*",
        size=112,
        photo="ai-09-hospital.png",
    )),
    ("statement", dict(
        lead="The road outside your house. The clinic\\ndown the street. Your child's secondary school.",
        punch="Most of it is\\nrun by your\\nstate.",
        size=124,
        photo="ai-10-classroom.png",
    )),
    ("list", dict(
        kicker="What your governor runs",
        title="The state\\n*government*",
        size=96,
        items=[("State roads", "Building and fixing the roads the state owns"),
               ("Health", "State hospitals and much of primary health care"),
               ("Education", "Public secondary schools and state universities"),
               ("Water and environment", "Water supply, sanitation, waste"),
               ("The state budget", "How the state's money is raised and spent")],
        photo="ai-11-market-trader.png",
    )),
    ("dates", dict(
        kicker="When you choose",
        title="Governor:\\n*Saturday 6 Feb*",
        size=96,
        rows=[("6 Feb", "2027", "Governorship election", "In 28 states. Same day as State House of Assembly"),
              ("8 states", "Other dates", "Anambra, Bayelsa, Edo, Ekiti, Imo, Kogi, Ondo, Osun", "Their governors are elected on a separate calendar")],
        photo="ai-01-polling-queue.png",
        source="INEC",
    )),
    ("cta", dict(
        lead="16 January matters. So does 6 February.\\nDon't stop after the first Saturday.",
        punch="Vote twice.\\nBoth Saturdays.",
        body="Same PVC, same polling unit. Save this and set a reminder.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(39, "Carousel", "Know Your Power",
    "Who does what: the governor. Most daily services are run by the state, and the governorship vote is on 6 Feb.",
    [("Busy public hospital corridor", "Your governor touches more of your life than your president"),
     ("Crowded public school classroom", "Roads, clinics, secondary schools: mostly run by your state"),
     ("Market woman at her stall", "What the governor runs: roads, health, education, water, the state budget"),
     ("Queue outside a polling unit", "Governorship election Sat 6 Feb in 28 states. 8 states on a separate calendar"),
     ("Young voters with inked thumbs", "Vote twice. Both Saturdays")],
    ["Governorship and State Assembly elections Sat 6 Feb 2027: INEC revised timetable, 26 Feb 2026",
     "8 states with off-cycle governorship elections (Anambra, Bayelsa, Edo, Ekiti, Imo, Kogi, Ondo, Osun), so 28 states vote for governor on 6 Feb: INEC",
     "State responsibilities: general description of state government functions under the 1999 Constitution"],
    """Your governor touches more of your daily life than your president.

The road outside your house. The clinic down the street. Your child's secondary school. Water. The state budget. Most of it is run by your state.

You choose your governor on Saturday 6 February 2027, in 28 states. (Anambra, Bayelsa, Edo, Ekiti, Imo, Kogi, Ondo and Osun elect their governors on a separate calendar.)

16 January matters. So does 6 February. Same PVC, same polling unit. Vote both Saturdays.""",
    ["""Your governor touches more of your life than your president.

State roads. State hospitals. Public secondary schools. Water. The state budget.

You choose your governor on Sat 6 Feb 2027, in 28 states. Vote both Saturdays. #NigeriaDecides2027""",
     """Anambra, Bayelsa, Edo, Ekiti, Imo, Kogi, Ondo and Osun elect their governors on a separate calendar. Everyone else: 6 February."""])

# ---------------------------------------------------------------- Day 38
write_script(38, "Carousel", "Vote Wisely", """
"They are all the same?" Here is how to actually compare them.
Spine: hook -> they're not the same, compare like an employer -> four things
to put side by side (plan, record, team, money) -> make your own scorecard.
Applies to every candidate equally.""", '''
COMPARE = [
    ("The plan", "Is it specific? Does it say how, by when\\nand with what money?", "ai-15-bus-stop-phone.png"),
    ("The record", "What did they actually do in their last\\njob, office or business?", "ai-06-walk-to-vote.png"),
    ("The team", "Running mate, party, allies. Who would\\nrun things with them?", "ai-04-friends-debate.png"),
    ("The money", "Can the promises be paid for?\\nAsk where it comes from.", "ai-11-market-trader.png"),
]

SLIDES = [
    ("cover", dict(
        title="\\u201cThey're all\\nthe same.\\u201d\\n*Here's how to\\ncompare them.*",
        size=116,
        photo="ai-14-town-hall.png",
    )),
    ("statement", dict(
        lead="They're not all the same.\\nBut slogans make them sound it.",
        punch="Compare them\\nlike you're\\nhiring.",
        size=124,
        body="Put any two candidates side by side on these four things.",
        photo="ai-13-family-table.png",
    )),
] + [
    ("statement", dict(kicker=f"Compare {i} of 4", punch=h, size=132, lead=None, body=b.replace("\\n", " "), photo=p))
    for i, (h, b, p) in enumerate(COMPARE, 1)
] + [
    ("cta", dict(
        lead="Score them yourself, one to five,\\non each of the four.",
        punch="Your scorecard.\\nYour choice.",
        body="Save this and use it before 16 January.",
        photo="ai-02-inked-thumb.png",
    )),
]''')
write_captions(38, "Carousel", "Vote Wisely",
    "Answers \"they're all the same\" with a simple way to compare any candidates: plan, record, team, money.",
    [("Town hall meeting", "\"They're all the same.\" Here's how to compare them"),
     ("Family around the dinner table", "Compare them like you're hiring"),
     ("Young man at a bus stop reading on his phone", "Compare 1: the plan"),
     ("Elderly man and young woman walking to vote", "Compare 2: the record"),
     ("Friends talking", "Compare 3: the team"),
     ("Market woman counting notes", "Compare 4: the money"),
     ("Inked thumb", "Score them yourself. Your scorecard, your choice")],
    ["No figures on this post"],
    """"They're all the same."

They're not. Slogans just make them sound it. Compare them like you're hiring for a job:

1. The plan: is it specific? How, by when, with what money?
2. The record: what did they actually do in their last office, job or business?
3. The team: running mate, party, allies. Who would run things with them?
4. The money: can the promises be paid for?

Score each candidate one to five on each. Your scorecard, your choice.""",
    ["""\"They're all the same.\"

They're not. Compare them like you're hiring:

1 The plan
2 The record
3 The team
4 The money

Score each one to five. Your scorecard, your choice. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 37
n = candidates(37, 4, ["LP", "NDC", "NDP"], "11 to 13", "tickets 14 to 16", "ai-03-public-count.png", "ai-07-ballot-box.png", "ai-27-wheelchair-voter.png")
write_captions(37, "Carousel", "Know the Candidates",
    "Meet the candidates, part 4 of 6. Tickets 11 to 13 on INEC's ballot: LP, NDC, NDP.",
    [("Public count at a polling unit", "Meet the candidates. Part 4 of 6"),
     ("Woman casting her ballot", "Same layout, same facts, no favourites"),
     ("Photo or monogram (real photo only)", "Ticket 11, LP: Sunday Chibuzo Okereke, 43. Running mate Hajja Bintu Konto"),
     ("Photo or monogram (real photo only)", "Ticket 12, NDC: Peter Gregory Obi, 65. Running mate Rabiu Musa Kwankwaso"),
     ("Photo or monogram (real photo only)", "Ticket 13, NDP: Ada Elizabeth Fredrick Okwori, 48. Running mate Uchenna Anthony Chukwuemeka"),
     ("Voter in a wheelchair being assisted", "Next: tickets 14 to 16. Information, not endorsement")],
    ["Names, ages, running mates, qualifications and ballot order: INEC Final List of Candidates (Presidential), Jan 2027 elections, PDF of 30 Oct 2026",
     "Candidate photos: still to add, real photos only (images/candidates/lp-president.png, ndc-president.png, ndp-president.png)"],
    """Meet the candidates, part 4 of 6.

Tickets 11 to 13 on the presidential ballot, in INEC's order:

11. LP: Sunday Chibuzo Okereke, 43. Running mate: Hajja Bintu Konto
12. NDC: Peter Gregory Obi, 65. Running mate: Rabiu Musa Kwankwaso
13. NDP: Ada Elizabeth Fredrick Okwori, 48. Running mate: Uchenna Anthony Chukwuemeka

Same layout and the same facts for every candidate, straight from INEC's final list. We don't rank, endorse or comment. Next: tickets 14 to 16.""",
    ["""Meet the candidates, part 4 of 6. Tickets 11 to 13, in INEC's ballot order:

11 LP: Sunday Chibuzo Okereke, 43
12 NDC: Peter Gregory Obi, 65
13 NDP: Ada Elizabeth Fredrick Okwori, 48

Facts from INEC's final list. Information, not endorsement. #NigeriaDecides2027""",
     """Running mates: Hajja Bintu Konto (LP), Rabiu Musa Kwankwaso (NDC), Uchenna Anthony Chukwuemeka (NDP).

Next in the series: tickets 14 to 16."""])
print("batch1 written")
