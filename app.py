import dash
import dash_bootstrap_components as dbc

"""
https://github.com/facultyai/dash-bootstrap-components

dash-bootstrap-components provides Bootstrap components.

Plotly Dash is great! However, creating the initial layout can require a lot 
of boilerplate. dash-bootstrap-components reduces this boilerplate by providing 
standard layouts and high-level components.

A good way to start customising the stylesheet is to use an alternative 
pre-compiled theme. Bootswatch is a great place to find new themes. Links to 
CDNs for each of the Bootswatch styles are also included , and can be used 
with the external_stylesheets argument of the Dash constructor:

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

Go to https://bootswatch.com/ to preview these Bootswatch themes:

dbc.themes.BOOTSTRAP
dbc.themes.CERULEAN
dbc.themes.COSMO
dbc.themes.CYBORG
dbc.themes.DARKLY
dbc.themes.FLATLY
dbc.themes.JOURNAL
dbc.themes.LITERA
dbc.themes.LUMEN
dbc.themes.LUX
dbc.themes.MATERIA
dbc.themes.MINTY
dbc.themes.PULSE
dbc.themes.SANDSTONE
dbc.themes.SIMPLEX
dbc.themes.SKETCHY
dbc.themes.SLATE
dbc.themes.SOLAR
dbc.themes.SPACELAB
dbc.themes.SUPERHERO
dbc.themes.UNITED
dbc.themes.YETI
"""

external_stylesheets = [
    dbc.themes.DARKLY, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True # see https://dash.plot.ly/urls
app.title = 'Tesla Predictor' # appears in browser title bar
server = app.server

# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
