# Read an unread page: ensemble glyphs -> decoder. usage: read_page.py page models...
# Output: tmp/read_<page>.txt with, per line, the glyph string and the decoded text.
import sys, re, json, os
import ctc, recog
from glyphs import read_gold, SPACE
from pages import nlines, HERE
from decode import LM, decode, render, letters, SIGNWORD
from eval_e2e import train_words

def extra_words():
    rows = [r for p in ('f188v', 'f176r', 'f176v') if os.path.exists(f'{HERE}/gold/{p}.txt') for r in read_gold(p)]
    ex = train_words(rows, set())
    for fn in ('f177_plain.txt', 'prior/bourdeau/f185_plain.txt', 'context_words.txt'):
        if not os.path.exists(f'{HERE}/{fn}'): continue
        for ln in open(f'{HERE}/{fn}'):
            if ln.startswith('#'): continue
            ex += [w.replace('v', 'u').replace('j', 'i') for w in re.findall(r'[a-z]+', ln.lower())]
    return ex

def read(page, ms, lm, out=None, **kw):
    rng = json.load(open(f'{HERE}/lines/{page}_ranges.json')) if os.path.exists(f'{HERE}/lines/{page}_ranges.json') else {}
    T, G, A, owner = [], [], [], []; lines = {}
    for k in range(nlines(page)):
        r = rng.get(str(k))
        if r == []: continue
        segs = [tuple(x) for x in r] if r else [None]
        for si, seg in enumerate(segs):                                # each cipher stretch of a mixed line apart
            toks, alts, hyps = recog.recognise(ms, page, k, [seg] if seg else None)
            t, g, a = recog.to_stream(toks, alts)
            if not t: continue
            g[0] = None if (seg is None or (si == 0 and seg[0] == 0)) else True
            if seg is not None and not (si == 0 and seg[0] == 0): T.append('|'); G.append(True); A.append([('|', 0.0)]); owner.append(k)
            lines.setdefault(k, []).append(''.join(toks))
            T += t; G += g; A += a; owner += [k] * len(t)
            if seg is not None and seg[1] < 3300: T.append('|'); G.append(True); A.append([('|', 0.0)]); owner.append(k)
    # decode stretches between '|' marks (clear text interrupts the cipher there)
    res = {}
    i = 0
    while i < len(T):
        if T[i] == '|': res.setdefault(owner[i], []).append('[clair]'); i += 1; continue
        j = i
        while j < len(T) and T[j] != '|': j += 1
        segs = decode(T[i:j], G[i:j], lm, A[i:j], **kw)
        for a, b, w, kind in segs:
            k = owner[i + a]
            res.setdefault(k, []).append(('{' + w + '}') if kind == 'o' else ('[#]' if w == '#' else w))
        i = j
    lines_out = []
    for k in sorted(lines):
        txt = ' '.join(res.get(k, []))
        txt = re.sub(r'\} \{', '', txt)
        lines_out.append(f'{k:2d} G  ' + ' | '.join(lines[k])); lines_out.append(f'{k:2d} T  ' + txt)
    s = '\n'.join(lines_out)
    if out: open(out, 'w').write(s + '\n')
    return s

if __name__ == '__main__':
    page = sys.argv[1]; ms = recog.load(sys.argv[2:])
    lm = LM(extra_words=extra_words())
    print(read(page, ms, lm, out=f'{HERE}/tmp/read_{page}.txt'))
