# -*- coding: utf-8 -*-
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x)


n = np.arange(0, 10)
x = np.linspace(0, 9, 100)

# simulate measurement with noise
y_meas = f(n) + 0.1 * np.random.randn(len(n))
y_real = f(x)

linear_interpolation = interp1d(n, y_meas)
y_interp1 = linear_interpolation(x)

cubic_interpolation = interp1d(n, y_meas, kind='cubic')
y_interp2 = cubic_interpolation(x)

fig, ax = plt.subplots()
ax.plot(n, y_meas, ':bs', label='noisy data')
ax.plot(x, y_real, '--k', lw=2, label='true function')
ax.plot(x, y_interp1, '-.r', label='linear interp')
ax.plot(x, y_interp2, '-g', label='cubic interp')
ax.legend(loc=3)
plt.show()