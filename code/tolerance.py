# Decoder tolerance control: true glyph strings of the gold lines, with injected glyph errors.
# usage: tolerance.py rate [seed]   (LM from the corpus only; the gold text is not in the lexicon extras)
import sys, random
import ctc
from glyphs import read_gold, CLASSES
from decode import LM, decode, letters, gold_tokens
rate = float(sys.argv[1]); seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
rnd = random.Random(seed)
CONF = {'E': 'BH', 'B': 'EH', 'F': 'GH', 'G': 'FI', 'H': 'BF', 'I': 'GM', 'M': 'AI', 'A': 'CD', 'C': 'AD', 'D': 'AC', 'L': 'IE'}
lm = LM()
L = E = 0
for page in ('f188v', 'f176r', 'f176v'):
    rows = read_gold(page)
    for s in range(0, len(rows), 6):                      # decode in chunks of 6 lines
        toks, gaps, truth = [], [], []
        for r in rows[s:s + 6]:
            t, g, tr = gold_tokens(r['text']); g[0] = None
            toks += t; gaps += g; truth += tr
        T, G = [], []
        for t, g in zip(toks, gaps):
            u = rnd.random()
            if t in CONF and u < rate * 0.7: T.append(rnd.choice(CONF[t])); G.append(g)          # substitution
            elif u < rate * 0.85: continue                                                         # deletion
            elif u < rate: T.append(t); G.append(g); T.append(rnd.choice('EABFGH')); G.append(False)  # insertion
            else: T.append(t); G.append(g)
        dec = ''.join(x for x in letters(decode(T, G, lm), T) if x)
        tr = ''.join(x for x in truth if x != '?')
        E += ctc.edit(dec, tr); L += len(tr)
print(f'glyph error rate {rate:.2f}: letter accuracy {1 - E / L:.4f} ({E} errors / {L} letters)', flush=True)
