import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import Axes3D  

# Éste algortimo resuelve la ecuación de Poisson para una malla de longitud
# L = 1 subdividida en N puntos y para dos densidades de carga de signo opuesto
# También fijamos potencial nulo en las paredes de la malla

# 1 Definimos el número de puntos en los que queremos hallar la solución , la
#   precisión , las matrices en las que guardaremos los resultados y los 
#   valores para las densidades de carga ( especificamos las posiciones de las
#   densidades de carga )

L = 1.0

N = 100

a = L / N

Epsilon = 1.0

Valor_Rho = 1.0

Precision = 1e-6

phi_1 = np.zeros ( [N , N ] , float )

phi_2 = np.zeros ( [N , N ] , float )

Rho = np.zeros ( [N , N ] , float )

Rho [ N // 5 : 2 * N//5 , 3 * N//5 : 4 * N//5 ] = Valor_Rho

Rho [ 3 * N//5 : 4 * N//5 , N // 5 : 2 * N//5 ] =  - Valor_Rho

# 2 Introducimos el algoritmo basado en Diferencias Finitas para la ecuación de
#   Poisson

Error = 1

while Error > Precision :  
    
    phi_2 [ 0 , : ] , phi_2 [ N - 1 , : ] , phi_2 [ : , 0 ] , phi_2 [ : , N - 1 ] = 0.0 , 0.0 , 0.0 , 0.0
                
    phi_2 [ 1 : N - 1 , 1 : N - 1 ] = ( 1 / 4 ) * ( phi_1 [ 2 : N  , 1 : N - 1 ] + phi_1 [ 0 : N - 2  , 1 : N - 1 ] + phi_1 [ 1 : N - 1  , 2 : N ] + phi_1 [ 1 : N - 1  , 0 : N - 2 ] ) + ( ( a ** 2 ) / (4 * Epsilon ) ) * Rho [1 : N - 1 , 1 : N - 1 ] 
                
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
      