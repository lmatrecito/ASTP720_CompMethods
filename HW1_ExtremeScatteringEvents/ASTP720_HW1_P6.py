# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 01:32:28 2020

@author: lizam
"""

# Homework 1 Problem 6 - Lens density: Use interpolator to plot values
# of N_e(x) halfway in between all x-values


from ASTP720_HW1_P5 import interpolation
import matplotlib.pyplot as plt
import pandas as pd

# Extracting data from lens density file
cols_list = ["x", "Ne"]                 # Changed the header to make it easier
lens = pd.read_csv('lens_density.csv', usecols=cols_list)
x = lens["x"]        
Ne = lens["Ne"]         

# Creating new x and Ne values
xhalf = x + 0.5                                    # Creating halfway x-values
xn = xhalf[:-1]         # Excluding that extra value, 20.5, that is not needed
Nen = []

# Using interpolator to get new Ne values
for i in range(len(xn)):
    d = interpolation(x[i+1], Ne[i+1], x[i], Ne[i])
    Nen.append(d(xn[i]))

# Setting Plot Specifics
plt.scatter(x, Ne, marker='.', c='r', label='Given Data Points')
plt.plot(xn, Nen, c='k',  label='Interpolated Set')
plt.legend()
plt.title('Lens Number Density Stuff')
plt.xlabel('x')
plt.ylabel('$N_{e}$(x)')
    

