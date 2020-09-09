# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 01:32:28 2020

@author: lizam
"""

# Homework 1 Problem 6 - Lens density: Use interpolator to plot values
# of N_e(x) halfway in between all x-values


#import pandas as pd
from ASTP720_HW1_P5 import interpolation
import matplotlib.pyplot as plt

#cols_list = ["x", "Ne"]
#lens = pd.read_csv('lens_density.csv', usecols=cols_list)
#x = lens["x"]        
#Ne = lens["Ne"]         

#x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#xn = [.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5]
#Ne = [0,0,.001,.008,.030,.065,.103,.130,.140,.132,.113,.089,.066,.046,.030,.019,.012,.007,.004,.002,.001]
yn = []

for i in range(len(xn)):
    d = interpolation(x[i+1], Ne[i+1], x[i], Ne[i])
    yn.append(d(xn[i]))
    print(yn)

plt.plot(x, Ne)
    

