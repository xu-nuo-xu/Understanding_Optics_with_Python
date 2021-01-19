# -*- coding: utf-8 -*-
from scipy.special import fresnel
import numpy
import matplotlib.pyplot as plt
t = numpy.linspace(-10, 10, 1000)
FS, FC = fresnel(t)
fig1 = plt.figure(figsize=(10, 5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(FC, FS, linewidth=2)
ax1.set_xlabel("C(t)", fontsize=14, weight='bold')
ax1.set_ylabel("S(t)", fontsize=14, weight='bold')
ax1.set_title("Cornu spiral", fontsize=16, weight='bold')

ax2 = plt.subplot(1, 2, 2)
ax2.plot(t, FS, ls='--', linewidth=2, label="S(t)", alpha=.8)
ax2.plot(t, FC, ls='-', linewidth=2, label="C(t)", alpha=.8)
ax2.set_xlabel("t", fontsize=14, weight='bold')
ax2.set_title("Fresnel integrals", fontsize=16, weight='bold')
plt.legend()
plt.show()