GlowScript 3.0 VPython

G=6.67e-11
ME=5.97e24
RE=6.37e6
RQ=RE+2.95e6
v0=12e3

mQ=1000

earth=sphere(pos=vector(0,0,0),radius=RE, texture=textures.earth)
QG=sphere(pos=vector(RQ,-4*RQ,0), radius=RE/10, color=color.yellow, make_trail=True)
earth.m=ME
QG.m=mQ
QG.p=QG.m*vector(0,v0,0)

t=0
dt=3*60

while t<7000:
  rate(100)
  r=QG.pos-earth.pos
  F=-G*earth.m*QG.m*norm(r)/mag(r)**2
  QG.p=QG.p + F*dt
  QG.pos=QG.pos+QG.p*dt/QG.m
  t=t+dt
print("v final = ",QG.p/QG.m," m/s")
vQG0=vector(0,v0,0)
theta=acos(dot(vQG0,QG.p/QG.m)/(mag(vQG0)*mag(QG.p/QG.m)))
print("deflection angle = ",theta*180/pi," deg")
