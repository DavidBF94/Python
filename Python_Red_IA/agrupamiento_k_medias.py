from pandas import DataFrame
import random 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

n = 200

x = []
y = []

for i in range ( n ):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    
Data = { 'x' : x , 'y': y}

df = DataFrame ( Data,columns=['x','y'])

plt.figure()
plt.scatter(x,y,c = 'black')

#

kmeans = KMeans(n_clusters = 3).fit(df)
centroids = kmeans.cluster_centers_

plt.figure()
plt.scatter(df['x'],df['y'],c = kmeans.labels_.astype(float), s = 50 , alpha = 0.5)
plt.scatter(centroids[:,0],centroids[:,1], c = 'red', s = 50)
