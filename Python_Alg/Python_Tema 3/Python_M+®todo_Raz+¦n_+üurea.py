import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de la razón áurea para hallar los mínimos
# de una función dada

# 1 Definimos la función problema

def f(x):
    return 3*x**4-2*x**5+x

# 2 Definimos la razón áurea, la precisión deseada, un valor inicial para el
#   error y el número de iteraciones

z = 1.618033988749894

Precision = 1e-8

Error = 1234

Iteraciones = 1

# 3 Fijamos unos valores iniciales x1 y x4 entre los que pensamos que se 
#   encuentra el mínimo, y a partir de ellos y de z obtenemos x2 y x3

x1 = -1

x4 = 1

x3 = (abs(x1-x4)+x1*z)/z

x2 = (abs(x1-x3)+x1*z)/z

x1x4 = [f(x1),f(x4)]

x2x3 = [f(x2),f(x3)]

# 4 Implementamos el algoritmo de la razón áurea comprobando al principio que
#   los valores iniciales x1 y x4 son adecuados 

if min(x2x3) > min(x1x4):
    
    print("Los límites escogidos no son adecuados")
    
else :
    
    while Error > Precision:
        
        if f(x2)<f(x3):
            
            x4 = x3
            
            x3 = x2
            
            x2 = (abs(x1-x3)+x1*z)/z
        
        else:
            
            x1 = x2
            
            x2 = x3 
            
            x3 = (abs(x1-x4)+x1*z)/z
        
        Error = abs(x4-x1)
        
        Iteraciones = Iteraciones+1

Minimo = (1/2)*(x2+x3)

# 5 Mostramos el valor aproximado para el mínimo de la función, su error y el 
#   número de iteraciones necesarias para alcanzar la precisión deseada
 
print("El valor mínimo se encuentra en x =",Minimo)

print("El error es:",Error)

print("El número de iteraciones ha sido:",Iteraciones)
