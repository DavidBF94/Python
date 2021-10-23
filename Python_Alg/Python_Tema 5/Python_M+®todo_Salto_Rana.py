import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método del salto de rana para resolver EDOS 

# 1 Definimos la función f(r)

g = 9.8

l = 0.1

def f ( r ):
    
    x1 = r[ 0 ]
    
    x2 = r[ 1 ]
    
    fx1 = x2
     
    fx2 = -( g / l ) * mt.sin ( x1 )
    
    f = np.array ( [ fx1 , fx2 ] , float )
    
    return f

# 2 Definimos los intervalos de integración t1 y t2 junto con todos los puntos
#   en los que dividiremos el intervalo

t1 = 0

t2 = 10

N = 1000

h = ( t2 - t1 ) / N

t = np.arange ( t1 , t2 , h )

# 3 Definimos los vectores donde guardaremos los puntos x1 y x2 , fijamos una
#   serie de condiciones iniciales para ambas variables y calculamos el primer
#   término medio ( r ( t + ( 1 / 2 ) * h ) )

x1points = []

x2points = []

r1 = np.array ( [ 179 * mt.pi / 180 , 0.0 ] , float )

r2 = r1 + ( 1 / 2 ) * h * f ( r1 )

# 4 Introducimos el algortitmo del método del salto de rana

for i in t :
    
    x1points.append ( r1 [ 0 ] )
    
    x2points.append ( r1 [ 1 ] )
    
    r1 = r1 + h * f ( r2 )
    
    r2 = r2 + h * f ( r1 )
    
# 5 Mostramos las soluciones por pantalla
    
mp.plot(x1points)

mp.show()

mp.plot(x2points)

mp.show()
    
    
    
    
    
    
    
