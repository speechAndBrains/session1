#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:25:02 2021

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
from navbar import Navbar

import scipy.stats as sc

nav = Navbar()

text1=dcc.Markdown('''
                      
                    **Change the mean value here for group 1**   
                       
                 ''')
                 
text2=dcc.Markdown('''
                    **Change the mean value here for group 2**
                 ''')
                 
text3=dcc.Markdown('''
                    **Change the standard deviation here**
                 ''')
                 
text4=dcc.Markdown('''
                    **Change the sample size here**
                 ''')

slider1=dcc.Slider(
        id='ex3_mean1',
        min=0,
        max=3,
        step=0.1,
        value=0,
        marks={0:'0',3:'3'},
    )

slider2=dcc.Slider(
        id='ex3_mean2',
        min=0,
        max=3,
        step=0.1,
        value=4,
        marks={0:'0',3:'3'},
    )

slider3=dcc.Slider(
        id='ex3_SD',
        min=0,
        max=3,
        step=0.1,
        value=1,
        marks={0:'0',3:'3'},
    )

slider4=dcc.Slider(
        id='ex3_sampleSize',
        min=0,
        max=1000,
        step=5,
        value=100,
        marks={0:'0',1000:'1000'},
    )

output=html.Div(id = 'output3',
                children = [],
                )


lesson=dbc.Card([dbc.CardBody([dcc.Markdown('''
                    #### Data Visualisation ####   
                    There are lots of different ways to present data. Below are four graphs that all show the same data. Each type of graph has different advantages and disadvantages. 
                    &nbsp 
                    
                    Scatterplots and histograms are good for showing raw data. However, on their own they can sometimes be hard to interpret. It can often be difficult to ascertain whether there are reliable differences between the distributions from these plots. 
                    &nbsp 

                    Bargraphs show the mean and the errorbars show how variable the data is around those mean values. This can be quite useful: when the errorbars do not overlap between the groups this often indicates that there is a significant difference between the means of the groups. 
                    It's worth noting though that means and errorbars can be strongly affected by outliers and outliers aren't shown on bargraphs. Parametric statistical tests (e.g. t-tests, ANOVAs etc.) assume that the data do not have significant outliers. So it can be difficult to know from looking at the plot
                    whether the assumptions of the test have been met.  For this reason, they are not very transparent and are not favoured by everyone.
                    &nbsp 
                    
                    Boxplots are a nice balance as they show the median of the data (the line across the middle of the box) and useful information about the
                    distribution of values and outliers. To make a boxplot the data is ranked in magnitude and seperated into four parts.  These are called quartiles.  The middle box accounts for middle 
                    50% of the data.  Outliers are shown by circles outside of the whiskers (the lines connected to the boxes). 
                    &nbsp 
                    
                    More recently researchers have been combining different plots, e.g. adding scatter plots to bargraphs, so that the raw data is presented as well as the summarised data.  
                    &nbsp 
                    
                    **Exercise: Play around with sliders and see how the visualisations are affected by different kinds of data**
                    * Which visualisations do you prefer and why?
                    * Which Visualisations provide the most information about the data?
                    * Which are simplest to understand and interpret the statistical result from?
                 ''')])],
                 color="dark",  
                 inverse=True,   
                 outline=False)

card1=dbc.Card([dbc.CardBody([text1,slider1,text2,slider2,text3,slider3,text4,slider4])],
    color="light",  
    inverse=False,   
    outline=False,  
)



body = dbc.Row([dbc.Col(card1,xs=12,md=12,lg=12)])

def dataVis_app():
    layout = html.Div([
        nav,
        lesson,
        body,
        output
    ])
    
    return layout

def build_ex3(mean1, mean2, SD,sampleSize):
    data1=np.random.normal(mean1,SD,sampleSize)
    data2=np.random.normal(mean2,SD,sampleSize)
    
    graph1,graph2,graph3,graph4=buildgraph_ex3(data1,data2)
   
    result=sc.ttest_ind(data1,data2)
    
    pval=round(result[1],4)
    if pval == 0:
        pval='p < 0.0001'
    tval=str(round(result[0],4))
    
    return graph1,graph2,graph3,graph4,pval,tval

def buildgraph_ex3(data1,data2):
    
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(mode='markers',x=data1,marker=dict(color='Blue')))
    fig1.add_trace(go.Scatter(mode='markers',x=data2,marker=dict(color='Red')))
    fig1.add_shape(type="line", x0=np.mean(data1), y0=1, x1=np.mean(data1), y1=100,line=dict(color="Blue",width=4,dash="dashdot"))
    fig1.add_shape(type="line", x0=np.mean(data2), y0=1, x1=np.mean(data2), y1=100,line=dict(color="Red",width=4,dash="dashdot"))
    
    
    fig1.update_layout(barmode='overlay')
    fig1.update_layout(xaxis_range=[-10,10])
    fig1.update_traces(opacity=0.7)
    fig1.layout.update(showlegend=False)
    fig1.update_layout(title_text='Scatter Plot')
    graph1 = dcc.Graph(figure = fig1)
    
    fig2=go.Figure()
    fig2.add_trace(go.Histogram(x=data1,name='Group 1'))
    fig2.add_trace(go.Histogram(x=data2,name='Group 2'))
    fig2.update_layout(barmode='overlay')
    fig2.update_traces(opacity=0.7)
    fig2.update_layout(title_text='Histogram')
    graph2 = dcc.Graph(figure = fig2)
    
    
    fig3 = go.Figure()
    fig3.add_trace(go.Box(y=data1,name='Group 1'))
    fig3.add_trace(go.Box(y=data2,name='Group 2'))
    fig3.update_layout(title_text='Boxplot')
    graph3 = dcc.Graph(figure = fig3)
    

    mult=sc.t.ppf((1 + 0.95)/2,len(data1)-1)
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(
    name='Control',
    x=['Group 1', 'Group 2'], y=[np.mean(data1), np.mean(data2)],
    error_y=dict(type='data', array=[sc.sem(data1)*mult,sc.sem(data2)*mult])
    ))
    fig4.update_layout(title_text='Bargraph with Errorbars')
    graph4 = dcc.Graph(figure = fig4)
    
    return graph1,graph2,graph3,graph4