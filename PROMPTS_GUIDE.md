# Prompts and how-to guide

How the campaign's images and videos were made, with the exact prompts, so
anyone on the team can make more that look and sound the same. Read
`CLAUDE.md` first for the rules; this file is the "how".

Contents
1. The workflow in one page
2. Prompts to give Claude (posts, videos, fixes)
3. AI photo prompts (every background used so far)
4. Video voice scripts
5. Tools and settings
6. What's in the repo, and what isn't

---

## 1. The workflow in one page

| Step | What happens | Where |
|---|---|---|
| Plan | Pick the day's row (topic, hook, format) | `CONTENT_PLAN.csv` |
| Photos | Generate a people-doing-election-things photo, or reuse one | `images/ai/` |
| Build | Copy a day script, write the slides or scenes, run it | `tools/day_NN.py` |
| Check | Look at every PNG, or watch the video | `Day NN - .../` |
| Captions | Instagram caption, X posts, sources | `Day NN - .../captions.md` |
| Review | Copy the day folder to the team review folder; one PDF of captions with `python3 tools/captions_pdf.py` | Desktop |
| Ship | Status `built`, `python3 tools/plan.py`, commit, `git push` | GitHub |

Formats: Carousel (1080x1350, ten slides at most, one story), Single
(one 1080x1350 image), Video (1080x1920 Reel, voiced).

---

## 2. Prompts to give Claude

These are the requests that produced the posts, cleaned up so they can be
reused. Change the parts in angle brackets.

### Build the next days

```
Read CLAUDE.md, CAROUSEL_GUIDE.md, CAMPAIGN_LOG.md and CONTENT_PLAN.csv in the
wcn-civic-campaign repo. Build Days <56 to 47>. Use the format in the sheet:
some carousels, some single images, some videos. Every background shows
Nigerians doing election things. Render every slide, look at each one, fill in
captions.md for each day, set Status to built, and copy the day folders to
"WCN Days <56 to 47> - for team review" on my Desktop.
```

### One carousel

```
Build Day <NN> as a carousel from its row in CONTENT_PLAN.csv. Ten slides at
most, and each slide must pick up the one before it (cover hook, the problem,
the facts, what to do, call to action). Brand: Sora only, lime #D1DD25, forest
#0D421F, logo top left, IG and X handles in the footer, swipe hand with SWIPE.
Non-partisan, INEC facts only, no "Source:" on the slides (sources go in
captions.md).
```

### One single image

```
Build Day <NN> as a single image. One strong line, a short body, a photo of
people doing an election thing. Copy tools/day_57_single.py.
```

### A video (Reel)

```
Make Day <NN> a voiced Reel, 1080x1920, with tools/video_engine.py. Topic:
<topic>. Write <6 to 8> short voice lines, one per scene, and build each scene
on a people photo with the WCN brutalist tags (square tags, thick ink border,
lime shadow), word-by-word subtitles and the scrolling ticker. Rules: no day
count anywhere in the video (days left go in the caption only), say INEC as
"Eye-neck" in the voice lines, never say "one post a day", soft crossfades
only (no shutter or whoosh), end on the WCN end card with both handles.
Check the stills for text running off the edge before rendering.
```

### Candidate posts

```
Build Meet The Candidates <part N of 6> for <parties>, in INEC ballot order,
with data/presidential_candidates.json and the party colours in
tools/parties.py. Same template for every candidate. Real photos only, from
images/candidates/; never AI. If a photo is missing, keep the monogram and
tell me which files to add.
```

### Fixes that came up (and what fixed them)

| Ask | What it changed |
|---|---|
| "This is plain, can you add image" | A design was drawn onto the blank card in the photo (`tools/pvc_card.py`) |
| The video looks like another brand's | Photo backgrounds with WCN tags on top, instead of flat colour |
| "I can't hear anything" | Voice on every scene, music ducked under it, loudness set to -14 LUFS |
| The transition is like a break in transmission | Soft crossfades only |
| Don't put the days in videos | No countdown or "days to go" in any video; days in the caption |

---

## 3. AI photo prompts

Made with Figma's `generate_image` (model gpt-image-2.5-flare), asked for
1080x1350 (comes back 1024x1280), in the Figma file "WCN Civic Campaign - AI
backgrounds". Videos crop the same photos to 9:16.

**The rules every prompt ends with** (keep them, so the set looks like one shoot):

```
Candid photojournalism, natural light. No party logos, no readable text.
Vertical composition, subjects in upper two thirds, lower third darker and
uncluttered.
```

The lower third is kept dark and empty because the headline sits there.

**Template for a new one**

