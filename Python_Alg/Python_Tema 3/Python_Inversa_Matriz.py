import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa un método para hallar la inversa de una matriz M
# resolviendo un sistema de ecuaciones lineales

def LUP(A,B):
    
    AB = np.c_[A,B]

    nf,nc = AB.shape
    
    I = np.eye(nf)
    
    # 1 Hallamos la fila que tiene mayor pivote (iterando sobre las columnas)
    
    for i in range(nf):
        
        fila_pivote_mayor = i
        
        pivote = abs(AB[i,i])
        
        for j in range(i+1,nf):
            
            if AB[j,i]>pivote:
                
                fila_pivote_mayor = j
                
                pivote = abs(AB[j,i])
    
    # 2 Intercambiamos las filas y hallamos las dimensiones de la matriz A final
              
        v1 = np.copy(AB[i,:])
        
        v2 = np.copy(AB[fila_pivote_mayor,:])
        
        AB[i,:] = v2
        
        AB[fila_pivote_mayor,:] = v1
        
    A = AB[:,0:nc-1]
    
    B = AB[:,nc-1]
    
    nf,nc = A.shape
    
    # 3 Implementamos el algoritmo de eliminación gaussiana sobre A e I y así 
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
    L = np.round(L,3)
    
    U = A
    U = np.round(U,3)
    
    # 4 Mostramos las matrices L (triangular inferior) y U (triangular superior)
    
    print("L=")
    
    print(L)
    
    print("U=")
    
    print(U)
    
    # 5 Hacemos sustitución hacia delante con la matriz L y B para obtener y
    
    LB = np.c_[L,B]
    
    Y = np.zeros(nf,float)
    
    for i in range(nf):
        
        Y[i] = LB[i,nc]
        
        for j in range(i):
            
            Y[i] = Y[i]-LB[i,j]*Y[j]
        
        Y[i] = Y[i]/LB[i,i]
    
    # 6 Hacemos sustitución hacia atrás con la matriz U e Y para obtener x
    
    UY = np.c_[U,Y]
     
    x = np.zeros(nf,float)
    
    for i in range(nf-1,-1,-1):
        
        x[i] = UY[i,nc]
    
        for j in range(i+1,nf):
            
            x[i] = x[i]-UY[i,j]*x[j]
    
    # 7 Mostramos las soluciones del sistema
    
    x = np.round(x,2)
    
    return x

# 8 Definimos la matriz M de la que queremos obtener la inversa, la matriz N
#   identidad para plantear el sistema de ecuaciones lineales y la matriz
#   inversa X

M = np.array([[0,1,1],[1,0,0],[0,0,1]])

nf,nc = M.shape

N = np.eye(nf)

X = np.zeros([nf,nf],float)

for i in range(nf):
    
    x = LUP(M,N[:,i])
    
    X[:,i] = x

print("La inversa de la matriz M es :")

print(X)

