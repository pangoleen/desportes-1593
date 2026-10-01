# Line-level CTC recogniser for the Desportes cipher hand (PyTorch, MPS).
import os, sys, json, math, random, numpy as np, torch, torch.nn as nn, torch.nn.functional as F
from PIL import Image
from scipy import ndimage
from pages import line_arr, HERE
from glyphs import CLASSES, C2I, SPACE, read_gold
torch.set_num_threads(1)
DEV = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')
H = 64            # network input height (line crops are 128 high, scaled 0.5)
NCLS = len(CLASSES) + 1
FIXW = 2112        # all batches are padded to this width (cudnn.benchmark re-tunes per shape)
torch.backends.cudnn.benchmark = True
AMP = DEV == 'cuda'

def prep(page, k, ranges=None, with_offset=False):
    """straightened line -> float array [64, W/2], white=0, ink=1; clear-text regions blanked; trimmed to ink extent"""
    a = line_arr(page, k).astype(np.float32)
    dark = np.percentile(a, 0.5)
    bg = ndimage.median_filter(np.percentile(a, 90, axis=0), 41, mode='nearest')     # column-wise paper level
    a = np.clip((bg[None, :] - a) / np.maximum(45.0, bg[None, :] - dark), 0, 1)
    if ranges:
        m = np.zeros(a.shape[1], bool)
        for x0, x1 in ranges: m[x0:x1] = True
        a[:, ~m] = 0
    col = (a > 0.45).sum(0); xs = np.where(col > 0)[0]; off = 0
    if len(xs): off = max(0, xs[0] - 40); a = a[:, off: xs[-1] + 40]
    im = Image.fromarray((a * 255).astype(np.uint8)).resize((a.shape[1] // 2, H), Image.BILINEAR)
    out = np.asarray(im, np.float32) / 255.0
    return (out, off) if with_offset else out

def augment(a, rng):
    h, w = a.shape
    # horizontal stretch, shear, small rotation, vertical shift via affine
    sx = rng.uniform(0.88, min(1.14, FIXW / w)); sy = rng.uniform(0.9, 1.1); sh = rng.uniform(-0.25, 0.25); dy = rng.uniform(-4, 4)
    nw = int(w * sx)
    im = Image.fromarray((a * 255).astype(np.uint8))
    # output (x,y) -> input: x_in = (x - sh*(y-h/2))/sx ; y_in = (y-h/2)/sy + h/2 - dy
    im = im.transform((nw, h), Image.AFFINE, (1 / sx, -sh / sx, sh * h / 2 / sx, 0, 1 / sy, h / 2 - h / 2 / sy - dy), resample=Image.BILINEAR)
    a = np.asarray(im, np.float32) / 255.0
    # elastic-ish: smooth random vertical displacement along x
    if rng.random() < 0.7:
        d = ndimage.gaussian_filter1d(rng.normal(0, 1, nw), 25) * 25
        yy, xx = np.mgrid[0:h, 0:nw].astype(np.float32)
        a = ndimage.map_coordinates(a, [yy + d[None, :], xx], order=1, mode='constant')
    # stroke thickness
    r = rng.random()
    if r < 0.25: a = ndimage.grey_dilation(a, size=(2, 2))
    elif r < 0.45: a = ndimage.grey_erosion(a, size=(2, 2))
    if rng.random() < 0.5: a = ndimage.gaussian_filter(a, rng.uniform(0.3, 1.0))
    a = a * rng.uniform(0.7, 1.3) + rng.normal(0, 0.04, a.shape) + rng.uniform(-0.05, 0.08)
    # bleed-through: faint shifted copy
    if rng.random() < 0.3:
        s = rng.integers(20, 200); a = a + 0.15 * np.roll(a[::-1], s, axis=1)
    return np.clip(a, 0, 1).astype(np.float32)

class Net(nn.Module):
    def __init__(self, rnn=0, width=0.75):
        super().__init__()
        c = [int(x * width) for x in (32, 64, 128, 192, 256)]
        def blk(i, o, pool):
            return nn.Sequential(nn.Conv2d(i, o, 3, padding=1), nn.BatchNorm2d(o), nn.ReLU(), nn.Conv2d(o, o, 3, padding=1), nn.BatchNorm2d(o), nn.ReLU(), nn.MaxPool2d(pool))
        self.cnn = nn.Sequential(blk(1, c[0], (2, 2)), blk(c[0], c[1], (2, 2)), blk(c[1], c[2], (2, 1)), blk(c[2], c[3], (2, 1)), blk(c[3], c[4], (4, 1)))
        self.drop = nn.Dropout(0.3)
        self.c1 = nn.Sequential(nn.Conv1d(c[4], 256, 5, padding=2), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.3))
        self.rnn = nn.GRU(256, rnn, bidirectional=True, batch_first=True) if rnn else None
        self.out = nn.Linear(2 * rnn if rnn else 256, NCLS)
    def forward(self, x):                      # x [B,1,64,W]
        with torch.autocast('cuda', dtype=torch.bfloat16, enabled=AMP):
            f = self.cnn(x.contiguous(memory_format=torch.channels_last)).squeeze(2)             # [B,C,W/4]
        f = self.c1(self.drop(f.float())).transpose(1, 2)
        if self.rnn is not None: f, _ = self.rnn(f)
        return self.out(f).log_softmax(-1)     # [B,T,NCLS]

def batchify(items):
    W = max(a.shape[1] for a, _ in items); W = FIXW if W <= FIXW else (W + 63) // 64 * 64
    x = np.zeros((len(items), 1, H, W), np.float32)
    for i, (a, _) in enumerate(items): x[i, 0, :, :a.shape[1]] = a
    return torch.from_numpy(x), [min(a.shape[1] // 4 + 2, W // 4) for a, _ in items], [y for _, y in items]

def greedy_pos(lp):
    """-> list of (class, frame index of the first frame of the run)"""
    p = lp.argmax(-1); out = []; prev = 0
    for f, q in enumerate(p):
        if q != prev and q != 0: out.append((CLASSES[q - 1], f))
        prev = q
    return out

def greedy(lp):
    """lp [T,NCLS] numpy -> class string"""
    p = lp.argmax(-1); out = []; prev = 0
    for q in p:
        if q != prev and q != 0: out.append(CLASSES[q - 1])
        prev = q
    return ''.join(out)

def edit(a, b):
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        p = d[:]; d[0] = i
        for j in range(1, len(b) + 1):
            d[j] = min(p[j] + 1, d[j - 1] + 1, p[j - 1] + (a[i - 1] != b[j - 1]))
    return d[-1]

def logprobs(model, a):
    model.eval()
    with torch.no_grad():
        x, _, _ = batchify([(a, '')])
        return model(x.to(DEV))[0].cpu().numpy()

def evaluate(model, rows, cache):
    tot = err = 0; outs = []
    for r in rows:
        a = cache[(r['page'], r['line'])]
        hyp = greedy(logprobs(model, a)[: a.shape[1] // 4 + 2])
        e = edit(hyp.replace(SPACE, ''), r['cls']); err += e; tot += len(r['cls']); outs.append((r, hyp, e))
    return err / max(1, tot), outs

def train(train_rows, val_rows, epochs=300, rnn=0, seed=0, out='model.pt', lr=2e-3, bs=8, log=print, init=None):
    rng = np.random.default_rng(seed); torch.manual_seed(seed)
    cache = {(r['page'], r['line']): prep(r['page'], r['line'], r['ranges']) for r in train_rows + val_rows}
    model = Net(rnn).to(DEV).to(memory_format=torch.channels_last)
    if init: model.load_state_dict(torch.load(init, map_location=DEV))
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-3)
    steps = epochs * math.ceil(len(train_rows) / bs)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=lr, total_steps=steps, pct_start=0.15)
    for ep in range(epochs):
        model.train(); idx = rng.permutation(len(train_rows)); tl = 0
        for b in range(0, len(idx), bs):
            items = []
            for i in idx[b:b + bs]:
                r = train_rows[i]; items.append((augment(cache[(r['page'], r['line'])], rng), r['cls_sp']))
            x, tl_, ys = batchify(items)
            lp = model(x.to(DEV)).transpose(0, 1)       # [T,B,C]
            if DEV != 'cuda': lp = lp.cpu()
            tgt = torch.tensor([C2I[c] for y in ys for c in y]); tlen = torch.tensor([len(y) for y in ys])
            loss = F.ctc_loss(lp, tgt.to(lp.device), torch.tensor(tl_), tlen, blank=0, zero_infinity=True)
            opt.zero_grad(); loss.backward(); nn.utils.clip_grad_norm_(model.parameters(), 5); opt.step(); sched.step(); tl += loss.item()
        if (ep + 1) % max(1, epochs // 15) == 0 or ep == epochs - 1:
            cer, _ = evaluate(model, val_rows, cache) if val_rows else (float('nan'), None)
            tcer, _ = evaluate(model, train_rows[:12], cache)
            torch.save(model.state_dict(), f'{HERE}/{out}')
            log(f'ep {ep + 1} loss {tl / math.ceil(len(idx) / bs):.3f} train-CER {tcer:.3f} val-CER {cer:.3f}')
    torch.save(model.state_dict(), f'{HERE}/{out}')
    return model, cache

if __name__ == '__main__':
    rows = read_gold('f188v')
    hold = {7, 8, 9, 10}
    tr = [r for r in rows if r['line'] not in hold]; va = [r for r in rows if r['line'] in hold]
    rnn = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    ep = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    model, cache = train(tr, va, epochs=ep, rnn=rnn, out=f'm188_r{rnn}.pt')
    cer, outs = evaluate(model, va, cache)
    for r, hyp, e in outs: print(r['line'], e, len(r['cls'])); print(' ref', r['cls']); print(' hyp', hyp)
