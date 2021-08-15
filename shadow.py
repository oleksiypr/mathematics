import plotly.graph_objs as go
import numpy as np


t = np.linspace(0, 20, 100)
x, y, z = np.cos(t), np.sin(t), t

R = np.array((x, y, z))
s = np.array([1., 1., -2])

A = np.array([
    [1., 0., -s[0]/s[2]],
    [0., 1., -s[1]/s[2]],
    [0., 0.,         0.]
])

R1 = A @ R

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

fig.update_layout(
    autosize=False,
    scene=dict(
        xaxis=dict(nticks=4, range=[-10, 10],),
        yaxis=dict(nticks=4, range=[-10, 10],),
        zaxis=dict(nticks=4, range=[  0, 20],),),
    width=800,
    height=800,
    margin=dict(r=20, l=10, b=10, t=10))


fig.show()
