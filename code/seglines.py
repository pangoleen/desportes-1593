# usage: seglines.py page  -> lines/<page>.json: angle, pitch, per-line centre curves (piecewise linear in x)
import sys, json, os, numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import uniform_filter1d
from pages import BLOCKS, HERE
page = sys.argv[1]; thr = 140; NS = 12
c, x0, y0, x1, y1 = BLOCKS[page]
im = Image.open(f'{HERE}/img/c{c}.jpg').convert('L').crop((x0, y0, x1, y1))
best = None
for ang in np.arange(-2.0, 2.01, 0.1):
    r = im.rotate(ang, resample=Image.BILINEAR, fillcolor=255)
    p = (np.asarray(r) < thr).sum(1).astype(float); v = uniform_filter1d(p, 7).var()
    if best is None or v > best[0]: best = (v, ang, r, p)
v, ang, rot, prof = best
A = np.asarray(rot) < thr
sm = uniform_filter1d(prof, 15)
z = sm - sm.mean(); ac = np.correlate(z, z, 'full')[len(z) - 1:]
pitch = 60 + int(np.argmax(ac[60:200]))
sm2 = uniform_filter1d(prof, int(pitch * 0.5))
peaks = [i for i in range(2, len(sm2) - 2) if sm2[i] >= sm2[i - 1] and sm2[i] > sm2[i + 1] and sm2[i] > 0.2 * np.percentile(sm2, 90)]
m = []
for p in peaks:
    if m and p - m[-1] < 0.6 * pitch:
        if sm2[p] > sm2[m[-1]]: m[-1] = p
    else: m.append(p)
# local centres per vertical strip, propagated from the middle outward
W = A.shape[1]; edges = np.linspace(0, W, NS + 1).astype(int); xc = ((edges[:-1] + edges[1:]) / 2).tolist()
P = [uniform_filter1d(A[:, edges[s]:edges[s + 1]].sum(1).astype(float), int(pitch * 0.45)) for s in range(NS)]
C = np.zeros((len(m), NS))
mid = NS // 2
def local(s, guess):
    lo = max(0, int(guess - 0.3 * pitch)); hi = min(A.shape[0], int(guess + 0.3 * pitch))
    seg = P[s][lo:hi]
    if seg.max() < 0.15 * P[s].max(): return guess
    return lo + int(np.argmax(seg))
for k, g in enumerate(m):
    C[k, mid] = local(mid, g)
    for s in range(mid + 1, NS): C[k, s] = local(s, C[k, s - 1])
    C[k, mid - 1] = local(mid - 1, C[k, mid])
    for s in range(mid - 2, -1, -1): C[k, s] = local(s, C[k, s + 1])
# smooth each curve with a quadratic fit
xs = np.array(xc)
for k in range(len(m)):
    co = np.polyfit(xs, C[k], 2); C[k] = np.polyval(co, xs)
os.makedirs(f'{HERE}/lines', exist_ok=True)
json.dump({'angle': float(ang), 'pitch': pitch, 'xc': xc, 'centres': C.round(1).tolist()}, open(f'{HERE}/lines/{page}.json', 'w'))
print(page, 'angle', round(float(ang), 2), 'pitch', pitch, 'lines', len(m))
d = rot.convert('RGB'); dr = ImageDraw.Draw(d)
for k in range(len(m)):
    pts = [(xc[s], C[k, s]) for s in range(NS)]
    dr.line(pts, fill=(255, 0, 0), width=4); dr.text((5, C[k, 0] - 50), str(k), fill=(0, 0, 255), font_size=50)
d.resize((d.width // 4, d.height // 4)).save(f'{HERE}/tmp/{page}_lines.jpg', quality=70)
