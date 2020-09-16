# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:14:54 2020

@author: lizam
"""


# Homework 2 Problem 2 - Using chosen parameters, numerically determine
# mass enclosed (and plot), total mass of dark matter halo M, mass
# profile and its derivative

import math as m

# Chosen parameters converted to cgs
c = 12                                    # Dimensionless concentration factor 
v200 = 200 * 10**5                        # Velocity at the radius r200 (cm/s)
r200 = 30 * 10**21                                        # Virial radius (cm)
G = 6.6743 * 10**(-8)                    # Gravitational constant (cm^3/g/s^2)

# Mass Enclosed, Menc(r) and Plotting
rs = r200/c                                            # Characteristic radius
x = r/r200
a = (c*x)/(1 + c*x)   # Splitting circular velocity equation to make it easier
b = c / (1+c)
vc = v200 * m.sqrt((1/x) * ((m.log(1 + c*x) - a) / (m.log(1 + c) - b)))
Menc = (r * vc**2) / G                                         # Mass enclosed

# Total Mass of Dark Matter Halo, M
Mdh = (1 / ((x*c) * (1 + (x*c))**2)) * ((4*m.pi*(r**3)) / 3)
# Mass Profile - Amount of Mass in Shell, M(r)

# dM(r)/dr