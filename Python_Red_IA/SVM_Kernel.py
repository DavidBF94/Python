import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()

from sklearn.datasets.samples_generator import make_blobs
from sklearn.svm import SVC
from sklearn.datasets.samples_generator import make_circles
from mpl_toolkits import mplot3d

###############################################################################

X,y = make_circles(200, factor = .1, noise = .1)
plt.figure()
plt.scatter( X[y == 0 ,0], X[y == 0, 1], c = 'skyblue' , s = 50, cmap='autumn')
plt.scatter( X[y == 1 ,0], X[y == 1, 1], c = 'salmon' , s = 50, cmap='autumn')

r = np.exp( -(X**2).sum(1))

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
    
def plot_3D(elev = 30, azim = 30, X=X, y=y):
    ax = plt.subplot(projection = '3d')
    ax.scatter3D(X[:,0],X[:,1],r,c = y, s = 50, cmap = 'autumn')
    ax.view_init(elev = elev, azim = azim)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')

plt.figure()
plot_3D()

clf = SVC(kernel = 'rbf', C = 1E6)
clf.fit(X,y)

plt.figure()
plt.scatter( X[y == 0 ,0], X[y == 0, 1], c = 'skyblue' , s = 50, cmap='autumn')
plt.scatter( X[y == 1 ,0], X[y == 1, 1], c = 'salmon' , s = 50, cmap='autumn')
plot_svc_decision_function(clf)
plt.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],s = 300, lw = 1, facecolors = 'none');
