# CLAUDE.md, WCN Civic Awareness

Instructions for anyone working in this repo, person or AI assistant. Read
this first, then `CAROUSEL_GUIDE.md` (the design and content rules) and
`CAMPAIGN_LOG.md` (what was decided and why).

## What this is

World Changers Network's non-partisan voter education campaign for Instagram
(`world_changersnetwork`) and X (`worldchangernet`). One post a day for 57 days,
from Day 57 (Fri 20 Nov 2026) to Day 1 (Fri 15 Jan 2027). Presidential and
National Assembly elections are Sat 16 Jan 2027; Governorship and State
Assembly are Sat 6 Feb 2027 (INEC revised timetable, 26 Feb 2026).

## The plan sheet: which day carries which topic

**`CONTENT_PLAN.csv` is the single source of truth.** It opens in Excel,
Numbers or Google Sheets. One row per day:

| Column | What goes in it |
|---|---|
| Day | 57 down to 1. Do not add or remove rows |
| Post date | Filled in automatically from the Day. Leave it |
| Format | `Carousel`, `Single` or `Video` |
| Pillar | Know Your Power, Know the Process, Vote Wisely, Peaceful Participation, Demand Accountability, Know the Candidates |
| Folder title | Short name for the day's folder, letters and numbers only, e.g. `Where Is Your PVC` |
| Hook (cover title) | The cover line. Provocative, never partisan |
| Notes | The idea, facts to use, anything to VERIFY |
| Status | `planned`, `writing`, `built` or `posted` |
| Owner | Who is making it |

`CONTENT_PLAN.md` is a read-only view of the sheet, rebuilt by the script.
Never edit it by hand.

### To change a topic

1. `git pull` so you have the latest sheet.
2. Open `CONTENT_PLAN.csv`, change the row (Hook, Folder title, Format,
   Notes...). Set Status and Owner if you are taking the day.
3. Save **as CSV** with the same name. (Excel: File > Save As > CSV UTF-8.)
4. Run `python3 tools/plan.py`. It checks the sheet, renames the day's folder
   if the Folder title changed, creates any missing folder, refreshes the
   header of a still-`planned` captions.md, and rebuilds `CONTENT_PLAN.md`.
   If the sheet has a problem it says which row and changes nothing.
5. Commit and push:
   ```bash
   git add -A
   git commit -m "Plan: Day 44 now covers <topic>"
   git push
   ```
   Everyone else gets it on their next `git pull`.

Swapping two days' topics: swap the whole rows' content (not the Day
numbers), run the script, push. If a swapped day is already `built`, also
update its `tools/day_NN.py` and re-render.

## To build a day

1. Set the day to `writing` with your name in the sheet, run `plan.py`, push.
   That tells the team you have it.
2. Copy `tools/day_57.py` to `tools/day_NN.py`. Set `DAY = NN`. `OUT` comes
   from the sheet automatically. Write the story spine, then the slides (ten
   at most). For a single image copy `tools/day_57_single.py` instead.
3. Photos go in `images/` (AI scenes in `images/ai/`, candidate cut-outs in
   `images/candidates/`). Name them in `photo="..."`.
4. `python3 tools/day_NN.py` renders into the day's folder. Check every slide.
5. Fill in that day's `captions.md`: slide table, sources, Instagram caption,
   X post or thread.
6. Set Status to `built`, run `plan.py`, commit, push. After it goes live,
   set `posted`.

Setup once: Google Chrome, Python 3, `pip3 install pillow`.

## Rules that do not move

- **Non-partisan.** Never tell anyone who to vote for. Never condemn, mock or
  praise a person, party, tribe or religion. Titles can sting the reader, never
  a candidate.
- **Candidates:** same template for all, INEC ballot order, INEC facts only
  (`data/presidential_candidates.json`), party colours from `tools/parties.py`.
  No candidate posts from Day 2 (campaigns close 24 hours before the vote).
- **No whyvote.ng.** WCN is not affiliated with it. Never name, link or tag it.
- **No "Source:" on slides.** Keep `source=` in the script and list sources in
  `captions.md`; check numbers against INEC.
- **Brand:** Sora only; lime `#D1DD25`, forest `#0D421F`; logo top left; IG
  and X icons with handles in the footer; swipe hand with SWIPE under it.
- **Photos:** people doing election things in every background. AI images
  never on candidate slides and never of real public figures.
- **Carousels tell a story.** Each slide picks up the one before it.
- **Every video is voiced.** One voice line per scene, mixed over the music
  bed by `tools/video_engine.py`. Never ship a silent video.
- **Videos carry no day count.** No "N days to go", no countdown, not even in
  the ticker, so any video can be shared on any day. Put the days left in the
  caption only. Videos are built with `tools/video_engine.py` (see a
  `tools/day_NN.py` whose Format is `Video`).
- **Voice lines:** say INEC as one word ("Eye-neck" in the script). Never say
  "one post a day".
- Change the look only in `tools/generate_carousel.py`, and write it down in
  `CAROUSEL_GUIDE.md` and `CAMPAIGN_LOG.md`.

## For an AI assistant

When asked to build Day NN: read this file, `CAROUSEL_GUIDE.md`,
`CAMPAIGN_LOG.md` and the Day NN row of `CONTENT_PLAN.csv`. Follow "To build a
day" exactly, render, look at every PNG, then fill in captions.md. When asked
to change a topic, edit the CSV row, run `tools/plan.py`, and show the diff.
Do not push without being asked.
