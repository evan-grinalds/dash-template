import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### Wanna go electric?

            More electric cars are on the road everyday. This makes you wonder, 
            can I afford one? This application answers that question by 
            predicting which model has the best value.
            
            """
        ),
        dcc.Link(dbc.Button('Predict Price', color='primary'), href='/predictions')
    ],
    md=4,
    align='center'
)

column2 = dbc.Col([html.Img(src='assets/model3.jpeg', className='img-fluid')
],
align='center'
)

layout = dbc.Row([column1, column2])
