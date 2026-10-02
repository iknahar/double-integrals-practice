"""Polar coordinates, the Jacobian r, and why random darts favour the outer half."""
import sympy as sp
r, t = sp.symbols("r theta", positive=True)
J = sp.Matrix([r * sp.cos(t), r * sp.sin(t)]).jacobian([r, t])
print(sp.simplify(J.det()))                          # r
inner = sp.integrate(r / sp.pi, (r, 0, sp.Rational(1, 2)), (t, 0, 2 * sp.pi))
print(inner, 1 - inner)                              # 1/4 3/4
