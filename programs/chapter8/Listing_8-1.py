import numpy as sc
import matplotlib as mpl

# # Set up matplotlib to use pgf. This MUST be done before pyplot of pylab
# mpl.use("pgf")
# pgf_with_rc_fonts = {
#   "font.family": "Dejavu Serif",
#   "font.serif": [],
#   "font.size": 21,
#   "xtick.labelsize": 10,
#   "ytick.labelsize": 10,
#   "savefig.dpi": 600,
# }
# mpl.rcParams.update(pgf_with_rc_fonts)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs) # 这里 (0, 0) 只表示弃用 2d 作 Arrow 的方法
        self._verts3d = xs, ys, zs

    def draw(self, renderer):   # 三维作图重写 draw 方法
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)    # 3d 转 2d
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))  # 二维平面中只有 x, y坐标
        print(zs)
        FancyArrowPatch.draw(self, renderer)


fig = plt.figure()
fig.set_size_inches(12, 7)
ax = fig.add_subplot(1, 1, 1, projection='3d')  # 注意 3d 子图

polAng = sc.pi / 4      # 偏振角为 pi / 4
# Plot the wave in the xy plane
x = sc.linspace(0, 2 * sc.pi, 512)
y = sc.sin(x) * sc.cos(polAng)
z = sc.sin(x) * sc.sin(polAng)
yy = sc.zeros(x.size)
zz = sc.zeros(x.size)
#plt.hold(True)
ax.plot(x, y, zz, 'k', ls='dotted')
ax.plot(x, yy, z, 'k', ls='dashed')
ax.plot(x, y, z, color='k')


# Plot the E vectors
xv = sc.linspace(0, 2 * sc.pi, 16)
yv = sc.sin(xv) * sc.cos(polAng)
zv = sc.sin(xv) * sc.sin(polAng)

for i in range(len(xv)):
    a = Arrow3D([xv[i], xv[i]], [0, yv[i]], [0, zv[i]],
                mutation_scale=10, lw=1, arrowstyle="-|>", ls='dashed', color='k')
    ax.add_artist(a)

a = Arrow3D([0, 0], [0, 1.25], [0, 0], mutation_scale=15,   # y 坐标轴
            lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)

a = Arrow3D([0, 0], [0, 0], [0, 1.25],
            mutation_scale=15, lw=1, arrowstyle="-|>", color="k")   # z 坐标轴
ax.add_artist(a)


a = Arrow3D([0, 2.75 * sc.pi], [0, 0], [0, 0],
            mutation_scale=15, lw=1, arrowstyle="-|>", color="k")   # x 坐标轴
ax.add_artist(a)
#plt.hold(True)

ax.set_xlim(0, 7.5)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
plt.axis('off')
ax.elev = 25
ax.azim = 10

ax.text(2.85 * sc.pi, 0, -0.1, r'$t$')
ax.text(-0.5, 1.25, 0, r'$\hat{x}$')
ax.text(-0.5, 0, 1.35, r'$\hat{y}$')

plt.show()
# fig.savefig('Fig_Pol_Plane_Polarization.png')
