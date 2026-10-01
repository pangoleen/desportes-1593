# usage: wspot.py page out.png line:word[:pad] ...  -> zoom on the n-th decoded word (0-based, [clair] counts) of a line
import sys, json
from PIL import Image, ImageDraw, ImageOps
from pages import line_img, HERE
page = sys.argv[1]; out = sys.argv[2]
st = json.load(open(f'{HERE}/tmp/struct_{page}.json'))
lines = {}
for e in st:
    L = lines.setdefault(e['line'], [])
    if e['kind'] == 'c': L.append([e]); continue
    if e['ws'] or not L or L[-1][0]['kind'] == 'c': L.append([e])
    else: L[-1].append(e)
ims = []
for a in sys.argv[3:]:
    p = a.split(':'); k = int(p[0]); wi = int(p[1]); pad = int(p[2]) if len(p) > 2 else 170
    ws = lines[k]; w = ws[min(wi, len(ws) - 1)]
    x0 = max(0, w[0]['x'] - pad); x1 = w[-1]['x'] + pad
    im = ImageOps.autocontrast(line_img(page, k), cutoff=0.5); x1 = min(im.width, x1)
    c = Image.new('L', (x1 - x0, 128 + 24), 255); c.paste(im.crop((x0, 0, x1, 128)), (0, 24))
    sc = 2.0; c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS); d = ImageDraw.Draw(c)
    d.text((2, 0), f'{k}:{wi}', fill=0, font_size=16)
    for ww in ws:
        for e in ww:
            if e['kind'] != 'c' and x0 <= e['x'] < x1:
                d.text((int((e['x'] - x0) * sc) - 4, 18), e['tok'], fill=0, font_size=22)
    ims.append(c)
W = max(c.width for c in ims); o = Image.new('L', (W, sum(c.height + 6 for c in ims)), 255); y = 0
for c in ims: o.paste(c, (0, y)); y += c.height + 6
o.save(out); print(o.size)
