# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:18:56 2020

@author: lizam
"""

# Homework 1 Problem 2 - Pseudo-isothermal sphere, calculate full width
# at half maximum in terms of r_c


from ASTP720_HW1_P1 import Bisection
from ASTP720_HW1_P1 import Newton
from ASTP720_HW1_P1 import Secant
import matplotlib.pyplot as plt

def f(x):
   return(x**2)
def df(x):
   return(2*x)
    
# Empty arrays help with plotting (setting all matrices equal)
l = []
m = []
n = []
t = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]

# Running functions and adding value to empty arrays created prior
for j in range (7):
    a, i = Bisection(0.0001, 3, f, t[j])               # Could not start at 0?
    l.append(i)
    xn, i = Newton(1.5, t[j])
    m.append(i)
    x0, i = Secant(0.0001, 3, t[j])      # Same as above, could not start at 0
    n.append(i)

# Setting Plot Specifics  
plt.plot(t, l, c='r', label='Bisection Method')
plt.plot(t, m, c='k', label='Newton Method')
plt.plot(t, n, c='b', label='Secant Method')
plt.legend()
plt.xlabel('Threshold')
plt.ylabel('Iterations Method Takes')
plt.title('Convergence')