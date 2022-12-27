# K-d tree Performance
# 28/10/2022
# Copyright (C) 2022

import numpy as np
from kdtree import kdtree
import time
from kNN_kdtree import kNN_kdtree
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

MAX = 100
t = np.zeros((MAX, MAX))
for D in range(1, MAX + 1):
    print('dimension = ', D)
    for N in range(1, MAX + 1):
        X = np.random.rand(N, D)
        Y = np.arange(1, N + 1)
        t1 = time.time()
        repeat = 100
        for i in range(repeat):
            node = kdtree(X, Y)
            Ztest = kNN_kdtree(node, X[0, :].reshape((1, D)), 1)
        t[D - 1, N - 1] = (time.time() - t1) / repeat

# 3D plot
x = np.arange(len(t))
y = np.arange(len(t))
x, y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, t, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
ax.set_xlabel('Dimension')
ax.set_ylabel('#Samples')
ax.set_zlabel('Computation time (s)')
plt.show()