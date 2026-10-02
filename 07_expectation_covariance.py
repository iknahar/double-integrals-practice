"""Averages and covariance as double integrals."""
import sympy as sp
x, y = sp.symbols("x y", real=True)
f = x + y                                      # the running-late hill
E = lambda g: sp.integrate(g * f, (y, 0, 1), (x, 0, 1))
ex, ey, exy = E(x), E(y), E(x * y)
print(ex, exy, exy - ex * ey)                  # 7/12 1/3 -1/144
top = sp.sqrt(1 - x**2)
cov_disk = sp.integrate(x * y / sp.pi, (y, -top, top), (x, -1, 1))
print(cov_disk)                                # 0
