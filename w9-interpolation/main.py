import numpy as np
import matplotlib.pyplot as plt
import sys

def visualize(given_x, given_y, interpolated_x, interpolated_y):
    font = {'family': 'serif',
    'color':  'darkred',
    'weight': 'bold',
    'size': 18,
    }
    plt.figure(figsize=(12, 7))
    plt.plot(given_x,given_y,'o', interpolated_x, interpolated_y) 
    plt.legend(["given points", "interpolated curve"], loc ="upper left")
    plt.title('y vs x graph', fontdict=font)
    plt.xlabel('x values', fontdict=font)
    plt.ylabel('y values', fontdict=font)
    plt.grid()
    plt.show()

def weightingFunction(index, x, xs):
    ret = 1
    n = xs.shape[0]
    for i in range(n):
        if i != index:
            ret = ret*(x-xs[i])/(xs[index] - xs[i])
    return ret

def lagrangeInterpolation(xs, ys, uxs):
    '''use all the points of xs and ys in interpolating uxs. if n points are given, it will use (n-1)th order polynomial interpolant.'''
    n = xs.shape[0]
    m = uxs.shape[0]
    uys = np.zeros(m)
    for i in range(m):
        for j in range(n):
            cur = ys[j] * weightingFunction(j, uxs[i], xs)
            uys[i] = uys[i] + cur
    return uys


def loadData():
    stk = np.loadtxt('stock.txt', dtype = 'str')
    stk = np.float128(stk[1:])
    n = stk.shape[0]
    days = np.zeros(n)
    indices = np.zeros(n)
    for i in range(n):
        days[i] = stk[i][0]
        indices[i] = stk[i][1]
    return days, indices

def main():
    days, indices = loadData()
    xs = days
    ys = indices
    minx = sys.float_info.max
    maxx = sys.float_info.min
    for day in days:
        minx = day if day < minx else minx
        maxx = day if day > maxx else maxx
    uxs = np.linspace(minx, maxx, 200)
    uys = lagrangeInterpolation(xs, ys, uxs)
    visualize(xs, ys, uxs, uys)

main()