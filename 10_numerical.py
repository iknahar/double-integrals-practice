"""scipy's dblquad (mind the argument order) and a Monte Carlo station."""
import numpy as np
from scipy import integrate
inside = lambda y, x: 1.0           # careful, dblquad passes y first
low = lambda x: max(0.0, x - 0.25)  # band edges at this x
high = lambda x: min(1.0, x + 0.25)
val, err = integrate.dblquad(inside, 0, 1, low, high)
print(round(val, 4))                            # 0.4375
#
rng = np.random.default_rng(0)
you, friend = rng.uniform(0, 60, size=(2, 1_000_000))
print(np.mean(np.abs(you - friend) <= 15))      # about 0.4375
