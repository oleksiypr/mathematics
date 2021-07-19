import plotly.graph_objs as go
import numpy as np
from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

Phi, R = np.mgrid[0:4*np.pi:100j, -5.:5.:100j]
X, Y = (R * np.cos(Phi), R * np.sin(Phi))

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Phi)])
fig.update_layout(title='Riemann Surface', autosize=False,
                  width=1000, height=1000,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.write_html('riemann_v2.html', auto_open=True)
