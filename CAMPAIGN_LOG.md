# Campaign log

Newest first.

## Wed 25 Nov 2026, standalone countdown series

- David selected a simple green background, bold white countdown, small WCN
  logo at top left, and a white footer with Instagram and X handles. This
  countdown series deliberately uses no background photos or swipe indicator.
- Added `countdowns/YYYY-MM-DD/` for every date from 25 Nov 2026 to 15 Jan
  2027: 52 through 1 days before the 16 Jan election. PNGs are 1080x1350;
  each folder also contains caption, alt text and production metadata.
- Current design `green-white-v2`: Sora-derived display instances with merged
  contours and cleaned Y/G joins, fixing the cracked-looking display lettering.
  Original Sora font and licence are retained; adapted fonts are named WCN
  Countdown. See `countdowns/_assets/static/FONT-NOTES.md`.
- All 52 dates, dimensions, image hashes, gallery links and X caption lengths
  checked. Final day says `DAY TO GO`. INEC calendar checked 25 Nov 2026.
  Accuracy/visual review remains visible in metadata; nothing published.
- Gallery: `countdowns/index.html`; scheduling index and simple tracker are in
  the same folder. Existing daily content and publishing statuses are retained.

## Fri 20 Nov 2026, setup and Day 57

- Arkcore: logo top left or right. Logo back, top left, on every slide; the
  earlier countdown pill stays gone.

- Arkcore: no "Source: INEC" on slides; carousels must flow as a story; put
  SWIPE under the hand; and give a single picture too. Day 57 rewritten as a
  story (see CAROUSEL_GUIDE 4b), sources hidden (kept in captions.md), and a
  single image added at `Day 57 .../single/01-post.png`.

- Arkcore: WCN is not affiliated with whyvote.ng, remove it. Removed from every
  slide, footer and caption. Sources now cite INEC. whyvote stays only as a
  private research pointer in the plan notes.

- Arkcore: backgrounds need people and energy, the countdown must be plain
  ("57 days to election"), and use a hand for swipe. Generated 8 AI scenes of
  Nigerians voting in Figma (file "WCN Civic Campaign - AI backgrounds", on
  the Education Arc team, uses Figma AI credits). Photos now render in colour
  under a forest fade. Cover carries a `57 days to election day` badge. Swipe
  is a lime hand icon.

- Arkcore: remove the top bar, use our fonts. Top bar (logo + countdown pill)
  removed. Anton dropped; Sora, the WCN brand font, now does display and body.
- Handles: Instagram `world_changersnetwork`, X `worldchangernet`.
- WCN's X already posts countdown tweets with `#61DaysToGo` style tags.

- Brand assets in (logo PNG, SVG, PDF). Arkcore: use our brand colour as the
  guide. Accent moved from a placeholder green to WCN lime `#D1DD25` and forest
  `#0D421F`. Footer now carries Instagram and X icons with the handles.

- Election dates confirmed: 16 Jan 2027 (President, NASS) and 6 Feb 2027
  (Governor, State Assembly), INEC revised timetable of 26 Feb 2026. INEC
  called a July 2026 viral graphic with different campaign dates fake.
- 57 days from 20 Nov to 16 Jan. Day 57 is today, Day 1 is 15 Jan.
- Folder layout copied from Eden Centre: root guide files, `tools/` engine and
  one script per post, one folder per post with slides and `captions.md`.
- Look taken from Ignovations (black and white photo, condensed caps, accent
  second line) and Arkcore's Pinterest board of Nigerian campaign posters
  (colour bands, cut-out portraits, thumbprint).
- Candidate photos and party colours: yes (Arkcore). This overrides the
  content plan's "no candidate images or party colours" note.
- INEC final list of presidential candidates (PDF, 30 Oct 2026) saved in
  `data/`. 19 tickets. Ticket 1 (A) is blank, remark "COURT ORDER".
- Fonts: Ignovations uses Gondens DEMO, a demo licence, so not used here.
- Plan sheet: `CONTENT_PLAN.csv` is now the single source of truth for topics,
  so anyone can change a day in Excel and push. `tools/plan.py` syncs folders
  and rebuilds `CONTENT_PLAN.md`. Workflow written in `CLAUDE.md`.
- Day 57 carousel, single image and captions copied to Arkcore's Desktop
  ("WCN Day 57 - for team review") for team feedback.
- Special post: one image of all 19 parties on the presidential ballot, INEC
  order, same chip per party (`tools/parties_single.py`,
  `Specials/Parties On The Ballot/`). Also on the Desktop for the team.

