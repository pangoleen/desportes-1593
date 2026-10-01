# Ensemble recognition of straightened lines: greedy CTC per model, token-level vote across models.
import sys, json, os, math, collections, numpy as np, torch
import ctc
from glyphs import CLASSES, SPACE
from pages import nlines, HERE

def load(files):
    ms = []
    for f in files:
        rnn = 128 if '_r' in os.path.basename(f) else 0
        m = ctc.Net(rnn).to(ctc.DEV).to(memory_format=torch.channels_last); m.load_state_dict(torch.load(f, map_location=ctc.DEV)); m.eval(); ms.append(m)
    return ms

def align(a, b):
    """edit alignment of sequences a (primary) and b; returns list of (i or None, j or None)"""
    n, m = len(a), len(b)
    D = np.zeros((n + 1, m + 1), np.int32); D[:, 0] = np.arange(n + 1); D[0, :] = np.arange(m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + (a[i - 1] != b[j - 1]))
    i, j = n, m; out = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i, j] == D[i - 1, j - 1] + (a[i - 1] != b[j - 1]): out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i > 0 and D[i, j] == D[i - 1, j] + 1: out.append((i - 1, None)); i -= 1
        else: out.append((None, j - 1)); j -= 1
    return out[::-1]

def vote(hyps):
    """token-level majority vote; returns (tokens, alts) where alts[i] = [(class, logp), ...] sorted, first = winner"""
    prim = hyps[0]; M = len(hyps)
    votes = [collections.Counter({c: 1}) for c in prim]            # per primary position
    ins = [collections.Counter() for _ in range(len(prim) + 1)]    # inserted tokens before primary position i
    for h in hyps[1:]:
        pos = 0
        for i, j in align(prim, h):
            if i is not None and j is not None: votes[i][h[j]] += 1; pos = i + 1
            elif i is not None: votes[i][''] += 1; pos = i + 1
            else: ins[pos][h[j]] += 1
    toks, alts = [], []
    def emit(counter, total):
        ranked = sorted(counter.items(), key=lambda kv: -kv[1])
        return [(c, math.log(v / total)) for c, v in ranked]
    for i in range(len(prim) + 1):
        for c, v in ins[i].items():
            if v * 2 > M: toks.append(c); alts.append([(c, math.log(v / M)), ('', math.log(max(M - v, 0.3) / M))])
        if i == len(prim): break
        r = emit(votes[i], M)
        if r[0][0] == '' and r[0][1] > math.log(0.5): continue       # majority says: no token here
        if r[0][0] == '': r = r[1:] + r[:1]
        toks.append(r[0][0]); alts.append(r)
    return toks, alts

def recognise(models, page, k, ranges=None, with_pos=False):
    a, off = ctc.prep(page, k, ranges, with_offset=True)
    lps = [ctc.logprobs(m, a)[: a.shape[1] // 4 + 2] for m in models]
    hyps = [ctc.greedy(lp) for lp in lps]
    toks, alts = vote(hyps)
    if not with_pos: return toks, alts, hyps
    # x position (original line pixels) of each voted token, taken from the model whose string is closest
    best = min(range(len(models)), key=lambda i: ctc.edit(hyps[i], ''.join(toks)))
    gp = ctc.greedy_pos(lps[best]); xs = [None] * len(toks)
    for i, j in align(''.join(toks), hyps[best]):
        if i is not None and j is not None: xs[i] = int(off + gp[j][1] * 8 + 12)
    last = int(off)
    for i in range(len(xs)):
        if xs[i] is None: xs[i] = last + 30
        xs[i] = int(xs[i]); last = xs[i]
    return toks, alts, hyps, xs

def to_stream(toks, alts, xs=None):
    """drop space tokens -> (glyph tokens, gaps, alts without spaces[, x positions])"""
    T, G, A, X = [], [], [], []; gap = True
    for i, (t, al) in enumerate(zip(toks, alts)):
        if t == SPACE: gap = True; continue
        al2 = [(c, lp) for c, lp in al if c not in (SPACE, '')] or [(t, 0.0)]
        T.append(t); G.append(gap); A.append(al2); gap = False
        if xs is not None: X.append(xs[i])
    return (T, G, A, X) if xs is not None else (T, G, A)

if __name__ == '__main__':
    page = sys.argv[1]; files = sys.argv[2:]
    ms = load(files)
    rng = json.load(open(f'{HERE}/lines/{page}_ranges.json')) if os.path.exists(f'{HERE}/lines/{page}_ranges.json') else {}
    out = []
    for k in range(nlines(page)):
        r = rng.get(str(k))
        if r == []: continue                                          # line without cipher
        toks, alts, hyps = recognise(ms, page, k, [tuple(x) for x in r] if r else None)
        out.append({'line': k, 'toks': ''.join(toks), 'alts': alts, 'hyps': hyps})
        print(k, ''.join(toks))
    json.dump(out, open(f'{HERE}/tmp/recog_{page}.json', 'w'))
