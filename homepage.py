#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:21:42 2021

@author: sam
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

##Function for returning rendered page with contents
def Homepage():
    layout = html.Div([
        nav,
        body,
        ])
    return layout

##Add the navigation bar
nav = Navbar()

##Text#############
text1=dcc.Markdown('''
                    ### Lesson 1: Variance, standard deviation, t-tests and probability distributions###  
                    
                 **Learning Outcomes:**
                 * To understand how the concept of the sum of squares and how this relates to variance and standard deviation.
                 * To understand how the independent samples t-test is calculated.
                 * To understand how means and standard deviations affect statistical significance.
                 * To understand some of the positives and negatives of different kinds of plots.
                 * To understand the concept of probability distributions and how they are used to derive p-values.
                 
                 ''')
                 
text2=dcc.Markdown('''
                    **Welcome to this lesson!**   
                    &nbsp
                    
                    Click on the tabs in the top right to start your learning.   
                    &nbsp 
                    
                    These materials were created by S.Evans1@westminster.ac.uk. Feel free to use these materials in your teaching and learning.   
                    Please let me know if you have any feedback at the above email address.   
                 ''')
####################

##Make cards for text                
card1=dbc.Card([dbc.CardBody([text1])],
    color="dark",  
    inverse=True,   
    outline=False,  
)

card2=dbc.Card([dbc.CardBody([text2])],
    color="light",  
    inverse=False,   
    outline=False,  
)

##Scale for all screen types so that each panel takes up the whole width of screen
body = dbc.Row([dbc.Col(card1,xs=12,md=12,lg=12),
             dbc.Col(card2,xs=12,md=12,lg=12)])
                             
##initialise 
app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width,initial-scale=1.0,maximum-scale=1.2, minimum-scale=0.5,'}],
                            external_stylesheets=[dbc.themes.BOOTSTRAP])

##use homepage function to create page layout
app.layout=html.Div(Homepage())


if __name__ == "__main__":
    app.run_server(debug=True, port=8889)