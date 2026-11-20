#!/usr/bin/env python3
"""Video engine for WCN Reels: 1080x1920, 30 fps, H.264 + AAC, voiced.

Look: WCN's own neo-brutalism. Full photos of people voting under a forest
tint, square sticker labels with a lime shadow, thumbprint and tick marks,
calendar tiles, a lime ticker, word-by-word subtitles, soft cross-fades.
Sora only. Every element is placed by `frame(t)` in the page, so each frame
is exact; Playwright steps through time and pipes frames to ffmpeg.

Use it from a day script: see tools/day_52.py. In short, LINES holds one
voice line per scene, spec() returns [scene(...), ..., end_card(...)], and
make(OUT, "video.mp4", spec, lines=LINES) renders it.

Helpers: tag(text, cls w|l|k, size, left, top, rotate, at, out, fx),
mark(thumb|tick|arrow, left, top, size, at), count tags (data-fx="count"),
.box cards, .cal calendar tiles, .stamp. `a`/`b` are the scene's start/end.

Rules: NO day count anywhere in a video (no "N days to go", no countdown,
not in the ticker), so a video can be shared on any day. The days left go in
the caption only. INEC is said "Eye-neck" in LINES (one word), never spelled out.
Never say "one post a day". Needs ~/kokoro model files (see voiceover.py).
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
FPS = 30
W, H = 1080, 1920
LEAD, TAIL, END_HOLD = 0.55, 0.85, 2.6
LIME, FOREST, INK, GREY = "#D1DD25", "#0D421F", "#06120A", "#C9CDBF"


def u(*p):
    return "file://" + os.path.join(ROOT, *p)


# ------------------------------------------------------------------ timing
S, VO, DURATION = [], [], 0.0


def set_timing(durs):
    """Each scene lasts its voice line plus LEAD + TAIL; the last holds longer."""
    global S, VO, DURATION
    VO = list(durs)
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


def scene(i, photo, sub, body, pos="center"):
    """One scene: photo background, forest tint, the layout from body(a, b),
    and the subtitle `sub` lighting up word by word over the voice line."""
    a, b = S[i]
    words = "".join(f'<span class="wd">{w} </span>' for w in sub.split())
    return (f'<section class="scene" data-in="{a}" data-out="{b}">'
            f'<div class="bg" data-fx="kb" data-in="{a}" data-out="{b}" style="background-image:url(\'{u("images", "ai", photo)}\');background-position:{pos}"></div>'
            f'<div class="tint"></div>{body(a, b)}'
            f'<div class="sub" data-fx="words" data-in="{a + LEAD}" data-dur="{VO[i]}" data-out="{b}"><p>{words}</p></div>'
            f'</section>')


def end_card(i, photo, sub, line="Show up. 16 Jan 2027."):
    """The closing scene every video shares: logo, a line, the handles."""
    return scene(i, photo, sub, lambda a, b: f'''
      <div class="a box" data-fx="slideup" data-r="-2" data-in="{a + .3}" data-out="99" style="left:120px;top:330px;width:840px;height:420px;display:flex;align-items:center;justify-content:center">
        <img src="{u('assets','logo','wcn-horizontal-forest.png')}" style="width:680px"/></div>
      {tag(line, "l", 60, 90, 720, -3, a + .8, 99)}
      <div class="a" data-fx="pop" data-r="0" data-in="{a + 1.4}" data-out="99" style="left:120px;top:920px;display:flex;flex-direction:column;gap:30px">
        <span class="soc">{icon(IG_ICON)}{IG_HANDLE}</span><span class="soc">{icon(X_ICON)}{X_HANDLE}</span></div>
      {mark("tick", 840, 960, 130, a + 1.8)}''')


def ticker_text(day=None):
    # No day count in videos, ever: they must work on any day.
    return "NIGERIA DECIDES 2027 ✓ COLLECT YOUR PVC ✓ KNOW YOUR BALLOT ✓ SHOW UP ✓ " * 4

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
      el.textContent=(el.dataset.prefix||'')+(f+(to-f)*outExpo(cl((t-a)/d))).toLocaleString('en-US',{minimumFractionDigits:dec,maximumFractionDigits:dec})+(el.dataset.suffix||'');
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


def build_html(path, scenes_html, day):
    body = (f'<img id="logo" src="{u("assets", "logo", "wcn-horizontal-lime-white.png")}"/>'
            + "".join(scenes_html)
            + f'<div class="ticker"><div>{ticker_text(day)}</div></div>')
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body>{body}<script>{JS}</script></body></html>")
    with open(path, "w", encoding="utf-8") as fh:
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


def build_audio(path, vo_dir):
    n = int(DURATION * SR)
    voice = np.zeros(n)
    for i, (a, _) in enumerate(S):
        v, sr = sf.read(os.path.join(vo_dir, f"{i + 1:02d}.wav"))
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


VOICE = os.environ.get("WCN_VOICE", "af_heart")


def synth(lines, vo_dir):
    """Voice each line with Kokoro into vo_dir/NN.wav. Lines already voiced
    with the same text are kept. Returns the durations in seconds."""
    os.makedirs(vo_dir, exist_ok=True)
    meta_path = os.path.join(vo_dir, "lines.json")
    old = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
    durs, k = [], None
    for i, line in enumerate(lines, 1):
        wav = os.path.join(vo_dir, f"{i:02d}.wav")
        if old.get(str(i)) == line and os.path.exists(wav):
            a, sr = sf.read(wav)
        else:
            if k is None:
                from kokoro_onnx import Kokoro
                home = os.path.expanduser("~/kokoro")
                k = Kokoro(os.path.join(home, "kokoro-v1.0.onnx"), os.path.join(home, "voices-v1.0.bin"))
            a, sr = k.create(line, voice=VOICE, speed=1.0, lang="en-us")
            sf.write(wav, a, sr)
        durs.append(round(len(a) / sr, 2))
    json.dump({str(i): l for i, l in enumerate(lines, 1)}, open(meta_path, "w"), indent=1)
    json.dump(durs, open(os.path.join(vo_dir, "durations.json"), "w"))
    return durs


def make(out_dir, mp4_name, spec, *, lines=None, durations=None, day=None):
    """Render a video. `spec()` returns the scenes' HTML (call scene() and
    end_card() inside it; timing is set before it runs). Voice comes from
    `lines` (spoken with Kokoro) or from existing vo/ files and `durations`.
    `--stills` on the command line writes one PNG per scene instead."""
    os.makedirs(out_dir, exist_ok=True)
    vo_dir = os.path.join(out_dir, "vo")
    durs = synth(lines, vo_dir) if lines else durations
    set_timing(durs)
    build = os.path.join(out_dir, ".video.html")
    build_html(build, spec(), day)
    stills = "--stills" in sys.argv
    js = os.path.join(out_dir, ".render.js")
    wav = os.path.join(out_dir, ".mix.wav")
    with open(js, "w") as fh:
        fh.write(NODE)
    if not stills:
        build_audio(wav, vo_dir)
    times = ",".join(str(round(b - TAIL + 0.2, 2)) for a, b in S[:-1]) + f",{DURATION - 0.5}"
    target = out_dir if stills else os.path.join(out_dir, mp4_name)
    try:
        subprocess.run(["node", js, build, target, str(FPS), str(DURATION),
                        "stills" if stills else "video", str(W), str(H), times, wav], check=True)
    finally:
        for p in (js, wav, build):
            if os.path.exists(p):
                os.remove(p)
    print(f"wrote {os.path.relpath(target, ROOT)} ({DURATION}s)")
