import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de la secante para la resolución de
# ecuaciones no lineales

# 1 Definimos la precisión que deseamos junto con un valor inicial para el
#   error

Precision = 1e-10

Error = 1234.0

Iteraciones = 1

# 2 Definimos la función (f(x)=0)

def f(x):
    return mt.exp(x)-2

# 3 Implementamos el algoritmo del método de la secante fijando unos valores
#   iniciales para comenzar a iterar

x1 = 1

x2 = 2

while Error > Precision:
    
    x3 = x2-f(x2)*((x2-x1)/(f(x2)-f(x1)))
    
    Error = abs(x3-x2)
    
    x1 = x2
    
    x2 = x3
    
    Iteraciones = Iteraciones+1
    
# 4 Mostramos la solución aproximada de la ecuación junto con el error y el
#   número de iteraciones necesarias para hallar la solución
   
print("La solución de la ecuación es:",x3)
print("El error es:",Error)
print("El número de iteraciones necesarias ha sido :",Iteraciones)