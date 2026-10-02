"""scipy's dblquad (mind the argument order) and Monte Carlo darts."""
import numpy as np
import numpy as np
from scipy import integrate
def bell(y, x):                     # careful, y comes first here
    return np.exp(-(x**2 + y**2) / 2) / (2 * np.pi)
#
top = lambda x: np.sqrt(1 - x**2)   # inner limits are functions of x
low = lambda x: -np.sqrt(1 - x**2)
val, err = integrate.dblquad(bell, -1, 1, low, top)
print(round(val, 6), round(1 - np.exp(-0.5), 6))   # 0.393469 twice
#
rng = np.random.default_rng(0)
pts = rng.normal(size=(1_000_000, 2))       # a million bell darts
print(np.mean((pts**2).sum(axis=1) < 1))    # about 0.3934
