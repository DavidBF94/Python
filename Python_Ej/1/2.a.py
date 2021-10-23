from matplotlib.pyplot import plot,show
from numpy import loadtxt
valores=loadtxt("millikan.txt")
x=valores[:,0]
y=valores[:,1]
plot(x,y,'bo')
show()