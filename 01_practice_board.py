"""Slice-by-slice volume on the practice board, f(x, y) = x + y."""
import sympy as sp
x, y = sp.symbols("x y", real=True)
f = x + y                       # my aim, written as a formula
#
# inner slice: x is frozen, y runs across the board
slice_area = sp.integrate(f, (y, 0, 1))
print("A(x) =", slice_area)                   # x + 1/2
#
# outer pass: add the slices up along x
print("total:", sp.integrate(slice_area, (x, 0, 1)))   # 1
#
# chance of the top-right quarter of the board
half = sp.Rational(1, 2)
p = sp.integrate(f, (y, half, 1), (x, half, 1))
print("top-right quarter:", p, float(p))      # 3/8 0.375
