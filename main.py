from bisection import *

def main():
    print("Bisection method on [0, 1] with equation f(x) = x^3 - 3x + 1")
    bisection(f, 0.0, 1.0, 100, 1e-6)
    print()
    print("Bisection method on [0.5, 2] with equation g(x) = x^3 - 2sin(x)")
    bisection(g, 0.5, 2.0, 100, 1e-6)


if __name__ == "__main__":
    main()