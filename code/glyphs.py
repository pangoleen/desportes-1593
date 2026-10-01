# Glyph classes and gold-file parsing.
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
PAIRS = {'A': 'an', 'B': 'bo', 'C': 'cp', 'D': 'dq', 'E': 'er', 'F': 'fs', 'G': 'gt', 'H': 'hu', 'I': 'ix', 'L': 'ly', 'M': 'mz'}
L2C = {}
for c, p in PAIRS.items():
    for ch in p: L2C[ch] = c
L2C['v'] = 'H'; L2C['j'] = 'I'
SIGNS = ['Q', 'K', 'P', '&', 'R', '#']     # que, qui, pour, et, par, other sign
SPACE = '_'
CLASSES = list('ABCDEFGHILM') + SIGNS + [SPACE]   # 18 classes; CTC blank = index 0
C2I = {c: i + 1 for i, c in enumerate(CLASSES)}
def text2cls(t, space=False):
    """gold text -> class string (one char per glyph); with space=True word gaps become '_'"""
    out = []; i = 0
    while i < len(t):
        ch = t[i]
        if ch == '=': out.append(t[i + 1]); i += 2; continue
        if ch in ' \t':
            if space and out and out[-1] != SPACE: out.append(SPACE)
            i += 1; continue
        if ch in 'QKP&R#': out.append(ch)
        elif ch in L2C: out.append(L2C[ch])
        else: raise ValueError(f'bad char {ch!r} in {t!r}')
        i += 1
    return ''.join(out)
def read_gold(page):
    rows = []
    for ln in open(f'{HERE}/gold/{page}.txt'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'): continue
        k, rng, text = [s.strip() for s in ln.split('|')]
        ranges = [tuple(map(int, r.split('-'))) for r in rng.split()] if rng else []
        rows.append({'page': page, 'line': int(k), 'ranges': ranges, 'text': text, 'cls': text2cls(text), 'cls_sp': text2cls(text.strip(), True)})
    return rows
if __name__ == '__main__':
    import sys
    for r in read_gold(sys.argv[1]): print(r['line'], len(r['cls']), r['cls'])
