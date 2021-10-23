import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
import random as rd
from mpl_toolkits.mplot3d import Axes3D
import itertools as itr
from sklearn.datasets import make_circles

###############################################################################

# Algoritmo para implementar una Red Neuronal 

# Realizado por : David Brunete Fernández

###############################################################################

# Definimos el vector n que indica el número de capas y el número de neuronas
# por capa.

n = np.array ( [ 1 , 4 , 8 , 1 ] , int )

###############################################################################

# Bloque 1

###############################################################################

# INICIO ALGORITMO GENERAL - PARTE 1

# Creamos la malla de puntos ( neuronas ) dados por el vector n con una matriz
# de ceros y los representamos con scatter.

nx = len ( n )

ny = np.amax ( n )

x = np.linspace ( 0 , nx - 1 , nx )

y = np.zeros ( [ ny , nx ] , int )

for i in range ( nx ) :
    
    Contador = 0
    
    for j in range ( n [ i ] ) :
        
       y [ j , i ] =  Contador
       
       Contador = Contador + 1
       
for i in range ( ny ) :
    
    mp.scatter( x , y [ i , : ] , s = 200 , facecolors = 'none' , edgecolors = 'b' )    

###############################################################################

# Bloque 2

###############################################################################

# Calculamos el número de caminos totales posibles dentro de nuestra red y 
# creamos una matriz yy donde los guardaremos en un futuro.
    
# Gracias a la libreria itertools ( .product en nuestro caso ) creamos una 
# lista ( C1 ) donde guardamos en forma de "tuple" las posibles combinaciones
# de caminos para nuestra red.

ncaminos = 1

for i in range ( nx ) :
    
    ncaminos = ncaminos * n [ i ]

yy = np.zeros ( [ ncaminos , nx ] , int )

Contador = 0

C1 = y [ 0 : n [ Contador ] , Contador ]
    
C2 = y [ 0 : n [ Contador + 1 ] , Contador + 1 ]

for i in range ( nx - 1 ) :
    
    C1 = list ( itr.product ( C1 , C2 ) )
    
    Contador = Contador + 1
    
    if Contador <= nx - 2 :
    
        C2 = y [ 0 : n [ Contador + 1 ] , Contador + 1 ]

###############################################################################

# Bloque 3

###############################################################################

# Dado que la lista C1 está en forma de "tuple" la pasamos a formato "int"
# guardando dichos datos en la matriz yy.
        
# Después los representamos con plot.

for i in range ( ncaminos ) :
    
    Q = C1 [ i ]
    
    Contador = nx - 1
    
    for j in range ( nx ) :
        
        if Contador <= 1 :
            
            yy [ i , Contador ] = Q [ 1 ]
            
            yy [ i , Contador - 1 ] = Q [ 0 ]
            
            break
        
        yy [ i , Contador ] = Q [ 1 ]
    
        Contador = Contador - 1
        
        Q = Q [ 0 ]
    
    mp.plot ( x , yy [ i , : ] , 'r' , linewidth = 0.1 )    

###############################################################################

# Hacemos una representación de toda nuestra Red Neuronal.
  
mp.show ( )    

###############################################################################

# Bloque 4

###############################################################################

# Introducimos nuestros valores para la Entrada ( X ) y la Salida ( S ) de
# entrenamiento para nuestra Red.

# Escalamos los valores de X y S entre 0 y 1 :

num = 300

X1 = []
S1 = []

for i in range ( num ):
    X1.append( rd.uniform ( -15 , 15 ) )
    S1.append (  X1[ i ] ** 2 )

X1 = np.array ( X1 )
S1 = np.array ( S1 )
 
X1 = X1.reshape(-1,1)
X1 = np.transpose ( X1 )

S1 = S1.reshape(-1,1)
S1 = np.transpose ( S1 )

X2 = np.zeros ( [ n [ 0 ] , num ] , float )

S2 = np.zeros ( [ n [ nx - 1 ] , num ] , float )

