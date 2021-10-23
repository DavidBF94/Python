import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()

from sklearn.datasets.samples_generator import make_blobs
from sklearn.svm import SVC

###############################################################################

plt.figure()
X,y = make_blobs(n_samples = 120, centers = 2, random_state = 0, cluster_std = 0.70)
plt.scatter( X[y == 0 ,0], X[y == 0, 1], c = 'skyblue' , s = 50, cmap='autumn')
plt.scatter( X[y == 1 ,0], X[y == 1, 1], c = 'salmon' , s = 50, cmap='autumn')

###############################################################################

model = SVC ( kernel = 'linear', C=1E10)
model.fit (X,y)

def plot_svc_decision_function ( model, ax = None, plot_support = True ):
    
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y,X = np.meshgrid(y,x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    
    ax.contour(X,Y,P,colors = 'k', levels = [-1, 0, 1], alpha = 0.5, linestyles = ['--', '-', '--'])
    
    if plot_support:
        ax.scatter( model.support_vectors_[:, 0], model.support_vectors_[:, 1], s = 300, linewidth = 1, facecolors= 'none');
    
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

plt.figure()
plt.scatter( X[y == 0 ,0], X[y == 0, 1], c = 'skyblue' , s = 50, cmap='autumn')
plt.scatter( X[y == 1 ,0], X[y == 1, 1], c = 'salmon' , s = 50, cmap='autumn')
plot_svc_decision_function(model);
