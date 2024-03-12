from bisection import *
from newton import *

def main():
    print("Bisection method on [0, 1] with equation f(x) = x^3 - 3x + 1")
    bisection(f, 0.0, 1.0, 100, 1e-6)
    print()
    print("Bisection method on [0.5, 2] with equation f(x) = x^3 - 2sin(x)")
    bisection(g, 0.5, 2.0, 100, 1e-6)
    print()
    print("Newton's method with equation f(x) = ((x - 2) * x + 1) * x - 3")
    newton(h, h_prima, 3.0, 100, 1e-6, 1e-6)
    print()


if __name__ == "__main__":
    main()