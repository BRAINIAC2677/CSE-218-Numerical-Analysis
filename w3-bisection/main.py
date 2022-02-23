import matplotlib.pyplot as plt
import numpy as np

def visualize(fun, x_low, x_high):
    '''parameters:
        fun: function which takes x as input and returns f(x) as output.
        x_low: lowest x value in the graph
        x_high: highest x value in the graph'''
    no_of_generated_points = 50
    font = {'family': 'serif',
    'color':  'darkred',
    'weight': 'bold',
    'size': 18,
    }
    plt.figure(figsize=(12, 7))
    plt.plot(np.linspace(x_low, x_high, no_of_generated_points), fun(np.linspace(x_low, x_high, no_of_generated_points)), 'g', np.linspace(x_low, x_high, no_of_generated_points), [0 for i in range(no_of_generated_points)], 'r')
    plt.legend(['f(x)', 'x-axis'], loc ="upper right")
    plt.title('Plot of f(x)', fontdict=font)
    plt.ylabel('f(x)', fontdict=font)
    plt.xlabel('x', fontdict=font)
    plt.grid()
    plt.show()


def visualBisection(low, high, fun, error_tolerance, max_iter=150):
    '''parameters:
        low: lower bound guess
        high: upper bound guess
        fun: fun: function which takes x as input and returns f(x) as output
    '''
    assert fun(low) * fun(high) <= 0,'no single root in this interval'
    assert max_iter > 0, 'invalid max_iter'
    assert error_tolerance > 0, 'invalid error_tolerance'
    prev_midx = None
    for i in range(max_iter):
        midx = (low + high)/2
        if i > 0:
            ea = np.absolute((midx - prev_midx)/midx)*100
            print(f'Iteration: {i}\nError: {ea:.6f}\n')
            if ea <= error_tolerance:
                return midx
        decider = fun(midx)*fun(high)
        if decider < 0:
            low = midx
        elif decider > 0:
            high = midx
        else:
            return midx
        prev_midx = midx
    return prev_midx

def f(x):
    fx = x**3 - 0.18*(x**2) + 4.752*(10**(-4))
    return fx

visualize(f, -1, 1)
print(visualBisection(0, .12, f, 0.5, 50))