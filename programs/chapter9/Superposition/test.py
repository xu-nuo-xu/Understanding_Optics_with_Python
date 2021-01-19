import random
import numpy as np
from numpy import pi, cos
import matplotlib.pyplot as plt
# Create the figure object
fig = plt.figure()
fig.set_size_inches(10, 10)
ax = fig.add_subplot(1, 1, 1)
tmax = 5
x = np.linspace(0, 4 * pi, 400)
t = np.linspace(0, tmax, 100)

y = [0 for xi in range(len(x))]
xx = [[0 for ti in range(len(t))]
      for xi in range(len(x))]
fraction = t[1] / tmax
for ti in range(len(t)):

    #print(var)
    for xi in range(len(x)):
        var = random.uniform(-pi*0.1, pi*0.1)
        xx[xi][ti] = cos(x[xi] + var)

for xi in range(len(x)):
    y[xi] = sum(xx[xi]) * fraction

ax.plot(x, y, 'k')
plt.show()