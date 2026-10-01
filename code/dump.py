# usage: dump.py page  -> prints per line: decoded words with their glyph classes, e.g. uoulu[HBHLH]
# '_' before a word = the recogniser saw a word gap there; '~' = no gap seen. Alternatives in ().
import sys, json
from pages import HERE
page = sys.argv[1]
st = json.load(open(f'{HERE}/tmp/struct_{page}.json'))
cur = None; words = []; w = None
def flush_line():
    global words
    if cur is not None: print(f'{cur:2d}  ' + ' '.join(words))
    words = []
for e in st:
    if e['line'] != cur:
        if w: words.append(w[0] + '[' + w[1] + ']')
        w = None; flush_line(); cur = e['line']
    if e['kind'] == 'c':
        if w: words.append(w[0] + '[' + w[1] + ']'); w = None
        words.append('[clair]'); continue
    g = e['tok'] + ('(' + ''.join(e['alt']) + ')' if e.get('alt') else '')
    v = e['val'] if e['kind'] != 'o' else e['val'].upper()
    if e['ws'] or w is None:
        if w: words.append(w[0] + '[' + w[1] + ']')
        w = [v, g]
    else: w[0] += v; w[1] += g
if w: words.append(w[0] + '[' + w[1] + ']')
flush_line()
