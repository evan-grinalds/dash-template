# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [   
        dcc.Markdown(
           """
           There were no easily accessible datasets for my topic, so I had to get creative. To create custom data, I used a Python’s 
           Beautiful Soup web scraping tutorial. Parsing the data from cars.com was easy because of their user-friendly API. 
           The values came out relatively clean because the script removed symbols and converted strings to integers. Finally, 
           I one-hot encoded the categorical features to numerical so I can fit a model.
            
           I observed that this was a supervised learning regression model as the target (price) was numerical. To get started, I 
           established a baseline by taking the mean of the data. If you saw a Model S driving down the street then this is how 
           you could guess it’s worth.
          
           With a few key features, I was confident that some machine learning techniques could accurately predict the price of a 
           given Tesla. Each method reduced the mean absolute error (MAE) to better predict the target (price). 
           
           1. Linear Regression was deployed to do a 80/20 split into training/validation. The split holds out the data from the testing 
           subset to prevent leakage. Leakage means it is overfit and fit too good to be true. It is used to minimize the residual 
           sum of squares between the observed targets in the dataset and the targets predicted by the linear approximation.

           2. Ridge Regression found a new line that didn’t fit the training data as well. In other words, it introduced a small amount 
           of bias into how the new line fit to the data. But in return for that small amount of bias, we get a significant drop in 
           variance. By starting with a slightly worse fit, it can provide better long-term predictions.

           3. XG Boost (eXtreme Gradient Boosting) was used because it is engineered for efficiency of compute time and memory resources. 
           It does this by using a block structure to support the parallelization of tree construction.

           4. Random Forest scored the most accurate because each decision tree trained on a random bootstrap sample of the data. 
           This type of ensembling is called “bagging.” Each split considered a random subset of the features.
            """
        ),
        # Baseline
        html.Img(src='assets/carbon (1).png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
        # Machine Learning
        html.Img(src='assets/carbon (2).png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}), 
        ],
)

layout = dbc.Row([column1])
