from equations import *

def bisection(f, a, b, nmax, epsilon):
    fa = f(a)
    fb = f(b)

    if math.copysign(1, fa) == math.copysign(1, fb):
        print("Error: f(a) and f(b) have the same sign")
        return
    
    error = b - a
    for n in range(0, nmax):
        error = error / 2
        c = a + error
        fc = f(c)
        print(f"n = {n}, c = {c}, f(c) = {fc}, error = {error}")
        if abs(error) < epsilon:
            print(f"Convergence achieved after {n} iterations")
            return c
        if math.copysign(1, fa) != math.copysign(1, fc):
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
