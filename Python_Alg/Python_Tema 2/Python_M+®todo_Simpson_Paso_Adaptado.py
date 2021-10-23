import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de Simpson con paso adaptado para la 
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

Suma1 = 0

for i in range(2,N-1,2):
    Suma1 = Suma1+f(Li+i*h)

S1 = (1/3)*(f(Li)+f(Ls)+2*Suma1)

Suma2 = 0

for i in range(1,N,2):
    Suma2 = Suma2+f(Li+i*h)

T1 = (2/3)*Suma2

I1 = h*(S1+2*T1)

print("N =",N,"Valor integral=",I1)

# 4 Doblamos el número de particiones y evaluamos la nueva aproximación para
#   la integral

N = 2*N

h = (1/2)*h

Suma2 = 0

for i in range(1,N,2):
    Suma2 = Suma2+f(Li+i*h)

T2 = (2/3)*Suma2

S2 = S1+T1

I2 = h*(S2+2*T2)

print("N =",N,"Valor integral=",I2)

# 5 Hallamos el error entre las dos aproximaciones e implementamos el algoritmo
#   del paso adaptado para el método de Simpson mostrando en cada caso el valor
#   de la integral y el número de particiones

Error = abs((1/15)*(I2-I1))

while Error > Precision:
    
    N = 2*N

    h = (1/2)*h
    
    I1 = I2
    
    S1 = S2
    
    T1 = T2
    
    Suma2 = 0

    for i in range(1,N,2):
        Suma2 = Suma2+f(Li+i*h)
    
    T2 = (2/3)*Suma2
    
    S2 = S1+T1
    
    I2 = h*(S2+2*T2)
    
    Error = abs((1/15)*(I2-I1))
    
    print("N =",N,"Valor integral=",I2)




