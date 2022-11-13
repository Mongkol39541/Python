# Gradient Descent
# 03/11/2022
# Copyright (C) 2022

import numpy as np
from matplotlib import pyplot as plt

def grad_desc(xO, f, df, lr=1e-2, eps=1e-2, show=True):
    xOld = xO
    xNew = xOld + 2*eps
    i = 0
    while abs(xNew - xOld) > eps:
        xOld = xNew
        xNew -= lr * df(xNew)
        if show:
            plt.plot(xNew, f(xNew), 'r')
            plt.text(xNew, f(xNew), str(i))
            plt.draw()
            plt.pause(0.2)
            i += 1
    return xNew

if __name__ == '__main__':
    def f(x):
        return x ** 4 -3 * x ** 3 +2
    
    def df(x):
        return 4 * x ** 3 - 9 * x **2

    x = np.arange(2, 2.41, 0.01)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')

    locals_min = grad_desc(2, f, df)

    exact_min = 9 / 4
    print('Gradient Descent\'s Local minimum occurs at', locals_min)
    print('Exact minimum occurs at', exact_min)
    print('Error rate is', abs((locals_min - exact_min) / exact_min * 100), '%')
    print('Accuracy rate is', 100 - abs((locals_min - exact_min) / exact_min * 100), '%')
    plt.show()