# Sheet of all code signs ('#' tokens) of a page. usage: signs.py page out.png
import sys, json
from PIL import Image, ImageDraw, ImageOps
from pages import line_img, HERE
page = sys.argv[1]; out = sys.argv[2]
st = json.load(open(f'{HERE}/tmp/struct_{page}.json'))
by = {}
for e in st:
    if e['kind'] != 'c': by.setdefault(e['line'], []).append(e)
cells = []
for k, es in sorted(by.items()):
    im = None
    for j, e in enumerate(es):
        if e['tok'] != '#': continue
        if im is None: im = ImageOps.autocontrast(line_img(page, k), cutoff=0.5)
        x = e['x']; c = Image.new('L', (230, 150), 255); c.paste(im.crop((max(0, x - 100), 0, x + 130, 128)), (0, 22))
        d = ImageDraw.Draw(c); d.text((2, 2), f'{k}:{j}', fill=0, font_size=16); d.line((95, 20, 125, 20), fill=0, width=2)
        cells.append(c)
n = len(cells); cols = 6; rows = (n + cols - 1) // cols
o = Image.new('L', (cols * 234, rows * 154), 255)
for i, c in enumerate(cells): o.paste(c, ((i % cols) * 234, (i // cols) * 154))
o.save(out); print(page, n, o.size)
