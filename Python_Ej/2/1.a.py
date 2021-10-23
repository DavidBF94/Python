from matplotlib.pyplot import plot,show,xlim,ylim
from math import tan,sqrt
from numpy import linspace
h=1.054571800*10**-34
m=9.1094*10**-31
w=10**-9
V=20
q=1.6022*10**-19
n=100
def y1(E):
    return tan(sqrt(w*w*m*E*q/(2*h*h)))
def y2(E):
    return sqrt((V-E)/E)
def y3(E):
    return -sqrt(E/(V-E))
E=[]
y11=[]
y22=[]
y33=[]
for i in linspace(0,20,n):
    y11.append(y1(i))
    y22.append(y2(i))
    y33.append(y3(i))
    E.append(i*q)
plot(E,y11)
plot(E,y22)
plot(E,y33)
show()
#Elegimos el intervalo para encontrar los distintos ceros
x1=float(input("Límite inferior en x: "))
x2=float(input("Límite superior en x: "))
y1=float(input(("Límite inferior en y: ")))
y2=float(input(("Límite superior en y: ")))
plot(E,y11)
plot(E,y22)
plot(E,y33)
xlim(x1,x2)
ylim(y1,y2)
show()



    

