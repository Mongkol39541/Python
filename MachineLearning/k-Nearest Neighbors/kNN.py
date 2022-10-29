# k-Nearest Neighbor
# 27/10/2022
# Copyright (C) 2022

import numpy as np

def kNN(Xtrain, Ytrain, Xtest, k=1):
    Ytest = []
    for x in Xtest:
        d = np.sqrt(np.sum((Xtrain - x)**2, axis=1))
        idx = np.argsort(d)
        (values, counts) = np.unique(Ytrain[idx[:k]], return_counts=True)
        ind = np.argmax(counts)
        Ytest.append(values[ind])
    return Ytest