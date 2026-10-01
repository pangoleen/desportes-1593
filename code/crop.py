# usage: crop.py canvas x y w h scale out
import sys
from PIL import Image, ImageOps
c,x,y,w,h=sys.argv[1],*map(int,sys.argv[2:6]); s=float(sys.argv[6]); out=sys.argv[7]
im=Image.open(f'img/c{c}.jpg').convert('L').crop((x,y,x+w,y+h))
im=ImageOps.autocontrast(im,cutoff=1)
if s!=1: im=im.resize((int(w*s),int(h*s)),Image.LANCZOS)
im.save(out)
