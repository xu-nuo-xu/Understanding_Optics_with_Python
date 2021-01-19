# Some standard imports
import numpy as sc
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


# Create the figure object
fig = plt.figure()
fig.set_size_inches(10, 10)
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Plot the wave in the xy plane
x = sc.linspace(0, 3 * sc.pi, 512)
y = sc.cos(x)
z = sc.sin(x)   # * (-1)  右旋 式(8.14a)(8.14b)
yy = sc.zeros(x.size)
zz = sc.zeros(x.size)
# plt.hold(True)

# Plot the E vectors
xv = sc.linspace(0, 2 * sc.pi, 16)
yv = sc.cos(xv)
zv = sc.sin(xv)     # * (-1)   右旋

# The E-vector and its envelope
for i in range(len(xv)):
    a = Arrow3D([xv[i], xv[i]], [0, yv[i]], [0, zv[i]],
                mutation_scale=15, lw=0.35, arrowstyle="-|>",  color='k')
    ax.add_artist(a)
ax.plot(x, y, z, color='k', lw=0.5)

# The x, y and t axes
a = Arrow3D([-0.5, -0.5], [0, 1.5], [0, 0], mutation_scale=15,
            lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(-0.5, 1.60, 0, r'$\hat{x}$')
a = Arrow3D([-0.50, -0.50], [0, 0], [0, 1.75],
            mutation_scale=15, lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(-0.5, 0, 1.85, r'$\hat{y}$')
a = Arrow3D([-0.5, 5.75 * sc.pi], [0, 0], [0, 0],
            mutation_scale=15, lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(5.85 * sc.pi, 0, -0.2, r'$t$')

# Set the axes properties
ax.set_xlim(0, 17.5)
ax.set_ylim(-1.7, 1.7)
ax.set_zlim(-1.7, 1.7)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
plt.axis('off')
ax.elev = 30
ax.azim = 35

# Show the plot
plt.show()
