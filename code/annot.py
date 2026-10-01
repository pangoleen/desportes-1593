# Annotated line sheets: the decoded letter (or sign word) is printed above each glyph.
# usage: annot.py page k0 k1 models...   -> tmp/an_<page>_<kk>.png ; also tmp/struct_<page>.json
import sys, re, json, os
from PIL import Image, ImageDraw, ImageOps
import ctc, recog
from pages import nlines, line_img, HERE
from decode import LM, decode, letters
from read_page import extra_words

def read_struct(page, ms, lm, **kw):
    rng = json.load(open(f'{HERE}/lines/{page}_ranges.json')) if os.path.exists(f'{HERE}/lines/{page}_ranges.json') else {}
    T, G, A, X, owner = [], [], [], [], []
    for k in range(nlines(page)):
        r = rng.get(str(k))
        if r == []: continue
        segs = [tuple(x) for x in r] if r else [None]
        for si, seg in enumerate(segs):
            toks, alts, hyps, xs = recog.recognise(ms, page, k, [seg] if seg else None, with_pos=True)
            t, g, a, x = recog.to_stream(toks, alts, xs)
            if not t: continue
            lead = seg is None or (si == 0 and seg[0] == 0)
            g[0] = None if lead else True
            if not lead: T.append('|'); G.append(True); A.append([('|', 0.0)]); X.append(0); owner.append(k)
            T += t; G += g; A += a; X += x; owner += [k] * len(t)
            if seg is not None and seg[1] < 3300: T.append('|'); G.append(True); A.append([('|', 0.0)]); X.append(0); owner.append(k)
    out = []; i = 0
    while i < len(T):
        if T[i] == '|': out.append({'line': owner[i], 'tok': '|', 'val': '[clair]', 'x': 0, 'ws': True, 'kind': 'c'}); i += 1; continue
        j = i
        while j < len(T) and T[j] != '|': j += 1
        segs = decode(T[i:j], G[i:j], lm, A[i:j], **kw)
        vals = letters(segs, T[i:j]); start = {a: kind for a, b, w, kind in segs}
        prevkind = None
        for a, b, w, kind in segs:
            for q in range(a, b):
                ws = (q == a) and not (kind == 'o' and prevkind == 'o')
                out.append({'line': owner[i + q], 'tok': T[i + q], 'val': vals[q], 'x': X[i + q], 'ws': ws, 'kind': kind, 'alt': [c for c, _ in A[i + q][1:]]})
            prevkind = kind
        i = j
    return out

def text_lines(struct):
    res = {}
    for e in struct:
        s = res.setdefault(e['line'], [])
        v = e['val'] if e['kind'] != 'o' else e['val'].upper()
        if e['ws'] and s: s.append(' ')
        s.append(v)
    return {k: ''.join(v) for k, v in res.items()}

def sheet(page, k, ents, nseg=4, scale=1.5, H=128):
    im = ImageOps.autocontrast(line_img(page, k, H), cutoff=0.5)
    W = im.width; ov = 60; seg = (W + (nseg - 1) * ov) // nseg; top = 30
    out = Image.new('L', (int(seg * scale), int((H + top) * scale) * nseg), 255)
    for i in range(nseg):
        x0 = i * (seg - ov)
        c = Image.new('L', (seg, H + top), 255); c.paste(im.crop((x0, 0, min(W, x0 + seg), H)), (0, top))
        c = c.resize((int(seg * scale), int((H + top) * scale)), Image.LANCZOS)
        d = ImageDraw.Draw(c)
        for e in ents:
            if x0 <= e['x'] < x0 + seg:
                xx = int((e['x'] - x0) * scale)
                v = e['val'] if e['kind'] != 'o' else e['val'].upper()
                if e['ws']: d.line((xx - 8, 4, xx - 8, 40), fill=120, width=2)
                d.text((xx - 4, 2), v, fill=0, font_size=26)
                if e.get('alt'): d.text((xx - 2, 30), '/' + ''.join(e['alt']), fill=90, font_size=14)
        out.paste(c, (0, i * int((H + top) * scale)))
    return out

if __name__ == '__main__':
    page = sys.argv[1]; k0, k1 = int(sys.argv[2]), int(sys.argv[3]); ms = recog.load(sys.argv[4:])
    lm = LM(extra_words=extra_words())
    st = read_struct(page, ms, lm)
    json.dump(st, open(f'{HERE}/tmp/struct_{page}.json', 'w'))
    tl = text_lines(st)
    open(f'{HERE}/tmp/read_{page}.txt', 'w').write('\n'.join(f'{k:2d}  {v}' for k, v in sorted(tl.items())) + '\n')
    for k in range(k0, k1 + 1):
        ents = [e for e in st if e['line'] == k and e['kind'] != 'c']
        if ents: sheet(page, k, ents).save(f'{HERE}/tmp/an_{page}_{k:02d}.png')
    print('done', page)
