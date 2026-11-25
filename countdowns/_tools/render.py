#!/usr/bin/env python3
"""Render the selected green/white countdown as a consistent dated series.

Run with the local environment: countdowns/_tools/.venv/bin/python countdowns/_tools/render.py
Existing date folders are skipped. Use a new design ID for future variations.
"""

import argparse
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / '_assets'
DESIGN_ID = 'green-white-v2'
SIZE = (1080, 1350)
SCALE = 2
GREEN = '#017B4C'
FOREST = '#0D421F'
WHITE = '#FFFFFF'
ELECTION = dt.date(2027, 1, 16)
START = dt.date(2026, 11, 25)
CHECKED = '2026-11-25'
SOURCE = 'https://inecnigeria.org/elections/calendar'


def font(size, weight=800):
    # Sora-derived display instances have merged contours and smooth Y/G joins.
    path = ASSETS / 'static' / f'WCNCountdown-{weight}.ttf'
    return ImageFont.truetype(str(path), round(size * SCALE))


def text_image(text, size, weight=800, colour=WHITE):
    face = font(size, weight)
    left, top, right, bottom = face.getbbox(text)
    layer = Image.new('RGBA', (right - left, bottom - top))
    ImageDraw.Draw(layer).text((-left, -top), text, font=face, fill=colour)
    return layer


