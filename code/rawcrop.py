# usage: rawcrop.py page line x0 x1 [dy0 dy1] [scale] out  -> crop of the deskewed block around a line (not straightened)
import sys, numpy as np
from PIL import Image, ImageOps
from pages import block, meta
page = sys.argv[1]; k = int(sys.argv[2]); x0, x1 = int(sys.argv[3]), int(sys.argv[4])
dy0, dy1 = int(sys.argv[5]), int(sys.argv[6]); sc = float(sys.argv[7]); out = sys.argv[8]
m = meta(page); A = block(page)
yc = int(np.interp((x0 + x1) / 2, m['xc'], m['centres'][k]))
im = Image.fromarray(A[max(0, yc + dy0): yc + dy1, x0:x1]); im = ImageOps.autocontrast(im, cutoff=0.5)
im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS).save(out)
