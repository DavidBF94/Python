import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
import random as rd
from mpl_toolkits.mplot3d import Axes3D  

# Éste algoritmo implementa un Método de Monte Carlo para la aproximación de 
# integrales  dobles definidas para determinadas funciones f(x,y) 

# 1 Definimos la función f(x,y) que deseamos integrar

def f ( x , y ):
    
    return x ** 2 + y ** 2

# 2 Fijamos los límites de integración en los ejes x e y 

x1 , x2 = -2.0 , 2.0

y1 , y2 = -2.0 , 2.0

# 3 Fijamos la cantidad de puntos que queremos para representar f(x,y) y la 
#   cantidad de números aleatorios que queremos emplear para la aproximación

M = 20

N = 100

# 4 Construimos la malla de puntos para representar f(x,y)

x = np.linspace ( x1 , x2 , M )

y = np.linspace ( y1 , y2 , M )

X , Y = np.meshgrid ( x , y )

# 5 Dibujamos f(x,y)

Z = np.zeros ( [ M , M ] , float )

for i in range ( M ):
    
    for j in range ( M ):
        
        Z [ i , j ] = f ( X [ i , j ] , Y [ i , j ] )
        
# 6 Hallamos el área base de nuestra "caja" e implementamos el Método de
#   Monte Carlo
        
A = ( x2 - x1 ) * ( y2 - y1 ) 

xx = np.random.uniform ( x1 , x2 , N )

yy = np.random.uniform ( y1 , y2 , N )

xx1 , yy1 , zz1 = [] , [] , []

Suma = 0

for i in range ( N ):
    
    Suma = Suma + f ( xx [ i ] , yy [ i ] )
    
    xx1.append ( xx [ i ] )
        
    yy1.append ( yy [ i ] )
        
    zz1.append ( f ( xx [ i ] , yy [ i ] ) )
    
    print ( " Iteracion = " , i )
        
    fig = mp.figure ( )

    ax = mp.axes(projection='3d')
            
    ax.plot_wireframe ( X , Y , Z , color = "black" )
    
    ax.scatter3D( xx1 , yy1 , zz1 , color = "red" )
    
    ax.view_init( 20 , 35 )
        
    mp.show ( )
    
# 7 Hallamos el valor aproximado de la integral y lo mostramos por pantalla

I = Suma * A / N
       
print ( " El valor aproximado de la integral es : " , I )

print ( " " )

print ( " Se han necesitado " , N , " números aleatorios " )
