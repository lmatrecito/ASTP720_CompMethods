# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:08:57 2020

@author: lizam
"""


# Homework 3 Problem 2 - Calculate the different number densities as a
# function of temperature T. Make a plot showing the different number 
# densities vary as a function of T

import numpy as np
import astropy.units as un


def read_coefficients(filename="A_coefficients.dat"):
    # unpack the text file
    l, u, As = np.loadtxt(filename, unpack=True, delimiter=",",
                          dtype={"names": ('l', 'u', 'A_ul'),
                                 "formats": (np.int, np.int, np.float)})
    # Apply units of inverse seconds
    As /= un.s
    # Create the dictionary to return
    Adict = dict()
    for i in range(len(l)):
        Adict[(l[i], u[i])] = As[i]
    return(Adict)
# Checking to see if above works
# p = read_coefficients()
# print(p)