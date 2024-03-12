import numpy as np

def f(x):
    return x**3 - 3 * x + 1

def f_prima(x):
    return 3 * x**2 - 3

def g(x):
    return x**3 - 2 * np.sin(x)

def h(x):
    return ((x - 2) * x + 1) * x - 3

def h_prima(x):
    return (3 * x - 4) * x + 1

def i(x):
    return x**5 + x**3 + 3