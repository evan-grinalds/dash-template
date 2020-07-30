# Imports from 3rd party libraries
import dash
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        # Drivetrain dropdown (Yes, No)
        dcc.Markdown('##### All-Wheel Drive?'), 
        dcc.Dropdown(
            id='all_wheel_drive', 
            options= [
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0},
            ],
            className = 'mb-3',
            value=0,
            placeholder='Select All-Wheel Drive'
        ), 
    # Year
        html.Div(  
            [
        dcc.Markdown('##### Year'), 
        daq.Slider(              
            id='age', 
            min=2012, 
            max=2020, 
            step=None,  
            marks={
                2012: '2012',
                2013: '2013',
                2014: '2014',
                2015: '2015',
                2016: '2016',
                2017: '2017',
                2018: '2018',
                2019: '2019',
                2020: '2020',
                }, 
            value=5,
            className='mb-4',
            handleLabel={
                'label': 'Current',
                'showCurrentValue': False
                },
            ),
            ],
            style={'marginTop': 15, 'marginBottom': 15},            
        ),
    ],
    md = 6,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])
