import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algortimo implementa el método del disparo para una ecuación 
# (o sistema de ecuaciones) diferencial

# 1 Definimos el intervalo de tiempos que nos interesa en base a las 
#   condiciones de contorno del problema en cuestión junto con la precisión
#   deseada

t1 = 0.0

t2 = 10.0

N = 1000

h = ( t2 - t1 ) / N

t = np.arange ( t1 , t2 , h )

Precision = 1e-10

# 2 Definimos la función del problema ( dr / dt = f ( r , t ) ) y las 
#   condiciones iniciales

g = 9.8

x01 = 0.0

def f ( r ):
    
    x1 = r [ 0 ]
    
    x2 = r [ 1 ]
    
    fx1 = x2
     
    fx2 = - g
    
    f = np.array ( [ fx1 , fx2 ] , float )
    
    return f

# 3 Definimos la función K_R que implementa el método R-K-4 para una 
#   determinada condición inicial

def K_R ( x02 ) :
    
    r = np.array ( [ x01 , x02 ] , float ) 
    
    x1points = []

    x2points = []
    
    x1points.append ( r [ 0 ] )
        
    x2points.append ( r [ 1 ] ) 
    
    for i in t :
        
        k1 = h * f ( r )
    
        k2 = h * f ( r + ( 1 / 2 ) * k1 )
        
        k3 = h * f ( r + ( 1 / 2 ) * k2 )
        
        k4 = h * f ( r + k3 )
        
        r = r + ( 1 / 6 ) * ( k1 + 2 * k2 + 2 * k3 + k4 )
        
        x1points.append ( r [ 0 ] )
        
        x2points.append ( r [ 1 ] ) 
        
    return x1points [ N ]

# 4 Implementamos el método de la Bisección con dos valores iniciales de prueba

x2_1 = 0.01

x2_2 = 1000.0

x1_1 = K_R ( x2_1 )

x1_2 = K_R ( x2_2 )

while abs ( x1_2 - x1_1 ) > Precision :
    
    x2_m = ( 1 / 2 ) * ( x2_1 + x2_2)
    
    x1_m = K_R ( x2_m )
    
    if x1_1 * x1_m > 0 :
        
        x2_1 = x2_m
        
        x1_1 = x1_m
        
    else :
        
        x2_2 = x2_m
        
        x1_2 = x1_m
        
x2_m = ( 1 / 2 ) * ( x2_1 + x2_2)

# 5 Mostramos por pantalla el valor inicial que necesitamos para que se cumplan
#   las condiciones de contorno

print ( " El valor inicial de x2 ( x02 ) es : " , x2_m )
      