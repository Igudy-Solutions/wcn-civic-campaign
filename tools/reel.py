#!/usr/bin/env python3
"""Election reel: a voiced motion video for Instagram Reels (and X).

1080x1920 (1080p vertical), 30 fps, H.264 + AAC MP4.

Look: WCN's own take on neo-brutalism. Full photos of people voting under a
forest tint, with hard-edged sticker labels on top (square corners, ink
border, lime shadow), civic marks instead of doodles (thumbprint, tick box,
arrow), calendar tiles for the dates, a scrolling lime ticker, word-by-word
subtitles on an ink strip, and soft cross-fades between scenes. Sora only.

Facts are the Day 57 facts (INEC). No "Source:" on screen. Nobody named, and
nobody told who to vote for.

Steps:
  python3 tools/voiceover.py       # writes vo/NN.wav + durations.json
  python3 tools/reel.py --stills   # one PNG per scene, for checking
  python3 tools/reel.py            # full render with voice and music bed

Scenes are timed to the voice: each scene lasts its line plus LEAD + TAIL.
Change words in SCENES below and in tools/voiceover.py (same order).
Needs Node with Playwright, ffmpeg, numpy, soundfile.
"""

import json
import os
import subprocess
import sys

import numpy as np
import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_carousel import IG_ICON, X_ICON, IG_HANDLE, X_HANDLE  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(ROOT, "Specials", "Election Reel")
VO_DIR = os.path.join(OUT_DIR, "vo")
BUILD = os.path.join(OUT_DIR, "reel.html")
MP4 = os.path.join(OUT_DIR, "election-reel.mp4")
FPS = 30
W, H = 1080, 1920
LEAD, TAIL, END_HOLD = 0.55, 0.85, 2.6
LIME, FOREST, INK, GREY = "#D1DD25", "#0D421F", "#06120A", "#C9CDBF"


def u(*p):
    return "file://" + os.path.join(ROOT, *p)


# ------------------------------------------------------------------ timing
with open(os.path.join(VO_DIR, "durations.json")) as fh:
    VO = json.load(fh)
S, t = [], 0.0
for i, d in enumerate(VO):
    length = LEAD + d + TAIL + (END_HOLD if i == len(VO) - 1 else 0)
    S.append((round(t, 2), round(t + length, 2)))
    t += length
DURATION = round(t, 2)

# ------------------------------------------------------------------ style
CSS = f"""
@font-face{{font-family:Sora;src:url('{u('fonts','Sora.ttf')}');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{FOREST}}}
body{{font-family:Sora;color:{INK};position:relative}}
.scene{{position:absolute;inset:0;overflow:hidden;visibility:hidden;background:{FOREST}}}
.bg{{position:absolute;inset:-3%;background-size:cover;background-position:center;
  filter:grayscale(1) contrast(1.15) brightness(1.05)}}
.tint{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,66,31,.62),rgba(13,66,31,.45) 35%,
  rgba(9,46,22,.82) 70%,rgba(6,18,10,.94))}}
.tint::after{{content:"";position:absolute;inset:0;background:{LIME};mix-blend-mode:soft-light;opacity:.35}}
.a{{position:absolute;will-change:transform}}
.tag{{font-weight:800;text-transform:uppercase;letter-spacing:-.015em;border:6px solid {INK};
  box-shadow:12px 12px 0 {LIME};padding:.14em .36em .1em;line-height:1;white-space:nowrap;transform-origin:left center}}
.tag .c{{display:inline-block;white-space:pre}}
.w{{background:#fff;color:{INK}}} .l{{background:{LIME};color:{FOREST};box-shadow:12px 12px 0 {INK}}}
.k{{background:{INK};color:{LIME};border-color:{LIME}}}
.box{{border:6px solid {INK};box-shadow:16px 16px 0 {LIME};background:#fff}}
#logo{{position:absolute;left:60px;top:120px;height:84px;z-index:30;filter:drop-shadow(0 4px 14px rgba(0,0,0,.4))}}
.sub{{position:absolute;left:60px;right:60px;top:1395px;z-index:20}}
.sub p{{display:inline;background:{INK};color:#fff;font-weight:700;font-size:44px;line-height:1.62;
  padding:6px 16px;box-decoration-break:clone;-webkit-box-decoration-break:clone;border-left:12px solid {LIME}}}
.sub .wd{{opacity:.18}}
.ticker{{position:absolute;left:-40px;width:1160px;top:1660px;height:84px;background:{LIME};border:6px solid {INK};
  transform:rotate(-3deg);overflow:hidden;z-index:25}}
.ticker div{{position:absolute;top:12px;white-space:nowrap;font-weight:800;font-size:44px;color:{FOREST};
  text-transform:uppercase;letter-spacing:.02em}}
.shut{{position:absolute;top:0;height:100%;z-index:40;border-left:6px solid {INK};border-right:6px solid {INK}}}
.hdr{{background:{FOREST};color:#fff;display:flex;align-items:center;justify-content:space-between;
  padding:24px 36px;border-bottom:6px solid {INK};font-weight:700;font-size:38px}}
.chip{{background:{LIME};color:{FOREST};border:5px solid {INK};padding:4px 20px;font-weight:800;font-size:30px}}
.cal{{width:430px;border:6px solid {INK};box-shadow:16px 16px 0 {LIME};background:#fff;text-align:center}}
.cal .m{{background:{FOREST};color:{LIME};font-weight:800;font-size:40px;padding:16px 0;border-bottom:6px solid {INK};letter-spacing:.06em}}
.cal .n{{font-weight:800;font-size:220px;line-height:1;letter-spacing:-.06em;color:{FOREST};padding-top:18px}}
.cal .d{{font-weight:800;font-size:40px;letter-spacing:.14em}}
.cal .o{{font-weight:600;font-size:28px;line-height:1.3;padding:14px 22px 26px;color:{INK}}}
.bar{{height:50px;border:6px solid {INK};background:#fff;overflow:hidden}}
.bar i{{display:block;height:100%;width:0;background:{LIME};border-right:6px solid {INK}}}
.stamp{{border:8px solid {FOREST};color:{FOREST};padding:8px 24px;font-weight:800;font-size:58px;
  letter-spacing:.04em;background:{LIME}}}
.soc{{display:flex;align-items:center;gap:18px;font-weight:700;font-size:42px;color:#fff;background:{INK};
  border:6px solid {LIME};padding:16px 28px}}
.soc svg{{width:52px;height:52px}}
"""

