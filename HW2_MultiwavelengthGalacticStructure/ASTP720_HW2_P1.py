# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:58:17 2020

@author: lizam
"""


# Homework 2 Problem 1 - Write a library that can perform at least one
# derivative & at least three integration functions i.e. midpoint rule, 
# trapezoidal rule, and Simpson's rule


def f(x):
    return x**2                    # Can choose any function, this one is easy


# Library that performs at least one derivative
def der(f, x):       
    h = 0.000001           
    df = (f(x + h) - f(x)) / (h)                # Definition of the derivative
    return(df)


# Three Integration Functions
# 1. Midpoint Rule 

# 2. Trapezoidal Rule
def trap(g, a, b, n):
    h = float(b - a) / n    # the higher the n, the better the convergence
    integ = 0.0
    integ += h * g(a)
    for i in range(1, n):
        integ += h * g(a + i*h)
    integ += h * g(b)
    return(integ)

# 3. Simpson's Rule
