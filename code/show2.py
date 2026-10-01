# usage: show2.py page k0 k1 -> tmp/<page>_<k0>-<k1>.png (stack of line sheets)
import sys
from PIL import Image, ImageDraw
from show import sheet
page=sys.argv[1]; k0=int(sys.argv[2]); k1=int(sys.argv[3]); nseg=int(sys.argv[4]) if len(sys.argv)>4 else 3
scale=float(sys.argv[5]) if len(sys.argv)>5 else 1.3
S=[sheet(page,k,nseg,scale) for k in range(k0,k1+1)]
out=Image.new('L',(S[0].width+40,sum(s.height+10 for s in S)),255)
y=0; d=ImageDraw.Draw(out)
for k,s in zip(range(k0,k1+1),S):
    out.paste(s,(40,y)); d.text((2,y+20),str(k),fill=0,font_size=28); y+=s.height+10
    d.line((0,y-5,out.width,y-5),fill=0,width=3)
fn=f'tmp/{page}_{k0:02d}-{k1:02d}.png'; out.save(fn); print(fn,out.size)
