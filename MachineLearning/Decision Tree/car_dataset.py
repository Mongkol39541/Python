# Car dataset loader
# 01/11/2022
# Copyright (C) 2022

from genericpath import isfile
import pandas as pd
import os
import numpy as np

def load(path='car.csv', return_attr_names=False, split_train_test=None):
    if os.path.isfile(path):
        car = pd.read_csv(path)
    else:
        url = 'https://archive.ics.uci.edu/ml/machine-' \
            'learning-databases/car/car.data'
        car = pd.read_csv(url, header=None)
        car.to_csv(path, index=False)
    
    attr_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']

    X = car.iloc[:, :6].values
    T = car.iloc[:, -1].values
    F = np.array(attr_names)
    if split_train_test:
        classes = np.unique(T)
        itrain = np.empty((0, ), dtype=np.int)
        itest = np.empty((0, ), dtype=np.int)
        for i in classes:
            idx = np.where(T == i)[0]
            split = int(len(idx) * split_train_test)
            itrain = np.concatenate((itrain, idx[:split]))
            itest = np.concatenate((itest, idx[split:]))
        return X[itrain], T[itrain], X[itest], T[itest]

    if return_attr_names:
        return X, T, F
    return X, T

# Car dataset

from ID3 import ID3
import car_dataset
X, T, F = car_dataset.load(return_attr_names=True)
tree = ID3(X, T, F)
tree.show()