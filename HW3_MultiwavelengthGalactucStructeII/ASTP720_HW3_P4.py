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
    b = 0.25
    c = 5.0
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return(dydt)
b = 0.25
c = 5.0
y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 101)
sol = odeint(pend, y0, t, args=(b, c))           # ode solver from scipy
# Plot Stuff
plt.plot(t, sol[:, 0], 'b', label='T(t)')
plt.plot(t, sol[:, 1], 'g', label='O(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('sol')
plt.grid()
plt.show()

# My ODE solvers
# [tF, yF] = forwardE('pend', y0, t)
# plt.plot(t, yF[:,0], 'k', label='Forward Eulers - Theta')
# plt.plot(t, yF[:,1], 'k', label='Forward Eulers - Omega')
# [tB, yB] = backwardE('pend', y0, t)
# plt.plot(t, yB[:,0], 'b', label='Backward Eulers - Theta')
# plt.plot(t, yB[:,1], 'b', label='Backward EUlers - Omega')
# [tH, yH] = Heuns('pend', y0, t)
# plt.plot(t, yH[:,0], 'g', label='Heuns - Theta')
# plt.plot(t, yH[:,1], 'g', label='Heuns - Omega')
# [tR, yR] = RK4('pend', y0, t, .001)
# plt.plot(t, yR[:,0], 'r', label='RK4 - Theta')
# plt.plot(t, yR[:,0], 'r', label='RK4 - Omega')