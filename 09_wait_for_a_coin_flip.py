"""How long two people must wait for a 50/50 chance of meeting."""
import sympy as sp
w = sp.symbols("w", positive=True)          # waiting time in hours
meet = 1 - (1 - w) ** 2                     # the two-triangle trick
coin = sp.solve(sp.Eq(meet, sp.Rational(1, 2)), w)
print([round(float(v) * 60, 1) for v in coin if v < 1])   # [17.6]
