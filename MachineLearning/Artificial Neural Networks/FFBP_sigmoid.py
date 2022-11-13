# Feedforward Backpropagation Neural Network (Sigmoid)
# 03/11/2022
# Copyright (C) 2022

import numpy as np

class FFBP:
    def __init__(self, X, T, hidden, lr=1e-1, alpha=1e-2, eps=1e-3, epochs=float('inf')):
        self.X = X
        self.T = T
        self.hidden = hidden
        self.lr = lr
        self.alpha = alpha
        self.eps = eps
        self.epochs = epochs

        self.d_in = self.X.shape[1]
        if len(self.T.shape) == 1:
            self.T = np.reshape(self.T, (len(X), 1))
        del X, T
        self.d_out = self.T.shape[1]

        self.error = []
        self.W = []
        self.init_weights()
        self.inputt = [None] * (len(self.W)+1)

        self.forward(self.X)
        self.backward()

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def d_sigmoid(x):
        return x * (1 - x) # x is cached from output of sigmoid

    @staticmethod
    def pad_ones(inputt):
        return np.hstack((inputt, np.ones((len(inputt), 1))))
    def init_weights(self):
        dim = [self.d_in] + self.hidden + [self.d_out]
        for i in range(len(self.hidden) + 1):
            self.W.append(np.random.rand(dim[i]+1, dim[i+1])) # add bias

    def forward(self, inputt):
        inputt = self.pad_ones(inputt)
        self.inputt[0] = inputt.copy()
        for i in range(len(self.W)):
            output = self.sigmoid(inputt @ self.W[i])
            inputt = self.pad_ones(output)
            self.inputt[i+1] = inputt.copy()
        return output
    
    def backward(self):
        epoch = 0
        dw = [0] * len(self.W)
        while True:
            epoch += 1
            output = self.forward(self.X)

            error = self.T - output
            mse = np.mean(error ** 2)
            print('epoch {}:\terror={}'.format(epoch, mse))
            self.error.append(mse)
            if mse < self.eps or epoch >= self.epochs:
                break

            # output layer
            delta = self.d_sigmoid(output) * error
            dw[-1] = self.lr * self.inputt[-2].T @ delta + self.alpha * dw[-1]
            self.W[-1] += dw[-1]
            # hidden layer
            for i in range(len(self.W)-2, -1, -1):
                delta = self.d_sigmoid(self.inputt[i+1]) * (delta @ self.W[i+1].T)
                delta = delta[:, :-1]
                dw[i] = self.lr * self.inputt[i].T @ delta + self.alpha * dw[i]
                self.W[i] += dw[i]