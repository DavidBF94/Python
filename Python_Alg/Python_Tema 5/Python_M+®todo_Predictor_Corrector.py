import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algortimo implementa el método Predictor-Corrector de cuarto orden para
# resolver ecuaciones (o sistemas de ecuaciones) diferenciales

# 1 Definimos la función del problema ( dr / dt = f ( r , t ) )

g = 9.8

l = 0.1

def f ( r ):
    
    x1 = r[ 0 ]
    
    x2 = r[ 1 ]
    
    fx1 = x2
     
    fx2 = -( g / l ) * mt.sin ( x1 )
    
    f = np.array ( [ fx1 , fx2 ] , float )
    
    return f

# 2 Fijamos los límites temporales , la precisión deseada y las condiciones
#   iniciales del problema

t1 = 0.0

t2 = 10.0

N = 10000

h = ( t2 - t1 ) / N

t = np.arange ( t1 , t2 , h )

Precision = 1e-4

x01 , x02 = 179 * mt.pi / 180 , 0.0

r = np.array ( [ x01 , x02 ] , float ) 

x1points , x2points = [] , []  
    
x1points.append ( r [ 0 ] ) , x2points.append ( r [ 1 ] ) 

# 3 Resolvemos mediante un método R-K-4 los tres pasos siguientes después de 
#   las condiciones iniciales
   
for i in range ( 3 ) :
    
    k1 = h * f ( r )
    
    k2 = h * f ( r + ( 1 / 2 ) * k1 )
        
    k3 = h * f ( r + ( 1 / 2 ) * k2 )
        
    k4 = h * f ( r + k3 )
        
    r = r + ( 1 / 6 ) * ( k1 + 2 * k2 + 2 * k3 + k4 )
        
    x1points.append ( r [ 0 ] )
        
    x2points.append ( r [ 1 ] )

# 4 Una vez tenemos las 4 primeras soluciones implementamos el método
#   Predictor-Corrector

for i in range ( 3 , N -1 ) :
    
    Error = 1234
        
    while Error > Precision :
        
        r1 = [x1points [ i ] , x2points [ i ] ]
            
        r2 = [x1points [ i - 1 ] , x2points [ i - 1 ] ]
            
        r3 = [x1points [ i - 2 ] , x2points [ i - 2 ] ]
            
        r4 = [x1points [ i - 3 ] , x2points [ i - 3 ] ]
            
        r5 = r + ( h / 24 ) * ( 55 * f ( r1 ) - 59 * f ( r2 ) + 37 * f ( r3 ) - 9 * f ( r4 ) )
            
        r6 = r + ( h / 24 ) * ( 9 * f ( r5 ) + 19 * f ( r1 ) - 5 * f ( r2 ) + f ( r3 ) )
        
        Error = np.amax ( abs ( ( 19 / 270 ) * ( r6 - r5 ) ) )
        
    r = r6
    
    x1points.append ( r [ 0 ] )
            
    x2points.append ( r [ 1 ] )

# 5 Mostramos las soluciones por pantalla
  
mp.plot ( t , x1points )

mp.show()

mp.plot ( t , x2points )

mp.show()
