# -*- coding: utf-8 -*-
from scipy.special import jn, yn, jn_zeros, yn_zeros
import matplotlib.pyplot as plt
import numpy as np

n = 0    # order
x = 0.0

# Bessel function of first kind
print("J_%d(%f) = %f" % (n, x, jn(n, x)))

x = 1.0
# Bessel function of second kind
print("Y_%d(%f) = %f" % (n, x, yn(n, x)))

# zeros of Bessel functions
n = 0  # order
m = 4  # number of roots to compute
print("zeros of Bessel functions are: ", jn_zeros(n, m))

# Plot Bessel fonctions
x = np.linspace(0, 10, 50)

markers = ['o', 's', '*', '+']
lines = ['-', '--', '-.', ':']

fig, ax = plt.subplots()
for n in range(4):
    ax.plot(x, jn(n, x), ls=str(lines[n]), marker=str(
        markers[n]), label=r"$J_%d(x)$" % n)
ax.legend()
plt.show()
