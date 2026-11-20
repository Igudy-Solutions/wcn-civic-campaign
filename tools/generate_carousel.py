#!/usr/bin/env python3
"""
WCN Civic Awareness, the render engine.

Every slide is real HTML and CSS, screenshotted with headless Chrome at 2x and
downsampled with Pillow so the type stays crisp. Same pipeline as Eden Centre
and Ignovations.

A day script (tools/day_57.py and so on) only holds words and photo names. It
calls `render_post(...)`. Never edit this file to make one post work; change the
look here once and every day picks it up.

Read CAROUSEL_GUIDE.md before changing anything here.
"""

import base64
import datetime as dt
import html as html_mod
import os
import re
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FONT_DIR = os.path.join(ROOT, "fonts")
IMAGE_DIR = os.path.join(ROOT, "images")
ASSET_DIR = os.path.join(ROOT, "assets")

# ------------------------------------------------------------------ election
# INEC revised timetable, released 26 Feb 2026.
PRESIDENTIAL_DAY = dt.date(2027, 1, 16)   # President, Senate, House of Reps
STATE_DAY = dt.date(2027, 2, 6)           # Governor, State House of Assembly

# ------------------------------------------------------------------ brand
# Handles shown in the footer with the Instagram and X icons.
IG_HANDLE = os.environ.get("WCN_IG", "world_changersnetwork")
X_HANDLE = os.environ.get("WCN_X", "worldchangernet")
BRAND = "World Changers Network"
LOGO = os.path.join(ASSET_DIR, "logo", "wcn-horizontal-lime-white.png")
# Arkcore (20 Nov): no "Source:" line on slides. Keep `source=` in day scripts
# anyway, it is the record of where each number came from, and it goes in
# captions.md. Flip this to True to print it on the slide again.
SHOW_SOURCES = False
HASHTAGS = "#YourVoteYourVoice #YourVoteCounts #NigeriaDecides2027"

INK = "#06120A"          # base, near black with the forest green in it
FOREST = "#0D421F"       # WCN forest green
ACCENT = "#D1DD25"       # WCN lime, from the logo. One line or one word per slide
ACCENT_INK = "#0D421F"   # WCN forest green, from the logo. Text on a lime fill
WHITE = "#FFFFFF"
DIM = "rgba(255,255,255,0.78)"

# ------------------------------------------------------------------ sizes
# 4:5 portrait is the default, it is the tallest ratio Instagram boosts.
# Square is there for the single image posts that need it.
SIZES = {"portrait": (1080, 1350), "square": (1080, 1080)}
SCALE = 2

CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
]


# Display sizes in day scripts were first set for a condensed face. Sora is
# wide, so every display size passes through px() and is scaled down here once.
DISP_SCALE = 0.8


def px(n):
    return int(round(n * DISP_SCALE))


def chrome():
    for c in CHROME_CANDIDATES:
        if c and os.path.exists(c):
            return c
    raise SystemExit("No Chrome found. Install Google Chrome or set CHROME=/path/to/chrome")


def days_to(date, today=None):
    today = today or dt.date.today()
    return (date - today).days


# ------------------------------------------------------------------ helpers
def b64_file(path):
    with open(path, "rb") as fh:
        return base64.b64encode(fh.read()).decode()


def data_uri(path):
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "png")
    return f"data:image/{mime};base64,{b64_file(path)}"


def esc(text):
    return html_mod.escape(text or "", quote=True)


def rich(text):
    """Escape, then turn the few marks we allow into markup.

    **word** bold white (in lead lines)
    *word*   accent colour
    [word]   accent marker block behind the word
    newline  line break
    """
    t = esc(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S)
    t = re.sub(r"\*(.+?)\*", r'<span class="acc">\1</span>', t, flags=re.S)
    t = re.sub(r"\[(.+?)\]", r'<span class="mark">\1</span>', t, flags=re.S)
    return t.replace("\n", "<br/>")


def find_photo(name):
    """Look a photo up in images/ (any subfolder). None means use the graphic."""
    if not name:
        return None
    direct = os.path.join(IMAGE_DIR, name)
    if os.path.isfile(direct):
        return direct
    for dirpath, _, files in os.walk(IMAGE_DIR):
        if name in files:
            return os.path.join(dirpath, name)
    print(f"  ! photo '{name}' not in images/, using the graphic background")
    return None


