# WCN election countdowns

52 dated posts: **25 November 2026 to 15 January 2027**, including today.
The countdown runs from 52 days to 1 day before the presidential and National
Assembly election on 16 January 2027. No election-day post is included.

Open [the visual index](index.html) to browse all images, or use
[the scheduling index](SCHEDULING_INDEX.md). Exports are 1080 × 1350 PNGs.

## Date folders

Each `YYYY-MM-DD/` folder contains:

- `green-white-v2.png` — the current countdown design with corrected lettering.
- `caption.txt` — a concise X caption, also usable for Instagram.
- `alt-text.txt` — accessible image description.
- `metadata.json` — date calculation, production and review status, source and file hash.

Future design versions can be added under the same date with different names.
The current batch uses only the selected tighter green/white design. The
layout was recreated as a reusable renderer using the Sora typeface and
WCN logo, avoiding generative differences across daily posts. The selected
reference image is preserved at `_assets/selected-design-reference.png`.

`tracker.csv` contains only Date, Topic and Published. Published is blank;
nothing in this batch has been published. `manifest.json` records production
details separately. All posts remain pending team accuracy and visual review.

## Sources and pre-publication review

Election date: [INEC election calendar](https://inecnigeria.org/elections/calendar),
checked 25 November 2026. Countdown calculation: election date minus the
intended posting date, in Africa/Lagos calendar dates. Reconfirm the election
schedule before publication. Captions make no procedural or candidate claims.

## Reproduce or extend

The supplied font is Sora, licensed under the SIL Open Font License included
at `_assets/Sora-OFL.txt`. WCN assets originate from
https://github.com/Igudy-Solutions/wcn-civic-campaign.

The v2 repair uses Sora-derived fixed-weight instances named WCN Countdown.
Contours are merged and the ExtraBold Y/G joins are cleaned for solid display
lettering. The original Sora font is preserved unchanged. Previous PNGs and their metadata are retained in the production workspace
under `_archive/green-white-v1/`; only corrected exports are committed here.

```sh
python3 -m venv countdowns/_tools/.venv
countdowns/_tools/.venv/bin/python -m pip install -r countdowns/_tools/requirements.txt
countdowns/_tools/.venv/bin/python countdowns/_tools/prepare_fonts.py
countdowns/_tools/.venv/bin/python countdowns/_tools/render.py --preview
countdowns/_tools/.venv/bin/python countdowns/_tools/render.py
```

The renderer skips complete existing date folders, stops on incomplete
folders, and preserves existing Published values when rebuilding the index.
It does not overwrite existing artwork. Add future designs with a new design
ID and retain this version for review history.
