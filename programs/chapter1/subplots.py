# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
fig1 = plt.figure(1)                # the first figure
ax1 = plt.subplot(211)             # the first subplot in the first figure
ax1.plot([1, 2, 3])
ax2 = plt.subplot(212)             # the second subplot in the first figure
ax2.plot([4, 5, 6])

fig2 = plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

# figure 1 current; subplot(212) still current
fig1 = plt.figure(1)
ax1 = plt.subplot(211)             # make subplot(211) in figure1 current
ax1.set_title('Easy as 1, 2, 3')  # subplot 211 title
plt.show()
