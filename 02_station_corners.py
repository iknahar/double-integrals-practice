"""The station problem: meet within 15 minutes, done with two corner triangles."""
import sympy as sp
x, y = sp.symbols("x y", real=True)
q = sp.Rational(1, 4)               # 15 minutes is a quarter hour
#
# friend arrives over 15 min after me: y runs from x + 1/4 up to 1
corner = sp.integrate(1, (y, x + q, 1), (x, 0, 1 - q))
print("one missed corner:", corner)           # 9/32
print("chance we meet:", 1 - 2 * corner)      # 7/16
