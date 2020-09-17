# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:17:12 2020

@author: lizam
"""


# Homework 2 Problem 3 - Write a matrix library that includes a Matrix
# class


# Creating a Matrix Class
class Matrix:
    def _init_(self, dims, fill):
        self.rows = dims[0]
        self.cols = dims[1]
        self.A = [[fill] * self.cols for i in range(self.rows)]