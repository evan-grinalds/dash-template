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
        
        html.Div(  
            [
        dcc.Markdown('##### Mileage'), 
        daq.Slider(              
            id='mileage', 
            min=10000, 
            max=100000, 
            step=None,  
            marks={
                10000: '10000',
                20000: '20000',
                30000: '30000',
                40000: '40000',
                50000: '50000',
                60000: '60000',
                70000: '70000',
                80000: '80000',
                90000: '90000',
                100000: '100000',
                }, 
            value=5,
            className='mb-4',
            handleLabel={
                'label': 'Current',
                'showCurrentValue': True
                },
            ),
            ],
            style={'marginTop': 15, 'marginBottom': 15},            
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])
