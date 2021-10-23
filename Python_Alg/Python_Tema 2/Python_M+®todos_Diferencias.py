import numpy as np
import math as mt
import matplotlib.pyplot as mp

# Éste algoritmo implementa métodos de diferencias para hallar numéricamente
# valores aproximados de derivadas

# 1 Definimos la función de 1 variable a derivar

def f(x):
    return x**3+x**2+x+1

# 2 Definimos el intervalo en el que deseamos realizar las derivadas y los 
#   puntos en los que deseamos evaluarlas para así podemos representar la 
#   función derivada
    
a = -2
b = 2

N = 1000

x = np.linspace(a,b,N)

# 3 Implementamos la diferencia hacia delante y la representamos

h = 1e-8

d1 = []

for i in x:
    df = (f(i+h)-f(i))/h
    d1.append(df)

mp.plot(x,d1)

mp.title("Primera derivada por diferencia hacia delante")

mp.show()

# 4 Implementamos la diferencia hacia atrás y la representamos

h = 1e-8

d2 = []

for i in x:
    df = (f(i)-f(i-h))/h
    d2.append(df)

mp.plot(x,d2)

mp.title("Primera derivada por diferencia hacia atrás")

mp.show()

# 5 Implementamos la diferencia centrada y la representamos

h = 1e-10

d3 = []

for i in x:
    df = (f(i+h/2)-f(i-h/2))/h
    d3.append(df)  

mp.plot(x,d3)

mp.title("Primera derivada por diferencia centrada")

mp.show()

# 6 Implementamos la diferencia centrada para obtener la segunda derivada y
#   representamos
    
h = 1e-8

d4 = []

for i in x:
    df = (f(i+h)-2*f(i)+f(i-h))/(h**2)
    d4.append(df)      

mp.plot(x,d4)

mp.title("Segunda derivada por diferencia centrada")

mp.show()

  