import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de Romberg basado en el método
# Trapezoidal con paso adaptado para la resolución de Integrales

# 1 Definimos la función de 1 variable a integrar

def f(x):
    
    return mt.sin(x)*x

# 2 Definimos los límites superior e inferior, la separación entre puntos, la
#   precisión deseada y el primer nivel de Romberg

Li = -10

Ls = 10

N = 1

h = (Ls-Li)/N

Precision = 0.0001

Nivel = 1

# 3 Introducimos el algoritmo del método Trapezoidal y definimos el primer
#   nivel de Romberg

I1 = (1/2)*(f(Li)+f(Ls))
I2 = 0

for i in range(1,N):
    I2 = I2+f(Li+i*h)

II1 = h*(I1+I2)

R = np.empty(Nivel,float)

R[0] = II1

print("N =",N,"Nivel =",Nivel,"R =",R)


# 4 Doblamos el número de particiones,evaluamos la nueva aproximación para la
#   integral y definimos el segundo nivel de Romberg

Nivel = Nivel+1

N = 2*N

h = (1/2)*h

Suma = 0

for i in range(1,N,2):
    Suma = Suma+f(Li+i*h)

II2 = (1/2)*II1+h*Suma

R = np.empty(Nivel,float)

R[0] = II2

R[1] = (1/3)*(II2-II1)

print("N =",N,"Nivel =",Nivel,"R =",R)

# 5 Hallamos el error entre las dos aproximaciones e implementamos el algoritmo
#   del paso adaptado para el método Trapezoidal y el algoritmo del método de
#   Romberg

Error = abs((1/3)*(R[1]))

while Error > Precision:
    
    N = 2*N

    h = (1/2)*h
    
    II1 = II2
    
    Suma = 0

    for i in range(1,N,2):
        Suma = Suma+f(Li+i*h)
    
    II2 = (1/2)*II1+h*Suma
    
    Nivel = Nivel+1
    
    RR = np.empty(Nivel,float)
    
    RR[0] = II2
    
    for i in range(1,Nivel):
        RR[i] = RR[i-1]+(1/(4**i-1))*(RR[i-1]-R[i-1])
    
    Error = abs(RR[Nivel-1]-RR[Nivel-2])
    
    print("N =",N,"Nivel =",Nivel,"R =",RR)
    
    R = RR
    
    
    
    
    
    
    