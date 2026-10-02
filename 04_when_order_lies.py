"""The function where swapping the order flips the sign of the answer."""
import sympy as sp
x, y = sp.symbols("x y", positive=True)
f = (x**2 - y**2) / (x**2 + y**2) ** 2
print(sp.integrate(f, (y, 0, 1), (x, 0, 1)))    # pi/4
print(sp.integrate(f, (x, 0, 1), (y, 0, 1)))    # -pi/4
