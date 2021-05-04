#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:16:05 2021

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

#get navigation bar
nav = Navbar()

#make basic features for the page that provide inputs to the dynamic functions or are static
text1=dcc.Markdown('''
                   
                    **Change the mean value here for group 1**
                 ''')
                 
text2=dcc.Markdown('''
                    **Change the mean value here for group 2**
                 ''')
                 
text3=dcc.Markdown('''
                    **Change the standard deviation here**
                 ''')

slider1=dcc.Slider(
        id='ex2_mean1',
        min=0,
        max=3,
        step=0.1,
        value=0,
        marks={0:'0',3:'3'},
    )

slider2=dcc.Slider(
        id='ex2_mean2',
        min=0,
        max=3,
        step=0.1,
        value=2,
        marks={0:'0',3:'3'},
    )

slider3=dcc.Slider(
        id='ex2_SD',
        min=0,
        max=3,
        step=0.1,
        value=0.5,
        marks={0:'0',3:'3'},
    )

#specify outputs from dynamic functions
output=html.Div(id = 'output2',
                children = [],
                )

lesson=dbc.Card([dbc.CardBody([dcc.Markdown('''
                    #### How the t-statistic is calculated and why changing the means and standard deviations matters ####   
                    We can rarely extract the data from every person in a population. This would take a massive amount of resources. So instead we have to extract smaller samples of that population.
                    Using those samples we can hope to draw conclusions about the population from which those smaller samples are taken. Imagine we wanted to know whether musicians were better at listening
                    to speech in noisy environments (given that they have so much experience of listening to music) compared to people who are not musicians. It would be impossible to recruit all the musicians in the UK or the world. 
                    So, the first step would be to recruit a sample of musicians and a sample of non-musicians and to compare their scores on a listening experiment. It's easy to see that if we did this a few times the mean scores and standard deviation of each sample would be
                    different for every sample. As the scores would differ for every set of samples, how would we know whether this represented an important (a significant) difference or was just part of the natural variation that occurs from taking different samples from these broader populations?
                    &nbsp 
                    
                    This is where inferential statistics come in. It gives us a way of deciding whether any difference that we observe from our samples represents a real difference between the two populations from which the samples were drawn.
                    How do we do that? Most parametric statistical tests (like t-tests and ANOVA) work by calculating a ratio of the size of the experimental manipulation (usually the difference between the means) divided by a measure of the spread of the data. 
                    &nbsp 
                    
                    For an independent samples t-tests we calculate the t-statistic. This is the difference between the means of the two groups divided by the pooled standard error (the total spread of the values taking into account the number of participants in the samples). 
                    As it is a ratio, if the value on the top of the equation (e.g. difference between the means) is large and the spread of the values is small, this will give a large t-statistic.  The reverse is true if the size of the difference is small and the spread of values is large.  
                    For a simple example: 3/1  = 3 whereas 1/3 = 0.33.
                    &nbsp
                    
                    Why is it a ratio?  It's obvious that a large difference between the means of the samples is more likely to indicate that there is a real difference between the two populations from which the values were taken. So it makes sense that this goes on the top of the equation.
                    Why do we put an estimate of the spread of the data on the bottom of the equation?  One way of thinking about this is that the mean is a less accurate summary of the data when there is a greater spread of values - so we can be less confident
                    in the difference between the means. Another way to think about it is that the less spread of values in the data, the less the values of one group overlap with the values of the other group.  By putting the estimate of the spread on the bottom of the equation it helps to scale (reduce) the influence of the 
                    size of the difference in means on the t-statistic.
                    
                     **Exercise: Change the sliders to see how it affects the t-statistic calculation**   
                    * What happens to the t-values when you increase the difference between the means (keep the standard deviation the same)?  What happens when you decrease it?
                    * What happens to the t-values when you fix the difference between the means but vary the standard deviation? What happens when you increase the standard deviation?  What happens when you decrease it?
                    * Make up some numbers and calculate the t-test by hand using the dynamic textbox as a guide to how to do the calculation.  

                    
                 ''')])],
                 color="dark",  
                 inverse=True,   
                 outline=False)

#add all elements into a single card
card1=dbc.Card([dbc.CardBody([text1,slider1,text2,slider2,text3,slider3])],
    color="light",  
    inverse=False,   
    outline=False,  
)

#create body element - concatenate all input and static elements
body = dbc.Row([dbc.Col(card1,xs=12,md=12,lg=12)])

#function for rendering the page including the output from the dynamic functions
def ttest_app():
    layout = html.Div([
        nav,
        lesson,
        body,
        output
    ])
    
    return layout

