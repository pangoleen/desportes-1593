# Page blocks, deskew and straightened line crops. Crops come from the canvas on demand (the disk is nearly full).
import json, os, numpy as np
from functools import lru_cache
from PIL import Image
BLOCKS = {  # page: (canvas, x0, y0, x1, y1)
 'f176r': (327, 930, 540, 4420, 5680),
 'f176v': (328, 1030, 600, 4560, 5640),
 'f188v': (352, 560, 540, 4200, 3100),
 'f189':  (353, 1020, 1150, 4450, 4800),
 'f186r': (347, 700, 1100, 4020, 6080),
 'f186v': (348, 800, 1080, 4180, 4520),
}
HERE = os.path.dirname(os.path.abspath(__file__))
def meta(page): return json.load(open(f'{HERE}/lines/{page}.json'))
@lru_cache(maxsize=8)
def block(page):
    c, x0, y0, x1, y1 = BLOCKS[page]
    im = Image.open(f'{HERE}/img/c{c}.jpg').convert('L').crop((x0, y0, x1, y1))
    return np.asarray(im.rotate(meta(page)['angle'], resample=Image.BICUBIC, fillcolor=255))
def nlines(page): return len(meta(page)['centres'])
@lru_cache(maxsize=512)
def line_arr(page, k, H=128):
    """Straightened line k as a uint8 array of height H (centre curve mapped to the middle row)."""
    m = meta(page); A = block(page); W = A.shape[1]
    yc = np.interp(np.arange(W), m['xc'], m['centres'][k])
    out = np.full((H, W), 255, np.uint8)
    top = np.round(yc - H / 2).astype(int)
    for x in range(W):
        a = top[x]; lo = max(0, a); hi = min(A.shape[0], a + H)
        if hi > lo: out[lo - a:hi - a, x] = A[lo:hi, x]
    return out
def line_img(page, k, H=128): return Image.fromarray(line_arr(page, k, H))
