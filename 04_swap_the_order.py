"""Changing the order of integration on the triangle 0 < x < y < 1."""
import sympy as sp
x, y = sp.symbols("x y", real=True)
g = sp.exp(y**2)
stuck = sp.integrate(g, (y, x, 1))
print(stuck)                     # needs erfi, a special function
swapped = sp.integrate(g, (x, 0, y), (y, 0, 1))
print(swapped, float(swapped))   # E/2 - 1/2 0.859
