# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:14:54 2020

@author: lizam
"""


# Homework 2 Problem 2 - Using chosen parameters, numerically determine
# mass enclosed (and plot), total mass of dark matter halo M, mass
# profile and its derivative

import math as m
import matplotlib.pyplot as plt

# Chosen parameters converted to cgs
c = 12                                    # Dimensionless concentration factor 
v200 = 200 * 10**5                        # Velocity at the radius r200 (cm/s)
r200 = 30 * 10**21                                        # Virial radius (cm)
G = 6.6743 * 10**(-8)                    # Gravitational constant (cm^3/g/s^2)

# Finding and Plotting Menc(r), Mass of DM Halo, M(r), M(r)/dr
r = 20 * 10**21
v = 350 * 10**5                                           
rad = []
Mr = []
v2 = []
Md = []
for i in range (30):
    x = r/r200
    a = (c*x)/(1 + c*x)   # Splitting circular velocity equation to make it easier
    b = c / (1+c)
    vc = v200 * m.sqrt((1/x) * ((m.log(1 + c*x) - a) / (m.log(1 + c) - b)))
    Menc = (r * vc**2) / G                                         # Mass enclosed
    Mdh = (1 / ((x*c) * (1 + (x*c))**2)) * ((4*m.pi*(r**3)) / 3)
    rad.append(r)
    Mr.append(Menc)
    v2.append(vc)
    Md.append(Mdh)
    r = r + r   # Without this, my code gave me the same number for the radius


#plt.plot(rad, Mr)
#plt.plot(rad, Md)
plt.plot(r, Mr)
plt.xscale('log')
plt.yscale('log')

