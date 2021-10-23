import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de las Sumas de Riemann para integrales

# 1 Definimos la función de 1 variable a integrar

def f(x):
    
    return 1+x+x**2+x**3

# 2 Definimos los límites superior e inferior y la separación entre puntos

Li = -10

Ls = 10

N = 100000

h = (Ls-Li)/N

# 3 Introducimos el algoritmo de las Sumas de Riemann

I = 0.0

for i in range(N+1):
    I = I+h*f(Li+i*h)
    
# 4 Mostramos en pantalla el resultado de la aproximación de la integral 
#   hallada mediante el algoritmo
    
print("El valor aproximado de la integral por sumas de Riemann es :",I)