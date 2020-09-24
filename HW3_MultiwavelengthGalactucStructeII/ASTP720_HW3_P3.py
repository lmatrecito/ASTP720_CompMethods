# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:11:02 2020

@author: lizam
"""


# Homework 3 Problem 3 - ODE package that includes Euler's method, 
# Heun's method, and the explicit RK4 method


# Defining a function to use with the following methods
def f(x):
    return x**2

# Forward Euler's Method
def forwardE(f, x):
    h = 0.001
    df = (f(x+h) - f(x)) / (h)
    return(df)
# Backward Euler's Method
def backwardE(f, x):
    h = 0.001
    df = (f(x) - f(x-h)) / (h)
    return(df)
# Checking to see if the functions work
# dff = forwardE(f, 1)
# dfb = backwardE(f, 1)
# print("Forward Euler's =", dff)
# print("Backward Euler's =", dfb)


# Heun's Method

# RK4 Method