```
<Who> <doing what election or civic thing> <where in Nigeria>, <mood>.
Candid photojournalism, natural light. No party logos, no readable text.
Vertical composition, subjects in upper two thirds, lower third darker and
uncluttered.
```

Never generate a real public figure or a candidate. Check each result for
anything that reads as a party logo, flag or slogan (one cap badge in
ai-14 had to be blurred). If a prop comes back blank (the voter card in
ai-16), it can be drawn on afterwards like `tools/pvc_card.py` does.

### The prompts used

**ai-01-polling-queue.png**

```
Documentary photograph, Nigeria election day: a long queue of diverse young Nigerian voters, men and women in everyday clothes, some in ankara prints and hijab, waiting patiently outside a primary school polling unit under morning sun, holding voter cards. Candid, photojournalism style, 35mm, shallow depth of field, natural light. No party logos, no text, no flags of parties. Vertical composition with subjects in upper two thirds, darker empty ground in the lower third.
```

**ai-02-inked-thumb.png**

```
Documentary photograph, Nigeria election day: close-up of a smiling young Nigerian woman holding up her thumb stained with purple voting ink, polling unit and other voters softly blurred behind her. Candid photojournalism, 50mm, natural daylight. No party logos, no text. Vertical composition, subject in upper two thirds, lower third darker and uncluttered.
```

**ai-03-public-count.png**

```
Documentary photograph, Nigeria: polling officials counting ballot papers aloud on a wooden table outdoors at a polling unit while a crowd of local Nigerian residents, young and old, watch closely and record on their phones. Transparent ballot box on the table. Candid photojournalism, natural light. No party logos, no readable text. Vertical composition, action in upper two thirds, lower third darker.
```

**ai-04-friends-debate.png**

```
Documentary photograph, Lagos Nigeria: a group of young Nigerian friends, university age, sitting together on a bench at a roadside, animated but friendly political discussion, one holding a smartphone, one holding a voter card. Street life, okada and danfo bus blurred in background. Candid, warm, energetic, natural light. No party logos, no text. Vertical composition, people in upper two thirds, lower third darker.
```

**ai-05-bvas-accreditation.png**

```
Documentary photograph, Nigeria: inside a polling unit classroom, a young Nigerian man places his finger on a small handheld biometric voter accreditation device held by an electoral official in a vest, other voters waiting behind. Candid photojournalism, natural window light. No logos, no readable text. Vertical composition, action in upper two thirds, lower third darker.
```

**ai-06-walk-to-vote.png**

```
Documentary photograph, Nigeria: an elderly Nigerian man in a cap and agbada and a young woman, perhaps his granddaughter, walking together on a dusty street towards a polling unit early morning, holding voter cards, neighbours walking in the same direction. Hopeful, candid, golden morning light. No party logos, no text. Vertical composition, people in upper two thirds, lower third darker road.
```

**ai-07-ballot-box.png**

```
Documentary photograph, Nigeria: a voter in a polling booth with a cardboard privacy screen, folding a ballot paper, then a hand dropping a folded ballot into a transparent ballot box, other Nigerians queueing outside the classroom door. Candid photojournalism. No party logos, no readable text. Vertical composition, action in upper two thirds, lower third darker.
```

**ai-08-pvc-collection.png**

```
Documentary photograph, Nigeria: busy queue of young Nigerians at a local government office collecting their permanent voter cards, an official at a desk handing a card to a smiling young man, others holding registration slips. Candid, energetic, natural light. No logos, no readable text. Vertical composition, people in upper two thirds, lower third darker.
```

**ai-09-hospital.png**

```
Busy corridor of a Nigerian public general hospital, nurses in white and patients waiting on benches, a young mother with a baby, ordinary Nigerians. Candid photojournalism, natural light. No party logos, no readable text. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

**ai-10-classroom.png**

```
Crowded Nigerian public secondary school classroom, students in uniform at wooden desks, a teacher at the chalkboard, sunlight through louvre windows. Candid photojournalism, natural light. No party logos, no readable text. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

**ai-11-market-trader.png**

```
Nigerian market woman at her foodstuff stall counting a few naira notes, thoughtful expression, busy open market behind her. Candid photojournalism, natural light. No party logos, no readable text. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

**ai-12-handshake.png**

```
Two young Nigerian men shaking hands and smiling outside a school polling unit on election day, calm neighbours chatting behind them, peaceful mood. Candid photojournalism, natural light. No party logos, no readable text. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

**ai-13-family-table.png**

```
Nigerian family around a dinner table at home in the evening, an uncle talking and gesturing, a young woman in her twenties listening with a confident expression, warm lamp light. Candid photojournalism. No party logos, no readable text. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

**ai-14-town-hall.png**

```
Community town hall meeting in a Nigerian civic centre, seated audience of all ages, a young woman standing and asking a question into a microphone. Candid photojournalism, natural light. No party logos, no banners, no readable text. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