for i in range ( n [ 0 ] ) :

    Xmin , Xmax = np.amin ( X1 [ i , : ] ) , np.amax ( X1 [ i , : ] )
    
    X2 [ i , : ] = ( X1 [ i , : ] - Xmin ) / ( Xmax - Xmin )
    
for i in range ( n [ nx - 1 ] ) :
    
    Smin , Smax = np.amin ( S1 [ i , : ] ) , np.amax ( S1 [ i , : ] )
    
    S2 [ i , : ] = ( S1 [ i , : ] - Smin ) / ( Smax - Smin )

###############################################################################

# Bloque 5
        
###############################################################################

# Fijamos unos valores iniciales aleatorios para los valores de los pesos entre
# capas ( W ij ) y para los valores de los pesos de los umbrales ( U i ).

U = np.zeros ( [ ny , nx - 1 ] , float )

Contador = 1

for i in range ( nx - 1 ) :
    
    for j in range ( n [ Contador ] ) :
        
        U [ j , i ] = rd.random ( )
    
    Contador = Contador + 1

nW = np.zeros ( nx - 1 , int )

for i in range ( nx - 1 ) :
    
    nW [ i ] = n [ i ] * n [ i + 1 ]
    
nWMax = np.amax ( nW )

W = np.zeros ( [ nWMax , nx - 1 ] , float )

for i in range ( nx - 1 ) :
    
    for j in range ( nW [ i ] ) :
        
        W [ j , i ] = rd.random ( )
        
        
# Definimos la Función Sigmoide.


#
    
def f ( x ) :

    return 1 / ( 1 + mt.exp ( - x ) )

#


###############################################################################
    
# Bloque 6
    
###############################################################################

# Algoritmo Principal de la Red Neuronal.

Alpha = 0.1

A = np.zeros ( [ ny , nx ] , float )

Error = []

