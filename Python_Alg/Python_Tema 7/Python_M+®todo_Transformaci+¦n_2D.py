import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
import random as rd

# Éste algoritmo implementa el Método de Transformación de números aleatorios
# para crear números aleatorios con una Distribución de Probabilidad no 
# Uniforme

# Representaremos dichos números en un gráfico 2D

# 1 Definimos la Distribución de Probabilidad que deseamos que sigan nuestros
#   números aleatorios

Sigma =  20.0

def Gauss ( x ):
    
    return ( 1 / mt.sqrt ( 2 * mt.pi * Sigma ** 2 ) ) * mt.exp ( ( - x ** 2) / ( 2 * Sigma ** 2 ) )

# 2 Fijamos los límites en los que deseamos dibujar la Distribución de 
#   Probabilidad , el número de puntos ( M  ) y la cantidad de números 
#   aleatorios que deseamos crear ( N )

a = - 100.0

b = 100.0

M = 1000

N = 100

# 3 Definimos los vectores en los que guardaremos: Los puntos para dibujar,
#   los números aleatorios iniciales y finales y los valores sobre la 
#   Distribución de Probabilidad

x = np.linspace ( a , b , M )

Aleatorios1 = np.zeros ( N , float )

Aleatorios2 = np.zeros ( N , float )

Theta = np.zeros ( N , float )
  
R = np.zeros ( N , float )

x1 = np.zeros ( N , float )

x2 = np.zeros ( N , float )

Px = np.zeros ( M , float )

Px1 = np.zeros ( N , float )

Px2 = np.zeros ( N , float )

# 4 Dibujamos la Distribución de Probabilidad

for i in range ( M ):

    Px [ i ] = Gauss ( x [ i ] )

# 5 Implementamos el Método de Transformación específico para nuestra
#   Distribución de Probabilidad 
   
for i in range ( N ):
    
    Aleatorios1 [ i ] = rd.random ( )
    
    Aleatorios2 [ i ] = rd.random ( )
    
    Theta [ i ] = Aleatorios1 [ i ] * 2 * mt.pi 
    
    R [ i ] = mt.sqrt ( -2 * ( Sigma ** 2 ) * mt.log ( 1 - Aleatorios2 [ i ] ) )
    
    x1 [ i  ] = R [ i ] * mt.cos ( Theta  [ i ] )
    
    x2 [ i  ] = R [ i ] * mt.sin ( Theta  [ i ] )
    
    Px1 [ i ] = Gauss ( x1 [ i ] )
    
    Px2 [ i ] = Gauss ( x2 [ i ] )
    
    print ( " Iteracion : " , i )
    
    mp.plot ( x  , Px , 'k-' )
    
    mp.plot ( x1  , Px1 , 'bo' )
    
    mp.plot ( x2  , Px2 , 'ro' )
    
    mp.show ( )
 