from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

x,y = make_classification( n_samples = 100, n_features = 1, n_classes = 2, n_clusters_per_class = 1, flip_y = 0.03, n_informative = 1, n_redundant = 0, n_repeated = 0)

plt.figure()
plt.scatter(x, y, c = y)

model = LinearRegression()
model.fit(x,y)

b0 = model.intercept_
b1 = model.coef_

xmin = min(x)
xmax = max(x)

plt.figure()
xx = np.linspace(xmin, xmax, 1000)
yy = ( b0 + b1[0]*xx)
plt.scatter(x, y, c = y)
plt.plot(xx,yy)

#Nuevo

X,Y = make_classification( n_samples = 100, n_features = 1, n_classes = 2, n_clusters_per_class = 1, flip_y = 0.03, n_informative = 1, n_redundant = 0, n_repeated = 0)

X = ( b0 + b1[0]*X)

Sigmoide = 1/(1+np.exp(-X))

Y = []

for i in range(0,len(Sigmoide)):
    if ( Sigmoide[i]<0.5 ):
        Y.append(0)
    elif (Sigmoide[i]>=0.5):
        Y.append(1)

plt.figure()      
plt.scatter(X, Y, c = Y)














