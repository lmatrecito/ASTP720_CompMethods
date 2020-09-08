# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:12:42 2020

@author: lizam
"""

# Homework 1 Problem 1 - Write a library (i.e. a separate file that you 
# can call) for the three root-finding algorithms we discussed in class
 

# 1. Bisection Method

def Bisection(a, b, f, t = .00001):
    x0 = a                                      # First point typically chosen
    x1 = b                                              # Second point choseen
    c = (x0+x1)/2             # Midpoint fomula, used for the Bisection Method
    y0 = f(x0)
    y1 = f(x1)
    y2 = f(c)
    i = 1
    while ((c-x1)/(x1)) > t or ((c-x1)/(x1)) < -t:   # Threshold for both ends
        if y2 * y0 < 0:    # Allows reasonable stop for getting into threshold
            x0 = x0
            x1 = c
            c = (x0+x1)/2 
            y0 = f(x0)
            y1 = f(x1)
            y2 = f(c)
            i = i + 1
        else:      # If above is not met, this allows for succesful completion
            x0 = x0
            x1 = c
            c = (x0+x1)/2 
            y0 = f(x0)
            y1 = f(x1)
            y2 = f(c)
            i = i + 1      
    return(c, i)


# 2. Newton Method

def f(x, xn):
    return((1+x**2)**(-1/2) - (1/2))
def df(x, xn):
    return(-x/((1+x**2)**(3/2)))

def Newton(xn, t = .00001):
    x1 = xn - f(xn)/(df(xn))                        # Formula for Netwon Method
    i = 1
    while (x1-xn)/xn > t or (x1-xn)/xn < -t:        # Again, setting threshold
        xn = x1
        x1 = xn - f(xn)/df(xn)
        i = i + 1
    return (x1, i)


# 3. Secant Method    

def Secant(x0, x1, t = .00001):
    a = x0
    b = x1
    y0 = f(a)
    y1 = f(b)
    xn = b - (float(b-a)/(y1-y0)) * y1
    y2 = f(xn)
    i = 1
    while ((xn-b)/b) > t or ((xn-b)/b) < -t:
        if y2 * y1 < 0:
            a = b
            b = xn
            y0 = f(a)
            y1 = f(b)
            xn = b - (float(b-a)/(y1-y0)) * y1
            y2 = f(xn)
            i = i + 1
        else:
            a = b
            b = xn
            y0 = f(a)
            y1 = f(b)
            xn = b - (float(b-a)/(y1-y0)) * y1
            y2 = f(xn)
            i = i + 1
        return(xn, i)
 
    
        
                


