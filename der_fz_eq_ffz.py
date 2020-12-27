import numpy as np
from numpy import pi
import pylab as plt
from colorsys import hls_to_rgb


def colorize(z):
    r = np.abs(z)
    arg = np.angle(z)

    h = (arg + pi)  / (2 * pi) + 0.5
    l = 1.0 - 1.0/(1.0 + r**0.3)
    s = 0.8

    c = np.vectorize(hls_to_rgb) (h,l,s) # --> tuple
    c = np.array(c)  # -->  array of (3,n,m) shape, but need (n,m,3)
    c = c.swapaxes(0,2)
    return c


N = 1000

x, y = np.ogrid[-5:5:N*1j, -5:5:N*1j]
z = x + 1j*y

w = (z**2 - 1)*(z - 2 - 1j)**2 / (z**2 + 2 + 2*1j)

img = colorize(w)
plt.imshow(img)
plt.show()