import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

dataset = make_blobs(n_samples = 200, n_features = 2, centers = 4, cluster_std = 1.6, random_state = 50)

points = dataset[0]

plt.figure()
plt.scatter(points[:,0],points[:,1])

plt.figure()
dendrogram = sch.dendrogram(sch.linkage(points, method = 'ward'))

hc = AgglomerativeClustering(n_clusters = 4, affinity = 'euclidean', linkage = 'ward')

y_hc = hc.fit_predict(points)

plt.figure()
plt.scatter(points[y_hc == 0,0], points[y_hc == 0,1],s = 100, c = 'cyan')
plt.scatter(points[y_hc == 1,0], points[y_hc == 1,1],s = 100, c = 'salmon')
plt.scatter(points[y_hc == 2,0], points[y_hc == 2,1],s = 100, c = 'yellow')
plt.scatter(points[y_hc == 3,0], points[y_hc == 3,1],s = 100, c = 'green')
