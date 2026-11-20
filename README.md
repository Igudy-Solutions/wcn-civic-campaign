# WCN Civic Awareness, 57 days to vote

World Changers' non-partisan voter education campaign for Instagram, one post a
day from Fri 20 Nov 2026 (Day 57) to Fri 15 Jan 2027 (Day 1). The presidential
and National Assembly elections are on Sat 16 Jan 2027, and governorship and
State House of Assembly on Sat 6 Feb 2027 (INEC revised timetable, 26 Feb 2026).

Slides render to Instagram portrait, 1080x1350 (square 1080x1080 with
`--square`). Every slide is HTML, screenshotted with headless Chrome at 2x and
downsampled with Pillow, the same pipeline as Eden Centre and Ignovations.

## Where things live

| Path | What it holds |
| --- | --- |
| `CAROUSEL_GUIDE.md` | The rules. Look, type, neutrality, candidate posts. Read this first. |
| `CLAUDE.md` | How to change a topic or build a day. Start here. |
| `CONTENT_PLAN.csv` | **The plan sheet.** Which day carries which topic. Opens in Excel. Edit this. |
| `CONTENT_PLAN.md` | Read-only view of the sheet, rebuilt by `tools/plan.py`. Do not edit. |
| `CAMPAIGN_LOG.md` | Decisions, open questions, sources. |
| `templates/` | `TEMPLATES.md` and preview renders of each slide type. |
| `tools/generate_carousel.py` | The engine. Shared by every day. |
| `tools/day_NN.py` | One small file per day, words and photo names only. |
| `tools/plan.py` | Syncs the sheet: checks it, renames or creates day folders, rebuilds `CONTENT_PLAN.md`. |
| `tools/reel.py` | The election motion video (MP4). See `Specials/Election Reel/captions.md`. |
| `tools/parties_single.py` | The one-image list of every party on the presidential ballot. |
| `tools/parties.py` | Party colours for candidate slides (confirm before use). |
| `data/` | INEC final list of presidential candidates (PDF and JSON). |
| `images/` | Your photos. `images/candidates/` for cut-out portraits. |
| `fonts/` | Sora, the WCN brand font (SIL Open Font License). |
| `assets/` | Every WCN brand file (logos PNG, JPG, SVG, PDF), style references, the original content plan. See `assets/README.md`. |
| `Day 57 - ...` to `Day 01 - ...` | One folder per day: rendered slides plus `captions.md`. |
| `Specials/` | Posts outside the daily countdown, e.g. `Parties On The Ballot`. |

## Rendering a day

```bash
pip3 install pillow
python3 tools/day_57.py            # portrait, into the Day 57 folder
python3 tools/day_57.py --square   # square copy, into Day 57/square/
```

Chrome is found automatically on macOS. Elsewhere set `CHROME=/path/to/chrome`.

## Starting a new day

1. Read that day's `captions.md` stub and its row in `CONTENT_PLAN.csv`.
2. Copy `tools/day_57.py` to `tools/day_NN.py`, set `DAY` (`OUT` comes
   from the sheet) and the slide list. Ten slides at most.
3. Drop photos into `images/` and name them in `photo=`.
4. Render, then fill in `captions.md` (slide table, sources, caption).
5. Add anything you decided to `CAMPAIGN_LOG.md`.

## The rules that do not move

Non-partisan. We never tell anyone who to vote for and never condemn anyone.
Every candidate gets the same layout, in INEC ballot order, with facts from
INEC's list only. Every number has a source in the day script and captions.md
(not printed on the slide). WCN is not affiliated with whyvote.ng. Procedural
claims (polling times, documents, ballot rules) are checked against INEC's
latest guidance before posting.
# wcn-civic-campaign
