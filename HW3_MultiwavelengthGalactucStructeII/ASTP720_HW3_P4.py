# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:11:24 2020

@author: lizam
"""


# Homework 3 Problem 4 - Test 3 ODE Functions against the damped 
# pendulum example in scipy's odeint() documentation.



import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from ASTP720_HW3_P3 import forwardE, backwardE, Heuns, RK4 

# Scipy system for a pendulum
def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return(dydt)
b = 0.25
c = 5.0
y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 101)
sol = odeint(pend, y0, t, args=(b, c))           # ode solver from scipy
# Plot Stuff
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

# My ODE solvers
[tE, yE] = forwardE('pend', y0, t, (b,c))
plt.plot(tE, yE[:0], 'k', label='Forward Eulers')
