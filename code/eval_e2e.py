# End-to-end held-out test: image -> ensemble glyphs -> decoder -> letters, against the gold text.
# usage: eval_e2e.py models...   (held-out lines: f188v 7-10, f176r 20-23)
import sys, re
import ctc, recog
from glyphs import read_gold, SPACE
from decode import LM, decode, render, letters, gold_tokens, SIGNWORD
HOLD = {('f188v', k) for k in range(7, 11)} | {('f176r', k) for k in range(20, 24)} | {('f176v', k) for k in range(20, 24)}
def train_words(rows, hold):
    ex = []
    for r in rows:
        if (r['page'], r['line']) in hold: continue
        t = r['text']
        for s, w in SIGNWORD.items(): t = t.replace(s, w if s != '&' else ' et ')
        ex += [w.replace('v', 'u').replace('j', 'i') for w in re.findall(r'[a-z]+', t)]
    return ex
if __name__ == '__main__':
    ms = recog.load(sys.argv[1:])
    rows = [r for p in ('f188v', 'f176r', 'f176v') for r in read_gold(p)]
    lm = LM(extra_words=train_words(rows, HOLD))
    G = E = L = LE = 0
    for page in ('f188v', 'f176r', 'f176v'):
        T, Gp, A, truth = [], [], [], []
        for r in rows:
            if (page, r['line']) not in HOLD or r['page'] != page: continue
            toks, alts, hyps = recog.recognise(ms, page, r['line'], r['ranges'])
            hyp = ''.join(t for t in toks if t != SPACE)
            e = ctc.edit(hyp, r['cls']); G += len(r['cls']); E += e
            print(page, r['line'], 'glyph errors', e, '/', len(r['cls']))
            if e: print('   ref', r['cls_sp']); print('   hyp', ''.join(toks))
            t, g, a = recog.to_stream(toks, alts); g[0] = None
            T += t; Gp += g; A += a
            truth += gold_tokens(r['text'])[2]
        segs = decode(T, Gp, lm, A)
        dec = ''.join(x for x in letters(segs, T) if x)
        tr = ''.join(x for x in truth if x != '?')
        le = ctc.edit(dec, tr); L += len(tr); LE += le
        print(page, 'letters', len(tr), 'errors', le, 'accuracy', round(1 - le / len(tr), 4))
        print('  ', render(segs))
    print(f'GLYPH accuracy {1 - E / G:.4f} ({E} errors / {G});  LETTER accuracy {1 - LE / L:.4f} ({LE} errors / {L})')
