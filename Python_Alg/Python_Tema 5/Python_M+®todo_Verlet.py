import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de Verlet para resolver ecuaciones 
# diferenciales de segundo orden de la forma (dx^2/dt^2 = f(x,t))

# 1 Definimos la función f(x,t)

G = 6.6738e-11

M = 1.9891e30

m = 5.9722e24

def mag(r):
    
    return mt.sqrt(sum(r*r))

def f(r):
    
    return -G*M*r/mag(r)**3

# 2 Fijamos la anchura y el límite del intervalo de integración junto con los
#   vectores donde iremos guardando los resultados de las iteraciones y las
#   condiciones iniciales

x0 = 1.5210e11

y0 = 0.0

vx0 = 0.0

vy0 = 2.9291e4

a = 0.0

b = 50e6

h = 3600.0

r = np.array([x0,y0],float)

v = np.array([vx0,vy0],float)

tpoints = np.arange(a,b,h)

xpoints = []

ypoints = []

# 3 Introducimos el algoritmo de Verlet

vmitad = v + 0.5 * h * f(r)

for t in tpoints:
    
    xpoints.append(r[0])
    
    ypoints.append(r[1])
    
    r = r + h * vmitad
    
    k = h * f(r)
    
    v = vmitad + 0.5 * k
    
    vmitad = vmitad + k

# 4 Mostramos las soluciones por pantalla
 
mp.plot(tpoints,xpoints)

mp.show()

mp.plot(tpoints,ypoints)

mp.show()

mp.plot(xpoints,ypoints)

mp.show()









