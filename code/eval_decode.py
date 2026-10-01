# Control: decode the TRUE class strings of held-out gold lines (and all lines) -> letter accuracy.
import sys, re
from glyphs import read_gold
from decode import LM, decode, render, letters, gold_tokens
hold = {('f188v', k) for k in range(7, 11)} | {('f176r', k) for k in range(20, 24)}
rows = [r for p in ('f188v', 'f176r') for r in read_gold(p)]
extra = []
for r in rows:
    if (r['page'], r['line']) in hold: continue
    extra += [w.replace('v', 'u').replace('j', 'i') for w in re.findall(r'[a-z]+', r['text'].replace('Q', 'que').replace('K', 'qui').replace('P', 'pour').replace('R', 'par'))]
lm = LM(extra_words=extra)
print('lexicon', len(lm.wc))
use_gaps = len(sys.argv) < 2 or sys.argv[1] != 'nogap'
tot = ok = 0
for page in ('f188v', 'f176r'):
    hr = [r for r in rows if r['page'] == page and (page, r['line']) in hold]
    toks, gaps, truth = [], [], []
    for r in hr:
        t, g, tr = gold_tokens(r['text']); g[0] = None
        toks += t; gaps += (g if use_gaps else [None] * len(g)); truth += tr
    segs = decode(toks, gaps, lm)
    dec = letters(segs, toks)
    good = sum(1 for a, b in zip(dec, truth) if a == b or b == '?'); tot += len(truth); ok += good
    print(page, 'letters', len(truth), 'correct', good, round(good / len(truth), 3))
    print(render(segs))
print('TOTAL letter accuracy', round(ok / tot, 4))
