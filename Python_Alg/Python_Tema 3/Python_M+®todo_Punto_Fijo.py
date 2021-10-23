import numpy as np
import math as mt
import matplotlib.pyplot as mp
import sympy as sp

# Éste algoritmo implementa el método del punto fijo para la resolución de
# ecuaciones no lineales

# 1 Definimos la precisión que deseamos junto con un valor inicial para el
#   error

Precision = 1e-10

Error = 1234.0

# 2 Definimos en simbolico la funcion del punto fijo (x=f(x)), su derivada y 
#   hallamos la función inversa en caso de que la función inicial no haga 
#   converger al método

x,y = sp.symbols('x y')
    
f = 2-sp.exp(-x)
    
df = sp.diff(f,x)

Ecuacion = y-f

f_inv = sp.solveset(Ecuacion,y)

# 3 Definimos la función y su derivada (que podemos haber hallado del paso 2)

def f(x):
    return 2-mt.exp(-x)

def df(x):
    return mt.exp(-x)

# 4 Fijamos un valor inicial para inicializar el método e implementamos el 
#   algoritmo del punto fijo (incluyendo la expresión para el error)

x0 = 1

Iteraciones = 1

while Error > Precision :
    
    x1 = f(x0)
    
    Error = abs((x1-x0)/(1-1/(df(x0))))
    
    x0 = x1
    
    Iteraciones = Iteraciones+1

# 5 Mostramos la solución aproximada de la ecuación junto con el error y el
#   número de iteraciones necesarias para hallar la solución
   
print("La solución de la ecuación es:",x1)
print("El error es:",Error)
print("El número de iteraciones necesarias ha sido :",Iteraciones)
