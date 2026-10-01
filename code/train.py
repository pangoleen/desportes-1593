# usage: train.py --pages f188v,f176r --hold f188v:7-10 --seed 0 --epochs 1500 --rnn 0 --out m.pt [--init x.pt]
import argparse, sys, functools, json
import ctc
from glyphs import read_gold
print = functools.partial(print, flush=True)
ap = argparse.ArgumentParser()
ap.add_argument('--pages', default='f188v'); ap.add_argument('--hold', default='f188v:7-10')
ap.add_argument('--seed', type=int, default=0); ap.add_argument('--epochs', type=int, default=1500)
ap.add_argument('--rnn', type=int, default=0); ap.add_argument('--out', default='m.pt'); ap.add_argument('--init', default=None)
ap.add_argument('--lr', type=float, default=2e-3); ap.add_argument('--bs', type=int, default=8)
a = ap.parse_args()
hold = set()
for h in a.hold.split(','):
    if not h: continue
    p, r = h.split(':'); lo, hi = (r.split('-') + [r])[:2]
    for k in range(int(lo), int(hi) + 1): hold.add((p, k))
rows = [r for p in a.pages.split(',') for r in read_gold(p)]
tr = [r for r in rows if (r['page'], r['line']) not in hold]; va = [r for r in rows if (r['page'], r['line']) in hold]
print('train lines', len(tr), 'glyphs', sum(len(r['cls']) for r in tr), 'val lines', len(va), 'glyphs', sum(len(r['cls']) for r in va))
model, cache = ctc.train(tr, va, epochs=a.epochs, rnn=a.rnn, seed=a.seed, out=a.out, lr=a.lr, bs=a.bs, log=print, init=a.init)
cer, outs = ctc.evaluate(model, va, cache)
print('FINAL val-CER', round(cer, 4))
for r, hyp, e in outs: print(r['page'], r['line'], e, len(r['cls'])); print(' ref', r['cls_sp']); print(' hyp', hyp)
