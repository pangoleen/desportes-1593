# Align the f. 177 plaintext to the cipher lines of f. 176 with a recogniser.
# Step 1: greedy decode of every line. Step 2: global alignment (Needleman-Wunsch) of the concatenated
# hypothesis against the plaintext class string -> the plaintext span of each line.
import sys, re, json, numpy as np, torch
from glyphs import L2C, CLASSES
from pages import nlines, HERE
import ctc

def plain_tokens(side):
    """f177 plaintext for one side -> list of (class, letter, word_index); and the words"""
    words = []
    for ln in open(f'{HERE}/f177_plain.txt'):
        if ln.startswith('#') or not ln.strip(): continue
        tag, text = ln.split(' ', 1)
        if tag[0] != side: continue
        text = text.replace('[?]', '').replace('[', '').replace(']', '').replace('?', '')
        words += text.split()
    toks = []
    for wi, w in enumerate(words):
        lw = w.lower()
        if lw == 'que': toks.append(('Q', 'que', wi)); continue
        if lw == 'qui': toks.append(('K', 'qui', wi)); continue
        if lw == 'pour': toks.append(('P', 'pour', wi)); continue
        if lw == 'et': toks.append(('&', 'et', wi)); continue
        if lw == '#': toks.append(('#', '#', wi)); continue
        if re.fullmatch(r'\d+', lw): toks.append(('#', lw, wi)); continue
        i = 0
        while i < len(lw):
            if lw.startswith('que', i): toks.append(('Q', 'que', wi)); i += 3; continue
            if lw.startswith('qui', i): toks.append(('K', 'qui', wi)); i += 3; continue
            ch = lw[i]
            if ch in L2C: toks.append((L2C[ch], ch, wi))
            i += 1
    return toks, words

def nw(hyp, ref, sub=1.0, gap=1.0):
    """global alignment; returns for each hyp position the ref index it maps to (or -1)"""
    n, m = len(hyp), len(ref)
    D = np.zeros((n + 1, m + 1), np.float32); D[:, 0] = np.arange(n + 1) * gap; D[0, :] = np.arange(m + 1) * gap
    hb = np.frombuffer(hyp.encode(), np.uint8); rb = np.frombuffer(ref.encode(), np.uint8)
    for i in range(1, n + 1):
        s = D[i - 1, :-1] + (rb != hb[i - 1]) * sub
        up = D[i - 1, 1:] + gap
        row = np.minimum(s, up)
        # left moves need a sequential pass
        prev = D[i, 0]
        for j in range(1, m + 1):
            v = row[j - 1]
            if prev + gap < v: v = prev + gap
            D[i, j] = v; prev = v
    i, j = n, m; mp = [-1] * n
    while i > 0 and j > 0:
        if D[i, j] == D[i - 1, j - 1] + (hyp[i - 1] != ref[j - 1]) * sub: mp[i - 1] = j - 1; i -= 1; j -= 1
        elif D[i, j] == D[i - 1, j] + gap: i -= 1
        else: j -= 1
    return mp, D[n, m]

if __name__ == '__main__':
    page = sys.argv[1]; mfile = sys.argv[2]; rnn = int(sys.argv[3])
    model = ctc.Net(rnn).to(ctc.DEV); model.load_state_dict(torch.load(mfile, map_location=ctc.DEV))
    side = page[-1]
    toks, words = plain_tokens(side); ref = ''.join(t[0] for t in toks)
    hyps = []
    for k in range(nlines(page)):
        a = ctc.prep(page, k); hyps.append(ctc.greedy(ctc.logprobs(model, a)))
    hyp = ''.join(hyps)
    mp, cost = nw(hyp, ref)
    print(page, 'hyp glyphs', len(hyp), 'ref glyphs', len(ref), 'edit cost', cost, 'rate', round(cost / len(ref), 3))
    pos = 0; out = {}
    last = 0
    for k, h in enumerate(hyps):
        idx = [mp[pos + i] for i in range(len(h)) if mp[pos + i] >= 0]
        pos += len(h)
        a = last; b = (max(idx) + 1) if idx else last
        b = max(b, a); last = b
        seg = toks[a:b]
        txt = []; pw = None
        for c, l, wi in seg:
            if pw is not None and wi != pw: txt.append(' ')
            txt.append(l if len(l) == 1 else {'que': 'Q', 'qui': 'K', 'pour': 'P', 'et': '&'}.get(l, '#')); pw = wi
        out[k] = {'a': a, 'b': b, 'text': ''.join(txt), 'hyp': h, 'ref': ref[a:b]}
        print(k, len(h), b - a, ''.join(txt)); print('   hyp', h); print('   ref', ref[a:b])
    json.dump(out, open(f'{HERE}/tmp/align_{page}.json', 'w'))
