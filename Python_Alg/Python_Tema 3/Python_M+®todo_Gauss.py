import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algortimo implementa el método de Gauss para la resolución de sistemas
# de ecuaciones lineales

# 1 Definimos las matrices A,B y la matriz completa AB, también hallamos las 
#   dimensiones de dicha matriz

A = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)

B = np.array([[-4],[3],[9],[7]],float)

AB = np.c_[A,B]

nf,nc = AB.shape

# 2 Implementamos el algoritmo de eliminación gaussiana

for i in range(nf):
    
    AB[i,:] = AB[i,:]/AB[i,i]
    
    for j in range(i+1,nf):
        
        AB[j,:] = AB[j,:]-AB[j,i]*AB[i,:]
        
# 3 Una vez tenemos la matriz AB escalonada resolvemos por sustitución hacia
#   atrás

x = np.zeros(nf,float)

for i in range(nf-1,-1,-1):
    
    x[i] = AB[i,nc-1]

    for j in range(i+1,nf):
        
        x[i] = x[i]-AB[i,j]*x[j]

# 4 Mostramos las soluciones del sistema
        
print("Las soluciones del sistema :" ,x)
