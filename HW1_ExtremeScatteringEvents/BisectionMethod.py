# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:12:42 2020

@author: lizam
"""

# Homework 1 Problem 1 - Write a library (i.e. a separate file that you 
# can call) for the three root-finding algorithms we discussed in class
 

# 1. Bisection Method

def Bisection(x0, x1, f, t=.00001):
    a = x0                                      # First point typically chosen
    b = x1                                              # Second point choseen
    c = (a+b)/2               # Midpoint fomula, used for the Bisection Method
    y0 = f(a)
    y1 = f(b)
    y2 = f(c)
    i = 1
    while ((c-b)/(b)) > t or ((c-b)/(b)) < -t:       # Threshold for both ends
        if y2 * y0 < 0:    # Allows reasonable stop for getting into threshold
            a = a
            b = c
            c = (a+b)/2 
            y0 = f(a)
            y1 = f(b)
            y2 = f(c)
            i = i + 1
        else:      # If above is not met, this allows for succesful completion
            a = c
            b = b
            c = (a+b)/2
            y0 = f(a)
            y1 = f(b)
            y2 = f(c)
            i = i + 1      
    return(c, i)
    


    


