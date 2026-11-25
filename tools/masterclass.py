#!/usr/bin/env python3
"""
WCN Monthly Masterclass flyers, 1080x1350 (Instagram portrait).

One flyer per row of Masterclass/schedule.csv. Edit the sheet, not this file.

    python3 tools/masterclass.py 2026-11-27            # one session, both layouts
    python3 tools/masterclass.py 2026-11-27 --layout arch
    python3 tools/masterclass.py --all                  # every row that has a title

Output: Masterclass/<date> - <Host>/flyer-<layout>.png

Layouts
  arch   text on the left, the host photo in a tall arch on the right
  card   the host photo in a big rounded card on top, text underneath

The host photo is used exactly as supplied (studio backgrounds kept), only
cropped to the frame. Photos live in images/hosts/.

Uses the same brand, font and Chrome render as the civic campaign
(tools/generate_carousel.py).
"""

import csv
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import generate_carousel as g  # noqa: E402

ROOT = g.ROOT
SHEET = os.path.join(ROOT, "Masterclass", "schedule.csv")
OUT_DIR = os.path.join(ROOT, "Masterclass")
HOST_DIR = os.path.join(ROOT, "images", "hosts")
LAYOUTS = ("arch", "card")

LIME, FOREST, INK = g.ACCENT, g.FOREST, g.INK
TBC = "To be announced"


