import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
import random as rd

# Éste algoritmo implementa un Método de Monte Carlo para la aproximación de 
# integrales definidas para determinadas funciones f(x)

# 1 Definimos la función f(x) que deseamos integrar

def f ( x ) :
    
    return ( mt.sin ( 1 / ( x * ( 2 - x ) ) ) ) ** 2

# 2 Fijamos los intervalos de integración 
    
a = 0.0

b = 2.0

# 3 Fijamos la cantidad M de puntos para dibujar f(x) , la cantidad N de 
#   números aleatorios iniciales para aproximar la integral , la precisión
#   deseada y los vectores donde guardaremos los puntos de f(x)

M = 1000

N = 10000

Precision = 1e-2

x = np.linspace ( a + 1e-10 , b - 1e-10 , M )

y = np.zeros ( M , float )

# 4 Hallamos los puntos para dibujar f(x)

for i in range ( M ) :
    
    y [ i ] = f (x [ i ] )

# 5 Introducimos el Método de Monte Carlo definiendo primero los vectores 
#   donde guardaremos los puntos que están dentro de la función y fuera de ella
#   y dando también un valor inicial para el error

Error = 1

while Error > Precision :
    
    x1 = []

    y1 = []

    Sumaf = 0.0

    Sumaff = 0.0
    
    for i in range ( N ) :
        
        x0 = b * rd.random ( )
        
        Sumaf = Sumaf + f ( x0 )
        
        Sumaff = Sumaff + f ( x0 ) * f ( x0 )
        
        x1.append ( x0 ) 
        
        y1.append ( f ( x0 ) )
        
        print ( " Iteración: " , i )
            
        mp.plot ( x , y , 'k-' )
            
        mp.plot ( x1 , y1 , 'bo' )
        
        mp.show ( )
        
    Varf = Sumaf / N + Sumaff / N
    
    Error = ( b - a ) * mt.sqrt ( Varf ) / mt.sqrt ( N )
    
    I = ( ( b - a ) / N ) * Sumaf
    
    N = 2 * N

# 6 Mostramos el valor aproximado de la integral con la precisión deseada y
#   la cantidad de números aleatorios necesitados
   
print ( " El valor aproximado de la Integral es : " , I )

print ( " " )

print ( " Se han necesitado " , N / 2 , " números aleatorios " )
 