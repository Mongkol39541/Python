from matplotlib.pyplot import plot
from perceptron import perceptron, plot_hyperplane2d
import numpy as np
from matplotlib import pyplot as plt

# And problem
X = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
T = [1, -1, -1, -1]
X = np.array(X)
X = np.hstack((X, np.ones((len(X), 1))))
w = perceptron(X, T)
plot_hyperplane2d(X, T, w)
plt.show()