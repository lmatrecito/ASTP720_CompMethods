# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:58:17 2020

@author: lizam
"""


# Homework 2 Problem 1 - Write a library that can perform at least one
# derivative and at three integration functions i.e. midpoint rule, 
# trapezoidal rule, and Simpson's rule


# Derivative
def f(x):
    return x**2

def derivative(func, xval):
    h = 0.000001
    df = (func(xval + h) - func(xval)) / (h)
    return(df)

p = derivative(f, 2)
print(p)
# Midpoint Rule 

# Trapezoidal Rule

# Simpson's Rule