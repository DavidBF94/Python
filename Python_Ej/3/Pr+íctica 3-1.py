from matplotlib.pyplot import plot,show
from numpy import array,arange
Sigma=10
s=28
b=8/3
def f(r,t):
    x=r[0]
    y=r[1]
    z=r[2]
    fx=Sigma*(y-x)
    fy=s*x-y-x*z
    fz=x*y-b*z
    return array([fx,fy,fz],float)

t0=0
tf=50
N=10000
h=(tf-t0)/N

t=arange(t0,tf,h)
x=[]
y=[]
z=[]

r=array([0,1,0],float)
for i in t:
    x.append(r[0])
    y.append(r[1])
    z.append(r[2])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r=r+(k1+2*k2+2*k3+k4)/6
plot(t,x)
plot(t,y)
plot(t,z)
show()
plot(x,z)
show()
    
    
