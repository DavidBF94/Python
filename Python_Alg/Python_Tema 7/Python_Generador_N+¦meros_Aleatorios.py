import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
import random as rd

# Éste algoritmo implementa una Relación de Recurrencia para hallar una 
# sucesión de números Pseudo-Aleatorios y comparamos con la sucesión de números
# hallados con la librería random de Python

# 1 Definimos las constantes de la Ecuación de Recurrencia

a = 1664525

c = 1013904223

m = 4294967296

# 2 Definimos la cantidad de números que deseamos y los arrays en donde los 
#   guardaremos, también definimos la semilla de nuestra Ecuación

N = 100

x1 = np.zeros ( N ,  float )

x2 = np.zeros ( N ,  float )

x1 [ 0 ] = 1

x2 [ 0 ] = rd.randrange ( 0 , 2 )

xx = np.linspace ( 0 , N , N ) 

# 3 Introducimos el algoritmo y vamos representando los números                 

for i in range ( 1 , N ):
    
    x1 [ i ] = ( a * x1 [ i - 1 ] + c ) % m
    
    x2 [ i ] = rd.random ( )
    
    print ( " Posición : " , i )
    
    mp.plot ( xx , x1 / m , " bo " )
    
    mp.plot ( xx , x2 , " ro " )
    
    mp.show ( ) 
 