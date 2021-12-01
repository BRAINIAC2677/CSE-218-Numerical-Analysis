import matplotlib.pyplot as plt
import numpy as np

def fun(x):
    fx = x**3 - 0.18*(x**2) + 4.752*(10**(-4))
    return fx

#graph plotting
plt.plot(np.arange(-7, 7), fun(np.arange(-7, 7)), 'r')
plt.title('Plot of f(x)')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()

def bisection(low, high, expected_ea, max_iter):
    assert fun(low) * fun(high) <= 0,"no single root in this interval"
    assert max_iter > 0, "invalid max_iter"

    prev_midx = None
    for i in range(max_iter):
        midx = (low + high)/2
        if i > 0:
            ea = np.absolute((midx - prev_midx)/midx)*100
            if ea <= expected_ea:
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

def visualBisection(low, high, expected_ea, max_iter):
    assert fun(low) * fun(high) <= 0,"no single root in this interval"
    assert max_iter > 0, "invalid max_iter"

    prev_midx = None
    for i in range(max_iter):
        midx = (low + high)/2
        if i > 0:
            ea = np.absolute((midx - prev_midx)/midx)*100
            if i < 21:
                print(f'Iteration: {i}\nError: {ea:.6f}\n')
            if ea <= expected_ea:
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

print(visualBisection(0, .12, 0.5, 50))