#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:16:42 2021

@author: sam
"""

import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Sum of Squares", href="/sd")),
        dbc.NavItem(dbc.NavLink("T-Tests", href="/ttest")),
        dbc.NavItem(dbc.NavLink("Data visualisation", href="/dataVis")),
        dbc.NavItem(dbc.NavLink("Significance Testing", href="/sig")),
        dbc.NavItem(dbc.NavLink("Author", href="https://www.samuel-evans.co.uk/about.html")),
    ],
    brand="Sunday Morning Stats: Lesson 1",
    brand_href="/",
    color="primary",
    dark=True,
    )
     
    return navbar