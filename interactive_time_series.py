import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
from datetime import datetime

init_notebook_mode(connected=True)

# Read in data and convert index to a datetime
df = pd.read_csv('building_one.csv', header=[0, 1], index_col=0)
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)

# Extract series from multi-index
energy_series = df.loc[:, ('Energy', '3')].copy()
steam_series  = df.loc[:, ("Steam" , "4")].copy()

# Plot
energy_data = go.Scatter(x=energy_series.index,
                         y=energy_series.values)

steam_data = go.Scatter(x=steam_series.index,
                        y=steam_series.values,
                        yaxis='y2')


layout_steam_energy = go.Layout(height=600, width=800,
                                title='Energy and Steam Plot',
                                xaxis=dict(title='Date'),
                                yaxis=dict(title='Energy', color='red'),
                                yaxis2=dict(title='Steam',
                                            color='blue',
                                            overlaying='y',
                                            side='right')
                                )

fig_steam_energy = go.Figure(data=[energy_data, steam_data], layout=layout_steam_energy)
fig_steam_energy.write_html('energy_steam_plot.html', auto_open=True)


# Create a list of annotations
df_short = df.loc[pd.Int64Index(df.index.isocalendar().week) == 5].copy()
steam_series_four = df_short.loc[:, ('Steam', '4')].copy()


def find_daily_maxes(x):
    """Return maximum measurement on each day and when it occurred in a dataframe"""
    x = x.copy().to_frame()
    x['day'] = x.index.day
    result =pd.concat([x.groupby('day').max(),
                      x.groupby('day').idxmax()], axis = 1).iloc[:, [0, 1]]
    result.columns = ['value', 'date']
    return result.set_index('date')


four_highs = find_daily_maxes(steam_series_four)


def format_time(dt):
    if pd.isnull(dt):
        return "NaT"
    else:
        return datetime.strftime(dt, "%a <br> %H:%M %p")


four_annotations = [dict(x = date, y = value[0],
                         xref = 'x', yref = 'y',
                         font=dict(color = 'blue'),
                         text = f'{format_time(date)}<br> {value[0]:.1f} Mlbs/hr')
                    for date, value in zip(four_highs.index, four_highs.values)]

# Create a data for annotations
steam_data_four = go.Scatter(
    x=steam_series_four.index,
    y=steam_series_four.values,
    line=dict(color='blue', width=1.1),
    opacity=0.8,
    name='Steam: Sensor 4',
    hoverinfo='text',
    text=[f'Sensor 4: {x:.1f} Mlbs/hr' for x in
          steam_series_four.values])

layout_steam_annotations = go.Layout(height=800, width=1000,
                   title='Steam Sensor with Daily High Annotations',
                   annotations=four_annotations)

fig_steam_annotations = go.Figure(data = [steam_data_four],
                layout=layout_steam_annotations)
fig_steam_annotations.write_html('steam_annotations_plot.html', auto_open=True)
