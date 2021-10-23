import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algortimo implementa el método de SR para resolver sistemas de 
# ecuaciones lineales

# 1 Definimos las matrices A,B, el vector con las estimaciones iniciales de las
#   soluciones del sistema,la precisión deseada y el parámetro alfa

A = np.array([[5,0,-2],[3,5,1],[0,-3,4]],float)

B = np.array([7,2,-4])

nf,nc = A.shape

N = 1

x = np.zeros(nf,float)

Precision = 1e-10

alfa = 1

# 2 Definimos las matrices D L y U

D = np.diag(A)

D = np.diagflat(D)

L = np.tril(A,-1)

U = A-L-D

# 3 Implementamos el método SR controlado

Error = 1234

while Error > Precision:

    for i in range(N):
        
        x = alfa*B+np.dot(((1-alfa)*D-alfa*U),x)
        
        x = np.dot(np.linalg.inv(D+alfa*L),x)
    
    N = N+1
    
    Error = max(abs(np.dot(A,x)-B))
 
# 4 Mostramos la solución aproximada del sistema junto con las iteraciones y el
#   error
    
x = np.round(x,2)

print("La solución aproximada del sistema es:")

print(x)

print("El número de iteraciones necesarias ha sido:",N)

print("El error es:",Error)
