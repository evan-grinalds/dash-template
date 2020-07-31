# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
search = load('assets/Tesla_Model_Final.pkl')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [   
         # Vehicle Type dropdown (Yes, No)
        dcc.Markdown('##### Vehicle'),
        dcc.Dropdown(
            id='vehicle', 
            options= [
                {'label': 'Tesla Model S', 'value': 1},
            ],
            className = 'mb-3',
            value=0,
            placeholder='Select vehicle'
        ),
        
        # Year dropdown (2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020)
        dcc.Markdown('##### Year'), 
        dcc.Dropdown(
            id='year', 
            options= [
                {'label': '2012', 'value': 2012},
                {'label': '2013', 'value': 2013},
                {'label': '2014', 'value': 2014},
                {'label': '2015', 'value': 2015},
                {'label': '2016', 'value': 2016},
                {'label': '2017', 'value': 2017},
                {'label': '2018', 'value': 2018},
                {'label': '2019', 'value': 2019},
                {'label': '2020', 'value': 2020},   
            ],
            className = 'mb-3',
            value=0,
            placeholder='Select year'
        ), 
        
        # Miles dropdown (20000, 40000, 60000, 80000, 100000, 120000)
        dcc.Markdown('##### Mileage'), 
        dcc.Dropdown(
            id='mileage', 
            options= [
                {'label': '20000', 'value': 20000},
                {'label': '40000', 'value': 40000},
                {'label': '60000', 'value': 60000},
                {'label': '80000', 'value': 80000},
                {'label': '100000', 'value': 100000},
                {'label': '120000', 'value': 120000},
            ],
            className = 'mb-3',
            value=0,
            placeholder='Select mileage'
        ), 
        
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
        dcc.Markdown('##### Ludacris Mode'),
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
        dcc.Markdown('##### All-Wheel Drive'), 
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
        html.H2('Price Prediction', className= 'mb-3'),
        html.Div(id='prediction-content', className='lead'),
        html.Div(id='image')
    ],
    md=6,
)
layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [
    Input('year', 'value'),
    Input('car', 'value'),
    Input('battery', 'value'),
    Input('ludacris_mode_Yes', 'value'),
    Input('ludacris_mode_No', 'value'),
    Input('all_wheel_drive_Yes', 'value'),
    Input('all_wheel_drive_No', 'value'),
    Input('mileage', 'value')   
    ],
)
def predict(year, car, battery, ludacris_mode_Yes, ludacris_mode_No, all_wheel_drive_Yes, all_wheel_drive_No, mileage):
    df = pd.DataFrame(
        columns=['year', 'car', 'battery', 'ludacris_mode_Yes', 'ludacris_mode_No', 'all_wheel_drive_Yes', 'all_wheel_drive_No', 'mileage'],
        data=[[year, car, battery, ludacris_mode_Yes, ludacris_mode_No, all_wheel_drive_Yes, all_wheel_drive_No, mileage]]
    )
    y_pred=search.predict(df)[0]
    return y_pred