**ai-15-bus-stop-phone.png**

```
Young Nigerian man at a busy Lagos bus stop reading intently on his phone, yellow buses and commuters blurred behind him. Candid photojournalism, natural light. No party logos, no readable text. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

**ai-16-pvc-proud.png**

```
Young Nigerian woman on a city street proudly holding up her plain green voter card toward the camera, friends behind her smiling. Candid photojournalism, natural light. No party logos, no readable text on the card. Vertical composition, subjects in upper two thirds, lower third darker and uncluttered.
```

---

## 4. Video voice scripts

One line per scene. The scene lasts as long as its line, plus a short pause.
Write numbers the way they should be said ("five thousand naira",
"twenty twenty three") and INEC as "Eye-neck".

### Election Reel (`Specials/Election Reel`, `tools/voiceover.py` + `tools/reel.py`)

Made before the no-day-count rule; new videos must not open with a countdown.

1. Fifty seven days. Nigeria votes on Saturday, the sixteenth of January.
2. In twenty twenty three, seventy three percent of registered voters stayed home.
3. Turnout was twenty six point seven percent, the lowest since nineteen ninety nine. The race was won by about one point eight million votes.
4. Now, over one hundred and three million Nigerians are registered. That includes you.
5. Mark two Saturdays. January sixteenth, for President and the National Assembly. February sixth, for Governor and State Assembly.
6. No P V C, no vote. Collect yours at your Eye-neck office, in person.
7. Your vote is your voice. Don't sell it. Don't waste it.
8. Show up. Follow World Changers Network.

### Day 52, vote-buying maths (`tools/day_52.py`)

1. Someone offers you five thousand naira for your vote.
2. It sounds like money. Now do the maths.
3. Four years is one thousand, four hundred and sixty one days.
4. Five thousand naira over four years is about three naira a day.
5. Three naira won't even buy a sachet of water.
6. But the people you elect will spend trillions of naira. On your roads, your hospitals, your schools.
7. And selling your vote is a crime under the Electoral Act.
8. Don't sell your vote. Show up and choose.

### Day 48, not your uncle's vote (`tools/day_48.py`)

1. Your uncle has an opinion on who you should vote for.
2. Your pastor or your imam might too.
3. So might your boss.
4. Listen to all of them. Then decide for yourself.
5. Your ballot is secret. Nobody sees who you choose.
6. Not their vote. Yours.

---

## 5. Tools and settings

| What | Tool | Setting |
|---|---|---|
| Slides | `tools/generate_carousel.py` | HTML rendered with Chrome at 2x, saved at 1080x1350 |
| Videos | `tools/video_engine.py` | 1080x1920, 30 fps, H.264 + AAC, crossfade 0.35s |
| Voice | Kokoro TTS (free, open source), voice `af_heart` | Model files in `~/kokoro/` from github.com/thewh1teagle/kokoro-onnx releases (model-files-v1.0); `pip3 install kokoro-onnx soundfile` |
| Music | Made in code inside `video_engine.py` (pads, kick, hats) | Ducked under the voice |
| Loudness | ffmpeg `loudnorm=I=-14:TP=-1.5:LRA=11` | Instagram level |
| Captions PDF | `tools/captions_pdf.py` | Needs pandoc and Chrome |
| Voter card face | `tools/pvc_card.py` | Generic design, no coat of arms or INEC logo |

To use a real person's voice instead of Kokoro, record each line as
`vo/01.wav`, `vo/02.wav`... in the day's folder and build; the engine times
the scenes to the recordings.

Setup once: Google Chrome, Python 3, ffmpeg, Node with Playwright,
`pip3 install pillow numpy kokoro-onnx soundfile`.

---

## 6. What's in the repo, and what isn't

Everything needed to generate is in the repo:

| What | Where |
|---|---|
| Logos (horizontal, stacked, mark; lime, white, black, forest) | `assets/logo/` |
| Full brand kit from the designer (PNG, JPG, PDF, SVG) | `assets/brand/` |
| Font: Sora (free, OFL licence) | `fonts/Sora.ttf` |
| Instagram and X icons, swipe hand, fingerprint | drawn in code in `tools/generate_carousel.py` |
| AI people photos | `images/ai/` |
| Candidate data, INEC ballot order | `data/presidential_candidates.json` |
| Party colours | `tools/parties.py` |
| Plan sheet | `CONTENT_PLAN.csv` |

Not in the repo (too big, download once): the Kokoro voice model files,
about 350 MB, into `~/kokoro/` (see section 5). Candidate photos are added to
`images/candidates/` as they come in.
