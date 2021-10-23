import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algortimo implementa el método de Jacobi para resolver sistemas de
# ecuaciones lineales

# 1 Definimos las matrices A,B, el número de iteraciones deseadas y el vector
# con las estimaciones iniciales de las soluciones del sistema

A = np.array([[5,0,-2],[3,5,1],[0,-3,4]],float)

B = np.array([7,2,-4])

nf,nc = A.shape

N = 25

x = np.zeros(nf,float)

# 2 Definimos las matrices D y G (G = L+U) del método de Jacobi

D = np.diag(A)

D = np.diagflat(D)

D_Inv = np.linalg.inv(D)

LU = A-D

# 3 Implementamos el método de Jacobi

for i in range(N):
    
    Dx = B-np.dot(LU,x)

    x = np.dot(D_Inv,Dx)
 
# 4 Mostramos la solución aproximada del sistema
    
x = np.round(x,2)

print("La solución aproximada del sistema es:")

print(x)

