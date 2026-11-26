import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import write_script, write_captions, ROOT
from batch1 import candidates  # noqa  (re-runs batch1 writes, harmless)

T = json.load(open(os.path.join(ROOT, "data", "presidential_candidates.json")))["tickets"]

# ---------------------------------------------------------------- Day 36
write_script(36, "Single", "Know the Process", """
Countdown single: 36 days. Your polling unit is printed on your PVC.
Polling units can move or be added, so check before January.
Photo: ai-16-pvc-proud-card (voter card face drawn in by tools/pvc_card.py).""", '''
SLIDES = [
    ("countdown", dict(
        days=36,
        kicker="Saturday 16 January 2027",
        big=320,
        title="days. *Do you know\\nyour polling unit?*",
        size=100,
        body="It's printed on your PVC. Units can move, so confirm yours with INEC before January.",
        photo="ai-16-pvc-proud-card.png",
        pos="50% 12%",
    )),
]''')
write_captions(36, "Single", "Know the Process",
    "Countdown single. Know your polling unit before January: it's on your PVC, and it's worth confirming with INEC.",
    [("Young woman holding up her voter card", "36 days. Do you know your polling unit? It's on your PVC. Confirm it with INEC")],
    ["Your polling unit details are on your PVC; confirm them through INEC's official voter verification channels or your INEC office"],
    """36 days to Saturday 16 January 2027.

Do you know your polling unit? Not roughly. Exactly.

It's printed on your PVC. Polling units can be moved or added, so confirm yours with INEC's official voter verification or at your INEC office before January. Then walk or drive past it once, so you know the way.""",
    ["""36 days to election day.

Do you know your polling unit? Exactly, not roughly.

It's printed on your PVC. Units can move, so confirm yours with INEC before January. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 35
write_script(35, "Carousel", "Know Your Power", """
What does your senator actually do?
Spine: hook -> 109 senators (3 per state, 1 for the FCT) -> what they do ->
you elect yours on 16 Jan with the president -> do you know their name?
Facts: 1999 Constitution (as amended), s.48 and Part II.""", '''
SLIDES = [
    ("cover", dict(
        title="What does\\nyour senator\\n*actually do?*",
        size=132,
        photo="ai-14-town-hall.png",
    )),
    ("stat", dict(
        kicker="The Senate",
        lead="Three for every state, one for the FCT:",
        number="109",
        label="senators. *One of them is yours.*",
        photo="ai-01-polling-queue.png",
        source="1999 Constitution",
    )),
    ("list", dict(
        kicker="The job",
        title="What your\\n*senator does*",
        size=96,
        items=[("Makes federal laws", "Every Act of the National Assembly passes the Senate"),
               ("Approves the national budget", "No federal spending without it"),
               ("Confirms top appointments", "Ministers, ambassadors, service chiefs"),
               ("Checks the government", "Committees question ministries and agencies"),
               ("Speaks for your district", "Brings your area's needs to Abuja")],
        photo="ai-10-classroom.png",
    )),
    ("statement", dict(
        lead="You choose your senator on\\nSaturday 16 January, the same day as the president.",
        punch="Can you name\\nyours today?",
        size=124,
        photo="ai-15-bus-stop-phone.png",
    )),
    ("cta", dict(
        lead="Find out who represents your senatorial\\ndistrict, and who wants to.",
        punch="Know them.\\nThen vote.",
        body="Save this. Share it with someone who skips the Senate box.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(35, "Carousel", "Know Your Power",
    "Who does what: the Senate. 109 senators, what they do, and that you elect yours on 16 Jan.",
    [("Town hall meeting", "What does your senator actually do?"),
     ("Queue outside a polling unit", "109 senators: 3 per state, 1 for the FCT"),
     ("Public school classroom", "Laws, the budget, confirming appointments, oversight, your district"),
     ("Young man reading on his phone", "You choose your senator on 16 Jan. Can you name yours?"),
     ("Young voters with inked thumbs", "Know them. Then vote")],
    ["109 senators, three per state and one for the FCT: 1999 Constitution (as amended), s.48",
     "Senate functions (lawmaking, appropriation, confirmation of appointments, oversight): 1999 Constitution (as amended)",
     "Senate elections held with the presidential election on Sat 16 Jan 2027: INEC timetable"],
    """What does your senator actually do?

There are 109 senators: three for every state and one for the FCT. One of them represents you.

Your senator:
1. Makes federal laws
2. Approves the national budget
3. Confirms top appointments like ministers and ambassadors
4. Checks the government through committees
5. Speaks for your district in Abuja

You choose your senator on Saturday 16 January, the same day as the president. Can you name yours today?""",
    ["""What does your senator actually do?

109 senators: 3 per state, 1 for the FCT.

They make federal laws, approve the budget, confirm ministers and check the government.

You choose yours on Sat 16 Jan. Can you name them? #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 34
write_script(34, "Carousel", "Peaceful Participation", """
No politician is worth your friendship. Five ways to argue without fighting.
Spine: hook -> it's okay to disagree -> five habits, one per slide -> CTA.""", '''
WAYS = [
    ("Ask before\\nyou argue.", "\\u201cWhy do you like them?\\u201d gets you further than \\u201cYou're wrong.\\u201d", "ai-04-friends-debate.png"),
    ("Talk issues,\\nnot insults.", "Debate the plan. Leave tribe, religion and family out of it.", "ai-13-family-table.png"),
    ("Agree on\\nthe facts first.", "If you can't agree what's true, check a trusted source together.", "ai-15-bus-stop-phone.png"),
    ("Know when\\nto stop.", "When voices rise, change the subject. You can pick it up another day.", "ai-11-market-trader.png"),
    ("Their vote\\nis theirs.", "You don't have to convince anyone. Respect the choice, keep the friend.", "ai-12-handshake.png"),
]

SLIDES = [
    ("cover", dict(
        title="No politician\\nis worth your\\n*friendship.*",
        size=128,
        photo="ai-12-handshake.png",
        pos="50% 15%",
    )),
    ("statement", dict(
        lead="Disagreeing is normal. It's democracy.",
        punch="Fighting\\nis optional.",
        size=132,
        body="Five ways to talk politics and still be friends tomorrow.",
        photo="ai-04-friends-debate.png",
    )),
] + [
    ("statement", dict(kicker=f"Way {i} of 5", punch=h, size=126, body=b, photo=p))
    for i, (h, b, p) in enumerate(WAYS, 1)
] + [
    ("cta", dict(
        lead="Politicians move on after elections.\\nYour friends and neighbours stay.",
        punch="Disagree.\\nStay friends.",
        body="Send this to the group chat that gets heated.",
        photo="ai-24-peace-walk.png",
    )),
]''')
write_captions(34, "Carousel", "Peaceful Participation",
    "Five habits for talking politics without losing friends.",
    [("Two young men shaking hands", "No politician is worth your friendship"),
     ("Friends debating", "Disagreeing is normal. Fighting is optional"),
     ("Friends debating", "1 Ask before you argue"),
     ("Family dinner", "2 Talk issues, not insults"),
     ("Young man reading on his phone", "3 Agree on the facts first"),
     ("Market woman at her stall", "4 Know when to stop"),
     ("Handshake", "5 Their vote is theirs"),
     ("Community peace walk", "Disagree. Stay friends")],
    [],
    """No politician is worth your friendship.

Disagreeing is normal. Fighting is optional. Five ways to talk politics and still be friends tomorrow:

1. Ask before you argue
2. Talk issues, not insults. Leave tribe and religion out of it
3. Agree on the facts first
4. Know when to stop
5. Their vote is theirs

Politicians move on after elections. Your friends and neighbours stay. Send this to the group chat that always gets heated.""",
    ["""No politician is worth your friendship.

5 ways to argue without fighting:
1 Ask before you argue
2 Issues, not insults
3 Agree on the facts first
4 Know when to stop

#NigeriaDecides2027""",
     """5 Their vote is theirs. Respect the choice, keep the friend.

Politicians move on. Neighbours stay."""])

# ---------------------------------------------------------------- Day 33
candidates(33, 5, ["NRM", "PDP", "PRP"], "14 to 16", "tickets 17 to 19", "ai-23-inked-group.png", "ai-07-ballot-box.png", "ai-01-polling-queue.png")
write_captions(33, "Carousel", "Know the Candidates",
    "Meet the candidates, part 5 of 6. Tickets 14 to 16 on INEC's ballot: NRM, PDP, PRP.",
    [("Young voters showing inked thumbs", "Meet the candidates. Part 5 of 6"),
     ("Woman casting her ballot", "Same layout, same facts, no favourites"),
     ("Photo or monogram (real photo only)", "Ticket 14, NRM: Nkem Esther Okereke, 43. Running mate Nasir Muhammed Sulaiman"),
     ("Photo or monogram (real photo only)", "Ticket 15, PDP: Sandy Ojang Onor, 60. Running mate Babangida Umaru"),
     ("Photo or monogram (real photo only)", "Ticket 16, PRP: Donald Duke, 64. Running mate Sule Mohammed"),
     ("Queue outside a polling unit", "Next: tickets 17 to 19. Information, not endorsement")],
    ["Names, ages, running mates, qualifications and ballot order: INEC Final List of Candidates (Presidential), Jan 2027 elections, PDF of 30 Oct 2026",
     "Candidate photos: still to add, real photos only (images/candidates/nrm-president.png, pdp-president.png, prp-president.png)"],
    """Meet the candidates, part 5 of 6.

Tickets 14 to 16 on the presidential ballot, in INEC's order:

14. NRM: Nkem Esther Okereke, 43. Running mate: Nasir Muhammed Sulaiman
15. PDP: Sandy Ojang Onor, 60. Running mate: Babangida Umaru
16. PRP: Donald Duke, 64. Running mate: Sule Mohammed

Same layout and the same facts for every candidate, straight from INEC's final list. We don't rank, endorse or comment. Next: tickets 17 to 19.""",
    ["""Meet the candidates, part 5 of 6. Tickets 14 to 16, in INEC's ballot order:

14 NRM: Nkem Esther Okereke, 43
15 PDP: Sandy Ojang Onor, 60
16 PRP: Donald Duke, 64

Facts from INEC's final list. Information, not endorsement. #NigeriaDecides2027""",
     """Running mates: Nasir Muhammed Sulaiman (NRM), Babangida Umaru (PDP), Sule Mohammed (PRP).

Last part next: tickets 17 to 19."""])

# ---------------------------------------------------------------- Day 31
write_script(31, "Carousel", "Know Your Power", """
Your House of Reps member: the job most people cannot describe.
Spine: hook -> 360 members, one per federal constituency -> the job ->
elected 16 Jan -> know yours. Facts: 1999 Constitution (as amended), s.49.""", '''
SLIDES = [
    ("cover", dict(
        title="Your House\\nof Reps member.\\n*The job most\\npeople can't\\ndescribe.*",
        size=108,
        photo="ai-04-friends-debate.png",
    )),
    ("stat", dict(
        kicker="The House of Representatives",
        lead="One for each federal constituency:",
        number="360",
        label="members. *The closest\\nfederal lawmaker to you.*",
        photo="ai-11-market-trader.png",
        source="1999 Constitution",
    )),
    ("list", dict(
        kicker="The job",
        title="What your\\n*Rep does*",
        size=96,
        items=[("Makes federal laws", "Bills pass both the House and the Senate"),
               ("Shapes the national budget", "Budget bills start their journey in the National Assembly"),
               ("Checks the government", "Committees question ministries and agencies"),
               ("Represents your constituency", "A smaller area than a senator's. Often a few LGAs"),
               ("Brings projects home", "Pushes for your area's needs in the budget")],
        photo="ai-09-hospital.png",
    )),
    ("statement", dict(
        lead="You choose your Rep on Saturday 16 January,\\non the same day as the president and senator.",
        punch="Three ballots.\\nOne trip.",
        size=124,
        photo="ai-07-ballot-box.png",
    )),
    ("cta", dict(
        lead="Find out who represents your federal\\nconstituency, and who wants the job.",
        punch="Know your\\nRep.",
        body="Save this and share it with someone in your area.",
        photo="ai-23-inked-group.png",
    )),
]''')
write_captions(31, "Carousel", "Know Your Power",
    "Who does what: the House of Representatives. 360 members, what they do, and that you elect yours on 16 Jan.",
    [("Friends talking", "Your House of Reps member: the job most people can't describe"),
     ("Market woman at her stall", "360 members, one per federal constituency"),
     ("Public hospital corridor", "Laws, the budget, oversight, your constituency, projects"),
     ("Ballot box", "You choose your Rep on 16 Jan. Three ballots, one trip"),
     ("Young voters with inked thumbs", "Know your Rep")],
    ["360 members, one per federal constituency: 1999 Constitution (as amended), s.49",
     "House functions: 1999 Constitution (as amended)",
     "House elections held with the presidential and Senate elections on Sat 16 Jan 2027: INEC timetable"],
    """Your House of Reps member: the job most people can't describe.

There are 360 members, one for each federal constituency. Yours is the federal lawmaker closest to you.

Your Rep:
1. Makes federal laws with the Senate
2. Shapes the national budget
3. Checks the government through committees
4. Represents your constituency
5. Pushes for your area's needs in the budget

You choose your Rep on Saturday 16 January. Three ballots, one trip: President, Senate, House of Reps.""",
    ["""Your House of Reps member: the job most people can't describe.

360 members, one per federal constituency. They make laws, shape the budget and check the government.

You choose yours on Sat 16 Jan. Three ballots, one trip. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 30
candidates(30, 6, ["SDP", "YPP", "ZLP"], "17 to 19", "", "ai-03-public-count.png", "ai-07-ballot-box.png", "ai-23-inked-group.png")
write_captions(30, "Carousel", "Know the Candidates",
    "Meet the candidates, part 6 of 6. Tickets 17 to 19 on INEC's ballot: SDP, YPP, ZLP. Closes the series.",
    [("Public count at a polling unit", "Meet the candidates. Part 6 of 6"),
     ("Woman casting her ballot", "Same layout, same facts, no favourites"),
     ("Photo or monogram (real photo only)", "Ticket 17, SDP: Adewole Ebenezer Adebayo, 54. Running mate Usman Muhammed Bugaje"),
     ("Photo or monogram (real photo only)", "Ticket 18, YPP: Peter Ada Agada, 54. Running mate Patience Ndidi Key"),
     ("Photo or monogram (real photo only)", "Ticket 19, ZLP: Daniel Daberechukwu Nwanyanwu, 66. Running mate Khalid Hassan"),
     ("Young voters with inked thumbs", "That's all 18. Ticket 1 blank by court order")],
    ["Names, ages, running mates, qualifications and ballot order: INEC Final List of Candidates (Presidential), Jan 2027 elections, PDF of 30 Oct 2026",
     "Ticket 1 (A) has no candidate listed, remark 'COURT ORDER': same list",
     "Candidate photos: still to add, real photos only (images/candidates/sdp-president.png, ypp-president.png, zlp-president.png)"],
    """Meet the candidates, part 6 of 6.

Tickets 17 to 19 on the presidential ballot, in INEC's order:

17. SDP: Adewole Ebenezer Adebayo, 54. Running mate: Usman Muhammed Bugaje
18. YPP: Peter Ada Agada, 54. Running mate: Patience Ndidi Key
19. ZLP: Daniel Daberechukwu Nwanyanwu, 66. Running mate: Khalid Hassan

That's all 18 presidential candidates. Ticket 1 has no candidate listed, by court order. Same layout and the same facts for everyone. We don't rank, endorse or comment. Now you know every name.""",
    ["""Meet the candidates, part 6 of 6. Tickets 17 to 19, in INEC's ballot order:

17 SDP: Adewole Ebenezer Adebayo, 54
18 YPP: Peter Ada Agada, 54
19 ZLP: Daniel Daberechukwu Nwanyanwu, 66

That's all 18. Information, not endorsement. #NigeriaDecides2027""",
     """Running mates: Usman Muhammed Bugaje (SDP), Patience Ndidi Key (YPP), Khalid Hassan (ZLP).

Ticket 1 has no candidate listed, by court order."""])

# ---------------------------------------------------------------- Day 29
vps = [(t["vp"]["display"], f"{t['party']} · Ticket {t['sn']}", str(t["sn"])) for t in T if t["vp"]]
chunks = [vps[0:6], vps[6:12], vps[12:18]]
slides_src = f'''VPS = {vps!r}

SLIDES = [
    ("cover", dict(
        title="Second\\nin line.\\n*Meet the\\nrunning mates.*",
        size=124,
        photo="ai-22-official-explains.png",
    )),
    ("statement", dict(
        lead="If anything happens to a president,\\nthe vice president takes over.",
        punch="You're voting\\nfor two people.",
        size=124,
        body="All 18 vice presidential candidates, in INEC's ballot order. Numbers are ballot tickets.",
        photo="ai-07-ballot-box.png",
        source="1999 Constitution, s.146",
    )),
] + [
    ("list", dict(kicker=f"Running mates · {{i}} of 3", title="Tickets\\n*" + VPS[i * 6 - 6][2] + " to " + VPS[i * 6 - 1][2] + "*",
                  size=84, items=VPS[i * 6 - 6:i * 6], photo=p))
    for i, p in ((1, "ai-01-polling-queue.png"), (2, "ai-03-public-count.png"), (3, "ai-06-walk-to-vote.png"))
] + [
    ("cta", dict(
        lead="Ticket 1 has no candidates listed,\\nby court order.",
        punch="Check the\\nwhole ticket.",
        body="Information, not endorsement. Your vote, your choice.",
        photo="ai-23-inked-group.png",
    )),
]'''
write_script(29, "Carousel", "Know the Candidates", """
Second in line. Meet the running mates: all 18 vice presidential candidates
from INEC's final list, in ballot order, three list slides of six.
Facts: INEC final list; VP succession, 1999 Constitution s.146.""", slides_src)
write_captions(29, "Carousel", "Know the Candidates",
    "All 18 vice presidential candidates in INEC's ballot order. A vote for president is a vote for the ticket.",
    [("Official explaining the ballot", "Second in line. Meet the running mates"),
     ("Woman casting her ballot", "If anything happens to a president, the VP takes over. You're voting for two"),
     ("Queue outside a polling unit", "Running mates, tickets 2 to 7"),
     ("Public count", "Running mates, tickets 8 to 13"),
     ("Walking to vote", "Running mates, tickets 14 to 19"),
     ("Young voters with inked thumbs", "Check the whole ticket")],
    ["Running mates and ballot order: INEC Final List of Candidates (Presidential), Jan 2027 elections, PDF of 30 Oct 2026",
     "Vice president succeeds the president: 1999 Constitution (as amended), s.146"],
    "Second in line.\n\nIf anything happens to a president, the vice president takes over. On 16 January you're voting for two people.\n\nThe running mates, in INEC's ballot order:\n\n" + "\n".join(f"{v[2]}. {v[1].split(' ·')[0]}: {v[0]}" for v in vps) +
    "\n\nTicket 1 has no candidates listed, by court order. Information, not endorsement.",
    ["""Second in line. If anything happens to a president, the VP takes over.

On 16 Jan you're voting for two people.

All 18 running mates, in INEC's ballot order, in the thread. #NigeriaDecides2027""",
     "\n".join(f"{v[2]} {v[1].split(' ·')[0]}: {v[0]}" for v in vps[:9]),
     "\n".join(f"{v[2]} {v[1].split(' ·')[0]}: {v[0]}" for v in vps[9:]) + "\n\nCheck the whole ticket."])

# ---------------------------------------------------------------- Day 28
write_script(28, "Single", "Know the Candidates", """
35 to 79: the age range of the presidential candidates. Facts only, no names.
Youngest 35, oldest 79; running mates 35 to 74 (INEC final list).""", '''
SLIDES = [
    ("stat", dict(
        kicker="The 2027 presidential ballot",
        lead="The youngest candidate is 35. The oldest is 79.",
        number="35\\u201379",
        size=250,
        label="The age range of the people\\n*asking for your vote.*",
        body="Their running mates range from 35 to 74. Age alone tells you nothing. The plan and the record tell you more.",
        photo="ai-06-walk-to-vote.png",
        pos="50% 15%",
        source="INEC final list",
    )),
]''')
write_captions(28, "Single", "Know the Candidates",
    "Facts only: the age range on the presidential ballot. No names, no judgement on age.",
    [("Elderly man and young woman walking to vote", "35 to 79: the age range of the presidential candidates. Running mates 35 to 74")],
    ["Ages as printed on INEC's Final List of Candidates (Presidential), Jan 2027 elections: presidential candidates 35 to 79, vice presidential candidates 35 to 74"],
    """35 to 79.

That's the age range of the 18 people asking to be your president. The youngest is 35. The oldest is 79. Their running mates range from 35 to 74.

Age alone tells you nothing. The plan, the record and the team tell you more. Look at all three before you choose.""",
    ["""35 to 79.

The age range of the 18 presidential candidates on the 2027 ballot. Running mates: 35 to 74.

Age alone tells you nothing. Check the plan, the record and the team. #NigeriaDecides2027"""])

# ---------------------------------------------------------------- Day 27
write_script(27, "Carousel", "Know the Candidates", """
Women on the 2027 presidential ballot: how many?
2 of 18 presidential candidates and 4 of 18 running mates are women
(INEC final list). Facts and names only, ballot order, no endorsement.""", '''
SLIDES = [
    ("cover", dict(
        title="Women on the\\n2027 presidential\\nballot. *How many?*",
        size=118,
        photo="ai-23-inked-group.png",
    )),
    ("stat", dict(
        kicker="Presidential candidates",
        lead="Out of 18 people running for president:",
        number="2",
        size=340,
        label="are women.",
        photo="ai-02-inked-thumb.png",
        source="INEC final list",
    )),
    ("stat", dict(
        kicker="Running mates",
        lead="Out of 18 vice presidential candidates:",
        number="4",
        size=340,
        label="are women.",
        photo="ai-22-official-explains.png",
        source="INEC final list",
    )),
    ("list", dict(
        kicker="In INEC's ballot order",
        title="The six\\n*women*",
        size=96,
        items=[("Peace Egobia Ofordile", "Running mate · APP · Ticket 8", "8"),
               ("Nafisat Usaku Abubakar", "Running mate · DLA · Ticket 10", "10"),
               ("Hajja Bintu Konto", "Running mate · LP · Ticket 11", "11"),
               ("Ada Elizabeth Fredrick Okwori", "President · NDP · Ticket 13", "13"),
               ("Nkem Esther Okereke", "President · NRM · Ticket 14", "14"),
               ("Patience Ndidi Key", "Running mate · YPP · Ticket 18", "18")],
        photo="ai-07-ballot-box.png",
        source="INEC final list",
    )),
    ("cta", dict(
        lead="6 of the 36 names on the presidential\\ntickets are women.",
        punch="Now you\\nknow.",
        body="Information, not endorsement. Your vote, your choice.",
        photo="ai-27-wheelchair-voter.png",
    )),
]''')
write_captions(27, "Carousel", "Know the Candidates",
    "Facts from INEC's list: 2 of 18 presidential candidates and 4 of 18 running mates are women.",
    [("Young voters with inked thumbs", "Women on the 2027 presidential ballot. How many?"),
     ("Inked thumb", "2 of 18 presidential candidates are women"),
     ("Official explaining the ballot", "4 of 18 running mates are women"),
     ("Ballot box", "The six women, in ballot order"),
     ("Voter being assisted at a polling unit", "6 of 36 names on the tickets. Now you know")],
    ["Gender and names as on INEC's Final List of Candidates (Presidential), Jan 2027 elections, PDF of 30 Oct 2026"],
    """Women on the 2027 presidential ballot: how many?

Presidential candidates: 2 of 18.
Running mates: 4 of 18.

In INEC's ballot order:
Ticket 8, APP: Peace Egobia Ofordile (running mate)
Ticket 10, DLA: Nafisat Usaku Abubakar (running mate)
Ticket 11, LP: Hajja Bintu Konto (running mate)
Ticket 13, NDP: Ada Elizabeth Fredrick Okwori (president)
Ticket 14, NRM: Nkem Esther Okereke (president)
Ticket 18, YPP: Patience Ndidi Key (running mate)

6 of the 36 names on the presidential tickets. Information, not endorsement.""",
    ["""Women on the 2027 presidential ballot:

2 of 18 presidential candidates
4 of 18 running mates

6 of 36 names on the tickets. Names in the thread, in INEC's ballot order. #NigeriaDecides2027""",
     """President: Ada Elizabeth Fredrick Okwori (NDP), Nkem Esther Okereke (NRM).

Running mates: Peace Egobia Ofordile (APP), Nafisat Usaku Abubakar (DLA), Hajja Bintu Konto (LP), Patience Ndidi Key (YPP)."""])
print("batch2 written")
