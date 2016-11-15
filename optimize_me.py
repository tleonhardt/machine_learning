#!/usr/bin/env python
import numpy as np
import scipy.optimize as spo

def integer_optimize():
    x = np.arange(1,101)
    f = (x % 6)**2 % 7 - np.sin(x)
    return x[np.argmax(f)]

def f(x):
    return -x**4 + 1000 * x**3 - 20 * x**2 + 4*x -6

if __name__ == '__main__':
    print("Integer optimium:  x = {}\n".format(integer_optimize()))

    max_x = spo.fmin(lambda x: -f(x), 0)
    print("Rational optimum: x = {}\n".format(max_x))
