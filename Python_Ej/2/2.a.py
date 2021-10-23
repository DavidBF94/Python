from numpy import linspace
from matplotlib.pyplot import plot,show
def f(x):
    if x>=0 and x<(1/2):
        return 1
    elif x>=(1/2) and x<1:
        return -1
ff=[]
x=[]
for i in linspace(0,1,1000):
    ff.append(f(i))
    x.append(i)
plot(x,ff)
show()

    
    