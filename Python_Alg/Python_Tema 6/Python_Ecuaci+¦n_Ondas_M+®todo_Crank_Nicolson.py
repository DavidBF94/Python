import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from scipy.interpolate import InterpolatedUnivariateSpline

# Éste algortimo trata de resolver la Ecuación de Ondas unidimensional con
# condiciones de contorno Phi (0) = Phi (L) = 0 para todo t y 
# Psi (x,t=0) = f(x)
# Se emplea el método de Crank-Nicolson basado en el método de Diferencias
# Finitas y el método Implícito

# 1 Definimos las constantes del problema, los pasos espaciales y temporales y
#   los vectores donde guardaremos la posición y el tiempo

v = 20.0

L = 3.0

d = 0.1

C = 1.0

Sigma = 0.3

N = 200

a = L / N

t1 = 0.0

t2 = 1.0

M = 1000

h = ( t2 -t1 ) / M

x = np.linspace ( 0 , L , N )

t = np.linspace ( t1 , t2 , M )

# 2 Definimos los valores de las matrices tridiagonales A y B , fijamos el
#   valor inicial para Psi (Psi(x,t=0)) , el vector b donde incluimos los 
#   valores de los extremos para tener un sistema de ecuaciones cuadrado

a1 = ( 2 * h * v * v ) / ( a * a )

a2 = - ( h * v * v ) / ( a * a )

b1 = - ( 2 * h * v * v ) / ( a * a )

b2 = ( h * v * v ) / ( a * a )

Phi = np.zeros ( N , float )

Psi = ( C * x * ( L - x ) ) / ( L * L ) * np.exp (  ( - ( x - d ) ** 2 ) / ( 2 * Sigma * Sigma ) )

Phi [ 0 ] = 0.0

Phi [ N - 1 ] = 0.0

PhiPsi = np.zeros ( 2 * N - 2 , float )

PhiPsi2 = np.zeros ( 2 * N , float )

PhiPsi [ 0 : ( 2 * N - 2 ) // 2 - 1 ] = Phi [ 1 : ( 2 * N - 2 ) // 2 ] 

PhiPsi [ ( 2 * N - 2 ) // 2 - 1 : ( 2 * N - 2 ) ] = Psi [ 0 : N ]

PhiPsi2 [ 0 : N ] , PhiPsi2 [ N : 2 * N ] = Phi , Psi

A = np.zeros ( [ 2 * N - 2 , 2 * N - 2 ] , float )

B = np.zeros ( [ 2 * N - 2 , 2 * N - 2 ] , float )

b = np.zeros ( [ 2 * N - 2 ] , float )

b [ ( 2 * N ) // 2 ] = 2 * b2 * Phi [ 0 ]

b [ ( 2 * N - 3 ) ] = 2 * b2 * Phi [ N - 1 ]

print ( " t = " , t1 )

mp.plot ( x , PhiPsi2 [0 : N ] )

mp.show ( )

# 4 Definimos las matrices A y B de nuestro sistema de ecuaciones de tal 
#   manera que cumplan con las ecuaciones del método de Crank-Nicolson
#   ( Sistema de ecuaciones cuadrado )

j = 0
    
k = 1

for i in range ( ( 2 * N ) // 2 ):
    
    if i == 0:
        
        A [ i , N - 2 ] = - 0.5 * h
        
        B [ i , N - 2 ] = 0.5 * h
        
    elif i == ( 2 * N ) // 2 - 1 :
        
        A [ i , 2 * N - 3 ] = - 0.5 * h
        
        B [ i , 2 * N - 3 ] = 0.5 * h
        
    else :
        
        A [ i , j ] = 1.0
        
        A [ i , N - 2 + k ] = -0.5 * h
        
        B [ i , j ] = 1.0
        
        B [ i , N - 2 + k ] = 0.5 * h
        
        j = j + 1
        
        k = k + 1

k = 1
   
for i in range ( ( 2 * N ) // 2 , ( 2 * N ) - 2 ) :
    
    if i == ( 2 * N ) // 2 :
        
        A [ i , 0 ] = a1
        
        A [ i , 1 ] = a2
        
        A [ i , N - 1 ] = 1.0
        
        B [ i , 0 ] = b1
        
        B [ i , 1 ] = b2
        
        B [ i , N - 1 ] = 1.0
        
    elif i == ( 2 * N ) - 3 :
        
        A [ i , N - 4 ] = a2
        
        A [ i , N - 3 ] = a1
        
        A [ i , ( 2 * N ) - 4 ] = 1.0
        
        B [ i , N - 4 ] = b2
        
        B [ i , N - 3 ] = b1
        
        B [ i , ( 2 * N ) - 4 ] = 1.0
        
    else :
        
        A [ i , k - 1 ] = a2
        
        A [ i , k ] = a1
        
        A [ i , k + 1 ] = a2
        
        A [ i , N - 1 + k ] = 1.0
        
        B [ i , k - 1 ] = b2
        
        B [ i , k ] = b1
        
        B [ i , k + 1 ] = b2
        
        B [ i , N - 1 + k ] = 1.0
        
        k = k + 1

# 5 Para cada paso temporal  resolvemos el Sistema de Ecuaciones Lineales y lo
#   mostramos por pantalla junto con el tiempo y el índice del valor máximo de
#   la solución

for i in t [ 1 : M ]:
     
    BB = np.dot ( B , PhiPsi ) + b
    
    PhiPsi = np.linalg.solve ( A , BB )
    
    PhiPsi2 [ 1 : N - 1 ] = PhiPsi [ 0 : ( 2 * N - 4 ) // 2 ]
    
    PhiPsi2 [ N : 2 * N ] = PhiPsi [ ( 2 * N - 4 ) // 2 : 2 * N - 2 ]
    
    print ( " t = " , i )
    
    l = abs ( PhiPsi2 [0 : N ] )
    
    result = np.where ( l == max ( l ) )
    
    print ( " Índice del valor máximo de la solución : " , result [ 0 ][ 0 ] )

    mp.plot ( x , abs ( PhiPsi2 [0 : N ] ) )
    
    mp.show ( )
