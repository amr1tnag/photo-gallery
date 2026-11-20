"""Make the web-ready image files the site serves.

For every img/NN.jpg this writes NN-640.webp, NN-1200.webp and NN-1800.webp,
and rebuilds img/meta.js (each photo's size plus a tiny blurred placeholder).

Run from the project folder after adding a photo:
    python tools/make_sizes.py
Needs Pillow:  python -m pip install pillow
"""
import base64
import glob
import io
import json
import os

from PIL import Image

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")
meta = {}
for f in sorted(glob.glob(os.path.join(IMG, "[0-9][0-9].jpg"))):
    n = os.path.basename(f)[:2]
    im = Image.open(f).convert("RGB")
    for w in (640, 1200, 1800):
        c = im.copy()
        c.thumbnail((w, w * 2))
        c.save(os.path.join(IMG, f"{n}-{w}.webp"), "WEBP", quality=78 if w < 1800 else 82, method=6)
    t = im.copy()
    t.thumbnail((24, 24))
    b = io.BytesIO()
    t.save(b, "WEBP", quality=40)
    meta[n] = {"w": im.width, "h": im.height,
               "q": "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()}
    print("done", n)

with open(os.path.join(IMG, "meta.js"), "w") as out:
    out.write("window.PHOTO_META=" + json.dumps(meta, separators=(",", ":")) + ";\n")
print(f"{len(meta)} photos -> img/meta.js")
