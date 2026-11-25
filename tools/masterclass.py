#!/usr/bin/env python3
"""
WCN Monthly Masterclass flyers, 1080x1080 square (default) or 1080x1350 with --portrait.

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
LAYOUTS = ("pass", "stamp", "bold", "brutal")
# Arkcore (25 Nov): square 1080x1080 by default, the details are short.
# --portrait gives 1080x1350. Only `pass` has a square version so far.
SIZE = "portrait" if "--portrait" in sys.argv else "square"
SQ = SIZE == "square"
H = 1080 if SQ else 1350

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
html,body{{width:1080px;height:{H}px;overflow:hidden}}
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
.info .ic{{flex:none;display:flex;color:{LIME}}}
.info div:first-child .ic{{color:{FOREST}}}
.info .txt{{display:block}}
.info div{{display:flex;align-items:center;gap:16px;padding:22px 22px;border-left:1.5px solid rgba(255,255,255,.12)}}
.info div:first-child{{border-left:0;background:{LIME};color:{FOREST}}}
.info small{{display:block;font-size:17px;letter-spacing:.14em;text-transform:uppercase;
  font-weight:700;opacity:.7;margin-bottom:6px}}
.info b{{font-size:25px;font-weight:700;letter-spacing:-.01em}}
.info .tbc{{color:rgba(255,255,255,.55);font-weight:600;font-style:italic}}
.foot{{position:absolute;left:64px;right:64px;bottom:50px;display:flex;
  justify-content:space-between;align-items:center;font-size:21px;font-weight:600}}
.soc{{display:inline-flex;align-items:center;gap:12px;margin-right:30px}}
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
    def cell(label, val, icon):
        v = f"<b>{g.esc(val)}</b>" if val else f'<b class="tbc">{TBC}</b>'
        return (f'<div><span class="ic">{ICONS[icon]}</span>'
                f'<span class="txt"><small>{label}</small>{v}</span></div>')
    return ('<div class="info">' + cell("Date", long, "date")
            + cell("Time", row.get("Time", "").strip(), "time")
            + cell("Where", row.get("Platform", "").strip(), "where") + "</div>")


_SVG = ('<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{}</svg>')
ICONS = {
    "date": _SVG.format('<rect x="3" y="4.5" width="18" height="16.5" rx="2.5"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4"/>'
                        '<circle cx="8" cy="14" r=".9" fill="currentColor"/><circle cx="12" cy="14" r=".9" fill="currentColor"/>'
                        '<circle cx="16" cy="14" r=".9" fill="currentColor"/>'),
    "time": _SVG.format('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>'),
    "where": _SVG.format('<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.6"/>'),
}


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


def circ(svg, bg=FOREST):
    """A social icon inside a filled circle (Arkcore, 25 Nov)."""
    svg = svg.replace('width="30" height="30"', 'width="24" height="24"').replace('width="27" height="27"', 'width="21" height="21"')
    return (f'<span style="display:inline-flex;align-items:center;justify-content:center;width:46px;'
            f'height:46px;border-radius:50%;background:{bg};flex:none">{svg}</span>')


# ------------------------------------------------------------------ layouts
def kicker_date(row):
    _, d, m = nice_date(row["Date"])
    return f"{d} {m}"


def socials_foot(color, right="SAVE THE DATE"):
    ig = circ(g.IG_ICON.format(c=LIME))
    x = circ(g.X_ICON.format(c=LIME))
    return (f'<div class="foot" style="color:{color}"><div><span class="soc">{ig}{g.esc(g.IG_HANDLE)}</span>'
            f'<span class="soc">{x}{g.esc(g.X_HANDLE)}</span></div>'
            f'<span class="free" style="color:{color}">{right}</span></div>')


def logo_file(name):
    p = os.path.join(g.ASSET_DIR, "logo", name)
    return p if os.path.exists(p) else g.LOGO


STAMP_CSS = """
.stamp{position:absolute;padding:16px;background:%(F)s;
  -webkit-mask:radial-gradient(circle 9px,#0000 98%%,#000) -14px -14px/28px 28px round,
               linear-gradient(#000 0 0) content-box;
  -webkit-mask-composite:source-over}
.stamp .in{width:100%%;height:100%%;background:#fff;padding:12px}
.stamp .ph{width:100%%;height:100%%;background-size:cover;background-repeat:no-repeat}
.swoosh{position:absolute;left:-14px;right:-14px;bottom:-12px;height:26px}
""" % dict(F=FOREST)


def layout_stamp(row):
    """Light, centred title on top, the host photo as a postage stamp."""
    t = row["Title"]
    sub = row.get("Subtitle", "").strip()
    fs = title_size(t, 74)
    return f"""<style>{PASS_CSS}{STAMP_CSS}</style><div class="light">
<div class="top"><img src="{g.data_uri(logo_file('wcn-horizontal-lime-green.png'))}" style="filter:none"/>
  <span class="pill">Monthly Masterclass</span></div>
<div style="position:absolute;left:64px;right:64px;top:190px;text-align:center">
  <h1 style="font-size:{fs}px;line-height:1.1">{headline(t)}</h1>
  {f'<p class="sub" style="font-size:31px;margin-top:22px;font-style:italic;font-weight:500">{g.esc(sub)}</p>' if sub else ''}
</div>
<div class="stamp" style="left:300px;top:{450 if sub else 400}px;width:480px;height:580px;transform:rotate(-3deg);
  filter:drop-shadow(0 24px 40px rgba(13,66,31,.25))">
  <div class="in"><div class="ph" style="background-image:url({photo_uri(row)});
    background-position:{row.get('Photo position') or '50% 20%'}"></div></div></div>
<div style="position:absolute;left:560px;top:{900 if sub else 850}px;background:{FOREST};color:#fff;border-radius:18px;
  padding:16px 26px;transform:rotate(-3deg);box-shadow:0 14px 30px rgba(13,66,31,.3)">
  <div style="font-size:16px;letter-spacing:.16em;font-weight:700;color:{LIME}">SPEAKER</div>
  <div style="font-family:'Display';font-weight:800;font-size:38px;letter-spacing:-.02em">{g.esc(row['Host'])}</div></div>
<div style="position:absolute;left:150px;top:{560 if sub else 510}px;width:170px;height:170px;border-radius:50%;
  background:{LIME};color:{FOREST};display:flex;flex-direction:column;align-items:center;justify-content:center;
  transform:rotate(-10deg);box-shadow:0 14px 30px rgba(13,66,31,.25);z-index:3">
  <span style="font-family:'Display';font-weight:800;font-size:60px;line-height:1">{nice_date(row['Date'])[1]}</span>
  <span style="font-weight:800;font-size:24px;letter-spacing:.14em">{nice_date(row['Date'])[2]}</span></div>
{info_bar(row)}
{socials_foot(FOREST)}
</div>"""


BOLD_CSS = """
.lime{position:absolute;inset:0;color:%(F)s;
  background:radial-gradient(800px 700px at 100%% 0%%,#EEF58A 0%%,transparent 60%%),
             linear-gradient(170deg,%(L)s 0%%,#C3D01C 100%%)}
.lime .big{font-family:'Display';font-weight:800;font-size:116px;letter-spacing:-.05em;line-height:.9;color:%(F)s}
.lime .ghost{position:absolute;left:-20px;right:-20px;bottom:250px;font-family:'Display';font-weight:800;
  font-size:300px;letter-spacing:-.06em;color:transparent;-webkit-text-stroke:2px rgba(13,66,31,.12);
  white-space:nowrap;line-height:1}
.lime h1{color:%(F)s}
.lime h1 .acc{color:#fff;background:%(F)s;padding:0 12px;border-radius:10px;-webkit-box-decoration-break:clone}
.lime .sub{color:rgba(13,66,31,.85)}
.lime .info{background:%(F)s;border:0;box-shadow:0 18px 40px rgba(13,66,31,.25)}
.lime .info div{border-left-color:rgba(255,255,255,.12);color:#fff}
.lime .info div:first-child{background:#fff;color:%(F)s}
.lime .info .ic{color:%(L)s}
.lime .info div:first-child .ic{color:%(F)s}
""" % dict(F=FOREST, L=LIME)


def layout_bold(row):
    """Lime, MASTERCLASS in giant type, photo with a forest offset block."""
    t = row["Title"]
    sub = row.get("Subtitle", "").strip()
    fs = title_size(t, 60)
    return f"""<style>{BOLD_CSS}</style><div class="lime">
<div class="ghost">MASTERCLASS</div>
<div class="top"><img src="{g.data_uri(logo_file('wcn-horizontal-forest.png'))}" style="filter:none"/>
  <span class="pill" style="border-color:{FOREST};color:{FOREST}">{kicker_date(row)}</span></div>
<div style="position:absolute;left:64px;right:64px;top:170px">
  <div style="font-weight:700;font-size:26px;letter-spacing:.2em;margin-bottom:8px">MONTHLY</div>
  <div class="big">MASTERCLASS</div></div>
<div style="position:absolute;left:84px;top:{430}px;width:430px;height:560px;border-radius:28px;background:{FOREST}"></div>
<div style="position:absolute;left:64px;top:410px;width:430px;height:560px;border-radius:28px;
  background:url({photo_uri(row)}) {row.get('Photo position') or '50% 20%'}/cover no-repeat;border:5px solid {FOREST}"></div>
<div style="position:absolute;left:560px;right:64px;top:420px">
  <h1 style="font-size:{fs}px;line-height:1.12">{headline(t)}</h1>
  {f'<p class="sub" style="font-size:27px;margin-top:20px">{g.esc(sub)}</p>' if sub else ''}
  <div style="margin-top:38px;border-top:3px solid {FOREST};padding-top:18px">
    <div style="font-size:17px;letter-spacing:.16em;font-weight:700;opacity:.7">SPEAKER</div>
    <div style="font-family:'Display';font-weight:800;font-size:44px;letter-spacing:-.02em">{g.esc(row['Host'])}</div></div>
</div>
{info_bar(row)}
{socials_foot(FOREST)}
</div>"""


PASS_CSS = f"""
.light{{position:absolute;inset:0;color:{FOREST};
  background:radial-gradient(700px 600px at 95% 10%, rgba(209,221,37,.45), transparent 60%),
             radial-gradient(700px 600px at 0% 100%, rgba(13,66,31,.12), transparent 60%),
             linear-gradient(180deg,#F7F9EC 0%,#EEF3DA 100%)}}
.light .pill{{border-color:{FOREST};color:{FOREST}}}
.light .kicker{{color:#5d6b0a}}
.light h1{{color:{FOREST}}}
.light h1 .acc{{color:{FOREST};background:{LIME};padding:0 14px;border-radius:10px;
  -webkit-box-decoration-break:clone}}
.light .sub{{color:rgba(13,66,31,.85)}}
.light .learn{{background:#fff;border-radius:26px;padding:26px 28px 14px;
  box-shadow:0 16px 40px rgba(13,66,31,.12)}}
.light .learn h3{{color:{FOREST};opacity:.6}}
.light .learn li{{font-size:23px;color:{INK}}}
.light .info{{background:#fff;border-color:rgba(13,66,31,.12);box-shadow:0 16px 40px rgba(13,66,31,.10)}}
.light .info div{{border-left-color:rgba(13,66,31,.1)}}
.light .info div:first-child{{background:{FOREST};color:#fff}}
.light .info .ic{{color:{FOREST}}}
.light .info div:first-child .ic{{color:{LIME}}}
.light .info .tbc{{color:rgba(13,66,31,.5)}}
.light .foot{{color:{FOREST}}}
.light .foot .free{{color:{FOREST}}}
"""


def layout_pass(row):
    """Light layout: the host photo on a WCN speaker pass hanging from a lanyard."""
    t = row["Title"]
    sub = row.get("Subtitle", "").strip()
    fs = title_size(t, 64 if SQ else 70)
    # square / portrait geometry
    txt_top, lan_h, card_top, card_h, ph_h, name_fs = ((250, 160, 140, 610, 425, 31) if SQ
                                                        else (420, 250, 230, 760, 480, 38))
    first = g.esc(row["Host"].split()[0])
    aka = g.esc((row.get("Also known as") or "").strip())
    ig = circ(g.IG_ICON.format(c=LIME))
    x = circ(g.X_ICON.format(c=LIME))
    logo_dark = os.path.join(g.ASSET_DIR, "logo", "wcn-horizontal-lime-green.png")
    logo = logo_dark if os.path.exists(logo_dark) else g.LOGO
    return f"""<style>{PASS_CSS}</style><div class="light">
<div class="top"><img src="{g.data_uri(logo)}" style="filter:none"/></div>
<div style="position:absolute;left:64px;top:{txt_top}px;width:540px">
  <div class="kicker" style="margin-bottom:20px">Monthly Masterclass · {nice_date(row['Date'])[1]} {nice_date(row['Date'])[2]}</div>
  <h1 style="font-size:{fs}px;line-height:1.12">{headline(t)}</h1>
  {f'<p class="sub" style="font-size:28px;margin-top:20px">{g.esc(sub)}</p>' if sub else ''}
</div>
<div style="position:absolute;right:205px;top:0;width:56px;height:{lan_h}px;background:{FOREST};
  transform:skewX(-6deg);box-shadow:inset 0 0 0 6px rgba(209,221,37,.35)"></div>
<div style="position:absolute;right:70px;top:{card_top}px;width:390px;height:{card_h}px;background:#fff;
  border-radius:28px;transform:rotate(5deg);box-shadow:0 30px 60px rgba(13,66,31,.25);padding:26px">
  <div style="width:90px;height:16px;border-radius:9px;background:#E4EAD0;margin:0 auto 22px"></div>
  <div style="height:{ph_h}px;border-radius:18px;background:url({photo_uri(row)}) {row.get('Photo position') or '50% 20%'}/cover no-repeat"></div>
  <div style="margin-top:18px;font-size:15px;letter-spacing:.16em;font-weight:700;color:#7d8a2a">SPEAKER</div>
  <div style="font-family:'Display';font-weight:800;font-size:{name_fs}px;color:{FOREST};letter-spacing:-.02em;line-height:1.1">{g.esc(row['Host'])}</div>
  {f'<div style="font-size:19px;font-weight:600;color:rgba(13,66,31,.7);margin-top:4px">aka {aka}</div>' if aka else ''}
  <div style="position:absolute;right:22px;top:18px;width:52px;height:52px;border-radius:50%;
    background:{LIME};display:flex;align-items:center;justify-content:center">
    <img src="{g.data_uri(os.path.join(g.ASSET_DIR, 'logo', 'wcn-mark-black.png'))}" style="width:34px;opacity:.85"/></div>
</div>
<div style="position:absolute;left:64px;right:64px;top:{850 if sub else 800}px">{learn_list(row)}</div>
{info_bar(row)}
<div class="foot"><div><span class="soc">{ig}{g.esc(g.IG_HANDLE)}</span>
  <span class="soc">{x}{g.esc(g.X_HANDLE)}</span></div><span class="free">SAVE THE DATE</span></div>
</div>"""


BRUTAL_CSS = """
.nb{position:absolute;inset:0;color:%(F)s;background-color:#F5F8E4;
  background-image:linear-gradient(rgba(13,66,31,.07) 2px,transparent 2px),
                   linear-gradient(90deg,rgba(13,66,31,.07) 2px,transparent 2px);
  background-size:54px 54px}
.nb .box{border:5px solid %(F)s;box-shadow:10px 10px 0 %(F)s;border-radius:18px}
.nb h1{color:%(F)s;line-height:1.08}
.nb h1 .acc{display:inline-block;color:%(F)s;background:%(L)s;border:5px solid %(F)s;box-shadow:8px 8px 0 %(F)s;
  border-radius:14px;padding:0 16px;transform:rotate(-2deg);margin-top:10px}
.nb .cell{position:absolute;background:#fff;display:flex;align-items:center;gap:16px;padding:0 22px}
.nb .cell small{display:block;font-size:16px;letter-spacing:.14em;text-transform:uppercase;font-weight:800;opacity:.65}
.nb .cell b{font-size:25px;font-weight:800;letter-spacing:-.01em}
.nb .cell .ic{display:flex}
""" % dict(F=FOREST, L=LIME)


def layout_brutal(row):
    """Neubrutalism: thick forest borders, hard offset shadows, lime stickers."""
    t = row["Title"]
    sub = row.get("Subtitle", "").strip()
    fs = title_size(t, 66 if SQ else 72)
    _, day, mon = nice_date(row["Date"])
    long = nice_date(row["Date"])[0]
    o = 0 if SQ else 140          # push things down on portrait
    ig = circ(g.IG_ICON.format(c=LIME))
    x = circ(g.X_ICON.format(c=LIME))
    def cell(left, width, icon, label, val, bg="#fff", fg=FOREST, icol=FOREST, shadow=FOREST):
        v = g.esc(val) if val else TBC
        return (f'<div class="cell box" style="left:{left}px;top:{H-245}px;width:{width}px;height:104px;'
                f'background:{bg};color:{fg};box-shadow:10px 10px 0 {shadow}"><span class="ic" style="color:{icol}">{ICONS[icon]}</span>'
                f'<span><small>{label}</small><b>{v}</b></span></div>')
    return f"""<style>{BRUTAL_CSS}</style><div class="nb">
<div class="top"><img src="{g.data_uri(logo_file('wcn-horizontal-lime-green.png'))}" style="filter:none"/>
  <span class="box" style="background:{LIME};padding:12px 22px;font-weight:800;font-size:20px;letter-spacing:.14em;
   box-shadow:6px 6px 0 {FOREST};border-radius:999px">MONTHLY MASTERCLASS</span></div>
<div style="position:absolute;left:64px;top:{230+o}px;width:520px">
  <h1 style="font-size:{fs}px">{headline(t)}</h1>
  {f'<div class="box" style="display:inline-block;margin-top:34px;background:#fff;padding:14px 20px;font-size:25px;font-weight:700;box-shadow:6px 6px 0 {FOREST}">{g.esc(sub)}</div>' if sub else ''}
</div>
<div class="box" style="position:absolute;right:76px;top:{160+o}px;width:390px;height:{500 if SQ else 620}px;
  transform:rotate(2.5deg);box-shadow:16px 16px 0 {FOREST};
  background:url({photo_uri(row)}) {row.get('Photo position') or '50% 20%'}/cover no-repeat"></div>
<div class="box" style="position:absolute;right:120px;top:{600+o+(0 if SQ else 120)}px;background:#fff;padding:12px 22px;
  transform:rotate(-2deg)">
  <div style="font-size:15px;letter-spacing:.16em;font-weight:800;color:#6f7d14">SPEAKER</div>
  <div style="font-family:'Display';font-weight:800;font-size:32px;letter-spacing:-.02em">{g.esc(row['Host'])}</div>
  {f'<div style="font-size:19px;font-weight:700;opacity:.7">aka {g.esc(row.get("Also known as","").strip())}</div>' if row.get("Also known as","").strip() else ''}</div>
<div class="box" style="position:absolute;right:400px;top:{130+o}px;width:136px;height:136px;border-radius:50%;
  background:{LIME};display:flex;flex-direction:column;align-items:center;justify-content:center;
  transform:rotate(-12deg);box-shadow:7px 7px 0 {FOREST};z-index:3">
  <span style="font-family:'Display';font-weight:800;font-size:52px;line-height:1">{day}</span>
  <span style="font-weight:800;font-size:21px;letter-spacing:.14em">{mon}</span></div>
{cell(64, 330, "date", "Date", long, bg=FOREST, fg="#fff", icol=LIME, shadow=LIME)}
{cell(420, 250, "time", "Time", row.get("Time", "").strip())}
{cell(696, 320, "where", "Where", row.get("Platform", "").strip(), bg=LIME)}
<div class="foot"><div><span class="soc">{ig}{g.esc(g.IG_HANDLE)}</span>
  <span class="soc">{x}{g.esc(g.X_HANDLE)}</span></div><span class="free" style="color:{FOREST}">SAVE THE DATE</span></div>
</div>"""


BUILDERS = {"pass": layout_pass, "stamp": layout_stamp, "bold": layout_bold, "brutal": layout_brutal}


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
        path = os.path.join(out, f"flyer-{lay}.png" if SQ else f"flyer-{lay}-portrait.png")
        g.render(html(row, lay), path, SIZE)
        print("  rendered", os.path.relpath(path, ROOT))


def main(argv):
    layouts = ("pass", "brutal") if SQ else LAYOUTS
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
