# WCN Monthly Masterclass flyers

One team member teaches a masterclass on the last Friday of each month.
Each session gets a square Instagram flyer (1080x1080, Arkcore 25 Nov; `--portrait` gives 1080x1350) in WCN brand
(Sora, lime `#D1DD25`, forest `#0D421F`, WCN logo top left).

| Path | What it holds |
| --- | --- |
| `Masterclass/schedule.csv` | **The schedule.** One row per session. Edit this, not the script |
| `images/hosts/` | Every host's studio photo, used as supplied (background kept) |
| `tools/masterclass.py` | The template. Renders a row into `Masterclass/<date> - <Host>/` |
| `Masterclass/<date> - <Host>/` | `flyer-brutal.png` (what we post) and `captions.md` (Instagram and X captions) |

## Schedule columns

| Column | What goes in it |
| --- | --- |
| Date | `YYYY-MM-DD` |
| Title | Main line. The last word (two for long titles) goes lime |
| Subtitle | Optional second line under the title |
| Highlight | Optional words from the title to put in the lime box, e.g. `10x`. Blank = last word or two |
| Host / Also known as | Full name, and a nickname shown in brackets |
| Photo | File name in `images/hosts/` |
| What you will learn | Optional, up to three points separated by `\|`. Arkcore (25 Nov): leave blank, no learn list on flyers |
| Time / Platform | Leave blank and the flyer says "To be announced" |
| Photo position | Optional CSS crop, e.g. `50% 15%`, if a face is cut off |
| Status | `planned`, `draft`, `approved`, `posted` |

A row with no Title is skipped.

## Render

```bash
python3 tools/masterclass.py 2026-11-27                 # square neubrutalism flyer (the chosen look)
python3 tools/masterclass.py 2026-11-27 --portrait      # all three layouts, portrait
python3 tools/masterclass.py 2026-12-18 --layout pass   # one layout
python3 tools/masterclass.py --all                      # every titled row
```

**`brutal` (neubrutalism, square) is the chosen look (Arkcore, 25 Nov).** Other layouts: `pass`: light, photo on a WCN
speaker pass hanging from a lanyard. Options: `stamp` (light, centred title, photo
as a postage stamp with a date sticker) and `bold` (lime, giant MASTERCLASS, photo
with a forest offset block), and `brutal` (neubrutalism: thick borders, hard
shadows, lime stickers; square too). The dark `arch` and `card` layouts were dropped.
Needs Google Chrome, Python 3 and Pillow, like the rest of the repo.

## Hosts on file

Goodness Igunma (iGoody), David Osaro, Tabitha Jedidiah, Abigail Onajinrin,
Anu Alade-Williams (Annie), Miracle, Vincent Odeh, Othniel Agera.
