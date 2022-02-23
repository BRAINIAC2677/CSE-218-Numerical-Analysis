import numpy as np
import matplotlib.pyplot as plt

def bisection(low, high, fun, expected_ea, max_iter=150):
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

def linearRegression(x, y):
    '''returns a0 and a1 fitting the linear model y = a0 + a1*x to the given x and y datasets, where x and y are numpy arrays'''
    x = np.float128(x)
    y = np.float128(y)
    n = x.shape[0]
    sx = np.sum(x)
    sy = np.sum(y)
    sxy = np.sum(x*y)
    sxsquared = np.sum(x**2)
    a1 = (n*sxy - sx*sy)/(n*sxsquared - sx**2)
    a0 = sy/n - a1*sx/n
    return a0, a1

def visualize(x, y):
    font = {'family': 'serif',
    'color':  'darkred',
    'weight': 'bold',
    'size': 18,
    }
    plt.figure(figsize=(12, 7))
    plt.plot(x, y, marker='o') 
    plt.legend(["dataset"], loc ="upper right")
    plt.title('y vs x graph', fontdict=font)
    plt.xlabel('x values', fontdict=font)
    plt.ylabel('y values', fontdict=font)
    plt.grid()
    plt.show()

def visualizeModel(x, y, predict_x, predicted_y):
    '''x and y are datasets and predicted_y is model prediction on predict_x values'''
    font = {'family': 'serif',
    'color':  'darkred',
    'weight': 'bold',
    'size': 18,
    }
    plt.figure(figsize=(12, 7))
    plt.plot(x, y, 'or', predict_x, predicted_y, 'o-b') 
    plt.legend(["Data points", "Regressed Model"], loc ="upper right")
    plt.title('Model Prediction Visualization', fontdict=font)
    plt.xlabel('x values', fontdict=font)
    plt.ylabel('y values', fontdict=font)
    plt.grid()
    plt.show()

def exponentialModel(x, y, byTransformation=True):
    '''returns a and b fitting the exponential model y = a*e^(bx) to the given x and y datasets, where x and y are numpy arrays'''
    x = np.float128(x)
    y = np.float128(y)
    if byTransformation:
        z = np.log(y)
        a0, a1 = linearRegression(x, z)
        a = np.exp(a0)
        b = a1
        return a, b
    else:
        def fun(b):
            s1 = np.sum(y*x*np.exp(b*x))
            s2 = np.sum(y*np.exp(b*x))
            s3 = np.sum(np.exp(2*b*x))
            s4 = np.sum(x*np.exp(2*b*x))
            f = s1 - s2/s3*s4
            return f
        b = bisection(-5, 5, fun, 0.005) #assumed b is between -5 and 5. Change it if necessary.
        a = np.sum(y*np.exp(b*x))/np.sum(np.exp(2*b*x))
        return a, b 

def predictExponentialModel(x, y, predict_x):
    n = predict_x.shape[0]
    predicted_y = np.zeros(shape=(n,))
    a, b = exponentialModel(x, y)
    for i in range(n):
        predicted_y[i] = a*np.exp(b*predict_x[i])
    return predicted_y


#visualization of dataset
x = np.arange(0, 31, 5)
y = np.array([1000, 550, 316, 180, 85, 56, 31])
print(x, y)
visualize(x, y)

#exponential model
visualizeModel(x, y, x, predictExponentialModel(x, y, x))

a, b = exponentialModel(x, y)
print(f'\n\na: {a:0.6f}\nb: {b:0.6f}\n')
predicted_drug = predictExponentialModel(x, y, np.array([40.0]))[0]
print(f'Predicted Drug: {predicted_drug:0.6f}\n\n')