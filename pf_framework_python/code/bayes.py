import matplotlib.pyplot as plt
import numpy as np
from math import pi, exp, sqrt
import matplotlib.cm as cm

N = 31
numsteps = 5

# set up grid
x = np.linspace(-10, 10, N)
v = np.linspace(-10, 10, N)
sp = (x[1] - x[0])/2
X, V = np.meshgrid(x, v)
# initial probability distribution is a delta function at origin
p0 = np.zeros(X.shape)
p0[N/2, N/2] = 1
plt.ion()
plt.imshow(p0, cmap = cm.Greys_r, interpolation='none')
plt.draw()
plt.show()
acc_var = 1 # Variance of random acceleration

for ii in range(0):
    print 'Step %d'%ii
    p1 = np.zeros(X.shape)
    for (i, j), p in np.ndenumerate(p0): #outer loop over configuration space
        for (k,l), x in np.ndenumerate(X):
            # new position is old position plus velocity
            if X[i,j] > X[k,l] + V[k,l] - sp and X[i,j] <= X[k,l] + V[k,l] + sp: 
                # Bayesian update with random acceleration
                p1[i,j] = p1[i,j] + exp(-0.5 * (V[i,j] - V[k,l])**2 / acc_var) / sqrt(2*pi*acc_var) * p0[k,l] 
    p0 = p1
    plt.imshow(p1, cmap = cm.Greys_r, interpolation='none')
    plt.draw()
    plt.show()