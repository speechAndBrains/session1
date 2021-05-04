#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:01:59 2021

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

lesson=dbc.Card([dbc.CardBody([dcc.Markdown('''
                    #### Understanding probability distributions through simulation ####   
                    In the t-test tab, you saw how the t-statistic or t-value is calculated. How do we get from a t-value to a p-value? And what does a p-value mean? 
                    &nbsp 
                    
                    For an independent samples t-test, the p-value is a measure of how likely it is that we would get a t-value as extreme as the one that we observed if the null hypothesis was true, e.g. if the means of the two groups don't really differ.
                    We often use a criterion of p < 0.05 as evidence that the means of two groups differ. This reflects the fact that we would only expect to get a difference as large as the difference that we found 5 times in every 100 tests we conducted. If we only conducted
                    one test, it would be unlikely that we would get a value this large, so we say it is "significant" and conclude that it is unlikely that there is no difference between the groups. This is called rejecting the null hypothesis. Indeed, 95 times in every 100, we wouldn't expect to get a value this large, so it's a suprisingly large difference..
                    &nbsp 
                    
                    How do we know what t-values we would expect if there was no difference between the groups? Well, statisticians have calculated the distribution of t-values you would expect if there was no difference between the groups. How did they do this? Likely using a combination of mathematical proofs and voodoo! You can compare your t-value to these numbers
                    to see whether the number you found was unlikely or not to belong to this null distribution. The shape of these distributions depend on the number of participants.
                    &nbsp 
                    
                    Perhaps the easiest way to prove to yourself that the statisticians got their sums right and to understand the logic behind these kinds of "inferential statistics" is to use a random number generator to construct a null distribution. We can use a random number generator to extract 
                    two different samples from the same population, a population of scores with a specified mean value. We know that there is no true difference between different samples taken from the same population (with the same mean). We can calculate the t-value from comparing these two samples.
                    If we do this a large number of times (e.g. 1000 times) we can build a histogram of the null distribution. We can then compare the t-value from samples to see if the difference is similar to the difference we would expect from the null distribution or not. If the value is very extreme 
                    compared to the null distribution we can assume the data are drawn from two different populations not the same population, e.g. we can reject the null hypothesis, and conclude that the samples are drawn from different distributions.
                   
                    
                 ''')])],
                 color="dark",  
                 inverse=True,   
                 outline=False)
                               
text1=dcc.Markdown('''
                    ##### Extract two samples from the same underlying distribution of values #####  
                    Using random number generators we can generate numbers with specific properties. If we extract two different, smaller samples from a distribution
                    with a specific mean, we would assume that the mean of the two different samples should be similar to one another. This is true, however, the difference between
                    the values changes each time we extract a different sample because of chance. Most of the time the difference in means between the samples
                    is very small (around 0). Every once and a while, that isn't the case and the difference is larger. We know however that the numbers were drawn from the same population
                    so there is no fundamental difference between the samples. Most of the time the mean difference will be around zero.
                    
                    **Exercise: Press button to extract two samples from the same distribution and run a t-test on the data **
                    * What would you expect the difference between the means to be?
                    * What would you expect the t-value to be?
                    * What would you expect the p-value to be?
                    * Press the button a few times, did you get any p-values < 0.05? (n.b. every once and a while you will find a value < 0.05, why?)
                 ''')

button1=html.Button('Go!',
                    id='button1',
                    n_clicks=0)

card1=dbc.Card([dbc.CardBody([text1,button1])],
    color="light",  
    inverse=False,   
    outline=False,
    )

body1 = dbc.Row([dbc.Col(card1,xs=12,md=12,lg=12)])

output1=html.Div(id = 'output4',
                children = [],
                )

text2=dcc.Markdown('''
                    ##### Generate a null distribution with a random number generator #####  
                    Using simulation is a good way to understand how probability distributions work. You are about to generate a null distribution by extracting
                    a 1000 small samples from the a population of values that have been generated using a random number generator. The code will calculate the t-value from the comparison of each of the 1000 set of samples and show the
                    distribution of t-values from this 1000 samples in a histogram. 
                    
                    **Exercise: Press button to extract generate a null distribution by taking 1000 sets of samples from the same population**
                    * How would you describe the shape of the distribution?  Where are most of the values?
                    * Estimate the mean of the distribution from these 1000 samples
                    * Roughly what % of values are have a t-value greater than 2?
                    * Press the button a few times does the distribution change, by a little or by a lot?
                 ''')                            

button2=html.Button('Go!',
                    id='button2',
                    n_clicks=0)
                      
output2=html.Div(id = 'output5',
                children = [],
                )

card2=dbc.Card([dbc.CardBody([text2,button2])],
    color="light",  
    inverse=False,   
    outline=False,
    )

body2 = dbc.Row([dbc.Col(card2,xs=12,md=12,lg=12)])

slider1=dcc.Slider(
        id='ex4_mean1',
        min=100,
        max=105,
        step=1,
        value=100,
        marks={100:'100',105:'105'},
    )

slider2=dcc.Slider(
        id='ex4_mean2',
        min=100,
        max=105,
        step=1,
        value=100,
        marks={100:'100',105:'105'},
    )