# civic marks, replacing generic doodles
THUMB = (f'<svg viewBox="0 0 100 120" width="{{s}}" height="{{h}}" fill="none" stroke="{{c}}" stroke-width="5" '
         f'stroke-linecap="round"><path d="M50 10C28 10 14 28 14 52v20"/><path d="M50 22C34 22 26 36 26 52v34"/>'
         f'<path d="M50 34C41 34 38 42 38 52v46"/><path d="M50 46v62"/><path d="M62 98V52c0-10-3-18-12-18"/>'
         f'<path d="M74 86V52c0-16-8-30-24-30"/><path d="M86 68V52c0-24-14-42-36-42"/></svg>')
TICK = (f'<svg viewBox="0 0 100 100" width="{{s}}" height="{{s}}"><rect x="8" y="8" width="84" height="84" fill="#fff" '
        f'stroke="{INK}" stroke-width="8"/><polyline points="24,52 42,70 78,30" fill="none" stroke="{FOREST}" '
        f'stroke-width="13" stroke-linecap="square"/></svg>')
ARROW = (f'<svg viewBox="0 0 120 60" width="{{s}}" height="{{h}}"><path d="M4 30H96M74 8l26 22-26 22" fill="none" '
         f'stroke="{LIME}" stroke-width="10" stroke-linecap="square"/></svg>')


