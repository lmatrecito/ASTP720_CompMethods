# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 01:21:27 2020

@author: lizam
"""

# Homework 1 Problem 4 - Repeat Prob. 3, but for the pseudo-isothermal
# sphere with the same parameters (except r_c = 1 AU)

import math as m
from ASTP720_HW1_P1 import Bisection
import matplotlib.pyplot as plt

# Just copying data from previous problem onto here
# Given values
r = 1                               # radius of observer's circular orbit (AU) 
P = 1                            # period of observer's circular orbit (years)
D = 1                                                 # diameter of lens (kpc)
a = 1                                                    # radius of lens (AU)
l = 21                                               # wavelength of lens (cm)
N0 = 0.01                                          # density of lens (pc/cm^3)

# Converting units to cm (with a little help from google)
r = 1.496e13
P = m.pi * 10**7                                                   # (seconds)
D = 3.0856e21
a = 1.496e13
N0 = 3.0856e16                                                        # (cm^2)
re = 2.83e-13 

# Solving for each value of x'
xps = 1 + (((l**2)*re*N0*D)/(m.pi*a**2))                # Splitting up x' eqn.