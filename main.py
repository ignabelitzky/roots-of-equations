from bisection import bisection_method
from newton import newton_method
from secant import secant_method
from equations import f, g, h, h_prima, i

def main():
    print("Bisection method on [0, 1] with equation f(x) = x^3 - 3x + 1")
    bisection_method(f, 0.0, 1.0, 100, 1e-6)
    print()
    print("Bisection method on [0.5, 2] with equation f(x) = x^3 - 2sin(x)")
    bisection_method(g, 0.5, 2.0, 100, 1e-6)
    print()
    print("Newton's method with equation f(x) = ((x - 2) * x + 1) * x - 3")
    newton_method(h, h_prima, 3.0, 100, 1e-6, 1e-6)
    print()
    print("Secant method on [-1, 1] with equation f(x) = x^5 + x^3 + 3")
    secant_method(i, -1.0, 1.0, 100, 1e-6)


if __name__ == "__main__":
    main()