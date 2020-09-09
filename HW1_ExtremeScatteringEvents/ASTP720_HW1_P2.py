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
    return (x**2-3)

 
l = []
m = []
n = []
t = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]
for j in range (7):
    a, i = Bisection(0.001, 3, f, t[j])
    l.append(i)
    xn, i = Newton(1.5, t[j])
    m.append(i)
    x0, i = Secant(0, 3, t[j])
    n.append(i)
    
plt.plot(t, l)
plt.plot(t, m)
plt.plot(t, n)