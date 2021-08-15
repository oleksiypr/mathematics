import plotly.graph_objs as go
import numpy as np
import numpy.linalg as la


t = np.linspace(0, 20, 100)
x, y, z = np.cos(t), np.sin(t), t

R = np.array((x, y, z))

A = np.array([
    [1., 0., 0.],
    [0., 1., 1.],
    [0., 0., 0.]
])

R1 = A @ R

fig = go.Figure()

'''
fig_orig = go.Figure(data=go.Scatter3d(x=x, y=y, z=z))

fig_shadow = go.Figure(
    data=go.Scatter3d(
        x=R1[0, :],
        y=R1[1, :],
        z=R1[2, :]
    )
)
'''
# tight layout

fig.add_trace(
    go.Scatter3d(
        x=R1[0, :],
        y=R1[1, :],
        z=R1[2, :]
    ))


fig.add_trace(go.Scatter3d(x=x, y=y, z=z))

# fig = fig_shadow
fig.update_layout(
    autosize=False,
    xaxis=go.layout.XAxis(
      range=[-150, 150],
      showgrid=True,
      zeroline=True,
      showline=True,
      gridcolor='#bdbdbd',
      gridwidth=2,
      zerolinecolor='#969696',
      zerolinewidth=4,
      linecolor='#636363',
      linewidth=6
    ),
    yaxis=go.layout.YAxis(
      range=[-150, 150],
      showgrid=True,
      zeroline=True,
      showline=True,
      gridcolor='#bdbdbd',
      gridwidth=2,
      zerolinecolor='#969696',
      zerolinewidth=4,
      linecolor='#636363',
      linewidth=6
    ),
    height=600,
    width=600,
)

fig.show()