- Election reel (`tools/reel.py`, `Specials/Election Reel/`): 34 s, 1080x1350.
  Style taken from the NectAll event videos Arkcore pointed to (sticker labels
  with a hard ink shadow, letters popping in, doodles, tickets and cards,
  slanted wipes, subtitle box), recoloured to forest and lime. Cream dotted
  background, so the logo is the forest version (`wcn-horizontal-forest.png`).
- Reel v2: Arkcore liked v1 but it looked too much like NectAll (they make
  NectAll videos too). Kept neo-brutalism, made it WCN's own: photo
  backgrounds of people, square labels with lime shadows, thumbprint and tick
  marks, calendar tiles, ticker, word-by-word subtitles, shutter cuts. Now
  1080x1920 with a voiceover (Kokoro, `tools/voiceover.py`) and a music bed.
- Reel fixes from Arkcore: INEC is said as one word ("eye-neck"), never
  spelled out; never say "one post a day"; the shutter transition and whoosh
  were too much, so scenes now cross-fade quietly.
- Arkcore: no day count in any video from now on, so videos can be shared on
  any day; the days left go in the caption.
- Arkcore: do not push to igudy/wcn-civic-campaign. Push to
  Igudy-Solutions/wcn-civic-campaign (waiting on GitHub being connected).

- Days 56 to 47 built (Arkcore: "generate the images for the next 10 days",
  "some video, some single image, some carousel"). Carousels 55, 53, 50, 49,
  47; singles 56, 54, 51; videos 52 and 48 (Format `Video` added to the plan
  sheet). Eight new AI backgrounds (ai-09 to ai-16, see images/ai/PROMPTS.md).
- Candidate slides without a photo now show a party monogram ("photo to
  come") instead of a dashed box. Real photos only, never AI.
- Day 57 CTA and caption no longer mention posting every day.

## Open questions

- Candidate photos for Day 49 (AA, AAC, ADC) and the rest of the series.

- Party colours in `tools/parties.py` are unconfirmed.
- Display order of names: INEC prints surname first. `display` names in the
  JSON are our reading; check spellings and order for the less known names.
- The 103.4m register figure is INEC's October 2026 update, not the final
  register. Update when INEC publishes the final number.

## 20 Nov 2026: Day 56 card no longer plain
Arkcore: the green card in the Day 56 photo was plain. `tools/pvc_card.py`
draws a generic voter-card face (no coat of arms, no INEC logo, grey bars
instead of real details) onto the card, keeping the thumb in front and the
photo's light. Output `images/ai/ai-16-pvc-proud-card.png`. The countdown
number now takes a `big=` size; Day 56 uses 320 so the date line clears the card.

## 26 Nov 2026: Days 46 to 1 built
Arkcore asked for every remaining daily post. All 46 days are built and set to
`built` in the sheet, Owner Claude, for team review. Mix: carousels, singles
and six voiced videos (Days 43, 32, 24, 16, 7 and 1, Format changed to Video).
The day scripts were written by `tools/_gen/batch1.py` to `batch4.py` and
`tools/_gen/videos.py` (these also write each captions.md); each day still has
its own `tools/day_NN.py` to re-render.

- Candidates: "Meet the candidates" Parts 2 to 6 (Days 45, 41, 37, 33, 30)
  use `candidate_slide`; every ticket shows "PHOTO TO COME" until real photos
  arrive. Day 29 lists all running mates; Day 27 the six women.
- New AI photos (Figma): ai-18 bus park, ai-19 airport, ai-22 official
  explains, ai-23 inked group, ai-24 peace walk, ai-26 results wall, ai-27
  wheelchair voter. Prompts in `PROMPTS_GUIDE.md`. Figma's plan hit its call
  limit, so four more planned photos were not made and existing ones reused.
- `k_list`: items can carry their own number, `start=` sets the first number,
  an optional `body` line, and lists of six or more go tight so they clear the
  footer.
- Marked VERIFY in captions: Christmas travel and transfer window (Day 23),
  vote-buying law (21), polling unit steps (18), glossary (17), rights (13),
  ballot cancellation (9), Japa / no diaspora voting (24), results process
  (16), movement restriction (7).

## 26 Nov 2026: day folders grouped, Day 51 rewritten, PVC collection special
- All day folders now live in `Daily Posts/` (Arkcore asked for one folder).
  `tools/plan.py` (`DAYS_DIR`), `captions_pdf.py` and `_gen/common.py` follow it;
  day scripts are unchanged because they use `folder_for`.
- Day 51 rewritten at Arkcore's ask: "Your future is worth fighting for." It
  leads with the stakes (hospital, school, job, four years) and makes the fight
  the vote: fight with your PVC, not your fists. Folder renamed to match.
- PVCs are out, so `Specials/Collect Your PVC` (`tools/special_pvc.py`) starts
  the collection push: no day count, post now and repost. Collection points and
  deadline marked VERIFY.
