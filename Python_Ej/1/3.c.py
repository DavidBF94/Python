import cmath
from numpy import linspace,empty
from math import pi,sin,sqrt
from matplotlib.pyplot import plot,show,imshow
b=100*10**-6
a=-100*10**-6
Nivel=11
Intensidades=[]
xx=[]
def q(u):
    alpha=pi/(20*10**-6)
    return ((sin(alpha*u))**2)
def f(u,x):
    Número=complex(0,(((2*pi*x*u)/(500*10**-9))))
    return sqrt(q(u))*cmath.exp(Número)
#Aquí se introduce el método de Romberg basado en el método trapezoidal
for x in linspace(-0.05,0.05,3000):    
    ListaIntegrales=[]
    n=1
    h=(b-a)/float(n)
    I=h*(1/2)*(f(a,x)+f(b,x))
    ListaIntegrales.append(I)
    for i in range(2,int(Nivel+1)):
        n=2*n
        h=(b-a)/n
        Impares=0
        for j in range(1,n,2):
            Impares=Impares+f(a+j*h,x)
        I=(1/2)*I+h*Impares
        ListaIntegrales.append(I)
    Combinaciones=ListaIntegrales
    for i in range(2,int(Nivel)):
        Combinación=[]
        L=len(Combinaciones)
        for j in range(1,L):
            Combinación1=((4**(i-1))/(4**(i-1)-1))*Combinaciones[j]
            Combinación2=(1/(4**(i-1)-1))*Combinaciones[j-1]
            Combinación.append(Combinación1-Combinación2)
        Combinaciones=Combinación
    I1=((4**(Nivel-1))/(4**(Nivel-1)-1))*Combinaciones[1]
    I2=(1/(4**(Nivel-1)-1))*Combinaciones[0]
    Integral=I1-I2
    Intensidades.append(Integral.real)
    xx.append(x)
#######################################################################
Intensidades2=[]
xx2=[]
n=len(xx)
for i in range(0,n):
    if Intensidades[i]>=0:
        Intensidades2.append(Intensidades[i])
        xx2.append(xx[i])
plot(xx2,Intensidades2)
show()
n=len(xx2)
Matriz=empty([n,n],float)
for i in range(0,n):
    for j in range(0,n):
        Matriz[i,j]=Intensidades2[j]
imshow(Matriz)
show()
        
        