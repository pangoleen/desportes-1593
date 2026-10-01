# Polyphonic decoder: glyph-class tokens (+ soft word gaps, + alternatives) -> period French, with a word
# lexicon, a word-bigram model and a character 5-gram fallback for out-of-lexicon stretches.
import json, os, math, re, itertools, collections
from glyphs import L2C, PAIRS
HERE = os.path.dirname(os.path.abspath(__file__))
SIGNWORD = {'Q': 'que', 'K': 'qui', 'P': 'pour', 'R': 'par', '&': 'et'}
W2SIGN = [('que', 'Q'), ('qui', 'K'), ('pour', 'P'), ('par', 'R')]

def patterns(w):
    """all class patterns a word may be written with (signs que/qui/pour/par optional)"""
    forms = {w}
    for s, g in W2SIGN:
        new = set()
        for f in forms:
            if s in f:
                parts = f.split(s)
                for mask in itertools.product((0, 1), repeat=min(len(parts) - 1, 3)):
                    out = parts[0]
                    for k, p in enumerate(parts[1:]):
                        out += (g if (k < len(mask) and mask[k]) else s) + p
                    new.add(out)
        forms |= new
    res = set()
    for f in forms:
        res.add(''.join(c if c in 'QKPR' else L2C[c] for c in f))
    return res

RULES = [(r'y', 'i'), (r'([bcdfglmnprt])\1', r'\1'), (r'z$', 's'), (r'x$', 's'), (r'ct', 't'), (r'sc(?=[ei])', 's'),
         (r'pt', 't'), (r'([ao])ul(?=[tdcx])', r'\1u'), (r'ung$', 'un'), (r'ph', 'f'), (r'th', 't'), (r'adu', 'au'),
         (r'bs', 's'), (r'oi', 'oy'), (r'ai', 'ay'), (r'ee$', 'e'), (r'an(?=[ct])', 'en'), (r'en(?=[ct])', 'an'),
         (r'gn', 'n'), (r'qu', 'c'), (r'ss', 's'), (r'^h', '')]
def spell_variants(w):
    out = set(); first = set()
    for pat, rep in RULES:
        v = re.sub(pat, rep, w)
        if v != w: first.add(v)
    out |= first
    for f in list(first)[:8]:
        for pat, rep in RULES[:8]:
            v = re.sub(pat, rep, f)
            if v != f and v != w: out.add(v)
    return out