text3=dcc.Markdown('''
                    ##### Comparing an observed value to a null distribution #####
                    As said previously, statisticians have calculated mathematical proofs for generating null distributions and don't rely on the kinds of simulated null dsitributions you have been creating.  
                    These distributions are referred to as the normal distribution, t-distribution and f-distribution depending on the particular statistical test used. The exact shape of these distributions depends on the number of participants (the degrees of freedom). 
                    &nbsp 
                    
                    When you move the slider below you can generate data drawn from the same or different means. The t-value
                    for the test of the difference between the samples is shown as a line on the t-distribution (the mathematically derived null distribution). 
                    If the t-value is very extreme in the tails of the distribution - it is unlikely that the samples are from the same distrbution - e.g. there is a significant difference between the samples.
                    
                    **Exercise: Move the sliders to change the mean of the distributions from which the two samples are taken**
                    * What happens to the p-value when the observed value is in the tails of the t-distribution?
                    * What happens when the observed value is around the centre of the distribution?
                    
                 ''')   

text4=dcc.Markdown('''
                    
                    **Change the mean value for group 1**
                 ''')
                 
text5=dcc.Markdown('''
                    **Change the mean value for group 2**
                 ''')

card3=dbc.Card([dbc.CardBody([text3,text4,slider1,text5,slider2])],
    color="light",  
    inverse=False,   
    outline=False,
    )

body3 = dbc.Row([dbc.Col(card3,xs=12,md=12,lg=12)])

#specify outputs from dynamic functions
output3=html.Div(id = 'output6',
                children = [],
                )

def sig_app():
    layout = html.Div([
        nav,
        lesson,
        body1,
        output1,
        body2,
        output2,
        body3,
        output3
    ])
    
    return layout

def build_bargraph_ex4(clicks):
    
    fig1=go.Figure()
    textOut1=[]
    if clicks > 0:
        dist=[]
       
        data1=np.round(np.random.normal(100,10,100))
        data2=np.round(np.random.normal(100,10,100))
        result=sc.ttest_ind(data1,data2)
        dist.append(result[0])
         
        mult=sc.t.ppf((1 + 0.95)/2,len(data1)-1)
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            name='Control',
            x=['Group 1', 'Group 2'], y=[np.mean(data1), np.mean(data2)],
            error_y=dict(type='data', array=[sc.sem(data1)*mult,sc.sem(data2)*mult])
            ))
        fig1.update_layout(title_text='Means of the two samples')
        
        textOut1='Difference in means = ' + str(round(np.mean(data1)-np.mean(data2),3)) + ' - t-value = ' + str(round(result[0],3)) + ' - p-value = ' + str(round(result[1],3))
        
    graph1 = dcc.Graph(figure = fig1)
    
    return graph1, textOut1      

def build_hist_ex4(clicks):
    
    #fig1=go.Figure()
    fig2=go.Figure()
    
    if clicks > 0:
        dist=[]
        for i in range(0,1000):
            data1=np.round(np.random.normal(100,10,100))
            data2=np.round(np.random.normal(100,10,100))
            result=sc.ttest_ind(data1,data2)
            dist.append(result[0])
        
        
        fig2.add_trace(go.Histogram(x=dist))
        fig2.update_xaxes(range=[-5,5])
        fig2.update_yaxes(range=[0,150])
        fig2.update_layout(title_text='T-values from 1000 samples')
        
    graph2 = dcc.Graph(figure = fig2)
    
    return graph2        

def build_expHyp_ex4(ex4_mean1,ex4_mean2):
   
    data1=np.round(np.random.normal(ex4_mean1,10,100))
    data2=np.round(np.random.normal(ex4_mean2,10,100))
    
    ref_result=sc.ttest_ind(data1,data2)
            
    mult=sc.t.ppf((1 + 0.95)/2,len(data1)-1)
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
    name='Control',
    x=['Group 1', 'Group 2'], y=[np.mean(data1), np.mean(data2)],
    error_y=dict(type='data', array=[sc.sem(data1)*mult,sc.sem(data2)*mult])
    ))
    fig3.update_layout(title_text='Samples from different populations')
    graph3 = dcc.Graph(figure = fig3)
    
    dist=[]
    
    for i in range(0,1000):
            data1=np.round(np.random.normal(100,10,100))
            data2=np.round(np.random.normal(100,10,100))
            result=sc.ttest_ind(data1,data2)
            dist.append(result[0])
    
    fig4 = go.Figure()
    x_t=np.linspace(sc.t.ppf(0.0033,98),sc.t.ppf(0.9967,98),100)
        
    fig4.add_trace(go.Scatter(x=x_t,y=sc.t.pdf(x_t,98)))
    fig4.update_layout(title_text='T-Distribution')        
    fig4.add_shape(type='line',x0=ref_result[0],y0=0,x1=ref_result[0],y1=0.5,line={'dash': 'dash'})
   
    graph4=dcc.Graph(figure = fig4)
    textOut2='Difference in means: ' + str(np.round(np.mean(ex4_mean1)-np.mean(ex4_mean2),3)) + ' - T-Value: ' + str(np.round(ref_result[0],3)) + ' - P-Value: ' + str(np.round(ref_result[1],3))

    return graph3, graph4, textOut2