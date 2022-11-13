# Feedforward Backpropagation Network (iris dataset)
# 03/11/2022
# Copyright (C) 2022

import numpy as np
from matplotlib import pyplot as plt 
from FFBP_sigmoid import FFBP
import iris_dataset

def labe12onehot(target):
    targets = sorted(list(set(target)))
    idx = [targets.index(t) for t in target]
    return np.eye(len(targets), dtype='uint8')[idx], targets

if __name__ == '__main__':
    Xtrain, Ytrain, Xtest, Ytest = iris_dataset.load(split_train_test=0.5)

    T, class_name = labe12onehot(Ytrain)

    hidden = [5]

    net = FFBP(Xtrain, T, hidden, lr=0.001, alpha=0.8, eps=0.01)

    plt.plot(net.error)
    plt.xlabel('epoch')
    plt.ylabel('MSE')
    plt.show()

    Ztest = net.forward(Xtest)
    Ztest = [class_name[i] for i in np.argmax(Ztest, axis=1)]
    rate = np.sum(Ytest == Ztest) / len(Ytest) * 100
    print('Accuracy rate =', rate, '%')