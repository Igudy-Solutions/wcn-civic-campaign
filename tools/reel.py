#!/usr/bin/env python3
"""Election reel: a 34 second motion video for Instagram (and X).

1080x1350 (4:5, the Instagram feed size), 30 fps, H.264 MP4, no sound. Add a
sound in the app when posting.

Style: taken from the NectAll event videos Arkcore pointed to. Cream dotted
paper, tilted sticker labels with a hard ink shadow, letters that pop in one
by one, small doodles, cards and tickets as props, a dark subtitle box at the
bottom, slanted panel wipes between scenes, and a solid colour end card.
Their purple and yellow become WCN forest and lime. Sora only.

Facts are the Day 57 facts (INEC). No "Source:" on screen. Nobody named, and
nobody told who to vote for.

How it works: one HTML page holds every scene. `frame(t)` in the page places
each element for time t (no CSS animations, so every frame is exact).
Playwright steps t through the video and pipes screenshots into ffmpeg.

  python3 tools/reel.py            # full render -> Specials/Election Reel/
  python3 tools/reel.py --stills   # one PNG per scene, for checking

To change words, edit HTML_BODY. Timing lives in data-in / data-out (seconds).
Needs Node with Playwright, and ffmpeg.
"""

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import IG_ICON, X_ICON, IG_HANDLE, X_HANDLE  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(ROOT, "Specials", "Election Reel")
BUILD = os.path.join(OUT_DIR, "reel.html")
MP4 = os.path.join(OUT_DIR, "election-reel.mp4")
FPS = 30
DURATION = 34.0
W, H = 1080, 1350
STILLS = [3.6, 7.9, 12.2, 16.4, 20.8, 25.0, 28.4, 33.0]

LIME, FOREST, INK, CREAM, GREY = "#D1DD25", "#0D421F", "#06120A", "#F4F1E8", "#D8D4C7"


def u(*p):
    return "file://" + os.path.join(ROOT, *p)


CSS = f"""
@font-face{{font-family:Sora;src:url('{u('fonts','Sora.ttf')}');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{CREAM}}}
body{{font-family:Sora;color:{INK};position:relative}}
.scene{{position:absolute;inset:0;overflow:hidden;visibility:hidden;background:{CREAM};
  background-image:radial-gradient(rgba(6,18,10,.13) 1.7px,transparent 2px);background-size:30px 30px}}
.scene.dark{{background-color:{FOREST};background-image:radial-gradient(rgba(209,221,37,.22) 1.7px,transparent 2px)}}
.a{{position:absolute;will-change:transform}}
.tag{{font-weight:800;text-transform:uppercase;letter-spacing:-.01em;border:5px solid {INK};
  box-shadow:9px 9px 0 {INK};border-radius:10px;padding:.13em .34em .1em;line-height:1;white-space:nowrap;
  transform-origin:left center}}
.tag .c{{display:inline-block;white-space:pre}}
.w{{background:#fff;color:{INK}}} .l{{background:{LIME};color:{FOREST}}} .g{{background:{FOREST};color:#fff}}
.card{{border:5px solid {INK};box-shadow:13px 13px 0 {INK};border-radius:24px;background:#fff;overflow:hidden}}
.photo{{padding:14px;background:#fff}}
.photo div{{width:100%;height:100%;border-radius:12px;border:4px solid {INK};background-size:cover;background-position:center}}
.cap{{position:absolute;left:50%;top:1150px;transform:translateX(-50%);background:{INK};color:#fff;
  font-weight:600;font-size:30px;line-height:1.38;padding:16px 28px;border-radius:12px;text-align:center;width:max-content;max-width:860px}}
#logo{{position:absolute;left:60px;top:56px;height:74px;z-index:30}}
.sweep{{position:absolute;top:-10%;height:120%;width:150%;left:-25%;z-index:40;background:{FOREST};
  border-left:10px solid {INK};border-right:10px solid {INK};transform:translateX(-130%) skewX(-16deg)}}
.sweep.l{{background:{LIME}}}
.hdr{{background:{FOREST};color:#fff;display:flex;align-items:center;justify-content:space-between;
  padding:22px 34px;border-bottom:5px solid {INK};font-weight:700;font-size:34px}}
.chip{{background:{LIME};color:{FOREST};border:4px solid {INK};border-radius:999px;padding:4px 18px;font-weight:800;font-size:28px}}
.ticket{{border:5px solid {INK};box-shadow:13px 13px 0 {INK};border-radius:20px;display:flex;overflow:hidden}}
.ticket .main{{flex:1;padding:30px 38px}}
.ticket .k{{font-weight:700;font-size:24px;letter-spacing:.14em;text-transform:uppercase;opacity:.8}}
.ticket .d{{font-weight:800;font-size:66px;letter-spacing:-.03em;line-height:1.05;margin:8px 0 10px;text-transform:uppercase}}
.ticket .o{{font-weight:600;font-size:30px}}
.ticket .stub{{width:150px;border-left:5px dashed {INK};display:flex;align-items:center;justify-content:center}}
.barcode{{width:74px;height:190px;background:repeating-linear-gradient(0deg,{INK} 0 5px,transparent 5px 9px,{INK} 9px 11px,transparent 11px 17px)}}
.stamp{{border:7px solid {FOREST};color:{FOREST};border-radius:14px;padding:6px 22px;font-weight:800;
  font-size:52px;letter-spacing:.04em;background:rgba(209,221,37,.92)}}
.soc{{display:flex;align-items:center;gap:16px;font-weight:700;font-size:36px;color:#fff;background:{INK};
  border:5px solid {INK};box-shadow:8px 8px 0 {LIME};border-radius:16px;padding:14px 26px}}
.soc svg{{width:46px;height:46px}}
.bar{{height:46px;border:5px solid {INK};border-radius:999px;background:#fff;overflow:hidden}}
.bar i{{display:block;height:100%;width:0;background:{LIME};border-right:5px solid {INK}}}
"""