def build_ex2(mean1, mean2, SD):
    #generate data
    data1=np.round(np.random.normal(mean1,SD,30))
    data2=np.round(np.random.normal(mean2,SD,30))
    
    #build dynamic objects
    graph=buildgraph_ex2(data1,data2)
    textBox=buildtext_ex2(data1,data2)
    
    return graph,textBox

def buildgraph_ex2(data1,data2):
    
    #make figure
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(mode='markers',x=data1,marker=dict(color='Blue')))
    fig1.add_trace(go.Scatter(mode='markers',x=data2,marker=dict(color='Red')))
    fig1.add_shape(type="line", x0=np.mean(data1), y0=1, x1=np.mean(data1), y1=30,line=dict(color="Blue",width=4,dash="dashdot"))
    fig1.add_shape(type="line", x0=np.mean(data2), y0=1, x1=np.mean(data2), y1=30,line=dict(color="Red",width=4,dash="dashdot"))
    
    fig1.update_layout(barmode='overlay')
    fig1.update_layout(xaxis_range=[-10,10])
    fig1.update_traces(opacity=0.7)
    fig1.layout.update(showlegend=False)
    fig1.layout.update(height=400)
    
    #same length so just looping for data1
    for i in range(len(data1)):
        fig1.add_shape(type="line", x0=np.mean(data1), y0=i, x1=data1[i], y1=i,line=dict(color="Purple",width=4,dash="dashdot"))
        fig1.add_shape(type="line", x0=np.mean(data2), y0=i, x1=data2[i], y1=i,line=dict(color="Orange",width=4,dash="dashdot"))
    
    #make into a dcc object
    graph = dcc.Graph(figure = fig1)
    
    return graph

def buildtext_ex2(data1,data2):
    
    #run t-test
    result=sc.ttest_ind(data1,data2)
    
    #format values of test to be more readable
    pval=round(result[1],4)
    if pval == 0:
        pval='p < 0.0001'
    tval=str(round(result[0],4))
    
    #calculate t-test 'by hand' for each element for the textbox
    mean1=np.mean(data1)
    mean2=np.mean(data2)
    ss1=sum((data1-np.mean(data1))**2)
    ss2=sum((data2-np.mean(data2))**2)
    dfs=len(data1)-1+len(data2)-1
    totalSS=ss1+ss2
    ser=totalSS/dfs
    com=math.sqrt((ser/len(data1))+(ser/len(data2)))
    
    returnText=generateText(tval,pval,data1,data2,dfs,ss1,ss2,com,totalSS,mean1,mean2)
                                                                        
    textBox = dcc.Textarea(value=returnText,style={'width': '100%', 'height': '100%'},rows=25)
    return textBox

def generateText(tval,pval,data1,data2,dfs,ss1,ss2,com,totalSS,mean1,mean2):
    
    #return the text
    returnText='The T value is: ' +  tval + ' and the associated p value is: ' + str(pval) + \
            '\n\n Values for Group 1: ' + str(data1) + \
            '\n\n Values for Group 2: ' + str(data2) + \
                '\n\nHow did we calculate this t-value?' + \
                    '\n\nFirst, we calculate the pooled standard error, this takes a few steps ...' + \
                        '\n\nCalculate the Sum of Squares for group 1: ' + str(np.round(((data1-mean1)**2),2)) + ' = ' + str(round(ss1,2)) + \
                            '\n\nCalculate Sum of Squares for group 2: ' + str(np.round(((data2-mean2)**2),2)) + ' = ' + str(round(ss2,2)) + \
                                '\n\nAdd the the sum of squares for each group: ' + str(round(ss1,2)) + ' + ' + str(round(ss2,2)) + ' = ' + str(round(totalSS,2)) + \
                                    '\n\nCalculate the degrees of freedom (number of participants -1 in each group): ' + str(len(data1)) + '-1 + ' + str(len(data2)) + '-1 = ' + str(dfs) + \
                                        '\n\nDivide the total sum of squares by degrees of freedom: ' + str(round(totalSS,2)) + ' / ' + str(dfs) + ' = ' + str(round(com,2)) + \
                                            '\n\nWell done! You calculated the pooled standard error: ' + str(round(com,2)) + \
                                                '\n\nFinally we can calculate the T-Value by dividing the difference between the means by the pooled standard error' + \
                                                    '\n\nt-value = (mean1-mean2)/pooled standard error : (' + str(round(mean1,2)) + ' - ' + str(round(mean2,2)) + ') / ' + str(round(com,2)) + ' = ' + str(round((mean1-mean2)/com,2))

    return returnText