def load():
    with open(SHEET, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def nice_date(iso):
    d = dt.date.fromisoformat(iso)
    return d.strftime("%a %-d %b %Y"), d.strftime("%-d"), d.strftime("%b").upper()


def css():
    return f"""
{g.font_css()}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:'Sans';color:#fff;position:relative;
  background:
    radial-gradient(900px 700px at 100% 0%, rgba(209,221,37,.22), transparent 60%),
    radial-gradient(800px 800px at 0% 100%, rgba(209,221,37,.10), transparent 60%),
    linear-gradient(160deg, #15592b 0%, {FOREST} 38%, {INK} 100%);}}
.dots{{position:absolute;inset:0;opacity:.18;
  background-image:radial-gradient(rgba(255,255,255,.55) 1.4px, transparent 1.6px);
  background-size:28px 28px;
  -webkit-mask-image:linear-gradient(200deg,#000 0%,transparent 45%);}}
.ring{{position:absolute;border:2px solid rgba(209,221,37,.35);border-radius:50%}}
.top{{position:absolute;left:64px;right:64px;top:56px;display:flex;
  justify-content:space-between;align-items:center;z-index:5}}
.top img{{height:58px;filter:drop-shadow(0 4px 14px rgba(0,0,0,.35))}}
.pill{{border:2px solid {LIME};color:{LIME};font-weight:700;font-size:20px;
  letter-spacing:.14em;text-transform:uppercase;padding:12px 22px;border-radius:999px}}
.kicker{{color:{LIME};font-weight:700;font-size:22px;letter-spacing:.16em;text-transform:uppercase}}
h1{{font-family:'Display';font-weight:800;letter-spacing:-.04em;line-height:1.02}}
h1 .acc{{color:{LIME}}}
.sub{{font-weight:500;color:rgba(255,255,255,.86);line-height:1.3}}
.learn h3{{font-weight:700;font-size:20px;letter-spacing:.16em;text-transform:uppercase;
  color:rgba(255,255,255,.6);margin-bottom:16px}}
.learn li{{list-style:none;display:flex;gap:16px;align-items:flex-start;font-size:25px;
  line-height:1.3;font-weight:500;margin-bottom:14px}}
.tick{{flex:none;width:34px;height:34px;border-radius:50%;background:{LIME};
  display:flex;align-items:center;justify-content:center;margin-top:-1px}}
.photo{{position:absolute;background-size:cover;background-repeat:no-repeat;
  box-shadow:0 30px 70px rgba(0,0,0,.45)}}
.name{{font-family:'Display';font-weight:800;font-size:34px;letter-spacing:-.02em}}
.role{{font-size:20px;font-weight:600;color:{FOREST};}}
.info{{position:absolute;left:64px;right:64px;bottom:118px;display:grid;
  grid-template-columns:1.25fr 1fr 1fr;border-radius:26px;overflow:hidden;
  background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.14)}}
.info div{{padding:22px 26px;border-left:1.5px solid rgba(255,255,255,.12)}}
.info div:first-child{{border-left:0;background:{LIME};color:{FOREST}}}
.info small{{display:block;font-size:17px;letter-spacing:.14em;text-transform:uppercase;
  font-weight:700;opacity:.7;margin-bottom:6px}}
.info b{{font-size:25px;font-weight:700;letter-spacing:-.01em}}
.info .tbc{{color:rgba(255,255,255,.55);font-weight:600;font-style:italic}}
.foot{{position:absolute;left:64px;right:64px;bottom:50px;display:flex;
  justify-content:space-between;align-items:center;font-size:21px;font-weight:600}}
.soc{{display:inline-flex;align-items:center;gap:10px;margin-right:30px}}
.foot .free{{color:{LIME};font-weight:700;letter-spacing:.06em}}
"""


TICK = (f'<span class="tick"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" '
        f'stroke="{FOREST}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>')


def headline(title):
    """Last word or two of the title in lime."""
    words = g.esc(title).split()
    n = 1 if len(words) <= 3 else 2
    return " ".join(words[:-n]) + f' <span class="acc">{" ".join(words[-n:])}</span>'


def learn_list(row):
    items = [s.strip() for s in (row.get("What you will learn") or "").split("|") if s.strip()]
    if not items:
        return ""
    lis = "".join(f"<li>{TICK}<span>{g.esc(s)}</span></li>" for s in items[:3])
    return f'<div class="learn"><h3>What you will learn</h3><ul>{lis}</ul></div>'


def info_bar(row):
    long, _, _ = nice_date(row["Date"])
    def cell(label, val):
        v = f"<b>{g.esc(val)}</b>" if val else f'<b class="tbc">{TBC}</b>'
        return f"<div><small>{label}</small>{v}</div>"
    return ('<div class="info">' + cell("Date", long) + cell("Time", row.get("Time", "").strip())
            + cell("Where", row.get("Platform", "").strip()) + "</div>")


def foot():
    ig = g.IG_ICON.format(c=LIME)
    x = g.X_ICON.format(c=LIME)
    return (f'<div class="foot"><div><span class="soc">{ig}{g.esc(g.IG_HANDLE)}</span>'
            f'<span class="soc">{x}{g.esc(g.X_HANDLE)}</span></div>'
            f'<span class="free">SAVE THE DATE</span></div>')


def host_line(row):
    aka = (row.get("Also known as") or "").strip()
    return g.esc(row["Host"]) + (f' <span style="opacity:.75;font-weight:600">({g.esc(aka)})</span>' if aka else "")


def top():
    return (f'<div class="top"><img src="{g.data_uri(g.LOGO)}"/>'
            f'<span class="pill">Monthly Masterclass</span></div>')


def photo_uri(row):
    p = os.path.join(HOST_DIR, row["Photo"])
    if not os.path.isfile(p):
        raise SystemExit(f"Host photo missing: {p}")
    return g.data_uri(p)


def title_size(title, base, long_at=30):
    return base if len(title) <= long_at else int(base * 0.84)


# ------------------------------------------------------------------ layouts
def layout_arch(row):
    t = row["Title"]
    fs = title_size(t, 78)
    sub = row.get("Subtitle", "").strip()
    inner = f"""
<div class="ring" style="width:760px;height:760px;right:-260px;top:120px"></div>
<div class="ring" style="width:560px;height:560px;right:-160px;top:220px;border-style:dashed"></div>
{top()}
<div class="photo" style="right:64px;top:168px;width:430px;height:620px;
  border-radius:215px 215px 28px 28px;background-image:url({photo_uri(row)});
  background-position:{row.get('Photo position') or '50% 20%'};border:6px solid {LIME}"></div>
<div style="position:absolute;right:40px;top:740px;width:478px;background:{LIME};color:{FOREST};
  border-radius:20px;padding:18px 24px;box-shadow:0 18px 40px rgba(0,0,0,.35)">
  <div class="role">YOUR HOST</div>
  <div class="name" style="font-size:30px;color:{FOREST}">{host_line(row)}</div>
</div>
<div style="position:absolute;left:64px;top:250px;width:500px">
  <div class="kicker" style="margin-bottom:22px">Masterclass · {nice_date(row['Date'])[1]} {nice_date(row['Date'])[2]}</div>
  <h1 style="font-size:{fs}px">{headline(t)}</h1>
  {f'<p class="sub" style="font-size:30px;margin-top:22px">{g.esc(sub)}</p>' if sub else ''}
</div>
<div style="position:absolute;left:64px;top:880px;right:64px">{learn_list(row)}</div>
{info_bar(row)}
{foot()}
"""
    return inner


def layout_card(row):
    t = row["Title"]
    sub = row.get("Subtitle", "").strip()
    _, day, mon = nice_date(row["Date"])
    fs = title_size(t, 70)
    inner = f"""
{top()}
<div class="photo" style="left:64px;right:64px;top:150px;height:520px;border-radius:32px;
  background-image:url({photo_uri(row)});background-position:{row.get('Photo position') or '50% 22%'}"></div>
<div style="position:absolute;left:64px;right:64px;top:150px;height:520px;border-radius:32px;
  background:linear-gradient(180deg,transparent 60%,rgba(6,18,10,.75) 100%)"></div>
<div style="position:absolute;right:96px;top:120px;width:150px;height:150px;border-radius:50%;
  background:{LIME};color:{FOREST};display:flex;flex-direction:column;align-items:center;
  justify-content:center;box-shadow:0 16px 40px rgba(0,0,0,.4);border:6px solid {FOREST}">
  <span style="font-family:'Display';font-weight:800;font-size:58px;line-height:1">{day}</span>
  <span style="font-weight:700;font-size:22px;letter-spacing:.14em">{mon}</span></div>
<div style="position:absolute;left:96px;top:592px">
  <div style="font-size:18px;letter-spacing:.16em;font-weight:700;color:{LIME}">YOUR HOST</div>
  <div class="name">{host_line(row)}</div></div>
<div style="position:absolute;left:64px;right:64px;top:712px">
  <h1 style="font-size:{fs}px">{headline(t)}</h1>
  {f'<p class="sub" style="font-size:29px;margin-top:14px">{g.esc(sub)}</p>' if sub else ''}
</div>
<div style="position:absolute;left:64px;right:64px;top:{960 if sub else 910}px">{learn_list(row).replace('<h3>What you will learn</h3>', '')}</div>
{info_bar(row)}
{foot()}
"""
    return inner


BUILDERS = {"arch": layout_arch, "card": layout_card}


def html(row, layout):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css()}</style></head>'
            f'<body><div class="dots"></div>{BUILDERS[layout](row)}</body></html>')


def build(row, layouts):
    if not row.get("Title", "").strip():
        print(f"  skip {row['Date']} {row['Host']}: no title yet")
        return
    first = row["Host"].split()[0]
    out = os.path.join(OUT_DIR, f"{row['Date']} - {first}")
    os.makedirs(out, exist_ok=True)
    for lay in layouts:
        path = os.path.join(out, f"flyer-{lay}.png")
        g.render(html(row, lay), path)
        print("  rendered", os.path.relpath(path, ROOT))


def main(argv):
    layouts = LAYOUTS
    if "--layout" in argv:
        layouts = (argv[argv.index("--layout") + 1],)
    rows = load()
    if "--all" in argv:
        pick = rows
    else:
        dates = [a for a in argv if a[:2] == "20"]
        if not dates:
            raise SystemExit(__doc__)
        pick = [r for r in rows if r["Date"] in dates]
        if not pick:
            raise SystemExit(f"No row for {dates} in {SHEET}")
    for r in pick:
        build(r, layouts)


if __name__ == "__main__":
    main(sys.argv[1:])
