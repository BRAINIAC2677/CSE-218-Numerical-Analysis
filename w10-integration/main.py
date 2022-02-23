import numpy as np
import matplotlib.pyplot as plt

def trapezoidalIntegration(lowerLimit, upperLimit, noOfSegment, integrand):
    h = (upperLimit - lowerLimit)/noOfSegment
    ans = integrand(lowerLimit) + integrand(upperLimit)
    for i in range(1, noOfSegment):
        ans += 2*integrand(lowerLimit + i*h)
    ans = ans*h/2
    return ans

def simpsonIntegration(lowerLimit, upperLimit, noOfApplication, integrand):
    noOfSegment = 2 * noOfApplication
    h = (upperLimit - lowerLimit)/noOfSegment
    ans = integrand(lowerLimit) + integrand(upperLimit)
    for i in range(1, noOfSegment):
        ans += (2 if i%2 == 0 else 4)*integrand(lowerLimit + i*h)
    ans = ans*h/3
    return ans

def integrate(lowerLimit, upperLimit, iterations, integrand, integrationFunction):
    prev = None
    for i in range(1, iterations+1):
        cur = integrationFunction(lowerLimit, upperLimit, i, integrand)
        print(f'Iteration: {i}\nAnswer: {cur:0.6f}')
        if prev is not None:
            ea = np.abs((prev - cur)/prev)*100
            print(f'Error: {ea:0.12f}')
        print("\n")
        prev = cur

def fun(x, cme = 5 * (10**-4)):
    f = 6.73*x + 6.725*(10**-8) + 7.26*(10**-4)*cme
    f /= 3.62*(10**-12)*x + 3.908*(10**-8)*x*cme
    f *= -1
    return f

integrate(1.22*(10**-4), 1.22*(10**-4)*0.5, 5, fun, trapezoidalIntegration)

integrate(1.22*(10**-4), 1.22*(10**-4)*0.5, 5, fun, simpsonIntegration)

def plot():
    initialConcentration = 1.22 * (10**-4)
    y = np.array([1.22, 1.20, 1.0, 0.8, 0.6, 0.4, 0.2])
    y = y * (10**-4)
    x = simpsonIntegration(initialConcentration, y, 5, fun)
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 18,
        }
    plt.figure(figsize=(12, 7))
    plt.plot(x, y, marker='o')
    plt.title("Time vs Oxygen Concentration Graph", fontdict=font)
    plt.ylabel("Oxygen Concentration, x(moles/cc)", fontdict=font)
    plt.xlabel("Time, t(s)", fontdict=font)
    plt.grid()
    plt.show()

plot()