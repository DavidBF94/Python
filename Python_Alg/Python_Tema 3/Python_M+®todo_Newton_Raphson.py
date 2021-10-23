import numpy as np
import math as mt
import matplotlib.pyplot as mp
import sympy as sp

# Éste algoritmo implementa el método de Newton-Raphson para la resolución de
# ecuaciones no lineales

# 1 Definimos la precisión que deseamos junto con un valor inicial para el
#   error

Precision = 1e-10

Error = 1234.0

Iteraciones = 1

# 2 Definimos en simbolico la funcion del método (f(x)=0) y su derivada 

x = sp.symbols('x')
    
f = 2-sp.exp(-x)
    
df = sp.diff(f,x)

# 3 Definimos la función y su derivada (que podemos haber hallado del paso 2)

def f(x):
    return mt.exp(x)-2

def df(x):
    return mt.exp(x)

# 4 Implementamos el algoritmo del método de Newton-Raphson fijando un valor
#   inicial para comenzar a iterar
    
x0 = 2

while Error > Precision:
    
    x = x0-f(x0)/df(x0)
    
    Error = abs(x-x0)
    
    x0 = x
    
    Iteraciones = Iteraciones+1
    
# 5 Mostramos la solución aproximada de la ecuación junto con el error y el
#   número de iteraciones necesarias para hallar la solución
   
print("La solución de la ecuación es:",x)
print("El error es:",Error)
print("El número de iteraciones necesarias ha sido :",Iteraciones)

