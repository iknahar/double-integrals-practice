"""The one function where swapping the order flips the sign of the answer."""
import sympy as sp
a, b = sp.symbols("a b", positive=True)
k = (a**2 - b**2) / (a**2 + b**2) ** 2
print(sp.integrate(k, (b, 0, 1), (a, 0, 1)))    # pi/4
print(sp.integrate(k, (a, 0, 1), (b, 0, 1)))    # -pi/4
