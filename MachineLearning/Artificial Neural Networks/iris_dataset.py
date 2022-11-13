import pandas as pd
import numpy as np

def load(path='iris.csv', split_train_test=None):
    iris = pd.read_csv(path)
    X = iris.iloc[:, :4].values
    Y = iris.iloc[:, -1].values
    if split_train_test:
        classes = np.unique(Y)
        itrain = np.empty((0,), dtype=np.int)
        itest = np.empty((0,), dtype=np.int)
        for i in classes:
            idx = np.where(Y == i)[0]
            split = int(len(idx) * split_train_test)
            itrain = np.concatenate((itrain, idx[:split]))
            itest = np.concatenate((itest, idx[split:]))
        return X[itrain], Y[itrain], X[itest], Y[itest]
    return X, Y

if __name__=='__main__':
    irisInputs, irisTargets = load()
    print(irisInputs.shape)
    print(irisTargets.shape)