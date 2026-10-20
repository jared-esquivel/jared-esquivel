from PIL import Image,ImageDraw,ImageFont,ImageFilter
import math,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'assets','hero');os.makedirs(OUT,exist_ok=True)
W,H=1200,490
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
heavy='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
F1=ImageFont.truetype(font,22);F2=ImageFont.truetype(heavy,92);F3=ImageFont.truetype(heavy,34)
def frame(t):
 im=Image.new('RGB',(W,H),(3,10,21));p=im.load()
 for y in range(H):
  for x in range(W):
   a=math.exp(-((x-920)**2/(2*300**2)+(y-200)**2/(2*230**2)))*0.21
   b=math.exp(-((x-220)**2/(2*210**2)+(y-140)**2/(2*160**2)))*0.12
   c=math.exp(-((x-630)**2/(2*330**2)+(y-410)**2/(2*150**2)))*0.10
   p[x,y]=(int(3+28*a+35*b),int(10+65*a+8*b+33*c),int(21+110*a+63*b+49*c))
 d=ImageDraw.Draw(im,'RGBA')
 for j in range(7):
  pts=[]
  for x in range(0,W+10,6):
   y=30+j*73+9*math.sin(x/145+t*2*math.pi+j*.6)+3*math.sin(x/65-t*2*math.pi*.7+j)
   pts.append((x,y))
  d.line(pts,fill=(60,125,160,21),width=1)
 reveal=min(1,max(0,(t*7-.35)))
 if reveal>0:
  d.text((130,155),'Hey there!',font=F1,fill=(220,228,241,int(245*reveal)))
  d.text((130,188),"I'm",font=F2,fill=(246,249,255,int(255*min(1,max(0,t*7-1.0)))))
  # gradient text via mask
  mask=Image.new('L',(W,H));md=ImageDraw.Draw(mask);md.text((345,188),'Jared',font=F2,fill=int(255*min(1,max(0,t*7-1.5))))
  grad=Image.new('RGB',(W,H));gp=grad.load()
  for x in range(340,710):
   k=max(0,min(1,(x-345)/370));gpcol=(int(39*(1-k)+46*k),int(145*(1-k)+235*k),int(255*(1-k)+160*k))
   for y in range(188,320):gp[x,y]=gpcol
  im.paste(grad,(0,0),mask)
  d=ImageDraw.Draw(im,'RGBA')
  k=min(1,max(0,t*7-2.4));d.line((346,302,346+321*k,302),fill=(48,218,224,int(255*k)),width=4)
  k=min(1,max(0,t*7-3.2));d.text((131,343),'Senior Software Developer',font=F3,fill=(56,195,235,int(255*k)))
  d.text((132,402),'REACT  /  TYPESCRIPT  /  AI-ASSISTED DEVELOPMENT',font=F1,fill=(133,158,180,int(220*k)))
 return im
# short entrance then a subtle, continuous ambient wave loop
frames=[frame(min(.999,i/35)) for i in range(36)]
frames[0].save(os.path.join(OUT,'hero.gif'),save_all=True,append_images=frames[1:],duration=95,loop=0,optimize=True)
frames[-1].save(os.path.join(OUT,'hero-static.png'),optimize=True)
print(os.path.getsize(os.path.join(OUT,'hero.gif')))
