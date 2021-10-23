import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algortimo implementa el método de la bisección para la resolución de 
# ecuaciones no lineales

# 1 Definimos la función problema (f(x)=0)

def f(x):
    return mt.exp(x)-2

# 2 Fijamos los intervalos iniciales entre los que pensamos que puede estar
#   la solución, también fijamos la precisión deseada,un valor que inicialice
#   el error y el número de iteraciones hasta alcanzar la solución con la
#   precisión deseada

x1 = 0

x2 = 1

Precision = 1e-10

Error = 1234

Iteraciones = 1

# 3 Implementamos el algortimo del método de la bisección teniendo en cuenta
#   que los valores de la función evaludada en los límites del intervalo debe
#   tener signos diferentes

if np.sign(f(x1))==np.sign(f(x2)):
    
    print("Los valores límite evaluados en la función tienen mismo signo")
    
else :
    
    while Error > Precision:
    
        xm = (1/2)*(x2+x1)
        
        if np.sign(f(xm))==np.sign(f(x1)):
            
            x1 = xm
        
        else:
            
            x2 = xm
        
        Error = abs(x2-x1)
        
        Iteraciones = Iteraciones+1

# 5 Mostramos la solución aproximada de la ecuación junto con el error y el
#   número de iteraciones necesarias para hallar la solución
   
print("La solución de la ecuación es:",xm)
print("El error es:",Error)
print("El número de iteraciones necesarias ha sido :",Iteraciones)
    