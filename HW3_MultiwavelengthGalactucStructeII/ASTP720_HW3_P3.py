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
    fnODEs = len(yinit)                                        # Number of ODEs
    fsub_int = int((x_range[-1] - x_range[0]) / h)    # Number of sub-intervals
    fx = x_range[0]                                   # Initializes variables x
    fy = yinit                                        # Initializes variables y
    # Creates arrays for solutions
    fxsol = [fx]
    fysol = [fy[0]]
    for i in range(fsub_int):
        fyp = feval(func, fx, fy)                               # Evaluates dy/dx
        for j in range(fnODEs):
            fy[j] = fy[j] + h*fyp[j] 
        fx += h                                          # Increases the x-step
        fxsol.append(fx)         
        for r in range(len(fy)):
            fysol.append(fy[r])             
    return([fxsol, fysol])
# Testing out Forward Euler
# Setting parameters first, easier this way
fh = 0.001
fx = [0.0, 2.0]
fyinitef = [4.0]
[tsef, ysef] = forwardE('myfunc', fyinitef, fx, fh)



# Backward Euler's Method
# Defining a vector and multiplying by a scalar
def mult(vector, scalar):
    newv = [0]*len(vector)
    for i in range(len(vector)):
        newv[i] = vector[i]*scalar
    return(newv)
# Backward Euler's
def backwardE(func, yinit, x_range, h):
    bnODEs = len(yinit)
    bsub_int = int((x_range[-1] - x_range[0]) / h)
    bx = x_range[0]
    by = yinit
    bxsol = [bx]
    bysol = [by[0]]
    for i in range(bsub_int):
        bypr = feval(func, bx+h, by)
        byp = mult(bypr, (1 / (1+h)))
        for j in range(bnODEs):
            by[j] = by[j] + h*byp[j]
        bx += h
        bxsol.append(bx)
        for r in range(len(by)):
            bysol.append(by[r])  # Saves all new y's
    return([bxsol, bysol])
# Testing out Backward Euler
bh = 0.001
bx = [0.0, 2.0]
byiniteb = [4.0]
[tseb, yseb] = backwardE('myfunc', byiniteb, bx, bh)



# Heun's Method
def Heuns(func, yinit, x_range, h):
    hnODEs = len(yinit)
    hsub_int = int((x_range[-1] - x_range[0])/h)
    hx = x_range[0]
    hy = yinit
    hxsol = [hx]
    hysol = [hy[0]]
    for i in range(hsub_int):
        hy0p = feval(func, hx, hy)
        hk1 = mult(hy0p, h)
        hypred = [u + v for u, v in zip(hy, hk1)]
        hy1p = feval(func, hx+h, hypred)
        for j in range(hnODEs):
            hy[j] = hy[j] + (h/2)*hy0p[j] + (h/2)*hy1p[j]
        hx = hx + h
        hxsol.append(hx)
        for r in range(len(hy)):
            hysol.append(hy[r])
    return([hxsol, hysol])
# Testing out Heun's
hh = 0.001
hx = [0.0, 2.0]
hyinith = [4.0]
[tsh, ysh] = Heuns('myfunc', hyinith, hx, hh)
    


# RK4 Method
def RK4(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0]) / h)
    rx = x_range[0]
    ry = yinit
    rxsol = np.empty(0)
    rxsol = np.append(rxsol, rx)
    rysol = np.empty(0)
    rysol = np.append(rysol, ry)
    # Settng up RK4
    for i in range(n):
        # First RK4 Step
        k1 = feval(func, rx, ry)
        yp2 = ry + k1 * (h/2)
        # Second RK4 Step
        k2 = feval(func, (rx+h)/2, yp2)
        yp3 = ry + k2 * (h/2)
        # Third RK4 Step
        k3 = feval(func, (rx+h)/2, yp3)
        yp4 = ry + k3 * h
        # Fourth RK4 Step
        k4 = feval(func, rx+h, yp4)
        for j in range(m):
            # RK4 Formula
            ry[j] = ry[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) 
        # Defining an x to later use in function
        rx = rx + h
        rxsol = np.append(rxsol, rx)
        # Corresponding y
        for r in range(len(ry)):
            rysol = np.append(rysol, ry[r])
            rsol = [rxsol, rysol]
    return(rsol)
# Testing out RK4
# Setting parameters
rh = 0.001
rx = np.array([0.0, 2.0])
ryinitr = np.array([1.0/10])
[tsr, ysr] = RK4('myfunc', ryinitr, rx, rh)
# print([ts, ys])



# Plotting to compare
plt.plot(tsef, ysef, c='k', label='Forward Eulers')
plt.plot(tseb, yseb, c='m', label='Backward Eulers')
plt.plot(tsr, ysr, c='r', label='RK4')
plt.plot(tsh, ysh, c='orange', label='Heuns')
# Exact Solution
dt = int((rx[-1]-rx[0])/rh)
t = [rx[0]+i*rh for i in range(dt+1)] 
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