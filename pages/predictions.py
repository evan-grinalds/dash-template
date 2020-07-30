# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        # Battery dropdown (60, 65, 70, 75, 80, 85, 90, 95, 100)
        dcc.Markdown('##### Battery (kwh)'), 
        dcc.Dropdown(
            id='battery', 
            options= [
                {'label': '60', 'value': 60},
                {'label': '65', 'value': 65},
                {'label': '70', 'value': 70},
                {'label': '75', 'value': 75},
                {'label': '80', 'value': 80},
                {'label': '85', 'value': 85},
                {'label': '90', 'value': 90},
                {'label': '95', 'value': 95},
                {'label': '100', 'value': 100},
            ],
            className = 'mb-3',
            value=0,
            placeholder='Select battery'
        ), 
        
        # Performance Type dropdown (Yes, No)
        dcc.Markdown('##### Ludacris Mode?'),
        dcc.Dropdown(
            id='ludacris_mode', 
            options= [
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0},
            ],
            className = 'mb-3',
            value=0,
            placeholder='Select performance'
        ),
        
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
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])
