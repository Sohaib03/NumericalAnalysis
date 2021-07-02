from math import exp
import matplotlib.pyplot as plt
import numpy as np


def func(x, y, b):

    sum_xye = 0
    sum_ye  = 0
    sum_xe  = 0
    sum_e2  = 0

    for i in range(len(x)):
        sum_xye += x[i] * y[i] * exp(b * x[i])
        sum_ye  += y[i] * exp(b * x[i])
        sum_xe  += x[i] * exp(2 * b * x[i])
        sum_e2  += exp(2 * b * x[i])
    
    return sum_xye - (sum_ye / sum_e2) * sum_xe

def getA(x, y, b):
    sum_ye  = 0
    sum_e2  = 0

    for i in range(len(x)):
        sum_ye  += y[i] * exp(b * x[i])
        sum_e2  += exp(2 * b * x[i])
    
    return (sum_ye / sum_e2)


def bisection(low, high, x, y, max_iteration = 20):
    mid = (low + high) / 2

    if (mid == 0):
        mid += 0.000000001

    if (max_iteration == 0):
        return mid

    if (func(x, y, mid) * func(x, y, low) < 0):
        return bisection(low, mid, x, y, max_iteration - 1)
    else:
        return bisection(mid, high, x, y, max_iteration - 1)
    

n = int(input())

xs = []
ys = []

for i in range(n):
    inp = input().split()
    x, y =  [float(i) for i in inp]


    xs.append(x)
    ys.append(y)


plt.scatter(xs, ys)

b = bisection(-0.5, 0, xs, ys)
a = getA(xs, ys, b)

def f(x, a, b):
    return a * exp(b * x)

x_points = np.arange(-1, 10, 0.01)
y_points = [f(k, a, b) for k in x_points]

plt.plot(x_points, y_points)
plt.show()


"""
6
0 1.000
1 0.891
3 0.708
5 0.562
7 0.447
9 0.355
"""