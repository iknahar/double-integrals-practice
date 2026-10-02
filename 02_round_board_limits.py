"""Limits that bend with a round board, and the lazy square mistake."""
import sympy as sp
x, y = sp.symbols("x y", real=True)
top = sp.sqrt(1 - x**2)        # where the circle's edge is, at this x
disk = sp.integrate(1 / sp.pi, (y, -top, top), (x, -1, 1))
print("round limits:", sp.simplify(disk))     # 1
lazy = sp.integrate(1 / sp.pi, (y, -1, 1), (x, -1, 1))
print("square limits:", lazy, float(lazy))    # 4/pi 1.273
