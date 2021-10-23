import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from scipy.fftpack import dst , idst
from scipy.interpolate import InterpolatedUnivariateSpline

# Éste algortimo trata de resolver la Ecuación de Schrodinger unidimensional
# para una particula libre con condiciones de contorno Psi (0) = Psi (L) = 0
# para todo t y Psi(x,t=0)=f(x)
# Se emplea el método Espectral

# 1 Definimos las constantes del problema, los pasos espaciales y temporales y
#   los vectores donde guardaremos la posición y el tiempo

m = 9.109e-31

hbar = 1.055e-34

sigma = 1.0e-10

kappa = 5.0e10

L = 1.0e-8

N = 1000

a = L / N

t1 = 0.0

t2 = 2e-15

M = 1000

h = ( t2 -t1 ) / M

x0 = L / 2

C = ( mt.pi * mt.pi * hbar ) / ( 2 * m * L * L )

x = np.linspace ( 0 , L , N )

t = np.linspace ( t1 , t2 , M )

# 2 Definimos las partes real e imaginaria de la Función de Onda inicial y 
#   hallamos los valores alpha {k} y eta {k} de la Transformada del Seno

rePsi = np.zeros ( N , float )

imPsi = np.zeros ( N , float )

rePsi [ 0 ] , rePsi [ N - 1 ] , imPsi [ 0 ] , imPsi [ N - 1 ] = 0.0 , 0.0 , 0.0 , 0.0

for n in range ( 1 , N - 1 ):
    
    xn = n * a
    
    gauss = mt.exp ( - ( xn - x0 ) ** 2 / ( 2 * sigma ** 2 ) )
    
    rePsi [ n ] = gauss * mt.cos ( kappa * xn )
    
    imPsi [ n ] = gauss * mt.sin ( kappa * xn )
    
alpha = dst ( rePsi )

eta = dst ( imPsi )

b = np.zeros ( N , float )

# 3 Normalizamos la función de onda interpolando el cuadrado de su valor 
#   absoluto y mostramos la solución de la parte real de la función de onda, el
#   tiempo y el valor de la integral de la densidad de probabilidad

f = InterpolatedUnivariateSpline ( x , ( np.abs ( rePsi ) ) ** 2 , k = 2 )

Integral = f.integral ( 0 , L )

rePsi = ( 1 / mt.sqrt ( Integral ) ) * rePsi

f = InterpolatedUnivariateSpline ( x , ( np.abs ( rePsi ) ) ** 2 , k = 2 )

Integral = f.integral ( 0 , L )

print ( " t = " , t1 )

print ( " Integral de la Densidad de Probabilidad = " , Integral )
    
mp.plot ( x , rePsi )
    
mp.show ( )

# 4 Hallamos b {k} = alpha {k} + i eta {k} para hacer luego la Transformada del
#   Seno Inversa sobre b {k}

for i in t:
    
    for k in range ( 0 , N ):
        
        angulo = C * ( k + 1 ) * ( k + 1 ) * i
        
        b [ k ] = alpha [ k ] * mt.cos ( angulo ) - eta [ k ] * mt.sin ( angulo )
    
    rePsi = idst ( b )
    
    # 5 Normalizamos la función de onda interpolando el cuadrado de su valor 
    #   absoluto y mostramos la solución de la parte real de la Función de Onda
    #    el tiempo y el valor de la integral de la densidad de probabilidad
    
    f = InterpolatedUnivariateSpline ( x , ( np.abs ( rePsi ) ) ** 2 , k = 2 )

    Integral = f.integral ( 0 , L )
    
    rePsi = ( 1 / mt.sqrt ( Integral ) ) * rePsi
    
    f = InterpolatedUnivariateSpline ( x , ( np.abs ( rePsi ) ) ** 2 , k = 2 )
    
    Integral = f.integral ( 0 , L )
    
    print ( " t = " , i )
    
    print ( " Integral de la Densidad de Probabilidad = " , Integral )
    
    mp.plot ( x , rePsi )
    
    mp.show ( )
