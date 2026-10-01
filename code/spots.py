# usage: spots.py page out.png line:idx[:halfwidth] ...   (idx = glyph index in the line, spaces not counted)
import sys, json
from PIL import Image, ImageDraw, ImageOps
from pages import line_img, HERE
page = sys.argv[1]; out = sys.argv[2]
st = json.load(open(f'{HERE}/tmp/struct_{page}.json'))
by = {}
for e in st:
    if e['kind'] != 'c': by.setdefault(e['line'], []).append(e)
ims = []
for a in sys.argv[3:]:
    p = a.split(':'); k = int(p[0]); idx = int(p[1]); hw = int(p[2]) if len(p) > 2 else 260
    es = by[k]; idx = max(0, min(idx, len(es) - 1)); x = es[idx]['x']
    im = ImageOps.autocontrast(line_img(page, k), cutoff=0.5)
    x0 = max(0, x - hw); x1 = min(im.width, x + hw)
    c = Image.new('L', (x1 - x0, 128 + 26), 255); c.paste(im.crop((x0, 0, x1, 128)), (0, 26))
    c = c.resize((int(c.width * 1.8), int(c.height * 1.8)), Image.LANCZOS); d = ImageDraw.Draw(c)
    d.text((2, 0), f'{k}:{idx}', fill=0, font_size=18)
    for j, e in enumerate(es):
        if x0 <= e['x'] < x1:
            d.text((int((e['x'] - x0) * 1.8) - 4, 18), e['val'], fill=0, font_size=22)
            if j == idx: d.line((int((e['x'] - x0) * 1.8) - 6, 46, int((e['x'] - x0) * 1.8) + 20, 46), fill=0, width=3)
    ims.append(c)
W = max(c.width for c in ims); o = Image.new('L', (W, sum(c.height + 6 for c in ims)), 255); y = 0
for c in ims: o.paste(c, (0, y)); y += c.height + 6
o.save(out); print(o.size)
