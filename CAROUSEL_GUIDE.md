# WCN Civic Awareness, Design and Build Guide

Single source of truth for the campaign. If you are an AI assistant starting
fresh, read this, then `CAMPAIGN_LOG.md`, then render a day.

## 1. What we are making

A 57 day countdown of voter education posts. Some days are carousels, some are
single images. The goal is turnout and informed choice, never a side.

- **4:5 portrait, 1080 x 1350** by default. Square only when a single image
  needs it (`--square`).
- **Ten slides is the hard ceiling** (Instagram's limit). Most carousels land
  at 5 to 8.
- Folder per day, named `Day NN - Title`, slides named `01-cover.png`,
  `02-slide-1.png` ... and the last `NN-cta.png`. A single image is `01-post.png`.

## 2. The look

Ignovations' energy, Nigerian campaign poster vocabulary, WCN's own brand.

- **Font: Sora only.** It is the WCN brand font (the face in the logo).
  Headlines are Sora ExtraBold (800), sentence case, tight tracking
  (-0.045em). Body is Sora Regular to SemiBold. No other typeface.
- **Brand colours** (from the WCN logo):

  | Token | Hex | Use |
  |---|---|---|
  | `ACCENT` | `#D1DD25` | WCN lime. One line or one word per slide, big numbers, icons |
  | `FOREST` / `ACCENT_INK` | `#0D421F` | WCN forest green. The background glow, text on a lime fill |
  | `INK` | `#06120A` | base of every slide |
  | white | `#FFFFFF` | headline text |

- **Logo top left** on every slide, the horizontal lime and white WCN logo
  (`assets/logo/wcn-horizontal-lime-white.png`), with a soft shadow so it holds
  on any photo. Nothing else at the top: the countdown lives in the cover badge.
- **Foot** on every slide: Instagram icon + `world_changersnetwork`, X icon +
  `worldchangernet`, then the swipe hand on the right (nothing on the last
  slide).
- **People in every background.** Arkcore (20 Nov): no blank backgrounds, we
  need life. Every slide gets a full colour photo of Nigerians doing election
  things: queues, inked thumbs, ballot boxes, PVC collection, friends arguing
  politics, the public count. The photo fills the top; a forest-to-ink fade
  rises from the floor so the words always sit on near black and stay legible.
  The graphic background (forest glow and thumbprint) is only a fallback.
- **Where photos come from.** Real photos first, from WCN's own events. Until
  then, AI generated scenes in `images/ai/` (made in Figma with the prompts in
  `images/ai/PROMPTS.md`). Rules for AI images: everyday Nigerians, no party
  logos or colours, no readable text, no real public figures, subjects in the
  upper two thirds. Do not use AI images on candidate slides.
- **Countdown badge** on the cover: a lime pill reading `57 days to election
  day`, the number in a forest circle. It is worked out from the day, so it is
  always right.
- **Swipe hand** bottom right on every slide but the last: a lime hand with
  motion lines and the word SWIPE underneath it.
- **Thumbprint** is the motif. Voting is a thumb.
- **Logos** are in `assets/logo/` (renamed) and `assets/brand/` (as supplied) for any slide
  that needs one, e.g. a closing slide.

Markup inside slide text: `*word*` lime, `[word]` lime block behind the word,
`**word**` bold white (in lead lines), `\n` line break.

## 3. Slide types

| Kind | Use |
|---|---|
| `cover` | The hook. One provocative question or claim. Nothing else |
| `statement` | Small lead lines, then the punch in display |
| `stat` | One big number, label, source |
| `dates` | Rows of date + what happens |
| `list` | Numbered points, up to about six |
| `countdown` | Giant day count, for single image countdown days |
| `candidate` | Party colour bands, cut-out portrait, INEC facts |
| `cta` | Save. Share. Show up. |

## 4. Titles: provocative, never partisan

The cover has one job, earn the swipe. It can sting the reader ("73% of us did
not vote. Will you be one of them?") or challenge a belief ("Your governor
touches more of your life than your president"). It never attacks, mocks or
praises a person, party, tribe or religion, and it never predicts a winner.

Test: would every candidate's supporters be comfortable sharing it? If not,
rewrite.

## 4b. Carousels tell a story

Arkcore (20 Nov): a carousel must flow, one slide to the next. Before writing
slides, write the spine in one line, e.g. for Day 57:

> hook -> what 2023 looked like -> why it mattered -> 2027 is bigger ->
> when you show up -> what you need first -> what not to trade it for ->
> don't be the 73% this time.

Then give every slide after the cover a `lead` line that picks up the slide
before it ("Here is what 2023 looked like.", "Did it matter?", "So when do you
show up?", "But none of that counts without one card."). If a slide could be
moved without anyone noticing, the story is broken. The last slide closes the
loop on the cover's hook.

## 5. Candidate posts

Arkcore's call (20 Nov 2026): candidate photos and party colours are in.

- Same template for everyone. Only the photo, name, party colours and INEC
  facts change.
- **Order is INEC's ballot order** from `data/presidential_candidates.json`.
  Groups of three per carousel, six carousels, then the running mates.
- Facts come only from INEC's final list (age, running mate, qualifications as
  printed). No slogans, no achievements, no criticism, no polls.
- Every candidate slide carries "Information, not endorsement".
- Cut-out portraits (transparent PNG) go in `images/candidates/` named
  `<party>-president.png`, e.g. `apc-president.png`. A JPG fills the frame
  instead.
- Party colours live in `tools/parties.py`, each marked unconfirmed until
  checked against the party logo.
- **No candidate content from Day 2** (14 Jan): campaigns close 24 hours
  before election day.

## 6. Facts and sources

- No "Source:" line on slides (Arkcore, 20 Nov). Still put `source=` on
  every slide in the day script and list sources in `captions.md`, so the team
  can check each number. `SHOW_SOURCES` in the engine turns them back on.
- **WCN is not affiliated with whyvote.ng.** It was used only as background
  research. Never name, link or tag it on a slide or in a caption. Cite INEC
  (or the primary source) for every number, and check the number against INEC
  before posting.
- Anything procedural (polling hours, what to bring, ballot rules, reporting
  channels) is marked VERIFY in the plan and checked against INEC's latest
  guidance before posting. The content plan says the same.

## 7. Platforms

We post on Instagram and X. The same PNGs go to both.

- Instagram: up to 10 slides in one carousel.
- X: up to 4 images per post. A longer carousel goes out as a thread, 4
  slides per post, cover first. Write each post so it reads alone.

## 8. Captions

Voice, from WCN's own X post (16 Nov 2026): short, direct, hopeful, a flag
emoji at most. "61 days to go. 🇳🇬 A new Nigeria won't come from the timeline.
It comes from the ballot box. Get your PVC, know your polling unit, and show
up. 🗳️" Start with the countdown, end with one clear action.

Each day's `captions.md` holds: post date, format, status, slide table, sources,
the Instagram caption, and the X post or thread (each under 280 characters). Caption ends with the campaign hashtags: `#YourVoteYourVoice #YourVoteCounts
#NigeriaDecides2027`, plus the day tag WCN already uses on X, e.g.
`#57DaysToGo`.

## 9. Making a new day, step by step

For anyone on the team, with or without an AI assistant.

1. **Set up once.** Install Google Chrome and Python 3, then
   `pip3 install pillow`. Clone the repo.
2. **Pick the day.** Open `CONTENT_PLAN.csv` (see `CLAUDE.md`), set the
   day to `writing` with your name, run `python3 tools/plan.py`, push. The day's folder Its
   `captions.md` stub has the date, format and idea.
3. **Write the words.** Copy `tools/day_57.py` to `tools/day_NN.py`. Set
   `DAY` (`OUT` is read from the sheet) and replace `SLIDES`. Ten
   slides at most. Write the story spine first (section 4b), then one idea
   per slide, cover first, CTA last. Every number gets `source=`.
4. **Add photos.** Put them in `images/` and write the filename in
   `photo="..."` on each slide. Candidate cut-outs go in `images/candidates/`.
5. **Render.** `python3 tools/day_NN.py` (add `--square` for a 1080x1080
   copy). Open the PNGs and check every line.
6. **Write captions.md.** Status, slide table, sources, Instagram caption and
   the X post or thread (4 images per X post, under 280 characters each).
7. **Log it.** Add anything you decided to `CAMPAIGN_LOG.md`, then commit and
   push.

If you change the look, change it in `tools/generate_carousel.py` and record
it here. Never edit the engine to make one post work.

## 10. Prompt for an AI assistant

> Read README.md, CAROUSEL_GUIDE.md and CAMPAIGN_LOG.md in this repo. Then
> build Day NN from its row in CONTENT_PLAN.csv (see CLAUDE.md): write tools/day_NN.py following
> tools/day_57.py, render it, and fill in that day's captions.md with the
> Instagram caption and the X thread. Follow the neutrality rules in
> section 4 and 5 exactly.


## 11. Videos (Reels)

- 1080x1920, voiced, built with `tools/video_engine.py`. The look is WCN's own
  neo-brutalism over photos of people (see CAMPAIGN_LOG for why it must not
  look like the NectAll videos).
- **No day count in any video.** Videos must be shareable on any day. The
  days left go in the caption.
- One voice line per scene, said the way it should sound: INEC is "Eye-neck",
  PVC is "P V C". Never say "one post a day".
- Scenes cross-fade softly. No shutters, no whoosh.
