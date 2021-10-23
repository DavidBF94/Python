import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import Axes3D  

# Éste algortimo resuelve la ecuación de Difusión unidimensional ( ecuación del 
# calor unidimensional ) mediante Diferencias Finitas

# 1 Definimos las constantes del problema, los límites de integración , la 
#   separación entre puntos, los vectores donde guardaremos los resultados y 
#   las condiciones iniciales del problema

D = 4.25e-6

L = 0.01

N = 100

a = L / N

t1 = 0.0

t2 = 1.0

M = 1000

h = ( t2 -t1 ) / M

x = np.linspace ( 0 , L , N )

t = np.linspace ( t1 , t2 , M )

T1 = np.zeros ( N , float )

T2 = np.zeros ( N , float )

T = np.zeros ( [ M , N ] , float )

T0 , TM , TF = 50.0 , 20.0 , 0.0

T1 [ 0 ] , T1 [ 1 : N - 1 ] , T1 [ N - 1 ] = T0 , TM , TF

T2 [ 0 ] , T2 [ N - 1 ] = T0 , TF

K = ( h * D ) / ( a * a )

# 2 Mostramos la temperatura en todos los puntos en el tiempo t1

mp.plot ( x , T1 )

mp.show ( )

print ( " t = " , t1 )

# 3 Implementamos el método de Diferencias Finitas para la ecuación de Difusión
#   Mostrando en cada paso temporal la solución para todos los puntos

for i in range ( M ):
    
    T2 [ 1 : N -1 ] = T1 [ 1 : N - 1 ] + K * ( T1 [ 2 : N ] + T1 [ 0 : N - 2 ] - 2 * T1 [ 1 : N - 1 ] )
    
    T1 , T2 = T2 , T1
    
    T [ i , : ] = T1
    
    mp.plot ( x , T1 )

    mp.show ( )
    
    print ( " t = " , t1 + h * ( i + 1 ) )
    
# 4 Mostramos un gráfico 3D con la solución de la ecuación ( T ( x , t ) ) 
#   rotando un poco la figura con view_init
    
X , tt = np.meshgrid ( x , t )

fig = mp.figure ( )

ax = mp.axes(projection='3d')

ax.plot_surface( X , tt , T )

ax.view_init( 60 , 35 )
    