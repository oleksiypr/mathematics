import matplotlib.pyplot as plt
import numpy as np

# Max number of iterations
M = 250

# Grid pixels N*N
N = 1000

# D - surrounding of point (x0, y0)
x0, y0 = (-0.5, 0.)
D = 1.0
ext = [x_min, x_max, y_min, y_max] = (x0 - D, x0 + D, y0 - D, y0 + D)

xs = np.linspace(x_min, x_max, N)
ys = np.linspace(y_min, y_max, N)

X, Y = np.meshgrid(xs, ys)
C = X + 1j*Y


def converge(c):
    z = 0
    n = 0
    while (z.real**2 + z.imag**2) <= 4 and n < M:
        z = z**2 + c
        n += 1
    return n


R = [[converge(C[i][j]) for i in range(N)] for j in range(N)]
R = np.array(R) / M
R = np.transpose(R)

plt.imshow(R, cmap='hsv',  interpolation='nearest', extent=ext)
plt.savefig('mandelbrot_1000by1000.png')
plt.show()