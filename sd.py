#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:52:06 2021

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



nav = Navbar()

text1=dcc.Markdown('''
                    
                    **Change the mean value here**
                 ''')
                 
text2=dcc.Markdown('''
                    **Change the standard deviation here**
                 ''')

slider1=dcc.Slider(
        id='ex1_mean',
        min=0,
        max=10,
        step=1,
        value=0,
        marks={0:'0',10:'10'},
    )

slider2=dcc.Slider(
        id='ex1_SD',
        min=0,
        max=10,
        step=1,
        value=5,
        marks={0:'0',10:'10'},
    )

output=html.Div(id = 'output1',
                children = [],
                )

lesson=dbc.Card([dbc.CardBody([dcc.Markdown('''
                    #### Sum of Squares, Variance and Standard Deviation ####   
                    Lots of people think that studying statistics is difficult. It's true that stats can sometimes be complicated, but stats are really just a way of simplifying data.
                    Imagine if you had to describe a set of data to another person without using any stats. How could you do it? You would probably just have to labouriously writing out every number. 
                    This would quickly become impossible with a large data set. Using stats provides a quick way of describing and drawing conclusions from data. 
                    &nbsp 
                    
                    If we wanted to describe our data to someone else, one thing we might use is a measure of central tendency. This is a way of describing the middle point of the data. Common measures 
                    include the mean (people call this the average, the sum of numbers divided by the number of numbers), 
                    the mode (the most frequently occuring number) or the median (the middle number when all the numbers are laid out in size order).
                    &nbsp 
                    
                    Telling people about the central number of a set of data only gets us so far though. It's also useful to know how spread out the numbers are. Note for example
                    that the mean of this set of numbers: **/10 10 10 10 10/** is identical to the mean for this set: **/12 8 14 6 10/** but the spread of values is obviously larger in the second set. 
                    So if we want to describe the set of numbers in more detail, we also need to provide a measure of spread. Note also that when the data has no spread at all, e.g. when all the numbers are the same
                    , the mean describes the set of numbers perfectly. As the numbers become more spread out, the mean becomes a less useful way of describing the numbers.
                    &nbsp 
                    
                    The sum of squares difference, variance and standard deviation are all measures of the spread of the data. The basis for all these measures is to
                    subtract each number in the set from the mean of the set of numbers. 
                    &nbsp
                    
                    In the sum of squares, the difference between the mean and each number in the set is squared and summed. Why do we square the numbers?  Because if we didn't the numbers would cancel themselves out when we summed them. The Sum of Squares is the 
                    basis for most parametric statistics. The variance is calculated by taking the mean of the sum of squares and the standard deviation by taking the squareroot of the variance.
                    By squarerooting the numbers we can undo the effect of squaring them during the sum of squares calculation. 
                    &nbsp
                    
                    There are two kind of standard deviation - the population and sample standard deviation. The population standard deviation is described above and should be calculated if you have 
                    sampled from all of the population for a measure, e.g. all the people in the world. For obvious reasons this is hard to do and rarely happens in psychology, so most often we 
                    use the sample standard deviation which takes into account the uncertainty of estimating the spread of data from a population from only a sample of that population by dividing the Sum of Squares by the number of numbers - 1. 
                    &nbsp
                    
                    Below is an illustration of how to calculate the spread of data. You can move the sliders to generate data with different properties. The data is shown by a scatterplot in which 
                    each value takes a numbered position on the y axis and the x axis represents the magnitude of that value. The blue dotted line corresponds to the mean of the set of numbers and the purple lines represent the deviation
                    of each value from the mean.
                    
                    **Exercise: Change the slides to see how it changes the calculation of the population standard deviation**   
                    * What happens to the plot when you increase the mean?  What happens when you decrease it?
                    * What happens to the plot when you increase the standard deviation?  What happens when you decrease it?
                    * Make up some numbers and calculate the population standard deviation for them using the dynamic textbox as a guide to how to do the calculation.  
                 ''')])],
                 color="dark",  
                 inverse=True,   
                 outline=False)

card1=dbc.Card([dbc.CardBody([text1,slider1,text2,slider2])],
    color="light",  
    inverse=False,   
    outline=False,  
)



body = dbc.Row([dbc.Col(card1,xs=12,md=12,lg=12)])

def Sd_app():
    layout = html.Div([
        nav,
        lesson,
        body,
        output
    ])
    
    return layout

 

def build_ex1(mean, SD):
    data=np.round(np.random.normal(mean,SD,10))

    graph=buildgraph_ex1(data)
    textBox=buildtext_ex1(data)
    
    
    return graph,textBox
    
def buildgraph_ex1(data):
    
    trueMean=np.mean(data)
    
    fig=px.scatter(x=data, y=[range(1,11,1)],range_x=[-20, 40],title='Scatter Plot')
    fig.add_shape(type="line", x0=trueMean, y0=1, x1=trueMean, y1=10,line=dict(color="Blue",width=4,dash="dashdot"))
    fig.layout.update(showlegend=False)
    fig.layout.update(height=500)
    
    for i in range(len(data)):
        fig.add_shape(type="line", x0=trueMean, y0=i+1, x1=data[i], y1=i+1,line=dict(color="Purple",width=4,dash="dashdot"))

    graph = dcc.Graph(figure = fig)
    
    return graph

def buildtext_ex1(data):
    trueMean=np.mean(data)
    
    returnText='The Values are: ' + str(data) + '\n' + '\n' + 'Population standard deviation:' + '\n\nStep 1. Calculate the mean (average):\n' + str(trueMean) + '\n\nStep 2. Subtract the mean from each value:\n' + str(data-trueMean) + \
        '\n\nStep 3. Square them:\n' + str(np.round((data-trueMean)**2,2)) + '\n\nStep 4: Sum them (Sum of Squares):\n' + str(round(sum((data-trueMean)**2),2)) + \
            '\n\nStep 5: Take the mean of the squared differences (Variance):\n' + str(round((sum((data-trueMean)**2))/len(data),2)) + '\n\nStep 6: Squareroot to undo the squaring (Population Standard Deviation):\n' + \
                 str(round(math.sqrt((sum((data-trueMean)**2))/len(data)),2)) 
    
    textBox = dcc.Textarea(value=returnText,
                           style={'width': '100%', 'height': '100%'},
                           rows=20)
    return textBox

