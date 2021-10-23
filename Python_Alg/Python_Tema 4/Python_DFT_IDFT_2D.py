import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import Axes3D  

# El presente algoritmo realiza una Transformada de Fourier Discreta (DFT) y
# una Transformada de Fourier Discreta Inversa (IDFT) 2-Dimensional sobre una
# determinada función o en su defecto sobre un conjunto de datos 2-D 
# Array 2-D

# 1 Definimos el intervalo sobre el que representaremos nuestra función y el 
#   número total de puntos de la malla en los ejes x (M) e y (N)
#   Después definimos nuestra función y la representamos

L = 10

M = 100

N = 100
 
x = np.linspace(0,L,M)

y = np.linspace(0,L,N)

X,Y = np.meshgrid(x,y)

def f(x,y):
    
    f1 = 3*np.sin(2*mt.pi*5*x/L+2*mt.pi*10*y/L)
    
    f2 = 2*np.sin(2*mt.pi*15*x/L+2*mt.pi*20*y/L)
    
    f3 = 1*np.cos(2*mt.pi*25*x/L+2*mt.pi*30*y/L)
    
    f = f1+f2+f3
    
    return f

Z = f(X,Y)

fig = mp.figure()

ax = mp.axes(projection='3d')

ax.plot_surface( X , Y , Z )

# 2 Realizamos la DFT 2-D sobre nuestros datos Z y representamos en el espacio 
#   de frecuencias

c = np.zeros([M,N],complex)

for k in range(M):
    
    for l in range(N):
        
        for m in range(M):
            
            for n in range(N):
                
                c[k,l] = c[k,l] + Z[m,n]*cmt.exp(-2j*cmt.pi*(k*m/M + l*n/N))

k = np.linspace(0,M,M)

l = np.linspace(0,N,N)

K,L = np.meshgrid(k,l)

fig = mp.figure()

ax = mp.axes(projection='3d')

ax.plot_surface( K , L , abs(c))

# 3 Realizamos la IDFT sobre nuestros datos c escogiendo límites máximos para
#   las frecuencias k y l y representamos

Z = np.zeros([M,N],complex)
                
Lim_k = 10

Lim_l = 10

for m in range(M):
            
    for n in range(N):
        
        for k in range(Lim_k+1):
    
            for l in range(Lim_l+1):
                
                Z[m,n] = Z[m,n] + (1/(M*N))*c[k,l]*cmt.exp(2j*cmt.pi*(k*m/M + l*n/N))

fig = mp.figure()

ax = mp.axes(projection='3d')

ax.plot_surface( X , Y , Z.real )                
                