import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algortimo implementa el Método de Diferencias Finitas para resolver la
# EDO de segundo orden ( dx ^ 2 / dt ^ 2 = - g ) ( x ( t1 ) = x ( t2) = 0 )

# 1 Fijamos las constantes, intervalo de integración , precisión y número de 
#   pasos

g = 9.81

Precision = 1e-6

t1 = 0.0

t2 = 10.0

N = 100

h = ( t2 - t1 ) / N

t = np.arange ( t1 , t2 , h )

# 2 Introducimos el método de Diferencias Finitas fijando las condiciones
#   iniciales

x1 = np.zeros ( N , float )

Error = 1234

while Error > Precision:
    
    x2 = np.zeros ( N , float )
    
    x2 [ 0 ] , x2 [ N - 1 ] = 0.0 , 0.0
    
    x2 [ 1 : N - 1 ] = (1 / 2 ) * ( x1 [ 2 : N ] + x1 [ 0 : N - 2 ] + h * h * g ) 
    
    Error = max ( abs ( x2 - x1 ) )
    
    x1 = x2

# 3 Mostramos la solución por pantalla
    
mp.plot ( t , x1 )

mp.show ( )