def centred_text(image, text, top, size, weight=800, width=None, height=None):
    layer = text_image(text, size, weight)
    if width is not None or height is not None:
        target = (round(width * SCALE) if width else layer.width,
                  round(height * SCALE) if height else layer.height)
        layer = layer.resize(target, Image.Resampling.LANCZOS)
    image.alpha_composite(layer, ((image.width - layer.width) // 2, round(top * SCALE)))


def draw_instagram(draw, x, y, size, colour):
    x, y, size = x * SCALE, y * SCALE, size * SCALE
    stroke = 3 * SCALE
    draw.rounded_rectangle((x, y, x + size, y + size), radius=9 * SCALE,
                           outline=colour, width=stroke)
    inset = size * .25
    draw.ellipse((x + inset, y + inset, x + size - inset, y + size - inset),
                 outline=colour, width=stroke)
    dot = 2 * SCALE
    cx, cy = x + size * .76, y + size * .23
    draw.ellipse((cx - dot, cy - dot, cx + dot, cy + dot), fill=colour)


def draw_x(draw, x, y, size, colour):
    # Official X silhouette mapped from the same 24-unit path used in the repo.
    points = [(17.75,2.5),(20.95,2.5),(13.95,10.5),(22.18,21.4),
              (15.74,21.4),(10.69,14.8),(4.92,21.4),(1.7,21.4),
              (9.18,12.84),(1.28,2.5),(7.88,2.5),(12.44,8.53)]
    def mapped(poly):
        return [((x + px * size / 24) * SCALE, (y + py * size / 24) * SCALE)
                for px, py in poly]
    draw.polygon(mapped(points), fill=colour)
    draw.polygon(mapped([(16.63,19.5),(18.4,19.5),(7.43,4.3),(5.53,4.3)]), fill=WHITE)


def render_artwork(days, destination):
    image = Image.new('RGBA', (SIZE[0] * SCALE, SIZE[1] * SCALE), GREEN)
    logo = Image.open(ASSETS / 'wcn-horizontal-lime-white.png').convert('RGBA')
    logo_width = 280 * SCALE
    logo = logo.resize((logo_width, round(logo.height * logo_width / logo.width)),
                       Image.Resampling.LANCZOS)
    image.alpha_composite(logo, (70 * SCALE, 70 * SCALE))

    # Same tall numeral proportions and compact spacing as the selected image.
    # Two-digit forms stay within 930px; single-digit forms retain their height.
    number = text_image(str(days), 840)
    number_width = round(number.width * (650 * SCALE / number.height) * .86)
    number = number.resize((min(number_width, 930 * SCALE), 650 * SCALE),
                           Image.Resampling.LANCZOS)
    image.alpha_composite(number, ((image.width - number.width) // 2, 216 * SCALE))
    label = 'DAY TO GO' if days == 1 else 'DAYS TO GO'
    centred_text(image, label, 881, 145, width=930, height=113)
    centred_text(image, '16 JANUARY 2027', 1056, 58, weight=600, width=745, height=55)

    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 1206 * SCALE, image.width, image.height), fill=WHITE)
    handles = [('world_changersnetwork', 'instagram'), ('worldchangernet', 'x')]
    layers = [text_image(name, 27, weight=500, colour=FOREST) for name, _ in handles]
    icon, gap, group_gap = 36, 16, 76
    total_width = sum(layer.width for layer in layers) + (icon + gap) * SCALE * 2 + group_gap * SCALE
    cursor = (image.width - total_width) // 2
    for layer, (_, kind) in zip(layers, handles):
        icon_left = cursor / SCALE
        if kind == 'instagram':
            draw_instagram(draw, icon_left, 1260, icon, FOREST)
        else:
            draw_x(draw, icon_left, 1259, icon + 2, FOREST)
        cursor += (icon + gap) * SCALE
        image.alpha_composite(layer, (cursor, 1278 * SCALE - layer.height // 2))
        cursor += layer.width + group_gap * SCALE
    image.convert('RGB').resize(SIZE, Image.Resampling.LANCZOS).save(destination, optimize=True)


def deliver_date(post_date, preview=False):
    days = (ELECTION - post_date).days
    if not 1 <= days <= 52:
        raise ValueError(f'Posting date outside this campaign batch: {post_date}')
    if preview:
        path = ROOT / '_preview' / f'{days:02d}-days.png'
        path.parent.mkdir(exist_ok=True)
        render_artwork(days, path)
        return path
    folder = ROOT / post_date.isoformat()
    if folder.exists():
        expected = [f'{DESIGN_ID}.png', 'caption.txt', 'alt-text.txt', 'metadata.json']
        if not all((folder / name).is_file() for name in expected):
            raise RuntimeError(f'Incomplete existing date folder requires recovery: {folder}')
        return folder
    folder.mkdir()
    path = folder / f'{DESIGN_ID}.png'
    render_artwork(days, path)
    unit = 'day' if days == 1 else 'days'
    caption = (f'{days} {unit} to go.\n\n16 January 2027. Your vote. Your choice.\n\n'
               '#YourVoteWillCount #NigeriaDecides2027\n')
    (folder / 'caption.txt').write_text(caption)
    alt = (f'Green election countdown graphic with a small World Changers Network logo '
           f'at the top left. Large white text reads "{days} {unit.upper()} TO GO" and '
           f'"16 JANUARY 2027". A white footer lists Instagram world_changersnetwork '
           f'and X worldchangernet.\n')
    (folder / 'alt-text.txt').write_text(alt)
    metadata = {
        'posting_date': post_date.isoformat(), 'timezone': 'Africa/Lagos',
        'election_date': ELECTION.isoformat(), 'days_remaining': days,
        'design_id': DESIGN_ID, 'artwork': path.name,
        'caption': 'caption.txt', 'alt_text': 'alt-text.txt',
        'dimensions': list(SIZE), 'production_status': 'rendered',
        'review_status': 'pending_team_review', 'published': False,
        'date_source': SOURCE, 'date_checked': CHECKED,
        'pre_publication_checks': ['Reconfirm INEC election date', 'Team accuracy and visual review'],
        'artwork_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    (folder / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
    return folder


def rebuild_index():
    rows = []
    for metadata in sorted(ROOT.glob('????-??-??/metadata.json')):
        data = json.loads(metadata.read_text())
        rows.append(data)
    (ROOT / 'manifest.json').write_text(json.dumps({
        'design_id': DESIGN_ID, 'election_date': ELECTION.isoformat(),
        'source_url': SOURCE, 'date_checked': CHECKED, 'posts': rows,
    }, indent=2) + '\n')
    tracker = ROOT / 'tracker.csv'
    published = {}
    if tracker.exists():
        with tracker.open(newline='') as fh:
            published = {r['Date']: r['Published'] for r in csv.DictReader(fh)}
    with tracker.open('w', newline='') as fh:
        writer = csv.writer(fh, lineterminator='\n')
        writer.writerow(['Date', 'Topic', 'Published'])
        for row in rows:
            days = row['days_remaining']
            writer.writerow([row['posting_date'], f"{days} {'day' if days == 1 else 'days'} to go",
                             published.get(row['posting_date'], '')])
    cards, table = [], []
    for row in rows:
        date, days, artwork = row['posting_date'], row['days_remaining'], row['artwork']
        image_path = f'{date}/{artwork}'
        cards.append(f'<article><a href="{image_path}"><img loading="lazy" src="{image_path}" '
                     f'alt="{days} days to election"></a><h2>{date} · {days} '
                     f'{"day" if days == 1 else "days"}</h2><a href="{date}/caption.txt">Caption</a> · '
                     f'<a href="{date}/alt-text.txt">Alt text</a></article>')
        table.append(f'| {date} | {days} | [Image]({image_path}) | '
                     f'[Caption]({date}/caption.txt) | [Alt text]({date}/alt-text.txt) |')
    (ROOT / 'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>WCN countdowns</title>
<style>body{font:16px system-ui;background:#f3f5f3;color:#0D421F;margin:32px}h1{margin-bottom:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px;max-width:1500px}
article{background:white;padding:12px;border-radius:8px}img{width:100%;display:block}h2{font-size:16px}
a{color:#0D421F}p{max-width:850px;line-height:1.5}</style>
<h1>WCN election countdowns</h1><p>25 November 2026–15 January 2027 · 52 days to 1 day.
Green/white v2 · corrected lettering. Every export is 1080 × 1350. Click an image to open the full PNG.
All posts await team review. Reconfirm the election schedule before publishing.</p><main class="grid">'''
        + ''.join(cards) + '</main></html>')
    (ROOT / 'SCHEDULING_INDEX.md').write_text(
        '# WCN countdown scheduling index\n\n'
        '52 dates, including today, 25 November 2026, through 15 January 2027. '
        'The last image correctly says DAY TO GO. No election-day post is included.\n\n'
        'Every post awaits team review and a schedule recheck. '
        f'Election date checked {CHECKED}: [INEC calendar]({SOURCE}).\n\n'
        '| Posting date | Days left | Artwork | Caption | Alt text |\n'
        '|---|---:|---|---|---|\n' + '\n'.join(table) + '\n')


def repair_existing():
    """Stage every corrected PNG before updating the dated files and index."""
    staged = []
    for metadata in sorted(ROOT.glob('????-??-??/metadata.json')):
        row = json.loads(metadata.read_text())
        destination = metadata.parent / f'{DESIGN_ID}.png'
        temporary = destination.with_suffix('.tmp.png')
        render_artwork(row['days_remaining'], temporary)
        staged.append((metadata, row, temporary, destination))
    for metadata, row, temporary, destination in staged:
        old = metadata.parent / row['artwork']
        if old.exists() and old != destination:
            archive = ROOT / '_archive' / row['design_id'] / row['posting_date']
            archive.mkdir(parents=True, exist_ok=True)
            archived_image = archive / old.name
            if archived_image.exists():
                raise FileExistsError(f'Archive already exists: {archived_image}')
            (archive / 'metadata.json').write_text(metadata.read_text())
            old.rename(archived_image)
        temporary.replace(destination)
        row.update(artwork=destination.name, design_id=DESIGN_ID,
                   artwork_sha256=hashlib.sha256(destination.read_bytes()).hexdigest(),
                   font_rendering='Sora-derived static weights; merged contours and cleaned display Y/G joins',
                   review_status='pending_team_review')
        metadata.write_text(json.dumps(row, indent=2) + '\n')
    rebuild_index()
    print(f'Repaired {len(staged)} countdowns; old exports archived.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', action='store_true', help='Render representative dates only')
    parser.add_argument('--repair-font-rendering', action='store_true',
                        help='Regenerate existing dates with corrected Sora rendering')
    args = parser.parse_args()
    if args.repair_font_rendering:
        repair_existing()
        return
    if args.preview:
        for days in [52, 51, 40, 11, 10, 9, 1]:
            print(deliver_date(ELECTION - dt.timedelta(days=days), preview=True))
        return
    for offset in range((ELECTION - START).days):
        date = START + dt.timedelta(days=offset)
        print(deliver_date(date))
    rebuild_index()


if __name__ == '__main__':
    main()
