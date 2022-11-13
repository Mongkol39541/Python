# Play Tennis Dataset Generator
# 31/10/2022
# Copyright (C) 2022

import numpy as np

def load(return_attr_names=False, split_train_test=None):
    X = [['Sunny', 'Hot', 'Hight', 'Weak'],
    ['Sunny', 'Hot', 'Hight', 'Strong'],
    ['Overcast', 'Hot', 'Hight', 'Weak'],
    ['Rain', 'Mild', 'Hight', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Strong'],
    ['Overcast', 'Cool', 'Normal', 'Strong'],
    ['Sunny', 'Mild', 'Hight', 'Weak'],
    ['Sunny', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'Normal', 'Weak'],
    ['Sunny', 'Mild', 'Normal', 'Strong'],
    ['Overcast', 'Mild', 'Hight', 'Strong'],
    ['Overcast', 'Hot', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'Hight', 'Strong']]
    F = ['Outlook', 'Temp', 'Humidity', 'Wind']
    T = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    X = np.array(X)
    T = np.array(T)
    F = np.array(F)
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