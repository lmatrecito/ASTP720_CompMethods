# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:14:54 2020

@author: lizam
"""


# Homework 2 Problem 2 - Using chosen parameters, numerically determine
# mass enclosed (and plot), total mass of dark matter halo M, mass
# profile and its derivative

# These are the values initially given in the HW
# rs = characteristic radius 
cg = 15           # Dimensionless concentration factor, higher c gives lower rs 
v200 = 160                   # Value of the velocity at the radius r200 (km/s)
r200 = 25                                 # Virial radius, equal to rs*c (kpc)

# Values I chose & converting into cgs units
c = 15
v200 = 160
# Mass Enclosed, Menc(r) and Plotting
Mencl = (r * vc**2) / G

# Total Mass of Dark Matter Halo, M

# Mass Profile - Amount of Mass in Shell, M(r)

# dM(r)/dr