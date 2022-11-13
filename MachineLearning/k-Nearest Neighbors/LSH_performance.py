# LSH Performance
# 30/10/2022
# Copyright (C) 2022

from LSH import LSH
import numpy as np
from kNN import kNN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

def genData(dim=100000, nperClass=50, nClass=3):
    Xtrain = []
    Xtest = []
    Ytrain = []
    Ytest = []
    for i in range(nClass):
        mu = (i+1) * np.random.rand(dim)
        Xtrain.append(np.random.rand(nperClass, dim) + mu)
        Xtest.append(np.random.rand(nperClass, dim) + mu)
        Ytrain.append(i * np.ones(nperClass, dtype=np.int))
        Ytest.append(i * np.ones(nperClass, dtype=np.int))
    return np.vstack(Xtrain), np.vstack(Xtest), np.hstack(Ytrain), np.hstack(Ytest)

if __name__ == '__main__':
    nClass = 3
    nperClass = 50
    DIM = range(1, 4002, 1000)
    k = 1
    repeat = 50
    tLSH = np.zeros((len(DIM), repeat))
    rateLSH = np.zeros((len(DIM), repeat))
    tkNN = np.zeros((len(DIM), repeat))
    ratekNN = np.zeros((len(DIM), repeat))
    for i, dim in enumerate(DIM):
        Xtrain, Xtest, Ytrain, Ytest = genData(dim, nperClass, nClass)
        for I in range(repeat):
            # LSH
            t1 = time.time()
            YtestLSH = LSH(Xtrain, Ytrain, Xtest, k)
            tLSH[i, I] = time.time() - t1
            rateLSH[i, I] = np.sum(Ytest == YtestLSH) / len(Ytest) * 100
            print('{0:d}: LSH = {1:.02f} s {2:.02f} %'.format(dim, tLSH[i, I], rateLSH[i, I]), end='\t')

            # kNN
            t1 = time.time()
            YtestkNN = kNN(Xtrain, Ytrain, Xtest, k)
            tkNN[i, I] = time.time() - t1
            ratekNN[i, I] = np.sum(Ytest == YtestkNN) / len(Ytest) * 100
            print('kNN = {0:.02f} s {1:.02f} %'.format(tkNN[i, I], ratekNN[i, I]))
        
    plt.plot(DIM, np.mean(rateLSH, axis=1), 'b')
    plt.plot(DIM, np.mean(ratekNN, axis=1), '--r')
    plt.xlabel('Dimension')
    plt.ylabel('Accuracy (%)')
    plt.legend(['LSH', 'kNN'])
    plt.show()

    plt.plot(DIM, np.mean(tLSH, axis=1), 'b')
    plt.plot(DIM, np.mean(tkNN, axis=1), '--r')
    plt.xlabel('Dimension')
    plt.ylabel('Processing time (s)')
    plt.legend(['LSH', 'kNN'])
    plt.show()