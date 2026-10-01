# usage: show.py page k [nseg] [scale] [out]  -> stacked segments of the straightened line with an x ruler
import sys, numpy as np
from PIL import Image, ImageDraw, ImageOps
from pages import line_img
def sheet(page, k, nseg=3, scale=1.3, H=128):
    im = ImageOps.autocontrast(line_img(page, k, H), cutoff=0.5)
    W = im.width; ov = 60; seg = (W + (nseg - 1) * ov) // nseg
    out = Image.new('L', (int(seg * scale), int((H + 14) * scale) * nseg), 255)
    for i in range(nseg):
        x0 = i * (seg - ov)
        c = Image.new('L', (seg, H + 14), 255); c.paste(im.crop((x0, 0, min(W, x0 + seg), H)), (0, 14))
        d = ImageDraw.Draw(c)
        for x in range((x0 // 100 + 1) * 100, x0 + seg, 100):
            d.line((x - x0, 0, x - x0, 6), fill=0); d.text((x - x0 + 2, 0), str(x), fill=0, font_size=11)
        c = c.resize((int(seg * scale), int((H + 14) * scale)), Image.LANCZOS)
        out.paste(c, (0, i * int((H + 14) * scale)))
    return out
if __name__ == '__main__':
    page = sys.argv[1]; k = int(sys.argv[2]); nseg = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    scale = float(sys.argv[4]) if len(sys.argv) > 4 else 1.3
    out = sys.argv[5] if len(sys.argv) > 5 else f'tmp/{page}_{k:02d}.png'
    sheet(page, k, nseg, scale).save(out); print(out)
