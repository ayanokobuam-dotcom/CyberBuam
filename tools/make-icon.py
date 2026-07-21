#!/usr/bin/env python3
"""Generates a flat-vector 'hacker in a hoodie' app icon in cyberbuam's
cyan/dark palette, at 512x512 (plus a downscaled 192x192)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

OUT_DIR = Path(__file__).resolve().parents[1]

BG = (3, 8, 13, 255)
BG_GLOW = (10, 28, 36, 255)
HOODIE = (12, 22, 30, 255)
HOODIE_LIGHT = (20, 36, 46, 255)
FACE_SHADOW = (2, 5, 8, 255)
CYAN = (57, 214, 255, 255)
GREEN = (0, 255, 136, 255)
CYAN_DIM = (57, 214, 255, 90)


def make_icon(size):
    S = 4  # supersample factor for smoother edges
    img = Image.new("RGBA", (size * S, size * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = size * S

    # rounded-square app background
    radius = int(s * 0.22)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=radius, fill=BG)

    # soft radial glow behind the figure
    glow = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([s * 0.18, s * 0.12, s * 0.82, s * 0.76], fill=BG_GLOW)
    glow = glow.filter(ImageFilter.GaussianBlur(s * 0.06))
    img.alpha_composite(glow)

    # shoulders / hoodie body (wide rounded trapezoid)
    body = [
        (s * 0.50, s * 0.42),
        (s * 0.86, s * 0.62),
        (s * 0.90, s * 0.98),
        (s * 0.10, s * 0.98),
        (s * 0.14, s * 0.62),
    ]
    d.polygon(body, fill=HOODIE)

    # hood dome
    d.pieslice([s * 0.26, s * 0.14, s * 0.74, s * 0.62], 180, 360, fill=HOODIE)
    d.rounded_rectangle([s * 0.26, s * 0.36, s * 0.74, s * 0.60], radius=int(s * 0.06), fill=HOODIE)

    # subtle highlight along the hood rim (light catching the fabric edge)
    d.arc([s * 0.27, s * 0.15, s * 0.73, s * 0.61], 200, 340, fill=HOODIE_LIGHT, width=max(2, int(s * 0.012)))

    # hood opening / face shadow (deep, featureless — the "faceless hacker" look)
    d.ellipse([s * 0.36, s * 0.30, s * 0.64, s * 0.60], fill=FACE_SHADOW)

    # glowing terminal-style eyes
    eye_w, eye_h = s * 0.075, s * 0.028
    eye_y = s * 0.435
    for cx in (s * 0.435, s * 0.565):
        d.rounded_rectangle(
            [cx - eye_w / 2, eye_y - eye_h / 2, cx + eye_w / 2, eye_y + eye_h / 2],
            radius=eye_h / 2, fill=CYAN,
        )
    eyes_glow = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    egd = ImageDraw.Draw(eyes_glow)
    for cx in (s * 0.435, s * 0.565):
        egd.ellipse([cx - eye_w, eye_y - eye_h * 2, cx + eye_w, eye_y + eye_h * 2], fill=CYAN_DIM)
    eyes_glow = eyes_glow.filter(ImageFilter.GaussianBlur(s * 0.02))
    img.alpha_composite(eyes_glow)
    # redraw crisp eyes on top of the glow
    for cx in (s * 0.435, s * 0.565):
        d.rounded_rectangle(
            [cx - eye_w / 2, eye_y - eye_h / 2, cx + eye_w / 2, eye_y + eye_h / 2],
            radius=eye_h / 2, fill=CYAN,
        )

    # drawstrings
    d.line([(s * 0.44, s * 0.58), (s * 0.41, s * 0.78)], fill=(30, 46, 56, 255), width=max(2, int(s * 0.012)))
    d.line([(s * 0.56, s * 0.58), (s * 0.59, s * 0.78)], fill=(30, 46, 56, 255), width=max(2, int(s * 0.012)))
    for pt in [(s * 0.41, s * 0.78), (s * 0.59, s * 0.78)]:
        d.ellipse([pt[0] - s * 0.015, pt[1] - s * 0.015, pt[0] + s * 0.015, pt[1] + s * 0.015], fill=CYAN)

    img = img.resize((size, size), Image.LANCZOS)
    return img


for size, name in [(512, "icon-512.png"), (192, "icon-192.png")]:
    icon = make_icon(size)
    icon.save(OUT_DIR / name)
    print("wrote", OUT_DIR / name)
