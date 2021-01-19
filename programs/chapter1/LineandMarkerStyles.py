# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 10)
fig, ax = plt.subplots()

ax.plot(x, x + 1, color="blue", linewidth=0.25)
ax.plot(x, x + 2, color="blue", linewidth=0.50)
ax.plot(x, x + 3, color="blue", linewidth=1.00)
ax.plot(x, x + 4, color="blue", linewidth=2.00)

# possible linestype options '-', '-.', ':', 'steps'
ax.plot(x, x + 5, color="red", lw=2, linestyle='-')
ax.plot(x, x + 6, color="red", lw=2, ls='-.')
ax.plot(x, x + 7, color="red", lw=2, ls=':')

# custom dash
line, = ax.plot(x, x + 8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10])  # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x + 9, color="green", lw=2, ls='-.', marker='+')
ax.plot(x, x + 10, color="green", lw=2, ls='-.', marker='o')
ax.plot(x, x + 11, color="green", lw=2, ls='-.', marker='s')
ax.plot(x, x + 12, color="green", lw=2, ls='-.', marker='1')

# marker size and color
ax.plot(x, x + 13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x + 14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x + 15, color="purple", lw=1, ls='-',
        marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x + 16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue")
# make a title for the subplot
ax.set_title('"ax.plot(x, y, ...)": Lines and/or markers',
             fontsize=16, weight='bold')
# make x and y axis label and set their font size and weight
ax.set_xlabel("X-Axis", fontsize=12, weight='bold')
ax.set_ylabel("Y-Axis", fontsize=12, weight='bold')
plt.show()
