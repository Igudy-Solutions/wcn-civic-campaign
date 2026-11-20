#!/usr/bin/env python3
"""Sync the 57 day plan from CONTENT_PLAN.csv.

CONTENT_PLAN.csv at the repo root is the single source of truth for which day
carries which topic. Open it in Excel, Numbers or Google Sheets, change a row,
save it as CSV (keep the name), then run:

  python3 tools/plan.py

It will:
  * check the sheet (57 rows, Day 57 down to Day 1, Format is Carousel or
    Single, Status is planned, writing, built or posted, no empty Folder title)
  * fill in the Post date for every day (worked out from the Day, so a wrong
    date typed in the sheet is simply corrected)
  * rename a day's folder when its Folder title changed
  * create any missing day folder with a captions.md stub
  * refresh the header of a captions.md stub that is still `planned`
  * rewrite CONTENT_PLAN.md, the read-only view of the sheet

It never deletes a folder and never touches the slides or captions of a day
whose status is writing, built or posted, except to rename its folder.

Then commit and push, and everyone has the new plan.

Day N is posted N days before the presidential election (Sat 16 Jan 2027),
so Day 57 is Fri 20 Nov 2026 and Day 1 is Fri 15 Jan 2027.
"""

import csv
import datetime as dt
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SHEET = os.path.join(ROOT, "CONTENT_PLAN.csv")
ELECTION = dt.date(2027, 1, 16)
FIELDS = ["Day", "Post date", "Format", "Pillar", "Folder title",
          "Hook (cover title)", "Notes", "Status", "Owner"]
FORMATS = {"carousel": "Carousel", "single": "Single", "video": "Video", "c": "Carousel", "s": "Single", "v": "Video"}
STATUSES = ["planned", "writing", "built", "posted"]


def date_of(day):
    return ELECTION - dt.timedelta(days=int(day))


def clean_title(title):
    """Folder titles become folder names, so keep them filesystem safe."""
    t = re.sub(r"[^A-Za-z0-9 \-]+", "", title or "").strip()
    return re.sub(r"\s+", " ", t)[:70]


def read_sheet():
    with open(SHEET, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    errors = []
    missing = [f for f in FIELDS if rows and f not in rows[0]]
    if missing:
        sys.exit(f"CONTENT_PLAN.csv is missing column(s): {', '.join(missing)}")
    days = []
    for i, r in enumerate(rows, start=2):
        try:
            r["Day"] = int(str(r["Day"]).strip())
        except ValueError:
            errors.append(f"row {i}: Day '{r['Day']}' is not a number")
            continue
        days.append(r["Day"])
        f = FORMATS.get(str(r["Format"]).strip().lower())
        if not f:
            errors.append(f"Day {r['Day']}: Format must be Carousel, Single or Video")
        r["Format"] = f or r["Format"]
        s = str(r["Status"]).strip().lower() or "planned"
        if s not in STATUSES:
            errors.append(f"Day {r['Day']}: Status must be one of {', '.join(STATUSES)}")
        r["Status"] = s
        r["Folder title"] = clean_title(r["Folder title"])
        if not r["Folder title"]:
            errors.append(f"Day {r['Day']}: Folder title is empty")
        r["Post date"] = date_of(r["Day"]).isoformat()
    if sorted(days, reverse=True) != list(range(57, 0, -1)):
        errors.append("the sheet must have exactly one row for each Day from 57 down to 1")
    if errors:
        sys.exit("CONTENT_PLAN.csv has problems:\n  " + "\n  ".join(errors))
    return sorted(rows, key=lambda r: -r["Day"])


def write_sheet(rows):
    with open(SHEET, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def existing_folder(day):
    prefix = f"Day {day:02d} - "
    for name in sorted(os.listdir(ROOT)):
        if name.startswith(prefix) and os.path.isdir(os.path.join(ROOT, name)):
            return name
    return None


def folder_for(day):
    """The folder a day script should render into. Reads the sheet, so a
    renamed topic is picked up without editing the script."""
    for r in read_sheet():
        if r["Day"] == int(day):
            return f"Day {r['Day']:02d} - {r['Folder title']}"
    raise SystemExit(f"Day {day} is not in CONTENT_PLAN.csv")


HEADER = """# Day {day}, {hook}

**Post on** {date}
**Format** {fmt}
**Pillar** {pillar}
**Status** {status}
**Built by** `tools/day_{day:02d}.py` (not written yet)
"""

STUB = HEADER + """
## Idea

{notes}

## The slides

Write the story spine first (CAROUSEL_GUIDE.md, section 4b).

| # | Photo | What it carries |
|---|---|---|
| 1 | | Cover: {hook} |

## Sources

(where each number came from; not printed on the slides)

## Instagram caption

(write here)

{hashtags}

## X (Twitter)

Max 4 images per post. A carousel over 4 slides goes out as a thread:
post 1 takes slides 1 to 4, each reply takes the next 4. Under 280 characters each.

**Post 1** (slides 1 to 4)

(write here)
"""


def fields(r):
    d = date_of(r["Day"])
    return dict(day=r["Day"], hook=r["Hook (cover title)"], date=d.strftime("%a %d %b %Y"),
                fmt=r["Format"], pillar=r["Pillar"], status=r["Status"],
                notes=r["Notes"] or "(none)",
                hashtags=f"#YourVoteYourVoice #YourVoteCounts #NigeriaDecides2027 #{r['Day']}DaysToGo")


def main():
    rows = read_sheet()
    made = renamed = refreshed = 0
    for r in rows:
        day = r["Day"]
        want = f"Day {day:02d} - {r['Folder title']}"
        have = existing_folder(day)
        if have and have != want:
            os.rename(os.path.join(ROOT, have), os.path.join(ROOT, want))
            print(f"  renamed  {have}  ->  {want}")
            renamed += 1
        elif not have:
            os.makedirs(os.path.join(ROOT, want))
            made += 1
        cap = os.path.join(ROOT, want, "captions.md")
        if not os.path.exists(cap):
            with open(cap, "w", encoding="utf-8") as fh:
                fh.write(STUB.format(**fields(r)))
        elif r["Status"] == "planned":
            # Keep whatever was written below the header; refresh the header
            # so a changed topic, pillar or format shows up.
            with open(cap, encoding="utf-8") as fh:
                text = fh.read()
            body = text.split("\n## ", 1)
            new = HEADER.format(**fields(r)) + ("\n## " + body[1] if len(body) > 1 else "")
            if new != text:
                with open(cap, "w", encoding="utf-8") as fh:
                    fh.write(new)
                refreshed += 1
    write_sheet(rows)

    md = ["# Content plan, 57 days to 16 January 2027", "",
          "Read-only view. **Edit `CONTENT_PLAN.csv`** (opens in Excel), then run",
          "`python3 tools/plan.py`, then commit and push. See CLAUDE.md.", "",
          "Notes that mention whyvote are research pointers only. WCN is not affiliated",
          "with whyvote.ng; never cite it in a post.", "",
          "| Day | Post date | Format | Pillar | Hook | Status | Owner | Notes |",
          "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        d = date_of(r["Day"]).strftime("%a %d %b")
        md.append(f"| {r['Day']} | {d} | {r['Format']} | {r['Pillar']} | {r['Hook (cover title)']} "
                  f"| {r['Status']} | {r['Owner']} | {r['Notes']} |")
    with open(os.path.join(ROOT, "CONTENT_PLAN.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md) + "\n")
    print(f"{made} folder(s) created, {renamed} renamed, {refreshed} stub(s) refreshed. "
          "CONTENT_PLAN.md rewritten.")


if __name__ == "__main__":
    main()
