"""Box-Muller: two flat random numbers become two bell-shaped ones."""
import numpy as np
rng = np.random.default_rng(1)
u1, u2 = rng.uniform(size=(2, 200_000))     # flat numbers between 0 and 1
#
# a distance with the right ramp, and a random angle
R = np.sqrt(-2 * np.log(u1))
theta = 2 * np.pi * u2
z1, z2 = R * np.cos(theta), R * np.sin(theta)
#
# a standard normal has mean 0 and spread 1, and the pair is independent
print("mean, sd of z1:", round(z1.mean(), 3), round(z1.std(), 3))
print("mean, sd of z2:", round(z2.mean(), 3), round(z2.std(), 3))
print("corr(z1, z2):", round(np.corrcoef(z1, z2)[0, 1], 3))
#
# the share within one unit of the centre should be 1 - e^(-1/2)
inside = np.mean(z1**2 + z2**2 < 1)
print("inside unit circle:", round(inside, 4), "exact:",
      round(1 - np.exp(-0.5), 4))
