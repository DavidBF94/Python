import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de R-K de orden 4 con paso adaptado

# 1 Definimos las funciones f(x,t) (dx/dt = f(x,t)) y R_K que introduce el 
#   método de R-K de cuarto orden para unos valores dados x,t y h

def f(x,t):
    
    f = -x**3+mt.sin(t)
    
    return f

def R_K(x,t,h):
    
    k1 = h*f(x,t)
    
    k2 = h*f(x+(1/2)*k1,t+(1/2)*h)
    
    k3 = h*f(x+(1/2)*k2,t+(1/2)*h)
    
    k4 = h*f(x+k3,t+h)
    
    x = x+(1/6)*(k1+2*k2+2*k3+k4)
    
    return x

# 2 Definimos los el intervalo de integración y el paso h inicial

a = 0

b = 10

N = 100

h = (b-a)/N

# 3 Definimos la precisión por paso y las listas en las que almacenaremos los
#   valores de x y de t (en Suma_t vamos anotando la posición temporal en la
#   que nos encontramos dado que h va variando)

Delta = 1e-10

t = []

x = []

x0 = 0

t0 = a

Suma_t = t0

x.append(x0)

t.append(t0)

# 4 Introducimos el método del paso adaptado para el método R-K de orden 4

while Suma_t <= b:
    
    x1 = R_K(x0,t0,h)
    
    x1 = R_K(x1,t0+h,h)
    
    x2 = R_K(x0,t0,2*h)
    
    Rho = 30*h*Delta/abs(x2-x1)
    
    if Rho > 1:
        
        h = h*(Rho**(1/4))
    
    while Rho < 1:
        
        h = h*(Rho**(1/4))
        
        x1 = R_K(x0,t0,h)
    
        x1 = R_K(x1,t0+h,h)
    
        x2 = R_K(x0,t0,2*h)
        
        Rho = 30*h*Delta/abs(x2-x1)
    
    x.append(x1)
    
    Suma_t = Suma_t+h
        
    t.append(Suma_t)
    
    x0 = x1
    
    t0 = Suma_t

# 5 Representamos la solución

mp.plot(t,x)

mp.show()

