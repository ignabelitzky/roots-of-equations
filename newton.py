from equations import *

def newton(f, f_prima, x, nmax, epsilon, delta):
    fx = f(x)
    print(f"x = {x}, f(x) = {fx}")

    for n in range(1, nmax + 1):
        fp = f_prima(x)
        if abs(fp) < delta:
            print("Small derivative")
            return None
        d = fx / fp
        x = x - d
        fx = f(x)
        print(f"n = {n}, x = {x}, f(x) = {fx}")
        if abs(d) < epsilon:
            print(f"Convergence achieved after {n} iterations")
            return None