# usage: gl.py page out.png line[:x0:x1] ...  -> straightened line (or part) at 2x with the recognised class above each glyph
import sys, json
from PIL import Image, ImageDraw, ImageOps
from pages import line_img, HERE
page = sys.argv[1]; out = sys.argv[2]
st = json.load(open(f'{HERE}/tmp/struct_{page}.json'))
ims = []
for a in sys.argv[3:]:
    p = a.split(':'); k = int(p[0])
    im = ImageOps.autocontrast(line_img(page, k), cutoff=0.5)
    x0 = int(p[1]) if len(p) > 1 else 0; x1 = int(p[2]) if len(p) > 2 else im.width
    sc = 2.0 if x1 - x0 <= 1000 else 1900 / (x1 - x0)
    c = Image.new('L', (x1 - x0, 128 + 30), 255); c.paste(im.crop((x0, 0, x1, 128)), (0, 30))
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS); d = ImageDraw.Draw(c)
    d.text((2, 0), f'{k}', fill=0, font_size=14)
    for e in st:
        if e['line'] == k and e['kind'] != 'c' and x0 <= e['x'] < x1:
            xx = int((e['x'] - x0) * sc)
            d.text((xx - 4, 14), e['tok'], fill=0, font_size=20)
            v = e['val'] if len(e['val']) == 1 else e['val'][:3]
            d.text((xx - 4, 36), v, fill=90, font_size=18)
            if e['ws']: d.line((xx - 10, 14, xx - 10, 56), fill=150, width=1)
    ims.append(c)
W = max(c.width for c in ims); o = Image.new('L', (W, sum(c.height + 6 for c in ims)), 255); y = 0
for c in ims: o.paste(c, (0, y)); y += c.height + 6
o.save(out); print(o.size)
