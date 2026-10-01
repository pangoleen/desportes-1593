# Compare a draft gold page with the ensemble's glyph strings; list the disagreements per line.
# usage: cmp_gold.py page models...
import sys
import ctc, recog
from glyphs import read_gold, SPACE
page = sys.argv[1]; ms = recog.load(sys.argv[2:])
tot = err = 0
for r in read_gold(page):
    toks, alts, hyps = recog.recognise(ms, page, r['line'], r['ranges'])
    hyp = ''.join(t for t in toks if t != SPACE); ref = r['cls']
    al = recog.align(ref, hyp); diffs = []
    for i, j in al:
        if i is None: diffs.append(f'+{hyp[j]}@{j}')
        elif j is None: diffs.append(f'-{ref[i]}@{i}')
        elif ref[i] != hyp[j]: diffs.append(f'{ref[i]}>{hyp[j]}@{i}')
    tot += len(ref); err += len(diffs)
    if diffs:
        # show context of each diff in the gold text (letter index -> text position)
        print(f"{r['line']:2d}  {' '.join(diffs)}"); print('    gold', r['cls_sp']); print('    hyp ', ''.join(toks))
print('lines', 'glyphs', tot, 'disagreements', err, round(err / tot, 4))