for Etapas in range ( 6000 ) :

    for Entradas in range ( num ) :
    
        # Calculamos los valores de activación de las neuronas en la matriz A
        # a partir de los datos de la Entrada y los Pesos : W ij , U i .
        
        for Columnas_A in range ( nx ) :
            
            if Columnas_A == 0 :
                
                for Filas_A in range ( n [ Columnas_A ] ) :
                    
                    A [ Filas_A , Columnas_A ] = X2 [ Filas_A , Entradas ]
                    
            else :
                
                Contador = 0
                
                for Filas_A in range ( n [ Columnas_A ] ) :
                    
                    SumaWA = 0
                    
                    for Filas_A_A in range ( n [ Columnas_A - 1 ] ) :
                        
                         a = A [ Filas_A_A , Columnas_A - 1 ]
                         
                         b = W [ Contador + Filas_A_A * n [ Columnas_A ] , Columnas_A - 1 ]
                         
                         SumaWA = SumaWA + a * b
                         
                    Contador = Contador + 1
                         
                    A [ Filas_A , Columnas_A ] = f ( SumaWA + U [ Filas_A , Columnas_A - 1 ] )
                    
        # Calculada la matriz A a partir de los datos de la Entrada y los Pesos :
        # W ij , U i .
        
        # FIN DEL ALGORITMO GENERAL - PARTE 1
    
    ###############################################################################
        
    # Bloque 7
    
    ###############################################################################
    
    
        # Introducimos un Algoritmo para una Red Neuronal de 4 Capas.
        
        
        # Distribuimos los pesos W ij de la matriz W en 3 matrices W1 , W2 y W3.
        
        # Será por tanto una matriz por cada zona de caminos entre capas.
        
        W1 = np.zeros ( [ n [ 0 ] , n [ 1 ] ] , float )
        
        W2 = np.zeros ( [ n [ 1 ] , n [ 2 ] ] , float )
        
        W3 = np.zeros ( [ n [ 2 ] , n [ 3 ] ] , float )
        
        Contador1 = 0
        
        Contador2 = 0
        
        Contador3 = 0
        
        for Filas in range ( n [ 0 ] ) :
            
            W1 [ Filas , : ] = W [ Contador1 * n [ 1 ] : ( Contador1 + 1 ) * n [ 1 ] , 0 ]
            
            Contador1 = Contador1 + 1
            
        for Filas in range ( n [ 1 ] ) :
            
            W2 [ Filas , : ] = W [ Contador2 * n [ 2 ] : ( Contador2 + 1 ) * n [ 2 ] , 1 ]
            
            Contador2 = Contador2 + 1
            
        for Filas in range ( n [ 2 ] ) :
        
            W3 [ Filas , : ] = W [ Contador3 * n [ 3 ] : ( Contador3 + 1 ) * n [ 3 ] , 2 ]
            
            Contador3 = Contador3 + 1
            
        # Derivada del Error respecto a los Umbrales U de la Capa 2.
        
        for j in range ( n [ 1 ] ) :
            
            e1 = A [ j ,  1 ] * ( 1 - A [ j ,  1 ] )
            
            for p in range ( n [ 2 ] ) :
                
                e2 = W2 [ j , p ] * A [ p , 2 ] * ( 1 - A [ p , 2 ] )
                
                for i in range ( n [ 3 ] ) :
                    
                    e3 = W3 [ p , i ] * A [ i , 3 ] * ( 1 - A [ i , 3 ] ) * ( A [ i , 3 ] - S2 [ i , Entradas ] ) 
                    
            U [ j , 0 ] = U [ j , 0 ] - Alpha * ( e1 * e2 * e3 )
            
        # Derivada del Error respecto a los Umbrales U de la Capa 3.
        
        for j in range ( n [ 2 ] ) :
            
            e1 = A [ j , 2 ] * ( 1 - A [ j , 2 ] )
            
            for i in range ( n [ 3 ] ) :
                
                e2 = W3 [ j , i ] * A [ i , 3] * ( 1 - A [ i , 3] ) * ( A [ i , 3 ] - S2 [ i , Entradas ] )
                
            U [ j , 1 ] = U [ j , 1 ] - Alpha * ( e1 * e2 )
        
        # Derivada del Error respecto a los Umbrales U de la Capa 4.
        
        for i in range ( n [ 3 ] ) :
            
            e1 = A [ i , 3 ] * ( 1 - A [ i , 3 ] ) * ( A [ i , 3 ] - S2 [ i , Entradas ] )
            
            U [ i , 2 ] = U [ i , 2 ] - Alpha * ( e1 )
        
        # Derivada del Error respecto a los Pesos W de la Capa 1.
        
        for j in range ( n [ 0 ] ) :
            
            for k in range ( n [ 1 ] ) :
                
                e1 = A [ j , 0 ] * A [ k , 1 ] * ( 1 - A [ k , 1 ] )
                
                for p in range ( n [ 2 ] ) :
                    
                    e2 = W2 [ k , p ] * A [ p , 2 ] * ( 1 - A [ p , 2 ] )
                    
                    for i in range ( n [ 3 ] ) :
                        
                        e3 = W3 [ p , i ] * A [ i , 3 ] * ( 1 - A [ i , 3 ] ) * ( A [ i , 3 ] - S2 [ i , Entradas ] )
                        
                W1 [ j , k ] = W1 [ j , k ] - Alpha * ( e1 * e2 * e3 )
        
        # Derivada del Error respecto a los Pesos W de la Capa 2.
        
        for j in range ( n [ 1 ] ) :
            
            for k in range ( n [ 2 ] ) :
                
                e1 = A [ j , 1 ] * A [ k , 2 ] * ( 1 - A [ k , 2 ] ) 
                
                for i in range ( n [ 3 ] ) :
                    
                    e2 = W3 [ k , i ] * A [ i , 3 ] * ( 1 - A [ i , 3 ] ) * ( A [ i , 3 ] - S2 [ i , Entradas ] )
                    
                W2 [ j , k ] = W2 [ j , k ] - Alpha * ( e1 * e2 )
                
        # Derivada del Error respecto a los Pesos W de la Capa 3.
        
        for j in range ( n [ 2 ] ) :
            
            for i in range ( n [ 3 ] ) :
                
                e1 = A [ j , 2 ] * A [ i , 3 ] * ( 1 - A [ i , 3 ] ) * ( A [ i , 3 ] - S2 [ i , Entradas ] )
            
                W3 [ j , i ] = W3 [ j , i ] - Alpha * ( e1 )
        
        # Volvemos a distribuir los valores de los pesos W ij de las matrices W1 , 
        # W2 y W3 en una única matriz W.
        
        W = np.zeros ( [ nWMax , nx - 1 ] , float )
        
        Contador1 = 0
        
        Contador2 = 0
        
        Contador3 = 0
        
        for Filas in range ( n [ 0 ] ) :
            
            W [ Contador1 * n [ 1 ] : ( Contador1 + 1 ) * n [ 1 ] , 0 ] = W1 [ Filas , : ]
            
            Contador1 = Contador1 + 1
            
        for Filas in range ( n [ 1 ] ) :
            
            W [ Contador2 * n [ 2 ] : ( Contador2 + 1 ) * n [ 2 ] , 1 ] = W2 [ Filas , : ]
            
            Contador2 = Contador2 + 1
            
        for Filas in range ( n [ 2 ] ) :
            
            W [ Contador3 * n [ 3 ] : ( Contador3 + 1 ) * n [ 3 ] , 2 ] = W3 [ Filas , : ]
            
            Contador3 = Contador3 + 1
    
    ###############################################################################
        
    # Bloque 8
    
    ###############################################################################
         
        # INICIO ALGORITMO GENERAL - PARTE 2    
        
        # Calculamos el Error cometido en cada Iteración.
        
        Err = 0.0
        
        for i in range ( n [ nx - 1 ] ) :
            
            Err = Err + 0.5 * ( ( A [ i , nx - 1 ] - S2 [ i , Entradas ] ) ** 2 )
        
        Error.append ( Err )
        
        # Mostramos por pantalla el Error.
        
    print ( " Etapa: " , Etapas )
        
        #mp.plot ( Error , 'bo:' )
            
        #mp.show ( )
        
    ###############################################################################




















