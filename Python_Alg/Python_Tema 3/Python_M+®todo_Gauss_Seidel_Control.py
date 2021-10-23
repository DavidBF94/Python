import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algortimo implementa el método de Gauss-Seidel para resolver sistemas de
# ecuaciones lineales

# 1 Definimos las matrices A,B, el vector con las estimaciones iniciales de las
#   soluciones del sistema y la precisión deseada

A = np.array([[5,0,-2],[3,5,1],[0,-3,4]],float)

B = np.array([7,2,-4])

nf,nc = A.shape

N = 1

x = np.zeros(nf,float)

Precision = 1e-10

# 2 Definimos las matrices DL (D+L) y U del método de Gauss-Seidel

DL = np.tril(A)

DL_Inv = np.linalg.inv(DL)

U = A-DL

# 3 Implementamos el método de Gauss-Seidel controlado

Error = 1234

while Error > Precision:

    for i in range(N):
        
        x = B-np.dot(U,x)
        
        x = np.dot(DL_Inv,x)
    
    N = N+1
    
    Error = max(abs(np.dot(A,x)-B))
 
# 4 Mostramos la solución aproximada del sistema junto con las iteraciones y el
#   error
    
x = np.round(x,2)

print("La solución aproximada del sistema es:")

print(x)

print("El número de iteraciones necesarias ha sido:",N)

print("El error es:",Error)
