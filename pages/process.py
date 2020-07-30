# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
           """
           I was curious which features influenced the price the most. As suspected, 
           the mileage was the most important factor followed by the year.
           """
        ),
        # Permutation Importance
        html.Img(src='assets/Screen Shot 2020-07-28 at 11.56.17 AM.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}), 
        dcc.Markdown(
            """ 
            This matrix shows exactly what mileage does to the price.
            """
        ),
        # Partial Dependence Plot
        html.Img(src='assets/Screen Shot 2020-07-28 at 12.00.22 PM.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
        dcc.Markdown(
            """
            If I had a budget of $40,000 then I would need to decide between an older 
            Model S or newer Model 3. My choice was the Model 3 because it has ludacris mode and 
            autopilot capabilities. That way I could take a quick nap during my commute.
            """
        ),
        # Conclusion
        html.Img(src='assets/Screen Shot 2020-07-29 at 6.09.38 PM.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}), 
      
        ],
)

layout = dbc.Row([column1])
