import numpy as np
import math as mt
import cmath as cmt
import matplotlib.pyplot as mp

# Éste algoritmo implementa el método de R-K-Fehlberg con paso adaptado

# 1 Definimos las funciones f(x,t) (dx/dt = f(x,t)) y R_K_F que introduce el 
#   método de R-K-Fehlberg para unos valores dados x,t y h

def f(x,t):
    
    f = -x**3+mt.sin(t)
    
    return f

def R_K_F(x,t,h):
    
    k1 = h*f(x,t)
    
    k2 = h*f(x+(1/4)*k1,t+(1/4)*h)
    
    k3 = h*f(x+(3/32)*k1+(9/32)*k2,t+(3/8)*h)
    
    k4 = h*f(x+(1932/2197)*k1-(7200/2197)*k2+(7296/2197)*k3,t+(12/13)*h)
    
    k5 = h*f(x+(439/216)*k1-8*k2+(3680/513)*k3-(845/4104)*k4,t+h)
    
    k6 = h*f(x-(8/27)*k1+2*k2-(3544/2565)*k3+(1859/4104)*k4-(11/40)*k5,t+(1/2)*h)
    
    x = x+(16/135)*k1+(6656/12825)*k3+(28561/56430)*k4-(9/50)*k5+(2/55)*k6
    
    E = (1/360)*k1-(128/4275)*k3-(2197/75240)*k4+(9/50)*k5+(2/55)*k6
    
    return x,abs(E)

# 2 Definimos los el intervalo de integración y el paso h inicial

a = 0

b = 10

N = 1000

h = (b-a)/N

# 3 Definimos la precisión por paso y las listas en las que almacenaremos los
#   valores de x y de t (en Suma_t vamos anotando la posición temporal en la
#   que nos encontramos dado que h va variando)

Delta = 1e-2

t = []

x = []

x0 = 0

t0 = a

Suma_t = t0

x.append(x0)

t.append(t0)

# 4 Introducimos el método del paso adaptado para el método R-K_F

while Suma_t <= b:
    
    xt,E = R_K_F(x0,t0,h)
    
    if E < Delta:
        
        s = (Delta/(2*E))**(1/4)
        
        h = s*h
    
    while E > Delta:
        
        s = (Delta/(2*E))**(1/4)
        
        h = s*h
        
        xt,E = R_K_F(x0,t0,h)
    
    x.append(xt)
    
    Suma_t = Suma_t+h
        
    t.append(Suma_t)
    
    x0 = xt
    
    t0 = Suma_t

# 5 Representamos la solución

mp.plot(t,x)

mp.show()

