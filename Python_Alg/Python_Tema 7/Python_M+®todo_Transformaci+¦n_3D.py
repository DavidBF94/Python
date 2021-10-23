import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
import random as rd
from mpl_toolkits.mplot3d import Axes3D  

# Éste algoritmo implementa el Método de Transformación de números aleatorios
# para crear números aleatorios con una Distribución de Probabilidad no 
# Uniforme

# Representaremos dichos números en un gráfico 3D

# 1 Definimos la Distribución de Probabilidad que deseamos que sigan nuestros
#   números aleatorios

Sigma =  20.0

def Gauss ( x , y ):
    
    return ( 1 / ( 2 * mt.pi * Sigma ** 2 ) ) * mt.exp ( ( - x ** 2 - y ** 2) / ( 2 * Sigma ** 2 ) )

# 2 Fijamos los límites en los que deseamos dibujar la Distribución de 
#   Probabilidad , el número de puntos ( M  ) y la cantidad de números 
#   aleatorios que deseamos crear ( N )

a = - 100.0

b = 100.0

M = 20

N = 100

# 3 Definimos los vectores en los que guardaremos: Los puntos para dibujar,
#   los números aleatorios iniciales y finales y los valores sobre la 
#   Distribución de Probabilidad

x = np.linspace ( a , b , M )

y = np.linspace ( a , b , M )

X , Y = np.meshgrid ( x , y )

Z = np.zeros ( [ M , M ] , float )

Aleatorios1 = np.zeros ( N , float )

Aleatorios2 = np.zeros ( N , float )

Theta = np.zeros ( N , float )
  
R = np.zeros ( N , float )

x1 = np.zeros ( N , float )

x2 = np.zeros ( N , float )

Px1x2 = np.zeros ( N , float )

# 4 Dibujamos la Distribución de Probabilidad

for i in range ( M ):
    
    for j in range ( M ):
        
        Z [ i , j ] = Gauss ( X [ i , j ] , Y [ i , j ] )
        
# 5 Implementamos el Método de Transformación específico para nuestra
#   Distribución de Probabilidad 

for i in range ( N ):
    
    Aleatorios1 [ i ] = rd.random ( )
    
    Aleatorios2 [ i ] = rd.random ( )
    
    Theta [ i ] = Aleatorios1 [ i ] * 2 * mt.pi 
    
    R [ i ] = mt.sqrt ( -2 * ( Sigma ** 2 ) * mt.log ( 1 - Aleatorios2 [ i ] ) )
    
    x1 [ i  ] = R [ i ] * mt.cos ( Theta  [ i ] )
    
    x2 [ i  ] = R [ i ] * mt.sin ( Theta  [ i ] )
    
    Px1x2 [ i ] = Gauss ( x1 [ i ] , x2 [ i ] )
    
    print ( " Iteracion : " , i )
        
    fig = mp.figure ( )
    
    ax = mp.axes(projection='3d')
        
    ax.plot_wireframe ( X , Y , Z , color = "black" )
    
    ax.scatter3D( x1 , x2 , Px1x2 , color = "blue" )
        
    ax.view_init( 20 , 35 )
        
    mp.show ( )
 