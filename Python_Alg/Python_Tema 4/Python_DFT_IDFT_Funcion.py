import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algortimo implementa la Transformada de Fourier Discreta (DFT) y la 
# Transformada de Fourier Discreta Inversa (IDFT) sobre un conjunto de valores
# discretos de una determinada función

# 1 Definimos la función sobre la que haremos el análisis de Fourier y la 
#   evaluamos

n = 1000

L = 10

x = np.linspace(0,L,n)

f = np.sin(2*mt.pi*50*x/L)+np.sin(2*mt.pi*100*x/L)+np.sin(2*mt.pi*150*x/L)

mp.plot(x,f)

mp.show()

N = len(f)

# 2 Definimos la función DFT que hallará la DFT del conjunto de datos f

def DFT(f):
    
    c = np.zeros(N,complex)
    
    for k in range(N):
        
        for n in range(N):
            
            c[k] = c[k]+f[n]*cmt.exp(-2j*cmt.pi*k*n/N)
            
    return c

# 3 Definimos la función IDFT que hallará la IDFT del conjunto de datos c 
#   (fijamos un límite para "limpiar" la señal en la IDFT)

def IDFT(c):
    
    Lim = 50
    
    c[Lim+1:N] = 0
    
    f = np.zeros(N,complex)
    
    for n in range(N):
        
        for k in range(Lim+1):
            
            f[n] = f[n]+(1/N)*c[k]*cmt.exp(2j*cmt.pi*k*n/N)
    
    return f

# 4 Hallamos los coeficientes de Fourier (c) para después hallar los valores
#   de la función habiendo eliminado algunas frecuencias (f) y representamos
#   ambos
   
c = abs(DFT(f))

mp.plot(c)
mp.show()

f = IDFT(DFT(f))

mp.plot(f.real)
mp.show()
