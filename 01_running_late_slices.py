"""Slicing a hill: the running-late density f(x, y) = x + y."""
import sympy as sp
x, y = sp.symbols("x y", real=True)
f = x + y                          # both of us lean late
#
# inner integral: x stays frozen, we add along y
slice_area = sp.integrate(f, (y, 0, 1))
print("one slice:", slice_area)                # x + 1/2
print("whole hill:", sp.integrate(slice_area, (x, 0, 1)))   # 1
#
# both of us arriving in the last half hour
h = sp.Rational(1, 2)
both_late = sp.integrate(f, (y, h, 1), (x, h, 1))
print("both late:", both_late)                 # 3/8
