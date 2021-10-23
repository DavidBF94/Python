from matplotlib.pyplot import imshow,show,quiver
from math import pi,sqrt
from numpy import zeros

eps=8.8541878176e-12
K=1/(4*pi*eps)
q1=1
q2=-1
L=100
N=100
h=L/N
I=10
c=1


#Creamos la malla de puntos

X=zeros([N+1,N+1],float)
Y=zeros([N+1,N+1],float)
for i in range(0,N+1):
    for j in range(0,N+1):
        X[i,j]=-(L//2)+h*j
        Y[j,i]=(L//2)-h*j
X=c*X
Y=c*Y

#Calculamos el potencial en cada punto de la malla

phi=zeros([N+1,N+1],float)
for i in range(0,N+1):
    for j in range(0,N+1):
        d1=(X[i,j]-I/2)**2+(Y[i,j])**2
        d2=(X[i,j]+I/2)**2+(Y[i,j])**2
        if d1!=0 and d2!=0:
           phi_1=K*q1*(1/sqrt(d1))
           phi_2=K*q2*(1/sqrt(d2))
           phi[i,j]=phi_1+phi_2
imshow(phi,origin="lower")
show()

#Calculamos y dibujamos las derivadas del potencial en cada punto

Ex=zeros([N+1,N+1],float)
Ey=zeros([N+1,N+1],float)
phix1=zeros([N+1,N+1],float)
phix2=zeros([N+1,N+1],float)
phiy1=zeros([N+1,N+1],float)
phiy2=zeros([N+1,N+1],float)
for i in range(0,N+1):
    for j in range(0,N+1):
        d1=(X[i,j]-I/2)**2+(Y[i,j])**2
        d2=(X[i,j]+I/2)**2+(Y[i,j])**2
        if d1!=0 and d2!=0:
           phix1[i,j]=(-K*q1*(-I/2+X[i,j]))/((d1)**(3/2))
           phix2[i,j]=(-K*q2*(I/2+X[i,j]))/((d2)**(3/2))
           phiy1[i,j]=(-K*q1*(Y[i,j]))/((d1)**(3/2))
           phiy2[i,j]=(-K*q2*(Y[i,j]))/((d2)**(3/2))
           Ex[i,j]=-phix1[i,j]-phix2[i,j]
           Ey[i,j]=-phiy1[i,j]-phiy2[i,j]

quiver(X,Y,Ex,Ey)
show()