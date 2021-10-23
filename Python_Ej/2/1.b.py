from matplotlib.pyplot import plot,show
from math import tan,sqrt
from numpy import linspace
#Se escriben las dos funciones del modo f(x)=0
h=1.054571800*10**-34
m=9.1094*10**-31
w=10**-9
V=20
q=1.6022*10**-19
Precisión=0.001*q
n=100
def f1(E):
    return tan(sqrt(w*w*m*E*q/(2*h*h)))-sqrt((V-E)/E)
def f2(E):
    return tan(sqrt(w*w*m*E*q/(2*h*h)))+sqrt(E/(V-E))
#Se dibujan las dos funciones
E=[]
f11=[]
f22=[]
for i in linspace(0,20,n):
    E.append(i*q)
    f11.append(f1(i))
    f22.append(f2(i))
plot(E,f11)
plot(E,f22)
show()
#Elegimos la función de la que hallar ceros
Elección=float(input("Elija función para la que hallar ceros(f1(1);f2(2)): "))
if Elección==1:
    f=f1
    ff=f11
else:
    f=f2
    ff=f22
#Obtenemos los diferentes pares de x para los que la función cambia de signo
Lista=[]
for i in range(0,n-1):
    if ff[i]*ff[i+1]<0:
        Lista.append(E[i])
        Lista.append(E[i+1])
print("Los pares de puntos donde la función cambia de signo son: ",Lista)
#Elegimos el intervalo entre el que se hallará un cero de la función
#teniendo en cuenta la forma de la gráfica
x1=float(input("Límite inferior en x: "))
x2=float(input("Límite superior en x: "))
#Introducimos el método de la Bisección
while abs(x1-x2)>Precisión:
    xx=(1/2)*(x1+x2)
    if f(xx)*f(x1)>0:
       x1=xx
    else:
       x2=xx
else:
    xx=(1/2)*(x1+x2)
print("El valor del cero de la función (J) es: ",xx)
print("El valor del cero de la función (eV) es: ",xx*6.242e+18)



