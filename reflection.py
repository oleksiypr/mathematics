import plotly.graph_objs as go
import numpy as np
from numpy.linalg import inv

theta_degrees = 60.
theta = np.radians(theta_degrees)

E = np.array([
    [1.,            0.,             0.],
    [0., np.cos(theta), -np.sin(theta)],
    [0., np.sin(theta),  np.cos(theta)]
])

TE = np.array([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., -1.]
])

T = E @ TE @ inv(E)

t = np.linspace(0, 20, 100)
x, y, z = np.cos(t), np.sin(t) - 2.0, t

R = np.array((x, y, z))
R1 = T @ R

# mirror plane
'''
x1 = np.linspace(-10., 10., 5)
y1 = np.linspace(-10., 10., 5)
z1 = np.zeros(5)
M1 = np.array((x1, y1, z1))
M = E @ M1
'''

fig = go.Figure()

fig.add_trace(
    go.Scatter3d(
        x=R1[0, :],
        y=R1[1, :],
        z=R1[2, :],
        mode="lines"
    ))


fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode="lines"
))


X, Y = np.meshgrid(
    np.linspace(-10., 10., 5),
    np.linspace(- 0., 10., 5)
)

fig.add_trace(go.Surface(
    x=X,
    y=Y,
    z=Y * np.tan(theta),
    opacity=0.5
))


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