def font_css():
    # Sora is the WCN brand font (it is the face in the logo). One family, two
    # jobs: ExtraBold for display, Regular to SemiBold for body.
    faces = [("Display", "Sora.ttf", "100 900"), ("Sans", "Sora.ttf", "100 900")]
    out = []
    for fam, f, w in faces:
        p = os.path.join(FONT_DIR, f)
        out.append(f"@font-face{{font-family:'{fam}';src:url(data:font/ttf;base64,{b64_file(p)}) "
                   f"format('truetype');font-weight:{w};font-display:block;}}")
    return "\n".join(out)


# ------------------------------------------------------------------ motifs
def fingerprint_svg(size=900, color=ACCENT, opacity=0.16, stroke=5):
    """A thumbprint drawn from broken concentric ridges. The voting motif."""
    cx, cy = size / 2, size / 2
    paths = []
    for i in range(1, 17):
        rx, ry = 18 * i + 6, 24 * i + 8
        circ = 3.1416 * (rx + ry)
        dash = circ * (0.62 + 0.03 * (i % 5))
        gap = circ * 0.08
        off = (i * 47) % int(circ)
        paths.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{color}" '
            f'stroke-width="{stroke}" stroke-linecap="round" stroke-dasharray="{dash:.0f} {gap:.0f}" '
            f'stroke-dashoffset="{off}" transform="rotate({-12 + i % 3 * 4} {cx} {cy})"/>')
    return (f'<svg class="print" width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
            f'style="opacity:{opacity}">{"".join(paths)}</svg>')


def swipe_hand(c=None):
    """A hand mid-swipe, with motion lines. Replaces the word Swipe."""
    c = c or ACCENT
    return f"""<svg width="78" height="64" viewBox="0 0 78 64" fill="none">
  <path d="M36 34V17.5a4.5 4.5 0 1 1 9 0V31" stroke="{c}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M45 31v-3.5a4 4 0 0 1 8 0V32" stroke="{c}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M53 32v-2a4 4 0 0 1 8 0v11c0 7.7-5.4 13-13 13h-3c-4 0-6.3-1.4-8.7-4.3l-8.6-10.5a4 4 0 0 1 5.8-5.4L36 38"
        stroke="{c}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M22 21c2.4-2.6 5.3-4 8.6-4" stroke="{c}" stroke-width="2.8" stroke-linecap="round" opacity="0.6"/>
  <path d="M16 28c1.4-1.6 3-2.9 4.8-3.8" stroke="{c}" stroke-width="2.8" stroke-linecap="round" opacity="0.35"/>
  <path d="M4 12h14M12 6l6 6-6 6" stroke="{c}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>
</svg>"""