num = 150

X1 = []

for i in range ( num ):
    X1.append( rd.uniform ( -15 , 15 ) )

X1 = np.array ( X1 )
X1 = X1.reshape(-1,1)
X1 = np.transpose ( X1 )
X1.sort()

X2 = np.zeros ( [ n [ 0 ] , num ] , float )

for i in range ( n [ 0 ] ) :

    Xmin , Xmax = np.amin ( X1 [ i , : ] ) , np.amax ( X1 [ i , : ] )
    
    X2 [ i , : ] = ( X1 [ i , : ] - Xmin ) / ( Xmax - Xmin )


S2 = np.zeros ( [ n [ nx - 1 ] , num ] , float )

for Entradas in range ( num ) :

    # Calculamos los valores de activación de las neuronas en la matriz A
    # a partir de los datos de la Entrada y los Pesos : W ij , U i .
    
    for Columnas_A in range ( nx ) :
        
        if Columnas_A == 0 :
            
            for Filas_A in range ( n [ Columnas_A ] ) :
                
                A [ Filas_A , Columnas_A ] = X2 [ Filas_A , Entradas ]
                
        else :
            
            Contador = 0
            
            for Filas_A in range ( n [ Columnas_A ] ) :
                
                SumaWA = 0
                
                for Filas_A_A in range ( n [ Columnas_A - 1 ] ) :
                    
                     a = A [ Filas_A_A , Columnas_A - 1 ]
                     
                     b = W [ Contador + Filas_A_A * n [ Columnas_A ] , Columnas_A - 1 ]
                     
                     SumaWA = SumaWA + a * b
                     
                Contador = Contador + 1
                     
                A [ Filas_A , Columnas_A ] = f ( SumaWA + U [ Filas_A , Columnas_A - 1 ] )  
    
    S2 [ 0 , Entradas ] = A [ 0 , 3 ]
    
for i in range ( n [ nx - 1 ] ) :
    
    S2 [ i , : ] = S2 [ i , : ] * ( Smax - Smin ) + Smin

mp.plot ( X1 , S2 , 'ro:' )
