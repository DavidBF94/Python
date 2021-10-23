import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método QR para la obtención de los autovalores
# y autovectores de una matriz A

# 1 Definimos la matriz A, calculamos sus dimensiones, fijamos la precisión
#   deseada y definimos para inicializar el proceso unas matrices Q,R,U y V

A = np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]],float)

nf,nc = A.shape

Precision = 1e-10

Error = 1234

Q = np.empty([nf,nc],float)

R = np.empty([nf,nc],float)

U = np.empty([nf,nc],float)

V = np.eye(nf)

# 2 Definimos una función que nos calcule el módulo de un vector v

def Modulo(v):
    
    return mt.sqrt(np.dot(v,v))

# 3 Definimos la función QR en la que se implementa el algoritmo para calcular
#   las matrices Q y R

def QR(A):
    
    Q = np.empty([nf,nc],float)
    
    U = np.empty([nf,nc],float)
    
    R = np.zeros([nf,nc],float)
    
    U[:,0] = A[:,0]
        
    Q[:,0] = U[:,0]/Modulo(U[:,0])
    
    for i in range(1,nc):
        
        U[:,i] = A[:,i]
        
        for j in range(i):
            
            U[:,i] = U[:,i]-np.dot(Q[:,j],A[:,i])*Q[:,j]
        
        Q[:,i] = U[:,i]/Modulo(U[:,i])
        
    for i in range(nf):
            
        R[i,i] = Modulo(U[:,i])
        
        for j in range(i+1,nc):
            
            R[i,j] = np.dot(Q[:,i],A[:,j])

    return Q,R

# 4 Implementamos el algoritmo QR y establecemos las condiciones para que los
#   valores fuera de la diagonal de la matriz A sean menores o iguales que la
#   precisión deseada

while Error > Precision:
    
    Q,R = QR(A)
    
    V = np.dot(V,Q)
    
    A = np.dot(R,Q)
    
    A_Copia = np.copy(A)
    
    for i in range(nc):
        
        A_Copia[i,i] = 0
    
    Error = np.max(np.abs(A_Copia))
    
# 5 Mostramos los autovalores y autovectores aproximados de la matriz A en base
#   a la precisión fijada 
    
print("Los autovalores de la matriz A son:")
        
print(np.diag(A))   

print("Los autovectores de la matriz A son:")

print(np.around(V,3))
