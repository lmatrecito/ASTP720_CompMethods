# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:11:02 2020

@author: lizam
"""


# Homework 3 Problem 3 - ODE package that includes Euler's method, 
# Heun's method, and the explicit RK4 method

import numpy as np
import matplotlib.pyplot as plt

# Defining a function to use for the following ODE package
def myfunc(x, y):
    dy = np.zeros((len(y)))
    dy[0] = np.exp(-2*x) - 2*y[0]
    return(dy)
# Function module used to evaluate equations
def feval(funcName, *args):
    return(eval(funcName)(*args))


# Euler's Methods:
# Forward Euler's Method
def forwardE(func, yinit, x_range, h):
    nODEs = len(yinit)                                        # Number of ODEs
    sub_int = int((x_range[-1] - x_range[0]) / h)    # Number of sub-intervals
    x = x_range[0]                                   # Initializes variables x
    y = yinit                                        # Initializes variables y
    # Creates arrays for solutions
    xsol = [x]
    ysol = [y[0]]
    for i in range(sub_int):
        yp = feval(func, x, y)                               # Evaluates dy/dx
        for j in range(nODEs):
            y[j] = y[j] + h*yp[j] 
        x += h                                          # Increases the x-step
        xsol.append(x)         
        for r in range(len(y)):
            ysol.append(y[r])             
    return([xsol, ysol])
# Testing out Forward Euler
# Setting parameters first, easier this way
h = 0.001
x = [0.0, 2.0]
yinitef = [4.0]
[tsef, ysef] = forwardE('myfunc', yinitef, x, h)


# Backward Euler's Method
# Defining a vector and multiplying by a scalar
def mult(vector, scalar):
    newv = [0]*len(vector)
    for i in range(len(vector)):
        newv[i] = vector[i]*scalar
    return(newv)
# Backward Euler's
def backwardE(func, yinit, x_range, h):
    nODEs = len(yinit)
    sub_intervals = int((x_range[-1] - x_range[0]) / h)
    x = x_range[0]
    y = yinit
    xsol = [x]
    ysol = [y[0]]
    for i in range(sub_intervals):
        ypr = feval(func, x+h, y)
        yp = mult(ypr, (1/(1+h)))
        for j in range(nODEs):
            y[j] = y[j] + h*yp[j]
        x += h
        xsol.append(x)
        for r in range(len(y)):
            ysol.append(y[r])  # Saves all new y's
    return([xsol, ysol])
# Testing out Backward Euler
h = 0.001
x = [0.0, 2.0]
yiniteb = [4.0]
[tseb, yseb] = backwardE('myfunc', yiniteb, x, h)
# Checking to see if the classes work
# dff = forwardE(f, 1)
# dfb = backwardE(f, 1)
# print("Forward Euler's =", dff)
# print("Backward Euler's =", dfb)


# Heun's Method
   
    
# RK4 Method
def RK4(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0]) / h)
    x = x_range[0]
    y = yinit
    xsol = np.empty(0)
    xsol = np.append(xsol, x)
    ysol = np.empty(0)
    ysol = np.append(ysol, y)
    # Settng up RK4
    for i in range(n):
        # First RK4 Step
        k1 = feval(func, x, y)
        yp2 = y + k1 * (h/2)
        # Second RK4 Step
        k2 = feval(func, (x+h)/2, yp2)
        yp3 = y + k2 * (h/2)
        # Third RK4 Step
        k3 = feval(func, (x+h)/2, yp3)
        yp4 = y + k3 * h
        # Fourth RK4 Step
        k4 = feval(func, x+h, yp4)
        for j in range(m):
            # RK4 Formula
            y[j] = y[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) 
        # Defining an x to later use in function
        x = x + h
        xsol = np.append(xsol, x)
        # Corresponding y
        for r in range(len(y)):
            ysol = np.append(ysol, y[r])
            sol = [xsol, ysol]
    return(sol)
# Testing out RK4
# Setting parameters
h = 0.001
x = np.array([0.0, 2.0])
yinitr = np.array([1.0/10])
[tsr, ysr] = RK4('myfunc', yinitr, x, h)
# print([ts, ys])



# Plotting to compare
plt.plot(tsef, ysef, c='k', label='Forward Eulers')
plt.plot(tseb, yseb, c='m', label='Backward Eulers')
plt.plot(tsr, ysr, c='r', label='RK4')
# Exact Solution
dt = int((x[-1]-x[0])/h)
t = [x[0]+i*h for i in range(dt+1)] 
yexact = []
for i in range(dt+1):
    ye = (1.0/10)*np.exp(-2*t[i]) + t[i]*np.exp(-2*t[i])
    yexact.append(ye)
plt.plot(t, yexact, 'b', label='Exact Solution')

# Plot Specifics
plt.ylim(0, .5)
plt.xlim(0, 2)
plt.legend()
plt.title('ODE Methods')