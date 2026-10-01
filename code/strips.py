# usage: strips.py canvas y0 y1 h step prefix x0,x1 [x0,x1 ...]
import sys
from PIL import Image, ImageOps
c=sys.argv[1]; y0,y1,h,step=map(int,sys.argv[2:6]); pre=sys.argv[6]
cols=[tuple(map(int,a.split(','))) for a in sys.argv[7:]]
im=Image.open(f'img/c{c}.jpg').convert('L')
y=y0;k=0
while y<y1:
    for j,(xa,xb) in enumerate(cols):
        ImageOps.autocontrast(im.crop((xa,y,xb,y+h)),cutoff=1).save(f'{pre}{k:02d}{"abcd"[j]}.png')
    y+=step;k+=1
print(k)
