import plotly.graph_objs as go
import numpy as np
from numpy.linalg import inv

# original data
t = np.linspace(0, 20, 100)
x, y, z = np.cos(t), np.sin(t) - 2.0, t

# reflection parameter
theta_degrees = 60.
theta = np.radians(theta_degrees)

# mirror plane matrix
E = np.array([
    [1.,            0.,             0.],
    [0., np.cos(theta), -np.sin(theta)],
    [0., np.sin(theta),  np.cos(theta)]
])

# reflection matrix
TE = np.array([
    [1., 0.,  0.],
    [0., 1.,  0.],
    [0., 0., -1.]
])

# reflection
T  = E @ TE @ inv(E)
R  = np.array([x, y, z])
R1 = T @ R

# mirror plane coordinates
X1, Y1 = np.meshgrid(np.linspace(-10., 10., 5), np.linspace(- 0., 10., 5))
Z1 = np.zeros([5, 5])

# mirror plane coordinate tensor of rank 3
M1 = np.array([X1, Y1, Z1])

# mirror plane
M = np.tensordot(E, M1, 1)

# 3D picture
fig = go.Figure()

fig.add_trace(go.Scatter3d(x=R1[0, :], y=R1[1, :], z=R1[2, :], mode="lines"))
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode="lines"))
fig.add_trace(go.Surface(x=M[0], y=M[1], z=M[2],opacity=0.5))

fig.update_layout(
    autosize=False,
    scene=dict(
        xaxis=dict(nticks=4, range=[-10, 10], ),
        yaxis=dict(nticks=4, range=[-10, 10], ),
        zaxis=dict(nticks=4, range=[-10, 10], ), ),
    width=800,
    height=800,
    margin=dict(r=10, l=10, b=10, t=10))

fig.show()
