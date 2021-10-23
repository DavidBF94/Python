import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algortimo implementa la factorización LU con  pivoting parcial para 
# sistemas de ecuaciones lineales


# 1 Definimos las matrices A,B y la identidad I,también hallamos las  
#    dimensiones de la matriz A

A = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)

B = np.array([[-4],[3],[9],[7]],float)

AB = np.c_[A,B]

nf,nc = AB.shape

I = np.eye(nf)

# 2 Hallamos la fila que tiene mayor pivote (iterando sobre las columnas)

for i in range(nf):
    
    fila_pivote_mayor = i
    
    pivote = abs(AB[i,i])
    
    for j in range(i+1,nf):
        
        if AB[j,i]>pivote:
            
            fila_pivote_mayor = j
            
            pivote = abs(AB[j,i])

# 3 Intercambiamos las filas y hallamos las dimensiones de la matriz A final
          
    v1 = np.copy(AB[i,:])
    
    v2 = np.copy(AB[fila_pivote_mayor,:])
    
    AB[i,:] = v2
    
    AB[fila_pivote_mayor,:] = v1
    
A = AB[:,0:nc-1]

B = AB[:,nc-1]

nf,nc = A.shape

# 4 Implementamos el algoritmo de eliminación gaussiana sobre A e I y así 
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

# 5 Mostramos las matrices L (triangular inferior) y U (triangular superior)

print("L=")

print(L)

print("U=")

print(U)

# 6 Hacemos sustitución hacia delante con la matriz L y B para obtener y

LB = np.c_[L,B]

Y = np.zeros(nf,float)

for i in range(nf):
    
    Y[i] = LB[i,nc]
    
    for j in range(i):
        
        Y[i] = Y[i]-LB[i,j]*Y[j]
    
    Y[i] = Y[i]/LB[i,i]

# 7 Hacemos sustitución hacia atrás con la matriz U e Y para obtener x

UY = np.c_[U,Y]
 
x = np.zeros(nf,float)

for i in range(nf-1,-1,-1):
    
    x[i] = UY[i,nc]

    for j in range(i+1,nf):
        
        x[i] = x[i]-UY[i,j]*x[j]

# 8 Mostramos las soluciones del sistema

x = np.round(x,2)
      
print("Las soluciones del sistema :" ,x)