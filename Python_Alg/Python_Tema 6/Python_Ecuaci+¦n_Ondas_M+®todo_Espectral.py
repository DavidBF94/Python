import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from scipy.fftpack import dst , idst
from scipy.interpolate import InterpolatedUnivariateSpline

# Éste algoritmo resuelve la Ecuación de Ondas Unidimensional con condiciones
# de contorno Phi(0) = Phi(L) = 0 para todo t y Psi(x,t=0) = f(x)
# Se emplea el Método Espectral

# 1 Definimos las constantes del problema, los pasos espaciales y temporales y
#   los vectores donde guardaremos la posición y el tiempo

v = 50.0

L = 1.0

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

Phi = np.zeros ( N , float )

Psi = np.zeros ( N , float )

Phi [ 0 ] , Phi [ N - 1 ] = 0.0 , 0.0 

print ( " t = " , t1 )

mp.plot ( x , Phi )

mp.show ( )

# 2 Definimos la función Phi inicial y hallamos los valores de la Transformada
#   del Seno alpha {k} y eta {k} 

for n in range ( 0 , N ):
    
    xn = n * a
    
    Psi [ n ] = ( C * xn * ( L - xn ) ) / ( L * L ) * np.exp (  ( - ( xn - d ) ** 2 ) / ( 2 * Sigma * Sigma ) )
    
    cte = ( - L ) / ( mt.pi * v )
    
    Psi [ n ] = cte * Psi [ n ]
    
alpha = dst ( Phi )

eta = dst ( Psi )

# 3 Tenemos en cuenta que la Transformada que hemos hallado ( en base a las
#   ecuaciones ) es k * eta {k}, así que hallamos eta {k}

for k in range ( 0 , N ):
    
    eta [ k ] = eta [ k ] / ( k + 1 )

# 4 Hallamos b {k} = alpha {k} + i eta {k} para hacer luego la Transformada del
#   Seno Inversa sobre b {k}

b = np.zeros ( N , float )

for i in t:
    
    for k in range ( 0 , N ):
        
        angulo = ( mt.pi * v * ( k + 1 ) * i ) / ( L )
        
        b [ k ] = alpha [ k ] * mt.cos ( angulo ) - eta [ k ] * mt.sin ( angulo )
        
    Phi = idst ( b )
    
    # 5 Pintamos la solución para Phi y su respectivo tiempo
    
    print ( " t = " , i )

    mp.plot ( x , np.abs ( Phi ) )
    
    mp.show ( )
            