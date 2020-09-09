# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 01:31:31 2020

@author: lizam
"""

# Homework 1 Problem 5 - Write lib. for piecewise linear interpolation
# given a set of x and y data points


def interpolation(x0, y0, x1, y1):
    s = (y1-y0) / (x1-x0) 
    def f(x):
        return ((s*(x-x0)) + y0)
    return f