STAR = (f'<svg viewBox="0 0 100 100" width="{{s}}" height="{{s}}"><path d="M50 4C55 38 62 45 96 50C62 55 55 62 50 96'
        f'C45 62 38 55 4 50C38 45 45 38 50 4Z" fill="{{c}}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/></svg>')
RING = (f'<svg viewBox="0 0 100 100" width="{{s}}" height="{{s}}"><circle cx="50" cy="50" r="40" fill="{FOREST}" '
        f'stroke="{INK}" stroke-width="7"/><circle cx="50" cy="50" r="16" fill="{CREAM}" stroke="{INK}" stroke-width="6"/></svg>')
SQUIG = (f'<svg viewBox="0 0 160 50" width="{{s}}" height="{{h}}"><polyline points="6,38 30,12 54,38 78,12 102,38 126,12 150,38" '
         f'fill="none" stroke="{FOREST}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def person(color, tick=False):
    t = (f'<circle cx="96" cy="26" r="20" fill="{LIME}" stroke="{INK}" stroke-width="5"/>'
         f'<polyline points="86,26 94,34 107,18" fill="none" stroke="{INK}" stroke-width="6" '
         f'stroke-linecap="round" stroke-linejoin="round"/>') if tick else ""
    return (f'<svg viewBox="0 0 120 150" width="120" height="150"><circle cx="60" cy="42" r="27" fill="{color}" '
            f'stroke="{INK}" stroke-width="5"/><path d="M14 146V120a46 40 0 0 1 92 0V146Z" fill="{color}" '
            f'stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>{t}</svg>')


def star(left, top, s=90, c=LIME, at=0.0, out=99):
    return (f'<div class="a" data-fx="doodle" data-in="{at}" data-out="{out}" '
            f'style="left:{left}px;top:{top}px">{STAR.format(s=s, c=c)}</div>')


def ring(left, top, s=80, at=0.0, out=99):
    return (f'<div class="a" data-fx="doodle" data-in="{at}" data-out="{out}" '
            f'style="left:{left}px;top:{top}px">{RING.format(s=s)}</div>')


def squig(left, top, s=150, at=0.0, out=99):
    return (f'<div class="a" data-fx="doodle" data-in="{at}" data-out="{out}" '
            f'style="left:{left}px;top:{top}px">{SQUIG.format(s=s, h=int(s * 50 / 160))}</div>')


def tag(text, cls, size, left, top, r, at, out, fx="type"):
    return (f'<div class="a tag {cls}" data-fx="{fx}" data-r="{r}" data-in="{at}" data-out="{out}" '
            f'style="left:{left}px;top:{top}px;font-size:{size}px">{text}</div>')


def cap(text, at, out):
    return f'<div class="cap" data-fx="cap" data-in="{at}" data-out="{out}">{text}</div>'


def photo(img, left, top, w, h, r, at, out):
    return (f'<div class="a card photo" data-fx="slideup" data-r="{r}" data-in="{at}" data-out="{out}" '
            f'style="left:{left}px;top:{top}px;width:{w}px;height:{h}px">'
            f'<div data-fx="kb" data-in="{at}" data-out="{out}" '
            f'style="background-image:url(\'{u("images", "ai", img)}\')"></div></div>')


def icon(svg):
    return svg.format(c=LIME)


# Scenes: (start, end). Cuts sit under a sweep, so scenes overlap by 0.1 s.
S = [(0, 4.3), (4.2, 8.7), (8.6, 12.9), (12.8, 17.1), (17.0, 21.5), (21.4, 25.7), (25.6, 29.4), (29.3, 99)]


def scene(i, inner, dark=False):
    a, b = S[i]
    return (f'<section class="scene{" dark" if dark else ""}" data-in="{a}" data-out="{b}">'
            f'{inner}</section>')


def people():
    out = []
    for i in range(10):
        voted = i in (1, 5, 8)
        col, row = i % 5, i // 5
        out.append(f'<div class="a" data-fx="pop" data-r="0" data-in="{5.6 + i * 0.07:.2f}" data-out="{S[1][1]}" '
                   f'style="left:{90 + col * 186}px;top:{700 + row * 200}px">'
                   f'{person(LIME if voted else GREY, tick=voted)}</div>')
    return "".join(out)


def ticket(cls, kick, date, offices, left, top, r, at, out):
    return (f'<div class="a ticket {cls}" data-fx="slideup" data-r="{r}" data-in="{at}" data-out="{out}" '
            f'style="left:{left}px;top:{top}px;width:860px">'
            f'<div class="main"><div class="k">{kick}</div><div class="d">{date}</div>'
            f'<div class="o">{offices}</div></div><div class="stub"><div class="barcode"></div></div></div>')


e = S  # short alias for the ends below
HTML_BODY = f"""
<img id="logo" src="{u('assets','logo','wcn-horizontal-forest.png')}"/>
{scene(0, f'''
  {tag("Nigeria decides 2027", "g", 34, 96, 230, -3, 0.15, e[0][1])}
  <div class="a tag l" data-fx="countpop" data-r="-4" data-in="0.35" data-out="{e[0][1]}" data-from="99" data-to="57" data-dur="1.3"
       style="left:90px;top:310px;font-size:300px">57</div>
  {tag("days to", "w", 100, 110, 690, 2, 1.1, e[0][1])}
  {tag("election day.", "l", 84, 130, 850, -2, 1.35, e[0][1])}
  {star(820, 330, 110, LIME, 0.9)}{ring(890, 560, 90, 1.2)}{squig(700, 720, 170, 1.4)}{star(930, 1010, 60, FOREST, 1.6)}
  {cap("Nigeria votes on Saturday 16 January 2027.", 1.9, e[0][1])}
''')}
{scene(1, f'''
  {tag("In 2023,", "w", 64, 90, 210, -3, e[1][0] + 0.3, e[1][1])}
  {tag("73% of us", "l", 124, 90, 310, 2, e[1][0] + 0.5, e[1][1])}
  {tag("stayed home.", "g", 84, 230, 500, -2, e[1][0] + 0.9, e[1][1])}
  {people()}
  {star(900, 200, 80, LIME, e[1][0] + 0.6)}
  {cap("About 93 million registered. About 25 million voted.", e[1][0] + 1.8, e[1][1])}
''')}
{scene(2, f'''
  {photo("ai-01-polling-queue.png", 140, 170, 800, 470, -2, e[2][0] + 0.2, e[2][1])}
  {tag("Turnout", "w", 60, 90, 690, -3, e[2][0] + 0.6, e[2][1])}
  <div class="a tag l" data-fx="count" data-r="2" data-in="{e[2][0] + 0.8}" data-out="{e[2][1]}" data-from="0" data-to="26.7" data-dec="1" data-suffix="%" data-dur="1.4"
       style="left:90px;top:780px;font-size:170px">0%</div>
  {tag("Lowest since 1999.", "g", 50, 300, 1000, -2, e[2][0] + 1.6, e[2][1])}
  {star(900, 690, 90, LIME, e[2][0] + 1.0)}{ring(960, 120, 64, e[2][0] + 0.5)}
  {cap("The race was won by about 1.8 million votes.<br/>68 million registered voters stayed home.", e[2][0] + 2.0, e[2][1])}
''')}
{scene(3, f'''
  {tag("Now, 2027.", "w", 76, 90, 200, -2, e[3][0] + 0.3, e[3][1])}
  <div class="a card" data-fx="slideup" data-r="1.5" data-in="{e[3][0] + 0.6}" data-out="{e[3][1]}" style="left:110px;top:350px;width:860px">
    <div class="hdr"><span>Voter register</span><span class="chip">2027</span></div>
    <div style="padding:30px 40px 40px">
      <div data-fx="count" data-in="{e[3][0] + 0.9}" data-out="{e[3][1]}" data-from="0" data-to="103.4" data-dec="1" data-suffix="M" data-dur="1.5"
           style="font-weight:800;font-size:200px;letter-spacing:-.05em;line-height:1;color:{FOREST}">0M</div>
      <div style="font-weight:700;font-size:44px;margin:6px 0 30px">registered voters</div>
      <div class="bar"><i data-fx="bar" data-in="{e[3][0] + 0.9}" data-out="99" data-to="100" data-dur="1.5"></i></div>
    </div>
  </div>
  {tag("That includes you.", "l", 60, 260, 880, -4, e[3][0] + 2.0, e[3][1], fx="stamp")}
  {star(880, 230, 90, LIME, e[3][0] + 0.9)}{squig(110, 1000, 150, e[3][0] + 2.2)}
  {cap("103.4 million Nigerians are registered for 2027.", e[3][0] + 2.2, e[3][1])}
''')}
{scene(4, f'''
  {tag("Two Saturdays.", "w", 82, 90, 190, -2, e[4][0] + 0.3, e[4][1])}
  {tag("Five offices.", "g", 82, 260, 320, 2, e[4][0] + 0.6, e[4][1])}
  {ticket("l", "Election day one", "Sat 16 Jan 2027", "President · Senate · House of Reps", 90, 500, -2, e[4][0] + 1.0, e[4][1])}
  {ticket("w", "Election day two", "Sat 06 Feb 2027", "Governor · State House of Assembly", 120, 820, 2, e[4][0] + 1.4, e[4][1])}
  {star(900, 330, 80, LIME, e[4][0] + 0.8)}{ring(940, 420, 64, e[4][0] + 1.1)}
  {cap("Mark both dates now.", e[4][0] + 2.0, e[4][1])}
''')}
{scene(5, f'''
  {tag("No PVC?", "w", 116, 90, 190, -3, e[5][0] + 0.3, e[5][1])}
  {tag("No vote.", "l", 116, 330, 360, 2, e[5][0] + 0.6, e[5][1])}
  <div class="a card" data-fx="slideup" data-r="-3" data-in="{e[5][0] + 1.0}" data-out="{e[5][1]}" style="left:150px;top:590px;width:780px;height:400px">
    <div class="hdr" style="color:{LIME}"><span>YOUR PVC</span><span class="chip">VOTER</span></div>
    <div style="display:flex;gap:40px;padding:34px 40px">
      <div style="width:170px;height:200px;border:5px solid {INK};border-radius:16px;background:{CREAM};display:flex;align-items:flex-end;justify-content:center;overflow:hidden">{person(LIME)}</div>
      <div style="flex:1;display:flex;flex-direction:column;gap:20px;padding-top:10px">
        <div style="height:26px;width:90%;background:{GREY};border-radius:8px"></div>
        <div style="height:26px;width:70%;background:{GREY};border-radius:8px"></div>
        <div style="height:26px;width:80%;background:{GREY};border-radius:8px"></div>
        <div style="height:60px;width:70%;margin-top:6px;background:repeating-linear-gradient(90deg,{INK} 0 5px,transparent 5px 9px,{INK} 9px 11px,transparent 11px 16px)"></div>
      </div>
    </div>
  </div>
  <div class="a stamp" data-fx="stamp" data-r="-9" data-in="{e[5][0] + 1.9}" data-out="{e[5][1]}" style="left:520px;top:900px">COLLECTED ✓</div>
  {star(120, 520, 80, LIME, e[5][0] + 1.2)}
  {cap("Collect yours at your INEC LGA office.<br/>In person. Nobody can do it for you.", e[5][0] + 2.1, e[5][1])}
''')}
{scene(6, f'''
  {photo("ai-02-inked-thumb.png", 130, 160, 820, 560, 2, e[6][0] + 0.2, e[6][1])}
  {tag("Your vote.", "w", 104, 90, 770, -3, e[6][0] + 0.7, e[6][1])}
  {tag("Your voice.", "l", 104, 250, 920, 2, e[6][0] + 1.0, e[6][1])}
  {star(890, 700, 90, LIME, e[6][0] + 1.2)}
  {cap("Don't sell it. Don't waste it.", e[6][0] + 1.7, e[6][1])}
''')}
{scene(7, f'''
  <div class="a card" data-fx="slideup" data-r="-2" data-in="{e[7][0] + 0.3}" data-out="99" style="left:170px;top:230px;width:740px;height:400px;background:{CREAM};display:flex;align-items:center;justify-content:center">
    <img src="{u('assets','logo','wcn-horizontal-forest.png')}" style="width:600px"/>
  </div>
  {tag("Show up. 16 Jan 2027.", "l", 52, 120, 590, -3, e[7][0] + 0.8, 99)}
  {tag("Follow for one post a day", "w", 34, 250, 780, 2, e[7][0] + 1.3, 99)}
  <div class="a" data-fx="pop" data-r="0" data-in="{e[7][0] + 1.7}" data-out="99" style="left:250px;top:900px;display:flex;flex-direction:column;gap:26px">
    <span class="soc">{icon(IG_ICON)}{IG_HANDLE}</span><span class="soc">{icon(X_ICON)}{X_HANDLE}</span>
  </div>
  {star(880, 170, 100, LIME, e[7][0] + 1.0)}{star(110, 1060, 70, LIME, e[7][0] + 1.5)}
''', dark=True)}
""" + "".join(
    f'<div class="sweep{" l" if i % 2 else ""}" data-fx="sweep" data-at="{S[i][0] + 0.05}"></div>'
    for i in range(1, len(S)))

JS = """
const cl=x=>Math.max(0,Math.min(1,x));
const c1=1.70158,c3=c1+1;
const backOut=x=>x<=0?0:x>=1?1:1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);
const backIn=x=>c3*x*x*x-c1*x*x;
const outExpo=x=>x>=1?1:1-Math.pow(2,-10*x);
const inOut=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
// split type tags into letters
for(const el of document.querySelectorAll('[data-fx=type]')){
  el.innerHTML=[...el.textContent].map(ch=>`<span class="c">${ch}</span>`).join('');
}
const els=[...document.querySelectorAll('[data-fx]')];
const scenes=[...document.querySelectorAll('.scene')];
const logo=document.getElementById('logo');
function frame(t){
  for(const s of scenes){const a=+s.dataset.in,b=+s.dataset.out;s.style.visibility=(t>=a&&t<b)?'visible':'hidden';}
  logo.style.visibility=t<29.35?'visible':'hidden';
  for(const el of els){
    const fx=el.dataset.fx, a=+el.dataset.in, b=+el.dataset.out, r=+(el.dataset.r||0);
    const out=backIn(cl((t-(b-0.3))/0.3));      // exit: shrink away in the last 0.3 s
    if(fx==='type'){
      const p=cl((t-a)/0.32);
      el.style.transform=`rotate(${r}deg) scaleX(${outExpo(p)*(1-out)}) scaleY(${1-out})`;
      el.style.opacity=t<a?0:1;
      [...el.children].forEach((c,i)=>{
        const q=backOut(cl((t-a-0.18-i*0.028)/0.32));
        c.style.transform=`translateY(${(1-q)*55}%) scale(${0.4+0.6*q})`; c.style.opacity=cl(q*2);
      });
    } else if(fx==='pop'||fx==='doodle'){
      const p=backOut(cl((t-a)/0.45));
      let rot=r+(1-p)*-25, fl=0;
      if(fx==='doodle'){rot+=Math.sin(t*1.6+a)*10; fl=Math.sin(t*2+a*3)*6;}
      el.style.transform=`translateY(${fl}px) rotate(${rot}deg) scale(${Math.max(0,p*(1-out))})`;
      el.style.transformOrigin='center';
    } else if(fx==='slideup'){
      const p=backOut(cl((t-a)/0.6));
      el.style.transform=`translateY(${(1-p)*900}px) rotate(${r+(1-p)*8}deg) scale(${1-out})`;
    } else if(fx==='stamp'){
      const p=cl((t-a)/0.28);
      el.style.transform=`rotate(${r}deg) scale(${(2.6-1.6*outExpo(p))*(1-out)})`;
      el.style.opacity=t<a?0:cl(p*3);
    } else if(fx==='count'||fx==='countpop'){
      const d=+el.dataset.dur,f=+el.dataset.from,to=+el.dataset.to,dec=+(el.dataset.dec||0);
      el.textContent=(f+(to-f)*outExpo(cl((t-a)/d))).toFixed(dec)+(el.dataset.suffix||'');
      if(el.classList.contains('tag')){
        const p=backOut(cl((t-a)/0.5));
        el.style.transform=`rotate(${r+(1-p)*-12}deg) scale(${Math.max(0,p*(1-out))})`;
      }
    } else if(fx==='bar'){
      el.style.width=(+el.dataset.to*outExpo(cl((t-a)/+el.dataset.dur)))+'%';
    } else if(fx==='kb'){
      el.style.transform=`scale(${1.05+0.1*cl((t-a)/(b-a))})`;
    } else if(fx==='cap'){
      const p=outExpo(cl((t-a)/0.5));
      el.style.opacity=Math.min(p,1-cl((t-(b-0.25))/0.25));
      el.style.transform=`translateX(-50%) translateY(${(1-p)*30}px)`;
    } else if(fx==='sweep'){
      const at=+el.dataset.at, p=cl((t-(at-0.4))/0.8);
      el.style.transform=`translateX(${-130+260*inOut(p)}%) skewX(-16deg)`;
    }
  }
}
window.frame=frame;
"""


def build_html():
    os.makedirs(OUT_DIR, exist_ok=True)
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body>{HTML_BODY}<script>{JS}</script></body></html>")
    with open(BUILD, "w", encoding="utf-8") as fh:
        fh.write(html)


NODE = r"""
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const [,, html, out, fps, dur, mode, w, h, stills] = process.argv;
(async () => {
  const opts = process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {};
  const b = await chromium.launch({ ...opts, args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await p.goto('file://' + html);
  await p.evaluate(async () => { await document.fonts.ready;
    await Promise.all([...document.images].map(i => i.decode().catch(()=>{}))); });
  await p.waitForTimeout(800);
  if (mode === 'stills') {
    for (const [i, t] of stills.split(',').map(Number).entries()) {
      await p.evaluate(t => frame(t), t);
      await p.screenshot({ path: `${out}/still-${i + 1}.png` });
    }
  } else {
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', fps,
      '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
      '-preset', 'medium', '-movflags', '+faststart', '-r', fps, out], { stdio: ['pipe', 'inherit', 'inherit'] });
    const n = Math.round(+fps * +dur);
    for (let f = 0; f < n; f++) {
      await p.evaluate(t => frame(t), f / +fps);
      const buf = await p.screenshot({ type: 'jpeg', quality: 94 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 150 === 0) process.stdout.write(`  frame ${f}/${n}\n`);
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
  }
  await b.close();
})();
"""


def main():
    build_html()
    stills = "--stills" in sys.argv
    js = os.path.join(OUT_DIR, ".render.js")
    with open(js, "w") as fh:
        fh.write(NODE)
    target = OUT_DIR if stills else MP4
    try:
        subprocess.run(["node", js, BUILD, target, str(FPS), str(DURATION),
                        "stills" if stills else "video", str(W), str(H),
                        ",".join(map(str, STILLS))], check=True)
    finally:
        os.remove(js)
    print("wrote", target)


if __name__ == "__main__":
    main()
