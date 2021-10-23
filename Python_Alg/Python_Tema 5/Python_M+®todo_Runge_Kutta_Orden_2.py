import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de Runge-Kutta de orden 2 para resolver 
# EDOS de primer orden (dx/dt = f(x,t))

# 1 Definimos la función f(x,t)

def f(x,t):
    
    f = -x**3+mt.sin(t)
    
    return f

# 2 Definimos los intervalos de integración t1 y t2 junto con todos los puntos
#   en los que dividiremos el intervalo

t1 = 0

t2 = 10

N = 100

h = (t2-t1)/N

# 3 Definimos los vectores para t y x e implementamos el método de R-K orden 2

t = np.linspace(t1,t2,N)

x = np.zeros(N,float)

x[0] = 0

for i in range(1,N):
    
    k1 = h*f(x[i-1],t[i-1])
    
    k2 = h*f(x[i-1]+(1/2)*k1,t[i-1]+(1/2)*h)
    
    x[i] = x[i-1]+k2
    
# 4 Mostramos en pantalla la gráfica con el resultado
    
mp.plot(t,x)

mp.show()

