from matplotlib.pyplot import plot,show
from numpy import loadtxt
valores=loadtxt("millikan.txt")
x=valores[:,0]
y=valores[:,1]
N=len(x)
Ex=[]
Ey=[]
Exx=[]
Exy=[]
for i in range(0,N):
    Ex0=(1/N)*x[i]
    Ey0=(1/N)*y[i]
    Exx0=(1/N)*(x[i]**2)
    Exy0=(1/N)*x[i]*y[i]
    Ex.append(Ex0)
    Ey.append(Ey0)
    Exx.append(Exx0)
    Exy.append(Exy0)
m=(sum(Exy)-sum(Ex)*sum(Ey))/(sum(Exx)-(sum(Ex))**2)
c=(sum(Exx)*sum(Ey)-sum(Ex)*sum(Exy))/(sum(Exx)-(sum(Ex))**2)
yy=[]
for i in range(0,N):
    yy0=m*x[i]+c
    yy.append(yy0)
plot(x,yy,'ro-')
plot(x,y,'bo')
show()
