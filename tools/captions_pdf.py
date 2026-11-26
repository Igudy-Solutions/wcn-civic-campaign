#!/usr/bin/env python3
"""Put every written captions.md into one PDF for review.

    python3 tools/captions_pdf.py
writes "WCN Captions.pdf" in the repo root. Days run in posting order
(Day 57 first), then the Specials. Days still `planned` are left out.
Needs pandoc and Chrome.
"""
import base64
import glob
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import chrome  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "WCN Captions.pdf")


def written(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"\*\*Status\*\*\s*(\S+)", s)
    return m is None or m.group(1).lower() != "planned"


def md_html(path):
    return subprocess.run(["pandoc", "-f", "gfm", "-t", "html", path],
                          capture_output=True, text=True, check=True).stdout


def main():
    days = []
    for p in glob.glob(os.path.join(ROOT, "Daily Posts", "Day *", "captions.md")):
        n = int(re.match(r"Day (\d+)", os.path.basename(os.path.dirname(p))).group(1))
        if written(p):
            days.append((n, p))
    days.sort(key=lambda t: -t[0])
    specials = sorted(glob.glob(os.path.join(ROOT, "Specials", "*", "captions.md")))
    parts = [p for _, p in days] + specials

    font = base64.b64encode(open(os.path.join(ROOT, "fonts", "Sora.ttf"), "rb").read()).decode()
    logo = os.path.join(ROOT, "assets", "logo", "wcn-horizontal-forest.png")
    logo_uri = "data:image/png;base64," + base64.b64encode(open(logo, "rb").read()).decode()

    toc = "".join(f"<li>{os.path.basename(os.path.dirname(p))}</li>" for p in parts)
    body = "".join(f'<section>{md_html(p)}</section>' for p in parts)
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>WCN Captions</title><style>
@font-face{{font-family:Sora;src:url(data:font/ttf;base64,{font});font-weight:100 900;}}
@page{{size:A4;margin:18mm 16mm;}}
body{{font-family:Sora;color:#14201a;font-size:10.5pt;line-height:1.55;}}
.cover{{height:250mm;display:flex;flex-direction:column;justify-content:center;page-break-after:always;}}
.cover img{{width:70mm;}}
.cover h1{{font-size:34pt;line-height:1.1;margin:14mm 0 4mm;color:#0D421F;letter-spacing:-0.02em;}}
.cover .bar{{width:40mm;height:4mm;background:#D1DD25;margin-bottom:8mm;}}
.cover p{{margin:0 0 2mm;}}
.cover ol{{margin-top:8mm;columns:1;font-size:9.5pt;}}
section{{page-break-before:always;}}
h1{{color:#0D421F;font-size:20pt;border-left:6mm solid #D1DD25;padding-left:4mm;margin:0 0 4mm;}}
h2{{color:#0D421F;font-size:13pt;margin:6mm 0 2mm;border-bottom:1px solid #D1DD25;padding-bottom:1mm;}}
h3{{font-size:11pt;}}
table{{border-collapse:collapse;width:100%;font-size:9pt;margin:2mm 0;}}
th,td{{border:1px solid #cfd8d2;padding:4px 6px;text-align:left;vertical-align:top;}}
th{{background:#0D421F;color:#fff;}}
code{{font-size:9pt;background:#f1f4ef;padding:0 3px;}}
blockquote{{margin:0;padding-left:4mm;border-left:2px solid #D1DD25;}}
</style></head><body>
<div class="cover"><img src="{logo_uri}"><h1>Captions for<br>team review</h1><div class="bar"></div>
<p>Instagram: world_changersnetwork · X: worldchangernet</p>
<p>{len(parts)} posts, in posting order.</p><ol>{toc}</ol></div>
{body}</body></html>"""
    tmp = os.path.join(ROOT, ".captions_tmp.html")
    open(tmp, "w", encoding="utf-8").write(html)
    subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + tmp],
                   check=True, capture_output=True)
    os.remove(tmp)
    print("wrote", OUT, len(parts), "posts")


if __name__ == "__main__":
    main()
