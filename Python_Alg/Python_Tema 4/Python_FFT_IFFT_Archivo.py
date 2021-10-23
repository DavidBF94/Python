import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algortimo implementa la Transformada de Fourier Rápida (FFT) y la 
# Transformada de Fourier Rápida Inversa (IFFT) sobre un conjunto de valores
# discretos de una determinada señal obtenidos de un archivo externo

# 1 Importamos los datos del fichero en cuestión, los representamos y hallamos
#   la longitud del conjunto de datos

f = np.loadtxt("pitch.txt",float)

mp.plot(f)
mp.show()

N = len(f)

# 2 Definimos la función FFT que hallará la FFT del conjunto de datos f

def FFT(f):
    
    E = np.zeros(N,complex)
    
    O = np.zeros(N,complex)
    
    c = np.zeros(N,complex)
    
    for k in range(N):
        
        for n in range(N//2):
            
            E[k] = E[k]+f[2*n]*cmt.exp(-2j*cmt.pi*k*n/(N//2))
            
            O[k] = O[k]+f[2*n+1]*cmt.exp(-2j*cmt.pi*k*n/(N//2))
            
        O[k] = cmt.exp(-2j*cmt.pi*k/N)*O[k]
            
        c[k] = E[k] + O[k]
            
    return c

# 3 Definimos la función IFFT que hallará la IFFT del conjunto de datos c 
#   (fijamos un límite para "limpiar" la señal en la IFFT)

def IFFT(c):
    
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
   
c = abs(FFT(f))

mp.plot(c)
mp.show()

f = IFFT(FFT(f))

mp.plot(f.real)
mp.show()