def mark(kind, left, top, s, at, c=LIME):
    svg = {"thumb": THUMB.format(s=s, h=int(s * 1.2), c=c), "tick": TICK.format(s=s),
           "arrow": ARROW.format(s=s, h=s // 2)}[kind]
    return f'<div class="a" data-fx="mark" data-in="{at}" data-out="99" style="left:{left}px;top:{top}px">{svg}</div>'


def tag(text, cls, size, left, top, r, at, out, fx="type"):
    return (f'<div class="a tag {cls}" data-fx="{fx}" data-r="{r}" data-in="{at}" data-out="{out}" '
            f'style="left:{left}px;top:{top}px;font-size:{size}px">{text}</div>')


def icon(svg):
    return svg.format(c=LIME)


# One entry per scene: photo, subtitle (what the voice says), and the layout.
# `a` is the scene start, `b` its end; positions are px on the 1080x1920 frame.
def scenes():
    out = []

    def sc(i, photo, sub, body, pos="center"):
        a, b = S[i]
        words = "".join(f'<span class="wd">{w} </span>' for w in sub.split())
        out.append(
            f'<section class="scene" data-in="{a}" data-out="{b}">'
            f'<div class="bg" data-fx="kb" data-in="{a}" data-out="{b}" style="background-image:url(\'{u("images", "ai", photo)}\');background-position:{pos}"></div>'
            f'<div class="tint"></div>{body(a, b)}'
            f'<div class="sub" data-fx="words" data-in="{a + LEAD}" data-dur="{VO[i]}" data-out="{b}"><p>{words}</p></div>'
            f'</section>')

    sc(0, "ai-06-walk-to-vote.png", "57 days. Nigeria votes on Saturday, 16 January.", lambda a, b: f'''
      {tag("Nigeria decides 2027", "k", 40, 80, 330, -3, a + .15, b)}
      <div class="a tag l" data-fx="countpop" data-r="-3" data-in="{a + .3}" data-out="{b}" data-from="99" data-to="57" data-dur="1.4"
           style="left:80px;top:440px;font-size:360px">57</div>
      {tag("days to", "w", 116, 100, 900, 2, a + 1.0, b)}
      {tag("election day.", "w", 96, 120, 1080, -2, a + 1.25, b)}
      {mark("thumb", 790, 520, 170, a + .9)}{mark("arrow", 820, 1240, 150, a + 1.6)}''')

    sc(1, "ai-01-polling-queue.png", "In 2023, 73% of registered voters stayed home.", lambda a, b: f'''
      {tag("In 2023,", "w", 72, 80, 330, -3, a + .3, b)}
      {tag("73% of us", "l", 140, 80, 450, 2, a + .55, b)}
      {tag("stayed home.", "k", 96, 180, 680, -2, a + .95, b)}
      {"".join(f'<div class="a" data-fx="mark" data-in="{a + 1.4 + j * .08:.2f}" data-out="99" style="left:{110 + (j % 5) * 180}px;top:{900 + (j // 5) * 200}px">'
               + THUMB.format(s=120, h=144, c=(LIME if j in (1, 5, 8) else "rgba(255,255,255,.45)")) + '</div>' for j in range(10))}''')

    sc(2, "ai-07-ballot-box.png", "Turnout was 26.7%, the lowest since 1999. The race was won by about 1.8 million votes.", lambda a, b: f'''
      {tag("Turnout, 2023", "w", 64, 80, 340, -3, a + .3, b)}
      <div class="a tag l" data-fx="count" data-r="2" data-in="{a + .6}" data-out="{b}" data-from="0" data-to="26.7" data-dec="1" data-suffix="%" data-dur="1.6"
           style="left:80px;top:460px;font-size:210px">0%</div>
      <div class="a" data-fx="pop" data-r="0" data-in="{a + .8}" data-out="{b}" style="left:90px;top:760px;width:900px">
        <div class="bar"><i data-fx="bar" data-in="{a + .8}" data-out="99" data-to="26.7" data-dur="1.6"></i></div></div>
      {tag("Lowest since 1999.", "k", 62, 140, 880, -2, a + 2.0, b)}
      {tag("Won by ~1.8M votes.", "w", 62, 200, 1040, 2, a + 4.6, b)}
      {mark("tick", 860, 300, 120, a + 1.2)}''')

    sc(3, "ai-05-bvas-accreditation.png", "Now, over 103 million Nigerians are registered. That includes you.", lambda a, b: f'''
      {tag("Now, 2027.", "w", 84, 80, 320, -2, a + .3, b)}
      <div class="a box" data-fx="slideup" data-r="1.5" data-in="{a + .6}" data-out="{b}" style="left:90px;top:490px;width:900px">
        <div class="hdr"><span>Voter register</span><span class="chip">2027</span></div>
        <div style="padding:30px 40px 44px">
          <div data-fx="count" data-in="{a + .9}" data-out="{b}" data-from="0" data-to="103.4" data-dec="1" data-suffix="M" data-dur="1.6"
               style="font-weight:800;font-size:220px;letter-spacing:-.05em;line-height:1;color:{FOREST}">0M</div>
          <div style="font-weight:700;font-size:48px;margin:8px 0 30px">registered voters</div>
          <div class="bar"><i data-fx="bar" data-in="{a + .9}" data-out="99" data-to="100" data-dur="1.6"></i></div>
        </div></div>
      <div class="a stamp" data-fx="stamp" data-r="-6" data-in="{a + LEAD + 3.2}" data-out="{b}" style="left:330px;top:1120px">THAT INCLUDES YOU</div>''')

    sc(4, "ai-04-friends-debate.png", "Mark two Saturdays. January 16, for President and the National Assembly. February 6, for Governor and State Assembly.", lambda a, b: f'''
      {tag("Mark two Saturdays.", "w", 70, 70, 320, -2, a + .3, b)}
      <div class="a cal" data-fx="slideup" data-r="-3" data-in="{a + 1.2}" data-out="{b}" style="left:70px;top:500px">
        <div class="m">JAN 2027</div><div class="n">16</div><div class="d">SATURDAY</div>
        <div class="o">President, Senate,<br/>House of Reps</div></div>
      <div class="a cal" data-fx="slideup" data-r="3" data-in="{a + LEAD + 4.3}" data-out="{b}" style="left:570px;top:560px">
        <div class="m">FEB 2027</div><div class="n">06</div><div class="d">SATURDAY</div>
        <div class="o">Governor, State<br/>House of Assembly</div></div>''')

    sc(5, "ai-08-pvc-collection.png", "No PVC, no vote. Collect yours at your INEC office, in person.", lambda a, b: f'''
      {tag("No PVC?", "w", 130, 80, 320, -3, a + .3, b)}
      {tag("No vote.", "l", 130, 300, 500, 2, a + .7, b)}
      <div class="a box" data-fx="slideup" data-r="-3" data-in="{a + 1.6}" data-out="{b}" style="left:140px;top:770px;width:800px;height:440px">
        <div class="hdr" style="color:{LIME}"><span>YOUR PVC</span><span class="chip">VOTER</span></div>
        <div style="display:flex;gap:40px;padding:34px 40px">
          <div style="width:180px;height:220px;border:6px solid {INK};background:#EEF0E2;display:flex;align-items:center;justify-content:center">{THUMB.format(s=110, h=132, c=FOREST)}</div>
          <div style="flex:1;display:flex;flex-direction:column;gap:22px;padding-top:10px">
            <div style="height:28px;width:90%;background:{GREY}"></div><div style="height:28px;width:68%;background:{GREY}"></div>
            <div style="height:28px;width:80%;background:{GREY}"></div>
            <div style="height:64px;width:72%;margin-top:6px;background:repeating-linear-gradient(90deg,{INK} 0 5px,transparent 5px 9px,{INK} 9px 11px,transparent 11px 16px)"></div>
          </div></div></div>
      <div class="a stamp" data-fx="stamp" data-r="-9" data-in="{a + LEAD + 3.4}" data-out="{b}" style="left:500px;top:1110px">IN PERSON ✓</div>''')

    sc(6, "ai-02-inked-thumb.png", "Your vote is your voice. Don't sell it. Don't waste it.", lambda a, b: f'''
      {tag("Your vote.", "w", 120, 80, 700, -3, a + .3, b)}
      {tag("Your voice.", "l", 120, 160, 880, 2, a + .6, b)}
      {tag("Don't sell it.", "k", 60, 100, 1110, -2, a + LEAD + 1.4, b)}
      {mark("thumb", 820, 330, 150, a + .9)}''', pos="50% 25%")

    sc(7, "ai-03-public-count.png", "Show up. Follow World Changers Network.", lambda a, b: f'''
      <div class="a box" data-fx="slideup" data-r="-2" data-in="{a + .3}" data-out="99" style="left:120px;top:330px;width:840px;height:420px;display:flex;align-items:center;justify-content:center">
        <img src="{u('assets','logo','wcn-horizontal-forest.png')}" style="width:680px"/></div>
      {tag("Show up. 16 Jan 2027.", "l", 60, 90, 720, -3, a + .8, 99)}
      <div class="a" data-fx="pop" data-r="0" data-in="{a + 1.4}" data-out="99" style="left:120px;top:920px;display:flex;flex-direction:column;gap:30px">
        <span class="soc">{icon(IG_ICON)}{IG_HANDLE}</span><span class="soc">{icon(X_ICON)}{X_HANDLE}</span></div>
      {mark("tick", 840, 960, 130, a + 1.8)}''')
    return "".join(out)


TICKER = ("NIGERIA DECIDES 2027 ✓ 57 DAYS TO GO ✓ COLLECT YOUR PVC ✓ SHOW UP ✓ " * 4)

JS = """
const cl=x=>Math.max(0,Math.min(1,x));
const c1=1.70158,c3=c1+1;
const backOut=x=>x<=0?0:x>=1?1:1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);
const backIn=x=>c3*x*x*x-c1*x*x;
const outExpo=x=>x>=1?1:1-Math.pow(2,-10*x);
const inOut=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
for(const el of document.querySelectorAll('[data-fx=type]')){
  el.innerHTML=[...el.textContent].map(ch=>`<span class="c">${ch}</span>`).join('');
}
const els=[...document.querySelectorAll('[data-fx]')];
const scenes=[...document.querySelectorAll('.scene')];
const logo=document.getElementById('logo'), tick=document.querySelector('.ticker div');
const LAST=+scenes[scenes.length-1].dataset.in; const XF=0.35;
function frame(t){
  for(const s of scenes){const a=+s.dataset.in,b=+s.dataset.out;const on=t>=a-0.001&&t<b+XF;
    s.style.visibility=on?'visible':'hidden'; s.style.opacity=a===0?1:inOut(cl((t-a)/XF));}
  logo.style.visibility=t<LAST+0.05?'visible':'hidden';
  tick.style.transform=`translateX(${-(t*120)%1400}px)`;
  for(const el of els){
    const fx=el.dataset.fx, a=+el.dataset.in, b=+el.dataset.out, r=+(el.dataset.r||0);
    const out=0;  // no exit moves: scenes cross-fade instead
    if(fx==='type'){
      const p=cl((t-a)/0.3);
      el.style.transform=`rotate(${r}deg) scaleX(${outExpo(p)*(1-out)}) scaleY(${1-out})`;
      el.style.opacity=t<a?0:1;
      [...el.children].forEach((c,i)=>{
        const q=backOut(cl((t-a-0.15-i*0.026)/0.3));
        c.style.transform=`translateY(${(1-q)*-60}%) rotate(${(1-q)*-20}deg)`; c.style.opacity=cl(q*2);
      });
    } else if(fx==='pop'||fx==='mark'){
      const p=backOut(cl((t-a)/0.45));
      let rot=r+(1-p)*30, fl=0;
      if(fx==='mark'){rot+=Math.sin(t*1.4+a)*6; fl=Math.sin(t*1.9+a*3)*8;}
      el.style.transform=`translateY(${fl}px) rotate(${rot}deg) scale(${Math.max(0,p*(1-out))})`;
      el.style.transformOrigin='center';
    } else if(fx==='slideup'){
      const p=backOut(cl((t-a)/0.6));
      el.style.transform=`translateX(${(1-p)*1200}px) rotate(${r+(1-p)*-10}deg) scale(${1-out})`;
    } else if(fx==='stamp'){
      const p=cl((t-a)/0.25);
      el.style.transform=`rotate(${r}deg) scale(${(2.8-1.8*outExpo(p))*(1-out)})`;
      el.style.opacity=t<a?0:cl(p*3);
    } else if(fx==='count'||fx==='countpop'){
      const d=+el.dataset.dur,f=+el.dataset.from,to=+el.dataset.to,dec=+(el.dataset.dec||0);
      el.textContent=(f+(to-f)*outExpo(cl((t-a)/d))).toFixed(dec)+(el.dataset.suffix||'');
      if(el.classList.contains('tag')){
        const p=backOut(cl((t-a)/0.5));
        el.style.transform=`rotate(${r+(1-p)*12}deg) scale(${Math.max(0,p*(1-out))})`;
      }
    } else if(fx==='bar'){
      el.style.width=(+el.dataset.to*outExpo(cl((t-a)/+el.dataset.dur)))+'%';
    } else if(fx==='kb'){
      el.style.transform=`scale(${1.06+0.1*cl((t-a)/(Math.min(b,a+20)-a))})`;
    } else if(fx==='words'){
      const ws=el.querySelectorAll('.wd'), d=+el.dataset.dur, n=ws.length;
      ws.forEach((w,i)=>{ w.style.opacity=t>=a+d*i/n-0.05?1:.18; });
      el.style.opacity=t<a-0.3?0:1;
    } else if(fx==='shut'){
      const at=+el.dataset.at, j=+el.dataset.j;
      const pin=inOut(cl((t-(at-0.42)+j*0.04)/0.36)), pout=inOut(cl((t-(at+0.02)-j*0.04)/0.36));
      el.style.transform=`translateY(${(pout>0?-pout:1-pin)*-100}%)`;
      el.style.transform=`translateY(${pout>0?-100*pout:(1-pin)*100}%)`;
    }
  }
}
window.frame=frame;
"""


def build_html():
    os.makedirs(OUT_DIR, exist_ok=True)
    body = (f'<img id="logo" src="{u("assets", "logo", "wcn-horizontal-lime-white.png")}"/>'
            + scenes()
            + f'<div class="ticker"><div>{TICKER}</div></div>')
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body>{body}<script>{JS}</script></body></html>")
    with open(BUILD, "w", encoding="utf-8") as fh:
        fh.write(html)


# ------------------------------------------------------------------ audio
SR = 48000


def music_bed(seconds):
    """A quiet, original synth bed: soft kick on the beat, and a warm four-chord
    pad. Made here, so no licence to worry about."""
    n = int(seconds * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    bpm = 100
    beat = 60 / bpm
    # pad: A minor, F, C, G (two bars each)
    chords = [[220, 261.6, 329.6], [174.6, 220, 261.6], [130.8, 196, 261.6], [196, 246.9, 293.7]]
    bar = beat * 4 * 2
    for k in range(int(seconds / bar) + 1):
        s0, s1 = int(k * bar * SR), min(n, int((k + 1) * bar * SR))
        if s0 >= n:
            break
        tt = t[s0:s1] - t[s0]
        env = np.minimum(1, tt / 0.6) * np.minimum(1, (bar - tt) / 0.6)
        for f in chords[k % 4]:
            out[s0:s1] += 0.05 * env * (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt))
    # kick
    kl = int(0.25 * SR)
    kt = np.arange(kl) / SR
    kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 14) * 0.5
    for k in range(int(seconds / beat)):
        s0 = int(k * beat * SR)
        e = min(n, s0 + kl)
        out[s0:e] += kick[:e - s0]
    # hats on the off-beat
    hl = int(0.05 * SR)
    rng = np.random.default_rng(7)
    for k in range(int(seconds / beat)):
        s0 = int((k + 0.5) * beat * SR)
        e = min(n, s0 + hl)
        if s0 < n:
            out[s0:e] += rng.normal(0, 1, e - s0) * np.exp(-np.arange(e - s0) / SR * 90) * 0.04
    # fade in and out
    f = int(1.0 * SR)
    out[:f] *= np.linspace(0, 1, f)
    out[-int(2 * SR):] *= np.linspace(1, 0, int(2 * SR))
    return out


def build_audio(path):
    n = int(DURATION * SR)
    voice = np.zeros(n)
    for i, (a, _) in enumerate(S):
        v, sr = sf.read(os.path.join(VO_DIR, f"{i + 1:02d}.wav"))
        if v.ndim > 1:
            v = v.mean(axis=1)
        if sr != SR:
            v = np.interp(np.arange(int(len(v) * SR / sr)) * sr / SR, np.arange(len(v)), v)
        s0 = int((a + LEAD) * SR)
        e = min(n, s0 + len(v))
        voice[s0:e] += v[:e - s0]
    voice *= 0.9 / max(1e-6, np.abs(voice).max())
    bed = music_bed(DURATION)
    # duck the bed under the voice
    env = np.convolve(np.abs(voice), np.ones(SR // 10) / (SR // 10), mode="same")
    duck = 1 - 0.55 * np.clip(env / 0.05, 0, 1)
    mix = voice + bed * 0.55 * duck
    mix *= 0.95 / np.abs(mix).max()
    sf.write(path, np.stack([mix, mix], axis=1), SR)


NODE = r"""
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const [,, html, out, fps, dur, mode, w, h, stills, audio] = process.argv;
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
      '-c:v', 'mjpeg', '-i', '-', '-i', audio, '-map', '0:v', '-map', '1:a',
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium',
      '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', '-r', fps, out],
      { stdio: ['pipe', 'inherit', 'inherit'] });
    const n = Math.round(+fps * +dur);
    for (let f = 0; f < n; f++) {
      await p.evaluate(t => frame(t), f / +fps);
      const buf = await p.screenshot({ type: 'jpeg', quality: 94 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 300 === 0) process.stdout.write(`  frame ${f}/${n}\n`);
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
    wav = os.path.join(OUT_DIR, ".mix.wav")
    with open(js, "w") as fh:
        fh.write(NODE)
    if not stills:
        build_audio(wav)
    times = ",".join(str(round(b - TAIL + 0.2, 2)) for a, b in S[:-1]) + f",{DURATION - 0.5}"
    target = OUT_DIR if stills else MP4
    try:
        subprocess.run(["node", js, BUILD, target, str(FPS), str(DURATION),
                        "stills" if stills else "video", str(W), str(H), times, wav], check=True)
    finally:
        os.remove(js)
        if os.path.exists(wav):
            os.remove(wav)
    print(f"wrote {target} ({DURATION}s)")


if __name__ == "__main__":
    main()
