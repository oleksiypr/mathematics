import plotly.graph_objs as go
import numpy as np
from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

xs = np.linspace(-5, 5, 1000)
ys = np.linspace(-5, 5, 1000)

X, Y = np.meshgrid(xs, ys)
Z = X + 1j*Y

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=np.angle(Z))])
fig.update_layout(title='Riemann Surface', autosize=False,
                  width=1000, height=1000,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.write_html('riemann_v2.html', auto_open=True)
