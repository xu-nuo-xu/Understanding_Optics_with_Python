from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero

x = linspace(-5 * pi, 5 * pi, 500)
y = (sin(x) / x)**2
fig = plt.figure(figsize=(8, 4))
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
ax.grid(True)
ax.set_xticks([-5 * pi, -4 * pi, -3 * pi, -2 * pi, -pi,
               0, pi, 2 * pi, 3 * pi, 4 * pi, 5 * pi])
ax.set_xticklabels(["$-5 \pi$", "$-4 \pi$", "$-3 \pi$", "$-2 \pi$",
                    "$- \pi$", "0", "$\pi$", "$2 \pi$", "$3 \pi$", "$4 \pi$", "$5 \pi$"])
ax.set_ylim((-.3, 1.2))
ax.set_yticklabels([])
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("->")
    ax.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
ax.plot(x, y, label=r"$sinc^{2} \ x$", color="k", linewidth=3, alpha=0.8)
ax.text(5.5 * pi, 0., "x")
ax.text(0.1, 1, "1")
ax.legend()
plt.tight_layout()
plt.savefig("sinc.png")
plt.show()
