import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
xs = np.linspace(-5, 5, 1000)
ys = np.linspace(-5, 5, 1000)

X, Y = np.meshgrid(xs, ys)
Z = X + 1j*Y


# Plot the surface.
surf_1 = ax.plot_surface(X, Y, np.angle(Z), cmap=cm.coolwarm,
                         linewidth=0, antialiased=False)

surf_2 = ax.plot_surface(X, Y, np.angle(Z) + 2*np.pi, cmap=cm.coolwarm,
                         linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-10.01, 10.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf_1, shrink=0.5, aspect=5)
fig.colorbar(surf_2, shrink=0.5, aspect=5)

plt.show()
