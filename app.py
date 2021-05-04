#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:05:05 2021

@author: sam
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.figure_factory as ff
import math 
import plotly.graph_objects as go
import pandas as pd
import scipy.stats as sc
import dash_bootstrap_components as dbc

#import functions in different pages
from navbar import Navbar
from homepage import Homepage
from sd import Sd_app, build_ex1
from ttest import ttest_app, build_ex2
from dataVis import dataVis_app, build_ex3
from sig import sig_app, build_bargraph_ex4, build_hist_ex4, build_expHyp_ex4

app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width,initial-scale=1.0,maximum-scale=1.2, minimum-scale=0.5,'}],
                            external_stylesheets=[dbc.themes.BOOTSTRAP])

#this is important and allows pages to differ and for items to be absent
app.config.suppress_callback_exceptions = True
server = app.server

#ger navigation bar
nav=Navbar()

#basically render output from functions embedded in each page
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

#functions for navigation
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return Homepage()
    elif pathname == '/sd':
        return Sd_app()
    elif pathname == '/ttest':
        return ttest_app()
    elif pathname == '/dataVis':
        return dataVis_app()
    elif pathname == '/sig':
        return sig_app()
    else:
        error=dbc.Jumbotron([
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P("The pathname was not recognised...")])
        return error 
    

#dynamic functions for sum of squares page
@app.callback(
    Output('output1', 'children'),
    [Input('ex1_mean', 'value'),Input('ex1_SD', 'value')]
)
def update_graph_ex1(mean,SD):
    graph,textBox = build_ex1(mean,SD)
    
    card1=dbc.Card([dbc.CardBody([graph])],
    color="light",  
    inverse=False,   
    outline=False,  
    )

    card2=dbc.Card([dbc.CardBody([textBox])],
    color="light",  
    inverse=False,   
    outline=False,  
    )

    ##Scale for all screen types so that each panel takes up the whole width of screen
    outCard=dbc.Row([dbc.Col(card1,xs=12,md=6,lg=6),
             dbc.Col(card2,xs=12,md=6,lg=6)])
    
    return outCard

#dynamic functions for t-test page
@app.callback(
    Output('output2', 'children'),
    [Input('ex2_mean1', 'value'),Input('ex2_mean2', 'value'),Input('ex2_SD', 'value')]
)
def update_graph_ex2(mean1,mean2,SD):
    graph,textBox = build_ex2(mean1,mean2,SD)
    
    card1=dbc.Card([dbc.CardBody([graph])],
    color="light",  
    inverse=False,   
    outline=False,  
    )
    
    card2=dbc.Card([dbc.CardBody([textBox])],
    color="light",  
    inverse=False,   
    outline=False,  
    )
    
    ##Scale for all screen types so that each panel takes up the whole width of screen
    outCard=html.Div(
        [dbc.Row(dbc.Col(card1,xs=12,md=12,lg=12)),
                  dbc.Row(dbc.Col(card2,xs=12,md=12,lg=12))])
    
    return outCard

#dynamic functions for data visualisation page
@app.callback(
    Output('output3', 'children'),
    [Input('ex3_mean1', 'value'),Input('ex3_mean2', 'value'),Input('ex3_SD', 'value'),Input('ex3_sampleSize', 'value')]
)
def update_graph_ex3(mean1,mean2,SD,sampleSize):
    graph1,graph2,graph3,graph4,pval,tval = build_ex3(mean1,mean2,SD,sampleSize)
    
    resultz="p-value =" + str(pval) + "\nt-value = " + str(tval)
    card1=dbc.Card([dbc.CardBody([html.P(resultz),graph1])],
    color="light",  
    inverse=False,   
    outline=False,  
    )

    card2=dbc.Card([dbc.CardBody([html.P(resultz),graph2])],
    color="light",  
    inverse=False,   
    outline=False,  
    )
    
    card3=dbc.Card([dbc.CardBody([html.P(resultz),graph3])],
    color="light",  
    inverse=False,   
    outline=False,  
    )
    
    card4=dbc.Card([dbc.CardBody([html.P(resultz),graph4])],
    color="light",  
    inverse=False,   
    outline=False,  
    )
    
    outCard= html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card1),xs=12,md=6,lg=3),
                dbc.Col(dbc.Card(card2),xs=12,md=6,lg=3),
                dbc.Col(dbc.Card(card3),xs=12,md=6,lg=3),
                dbc.Col(dbc.Card(card4),xs=12,md=6,lg=3),
            ]
    )])

    return outCard

#dynamic functions for significance testing page
@app.callback(
    Output('output4', 'children'),
    [Input('button1', 'n_clicks')]
)
def update_bargraph_ex4(clicks):
    
    graph1,textOut1 = build_bargraph_ex4(clicks)
    
    card1=dbc.Card([dbc.CardBody([textOut1,graph1])],
    color="light",  
    inverse=False,   
    outline=False,  
    )

    ##Scale for all screen types so that each panel takes up the whole width of screen
    outCard= html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card1),xs=12,md=6,lg=6)
               
            
            ]
    )])
    
    return outCard

@app.callback(
    Output('output5', 'children'),
    [Input('button2', 'n_clicks')]
)
def update_hist_ex4(clicks):
    
    graph2 = build_hist_ex4(clicks)
    
    card1=dbc.Card([dbc.CardBody([graph2])],
    color="light",  
    inverse=False,   
    outline=False,  
    )

    ##Scale for all screen types so that each panel takes up the whole width of screen
    outCard= html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card1),xs=12,md=6,lg=6)
                    
            ]
    )])
    
    return outCard

#nw bit
@app.callback(
    Output('output6', 'children'),
    [Input('ex4_mean1', 'value'),Input('ex4_mean2', 'value')]
)
def update_hist_ex4(ex4_mean1,ex4_mean2):
    
    graph3,graph4,textOut2 = build_expHyp_ex4(ex4_mean1,ex4_mean2)
    
    card1=dbc.Card([dbc.CardBody([textOut2,graph3])],
    color="light",  
    inverse=False,   
    outline=False,  
    )

    card2=dbc.Card([dbc.CardBody([graph4])],
    color="light",  
    inverse=False,   
    outline=False,  
    )

    outCard= html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card1),xs=6,md=6,lg=6),
                dbc.Col(dbc.Card(card2),xs=6,md=6,lg=6),
                
            ]
    )])
      
    
    return outCard

if __name__ == '__main__':
    app.run_server(debug=True)   