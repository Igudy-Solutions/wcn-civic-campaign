"""Writes tools/day_NN.py and the day's captions.md from a compact spec.
Used to build Days 46 to 1 in one pass; the generated day scripts are the
source of truth afterwards (edit those, not this)."""
import csv
import datetime as dt
import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TAGS = "#YourVoteYourVoice #YourVoteCounts #NigeriaDecides2027"


def row(day):
    for r in csv.DictReader(open(os.path.join(ROOT, "CONTENT_PLAN.csv"), encoding="utf-8-sig")):
        if int(r["Day"]) == day:
            return r
    raise KeyError(day)


def folder(day):
    r = row(day)
    return os.path.join(ROOT, f"Day {day:02d} - {r['Folder title']}")


def date_of(day):
    return dt.date(2026, 11, 20) + dt.timedelta(days=57 - day)


def write_script(day, fmt, pillar, doc, slides_src, extra_imports=""):
    d = date_of(day)
    head = f'"""Day {day}: {d:%a} {d.day} {d:%b %Y}. {fmt}. {pillar}.\n\n{doc.strip()}\n"""\n'
    body = f'''import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import render_post  # noqa: E402
from plan import folder_for  # noqa: E402
{extra_imports}
DAY = {day}
OUT = folder_for(DAY)

{slides_src.strip()}

if __name__ == "__main__":
    render_post(SLIDES, OUT, day=DAY)
'''
    path = os.path.join(ROOT, "tools", f"day_{day:02d}.py")
    open(path, "w").write("#!/usr/bin/env python3\n" + head + body)
    return path


def x_posts(posts, nslides):
    out = []
    if nslides > 4:
        out.append("X allows 4 images per post, so this goes out as a thread.\n")
    for i, p in enumerate(posts, 1):
        assert len(p) <= 280, (len(p), p)
        if nslides > 4:
            a = (i - 1) * 4 + 1
            b = min(i * 4, nslides)
            rng = f"slide {a}" if a == b else f"slides {a} to {b}"
            label = f"**Post {i}**" + (" (" + rng + ")" if i == 1 else f", reply ({rng})")
        else:
            label = f"**Post {i}**"
        out.append(f"{label}\n\n{p}\n")
    return "\n".join(out)


def write_captions(day, fmt, pillar, idea, slides, sources, ig, x, built_by=None):
    r = row(day)
    d = date_of(day)
    title = r["Folder title"]
    table = "| # | Photo | What it carries |\n|---|---|---|\n" + "\n".join(
        f"| {i} | {p} | {w} |" for i, (p, w) in enumerate(slides, 1))
    src = "\n".join(f"- {s}" for s in sources) if sources else "- No figures on this post"
    tag = f"{TAGS} #{day}DaysToGo" if day > 1 else f"{TAGS} #1DayToGo"
    kind = "scenes" if fmt == "Video" else "slides"
    md = f"""# Day {day}, {title}

**Post on** {d:%a} {d.day:02d} {d:%b %Y}
**Format** {fmt}
**Pillar** {pillar}
**Status** built, for team review
**Built by** `{built_by or f"tools/day_{day:02d}.py"}`

{idea.strip()}

## The {kind}

{table}

## Sources

(not printed on the {kind})

{src}

## Instagram caption

{ig.strip()}

{tag}

## X (Twitter)

{x_posts(x, len(slides) if fmt == "Carousel" else 1)}"""
    open(os.path.join(folder(day), "captions.md"), "w").write(md)
