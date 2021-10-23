import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math as mt

x1 = []
x2 = []
y = []
n = 100

for i in range(n):
    x1.append(rd.random())
    x2.append(rd.random())
    y.append(round(rd.random()))

x1_x2 = np.zeros([n,2],float)
x1_x2[:,0] = x1
x1_x2[:,1] = x2
y = np.array(y)

plt.figure()
plt.scatter(x1_x2[y==0,0],x1_x2[y==0,1],c='salmon')
plt.scatter(x1_x2[y==1,0],x1_x2[y==1,1],c='skyblue')

#Nuevos

X1 = []
X2 = []
Y = []
N = 100

for i in range(N):
    X1.append(rd.random())
    X2.append(rd.random())
    
X1_X2 = np.zeros([N,2],float)
X1_X2[:,0] = X1
X1_X2[:,1] = X2

plt.figure()
plt.scatter(X1_X2[:,0],X1_X2[:,1],c = 'black')

filas = []
for i in range(N):
    distanciaMenor = 2
    for j in range(n):
        distancia = mt.sqrt((X1_X2[i,0]-x1_x2[j,0])**2 + (X1_X2[i,1]-x1_x2[j,1])**2) 
        if distancia < distanciaMenor:
            distanciaMenor = distancia
            fila = j
    filas.append(fila)

for i in range(N):
    if y[filas[i]] == 0:
        Y.append(0)
    else:
        Y.append(1)
        
Y = np.array(Y)

plt.figure()
plt.scatter(x1_x2[y==0,0],x1_x2[y==0,1],c='salmon')
plt.scatter(x1_x2[y==1,0],x1_x2[y==1,1],c='skyblue')
plt.scatter(X1_X2[Y==0,0],X1_X2[Y==0,1],c='red')
plt.scatter(X1_X2[Y==1,0],X1_X2[Y==1,1],c='blue')
