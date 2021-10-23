import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método Trapezoidal con paso adaptado para la 
# resolución de integrales

# 1 Definimos la función de 1 variable a integrar

def f(x):
    
    return mt.sin(x)*x

# 2 Definimos los límites superior e inferior, la separación entre puntos y la
#   precisión deseada

Li = -10

Ls = 10

N = 1

h = (Ls-Li)/N

Precision = 0.0001

# 3 Introducimos el algoritmo del método Trapezoidal

I1 = (1/2)*(f(Li)+f(Ls))
I2 = 0

for i in range(1,N):
    I2 = I2+f(Li+i*h)

II1 = h*(I1+I2)

print("N =",N,"Valor integral=",II1)


# 4 Doblamos el número de particiones y evaluamos la nueva aproximación para
#   la integral

N = 2*N

h = (1/2)*h

Suma = 0

for i in range(1,N,2):
    Suma = Suma+f(Li+i*h)

II2 = (1/2)*II1+h*Suma

print("N =",N,"Valor integral=",II2)

# 5 Hallamos el error entre las dos aproximaciones e implementamos el algoritmo
#   del paso adaptado para el método Trapezoidal mostrando en cada caso el
#   valor de la integral y el número de particiones

Error = abs((1/3)*(II2-II1))

while Error > Precision:
    
    N = 2*N

    h = (1/2)*h
    
    II1 = II2
    
    Suma = 0

    for i in range(1,N,2):
        Suma = Suma+f(Li+i*h)
    
    II2 = (1/2)*II1+h*Suma
    
    Error = abs((1/3)*(II2-II1))
    
    print("N =",N,"Valor integral=",II2)

