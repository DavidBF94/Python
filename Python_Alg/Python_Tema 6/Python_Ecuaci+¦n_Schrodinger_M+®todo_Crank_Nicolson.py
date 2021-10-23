import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from scipy.interpolate import InterpolatedUnivariateSpline

# Éste algortimo trata de resolver la Ecuación de Schrodinger unidimensional
# para una particula libre con condiciones de contorno Psi (0) = Psi (L) = 0
# para todo t y Psi(x,t=0)=f(x)
# Se emplea el método de Crank-Nicolson basado en el método de Diferencias
# Finitas y el método Implícito

# 1 Definimos las constantes del problema, los pasos espaciales y temporales y
#   los vectores donde guardaremos la posición y el tiempo

m = 9.109e-31

hbar = 1.055e-34

sigma = 1.0e-10

kappa = 5.0e10

L = 1.0e-8

N = 200

a = L / N

t1 = 0.0

t2 = 2e-15

M = 1000

h = ( t2 -t1 ) / M

x0 = L / 2

x = np.linspace ( 0 , L , N )

t = np.linspace ( t1 , t2 , M )

# 2 Definimos los valores de las matrices tridiagonales A y B , fijamos el
#   valor inicial para Psi (Psi(x,t=0)) , el vector b donde incluimos los 
#   valores de los extremos para tener un sistema de ecuaciones cuadrado

a1 = ( 1 + ( 1j * h * hbar ) / ( 2 * m * a * a ) )

a2 = - ( 1j * h * hbar ) / ( 4 * m * a * a )

b1 = ( 1 - ( 1j * h * hbar ) / ( 2 * m * a * a ) )

b2 =  ( 1j * h * hbar ) / ( 4 * m * a * a )

Psi = np.exp ( - ( x - x0 ) ** 2 / ( 2 * sigma ** 2 ) ) * np.exp (1j * kappa * x )

Psi [ 0 ] , Psi [ N - 1 ] = 0.0 , 0.0

A = np.zeros ( [ N - 2 , N - 2 ] , complex )

B = np.zeros ( [ N - 2 , N - 2 ] , complex )

b = np.zeros ( [ N - 2 ] , complex )

b [ 0 ] , b [ N - 3 ] = 2 * b2 * Psi [ 0 ] , 2 * b2 * Psi [ N - 1 ]

# 3 Normalizamos la función de onda interpolando el cuadrado de su valor 
#   absoluto y mostramos la solución de la parte real de la función de onda, el
#   tiempo y el valor de la integral de la densidad de probabilidad

f = InterpolatedUnivariateSpline ( x , ( np.abs ( Psi ) ) ** 2 , k = 2 )

Integral = f.integral ( 0 , L )

Psi = ( 1 / mt.sqrt ( Integral ) ) * Psi

f = InterpolatedUnivariateSpline ( x , ( np.abs ( Psi ) ) ** 2 , k = 2 )

Integral = f.integral ( 0 , L )

print ( " t = " , t1 )

print ( " Integral de la Densidad de Probabilidad = " , Integral )

mp.plot ( x , np.real (Psi ) )

mp.show ( )

# 4 Definimos las matrices A y B de nuestro sistema de ecuaciones de tal 
#   manera que cumplan con las ecuaciones del método de Crank-Nicolson
#   ( Sistema de ecuaciones cuadrado )

for i in range ( N - 2 ):
    
    if i == 0:
        
        A [ i , i ] , A [ i , i + 1 ]  = a1 , a2 
        
        B [ i , i ] , B [ i , i + 1 ]  = b1 , b2 
        
    elif i == N - 3:
    
        A [ i , i - 1 ] , A [ i , i ] = a2 , a1
        
        B [ i , i - 1 ] , B [ i , i ] = b2 , b1
        
    else :
        
        A [ i , i - 1 ] , A [ i , i ] , A [ i , i + 1 ] = a2 , a1 , a2
        
        B [ i , i - 1 ] , B [ i , i ] , B [ i , i + 1 ] = b2 , b1 , b2

# 5 Introducimos el método de Crank-Nicolson
        
for i in t [ 1 : M ]:
    
    BB = np.dot ( B , Psi [ 1 : N - 1 ] ) + b
    
    Psi [ 1 : N - 1 ] = np.linalg.solve ( A , BB )
    
    # 6 Normalizamos la función de onda recién calculada y mostramos la 
    #   solución de la parte real de la función de onda, el tiempo y el valor
    #   de la integral de la densidad de probabilidad
    
    f = InterpolatedUnivariateSpline ( x , ( np.abs ( Psi ) ) ** 2 , k = 2 )

    Integral = f.integral ( 0 , L )
    
    Psi = ( 1 / mt.sqrt ( Integral ) ) * Psi
    
    f = InterpolatedUnivariateSpline ( x , ( np.abs ( Psi ) ) ** 2 , k = 2 )

    Integral = f.integral ( 0 , L )
    
    print ( " t = " , i )
    
    print ( " Integral de la Densidad de Probabilidad = " , Integral )
    
    mp.plot ( x , np.real (Psi ) )

    mp.show ( )
    