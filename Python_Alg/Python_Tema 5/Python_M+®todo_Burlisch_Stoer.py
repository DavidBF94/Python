import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de Burlisch-Stoer basado en el método del
# punto medio (Runge-Kutta-2)

# 1 Definimos la función de la ecuación (o sistema de ecuaciones) diferencial
#   dr/dt = f(r,t)

g = 9.8

l = 0.1

def f ( r ):
    
    x1 = r [ 0 ]
    
    x2 = r [ 1 ]
    
    fx1 = x2
     
    fx2 = -( g / l ) * mt.sin ( x1 )
    
    f = np.array ( [ fx1 , fx2 ] , float )
    
    return f

# 2 Fijamos el intervalo de tiempo, la anchura H del paso, la precisión y las
#   condiciones iniciales

n_ec = 2

t1 = 0.0

t2 = 10.0

N = 100

H = ( t2 - t1 ) / N

Delta = 1e-8

t = np.arange ( t1 , t2 , H )

x1points = []

x2points = []

x01 = 179 * mt.pi / 180

x02 = 0.0

r = np.array ( [ x01 , x02 ] , float )

# 3 Implementamos el algortitmo de Burlisch-Stoer

for i in t :
    
    x1points.append( r [ 0 ] )
    
    x2points.append( r [ 1 ] )
    
    n = 1
    
    r1 = r + ( 1 / 2 ) * H * f ( r )
    
    r2 = r + H * f ( r1 )
    
    R1 = np.zeros ( [ 1 , n_ec ] , float )
    
    R1 [ 0 ] = ( 1 / 2 ) * ( r2 + r1 + ( 1 / 2 ) * H * f ( r2 ) )
    
    Error = 2 * H * Delta
    
    while Error > H * Delta :
        
        n = n + 1
        
        h = H / n
        
        r1 = r + ( 1 / 2 ) * h * f ( r )
    
        r2 = r + h * f ( r1 )
        
        for i in range ( n-1 ) :
            
            r1 = r1 + h * f ( r2 )
    
            r2 = r2 + h * f ( r1 )
            
        R2 = np.zeros ( [ n , n_ec ] , float )
        
        R2 [ 0 ] = ( 1 / 2 ) * ( r2 + r1 + ( 1 / 2 ) * h * f ( r2 ) )
        
        for m in range ( 1 , n ) :
            
            Error = ( R2 [ m - 1 ] - R1 [ m - 1 ] ) / ( ( n / ( n - 1 ) ) ** (2 * m) - 1 )
            
            R2 [ m ] = R2 [ m - 1 ] + Error
            
        Error = abs ( Error [ 0 ] )
        
        R1 = R2
        
    r = R2 [ n - 1 ]
    
# 4 Mostramos las soluciones por pantalla
    
mp.plot ( t , x1points )

mp.plot ( t , x1points , "b. " )

mp.show()

mp.plot ( t , x2points )

mp.plot ( t , x2points , "b. " )

mp.show()
           