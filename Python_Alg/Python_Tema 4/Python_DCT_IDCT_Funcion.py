import copy as cp
import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algortimo implementa la Transformada del Coseno Discreta (DCT) y la 
# Transformada del Coseno Discreta Inversa (DCTI) sobre un conjunto de valores
# discretos de una determinada función

# 1 Definimos la función sobre la que haremos el análisis de Fourier, la 
#   evaluamos y la simetrizamos

n = 1000

L = 10

x = np.linspace(0,L,n)

f = np.sin(2*mt.pi*50*x/L)+np.sin(2*mt.pi*100*x/L)+np.sin(2*mt.pi*150*x/L)

N = len(f)

f1 = cp.copy(f)

f2 = np.zeros(N,float)

for i in range(0,N):
    
    f2[i] = f1[N-1-i]

f = np.zeros(2*N,float)

f[0:N] = f1

f[N:2*N] = f2

N = len(f)

mp.plot(f)
mp.show()

# 2 Definimos la función DCT que hallará la DCT del conjunto de datos f

def DCT(f):
    
    c = np.zeros(N//2,complex)
    
    for k in range(N//2):
        
        c[k] = f[0]+f[N//2-1]*mt.cos(2*mt.pi*k*(N/2)/N)
        
        for n in range(1,N//2):
            
            c[k] = c[k]+2*f[n]*mt.cos(2*mt.pi*k*n/N)
            
    return c

# 3 Definimos la función IDCT que hallará la IDCT del conjunto de datos c 
#   (fijamos un límite para "limpiar" la señal en la IDCT)

def IDCT(c):
    
    Lim = 50
    
    c[Lim+1:N] = 0
    
    f = np.zeros(N//2,complex)
    
    for n in range(N//2):
        
        f[n] = (1/N)*(c[0]+c[N//2-1]*mt.cos(2*mt.pi*n*(N/2)/N))
        
        for k in range(1,Lim+1):
            
            f[n] = f[n]+(2/N)*c[k]*mt.cos(2*mt.pi*k*n/N)
    
    return f

# 4 Hallamos los coeficientes de Fourier (c) para después hallar los valores
#   de la función habiendo eliminado algunas frecuencias (f) y representamos
#   ambos
   
c = abs(DCT(f))

mp.plot(c)
mp.show()

f = IDCT(DCT(f))

mp.plot(f.real)
mp.show()

