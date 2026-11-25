#!/usr/bin/env python3
"""Put a voter-card face on the plain green card in ai-16-pvc-proud.png.

The AI photo came back with a blank green card. This draws a generic,
illustrative "Permanent Voter's Card" face (no coat of arms, no INEC logo,
no real names or numbers: grey bars stand in for the details), warps it onto
the card in perspective, keeps the thumb in front, and carries the photo's
own light and shading across it.

    python3 tools/pvc_card.py
writes images/ai/ai-16-pvc-proud-card.png
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "images", "ai", "ai-16-pvc-proud.png")
DST = os.path.join(ROOT, "images", "ai", "ai-16-pvc-proud-card.png")
FONT = os.path.join(ROOT, "fonts", "Sora.ttf")

W, H = 1000, 630  # ID-1 card ratio


def font(size, weight):
    f = ImageFont.truetype(FONT, size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def card_face():
    im = Image.new("RGB", (W, H), "#2c9a5c")
    d = ImageDraw.Draw(im)
    # soft diagonal guilloche lines
    for i in range(-H, W, 14):
        d.line([(i, H), (i + H, 0)], fill="#33a464", width=3)
    for k in range(0, 9):
        y0 = 250 + k * 34
        pts = [(x, y0 + 14 * np.sin(x / 70 + k)) for x in range(0, W + 10, 10)]
        d.line(pts, fill="#3fb071", width=2)
    # header band
    d.rectangle([0, 0, W, 170], fill="#f4f7f2")
    d.rectangle([0, 170, W, 182], fill="#0d421f")
    d.text((W / 2, 52), "FEDERAL REPUBLIC OF NIGERIA", font=font(40, 600), fill="#0d421f", anchor="mm")
    d.text((W / 2, 118), "PERMANENT VOTER'S CARD", font=font(62, 800), fill="#14713b", anchor="mm")
    # portrait
    px0, py0, px1, py1 = 48, 216, 318, 576
    d.rounded_rectangle([px0, py0, px1, py1], 14, fill="#e3e9e3", outline="#f4f7f2", width=6)
    cx = (px0 + px1) / 2
    d.ellipse([cx - 66, py0 + 60, cx + 66, py0 + 200], fill="#8fa596")
    d.pieslice([cx - 125, py0 + 215, cx + 125, py0 + 470], 180, 360, fill="#8fa596")
    # detail rows: label + bar, no real data
    f = font(26, 700)
    x = 362
    rows = [("VIN", 520), ("NAME", 560), ("DATE OF BIRTH", 300), ("POLLING UNIT", 470)]
    y = 214
    for label, w in rows:
        d.text((x, y), label, font=f, fill="#e6f2e9")
        d.rounded_rectangle([x, y + 38, x + w, y + 62], 8, fill="#f4f7f2")
        y += 92
    # chip
    d.rounded_rectangle([850, 470, 950, 560], 12, fill="#d9b85c", outline="#a8893a", width=4)
    d.line([(850, 515), (950, 515)], fill="#a8893a", width=4)
    d.line([(900, 470), (900, 560)], fill="#a8893a", width=4)
    return im


def lines():
    # edges of the green card, fitted from the photo (y = a*x + b, x = c*y + d)
    top = (-0.02863, 384.87)
    bot = (-0.02772, 508.45)
    left = (0.03680, 247.10)
    right = (0.04025, 443.97)
    return top, bot, left, right


def meet(h, v):
    a, b = h
    c, d = v
    y = (a * d + b) / (1 - a * c)
    return c * y + d, y


def perspective_coeffs(dst_pts, src_pts):
    # coefficients mapping output (photo) coords -> input (card face) coords
    A, B = [], []
    for (x, y), (u, v) in zip(dst_pts, src_pts):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


def main():
    photo = Image.open(SRC).convert("RGB")
    a = np.asarray(photo).astype(np.float32)
    top, bot, left, right = lines()
    quad = [meet(top, left), meet(top, right), meet(bot, right), meet(bot, left)]
    coeffs = perspective_coeffs(quad, [(0, 0), (W, 0), (W, H), (0, H)])
    face = card_face()
    # rounded card corners on the face itself
    rmask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(rmask).rounded_rectangle([0, 0, W - 1, H - 1], 40, fill=255)
    warped = face.transform(photo.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    wmask = rmask.transform(photo.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)

    # where the green card actually shows (so the thumb stays in front)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = ((g > 110) & (g - r > 35) & (g - b > 10)).astype(np.uint8) * 255
    gmask = Image.fromarray(green).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    mask = np.minimum(np.asarray(wmask, np.float32), np.asarray(gmask, np.float32)) / 255.0

    # carry the photo's light across the card
    lum = a.mean(axis=2)
    inside = mask > 0.9
    shade = (lum / lum[inside].mean())[..., None]
    shade = np.clip(shade, 0.75, 1.2)
    w = np.asarray(warped).astype(np.float32) * shade
    # a touch of the photo's grain/softness
    out = a * (1 - mask[..., None]) + w * mask[..., None]
    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
    img.save(DST)
    print("wrote", DST, "quad", [tuple(round(v, 1) for v in p) for p in quad])


if __name__ == "__main__":
    main()