ARROW = ('<svg width="54" height="18" viewBox="0 0 54 18" fill="none"><path d="M1 9h50M43 2l8 7-8 7" '
         'stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


# ------------------------------------------------------------------ page
BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:%(W)spx;height:%(H)spx;overflow:hidden;background:%(INK)s;}
body{font-family:'Sans';color:#fff;-webkit-font-smoothing:antialiased;position:relative;}
.bg{position:absolute;inset:0;background-size:cover;background-position:%(POS)s;
  filter:saturate(0.9) contrast(1.06) brightness(0.92);}
.graphic{position:absolute;inset:0;background:
  radial-gradient(120%% 80%% at 85%% 8%%, rgba(209,221,37,0.16), transparent 55%%),
  radial-gradient(90%% 60%% at 0%% 100%%, rgba(13,66,31,0.55), transparent 65%%),
  linear-gradient(160deg,#0D2A17 0%%,#06120A 62%%);}
.graphic .print{position:absolute;right:-260px;top:-140px;}
.grain{position:absolute;inset:0;opacity:0.10;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/></filter><rect width='160' height='160' filter='url(%%23n)'/></svg>");}
.scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,18,10,0.45) 0%%,
  rgba(6,18,10,0.0) 16%%,rgba(6,18,10,0.30) 32%%,rgba(6,18,10,0.85) 52%%,rgba(6,18,10,0.96) 70%%,
  rgba(6,18,10,0.98) 100%%);}
.badge{display:inline-flex;align-items:center;gap:16px;background:%(ACCENT)s;color:%(ACCENT_INK)s;
  border-radius:999px;padding:14px 28px 14px 16px;font-weight:800;font-size:30px;letter-spacing:-0.01em;
  margin-bottom:30px;box-shadow:0 10px 40px rgba(0,0,0,0.35);}
.badge .n{background:%(ACCENT_INK)s;color:%(ACCENT)s;border-radius:999px;min-width:66px;height:66px;
  display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:800;padding:0 14px;}
.foot .swipe{flex-direction:column;align-items:center;gap:4px;}
.swipelabel{font-weight:700;font-size:17px;letter-spacing:0.26em;text-transform:uppercase;color:%(ACCENT)s;}
.frame{position:absolute;inset:0;padding:64px 72px 58px;display:flex;flex-direction:column;}
.top{display:flex;align-items:center;justify-content:space-between;}
.brand{display:flex;align-items:center;gap:14px;font-weight:700;font-size:22px;
  letter-spacing:0.28em;text-transform:uppercase;}
.brand .dot{width:16px;height:16px;border-radius:50%%;background:%(ACCENT)s;
  box-shadow:0 0 0 6px rgba(209,221,37,0.22);}
.logotop{margin-bottom:28px;}
.logotop img{height:78px;width:auto;display:block;filter:drop-shadow(0 2px 10px rgba(0,0,0,0.6));}
.brand img{height:66px;width:auto;display:block;}
.count{font-weight:700;font-size:21px;letter-spacing:0.16em;text-transform:uppercase;
  border:2px solid rgba(255,255,255,0.85);border-radius:999px;padding:11px 22px;
  background:rgba(7,9,11,0.72);backdrop-filter:blur(6px);}
.count b{color:%(ACCENT)s;}
.stack{margin-top:auto;}
.kicker{font-weight:700;font-size:24px;letter-spacing:0.3em;text-transform:uppercase;
  color:%(ACCENT)s;margin-bottom:24px;}
.disp{font-family:'Display';font-weight:800;line-height:1.04;letter-spacing:-0.045em;color:#fff;}
.disp .acc,.lead .acc{color:%(ACCENT)s;}
.mark{background:%(ACCENT)s;color:%(ACCENT_INK)s;padding:0 0.12em;
  box-decoration-break:clone;-webkit-box-decoration-break:clone;}
.lead{font-weight:500;font-size:40px;line-height:1.38;color:rgba(255,255,255,0.88);
  letter-spacing:-0.01em;margin-bottom:30px;text-shadow:0 2px 18px rgba(0,0,0,0.75);}
.lead b{color:#fff;font-weight:700;}
.body{font-weight:400;font-size:32px;line-height:1.5;color:%(DIM)s;margin-top:28px;max-width:900px;}
.source{font-weight:500;font-size:20px;letter-spacing:0.06em;color:rgba(255,255,255,0.55);margin-top:26px;}
.foot{display:flex;align-items:center;justify-content:space-between;padding-top:44px;
  font-weight:600;font-size:24px;}
.foot .handle{display:flex;align-items:center;gap:34px;color:rgba(255,255,255,0.92);}
.soc{display:flex;align-items:center;gap:12px;}
.foot .swipe{display:flex;align-items:center;gap:14px;font-weight:700;}
.foot .page{color:rgba(255,255,255,0.55);letter-spacing:0.1em;}
"""


def page(inner, *, size="portrait", photo=None, pos="50% 30%", extra_css="", graphic=True, dim=0):
    W, H = SIZES[size]
    css = BASE_CSS % dict(W=W, H=H, INK=INK, ACCENT=ACCENT, ACCENT_INK=ACCENT_INK,
                          DIM=DIM, POS=pos)
    path = find_photo(photo)
    if path:
        layers = f'<div class="bg" style="background-image:url({data_uri(path)})"></div><div class="scrim"></div>'
        if dim:
            layers += f'<div style="position:absolute;inset:0;background:rgba(6,18,10,{dim})"></div>'
    elif graphic:
        layers = f'<div class="graphic">{fingerprint_svg(1000)}</div>'
    else:
        layers = ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{font_css()}
{css}
{extra_css}
</style></head><body>{layers}<div class="grain"></div>
<div class="frame">{inner}</div></body></html>"""


def logo_top():
    """WCN logo, top left, on every slide (Arkcore, 20 Nov). Logo only: the
    countdown lives in the cover badge, not up here."""
    if not os.path.exists(LOGO):
        return ""
    return f'<div class="logotop"><img src="{data_uri(LOGO)}" alt="{esc(BRAND)}"/></div>'


def topbar(day):
    n = day if day is not None else days_to(PRESIDENTIAL_DAY)
    label = "Election day" if n == 0 else f"<b>{n}</b> {'day' if n == 1 else 'days'} to vote"
    mark = (f'<img src="{data_uri(LOGO)}" alt="{esc(BRAND)}"/>' if os.path.exists(LOGO)
            else f'<span class="dot"></span>{esc(BRAND)}')
    return (f'<div class="top"><div class="brand">{mark}</div>'
            f'<div class="count">{label}</div></div>')


IG_ICON = ('<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2">'
           '<rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.3"/>'
           '<circle cx="17.6" cy="6.4" r="1.2" fill="{c}" stroke="none"/></svg>')
X_ICON = ('<svg width="27" height="27" viewBox="0 0 24 24"><path fill="{c}" d="M17.75 2.5h3.2l-7 8 8.23 10.9'
          'h-6.44l-5.05-6.6-5.77 6.6H1.7l7.48-8.56L1.28 2.5h6.6l4.56 6.03 5.31-6.03Zm-1.12 17h1.77L7.43 '
          '4.3h-1.9l11.1 15.2Z"/></svg>')


def socials():
    ig = IG_ICON.format(c=ACCENT)
    x = X_ICON.format(c=ACCENT)
    return (f'<div class="handle"><span class="soc">{ig}{esc(IG_HANDLE)}</span>'
            f'<span class="soc">{x}{esc(X_HANDLE)}</span></div>')


def footer(index, total, last):
    handle = socials()
    if last or total == 1:
        right = ""
    else:
        right = (f'<div class="swipe">{swipe_hand()}'
                 f'<span class="swipelabel">Swipe</span></div>')
    return f'<div class="foot">{handle}{right}</div>'


# ------------------------------------------------------------------ slide kinds
def badge(day=None):
    n = day if day is not None else days_to(PRESIDENTIAL_DAY)
    word = "day" if n == 1 else "days"
    return f'<div class="badge"><span class="n">{n}</span>{word} to election day</div><br/>'


def k_cover(c):
    size = c.get("size", 118)
    out = badge(c.get("_day")) if c.get("badge", True) else ""
    if c.get("kicker"):
        out += f'<div class="kicker">{esc(c["kicker"])}</div>'
    out += f'<div class="disp" style="font-size:{px(size)}px">{rich(c["title"])}</div>'
    if c.get("sub"):
        out += f'<div class="body">{rich(c["sub"])}</div>'
    return out


def k_statement(c):
    """Small wide-sans lead lines, then the punch in the display face."""
    out = ""
    if c.get("kicker"):
        out += f'<div class="kicker">{esc(c["kicker"])}</div>'
    if c.get("lead"):
        out += f'<div class="lead">{rich(c["lead"])}</div>'
    out += (f'<div class="disp" style="font-size:{px(c.get("size", 104))}px;color:{ACCENT}">'
            f'{rich(c["punch"])}</div>')
    if c.get("body"):
        out += f'<div class="body">{rich(c["body"])}</div>'
    if SHOW_SOURCES and c.get("source"):
        out += f'<div class="source">Source: {esc(c["source"])}</div>'
    return out


def k_stat(c):
    out = ""
    if c.get("kicker"):
        out += f'<div class="kicker">{esc(c["kicker"])}</div>'
    if c.get("lead"):
        out += f'<div class="lead">{rich(c["lead"])}</div>'
    out += (f'<div class="disp" style="font-size:{px(c.get("size", 300))}px;line-height:0.9;color:{ACCENT}">'
            f'{esc(c["number"])}</div>')
    out += f'<div class="disp" style="font-size:{px(c.get("label_size", 64))}px;margin-top:18px">{rich(c["label"])}</div>'
    if c.get("body"):
        out += f'<div class="body">{rich(c["body"])}</div>'
    if SHOW_SOURCES and c.get("source"):
        out += f'<div class="source">Source: {esc(c["source"])}</div>'
    return out


DATES_CSS = """
.row{display:flex;gap:34px;align-items:stretch;padding:30px 0;border-top:2px solid rgba(255,255,255,0.18);}
.row:last-child{border-bottom:2px solid rgba(255,255,255,0.18);}
.row .d{font-family:'Display';font-size:72px;line-height:0.95;color:%s;min-width:250px;font-weight:800;letter-spacing:-0.04em;}
.row .d small{display:block;font-family:'Sans';font-weight:700;font-size:20px;letter-spacing:0.2em;color:#fff;margin-top:10px;}
.row .w{font-weight:600;font-size:34px;line-height:1.35;align-self:center;}
.row .w span{display:block;font-weight:400;font-size:24px;color:rgba(255,255,255,0.65);margin-top:6px;}
""" % ACCENT


def k_dates(c):
    out = f'<div class="kicker">{esc(c["kicker"])}</div>' if c.get("kicker") else ""
    if c.get("lead"):
        out += f'<div class="lead">{rich(c["lead"])}</div>'
    if c.get("title"):
        out += f'<div class="disp" style="font-size:{px(c.get("size", 96))}px;margin-bottom:34px">{rich(c["title"])}</div>'
    for d, small, what, note in c["rows"]:
        out += (f'<div class="row"><div class="d">{esc(d)}<small>{esc(small)}</small></div>'
                f'<div class="w">{esc(what)}<span>{esc(note)}</span></div></div>')
    if SHOW_SOURCES and c.get("source"):
        out += f'<div class="source">Source: {esc(c["source"])}</div>'
    return out


LIST_CSS = """
.li{display:flex;gap:26px;align-items:baseline;padding:20px 0;border-top:2px solid rgba(255,255,255,0.14);}
.li .n{font-family:'Display';font-weight:800;font-size:54px;color:%s;min-width:62px;}
.li .t{font-weight:600;font-size:36px;line-height:1.3;}
.li .t span{display:block;font-weight:400;font-size:26px;color:rgba(255,255,255,0.68);margin-top:6px;}
""" % ACCENT


def k_list(c):
    out = ""
    if c.get("kicker"):
        out += f'<div class="kicker">{esc(c["kicker"])}</div>'
    out += f'<div class="disp" style="font-size:{px(c.get("size", 92))}px;margin-bottom:28px">{rich(c["title"])}</div>'
    for i, item in enumerate(c["items"], 1):
        head, note = (item if isinstance(item, (list, tuple)) else (item, ""))
        out += (f'<div class="li"><div class="n">{i:02d}</div><div class="t">{esc(head)}'
                f'{f"<span>{esc(note)}</span>" if note else ""}</div></div>')
    if SHOW_SOURCES and c.get("source"):
        out += f'<div class="source">Source: {esc(c["source"])}</div>'
    return out


def k_cta(c):
    out = f'<div class="lead">{rich(c.get("lead", "If this was useful, share it with one person who has not collected their PVC."))}</div>'
    punch = rich(c.get("punch", "Save. Share.\nShow up."))
    out += (f'<div class="disp" style="font-size:{px(c.get("size", 136))}px;color:{ACCENT}">'
            f'{punch}</div>')
    out += f'<div class="body">{rich(c.get("body", "Non-partisan. Your vote, your choice. Just use it."))}</div>'
    return out


COUNTDOWN_CSS = """
.big{font-family:'Display';font-weight:800;font-size:400px;line-height:0.85;color:%s;letter-spacing:-0.06em;}
""" % ACCENT


def k_countdown(c):
    n = c.get("days", days_to(PRESIDENTIAL_DAY))
    out = f'<div class="kicker">{esc(c.get("kicker", "Saturday 16 January 2027"))}</div>'
    out += f'<div class="big">{n}</div>'
    out += f'<div class="disp" style="font-size:{px(c.get("size", 108))}px;margin-top:26px">{rich(c.get("title", "Days to *election day.*"))}</div>'
    if c.get("body"):
        out += f'<div class="body">{rich(c["body"])}</div>'
    return out


# ---- candidates: party colours, cut-out portrait, same layout for everyone
CAND_CSS = """
.cband{position:absolute;inset:0;overflow:hidden;}
.cband i{position:absolute;width:1700px;height:230px;left:-300px;transform:rotate(-24deg);}
.cphoto{position:absolute;left:0;right:0;bottom:0;height:78%%;background-size:contain;
  background-repeat:no-repeat;background-position:center bottom;}
.cphoto.full{height:100%%;background-size:cover;background-position:%(POS)s;}
.cfade{position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%%,rgba(7,9,11,0.88) 72%%,rgba(7,9,11,0.98) 100%%);}
.cname{font-family:'Display';font-weight:800;font-size:86px;line-height:1.0;letter-spacing:-0.045em;}
.cparty{display:inline-flex;align-items:center;gap:14px;margin-top:22px;font-weight:700;font-size:26px;
  letter-spacing:0.12em;text-transform:uppercase;padding:12px 22px;border-radius:8px;}
.facts{margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:16px 34px;}
.fact b{display:block;font-weight:700;font-size:18px;letter-spacing:0.2em;text-transform:uppercase;color:rgba(255,255,255,0.55);}
.fact span{font-weight:600;font-size:28px;line-height:1.3;}
.frame .kicker{text-shadow:0 2px 14px rgba(0,0,0,0.85);}
.neutral{margin-top:26px;font-size:19px;font-weight:500;color:rgba(255,255,255,0.6);letter-spacing:0.04em;}
"""


def candidate_layers(c):
    cols = c.get("colours", ["#444", "#666", "#888"])
    bands = "".join(f'<i style="background:{col};top:{-120 + i * 250}px;opacity:0.92"></i>'
                    for i, col in enumerate(cols * 3))
    path = find_photo(c.get("photo"))
    cut = bool(path and path.lower().endswith(".png") and c.get("cutout", True))
    photo = ""
    if path:
        photo = (f'<div class="cphoto{"" if cut else " full"}" '
                 f'style="background-image:url({data_uri(path)})"></div>')
    else:
        photo = (f'<div style="position:absolute;left:290px;top:190px;width:500px;height:560px;'
                 f'border:3px dashed rgba(255,255,255,0.9);border-radius:24px;background:rgba(7,9,11,0.55);'
                 f'display:flex;align-items:center;justify-content:center;text-align:center;padding:30px;'
                 f'font-weight:700;font-size:22px;letter-spacing:0.14em;color:#fff">'
                 f'CUT-OUT PHOTO<br/>images/candidates/<br/>{esc(c.get("photo") or "")}</div>')
    return f'<div class="cband">{bands}</div>{photo}<div class="cfade"></div>'


def k_candidate(c):
    out = f'<div class="kicker">{esc(c.get("kicker", "On the ballot · President"))}</div>'
    out += f'<div class="cname">{rich(c["name"])}</div>'
    pc = c.get("colours", [ACCENT])[0]
    out += (f'<div class="cparty" style="background:{pc};color:{c.get("party_ink", "#fff")}">'
            f'{esc(c["party"])}</div>')
    if c.get("facts"):
        out += '<div class="facts">' + "".join(
            f'<div class="fact"><b>{esc(k)}</b><span>{esc(v)}</span></div>' for k, v in c["facts"]) + "</div>"
    out += (f'<div class="neutral">{esc(c.get("note", "Information, not endorsement. Every candidate gets the same layout."))}'
            f'{" Source: " + esc(c["source"]) if SHOW_SOURCES and c.get("source") else ""}</div>')
    return out


BALLOT_CSS = """
.bgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px 22px;margin-top:6px;}
.brow{display:flex;align-items:center;gap:14px;background:rgba(6,18,10,0.72);border:1px solid rgba(255,255,255,0.10);
  border-radius:14px;padding:9px 12px;backdrop-filter:blur(4px);}
.brow .ab{min-width:78px;height:44px;border-radius:9px;display:flex;align-items:center;justify-content:center;
  font-weight:800;font-size:21px;letter-spacing:0.02em;}
.brow .nm{font-weight:600;font-size:21px;line-height:1.15;color:#fff;}
.brow .nm small{display:block;font-weight:400;font-size:15px;color:rgba(255,255,255,0.6);margin-top:2px;}
.brow.blank .nm{color:rgba(255,255,255,0.55);font-style:italic;}
"""


def k_ballot(c):
    """Every party on a ballot, in INEC order, one tile each. Same size and
    weight for every party: only the colour chip differs."""
    out = ""
    if c.get("kicker"):
        out += f'<div class="kicker">{esc(c["kicker"])}</div>'
    out += f'<div class="disp" style="font-size:{px(c.get("size", 96))}px;margin-bottom:{c.get("gap", 22)}px">{rich(c["title"])}</div>'
    out += '<div class="bgrid">'
    for t in c["tickets"]:
        col, ink = t.get("colour", "#333"), t.get("ink", "#fff")
        cls = "brow blank" if not t.get("name") else "brow"
        name = esc(t.get("name") or t.get("blank", ""))
        sub = f'<small>{esc(t["sub"])}</small>' if t.get("sub") else ""
        out += (f'<div class="{cls}"><div class="ab" style="background:{col};color:{ink}">{esc(t["party"])}</div>'
                f'<div class="nm">{name}{sub}</div></div>')
    out += "</div>"
    if c.get("body"):
        out += f'<div class="body" style="font-size:24px;margin-top:22px">{rich(c["body"])}</div>'
    return out


KINDS = {"ballot": k_ballot, "cover": k_cover, "statement": k_statement, "stat": k_stat, "dates": k_dates,
         "list": k_list, "cta": k_cta, "countdown": k_countdown, "candidate": k_candidate}
EXTRA = DATES_CSS + LIST_CSS + COUNTDOWN_CSS + BALLOT_CSS


def build(kind, cfg, index, total, day, size):
    last = index == total - 1
    cfg = dict(cfg, _day=day)
    inner = logo_top() + f'<div class="stack">{KINDS[kind](cfg)}</div>' + footer(index, total, last)
    pos = cfg.get("pos", "50% 30%")
    if kind == "candidate":
        W, H = SIZES[size]
        css = BASE_CSS % dict(W=W, H=H, INK=INK, ACCENT=ACCENT, ACCENT_INK=ACCENT_INK, DIM=DIM, POS=pos)
        return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{font_css()}{css}{CAND_CSS % dict(POS=pos)}</style></head><body>{candidate_layers(cfg)}
<div class="grain"></div><div class="frame">{inner}</div></body></html>"""
    return page(inner, size=size, photo=cfg.get("photo"), pos=pos, extra_css=EXTRA, dim=cfg.get("dim", 0))


# ------------------------------------------------------------------ render
def render(markup, out_path, size="portrait"):
    W, H = SIZES[size]
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(markup)
        tmp = fh.name
    raw = out_path + ".raw.png"
    try:
        subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--hide-scrollbars", f"--force-device-scale-factor={SCALE}",
                        f"--window-size={W},{H}", "--virtual-time-budget=3000",
                        f"--screenshot={raw}", f"file://{tmp}"],
                       capture_output=True, timeout=120)
        if not os.path.exists(raw):
            raise RuntimeError(f"Chrome produced no screenshot for {out_path}")
        img = Image.open(raw).convert("RGB")
        if img.size != (W, H):
            img = img.resize((W, H), Image.LANCZOS)
        img.save(out_path, "PNG", optimize=True)
    finally:
        for p in (tmp, raw):
            if os.path.exists(p):
                os.remove(p)
    return out_path


def slide_names(total):
    if total == 1:
        return ["01-post.png"]
    names = ["01-cover.png"] + [f"{i + 2:02d}-slide-{i + 1}.png" for i in range(total - 2)]
    return names + [f"{total:02d}-cta.png"]


def render_post(slides, out_dir, *, day=None, size=None):
    """Render one day. `slides` is a list of (kind, cfg). Max 10, Instagram's ceiling."""
    size = size or ("square" if "--square" in sys.argv else "portrait")
    if len(slides) > 10:
        raise SystemExit(f"{len(slides)} slides. Instagram allows 10 at most.")
    out_dir = os.path.join(ROOT, out_dir)
    os.makedirs(out_dir, exist_ok=True)
    if size == "square":
        out_dir = os.path.join(out_dir, "square")
        os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        if re.match(r"\d\d-.*\.png$", f):
            os.remove(os.path.join(out_dir, f))
    names = slide_names(len(slides))
    for i, ((kind, cfg), name) in enumerate(zip(slides, names)):
        render(build(kind, cfg, i, len(slides), day, size), os.path.join(out_dir, name), size)
        print("  rendered", name)
    print(f"\n{len(slides)} slide(s) in {os.path.relpath(out_dir, ROOT)}")
