import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

# Read in data with two headers

df = pd.read_csv('building_one.csv', header=[0,1], index_col=0)

# Extract energy series from multi-index
energy_series = df.loc[:, ('Energy', '3')]

# Plot
energy_data = go.Scatter(x=energy_series.index,
                         y=energy_series.values)

layout = go.Layout(title='Energy Plot',
                   xaxis=dict(title='Date'),
                   yaxis=dict(title='(kWh)'))

fig = go.Figure(data=[energy_data], layout=layout)
fig.write_html('energy_plot.html', auto_open=True)