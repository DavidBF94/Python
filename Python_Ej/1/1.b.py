from numpy import linspace
from matplotlib.pyplot import plot,show,xlabel,ylabel
for r in linspace(1,4,3000):
    x0=(1/2)
    x=r*x0*(1-x0)
    for i in range(1,1001):
        x=r*x*(1-x)
    xx=[]
    rr=[]
    for j in range(1,1001):
        x=r*x*(1-x)
        xx.append(x)
        rr.append(r)
    plot(rr,xx,'ko')
xlabel("Eje r")
ylabel("Eje x")
show()