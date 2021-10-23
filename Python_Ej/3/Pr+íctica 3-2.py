from matplotlib.pyplot import plot,show
from numpy import zeros,arange
from math import sin,pi

Años=10
Tau0=365
Tau=Tau0*Años
A=10
B=12
D=0.1

L=20
N=40
a=L/N
h=1

Tf=11
Tmid=0
T0=A+B*sin(2*pi/Tau0)

tt=arange(1,Tau+1,h)
n=len(tt)
xx=arange(0,L+a,a)
l=len(xx)

T=zeros([n,l],float)
T[0,0]=T0
T[0,l-1]=Tf
T[0,1:l-1]=Tmid

Coef=h*D/(a*a)
plot(xx,T[0,:])
show()
t=1

for i in range(1,n):
    t=t+h  
    for x in range(1,l-1):
        T[i,0]=A+B*sin(2*pi*t/Tau0)
        T[i,l-1]=Tf
        T[i,1:l-1]=T[i-1,1:l-1]+Coef*(T[i-1,2:l]+T[i-1,0:l-2]-2*T[i-1,1:l-1])
    plot(xx,T[i,:])
    show()
    print("En el día ",t,"la temperatura superfic es: ",A+B*sin(2*pi*t/Tau0))      

for i in range(1,5):
    plot(xx,T[(Tau-Tau0)+i*90,:])
    print((Tau-Tau0)+i*90)
show()