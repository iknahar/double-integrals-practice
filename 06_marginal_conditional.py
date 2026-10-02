"""Normalising 8xy on a triangle, its marginals and a conditional slice."""
import sympy as sp
x, y, c = sp.symbols("x y c", positive=True)
vol = sp.integrate(c * x * y, (x, 0, y), (y, 0, 1))
c_val = sp.solve(sp.Eq(vol, 1), c)[0]
print(vol, c_val)                         # c/8 8
f = c_val * x * y
fx = sp.integrate(f, (y, x, 1))           # slice at x: y from x to 1
fy = sp.integrate(f, (x, 0, y))           # slice at y: x from 0 to y
print(sp.expand(fx), fy)                  # -4x**3 + 4x, 4y**3
cond = sp.simplify(f / fx)                # one slice, rescaled
print(cond, sp.simplify(sp.integrate(cond, (y, x, 1))))   # ..., 1
