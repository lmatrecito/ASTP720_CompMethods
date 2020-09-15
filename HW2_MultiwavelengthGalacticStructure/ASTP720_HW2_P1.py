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
    df = (f(x+h) - f(x)) / (h)                # Definition of the derivative
    return(df)
#n = der(f, 2)
#print(n)

# Three Integration Functions
# 1. Midpoint Rule 

# 2. Trapezoidal Rule
def trap(f, a, b, n):
    h = (b-a) / n    # the higher the n, the better the convergence
    ig = 0
    ig += h * f(a)
    for i in range(1, n):
        ig += h * f(a + i*h)
    ig += h * f(b)
    return(ig)
#p = trap(f, 0, 1, 1000)
#print(p)

# 3. Simpson's Rule
def simp(f, a, b, n):
    h = (b-a) / n
    k = 0
    x = a + h
    for i in range(1, n//2 + 1):    
        k += 4*f(x)
        x += 2*h
        
    x = a + 2*h
    for i in range(1, n//2):
        k += 2*f(x)
        x += 2*h
    return((h/3) * (f(a) + f(b) + k))
#p = simp(f, 0, 1, 1000)
#print(p)

