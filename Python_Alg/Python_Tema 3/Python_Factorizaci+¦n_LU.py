import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algortimo implementa la factorización LU para sistemas de ecuaciones
# lineales

# 1 Definimos las matrices A,B y la identidad I,también hallamos las  
#    dimensiones de la matriz A

A = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)

B = np.array([[-4],[3],[9],[7]],float)

nf,nc = A.shape

I = np.eye(nf)

# 2 Implementamos el algoritmo de eliminación gaussiana sobre A e I y así 
#   obtener L y U

for i in range(nf):
    
    AA =np.copy(A)
    
    A[i,:] = A[i,:]/A[i,i]
    
    I[i,:] = I[i,:]/AA[i,i]
    
    for j in range(i+1,nf):
        
        AA =np.copy(A)
        
        A[j,:] = A[j,:]-A[j,i]*A[i,:]
        
        I[j,:] = I[j,:]-AA[j,i]*I[i,:]
        
L = np.linalg.inv(I)
L = np.round(L,2)

U = A

# 3 Mostramos las matrices L (triangular inferior) y U (triangular superior)

print("L=")

print(L)

print("U=")

print(U)

# 4 Hacemos sustitución hacia delante con la matriz L y B para obtener y

LB = np.c_[L,B]

Y = np.zeros(nf,float)

for i in range(nf):
    
    Y[i] = LB[i,nc]
    
    for j in range(i):
        
        Y[i] = Y[i]-LB[i,j]*Y[j]
    
    Y[i] = Y[i]/LB[i,i]

# 5 Hacemos sustitución hacia atrás con la matriz U e Y para obtener x

UY = np.c_[U,Y]
 
x = np.zeros(nf,float)

for i in range(nf-1,-1,-1):
    
    x[i] = UY[i,nc]

    for j in range(i+1,nf):
        
        x[i] = x[i]-UY[i,j]*x[j]

# 6 Mostramos las soluciones del sistema
        
print("Las soluciones del sistema :" ,x)
    