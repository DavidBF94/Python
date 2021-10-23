from cmath import exp,pi
from numpy import linspace,loadtxt
from matplotlib.pyplot import plot,show

N=1000

#Definimos la función del problema y calculamos puntos del intervalo

x=[]
f=[]
for i in linspace(0,1,N):
    x.append(i)
    if i>=0 and i<(1/2):
        f.append(1)
    elif i>=(1/2) and i<=1:
        f.append(-1)
        
#Definimos la función de la Transformada de Fourier Discreta
        
def TFD(f):
    l=len(f)
    c=[]
    for k in range(0,l//2):
        cc=0
        for n in range(0,l):
            cc=cc+f[n]*exp(-2j*pi*k*n/l)
        c.append(cc)
    return(c)

#Definimos la función de la Transformada de Fourier Discreta Inversa
    
def TFDI(f):
    l=len(f)
    y=[]
    for n in range(0,l*2):
        yy=0
        for k in range(0,l):
            yy=yy+(1/(l))*f[k]*exp(2j*pi*n*k/(l*2))
        y.append(yy)
    return(y)
    
#Dibujamos los coeficientes de Fourier

p=loadtxt("pitch.txt")
plot(x,f)
show()
c=TFD(f)
l=len(c)
for i in range(0,l):
    c[i]=abs(c[i])
plot(c)
show()

#Escogemos un límite para los coeficientes de Fourier (TFD)

c=TFD(f)
Límite=500
for i in range(0,N//2):
    if i>Límite:
        c[i]=0

#Dibujamos los puntos correspondientes a la Transformada Inversa

y=TFDI(c)
l=len(y)
for i in range(0,l):
    y[i]=y[i].real
plot(x,y)
show()