import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import Axes3D  

# Éste algortimo resuelve la ecuación de Laplace en dos dimensiones y 
# cordenadas cartesianas en una malla cuadrada con potencial V en la parte de
# arriba y potencial nulo en los otros tres bordes del cuadrado 

# 1 Definimos el número de puntos en los que queremos hallar la solución , la
#   precisión y las matrices en las que guardaremos los resultados

N = 50

V = 1.0

Precision = 1e-6

phi_1 = np.zeros ( [N , N ] , float )

phi_2 = np.zeros ( [N , N ] , float )

phi_1 [ 0 , : ] = V

# 2 Introducimos el algoritmo basado en Diferencias Finitas para la ecuación de
#   Laplace

Error = 1

while Error > Precision :

    for i in range ( N ) :
        
        for j in range ( N ) :
            
            if i == 0 or i == N - 1 or j == 0 or j == N - 1 :
                
                phi_2 [ i , j ] = phi_1 [ i , j ]
            
            else :
                
                phi_2 [ i , j ] = ( 1 / 4 ) * (phi_1 [ i + 1 , j ] + phi_1 [ i - 1 , j ] + phi_1 [ i , j + 1 ] + phi_1 [ i , j - 1 ] )
                
    Error = np.max ( abs ( phi_2 - phi_1 ) )
    
    phi_1 , phi_2 = phi_2 , phi_1
    
# 3 Mostramos un gráfico de densidad con las soluciones
    
mp.imshow ( phi_1 , origin = " lower " )

mp.show ( )

# 4 Mostramos un gráfico 3D con las soluciones ( rotamos con view_init un 
#   poco la imagen )

x = np.linspace ( 0 , N , N )

y = np.linspace ( 0 , N , N )

X , Y = np.meshgrid ( x , y )

fig = mp.figure ( )

ax = mp.axes(projection='3d')

ax.plot_surface( X , Y , phi_1 )

ax.view_init( 60 , 35 )
      