import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

fig = plt.figure(frameon=False)
fig.set_size_inches(8, 8)
ax = plt.Axes(fig, [0, 0, 1, 1])
ax.set_axis_off()
fig.add_axes(ax)

delta = 0.01
x = y = np.arange(-3, 3, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1, 1, 0, -3)
Z2 = mlab.bivariate_normal(X, Y, 1, 1, 0, 0.25)
Z = Z2 - Z1
im = plt.imshow(Z, interpolation="bilinear", cmap=cm.gist_ncar, origin="lower",
                extent=[-3, 3, -3, 3], vmax=abs(Z).max(), vmin=-abs(Z).max())
plt.savefig("icon.png")
