from equations import *
import matplotlib.pyplot as plt
import numpy as np


def bisection(f, a, b, nmax, epsilon):
    num_points = 1000
    x = []
    y = []
    pointsX = []
    pointsY = []

    x = np.linspace(a, b, num_points)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bisection Method')

    fa = f(a)
    fb = f(b)

    if np.sign(fa) == np.sign(fb):
        print("Error: f(a) and f(b) have the same sign")
        return
    
    error = b - a
    for n in range(0, nmax):
        error = error / 2
        c = a + error
        fc = f(c)
        print(f"n = {n}, c = {c}, f(c) = {fc}, error = {error}")
        pointsX.append(c)
        pointsY.append(fc)
        if abs(error) < epsilon:
            print(f"Convergence achieved after {n} iterations")
            plt.scatter(pointsX, pointsY, color='red')
            plt.show()
            return c
        if np.sign(fa) != np.sign(fc):
            b = c
            fb = fc
        else:
            a = c
            fa = fc


'''
Bisection method theorem
If the bisection algorithm is applied to a continuous function f on an interval [a, b],
where f(a)f(b) < 0, then, after n steps, an approcimate root will have been computed
with error at most (b-a)/2^(n+1).
'''