DISC = 2.0
class LM:
    def __init__(self, extra_words=(), min_count=3, extra_weight=30):
        wc = json.load(open(f'{HERE}/lm/words.json'))
        self.wc = collections.Counter({w: c for w, c in wc.items() if c >= min_count and (len(w) > 1 or w in 'ayo')})
        for w in extra_words:
            if w and all(c in L2C for c in w): self.wc[w] += extra_weight
        # the scribe's phonetic spelling: add variant forms of frequent words at a fifth of their count
        self.canon = {}
        for w, c in list(self.wc.items()):
            if c < 5 or len(w) < 4: continue
            for v in spell_variants(w):
                if v not in self.wc: self.wc[v] = max(1, c // 5); self.canon[v] = w
        self.wc['et'] += 0; self.N = sum(self.wc.values())
        bg = json.load(open(f'{HERE}/lm/bigrams.json'))
        self.bg = {}; self.ctx = collections.Counter()
        self.kept = collections.Counter()            # discounted bigram mass per context
        for k, c in bg.items():
            a, b = k.split(' ')
            if b in self.wc:
                self.ctx[a] += c
                if c > DISC: self.bg[k] = c; self.kept[a] += c - DISC
        self.ch = json.load(open(f'{HERE}/lm/char5.json'))
        self.ch4 = collections.Counter()
        for k, c in self.ch.items(): self.ch4[k[:4]] += c
        self.trie = {}
        for w in self.wc:
            for p in patterns(w):
                node = self.trie
                for c in p: node = node.setdefault(c, {})
                node.setdefault('$', []).append(w)
    def uni(self, w): return (self.wc.get(w, 0) + 0.05) / (self.N + 1e5)
    def logp(self, w, prev, lam=0.7):
        prev = self.canon.get(prev, prev)
        b = self.bg.get(prev + ' ' + self.canon.get(w, w), 0); c = self.ctx.get(prev, 0) + 10.0
        pb = max(b - DISC, 0.0) / c                   # absolute discounting; the corpus holds duplicate volumes
        back = 1.0 - self.kept.get(prev, 0) / c
        return math.log(pb + back * self.uni(w))
    def charlp(self, hist, ch):                       # 5-gram with add-k smoothing over 23 symbols
        h = (hist[-4:]).rjust(4)
        return math.log((self.ch.get(h + ch, 0) + 0.3) / (self.ch4.get(h, 0) + 0.3 * 23))

def decode(tokens, gaps, lm, alts=None, beam=40, a_nogap=1.2, b_ingap=3.0, oov=-4.0, sub_pen=1.0, hard_breaks=()):
    """tokens: list of class chars; gaps[i] True if a word gap was seen before token i (None = unknown, e.g. line break).
    alts[i]: list of (class, logprob) alternatives for token i (first = main, logprob <= 0).
    Returns list of (start, end, word, kind)."""
    n = len(tokens)
    if alts is None: alts = [[(t, 0.0)] for t in tokens]
    best = [dict() for _ in range(n + 1)]             # best[i][prev] = (score, back)
    best[0]['<s>'] = (0.0, None)
    def push(j, prev, score, back):
        d = best[j]
        if prev not in d or d[prev][0] < score: d[prev] = (score, back)
    for i in range(n):
        if not best[i]: continue
        hyps = sorted(best[i].items(), key=lambda kv: -kv[1][0])[:beam]
        best[i] = dict(hyps)
        start_pen = 0.0 if (gaps[i] is None or gaps[i] or i == 0) else -a_nogap
        # enumerate lexicon words from i (with alternatives)
        cands = []                                    # (j, word, acoustic)
        stack = [(i, lm.trie, 0.0, 0)]
        while stack:
            k, node, ac, nsub = stack.pop()
            if '$' in node and k > i:
                for w in node['$']: cands.append((k, w, ac))
            if k >= n: continue
            if k > i and k in hard_breaks: continue
            pen = -b_ingap if (k > i and gaps[k]) else 0.0
            for r, (c, lp) in enumerate(alts[k]):
                if r > 0 and nsub >= 1: break
                nx = node.get(c)
                if nx is not None: stack.append((k + 1, nx, ac + pen + lp - (sub_pen if r else 0.0), nsub + (r > 0)))
        t = tokens[i]
        for prev, (sc, back) in hyps:
            pw = prev if not prev.startswith('<') else '<s>'
            for j, w, ac in cands:
                push(j, w, sc + start_pen + ac + lm.logp(w, pw), (i, prev, w, 'w'))
            if t in SIGNWORD:
                w = SIGNWORD[t]; push(i + 1, w, sc + start_pen + lm.logp(w, pw), (i, prev, w, 's'))
            elif t == '#':
                push(i + 1, '<#>', sc + start_pen - 2.0, (i, prev, '#', 's'))
            else:
                # out-of-lexicon glyph: letter chosen by the character model given the previous letters
                hist = prev[5:] if prev.startswith('<o>') else ' '
                for ch in PAIRS[t]:
                    lp = lm.charlp(hist, ch)
                    push(i + 1, '<o>' + (hist + ch)[-4:], sc + oov + lp + (start_pen if not prev.startswith('<o>') else (-b_ingap * 0 if not gaps[i] else -0.5)), (i, prev, ch, 'o'))
    if not best[n]: return []
    prev = max(best[n].items(), key=lambda kv: kv[1][0])[0]
    out = []; j = n
    while j > 0:
        sc, back = best[j][prev]; i, pprev, w, kind = back
        out.append((i, j, w, kind)); j, prev = i, pprev
    return out[::-1]

def render(segs):
    """-> text with spaces; out-of-lexicon letters are joined and wrapped in {}"""
    out = []; buf = ''
    for i, j, w, kind in segs:
        if kind == 'o': buf += w; continue
        if buf: out.append('{' + buf + '}'); buf = ''
        out.append('[#]' if w == '#' else w)
    if buf: out.append('{' + buf + '}')
    return ' '.join(out)

def letters(segs, tokens):
    """per-token decoded value: a letter, or the sign word for a sign token"""
    res = [None] * len(tokens)
    for i, j, w, kind in segs:
        if kind in 'so': res[i] = w; continue
        # distribute the word's letters over tokens (signs inside words take their word)
        p = 0
        for k in range(i, j):
            t = tokens[k]
            if t in SIGNWORD and w.startswith(SIGNWORD[t], p): res[k] = SIGNWORD[t]; p += len(SIGNWORD[t])
            else: res[k] = w[p]; p += 1
    return res

def gold_tokens(text):
    """gold text -> (classes, gaps, truth values per token)"""
    toks, gaps, truth = [], [], []; gap = True
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == ' ': gap = True; i += 1; continue
        if ch == '=': toks.append(text[i + 1]); truth.append('?'); i += 2
        elif ch in SIGNWORD: toks.append(ch); truth.append(SIGNWORD[ch]); i += 1
        elif ch == '#': toks.append('#'); truth.append('#'); i += 1
        else: toks.append(L2C[ch]); truth.append('u' if ch == 'v' else 'i' if ch == 'j' else ch); i += 1
        gaps.append(gap); gap = False
    return toks, gaps, truth
