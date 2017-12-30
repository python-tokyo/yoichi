import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt

def f():
    y, x = np.mgrid[-11:11:1500j, -16:6:1500j]
    z = 40 * np.cos(x**2 + y**2)
#    z[0, 1] = 2000
    z[0, 0] = -9000
    ls = colors.LightSource(315, 45)
    fig, ax = plt.subplots(ncols=1, figsize=(8, 8), frameon=False)
    fig.frameon = False
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)
    rgb = ls.shade(z, plt.cm.copper)
    ax.imshow(rgb, interpolation='bilinear')

f()
plt.savefig("background.png")
