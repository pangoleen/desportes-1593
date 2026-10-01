# Build period-French counts in the cipher's alphabet (j->i, v->u, no accents, elisions joined).
# Clean files (modern print) are counted as they are. Dirty files (18th-century print whose long s the OCR
# read as f) are repaired first: every non-final f is f-or-s, chosen by the clean bigram / unigram counts.
# usage: lm_build.py  -> lm/words.json, lm/bigrams.json, lm/char5.json
import sys, re, json, os, glob, unicodedata, collections, itertools
from glyphs import L2C
HERE = os.path.dirname(os.path.abspath(__file__))
DIRTY = ('memoiresdelaligu', 'bub_gb_xJtZkMUIQQ8C')
def norm(t):
    t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = t.replace('œ', 'oe').replace('æ', 'ae').replace('ç', 'c').replace('ſ', 's').replace('&', ' et ')
    t = re.sub(r"[’'`]", '', t); t = re.sub(r'-\n', '', t)
    return t.replace('j', 'i').replace('v', 'u').replace('k', 'c').replace('w', 'uu')
COMMON = set('de la le et que les a en il qui ne des est pour par ce du au un nous uous ie se si plus pas son sa ses mon ma tout bien dieu roy monsieur lettre estre auoir faire fe fi fon fa fes'.split())
def paragraphs(fn):
    txt = norm(open(fn, encoding='utf-8', errors='ignore').read())
    for para in re.split(r'\n\s*\n', txt):
        ws = re.findall(r'[a-z]+', para)
        if len(ws) < 8 or sum(w in COMMON for w in ws) < max(1, len(ws) // 6): continue
        yield [w for w in ws if all(c in L2C for c in w)]
def variants(w):
    pos = [i for i, c in enumerate(w[:-1]) if c == 'f']          # final s is a round s in old print
    if not pos or len(pos) > 4: return [w]
    out = []
    for mask in range(1 << len(pos)):
        v = list(w)
        for b, p in enumerate(pos):
            if mask >> b & 1: v[p] = 's'
        out.append(''.join(v))
    return out
if __name__ == '__main__':
    files = sorted(glob.glob(f'{HERE}/corpus/*.txt'))
    clean = [f for f in files if not os.path.basename(f).startswith(DIRTY)]; dirty = [f for f in files if f not in clean]
    wc = collections.Counter(); bg = collections.Counter(); ch = collections.Counter()
    def count(ws, wt=1):
        prev = '<s>'
        for w in ws: wc[w] += wt; bg[prev + ' ' + w] += wt; prev = w
        s = ' ' + ' '.join(ws) + ' '
        for i in range(len(s) - 4): ch[s[i:i + 5]] += wt
    n = 0
    for fn in clean:
        for ws in paragraphs(fn): count(ws); n += len(ws)
    print('clean words', n, 'types', len(wc), flush=True)
    cwc = dict(wc); cbg = dict(bg); fixed = kept = dropped = 0
    for fn in dirty:
        for ws in paragraphs(fn):
            out = []; prev = '<s>'
            for w in ws:
                if 'f' in w[:-1]:
                    vs = variants(w)
                    best = max(vs, key=lambda v: (cbg.get(prev + ' ' + v, 0) * 50 + cwc.get(v, 0)))
                    if cwc.get(best, 0) == 0:
                        dropped += 1; prev = '<s>'
                        if out: count(out); n += len(out)
                        out = []; continue                        # unknown word with f: break the sequence
                    if best != w: fixed += 1
                    else: kept += 1
                    w = best
                out.append(w); prev = w
            if out: count(out); n += len(out)
        print(os.path.basename(fn), 'done; fixed', fixed, 'kept', kept, 'dropped', dropped, flush=True)
    os.makedirs(f'{HERE}/lm', exist_ok=True)
    json.dump(dict(wc), open(f'{HERE}/lm/words.json', 'w'))
    json.dump({k: c for k, c in bg.items() if c >= 2}, open(f'{HERE}/lm/bigrams.json', 'w'))
    json.dump(dict(ch), open(f'{HERE}/lm/char5.json', 'w'))
    print('total words', n, 'types', len(wc))
